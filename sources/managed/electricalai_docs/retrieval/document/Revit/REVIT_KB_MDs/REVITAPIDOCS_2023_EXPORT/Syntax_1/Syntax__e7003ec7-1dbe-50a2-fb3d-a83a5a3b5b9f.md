[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReferencePlane Class

---



|  |
| --- |
| [Members](3d4b050d-6f7a-1d67-c3c5-0fce92d5b25d.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Represents a reference plane of Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class ReferencePlane : DatumPlane ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ReferencePlane _ 	Inherits DatumPlane ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ReferencePlane : public DatumPlane ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void Getinfo_ReferencePlane(ReferencePlane refPlane)
{
    string message = "Reference Plane: ";
    //get the bubble end of the reference plane
    XYZ bubbleEnd = refPlane.BubbleEnd;
    message += "\nBubble end: (" + bubbleEnd.X + ", "
                       + bubbleEnd.Y + ", " + bubbleEnd.Z + ")";

    //get the direction of the reference plane
    XYZ direction = refPlane.Direction;
    message += "\nDirection: (" + direction.X + ", "
                    + direction.Y + ", " + direction.Z + ")";

    //get the freeEnd of the reference plane
    XYZ freeEnd = refPlane.FreeEnd;
    message += "\nFree End: (" + freeEnd.X + ", "
                    + freeEnd.Y + ", " + freeEnd.Z + ")";

    //get the name of the reference plane
    message += "\nName: " + refPlane.Name;

    //get the normal vector of the reference plane
    XYZ normal = refPlane.Normal;
    message += "\nNormal vector: (" + normal.X + ", "
                    + normal.Y + ", " + normal.Z + ")";

    //get the geometry plane to which the reference plane assigned 
    Autodesk.Revit.DB.Plane plane = refPlane.GetPlane();
    message += "\norigin of the plane: (" + plane.Origin.X + ", "
                    + plane.Origin.Y + ", " + plane.Origin.Z + ")";

    message += "\nnormal of the plane: (" + plane.Normal.X + ", "
                    + plane.Normal.Y + ", " + plane.Normal.Z + ")";

    message += "\nXvec of the plane: (" + plane.XVec.X + ", "
                    + plane.XVec.Y + ", " + plane.XVec.Z + ")";

    message += "\nYvec of the plane: (" + plane.YVec.X + ", "
                    + plane.YVec.Y + ", " + plane.YVec.Z + ")";

    TaskDialog.Show("Revit",message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub Getinfo_ReferencePlane(refPlane As ReferencePlane)
    Dim message As String = "Reference Plane: "
    'get the bubble end of the reference plane
    Dim bubbleEnd As XYZ = refPlane.BubbleEnd
    message += ((vbLf & "Bubble end: (" + bubbleEnd.X & ", ") + bubbleEnd.Y & ", ") + bubbleEnd.Z & ")"

    'get the direction of the reference plane
    Dim direction As XYZ = refPlane.Direction
    message += ((vbLf & "Direction: (" + direction.X & ", ") + direction.Y & ", ") + direction.Z & ")"

    'get the freeEnd of the reference plane
    Dim freeEnd As XYZ = refPlane.FreeEnd
    message += ((vbLf & "Free End: (" + freeEnd.X & ", ") + freeEnd.Y & ", ") + freeEnd.Z & ")"

    'get the name of the reference plane
    message += vbLf & "Name: " & Convert.ToString(refPlane.Name)

    'get the normal vector of the reference plane
    Dim normal As XYZ = refPlane.Normal
    message += ((vbLf & "Normal vector: (" + normal.X & ", ") + normal.Y & ", ") + normal.Z & ")"

    'get the geometry plane to which the reference plane assigned 
 Dim plane As Autodesk.Revit.DB.Plane = refPlane.GetPlane()
    message += ((vbLf & "origin of the plane: (" + plane.Origin.X & ", ") + plane.Origin.Y & ", ") + plane.Origin.Z & ")"

    message += ((vbLf & "normal of the plane: (" + plane.Normal.X & ", ") + plane.Normal.Y & ", ") + plane.Normal.Z & ")"

    message += ((vbLf & "Xvec of the plane: (" + plane.XVec.X & ", ") + plane.XVec.Y & ", ") + plane.XVec.Z & ")"

    message += ((vbLf & "Yvec of the plane: (" + plane.YVec.X & ", ") + plane.YVec.Y & ", ") + plane.YVec.Z & ")"

    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB DatumPlane](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)    
  Autodesk.Revit.DB ReferencePlane

# See Also

[ReferencePlane Members](3d4b050d-6f7a-1d67-c3c5-0fce92d5b25d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)