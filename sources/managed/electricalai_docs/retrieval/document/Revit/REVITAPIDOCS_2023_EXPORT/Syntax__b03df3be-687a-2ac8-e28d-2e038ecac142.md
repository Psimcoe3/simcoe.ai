[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Curve Property

---



|  |
| --- |
| [LocationCurve Class](9dd6eb99-f105-a05f-dc1b-dfde17b8768c.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Provides the ability to get and set the curve of a curve based element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Curve Curve { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Curve As Curve 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Curve^ Curve { 	Curve^ get (); 	void set (Curve^ value); } ``` |

# Remarks

This property can be used to set the location of curve based element to any desired position. Many elements are curve based. Some examples are walls, beams and braces.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
void MoveUsingCurveParam(Autodesk.Revit.ApplicationServices.Application application, Wall wall)
{
    LocationCurve wallLine = wall.Location as LocationCurve;
    XYZ p1 = XYZ.Zero;
    XYZ p2 = new XYZ(10, 20, 0);
    Line newWallLine = Line.CreateBound(p1, p2);

    // Change the wall line to a new line.
    wallLine.Curve = newWallLine;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub MoveUsingCurveParam(application As Autodesk.Revit.ApplicationServices.Application, wall As Wall)
    Dim wallLine As LocationCurve = TryCast(wall.Location, LocationCurve)
    Dim p1 As XYZ = XYZ.Zero
    Dim p2 As New XYZ(10, 20, 0)
    Dim newWallLine As Line = Line.CreateBound(p1, p2)

    ' Change the wall line to a new line.
    wallLine.Curve = newWallLine
End Sub
```

# See Also

[LocationCurve Class](9dd6eb99-f105-a05f-dc1b-dfde17b8768c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)