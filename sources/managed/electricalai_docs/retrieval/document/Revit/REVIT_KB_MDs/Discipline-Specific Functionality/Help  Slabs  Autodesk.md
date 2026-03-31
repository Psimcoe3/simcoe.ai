---
created: 2026-01-28T21:10:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Slabs_html
author: 
---

# Help | Slabs | Autodesk

> ## Excerpt
> Both Slab (Structural Floor) and Slab Foundation are represented by the Floor class and are distinguished by the IsFoundationSlab property.

---
## Slab

Both Slab (Structural Floor) and Slab Foundation are represented by the Floor class and are distinguished by the IsFoundationSlab property.

The Slab Span Directions are represented by the IndependentTag class in the API and are available as follows:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-23AFA5D3-DFA8-48EE-BDC3-EFB37BADCB7D-low.png)**Figure 157: Slab span directions**

When using Floor.Create() to create a Slab, Span Directions are not automatically created. There is also no way to create them directly.

The Slab compound structure layer Structural Deck properties are exposed by the following properties:

-   CompoundStructuralLayer.DeckUsage
-   DeckProfile

The properties are outlined in the following dialog box:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F892CB9B-E142-4112-8925-32C543D8A9AA-low.png)**Figure 158: Floor CompoundStructuralLayer properties**
