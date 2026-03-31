---
created: 2026-01-28T21:02:10 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Edge_and_face_parameterization_html
author: 
---

# Help | Edge and face parameterization | Autodesk

> ## Excerpt
> Edges are boundary curves for a given face.

---
Edges are boundary curves for a given face.

Iterate the edges of a Face using the EdgeLoops property. Each loop represents one closed boundary on the face. Edges are always parameterized from 0 to 1. It is possible to extract the Curve representation of an Edge with the Edge.AsCurve() and Edge.AsCurveFollowingFace() functions.

An edge is usually defined by computing intersection of two faces. But Revit doesn’t recompute this intersection when it draws graphics. So the edge stores a list of points - end points for a straight edge and a tessellated list for a curved edge. The points are parametric coordinates on the two faces. These points are available through the TessellateOnFace() method.

Sections produce “cut edges”. These are artificial edges - not representing a part of the model-level geometry, and thus do not provide a Reference.

### Edge direction

Direction is normally clockwise on the first face (first representing an arbitrary face which Revit has identified for a particular edge). But because two different faces meet at one particular edge, and the edge has the same parametric direction regardless of which face you are concerned with, sometimes you need to figure out the direction of the edge on a particular face.

The figure below illustrated how this works. For Face 0, the edges are all parameterized clockwise. For Face 1, the edge shared with Face 0 is not re-parameterized; thus with respect to Face 1 the edge has a reversed direction, and some edges intersect where both edges’ parameters are 0 (or 1).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_edge_direction.png)**Edge parameterization**

The API sample “PanelEdgeLengthAngle” shows how to recognize edges that are reversed for a given face. It uses the tangent vector at the edge endpoints to calculate the angle between adjacent edges, and detect whether or not to flip the tangent vector at each intersection to calculate the proper angle.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/paneledgelengthangle_sample.png)**PanelEdgeLengthAngle results**
