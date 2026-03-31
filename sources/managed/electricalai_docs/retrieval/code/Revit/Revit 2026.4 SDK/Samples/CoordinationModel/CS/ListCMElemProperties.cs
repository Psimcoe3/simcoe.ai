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
using System.Linq;
using System.Windows.Forms;
using Autodesk.Revit.DB;
using Autodesk.Revit.DB.ExternalData;
using Autodesk.Revit.UI;
using Autodesk.Revit.UI.Selection;
using Revit.SDK.Samples.CoordinationModels.CS;
using View = Autodesk.Revit.DB.View;

namespace Revit.SDK.Samples.CoordinationModel.ListCMElemProperties.CS
{
   /// <summary>
   ///   This command gets the properties of an element inside a coordination model instance and writes them in a .txt file.
   ///   
   ///   To run this sample, 
   ///   (1) Open a model with at least one cloud coordination model linked.
   ///   (2) Run the command. 
   ///       It will prompt the user to select an element inside a coordination model to drop its properties
   ///       into a .txt file saved near the Revit file or in current user's temporary folder.
   /// </summary>
   [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
   [Autodesk.Revit.Attributes.Regeneration(Autodesk.Revit.Attributes.RegenerationOption.Manual)]
   [Autodesk.Revit.Attributes.Journaling(Autodesk.Revit.Attributes.JournalingMode.NoCommandData)]
   public class Command : IExternalCommand
   {
      static int index = 0;

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
            // prompt the user to select a coordination model element
            Reference cmInstanceRef = activeDoc.Selection.PickObject(ObjectType.Subelement, "Select an element inside a Coordination Model.");
            // obtain the coordination model instance
            Element cmInstance = doc.GetElement(cmInstanceRef);
            if (cmInstance != null && CoordinationModelLinkUtils.IsCoordinationModelInstance(doc, cmInstance))
            {              
               // obtain the coordination model type
               ElementType cmType = doc.GetElement(cmInstance.GetTypeId()) as ElementType;
               if (cmType != null)
               {                  
                  CoordinationModelLinkData data = CoordinationModelLinkUtils.GetCoordinationModelTypeData(doc, cmType);
                  if (data != null && data.GetPathType() == CoordinationModelLinkPathType.Cloud)
                  {
                     IList<CoordinationModelElementProperty> cmElementProperties = CoordinationModelLinkUtils.GetAllPropertiesForReferenceInsideCoordinationModel(doc, cmInstance, cmInstanceRef);
                     if (null != cmElementProperties && cmElementProperties.Any())
                     {
                        Dictionary<string, List<CoordinationModelElementProperty>> mapPropertyGroup2Properties = new Dictionary<string, List<CoordinationModelElementProperty>>();
                        foreach (var elementProperty in cmElementProperties)
                        {
                           string propertyGroup = elementProperty.Group;
                           if (null != propertyGroup)
                           {
                              List<CoordinationModelElementProperty> groupProperties;
                              if (!mapPropertyGroup2Properties.TryGetValue(propertyGroup, out groupProperties))
                                 groupProperties = new List<CoordinationModelElementProperty>();

                              groupProperties.Add(elementProperty);
                              mapPropertyGroup2Properties[propertyGroup] = groupProperties;
                           }
                        }

                        string propertiesPerGroupStr = "";
                        foreach (var propertyGroupProperties in mapPropertyGroup2Properties)
                        {
                           string groupName = propertyGroupProperties.Key;
                           propertiesPerGroupStr += groupName + " : " + "\n";
                           foreach (var groupProperty in propertyGroupProperties.Value)
                           {
                              string propertyName = groupProperty.Name;
                              string propertyValue = groupProperty.Value;
                              propertiesPerGroupStr += propertyName + " = " + propertyValue + "\n";
                           }
                           propertiesPerGroupStr += "\n";
                        }

                        // export grouped properties to a .txt file near the Revit doc file or in temp folder.
                        if (propertiesPerGroupStr.Length > 0)
                        {
                           string docPath = null != doc ? doc.PathName : string.Empty;
                           if (!string.IsNullOrEmpty(docPath))
                           {
                              docPath = Path.GetDirectoryName(docPath);
                           }
                           else
                           {
                              // temporary path
                              docPath = Path.Combine(Path.GetTempPath(), "CoordinationModelProperties");
                              if (!Directory.Exists(docPath))
                              {
                                 Directory.CreateDirectory(docPath);
                              }                                    
                           }
                           int elemIndex = ++index;
                           string fileName = elemIndex.ToString() + "_CMElementProperties.txt";
                           string filePath = Path.Combine(docPath, fileName);

                           if (!File.Exists(filePath))
                           {
                              File.Create(filePath).Dispose();

                              using (TextWriter tw = new StreamWriter(filePath))
                              {
                                 tw.WriteLine(propertiesPerGroupStr);
                              }
                           }
                           else
                           {
                              using (TextWriter tw = new StreamWriter(filePath, false /*append*/))
                              {
                                 tw.WriteLine(propertiesPerGroupStr);
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
