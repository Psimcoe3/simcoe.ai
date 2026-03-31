[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewType Property

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

The type of the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ViewType ViewType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ViewType As ViewType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ViewType ViewType { 	ViewType get (); } ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetViewType(Autodesk.Revit.DB.View view)
{
    // Get the view type of the given view, and format the prompt string
    String prompt = "The view is ";

    switch (view.ViewType)
    {
        case ViewType.AreaPlan:
            prompt += "an area view.";
            break;
        case ViewType.CeilingPlan:
            prompt += "a reflected ceiling plan view.";
            break;
        case ViewType.ColumnSchedule:
            prompt += "a column schedule view.";
            break;
        case ViewType.CostReport:
            prompt += "a cost report view.";
            break;
        case ViewType.Detail:
            prompt += "a detail view.";
            break;
        case ViewType.DraftingView:
            prompt += "a drafting view.";
            break;
        case ViewType.DrawingSheet:
            prompt += "a drawing sheet view.";
            break;
        case ViewType.Elevation:
            prompt += "an elevation view.";
            break;
        case ViewType.EngineeringPlan:
            prompt += "an engineering view.";
            break;
        case ViewType.FloorPlan:
            prompt += "afloor plan view.";
            break;
        case ViewType.Internal:
            prompt += "Revit's internal view.";
            break;
        case ViewType.Legend:
            prompt += "a legend view.";
            break;
        case ViewType.LoadsReport:
            prompt += "a loads report view.";
            break;
        case ViewType.PanelSchedule:
            prompt += "a panel schedule view.";
            break;
        case ViewType.PresureLossReport:
            prompt += "a pressure loss report view.";
            break;
        case ViewType.Rendering:
            prompt += "a rendering view.";
            break;
        case ViewType.Report:
            prompt += "a report view.";
            break;
        case ViewType.Schedule:
            prompt += "a schedule view.";
            break;
        case ViewType.Section:
            prompt += "a cross section view.";
            break;
        case ViewType.ThreeD:
            prompt += "a 3-D view.";
            break;
        case ViewType.Undefined:
            prompt += "an undefined/unspecified view.";
            break;
        case ViewType.Walkthrough:
            prompt += "a walkthrough view.";
            break;
        default:
            break;
    }

    // Give the user some information
    TaskDialog.Show("Revit",prompt);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetViewType(view As Autodesk.Revit.DB.View)
    ' Get the view type of the given view, and format the prompt string
    Dim prompt As [String] = "The view is "

    Select Case view.ViewType
        Case ViewType.AreaPlan
            prompt += "an area view."
            Exit Select
        Case ViewType.CeilingPlan
            prompt += "a reflected ceiling plan view."
            Exit Select
        Case ViewType.ColumnSchedule
            prompt += "a column schedule view."
            Exit Select
        Case ViewType.CostReport
            prompt += "a cost report view."
            Exit Select
        Case ViewType.Detail
            prompt += "a detail view."
            Exit Select
        Case ViewType.DraftingView
            prompt += "a drafting view."
            Exit Select
        Case ViewType.DrawingSheet
            prompt += "a drawing sheet view."
            Exit Select
        Case ViewType.Elevation
            prompt += "an elevation view."
            Exit Select
        Case ViewType.EngineeringPlan
            prompt += "an engineering view."
            Exit Select
        Case ViewType.FloorPlan
            prompt += "afloor plan view."
            Exit Select
        Case ViewType.Internal
            prompt += "Revit's internal view."
            Exit Select
        Case ViewType.Legend
            prompt += "a legend view."
            Exit Select
        Case ViewType.LoadsReport
            prompt += "a loads report view."
            Exit Select
        Case ViewType.PanelSchedule
            prompt += "a panel schedule view."
            Exit Select
        Case ViewType.PresureLossReport
            prompt += "a pressure loss report view."
            Exit Select
        Case ViewType.Rendering
            prompt += "a rendering view."
            Exit Select
        Case ViewType.Report
            prompt += "a report view."
            Exit Select
        Case ViewType.Schedule
            prompt += "a schedule view."
            Exit Select
        Case ViewType.Section
            prompt += "a cross section view."
            Exit Select
        Case ViewType.ThreeD
            prompt += "a 3-D view."
            Exit Select
        Case ViewType.Undefined
            prompt += "an undefined/unspecified view."
            Exit Select
        Case ViewType.Walkthrough
            prompt += "a walkthrough view."
            Exit Select
        Case Else
            Exit Select
    End Select

    ' Give the user some information
    TaskDialog.Show("Revit", prompt)
End Sub
```

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)