[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateFromRebarShape Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new shape driven Rebar, as an instance of a RebarShape. The instance will have the default shape parameters from the RebarShape, and its location is based on the bounding box of the shape in the shape definition. Hooks are removed from the shape before computing its bounding box. If appropriate hooks can be found in the document, they will be assigned arbitrarily.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public static Rebar CreateFromRebarShape( 	Document doc, 	RebarShape rebarShape, 	RebarBarType barType, 	Element host, 	XYZ origin, 	XYZ xVec, 	XYZ yVec ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateFromRebarShape ( _ 	doc As Document, _ 	rebarShape As RebarShape, _ 	barType As RebarBarType, _ 	host As Element, _ 	origin As XYZ, _ 	xVec As XYZ, _ 	yVec As XYZ _ ) As Rebar ``` |

 

| Visual C++ |
| --- |
| ``` public: static Rebar^ CreateFromRebarShape( 	Document^ doc,  	RebarShape^ rebarShape,  	RebarBarType^ barType,  	Element^ host,  	XYZ^ origin,  	XYZ^ xVec,  	XYZ^ yVec ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     A document.

rebarShape
:   Type:  [Autodesk.Revit.DB.Structure RebarShape](0a370e32-eaba-785e-7e1f-9330929525fc.htm)    
     A RebarShape element that defines the shape of the rebar.

barType
:   Type:  [Autodesk.Revit.DB.Structure RebarBarType](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)    
     A RebarBarType element that defines bar diameter, bend radius and material of the rebar.

host
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element to which the rebar belongs. The element must support rebar hosting;  [!:Autodesk::Revit::DB::Structure::RebarHostData]  .

origin
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The lower-left corner of the shape's bounding box will be placed at this point in the project.

xVec
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The x-axis in the shape definition will be mapped to this direction in the project.

yVec
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The y-axis in the shape definition will be mapped to this direction in the project.

#### Return Value

The newly created Rebar instance, or    a null reference (  Nothing  in Visual Basic)  if the operation fails.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Create 2 adjacent rebars with the given RebarShape and RebarBarType
private List<Rebar> CreateRebar(Document doc, Wall wall, RebarShape barShape, RebarBarType barType)
{
    List<Rebar> newRebars = new List<Rebar>();

    Rebar bar = Rebar.CreateFromRebarShape(doc, barShape, barType, wall, new XYZ(2, 0, 2), new XYZ(1, 0, 0), new XYZ(0, 0, 1));
    // call regenerate so that the TotalLength will be calculated before the transaction is committed
    doc.Regenerate();
    newRebars.Add(bar);

    // add a second bar adjacent to the first one
    double barLength = bar.TotalLength;
    bar = Rebar.CreateFromRebarShape(doc, barShape, barType, wall, new XYZ(2 + barLength, 0, 2), new XYZ(1, 0, 0), new XYZ(0, 0, 1));
    newRebars.Add(bar);

    return newRebars;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Create 2 adjacent rebars with the given RebarShape and RebarBarType
Private Function CreateRebar(doc As Document, wall As Wall, barShape As RebarShape, barType As RebarBarType) As List(Of Rebar)
    Dim newRebars As New List(Of Rebar)()

    Dim bar As Rebar = Rebar.CreateFromRebarShape(doc, barShape, barType, wall, New XYZ(2, 0, 2), New XYZ(1, 0, 0), _
        New XYZ(0, 0, 1))
    ' call regenerate so that the TotalLength will be calculated before the transaction is committed
    doc.Regenerate()
    newRebars.Add(bar)

    ' add a second bar adjacent to the first one
    Dim barLength As Double = bar.TotalLength
    bar = Rebar.CreateFromRebarShape(doc, barShape, barType, wall, New XYZ(2 + barLength, 0, 2), New XYZ(1, 0, 0), _
        New XYZ(0, 0, 1))
    newRebars.Add(bar)

    Return newRebars
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element host was not found in the given document. -or- host is not a valid rebar host. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | xVec has zero length. -or- yVec has zero length. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)