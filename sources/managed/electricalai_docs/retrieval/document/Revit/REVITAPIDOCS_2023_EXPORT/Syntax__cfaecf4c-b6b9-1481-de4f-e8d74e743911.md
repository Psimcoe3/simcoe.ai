[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementOwnerViewFilter Class

---



|  |
| --- |
| [Members](b898c6a2-434b-a746-180a-f3f2d7da8ca0.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A filter used to match elements which are owned by a particular view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class ElementOwnerViewFilter : ElementQuickFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ElementOwnerViewFilter _ 	Inherits ElementQuickFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ElementOwnerViewFilter : public ElementQuickFilter ``` |

# Remarks

This filter is a quick filter. Quick filters operate only on the ElementRecord, a low-memory class which has a limited interface to read element properties. Elements which are rejected by a quick filter will not be expanded in memory.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Use ElementOwnerView filter to find TextNotes in the active view

// Create an ElementOwnerView filter with id of active view
ElementOwnerViewFilter elementOwnerViewFilter = new ElementOwnerViewFilter(document.ActiveView.Id);

// Apply the filter to the elements in the active document,
// Use shortcut method OfClass() to find TextNotes only
FilteredElementCollector collector = new FilteredElementCollector(document);
ICollection<Element> textNotesOfActiveView =
    collector.WherePasses(elementOwnerViewFilter).OfClass(typeof(TextNote)).ToElements();

// Find TextNotes which are not owned by active view: use an inverted filter to match TextNotes
ElementOwnerViewFilter notOwnedFilter = new ElementOwnerViewFilter(document.ActiveView.Id, true); // inverted filter
collector = new FilteredElementCollector(document);
ICollection<Element> notOwnedByViewFounds =
    collector.WherePasses(notOwnedFilter).OfClass(typeof(TextNote)).ToElements();
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Use ElementOwnerView filter to find TextNotes in the active view


' Create an ElementOwnerView filter with id of active view
Dim elementOwnerViewFilter As New ElementOwnerViewFilter(document.ActiveView.Id)

' Apply the filter to the elements in the active document,
' Use shortcut method OfClass() to find TextNotes only
Dim collector As New FilteredElementCollector(document)
Dim textNotesOfActiveView As ICollection(Of Element) = collector.WherePasses(elementOwnerViewFilter).OfClass(GetType(TextNote)).ToElements()

' Find TextNotes which are not owned by active view: use an inverted filter to match TextNotes
Dim notOwnedFilter As New ElementOwnerViewFilter(document.ActiveView.Id, True)
' inverted filter
collector = New FilteredElementCollector(document)
Dim notOwnedByViewFounds As ICollection(Of Element) = collector.WherePasses(notOwnedFilter).OfClass(GetType(TextNote)).ToElements()
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementQuickFilter](ebc95d82-11fc-69f6-2df1-52331dd36443.htm)    
  Autodesk.Revit.DB ElementOwnerViewFilter

# See Also

[ElementOwnerViewFilter Members](b898c6a2-434b-a746-180a-f3f2d7da8ca0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)