[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AdaptiveComponentInstanceUtils Class

---



|  |
| --- |
| [Members](e2dffdd5-152e-937f-940a-5fd6fa06df6b.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

An interface for Adaptive Component Instances.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static class AdaptiveComponentInstanceUtils ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class AdaptiveComponentInstanceUtils ``` |

 

| Visual C++ |
| --- |
| ``` public ref class AdaptiveComponentInstanceUtils abstract sealed ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void CreateAdaptiveComponentInstance(Document document, FamilySymbol symbol)
{
    // Create a new instance of an adaptive component family
    FamilyInstance instance = AdaptiveComponentInstanceUtils.CreateAdaptiveComponentInstance(document, symbol);

    // Get the placement points of this instance
    IList<ElementId> placePointIds = new List<ElementId>();
    placePointIds = AdaptiveComponentInstanceUtils.GetInstancePlacementPointElementRefIds(instance);
    double x = 0;

    // Set the position of each placement point
    foreach (ElementId id in placePointIds)
    {
        ReferencePoint point = document.GetElement(id) as ReferencePoint;
        point.Position = new Autodesk.Revit.DB.XYZ(10*x, 10*Math.Cos(x), 0);
        x += Math.PI/6;
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub CreateAdaptiveComponentInstance(document As Document, symbol As FamilySymbol)
    ' Create a new instance of an adaptive component family
    Dim instance As FamilyInstance = AdaptiveComponentInstanceUtils.CreateAdaptiveComponentInstance(document, symbol)

    ' Get the placement points of this instance
    Dim placePointIds As IList(Of ElementId) = New List(Of ElementId)()
    placePointIds = AdaptiveComponentInstanceUtils.GetInstancePlacementPointElementRefIds(instance)
    Dim x As Double = 0

    ' Set the position of each placement point
    For Each id As ElementId In placePointIds
        Dim point As ReferencePoint = TryCast(document.GetElement(id), ReferencePoint)
        point.Position = New Autodesk.Revit.DB.XYZ(10 * x, 10 * Math.Cos(x), 0)
        x += Math.PI / 6
    Next
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB AdaptiveComponentInstanceUtils

# See Also

[AdaptiveComponentInstanceUtils Members](e2dffdd5-152e-937f-940a-5fd6fa06df6b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)