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
using System.Linq;

using Autodesk.Revit.DB;
using Autodesk.Revit.DB.ExternalData;
using Autodesk.Revit.UI;
using Autodesk.Revit.UI.Selection;

namespace Revit.SDK.Samples.CoordinationModel.ReloadCM.CS
{
   /// <summary>
   ///   This command reloads one or more coordination models.
   ///   
   ///   To run this sample, 
   ///   (1) Open a model with at least one coordination model linked.
   ///   (2) Optionally, upload a new version of a cloud coordination model linked in the file that was opened.
   ///   (3) Run the command. 
   ///       It will prompt the user to select one or more coordination models and reload the latest version 
   ///       of the corresponding coordination model types.
   ///   (4) Optionally, verify that the newly uploaded version is now linked in the Revit model.
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
            // we use a HashSet here, since there can be multiple coordination model instances of the same type
            HashSet<Element> cmTypes = new HashSet<Element>();

            // prompt the user to select one or more coordination models to reload
            List<Reference> refs = activeDoc.Selection.PickObjects(ObjectType.Element, new CMSelectionFilter(), "Select coordination model(s) to reload").ToList();
            foreach (Reference reference in refs)
            {
               Element cmInstance = doc.GetElement(reference);
               if (cmInstance != null)
               {
                  // obtain the coordination model type (which will actually be reloaded and all its instances will reflect that)
                  ElementType cmType = doc.GetElement(cmInstance.GetTypeId()) as ElementType;
                  if (cmType != null)
                  {
                     cmTypes.Add(cmType);
                  }
               }
            }

            using (Transaction trans = new Transaction(doc, "Reload Coordination Model(s)"))
            {
               trans.Start();

               foreach (ElementType cmType in cmTypes)
               {
                  // reload the coordination model type
                  CoordinationModelLinkUtils.Reload(doc, cmType);
               }

               trans.Commit();
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
