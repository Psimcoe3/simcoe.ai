using Autodesk.Revit.DB.Structure;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ContextualAnalyticalModel
{
   /// <summary>
   /// Selects the analytical elements that are connected to an analytical node
   /// Implements the Revit add-in interface IExternalCommand
   /// </summary>
   [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
   [Autodesk.Revit.Attributes.Regeneration(Autodesk.Revit.Attributes.RegenerationOption.Manual)]
   class AnalyticalNodeConnectedElements : IExternalCommand
   {
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
      public virtual Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
      {
         try
         {
            UIDocument uiDoc = commandData.Application.ActiveUIDocument;
            Document document = uiDoc.Document;

            Reference refNode = uiDoc.Selection.PickObject(Autodesk.Revit.UI.Selection.ObjectType.Element, "Please select an Anlytical Node");
            if (refNode != null)
            {
               // Analytical nodes are ReferencePoints objects
               ReferencePoint analyticalNode = document.GetElement(refNode.ElementId) as ReferencePoint;
               if (analyticalNode == null)
                  return Result.Failed;

               // Get the AnalyticalToPhysicalAssociationManager to obtain the associated physical elements of analytical elements
               AnalyticalToPhysicalAssociationManager assocManager = AnalyticalToPhysicalAssociationManager.GetAnalyticalToPhysicalAssociationManager(document);

               if (assocManager == null)
                  return Result.Failed;

               // The hub contains information about the connected elements in the node
               Hub hub = document.GetElement(analyticalNode.GetHubId()) as Hub;
               if (hub == null)
                  return Result.Failed;

               HashSet<ElementId> analyticalIds = new HashSet<ElementId>();
               HashSet<ElementId> physicalIds = new HashSet<ElementId>();

               // 1. Obtain analytical elements that have this node as end node
               foreach (Connector connector in hub.GetHubConnectorManager().Connectors)
               {
                  // Get the analytical elements connected to the Hub
                  foreach (Connector analyticalElementConnector in connector.AllRefs)
                  {
                     // Check that is analytical element
                     if (analyticalElementConnector.Owner is AnalyticalElement)
                     {
                        analyticalIds.Add(analyticalElementConnector.Owner.Id);
                        physicalIds.UnionWith(assocManager.GetAssociatedElementIds(analyticalElementConnector.Owner.Id));
                     }
                  }
               }

               // 2. Obtain analytical elements that have this node as hosted node
               PointElementReference pointRef = analyticalNode.GetPointElementReference();
               if (pointRef != null)
               {
                  Reference elemRef = null;
                  if (pointRef is PointOnEdge)
                  {
                     elemRef = (pointRef as PointOnEdge).GetEdgeReference();
                  }
                  else if (pointRef is PointOnFace)
                  {
                     elemRef = (pointRef as PointOnFace).GetFaceReference();
                  }

                  if (elemRef != null && elemRef.ElementId != ElementId.InvalidElementId)
                  {
                     analyticalIds.Add(elemRef.ElementId);
                     physicalIds.UnionWith(assocManager.GetAssociatedElementIds(elemRef.ElementId));
                  }
               }

               Autodesk.Revit.UI.Selection.Selection selection = uiDoc.Selection;
               analyticalIds.Add(analyticalNode.Id);
               selection.SetElementIds(analyticalIds);
            }
         }
         catch (Exception ex)
         {
            message = ex.Message;
            return Result.Failed;
         }

         return Result.Succeeded;
      }
   }
}
