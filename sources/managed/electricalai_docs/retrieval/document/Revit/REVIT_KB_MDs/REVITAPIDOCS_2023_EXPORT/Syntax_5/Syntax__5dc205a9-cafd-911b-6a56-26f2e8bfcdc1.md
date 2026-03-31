[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreaLoad Class

---



|  |
| --- |
| [Members](09dbcdc8-e3b9-35d3-34aa-977e3119e3d8.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

An object that represents a force applied across an area.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class AreaLoad : LoadBase ``` |

 

| Visual Basic |
| --- |
| ``` Public Class AreaLoad _ 	Inherits LoadBase ``` |

 

| Visual C++ |
| --- |
| ``` public ref class AreaLoad : public LoadBase ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetInfo_AreaLoad(AreaLoad areaLoad)
{
    string message = "AreaLoad Force : ";
    // Get areaload force1 position
    message += "\nAreaLoad Force1 position :(" + areaLoad.ForceVector1.X + ", "
        + areaLoad.ForceVector1.Y + ", " + areaLoad.ForceVector1.Z + ")";
    // Get areaload force2 position
    message += "\nAreaLoad Force2 position :(" + areaLoad.ForceVector2.X + ", "
        + areaLoad.ForceVector2.Y + ", " + areaLoad.ForceVector2.Z + ")";
    // Get areaload force3 position
    message += "\nAreaLoad Force3 position :(" + areaLoad.ForceVector3.X + ", "
        + areaLoad.ForceVector3.Y + ", " + areaLoad.ForceVector3.Z + ")";

    // Get Loops
    int loopIndex = 0;
    foreach (CurveLoop curveLoop in areaLoad.GetLoops())
    {
       message += "\nLoop " + loopIndex + " consist of following points :";
       foreach (Curve curve in curveLoop)
       {
          message += " (" + curve.GetEndPoint(0).X + ", " + curve.GetEndPoint(0).Y + ", " + curve.GetEndPoint(0).Z + ")";
       }
       loopIndex++;
    }

    // Get ref points information
    for (int k = 0; k < areaLoad.NumRefPoints; k++)
    {
        // Get areaload Ref point
        message += "\nAreaLoad Ref point :(" + areaLoad.GetRefPoint(k).X + ", "
            + areaLoad.GetRefPoint(k).Y + ", " + areaLoad.GetRefPoint(k).Z + ")";
    }
    TaskDialog.Show("Revit",message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetInfo_AreaLoad(areaLoad As AreaLoad)
    Dim message As String = "AreaLoad Force : "
    ' Get areaload force1 position
 message += vbLf & "AreaLoad Force1 position :(" & Convert.ToString(areaLoad.ForceVector1.X) & ", " & Convert.ToString(areaLoad.ForceVector1.Y) & ", " & Convert.ToString(areaLoad.ForceVector1.Z) & ")"
    ' Get areaload force2 position
 message += vbLf & "AreaLoad Force2 position :(" & Convert.ToString(areaLoad.ForceVector2.X) & ", " & Convert.ToString(areaLoad.ForceVector2.Y) & ", " & Convert.ToString(areaLoad.ForceVector2.Z) & ")"
    ' Get areaload force3 position
 message += vbLf & "AreaLoad Force3 position :(" & Convert.ToString(areaLoad.ForceVector3.X) & ", " & Convert.ToString(areaLoad.ForceVector3.Y) & ", " & Convert.ToString(areaLoad.ForceVector3.Z) & ")"

    ' Get Loops
    Dim loopIndex As Integer = 0
    For Each curveLoop As CurveLoop In areaLoad.GetLoops()
        message += vbLf & "Loop " +  loopIndex + " consist of following points :"
        For Each curve As Autodesk.Revit.DB.Curve In curveLoop
            message += ((" (" + curve.GetEndPoint(0).X & ", ") + curve.GetEndPoint(0).Y & ", ") + curve.GetEndPoint(0).Z & ")"
        Next
         loopIndex =  loopIndex + 1
    Next

    ' Get ref points information
    For k As Integer = 0 To areaLoad.NumRefPoints - 1
        ' Get areaload Ref point
        message += ((vbLf & "AreaLoad Ref point :(" + areaLoad.GetRefPoint(k).X & ", ") + areaLoad.GetRefPoint(k).Y & ", ") + areaLoad.GetRefPoint(k).Z & ")"
    Next
    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB.Structure LoadBase](4130f6dc-1963-2105-d85b-e08a7c34af8b.htm)    
  Autodesk.Revit.DB.Structure AreaLoad

# See Also

[AreaLoad Members](09dbcdc8-e3b9-35d3-34aa-977e3119e3d8.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)