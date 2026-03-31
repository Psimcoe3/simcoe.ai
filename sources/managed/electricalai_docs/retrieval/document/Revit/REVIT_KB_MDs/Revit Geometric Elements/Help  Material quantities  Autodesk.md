---
created: 2026-01-28T21:03:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Material_quantities_html
author: 
---

# Help | Material quantities | Autodesk

> ## Excerpt
> There are methods to directly obtain the material volumes and areas computed by Revit for material takeoff schedules:

---
There are methods to directly obtain the material volumes and areas computed by Revit for material takeoff schedules:

-   Element.GetMaterialIds() – obtains a list of materials within an element
-   Element.GetMaterialVolume() – obtains the volume of a particular material in an element
-   Element.GetMaterialArea() – obtains the area of a particular material in an element

The methods apply to categories of elements where Category.HasMaterialQuantities property is true. In practice, this is limited to elements that use compound structure, like walls, roofs, floors, ceilings, a few other basic 3D elements like stairs, plus 3D families where materials can be assigned to geometry of the family, like windows, doors, columns, MEP equipment and fixtures, and generic model families. Note that within these categories there are further restrictions about how material quantities can be extracted. For example, curtain walls and curtain roofs will not report any material quantities themselves; the materials used by these constructs can be extracted from the individual panel elements that make up the curtain system.

Note that the volumes and areas computed by Revit may be approximate in some cases. For example, for individual layers within a wall, minor discrepancies might appear between the volumes visible in the model and those shown in the material takeoff schedule. These discrepancies tend to occur when you use the wall sweep tool to add a sweep or a reveal to a wall, or under certain join conditions.

The SDK sample “MaterialQuantities” combines both the material quantity extraction tools and temporary suppression of cutting elements (opening, windows, and doors) to extract both gross and net material quantities.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/material_quantities.png)
