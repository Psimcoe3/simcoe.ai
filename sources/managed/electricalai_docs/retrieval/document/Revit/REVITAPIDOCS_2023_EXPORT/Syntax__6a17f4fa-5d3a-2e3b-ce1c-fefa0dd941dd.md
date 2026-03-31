[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCurveElementIds Method

---



|  |
| --- |
| [PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Retrieves the set of ElementIds of curves forming the boundary of the Path Reinforcement.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> GetCurveElementIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCurveElementIds As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ GetCurveElementIds() ``` |

#### Return Value

A collection of ElementIds of ModelCurve elements.

# Remarks

Each ElementId in the collection is an Id of an Element of type ModelCurve.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void Getinfo_PathReinforcementCurve(PathReinforcement pathReinforcement)
{
    string message = "Path Reinforcement Curves : ";

    // Get path reinforcement curves by iterating the Curves property
    IList<ElementId> curveIds = pathReinforcement.GetCurveElementIds();
    foreach (Autodesk.Revit.DB.ElementId ii in curveIds)
    {
        ModelCurve pathReinforcementCurve = doc.GetElement(ii) as ModelCurve;
        if (null == pathReinforcementCurve)
        {
            continue;
        }

        Autodesk.Revit.DB.Curve curve = pathReinforcementCurve.GeometryCurve;

        // Get curve start point
        message += "\nCurve start point:(" + curve.GetEndPoint(0).X + ", "
            + curve.GetEndPoint(0).Y + ", " + curve.GetEndPoint(0).Z + ")";
        // Get curve end point
        message += "; Curve end point:(" + curve.GetEndPoint(1).X + ", "
            + curve.GetEndPoint(1).Y + ", " + curve.GetEndPoint(1).Z + ")";


    }
    TaskDialog.Show("Revit", message);

}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub Getinfo_PathReinforcementCurve(pathReinforcement As PathReinforcement)
    Dim message As String = "Path Reinforcement Curves : "

    ' Get path reinforcement curves by iterating the Curves property
    Dim curveIds As IList(Of ElementId) = pathReinforcement.GetCurveElementIds()
    For Each ii As Autodesk.Revit.DB.ElementId In curveIds
        Dim pathReinforcementCurve As ModelCurve = TryCast(doc.GetElement(ii), ModelCurve)
        If pathReinforcementCurve Is Nothing Then
            Continue For
        End If

        Dim curve As Autodesk.Revit.DB.Curve = pathReinforcementCurve.GeometryCurve

        ' Get curve start point
        message += ((vbLf & "Curve start point:(" + curve.GetEndPoint(0).X & ", ") + curve.GetEndPoint(0).Y & ", ") + curve.GetEndPoint(0).Z & ")"
        ' Get curve end point



        message += (("; Curve end point:(" + curve.GetEndPoint(1).X & ", ") + curve.GetEndPoint(1).Y & ", ") + curve.GetEndPoint(1).Z & ")"
    Next
    TaskDialog.Show("Revit", message)

End Sub
```

# See Also

[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)