[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreatePipeConnector Method (Document, PipeSystemType, Reference)

---



|  |
| --- |
| [ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Create a new pipe ConnectorElement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ConnectorElement CreatePipeConnector( 	Document document, 	PipeSystemType pipeSystemType, 	Reference planarFace ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreatePipeConnector ( _ 	document As Document, _ 	pipeSystemType As PipeSystemType, _ 	planarFace As Reference _ ) As ConnectorElement ``` |

 

| Visual C++ |
| --- |
| ``` public: static ConnectorElement^ CreatePipeConnector( 	Document^ document,  	PipeSystemType pipeSystemType,  	Reference^ planarFace ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to add the connector to.

pipeSystemType
:   Type:  [Autodesk.Revit.DB.Plumbing PipeSystemType](24165d09-9267-54b7-3e32-6405d1343c2e.htm)    
     The PipeSystemType of the connector.

planarFace
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The planar face to place the connector on.

#### Return Value

The pipe ConnectorElement.

# Remarks

Regenerates the document.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void CreatePipeConnectors(UIDocument uiDocument, Extrusion extrusion)
{
    // get the faces of the extrusion
    Options geoOptions = uiDocument.Document.Application.Create.NewGeometryOptions();
    geoOptions.View = uiDocument.Document.ActiveView;
    geoOptions.ComputeReferences = true;

    List<PlanarFace> planarFaces = new List<PlanarFace>();
    Autodesk.Revit.DB.GeometryElement geoElement = extrusion.get_Geometry(geoOptions);
    foreach (GeometryObject geoObject in geoElement)
    {
        Solid geoSolid = geoObject as Solid;
        if (null != geoSolid)
        {
            foreach (Face geoFace in geoSolid.Faces)
            {
                if (geoFace is PlanarFace)
                {
                    planarFaces.Add(geoFace as PlanarFace);
                }
            }
        }
    }

    if (planarFaces.Count > 1)
    {
        // Create the Supply Hydronic pipe connector
        //PipeConnector connSupply = 
        //    uiDocument.Document.FamilyCreate.NewPipeConnector(planarFaces[0].Reference, 
        //                                           PipeSystemType.SupplyHydronic);
        ConnectorElement connSupply =
            ConnectorElement.CreatePipeConnector(uiDocument.Document, PipeSystemType.SupplyHydronic, planarFaces[0].Reference);
        Parameter param = connSupply.get_Parameter(BuiltInParameter.CONNECTOR_RADIUS);
        param.Set(1.0); // 1' radius
        param = connSupply.get_Parameter(BuiltInParameter.RBS_PIPE_FLOW_DIRECTION_PARAM);
        param.Set(2);

        // Create the Return Hydronic pipe connector
        //PipeConnector connReturn =
        //    uiDocument.Document.FamilyCreate.NewPipeConnector(planarFaces[1].Reference,
        //                                           PipeSystemType.ReturnHydronic);
        ConnectorElement connReturn =
            ConnectorElement.CreatePipeConnector(uiDocument.Document, PipeSystemType.ReturnHydronic, planarFaces[1].Reference);
        param = connReturn.get_Parameter(BuiltInParameter.CONNECTOR_RADIUS);
        param.Set(0.5); // 6" radius
        param = connReturn.get_Parameter(BuiltInParameter.RBS_PIPE_FLOW_DIRECTION_PARAM);
        param.Set(1);
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub CreatePipeConnectors(uiDocument As UIDocument, extrusion As Extrusion)
    ' get the faces of the extrusion
    Dim geoOptions As Options = uiDocument.Document.Application.Create.NewGeometryOptions()
    geoOptions.View = uiDocument.Document.ActiveView
    geoOptions.ComputeReferences = True

    Dim planarFaces As New List(Of PlanarFace)()
    Dim geoElement As Autodesk.Revit.DB.GeometryElement = extrusion.Geometry(geoOptions)
    For Each geoObject As GeometryObject In geoElement
        Dim geoSolid As Solid = TryCast(geoObject, Solid)
        If geoSolid IsNot Nothing Then
            For Each geoFace As Face In geoSolid.Faces
                If TypeOf geoFace Is PlanarFace Then
                    planarFaces.Add(TryCast(geoFace, PlanarFace))
                End If
            Next
        End If
    Next

    If planarFaces.Count > 1 Then
        ' Create the Supply Hydronic pipe connector
        'PipeConnector connSupply = 
        '    uiDocument.Document.FamilyCreate.NewPipeConnector(planarFaces[0].Reference, 
        '                                           PipeSystemType.SupplyHydronic);
        Dim connSupply As ConnectorElement = ConnectorElement.CreatePipeConnector(uiDocument.Document, PipeSystemType.SupplyHydronic, planarFaces(0).Reference)
        Dim param As Parameter = connSupply.Parameter(BuiltInParameter.CONNECTOR_RADIUS)
        param.[Set](1.0)
        ' 1' radius
        param = connSupply.Parameter(BuiltInParameter.RBS_PIPE_FLOW_DIRECTION_PARAM)
        param.[Set](2)

        ' Create the Return Hydronic pipe connector
        'PipeConnector connReturn =
        '    uiDocument.Document.FamilyCreate.NewPipeConnector(planarFaces[1].Reference,
        '                                           PipeSystemType.ReturnHydronic);
        Dim connReturn As ConnectorElement = ConnectorElement.CreatePipeConnector(uiDocument.Document, PipeSystemType.ReturnHydronic, planarFaces(1).Reference)
        param = connReturn.Parameter(BuiltInParameter.CONNECTOR_RADIUS)
        param.[Set](0.5)
        ' 6" radius
        param = connReturn.Parameter(BuiltInParameter.RBS_PIPE_FLOW_DIRECTION_PARAM)
        param.[Set](1)
    End If
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The reference is not a planar face. -or- document is not a family document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Connector creation is not allowed in this family. |

# See Also

[ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)

[CreatePipeConnector Overload](c6188202-bd11-204d-de6e-afa1c6799d50.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)