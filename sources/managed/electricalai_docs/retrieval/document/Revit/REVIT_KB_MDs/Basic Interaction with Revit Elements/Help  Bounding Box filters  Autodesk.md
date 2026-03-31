---
created: 2026-01-28T20:48:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Bounding_Box_filters_html
author: 
---

# Help | Bounding Box filters | Autodesk

> ## Excerpt
> The BoundingBox filters:

---
The BoundingBox filters:

-   BoundingBoxIsInsideFilter
-   BoundingBoxIntersectsFilter
-   BoundingBoxContainsPointFilter

help you find elements whose bounding boxes meet a certain criteria. You can check if each element’s bounding box is inside a given volume, intersects a given volume, or contains a given point. You can also reverse this check to find elements which do not intersect a volume or contain a given point.

BoundingBox filters use Outline as their inputs. Outline is a class representing a right rectangular prism whose axes are aligned to the Revit world coordinate system.

These filters work best for shapes whose actual geometry matches closely the geometry of its bounding box. Examples might include linear walls whose curve aligns with the X or Y direction, rectangular rooms formed by such walls, floors or roofs aligned to such walls, or reasonably rectangular families. Otherwise, there is the potential for false positives as the bounding box of the element may be much bigger than the actual geometry. (In these cases, you can use the actual element’s geometry to determine if the element really meets the criteria).
