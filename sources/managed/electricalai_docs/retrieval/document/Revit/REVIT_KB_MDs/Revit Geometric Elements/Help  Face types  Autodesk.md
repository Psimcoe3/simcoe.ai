---
created: 2026-01-28T21:02:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Face_types_html
author: 
---

# Help | Face types | Autodesk

> ## Excerpt
> Revit uses a variety of curve types to represent face geometry in a document. These include:

---
Revit uses a variety of curve types to represent face geometry in a document. These include:

<table summary="" id="GUID-12AF716F-7135-405B-8005-26A15EB58025__TABLE_6C2033AA354141EB83F6506DD7E2CF21"><tbody><tr><td><b>Face type</b></td><td><b>Revit API class</b></td><td><b>Definition</b></td><td><b>Notes</b></td></tr><tr><td>Plane</td><td>PlanarFace</td><td>A plane defined by the origin and unit vectors in U and V.</td><td></td></tr><tr><td>Cylinder</td><td>CylindricalFace</td><td>A face defined by extruding a circle along an axis.</td><td>.Radius provides the “radius vectors” – the unit vectors of the circle multiplied by the radius value.</td></tr><tr><td>Cone</td><td>ConicalFace</td><td>A face defined by rotation of a line about an axis.</td><td>.Radius provides the “radius vectors” – the unit vectors of the circle multiplied by the radius value.</td></tr><tr><td>Revolved face</td><td>RevolvedFace</td><td>A face defined by rotation of an arbitrary curve about an axis.</td><td>.Radius provides the unit vectors of the plane of rotation, there is no “radius” involved.</td></tr><tr><td>Ruled surface</td><td>RuledFace</td><td>A face defined by sweeping a line between two profile curves, or one profile curve and one point.</td><td>Both curve(s) and point(s) can be obtained as properties.</td></tr><tr><td>Hermite face</td><td>HermiteFace</td><td>A face defined by Hermite interpolation between points.</td><td></td></tr></tbody></table>

Mathematical representations of all of the Revit face types can be found in: [Mathematical representation of face types](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Mathematical_representation_of_face_types_html).
