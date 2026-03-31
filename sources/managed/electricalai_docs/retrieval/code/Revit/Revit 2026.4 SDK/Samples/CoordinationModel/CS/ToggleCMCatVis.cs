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
using System.Windows.Forms;
using Autodesk.Revit.DB;
using Autodesk.Revit.DB.ExternalData;
using Autodesk.Revit.UI;
using Autodesk.Revit.UI.Selection;
using Revit.SDK.Samples.CoordinationModels.CS;
using View = Autodesk.Revit.DB.View;

namespace Revit.SDK.Samples.CoordinationModel.ToggleCMCatVis.CS
{
   /// <summary>
   ///   This command sets the visibility of one or more coordination model type categories.
   ///   
   ///   To run this sample, 
   ///   (1) Open a model with at least one coordination model linked.
   ///   (2) Run the command. 
   ///       It will prompt the user to select a coordination model instance, present a list of categories inside 
   ///       the corresponding coordination model type, then switch on/off the visibility of the selected categories.
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
         View view = activeDoc.ActiveView;

         try
         {
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
                     // obtain the categories of the coordination model type
                     CoordinationModelLinkData data = CoordinationModelLinkUtils.GetCoordinationModelTypeData(doc, cmType);
                     if (data != null && data.GetPathType() == CoordinationModelLinkPathType.Cloud)
                     {
                        IList<string> allCategories = data.GetCategoryNames();
                        if (allCategories != null && allCategories.Count > 0)
                        {
                           // prompt the user to select one or more categories
                           CategoriesForm categoriesForm = new CategoriesForm(allCategories);
                           if (categoriesForm.ShowDialog() == DialogResult.OK)
                           {
                              using (Transaction trans = new Transaction(doc, "Toggle Coordination Model Category Visibility"))
                              {
                                 trans.Start();

                                 foreach (string cat in categoriesForm.SelectedCategories)
                                 {
                                    // toggle the visibility of the coordination model category
                                    bool isVisible = CoordinationModelLinkUtils.GetVisibilityOverrideForCategory(doc, view, cmType, cat);
                                    CoordinationModelLinkUtils.SetVisibilityOverrideForCategory(doc, view, cmType, cat, !isVisible);
                                 }

                                 trans.Commit();
                              }
                           }
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
