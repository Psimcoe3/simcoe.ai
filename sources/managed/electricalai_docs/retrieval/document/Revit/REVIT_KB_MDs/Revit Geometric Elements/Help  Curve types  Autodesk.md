---
created: 2026-01-28T21:01:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_types_html
author: 
---

# Help | Curve types | Autodesk

> ## Excerpt
> Revit uses a variety of curve types to represent curve geometry in a document.

---
Revit uses a variety of curve types to represent curve geometry in a document.

Curve types in Revit include:

<table summary="" id="GUID-AB7DD330-5FCA-47B3-BAC3-0E0658164FE8__TABLE_CA3E6D46CACF449C8F24C733188A98CF"><tbody><tr><td><b>Curve type</b></td><td><b>Revit API class</b></td><td><b>Definition</b></td><td><b>Notes</b></td></tr><tr><td>Bound line</td><td>Line</td><td>A line segment defined by its endpoints.</td><td>Obtain endpoints from Curve.GetEndpoint()</td></tr><tr><td>Unbound line</td><td>Line</td><td>An infinite line defined by a location and direction</td><td>Identify these with Curve.IsBound.<p>Evaluate point and tangent vector at raw parameter= 0 to find the input parameters for the equation of the line.</p></td></tr><tr><td>Arc</td><td>Arc</td><td>A bound circular arc</td><td>Begin and end at a certain angle. These angles can be obtained by the raw parameter values at each end of the arc.</td></tr><tr><td>Circle</td><td>Arc</td><td>An unbound circle</td><td>Identify with Curve.IsBound.<p>Use raw parameter for evaluation (from 0 to 2π)</p></td></tr><tr><td>Cylindrical helix</td><td>CylindricalHelix</td><td>A helix wound around a cylinder making constant angle with the axis of the cylinder</td><td>Used only in specific applications in stairs and railings, and should not be used or encountered when accessing curves of other Revit elements and geometry.</td></tr><tr><td>Elliptical arc</td><td>Ellipse</td><td>A bound elliptical segment</td><td></td></tr><tr><td>Ellipse</td><td>Ellipse</td><td>An unbound ellipse</td><td>Identify with Curve.IsBound. Use raw parameter for evaluation (from 0 to 2π)</td></tr><tr><td>NURBS</td><td>NurbSpline</td><td>A non-uniform rational B-spline</td><td>Used for splines sketched in various Revit tools, plus imported geometry</td></tr><tr><td>Hermite</td><td>HermiteSpline</td><td>A spline interpolate between a set of points</td><td>Used for tools like Curve by Points and flexible ducts/pipes, plus imported geometry</td></tr><tr><td colspan="2">CurveUV</td><td>A curve in the 2D parameter space of a surface in 3D space.</td><td>This class helps translate geometry (BReps) from external applications to Revit. Some geometric modelers represent the shape of an edge in a solid (or open shell) by a 3D curve, others use 2D curves in the parameter spaces of the edge’s faces, and others might use both. Revit can benefit from being given the CurveUVs for an edge when translating geometry, and this class accommodates the passing of such information.</td></tr></tbody></table>

Mathematical representations of all of the Revit curve types can be found in: [Mathematical representation of face types](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Mathematical_representation_of_face_types_html).
