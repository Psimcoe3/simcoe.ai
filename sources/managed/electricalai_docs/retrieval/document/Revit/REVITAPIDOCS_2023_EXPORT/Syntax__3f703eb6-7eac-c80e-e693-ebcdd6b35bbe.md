[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointLoad Class

---



|  |
| --- |
| [Members](bc80259d-8acc-3f3b-ecb7-0997d38bd4d2.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

An object that represents a force/moment applied to a single point.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class PointLoad : LoadBase ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PointLoad _ 	Inherits LoadBase ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PointLoad : public LoadBase ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void Getinfo_PointLoad(PointLoad pointLoad)
{
    string message = "Point Load :";

    // Get the load case name
    message += "\nLoad case for load: " + pointLoad.LoadCaseName;

    //get the three dimensional force applied to the point load
    message += "\nForce: (" + pointLoad.ForceVector.X + ", " +
             pointLoad.ForceVector.Y + ", " + pointLoad.ForceVector.Z + ")";

    //get the three dimensional moment application to the point load
    message += "\nMoment: (" + pointLoad.MomentVector.X + ", " +
             pointLoad.MomentVector.Y + ", " + pointLoad.MomentVector.Z + ")";

    //get the three dimensional coordinates of point load
    message += "\nPoint load location: (" + pointLoad.Point.X + ", " +
             pointLoad.Point.Y + ", " + pointLoad.Point.Z + ")";

    TaskDialog.Show("Revit",message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub Getinfo_PointLoad(pointLoad As PointLoad)
    Dim message As String = "Point Load :"

    ' Get the load case name
    message += vbLf & "Load case for load: " & Convert.ToString(pointLoad.LoadCaseName)

    'get the three dimensional force applied to the point load
 message += vbLf & "Force: (" & Convert.ToString(pointLoad.ForceVector.X) & ", " & Convert.ToString(pointLoad.ForceVector.Y) & ", " & Convert.ToString(pointLoad.ForceVector.Z) & ")"

    'get the three dimensional moment application to the point load
 message += vbLf & "Moment: (" & Convert.ToString(pointLoad.MomentVector.X) & ", " & Convert.ToString(pointLoad.MomentVector.Y) & ", " & Convert.ToString(pointLoad.MomentVector.Z) & ")"

    'get the three dimensional coordinates of point load
    message += vbLf & "Point load location: (" & Convert.ToString(pointLoad.Point.X) & ", " & Convert.ToString(pointLoad.Point.Y) & ", " & Convert.ToString(pointLoad.Point.Z) & ")"

    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB.Structure LoadBase](4130f6dc-1963-2105-d85b-e08a7c34af8b.htm)    
  Autodesk.Revit.DB.Structure PointLoad

# See Also

[PointLoad Members](bc80259d-8acc-3f3b-ecb7-0997d38bd4d2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)