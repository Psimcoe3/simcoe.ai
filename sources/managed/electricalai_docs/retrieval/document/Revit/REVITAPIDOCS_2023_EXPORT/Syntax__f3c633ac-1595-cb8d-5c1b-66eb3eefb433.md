[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpotDimension Class

---



|  |
| --- |
| [Members](5d70c697-396a-cc67-2caf-5608f556a456.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Object representing various types of SpotDimension

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public class SpotDimension : Dimension ``` |

 

| Visual Basic |
| --- |
| ``` Public Class SpotDimension _ 	Inherits Dimension ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SpotDimension : public Dimension ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void Getinfo_SpotDimension(SpotDimension spotDimension)
{
    string message = "SpotDimension's Location : ";
    Location location = spotDimension.Location;

    if (location is LocationPoint)
    {
        LocationPoint point = location as LocationPoint;

        message += "\n" + location.GetType().Name + " : ";
        message += "(" + point.Point.X + ", " + point.Point.Y + ", " + point.Point.Z + ")";
    }
    else
    {
        LocationCurve locCurve = location as LocationCurve;
        Curve curve = locCurve.Curve;
        message += "\n" + location.GetType().Name + " : ";
        message += "\nStart Point : " + "(" + curve.GetEndPoint(0).X + ", "
                    + curve.GetEndPoint(0).Y + ", " + curve.GetEndPoint(0).Z + ")";
        message += "\nEnd point : " + "(" + curve.GetEndPoint(1).X + ", "
                    + curve.GetEndPoint(1).Y + ", " + curve.GetEndPoint(1).Z + ")";
    }

    TaskDialog.Show("Revit",message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub Getinfo_SpotDimension(spotDimension As SpotDimension)
    Dim message As String = "SpotDimension's Location : "
    Dim location As Location = spotDimension.Location

    If TypeOf location Is LocationPoint Then
        Dim point As LocationPoint = TryCast(location, LocationPoint)

        message += vbLf + location.[GetType]().Name & " : "
        message += (("(" + point.Point.X & ", ") + point.Point.Y & ", ") + point.Point.Z & ")"
    Else
        Dim locCurve As LocationCurve = TryCast(location, LocationCurve)
        Dim curve As Curve = locCurve.Curve
        message += vbLf + location.[GetType]().Name & " : "
        message += (((vbLf & "Start Point : " & "(") + curve.GetEndPoint(0).X & ", ") + curve.GetEndPoint(0).Y & ", ") + curve.GetEndPoint(0).Z & ")"
        message += (((vbLf & "End point : " & "(") + curve.GetEndPoint(1).X & ", ") + curve.GetEndPoint(1).Y & ", ") + curve.GetEndPoint(1).Z & ")"
    End If

    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB Dimension](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm)    
  Autodesk.Revit.DB SpotDimension

# See Also

[SpotDimension Members](5d70c697-396a-cc67-2caf-5608f556a456.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)