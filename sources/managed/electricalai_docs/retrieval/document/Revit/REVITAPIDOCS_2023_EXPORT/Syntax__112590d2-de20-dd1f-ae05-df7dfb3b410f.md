[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetGeneratingElementIds Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Returns the ids of the element(s) that generated the input geometry object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> GetGeneratingElementIds( 	GeometryObject geometryObject ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetGeneratingElementIds ( _ 	geometryObject As GeometryObject _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ GetGeneratingElementIds( 	GeometryObject^ geometryObject ) ``` |

#### Parameters

geometryObject
:   Type:  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
     The geometry object whose generating element is requested.

#### Return Value

The id(s) of the element(s) that generated (or may have generated) the given geometry object. Empty if no generating elements are found. If the set contains just one id, it is the id of the element that generated the geometry object.

# Remarks

This function supports many different types of relationships among elements. Most of these relationships will return a single element, for example:

* Window and door cutting walls
* Openings cutting hosts
* Face splitting faces
* Wall sweep or reveal traversing wall

A few relationships have the potential for returning multiple elements, including:

* Walls joining to other wall(s)
* Elements extending to roof(s)

If more than one id is returned, one of them (unspecified) is the id of the element that generated the geometry object and the others are ids of related elements. For example, if a wall A is joined to two walls B and C in a way that creates two end faces, and if this function is called for one of the two end faces, it will return the ids of walls B and C.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Find elements joined or attached to the end faces of a given wall (such as walls and roofs).
// Mid-joined walls (such as in a T configuration) are not found because they do not affect end face geometry.

ICollection<ElementId> joinedElements = new Collection<ElementId>(); // collection to store the walls joined to the selected wall

// find all faces of the selected wall
GeometryElement geometryElement = wall.get_Geometry(new Options());
foreach (GeometryObject geometryObject in geometryElement)
{
    if (geometryObject is Solid)
    {
        Solid solid = geometryObject as Solid;
        foreach (Face face in solid.Faces)
        {
            // for each face, find the other elements that generated the geometry of that face
            ICollection<ElementId> generatingElementIds = wall.GetGeneratingElementIds(face);

            generatingElementIds.Remove(wall.Id); // remove the originally selected wall, leaving only other elements joined to it
            foreach (ElementId id in generatingElementIds)
            {
                if (!(joinedElements.Contains(id)))
                    joinedElements.Add(id); // add each wall joined to this face to the overall collection 
            }
        }
    }
}

uidocument.Selection.SetElementIds(joinedElements); // select all of the joined elements
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Find elements joined or attached to the end faces of a given wall (such as walls and roofs).
' Mid-joined walls (such as in a T configuration) are not found because they do not affect end face geometry.


Dim joinedElements As ICollection(Of ElementId) = New Collection(Of ElementId)()
' collection to store the walls joined to the selected wall
' find all faces of the selected wall
Dim geometryElement As GeometryElement = wall.Geometry(New Options())
For Each geometryObject As GeometryObject In geometryElement
    If TypeOf geometryObject Is Solid Then
        Dim solid As Solid = TryCast(geometryObject, Solid)
        For Each face As Face In solid.Faces
            ' for each face, find the other elements that generated the geometry of that face
            Dim generatingElementIds As ICollection(Of ElementId) = wall.GetGeneratingElementIds(face)

            generatingElementIds.Remove(wall.Id)
            ' remove the originally selected wall, leaving only other elements joined to it
            For Each id As ElementId In generatingElementIds
                If Not (joinedElements.Contains(id)) Then
                    joinedElements.Add(id)
                    ' add each wall joined to this face to the overall collection 
                End If
            Next
        Next
    End If
Next

uidocument.Selection.SetElementIds(joinedElements)
' select all of the joined elements
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input geometryObject is invalid and so cannot be used to obtain the generating element ids. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)