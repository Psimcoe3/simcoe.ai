---
created: 2026-01-28T21:02:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Face_analysis_html
author: 
---

# Help | Face analysis | Autodesk

> ## Excerpt
> There are several Face methods which are tools suitable for use in geometric analysis.

---
There are several Face methods which are tools suitable for use in geometric analysis.

### Intersect()

The Intersect method computes the intersection between the face and a curve. It can be used in to identify:

-   The intersection point(s) between the two objects
-   The edge nearest the intersection point, if there is an edge close to this location
-   Curves totally coincident with a face
-   Curves and faces which do not intersect
    
    ### Project()
    

The Project method projects a point on the input face, and returns information on the projection point, the distance to the face, and the nearest edge to the projection point.

### Triangulate()

The Triangulate method obtains a triangular mesh approximating the face. There are two overloads to this method. The parameterless method is similar to Curve.Tessellate() in that the mesh’s points are accurate within the input tolerance used by Revit (slightly larger than 1/16”). The second Triangulate method accepts a level of detail as an argument ranging from 0 (coarse) to 1 (fine).
