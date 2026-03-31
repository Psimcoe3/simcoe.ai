---
created: 2026-01-28T21:34:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_html
author: 
---

# Help | Selection | Autodesk

> ## Excerpt
> You can get the selected objects from the current active document using the UIDocument.Selection.GetElementIds() method which returns a collection fo ElementIds of the selected elements. The collection returned by this method can be used directly with FilteredElementCollector to filter the selected elements.

---
You can get the selected objects from the current active document using the UIDocument.Selection.GetElementIds() method which returns a collection fo ElementIds of the selected elements. The collection returned by this method can be used directly with FilteredElementCollector to filter the selected elements.

The Selection object can also be used to change the current selection programmatically using the SetElementIds() method.

**Pages in this section**

-   [Changing the Selection](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_Changing_the_Selection_html)
-   [User Selection](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_User_Selection_html)
-   [Filtered User Selection](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_Filtered_User_Selection_html)

**Parent page:** [Basic Interaction with Revit Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_html)
