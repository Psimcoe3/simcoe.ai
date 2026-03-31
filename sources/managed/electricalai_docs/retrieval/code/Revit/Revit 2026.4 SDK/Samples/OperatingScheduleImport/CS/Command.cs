//
// (C) Copyright 2003-2024 by Autodesk, Inc.
//
// Permission to use, copy, modify, and distribute this software in
// object code form for any purpose and without fee is hereby granted,
// provided that the above copyright notice appears in all copies and
// that both that copyright notice and the limited warranty and
// restricted rights notice below appear in all supporting
// documentation.
//
// AUTODESK PROVIDES THIS PROGRAM "AS IS" AND WITH ALL FAULTS.
// AUTODESK SPECIFICALLY DISCLAIMS ANY IMPLIED WARRANTY OF
// MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. AUTODESK, INC.
// DOES NOT WARRANT THAT THE OPERATION OF THE PROGRAM WILL BE
// UNINTERRUPTED OR ERROR FREE.
//
// Use, duplication, or disclosure by the U.S. Government is subject to
// restrictions set forth in FAR 52.227-19 (Commercial Computer
// Software - Restricted Rights) and DFAR 252.227-7013(c)(1)(ii)
// (Rights in Technical Data and Computer Software), as applicable.
//

using System;
using System.Collections.Generic;

using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System.IO;
using System.Linq;
using Autodesk.Revit.DB.Analysis;
using System.Globalization;
using System.Security;


namespace Revit.SDK.Samples.OperatingScheduleImport.CS
{
   /// <summary>
   /// A command that imports the operational schedule usage data from a file. 
   /// </summary>
   [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
   [Autodesk.Revit.Attributes.Regeneration(Autodesk.Revit.Attributes.RegenerationOption.Manual)]
   public class Command : IExternalCommand
   {
      /// <summary>
      /// An external command for Revit that imports the operational schedule usage data from a file. 
      /// </summary>
      /// <param name="commandData">An object that is passed to the external application 
      /// which contains data related to the command, 
      /// such as the application object and active view.</param>
      /// <param name="message">A message that can be set by the external application 
      /// which will be displayed if a failure or cancellation is returned by 
      /// the external command.</param>
      /// <param name="elements">A set of elements to which the external application 
      /// can add elements that are to be highlighted in case of failure or cancellation.</param>
      /// <returns>Return the status of the external command. 
      /// A result of Succeeded means that the API external method functioned as expected. 
      /// Cancelled can be used to signify that the user cancelled the external operation 
      /// at some point. Failure should be returned if the application is unable to proceed with 
      /// the operation.</returns>
      public virtual Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
      {
         try
         {
            Document document = commandData.Application.ActiveUIDocument.Document;

            // Read a file with a date timestamp and a usage value separated by a comma.
            // All dates are in the year 2023 (the year required by the API).
            // For example:
            //   12/18/2023 16:00,0.309338995
            // Means that on 12/18 at 2:00 the space is used 30.9338995%

            var lines = File.ReadAllLines("OperatingScheduleImport.csv").ToList();
            lines.RemoveAt(0); // Remove the header line.

            // Read in the values form the file format.
            var yearUsageData = new List<(DateTime, double)>();
            foreach (var line in lines)
            {
               if (line.Split(',') is [var dateString, var usageString]
                  && DateTime.ParseExact(dateString, "M/d/yyyy H:mm", CultureInfo.InvariantCulture) is DateTime dateTime
                  && dateTime.Year == 2023 // The year required by the API.
                  && double.Parse(usageString) is double usage
                  && 0.0 <= usage && usage <= 1.0 // The usage range required by the API.
               )
               {
                  yearUsageData.Add((dateTime, usage));
               }
               else
               {
                  message = $"Invalid file syntax at: {line}";
                  return Result.Failed;
               }
            }

            // Group usage by day of year (2/1/2023 = 32).
            var usageByDay = yearUsageData.GroupBy(items => items.Item1.DayOfYear).Select(items => (items.Key, items.ToList()));

            using var transaction = new Transaction(document, "import data");
            transaction.Start();

            // Some buildings will have days of inactivity.
            // To reduce the total number of day schedules that need to be created, first make a day schedule with no activity.
            // All days with no activity will use this same schedule.
            var offDaySchedule = BuildingOperatingDaySchedule.Create(document, $"ImportedDayOff");

            // Create the year schedule.
            // New YearSchedules require a default DaySchedule. Use the offDaySchedule as the default.
            var yearSchedule = BuildingOperatingYearSchedule.Create(document, offDaySchedule, "ImportedYear");

            // Create the day schedules.
            foreach (var (day, dayUsage) in usageByDay)
            {
               // To reduce clutter, only create day schedules that have usage.
               if (dayUsage.Any(items => items.Item2 > 0.0))
               {
                  var date = dayUsage.First().Item1;

                  var daySchedule = BuildingOperatingDaySchedule.Create(document, $"ImportedDay{day:000}");

                  foreach (var (hourDateTime, usage) in dayUsage)
                  {
                     daySchedule.SetValueForHour(hourDateTime.Hour, usage);
                  }
                  // The API requires the date be in Universal Time Coordinated.
                  yearSchedule.SetScheduleForDay(DateTime.SpecifyKind(date, DateTimeKind.Utc), daySchedule);
               }
            }

            // Set every occupancy schedule to the imported values.
            var hVACLoadTypeElems = new FilteredElementCollector(document).OfClass(typeof(HVACLoadType)).ToElements().ToList();
            foreach (var hVACLoadTypeElem in hVACLoadTypeElems)
            {
               hVACLoadTypeElem.get_Parameter(BuiltInParameter.SPACE_OCCUPANCY_SCHEDULE_PARAM).Set(yearSchedule.Id);
            }

            transaction.Commit();

            return Result.Succeeded;
         }
         catch (Exception ex) when (
            ex is System.IO.IOException || ex is UnauthorizedAccessException || ex is System.IO.FileNotFoundException || ex is NotSupportedException || ex is SecurityException ||
            ex is System.ArgumentException ||
            ex is FormatException || ex is OverflowException
         )
         {
            message = ex.Message;
            return Result.Failed;
         }
      }
   }
}

