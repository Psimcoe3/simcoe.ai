[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FieldDomainPointsByParameter Class

---



|  |
| --- |
| [Members](cd5dedd9-3347-3175-365f-2f325eddbd92.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Represents a set of one-dimensional point coordinates (defined usually on curve)

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class FieldDomainPointsByParameter : FieldDomainPoints ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FieldDomainPointsByParameter _ 	Inherits FieldDomainPoints ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FieldDomainPointsByParameter : public FieldDomainPoints ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
Document doc = commandData.Application.ActiveUIDocument.Document;
UIDocument uiDoc = commandData.Application.ActiveUIDocument;

SpatialFieldManager sfm = SpatialFieldManager.GetSpatialFieldManager(doc.ActiveView);
if (sfm == null)
{
    sfm = SpatialFieldManager.CreateSpatialFieldManager(doc.ActiveView, 1);
}

ReferenceArray ra = new ReferenceArray();
Reference curveRef = uiDoc.Selection.PickObject(ObjectType.Element, "Select a curve");
ra.Append(curveRef);

foreach (Reference reference in ra)
{
    ModelCurve modelCurve = doc.GetElement(reference) as ModelCurve;
    Curve curve = modelCurve.GeometryCurve;
    if (curve == null)
    {
        TaskDialog.Show("Error", "Must select a curve");
        return Result.Cancelled;
    }
    else
    {
        int idx = sfm.AddSpatialFieldPrimitive(curve.Reference);

        IList<double> pts = new List<double>();

        double u = curve.GetEndParameter(0);
        double range = curve.GetEndParameter(1) - u;
        for (int ii = 0; ii < 10; ii++)
        {
            pts.Add(u);
            u = u + range / 10;
        }

        FieldDomainPointsByParameter pnts = new FieldDomainPointsByParameter(pts);

        List<double> doubleList = new List<double>();
        IList<ValueAtPoint> valList = new List<ValueAtPoint>();
        double x = 0;
        while (valList.Count < pts.Count)
        //for (double x = 0; x < 1; x = x + 0.1)
        {
            doubleList.Clear();
            doubleList.Add(x * 10);
            valList.Add(new ValueAtPoint(doubleList));
            x = x + 0.1;
        }
        FieldValues vals = new FieldValues(valList);

        AnalysisResultSchema resultSchema = new AnalysisResultSchema("Schema Name", "Description");
        int schemaIndex = sfm.RegisterResult(resultSchema);
        sfm.UpdateSpatialFieldPrimitive(idx, pnts, vals, schemaIndex);
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Dim doc As Document = commandData.Application.ActiveUIDocument.Document
Dim uiDoc As UIDocument = commandData.Application.ActiveUIDocument

Dim sfm As SpatialFieldManager = SpatialFieldManager.GetSpatialFieldManager(doc.ActiveView)
If sfm Is Nothing Then
    sfm = SpatialFieldManager.CreateSpatialFieldManager(doc.ActiveView, 1)
End If

Dim ra As New ReferenceArray()
Dim curveRef As Reference = uiDoc.Selection.PickObject(ObjectType.Element, "Select a curve")
ra.Append(curveRef)

For Each reference As Reference In ra
    Dim modelCurve As ModelCurve = TryCast(doc.GetElement(reference), ModelCurve)
    Dim curve As Curve = modelCurve.GeometryCurve
    If curve Is Nothing Then
        TaskDialog.Show("Error", "Must select a curve")
        Return Result.Cancelled
    Else
        Dim idx As Integer = sfm.AddSpatialFieldPrimitive(curve.Reference)

        Dim pts As IList(Of Double) = New List(Of Double)()

        Dim u As Double = curve.GetEndParameter(0)
        Dim range As Double = curve.GetEndParameter(1) - u
        For ii As Integer = 0 To 9
            pts.Add(u)
            u = u + range / 10
        Next

        Dim pnts As New FieldDomainPointsByParameter(pts)

        Dim doubleList As New List(Of Double)()
        Dim valList As IList(Of ValueAtPoint) = New List(Of ValueAtPoint)()
        Dim x As Double = 0
        While valList.Count < pts.Count
            'for (double x = 0; x < 1; x = x + 0.1)
            doubleList.Clear()
            doubleList.Add(x * 10)
            valList.Add(New ValueAtPoint(doubleList))
            x = x + 0.1
        End While
        Dim vals As New FieldValues(valList)

        Dim resultSchema As New AnalysisResultSchema("Schema Name", "Description")
        Dim schemaIndex As Integer = sfm.RegisterResult(resultSchema)
        sfm.UpdateSpatialFieldPrimitive(idx, pnts, vals, schemaIndex)
    End If
Next
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB.Analysis FieldDomainPoints](5b145517-1904-4b5f-2f66-0d84b259335b.htm)    
  Autodesk.Revit.DB.Analysis FieldDomainPointsByParameter

# See Also

[FieldDomainPointsByParameter Members](cd5dedd9-3347-3175-365f-2f325eddbd92.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)