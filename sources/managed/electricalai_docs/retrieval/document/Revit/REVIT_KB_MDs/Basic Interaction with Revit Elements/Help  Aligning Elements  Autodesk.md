---
created: 2026-01-28T20:50:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Aligning_Elements_html
author: 
---

# Help | Aligning Elements | Autodesk

> ## Excerpt
> The ItemFactoryBase.NewAlignment() method can create a new locked alignment between two references. These two references must be one of the following combinations:

---
The ItemFactoryBase.NewAlignment() method can create a new locked alignment between two references. These two references must be one of the following combinations:

-   2 planar faces
-   2 lines
-   line and point
-   line and reference plane
-   2 arcs
-   2 cylindrical faces

These references must be already geometrically aligned as this function will not force them to become aligned. If the alignment can be created a new Dimension object is returned representing the locked alignment. Otherwise an exception will be thrown.

The NewAlignment() method also requires a view which will determine the orientation of the alignment.

See the CreateTruss example in the FamilyCreation folder included with the SDK Samples. It has several examples of the use of NewAlignment(), such as locking the bottom chord of a new truss to a bottom reference plane.
