[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new wire.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static Wire Create( 	Document document, 	ElementId wireTypeId, 	ElementId viewId, 	WiringType wiringType, 	IList<XYZ> vertexPoints, 	Connector startConnectorTo, 	Connector endConnectorTo ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	wireTypeId As ElementId, _ 	viewId As ElementId, _ 	wiringType As WiringType, _ 	vertexPoints As IList(Of XYZ), _ 	startConnectorTo As Connector, _ 	endConnectorTo As Connector _ ) As Wire ``` |

 

| Visual C++ |
| --- |
| ``` public: static Wire^ Create( 	Document^ document,  	ElementId^ wireTypeId,  	ElementId^ viewId,  	WiringType wiringType,  	IList<XYZ^>^ vertexPoints,  	Connector^ startConnectorTo,  	Connector^ endConnectorTo ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

wireTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the wire type of the newly created wire.

viewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The view in which the wire is to be visible. This must be the id of a floor plan or reflected ceiling plan view.

wiringType
:   Type:  [Autodesk.Revit.DB.Electrical WiringType](fb484864-f9d0-7335-1f91-d7ac587f15fb.htm)    
     Specifiies the wiring type for the newly created wire. The shape of the wire is determined by this value and the total number of points supplied via the vertexPoints and endpoint connectors. If the wiring type is WiringType.Arc:

    * If there are 2 total points supplied, the wire is a straight-line wire.
    * If there are 3 total points supplied, the wire is a circular arc wire.
    * If there are 4 or more points, the wire is a spline wire.

    If the wiring type is WiringType.Chamfer, a polyline wire will be created connecting all the points.

vertexPoints
:   Type:  System.Collections.Generic IList   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vertex point of the wire. If the startConnectorTo is    a null reference (  Nothing  in Visual Basic)  , the first vertex of the vertexPoints will be the start point, otherwise, the start connector origin will be the start point. If the endConnectorTo is    a null reference (  Nothing  in Visual Basic)  , the last vertex of the vertexPoints will be the end point, otherwise, the end connector origin will be the end point.

startConnectorTo
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The connector to which the wire start point connects. If    a null reference (  Nothing  in Visual Basic)  , the start point connects to no existing connector. If set with a connector, the connector's origin will be added to the wire's vertices as the start point.

endConnectorTo
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The connector to which the wire end point connects. If    a null reference (  Nothing  in Visual Basic)  , the end point connects to no existing connector. If set with a connector, the connector's origin will be added to the wire's vertices as the end point.

#### Return Value

The wire created.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Create an unconnected straight line wire between two points
public Wire CreateWire(Document document)
{
    Wire wire = null;

    FilteredElementCollector collector = new FilteredElementCollector(document);
    IList<Element> wireTypes = collector.OfCategory(BuiltInCategory.OST_Wire).WhereElementIsElementType().ToElements();
    WireType wireType = wireTypes.First() as WireType;

    if (wireType != null)
    {
        IList<XYZ> wireVertices = new List<XYZ>();
        wireVertices.Add(new XYZ(0, 0, 0));
        wireVertices.Add(new XYZ(2, 0, 0));

        wire = Wire.Create(document, wireType.Id, document.ActiveView.Id, WiringType.Arc, wireVertices, null, null);
    }

    return wire;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
  ' Create an unconnected straight line wire between two points
  Public Function CreateWire(document As Document) As Wire
   Dim wire__1 As Wire = Nothing

   Dim collector As New FilteredElementCollector(document)
   Dim wireTypes As IList(Of Element) = collector.OfCategory(BuiltInCategory.OST_Wire).WhereElementIsElementType().ToElements()
   Dim wireType As WireType = TryCast(wireTypes.First(), WireType)

   If wireType IsNot Nothing Then
      Dim wireVertices As IList(Of XYZ) = New List(Of XYZ)()
      wireVertices.Add(New XYZ(0, 0, 0))
      wireVertices.Add(New XYZ(2, 0, 0))

      wire__1 = Wire.Create(document, wireType.Id, document.ActiveView.Id, WiringType.Arc, wireVertices, Nothing, _
         Nothing)
   End If

   Return wire__1
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | wireTypeId is not a valid WireType id. -or- viewId does not represent a view valid for a Wire element. Either a floor plan or reflected ceiling plan is expected. -or- vertexPoints is not valid, because one or more points are coincident by comparing the X and Y of the points, or there are not at least two points including the connectors. -or- startConnectorTo cannot be connected to a wire, as it is not an electrical connector. -or- endConnectorTo cannot be connected to a wire, as it is not an electrical connector. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)