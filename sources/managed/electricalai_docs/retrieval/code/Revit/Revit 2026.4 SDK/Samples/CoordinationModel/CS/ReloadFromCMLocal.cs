//
// (C) Copyright 2003-2025 by Autodesk, Inc.
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
using System.IO;
using System.Reflection;
using System.Text.Json;

using Autodesk.Revit.DB;
using Autodesk.Revit.DB.ExternalData;
using Autodesk.Revit.UI;
using Autodesk.Revit.UI.Selection;
using Revit.SDK.Samples.CoordinationModels.CS;

namespace Revit.SDK.Samples.CoordinationModel.ReloadFromCMLocal.CS
{
   /// <summary>
   ///   This command reloads a local coordination model from another local Navisworks file with a path specified in CMSettings.json.
   ///   
   ///   To run this sample, 
   ///   (1) Open a model with at least one local coordination model linked.
   ///   (2) Specify the local nwc/nwd file to load from in CMSettings.json.
   ///   (3) Run the command. 
   ///       It will prompt the user to select a local coordination model instance to reload its type from the local nwc/nwd file path specified in CMSettings.json.     
   /// </summary>
   [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
   [Autodesk.Revit.Attributes.Regeneration(Autodesk.Revit.Attributes.RegenerationOption.Manual)]
   [Autodesk.Revit.Attributes.Journaling(Autodesk.Revit.Attributes.JournalingMode.NoCommandData)]
   public class Command : IExternalCommand
   {
      #region Interface implementation
      /// <summary>
      /// Implement this method as an external command for Revit.
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
      public Autodesk.Revit.UI.Result Execute(ExternalCommandData commandData, ref String message, Autodesk.Revit.DB.ElementSet elements)
      {
         UIDocument activeDoc = commandData.Application.ActiveUIDocument;
         Document doc = activeDoc.Document;

         try
         {
            CMConfig cmConfig = Config.ReadConfig();
            string filePath = cmConfig?.LocalFileCfg?.FilePath;

            // first let's try with a provided absolute path of the file.
            if (string.IsNullOrEmpty(filePath))
            {
               string fileNameInCurrentDirectory = cmConfig?.LocalFileCurrentDirectoryCfg?.FileName;
               // now let's try with a file found in current directory
               if (string.IsNullOrEmpty(fileNameInCurrentDirectory))
               {
                  message = "Error reading file path from CMSettings.json";
                  return Result.Failed;
               }
               else
               {
                  string assemblyLocation = Assembly.GetExecutingAssembly().Location;
                  Environment.CurrentDirectory = Path.GetDirectoryName(assemblyLocation);
                  filePath = Path.GetFullPath(fileNameInCurrentDirectory);
                  if (string.IsNullOrEmpty(filePath))
                  {
                     message = "Error reading file path from CMSettings.json";
                     return Result.Failed;
                  }
               }
            }

            // prompt the user to select a coordination model
            IList<Element> cmElement = activeDoc.Selection.PickElementsByRectangle(new CMSelectionFilter(), "Select a coordination model by rectangle.");
            if (cmElement.Count == 1)
            {
               Element cmInstance = cmElement[0];
               if (cmInstance != null)
               {
                  // obtain the coordination model type
                  ElementType cmType = doc.GetElement(cmInstance.GetTypeId()) as ElementType;
                  if (cmType != null)
                  {
                     CoordinationModelLinkData data = CoordinationModelLinkUtils.GetCoordinationModelTypeData(doc, cmType);
                     if (data != null && data.GetPathType() != CoordinationModelLinkPathType.Cloud)
                     {
                        using (Transaction trans = new Transaction(doc, "Reload Coordination Model view from local file"))
                        {
                           trans.Start();

                           // reload the local coordination model from the local file path specified in CMSettings.json
                           CoordinationModelLinkUtils.ReloadLocalCoordinationModelFrom(doc, cmType, filePath);

                           trans.Commit();
                        }
                     }
                  }
               }
            }
         }
         catch (Exception ex)
         {
            message = ex.ToString();
            return Result.Failed;
         }
         
         return Result.Succeeded;
      }
      #endregion
   }
}
