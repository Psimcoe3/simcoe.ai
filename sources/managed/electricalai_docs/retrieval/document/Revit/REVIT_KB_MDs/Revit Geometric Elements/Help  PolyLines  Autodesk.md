---
created: 2026-01-28T21:01:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_PolyLines_html
author: 
---

# Help | PolyLines | Autodesk

> ## Excerpt
> A polyline is a collection of line segments defined by a set of coordinate points. These are typically encountered in imported geometry. The PolyLine class offers the ability to read the coordinates:

---
A polyline is a collection of line segments defined by a set of coordinate points. These are typically encountered in imported geometry. The PolyLine class offers the ability to read the coordinates:

-   PolyLine.NumberOfCoordinates – the number of points in the polyline
-   PolyLine.GetCoordinate() – gets a coordinate by index
-   PolyLine.GetCoordinates() – gets a collection of all coordinates in the polyline
-   PolyLine.Evaluate() – given a normalized parameter (from 0 to 1) evaluates an XYZ point along the extents of the entire polyline
