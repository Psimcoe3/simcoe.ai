//
// (C) Copyright 2003-2019 by Autodesk, Inc.
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
using System.Text;

using Autodesk.Revit;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using Autodesk.Revit.ApplicationServices;
using System.Linq;
using System.Runtime;
using Autodesk.Revit.DB.Structure;

namespace Revit.SDK.Samples.HelloRevit.CS
{
   /// <summary>
   /// Demonstrate how a basic ExternalCommand can be added to the Revit user interface. 
   /// And demonstrate how to create a Revit style dialog.
   /// </summary>
   [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
   [Autodesk.Revit.Attributes.Regeneration(Autodesk.Revit.Attributes.RegenerationOption.Manual)]
   [Autodesk.Revit.Attributes.Journaling(Autodesk.Revit.Attributes.JournalingMode.NoCommandData)]
   public class TestCommand : IExternalCommand
   {
      #region IExternalCommand Members

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
      public Autodesk.Revit.UI.Result Execute(ExternalCommandData commandData,
          ref string message, Autodesk.Revit.DB.ElementSet elements)
      {
         UIApplication uiApp = commandData.Application;
         Document doc = uiApp.ActiveUIDocument.Document;

         try
         {
            Reference refer = uiApp.ActiveUIDocument.Selection.PickObject(Autodesk.Revit.UI.Selection.ObjectType.Element);
            AnalyticalElement analyticalElement = doc.GetElement(refer.ElementId) as AnalyticalElement;
            List<ElementId> ids = new List<ElementId>();
            if (analyticalElement != null)
            {
               ids = GetConnectedElements(doc, analyticalElement);
            }

            uiApp.ActiveUIDocument.Selection.SetElementIds(ids);

            return Result.Succeeded;
         }
         catch (Exception ex)
         {
            message = ex.Message;
            return Result.Failed;
         }
      }

      private static List<ElementId> GetConnectedElements(Document doc, AnalyticalElement analyticalElement)
      {
         List<ElementId> elementIds = new List<ElementId>();

         ConnectorManager connMan = analyticalElement.ConnectorManager;
         if (connMan == null)
            return elementIds;

         foreach (Connector mainConnector in connMan.Connectors)
         {
            ConnectorSet connectorSet = mainConnector.AllRefs;
            ConnectorSetIterator csi = connectorSet.ForwardIterator();

            while (csi.MoveNext())
            {
               Connector connector = csi.Current as Connector;

               Hub hub = doc.GetElement(connector.Owner.Id) as Hub;
               if (hub != null)
               {
                  ReferencePoint analyticalNode = doc.GetElement(hub.GetPointId()) as ReferencePoint;
                  if (analyticalNode == null)
                     continue;

                  PointElementReference pointRef = analyticalNode.GetPointElementReference();
                  if (pointRef != null) //hosted node - obtain host element
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
                        elementIds.Add(elemRef.ElementId);
                     }
                  }
                  else
                  {
                     //end node
                     elementIds.AddRange(GetElementsConnectedInHub(doc, hub, analyticalElement.Id));
                  }
               }
            }
         }

         //get hosted elements
         ElementClassFilter filter = new ElementClassFilter(typeof(ReferencePoint));
         foreach (var id in analyticalElement.GetDependentElements(filter))
         {
            ReferencePoint analyticalNode = doc.GetElement(id) as ReferencePoint;
            if (analyticalNode == null)
               continue;

            Hub hub = doc.GetElement(analyticalNode.GetHubId()) as Hub;
            if (hub == null)
               continue;

            elementIds.AddRange(GetElementsConnectedInHub(doc, hub, analyticalElement.Id));

         }
         return elementIds;
         #endregion
      }

      private static List<ElementId> GetElementsConnectedInHub(Document doc, Hub hub, ElementId ownerId)
      {
         List<ElementId> ids = new List<ElementId>();
         if (hub == null || doc == null)
            return ids;

         ConnectorManager connectorMgr = hub.GetHubConnectorManager();
         if (connectorMgr != null)
         {
            foreach (Connector conn in connectorMgr.Connectors)
            {
               ConnectorSet connectorSetConn = conn.AllRefs;
               ConnectorSetIterator csiConn = connectorSetConn.ForwardIterator();

               while (csiConn.MoveNext())
               {
                  Connector hubConn = csiConn.Current as Connector;
                  if (hubConn.Owner is AnalyticalElement && hubConn.Owner.Id != ownerId)
                  {
                     ids.Add(hubConn.Owner.Id);
                  }
               }
            }
         }

         return ids;
      }
   }
}
