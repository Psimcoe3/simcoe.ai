---
created: 2026-01-28T21:34:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_html
author: 
---

# Help | GeometryObject Class | Autodesk

> ## Excerpt
> The indexed property Element.Geometry[] can be used to pull the geometry of any model element (3D element). This applies both to system family instances such as walls, floors and roofs, and also to family instances of many categories, e.g. doors, windows, furniture, or masses.

---
The indexed property Element.Geometry\[\] can be used to pull the geometry of any model element (3D element). This applies both to system family instances such as walls, floors and roofs, and also to family instances of many categories, e.g. doors, windows, furniture, or masses.

The property GeometryObject.Id returns an integer value which may be used to identify the GeometryObject in its associated GeometryElement when the value is non-negative and not duplicated by other GeometryObjects in the associated GeometryElement.

The extracted geometry is returned to you as Autodesk.Revit.DB.GeometryElement. You can iterate through the geometry members of that element by using the GetEnumerator() method.

Typically, the objects returned at the top level of the extracted geometry will be one of:

-   [Solids, Faces and Edges](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_html) – a boundary representation made up of faces and edges
-   [Meshes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Meshes_html) – a 3D array of triangles
-   [Curves](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_html) – a bounded 3D curve
-   [Points](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Points_html) – a visible point datum at a given 3D location
-   [PolyLines](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_PolyLines_html) – a series of line segments defined by 3D points
-   [GeometryInstances](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_GeometryInstances_html) – an instance of a geometric element positioned within the element

This figure illustrates the hierarchy of objects found by geometry extraction.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/geometry_hierarchy.png)
