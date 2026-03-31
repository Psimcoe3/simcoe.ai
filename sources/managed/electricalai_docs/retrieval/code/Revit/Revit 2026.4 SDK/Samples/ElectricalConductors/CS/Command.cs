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

using Autodesk.Revit.DB;
using Autodesk.Revit.DB.Electrical;
using Autodesk.Revit.UI;
using System;
using System.Collections.Generic;
using System.Linq;
using TaskDialog = Autodesk.Revit.UI.TaskDialog;

namespace Revit.SDK.Samples.ElectricalConductors.CS
{
   /// <summary>
   /// Set conductor size on an electrical circuit.
   /// </summary>
   [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
   [Autodesk.Revit.Attributes.Regeneration(Autodesk.Revit.Attributes.RegenerationOption.Manual)]
   public class SetConductorSizeOnCircuit : IExternalCommand
   {
      #region IExternalCommand Members Implementation
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
      public Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
      {
         if (null == commandData)
         {
            throw new ArgumentNullException("commandData");
         }
         
         try
         {
            Document doc = commandData.Application.ActiveUIDocument.Document;
            if (null == doc)
            {
               TaskDialog.Show("Error", "Document is null.");
               return Result.Failed;
            }
            ElectricalSystem circuit = new FilteredElementCollector(doc).OfClass(typeof(ElectricalSystem)).FirstElement() as ElectricalSystem;
            if (null == circuit)
            {
               TaskDialog.Show("Error", "Can not find a valid electrical circuit");
               return Result.Failed;
            }

            // find the conductor size 12
            ElementId targetConductorSizeId = ConductorSize.GetConductorSizeIdByName(doc, "12");
            if (ElementId.InvalidElementId == targetConductorSizeId)
            {
               targetConductorSizeId = CreateConductorSize(doc);
               if (ElementId.InvalidElementId == targetConductorSizeId)
               {
                  TaskDialog.Show("Error", "Create conductor size failed.");
                  return Result.Failed;
               }
            }

            // find the first cable size that is using conductor size 12
            ElementId targetCableSizeId = FindFirstCableSize(doc, targetConductorSizeId);
            if (ElementId.InvalidElementId == targetCableSizeId)
            {
               targetCableSizeId = CreateCableSize(doc, targetConductorSizeId);
               if (ElementId.InvalidElementId == targetCableSizeId)
               {
                  TaskDialog.Show("Error", "Create cable size failed.");
                  return Result.Failed;
               }
            }

            // find the first cable type that is using the cable size
            ElementId targetCableTypeId = FindFirstCableType(doc, targetCableSizeId);
            if (ElementId.InvalidElementId == targetCableTypeId)
            {
               targetCableTypeId = CreateCableType(doc, targetCableSizeId);
               if (ElementId.InvalidElementId == targetCableTypeId)
               {
                  TaskDialog.Show("Error", "Create cable type failed.");
                  return Result.Failed;
               }
            }

            using (Transaction transaction = new Transaction(doc, "set conductor size to electrical circuit"))
            {
               transaction.Start();
               circuit.CableType = targetCableTypeId;
               // regeneration is necessary after setting CableType
               doc.Regenerate();
               circuit.CableSize = targetCableSizeId;
               transaction.Commit();
            }
            return Result.Succeeded;
         }
         catch (Exception ex) 
         {
            message = ex.Message;
            TaskDialog.Show("Error", message);
            return Result.Failed;
         }
      }
      #endregion IExternalCommand Members Implementation

      #region Class Implementations
      private ElementId CreateConductorSize(Document doc)
      {
         if (null == doc)
         {
            TaskDialog.Show("Error", "Document is null.");
            return ElementId.InvalidElementId;
         }
         try
         {
            using (Transaction transaction = new Transaction(doc, "create conductor size"))
            {
               transaction.Start();
               ConductorSize conductorSize12 = ConductorSize.Create(doc);
               conductorSize12.Name = "12";
               conductorSize12.Diameter = 0.0067341666666666678;
               transaction.Commit();

               return conductorSize12.Id;
            }
         }
         catch (Exception ex)
         {
            TaskDialog.Show("Error", ex.Message);
            return ElementId.InvalidElementId;
         }
      }

      private ElementId CreateCableSize(Document doc, ElementId conductorSizeId)
      {
         if (null == doc)
         {
            TaskDialog.Show("Error", "Document is null.");
            return ElementId.InvalidElementId;
         }
         try
         {
            using (Transaction transaction = new Transaction(doc, "create cable size"))
            {
               transaction.Start();
               CableSize cableSize = CableSize.Create(doc);
               cableSize.NumberOfHotConductors = 1;
               cableSize.NumberOfNeutralConductors = 1;
               cableSize.NumberOfGroundConductors = 1;
               cableSize.HotConductorSize = conductorSizeId;
               cableSize.NeutralConductorSize = conductorSizeId;
               cableSize.GroundConductorSize = conductorSizeId;
               transaction.Commit();

               return cableSize.Id;
            }
            
         }
         catch (Exception ex)
         {
            TaskDialog.Show("Error", ex.Message);
            return ElementId.InvalidElementId;
         }
      }

      private ElementId CreateCableType(Document doc, ElementId cableSizeId)
      {
         if (null == doc)
         {
            TaskDialog.Show("Error", "Document is null.");
            return ElementId.InvalidElementId;
         }
         try
         {
            using (Transaction transaction = new Transaction(doc, "create cable type"))
            {
               transaction.Start();
               CableType cableType = CableType.Create(doc);
               cableType.SetCableSizeUsable(cableSizeId, true);
               transaction.Commit();

               return cableType.Id;
            }
         }
         catch (Exception ex)
         {
            TaskDialog.Show("Error", ex.Message);
            return ElementId.InvalidElementId;
         }
      }

      private ElementId FindFirstCableSize(Document doc, ElementId usedConductorSizeId)
      {
         if(null == doc || ElementId.InvalidElementId == usedConductorSizeId) 
            return ElementId.InvalidElementId;

         IList<ElementId> cableSizeIds = CableSize.GetCableSizeIds(doc);
         foreach (ElementId cableSizeId in cableSizeIds)
         {
            CableSize cableSize = CableSize.GetCableSize(doc, cableSizeId);
            if (null == cableSize)
               continue;
            if (usedConductorSizeId == cableSize.HotConductorSize &&
               usedConductorSizeId == cableSize.NeutralConductorSize &&
               usedConductorSizeId == cableSize.GroundConductorSize)
            {
               return cableSizeId;
            }
         }
         return ElementId.InvalidElementId;
      }

      private ElementId FindFirstCableType(Document doc, ElementId usableCableSizeId)
      {
         if (null == doc || ElementId.InvalidElementId == usableCableSizeId)
            return ElementId.InvalidElementId;

         IList<ElementId> cableTypeIds = CableType.GetCableTypeIds(doc);
         foreach (ElementId cableTypeId in cableTypeIds)
         {
            CableType cableType = doc.GetElement(cableTypeId) as CableType;
            if (null == cableType)
               continue;
            if (cableType.IsCableSizeUsable(usableCableSizeId))
            {
               return cableTypeId;
            }
         }
         return ElementId.InvalidElementId;
      }
      #endregion
   }

   /// <summary>
   /// Remove cable size
   /// </summary>
   [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
   [Autodesk.Revit.Attributes.Regeneration(Autodesk.Revit.Attributes.RegenerationOption.Manual)]
   public class RemoveCableSize : IExternalCommand
   {
      #region IExternalCommand Members Implementation
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
      public Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
      {
         if (null == commandData)
         {
            throw new ArgumentNullException("commandData");
         }

         try
         {
            Document doc = commandData.Application.ActiveUIDocument.Document;
            if (null == doc)
            {
               TaskDialog.Show("Error", "Document is null.");
               return Result.Failed;
            }

            using (Transaction transaction = new Transaction(doc, "remove cable size"))
            {
               transaction.Start();
               ElementId cableSizeId = CableSize.GetCableSizeIds(doc).First();
               if (cableSizeId != null && cableSizeId != ElementId.InvalidElementId)
               {
                  doc.Delete(cableSizeId);
               }
               transaction.Commit();
            }
            return Result.Succeeded;
         }
         catch (Exception ex)
         {
            message = ex.Message;
            TaskDialog.Show("Error", message);
            return Result.Failed;
         }
      }
      #endregion IExternalCommand Members Implementation
   }

   /// <summary>
   /// Remove conductor size
   /// </summary>
   [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
   [Autodesk.Revit.Attributes.Regeneration(Autodesk.Revit.Attributes.RegenerationOption.Manual)]
   public class RemoveConductorSize : IExternalCommand
   {
      #region IExternalCommand Members Implementation
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
      public Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
      {
         if (null == commandData)
         {
            throw new ArgumentNullException("commandData");
         }

         try
         {
            Document doc = commandData.Application.ActiveUIDocument.Document;
            if (null == doc)
            {
               TaskDialog.Show("Error", "Document is null.");
               return Result.Failed;
            }

            using (Transaction transaction = new Transaction(doc, "remove conductor size"))
            {
               transaction.Start();
               ElementId conductorSizeId = ConductorSize.GetConductorSizeIdByName(doc, "12");
               if (conductorSizeId != ElementId.InvalidElementId)
                  doc.Delete(conductorSizeId);
               transaction.Commit();
            }
            return Result.Succeeded;
         }
         catch (Exception ex)
         {
            message = ex.Message;
            TaskDialog.Show("Error", message);
            return Result.Failed;
         }
      }
      #endregion IExternalCommand Members Implementation
   }
}

