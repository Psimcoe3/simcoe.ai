---
created: 2026-01-28T21:01:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_analysis_html
author: 
---

# Help | Curve analysis | Autodesk

> ## Excerpt
> There are several Curve methods which are tools suitable for use in geometric analysis.

---
There are several Curve methods which are tools suitable for use in geometric analysis.

In some cases, these APIs do more than you might expect by a quick review of their names.

### Intersect()

The Intersect method allows you compare two curves to find how they differ or how they are similar. It can be used in the manner you might expect, to obtain the point or point(s) where two curves intersect one another, but it can also be used to identify:

-   Collinear lines
-   Overlapping lines
-   Identical curves
-   Totally distinct curves with no intersections

The return value identifies these different results, and the output IntersectionSetResult contains information on the intersection point(s).

### Project()

The Project method projects a point onto the curve and returns information about the nearest point on the curve, its parameter, and the distance from the projection point.

### Tessellate()

This splits the curve into a series of linear segments, accurate within a default tolerance. For Curve.Tessellate(), the tolerance is slightly larger than 1/16”. This tolerance of approximation is the tolerance used internally by Revit as adequate for display purposes.

Note that only lines may be split into output of only two tessellation points; non-linear curves will always output more than two points even if the curve has an extremely large radius which might mathematically equate to a straight line.
