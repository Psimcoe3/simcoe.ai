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
using System.IO;
using System.Reflection;
using System.Text.Json;

using Autodesk.Revit.DB;
using Autodesk.Revit.DB.ExternalData;
using Autodesk.Revit.UI;

namespace Revit.SDK.Samples.CoordinationModel.LinkCMCloud.CS
{
   /// <summary>
   ///   This command links an Autodesk Docs model view with parameters specified in CMSettings.json as a coordination model.
   ///   
   ///   To run this sample, 
   ///   (1) Open a new or existing Revit model
   ///   (2) Specify the parameters corresponding to an Autodesk Docs model view to which you have access in CMSettings.json.
   ///   (3) Run the command. 
   ///       It will link an instance of the specified model view, positioned according to the Positioning option specified in CMSettings.json
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
            string accountId = cmConfig?.CloudFileCfg?.AccountId;
            string projectId = cmConfig?.CloudFileCfg?.ProjectId;
            string fileId = cmConfig?.CloudFileCfg?.FileId;
            string viewName = cmConfig?.CloudFileCfg?.ViewName;
            CoordinationModelLinkOptions linkOptions = new CoordinationModelLinkOptions();
            linkOptions.Positioning = cmConfig?.Positioning ?? CoordinationModelPositioning.OriginToInternalOrigin;

            if (string.IsNullOrEmpty(accountId) || string.IsNullOrEmpty(projectId) || string.IsNullOrEmpty(fileId) || string.IsNullOrEmpty(viewName))
            {
               message = "Error reading cloud model parameters from CMSettings.json";
               return Result.Failed;
            }

            using (Transaction trans = new Transaction(doc, "Insert Coordination Model view from cloud file"))
            {
               trans.Start();

               // link an instance of the model view and place it according to the specified Positioning option
               CoordinationModelLinkUtils.Link3DViewFromAutodeskDocs(doc, accountId, projectId, fileId, viewName, linkOptions);

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
