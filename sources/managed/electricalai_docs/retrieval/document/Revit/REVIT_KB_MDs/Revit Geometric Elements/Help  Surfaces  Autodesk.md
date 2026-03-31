---
created: 2026-01-28T21:04:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Surfaces_html
author: 
---

# Help | Surfaces | Autodesk

> ## Excerpt
> The surface class represents the mathematical representation of a surface.

---
The surface class represents the mathematical representation of a surface.

The surface class is not derived from the GeometryObject class and not bounded by edges or edge loops. A bounded surface in Revit is represented by the [Face](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_html) class.

Surface is the base class for more specific surfaces:

-   Plane
-   CylindricalSurface
-   ConicalSurface
-   RuledSurface
-   RevolvedSurface
-   HermiteSurface
-   OffsetSurface - Represents a surface offset by a fixed distance in the direction of the originating surface normal. The signed offset distance is in the direction of the originating surface’s oriented normal vector at any given point, which can be the same as or opposite to the originating surface’s parametric normal vector.

These subclasses contain Create() methods and read-only properties and are suitable for constructing import geometry. See the [DirectShape](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_DirectShape_html "This element type can store arbitrary geometry obtained from import operations or calculations in either a project or family document.") topic for examples of using Surfaces in geometry creation.
