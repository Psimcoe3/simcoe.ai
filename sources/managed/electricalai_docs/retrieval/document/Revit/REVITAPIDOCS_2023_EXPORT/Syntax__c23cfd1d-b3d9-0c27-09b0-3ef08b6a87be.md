[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WorksharingDisplayMode Enumeration

---



|  |
| --- |
| [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Indicates which worksharing display mode a view is in.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public enum WorksharingDisplayMode ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration WorksharingDisplayMode ``` |

 

| Visual C++ |
| --- |
| ``` public enum class WorksharingDisplayMode ``` |

# Members

| Member name | Description |
| --- | --- |
| Off | No active worksharing display mode. |
| CheckoutStatus | The view is displaying the checkout status of elements. |
| Owners | The view is displaying the specific owners of elements. |
| ModelUpdates | The view is displaying model updates. |
| Worksets | The view is displaying which workset each element is assigned to. |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetWorksharingDisplayMode(View view)
{
    // Get and Set worksharingDisplayMode of a given view
    WorksharingDisplayMode displayMode = view.GetWorksharingDisplayMode();
    Autodesk.Revit.UI.TaskDialog.Show("GetWorksharingDisplayMode", "WorksharingDisplayMode : " + displayMode);

    view.SetWorksharingDisplayMode(WorksharingDisplayMode.CheckoutStatus);
    Autodesk.Revit.UI.TaskDialog.Show("SetWorksharingDisplayMode", "CheckoutStatus was set for View: " + view.Name);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetWorksharingDisplayMode(view As View)
    ' Get and Set worksharingDisplayMode of a given view
    Dim displayMode As WorksharingDisplayMode = view.GetWorksharingDisplayMode()
    Autodesk.Revit.UI.TaskDialog.Show("GetWorksharingDisplayMode", "WorksharingDisplayMode : " + displayMode)

    view.SetWorksharingDisplayMode(WorksharingDisplayMode.CheckoutStatus)
    Autodesk.Revit.UI.TaskDialog.Show("SetWorksharingDisplayMode", "CheckoutStatus was set for View: " + view.Name)
End Sub
```

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)