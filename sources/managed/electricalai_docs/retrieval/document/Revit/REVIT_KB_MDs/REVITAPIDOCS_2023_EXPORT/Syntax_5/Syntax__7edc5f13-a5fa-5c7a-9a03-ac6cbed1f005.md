[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanViewRange Class

---



|  |
| --- |
| [Members](a4646f2b-a4ae-f631-196e-e0aaf4e9576f.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

This class represents the view range of a plan view or a plan region. It records the element ids of the levels which a plane is relative to and the offset of each plane from that level.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class PlanViewRange : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PlanViewRange _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PlanViewRange : IDisposable ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private ElementId GetViewRangeTopClipPlane(Document doc, View view)
{
    ElementId topClipPlane = ElementId.InvalidElementId;

    if (view is ViewPlan)
    {
        ViewPlan viewPlan = view as ViewPlan;
        PlanViewRange viewRange = viewPlan.GetViewRange();

        topClipPlane = viewRange.GetLevelId(PlanViewPlane.TopClipPlane);
        double dOffset = viewRange.GetOffset(PlanViewPlane.TopClipPlane);

        if (topClipPlane != ElementId.InvalidElementId)
        {
            Element levelAbove = doc.GetElement(topClipPlane);
            TaskDialog.Show(view.Name, "Top Clip Plane: " + levelAbove.Name + "\r\nTop Offset: " + dOffset + " ft");
        }
    }

    return topClipPlane;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Function GetViewRangeTopClipPlane(doc As Document, view As View) As ElementId
    Dim topClipPlane As ElementId = ElementId.InvalidElementId

    If TypeOf view Is ViewPlan Then
        Dim viewPlan As ViewPlan = TryCast(view, ViewPlan)
        Dim viewRange As PlanViewRange = viewPlan.GetViewRange()

        topClipPlane = viewRange.GetLevelId(PlanViewPlane.TopClipPlane)
        Dim dOffset As Double = viewRange.GetOffset(PlanViewPlane.TopClipPlane)

        If topClipPlane.IntegerValue > 0 Then
            Dim levelAbove As Element = doc.GetElement(topClipPlane)
            TaskDialog.Show(view.Name, "Top Clip Plane: " + levelAbove.Name + vbCr & vbLf & "Top Offset: " + dOffset + " ft")
        End If
    End If

    Return topClipPlane
End Function
```

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB PlanViewRange

# See Also

[PlanViewRange Members](a4646f2b-a4ae-f631-196e-e0aaf4e9576f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)