---
created: 2026-01-28T20:48:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Create_a_FilteredElementCollector_html
author: 
---

# Help | Create a FilteredElementCollector | Autodesk

> ## Excerpt
> The main class used for element iteration and filtering is called FilteredElementCollector. It is constructed in one of three ways:

---
The main class used for element iteration and filtering is called FilteredElementCollector. It is constructed in one of three ways:

1.  From a document - will search and filter the set of elements in a document
2.  From a document and set of ElementIds - will search and filter a specified set of elements
3.  From a document and a view - will search and filter the visible elements in a view

Note: Always check that a view is valid for element iteration when filtering elements in a specified view by using the static FilteredElementCollector.IsViewValidForElementIteration().

When the object is first created, there are no filters applied. This class requires that at least one condition be set before making at attempt to access the elements, otherwise an exception will be thrown.
