---
created: 2026-01-28T21:01:52 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Points_html
author: 
---

# Help | Points | Autodesk

> ## Excerpt
> A point represents a visible coordinate in 3D space.

---
A point represents a visible coordinate in 3D space.

Points are typically encountered in mass family elements like ReferencePoint. The Point class provides read access to its coordinates, and an ability to obtain a reference to the point for use as input to other functions.

### Point creation

There are two ways to create Points:

-   Create(XYZ) - creates a Point at the given coordinates.
-   Create(XYZ, ElementId) - creates a Point at given coordinates and assigns it a color based on the GraphicsStyle element (specified by ElementId).
