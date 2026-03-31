---
created: 2026-01-28T21:02:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_html
author: 
---

# Help | Solids, Faces and Edges | Autodesk

> ## Excerpt
> A Solid is a Revit API object which represents a collection of faces and edges. Typically in Revit these collections are fully enclosed volumes, but a shell or partially bounded volume can also be encountered. Note that sometimes the Revit geometry will contain unused solids containing zero edges and faces. Check the Edges and Faces members to filter out these solids.

---
A Solid is a Revit API object which represents a collection of faces and edges. Typically in Revit these collections are fully enclosed volumes, but a shell or partially bounded volume can also be encountered. Note that sometimes the Revit geometry will contain unused solids containing zero edges and faces. Check the Edges and Faces members to filter out these solids.

The Revit API offers the ability to read the collections of faces and edges, and also to compute the surface area, volume, and centroid of the solid.
