[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IViewSheetSet Interface

---



|  |
| --- |
| [Members](538dc970-ea92-b42c-144c-481032f284bf.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

This interface represents a selected set of views/sheets which will be used for printing.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public interface IViewSheetSet ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IViewSheetSet ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IViewSheetSet ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void SwitchToAutomaticOrder(Document doc, ViewSheetSetting viewSheetSetting)
{
   IViewSheetSet viewSheetSet = viewSheetSetting.CurrentViewSheetSet;
   var sheetBrowserOrg = BrowserOrganization.GetCurrentBrowserOrganizationForSheets(doc);
   var viewBrowserOrg = BrowserOrganization.GetCurrentBrowserOrganizationForViews(doc);
   viewSheetSet.SheetOrganizationId = sheetBrowserOrg.Id;
   viewSheetSet.ViewOrganizationId = viewBrowserOrg.Id;
   viewSheetSet.IsAutomatic = true; // IsAutomatic must be true then views and sheets will be ordered by Browser Organization
}

private void SwitchToCustomOrder(Document doc, ViewSheetSetting viewSheetSetting, IReadOnlyList<View> customViews)
{
   IViewSheetSet viewSheetSet = viewSheetSetting.CurrentViewSheetSet;
   // IsAutomatic must be false, then OrderedViewList will be organized in custom order
   // Note that the moment you set IsAutomatic from true to false, the order in OrderedViewList will be organized by Browser Organization
   viewSheetSet.IsAutomatic = false; // IMPORTANT: IsAutomatic before assigning OrderedViewList
   viewSheetSet.OrderedViewList = customViews;
}
```

# See Also

[IViewSheetSet Members](538dc970-ea92-b42c-144c-481032f284bf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)