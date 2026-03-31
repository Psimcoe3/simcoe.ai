---
created: 2026-01-28T21:03:11 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Utility_Classes_html
author: 
---

# Help | Geometry Utility Classes | Autodesk

> ## Excerpt
> A number of utility classes are available for working with geometry objects.

---
A number of utility classes are available for working with geometry objects.

### HostObjectUtils

The HostObjectUtils class offers methods as a shortcut to locate certain faces of compound HostObjects. These utilities retrieve the faces which act as the boundaries of the object's CompoundStructure:

-   HostObjectUtils.GetSideFaces() – applicable to Walls and FaceWalls; you can obtain either the exterior or interior finish faces.
-   HostObjectUtils.GetTopFaces() and HostObjectUtils.GetBottomFaces() – applicable to roofs, floors, and ceilings.
    
    ### SolidUtils
    

The SolidUtils class contains methods to perform operations on solids.

-   SolidUtils.Clone() - creates a new Solid which is a copy of the input Solid
-   SolidUtils.SplitVolumes() - takes a solid which includes disjoint enclosed volumes and returns newly created Solid objects representing each volume. If no splitting is necessary, the input solid is returned.
-   SolidUtils.TessellateSolidOrShell() - triangulates a given input Solid (which can be one or more fully closed volumes, or an open shell). Returns a TriangulatedSolidOrShell object which allows access to the stored triangulated boundary component of a solid or a triangulated connected component of a shell.
-   SolidUtils.CreateTransformed() - creates a new solid which is the transformation of the input solid.
    
    ### JoinGeometryUtils
    

The JoinGeometryUtils class contains methods for joining and unjoining elements, and for managing the order in which elements are joined. These utilities are not available for family documents.

-   JoinGeometryUtils.AreElementsJoined() - determines whether two elements are joined
-   JoinGeometryUtils.GetJoinedElements() - returns all elements joined to given element
-   JoinGeometryUtils.JoinGeometry() - creates a join between two elements that share a comon face. The visible edge between the joined elements is removed. and the joined elements then share the same line weight and fill pattern.
-   JoinGeometryUtils.UnjoinGeometry() - removes a join between two joined elements
-   JoinGeometryUtils.SwitchJoinOrder() - reverses the order in which two elements are joined. The cutting element becomes the cut element and vice versa.
-   JoinGeometryUtils . IsCuttingElementInJoin() - determines whether the first of two joined elements is cutting the second element or vice versa.
    
    ### FacetingUtils
    

This class is used to convert a triangulated structure into a structure in which some of the triangles have been consolidated into quadrilaterals.

-   FacetingUtils.ConvertTrianglesToQuads() - this method takes a TriangulationInterface (constructed from a TriangulatedSolidOrShell) as input and returns a collection of triangles and quadrilaterals representing the original triangulated object.
