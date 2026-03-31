[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BRepBuilder Members

---



|  |
| --- |
| [BRepBuilder Class](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [BRepBuilder](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [BRepBuilder](b3eb95b6-2297-44dc-df94-38aed1940b8c.htm) | Construct a BRepBuilder to use in constructing geometry. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddCoEdge](c4713a48-712b-e293-6745-a266af97e195.htm) | Add a co-edge associated to a previously added edge. A co-edge represents the use of an edge on one of the edge's faces. BrepBuilder allows at most two faces per edge, hence at most two co-edges per edge, and the co-edges must have opposite bCoEdgeIsReversed flags. The co-edges in a loop must be added in the order in which they occur in loop (i.e., in their topological order). |
| Public method | [AddEdge](75963b10-7aec-dd68-e160-4a198161dadc.htm) | Add a new edge to the geometry being built. The BRepBuilder uses edges only to store edge geometry and to track pairs of co-edges that share an edge. |
| Public method | [AddFace](cb899f6d-c4e0-0983-ab70-bae0a620dc8d.htm) | Creates an empty face in the geometry being built. Other BRepBuilder methods are used to add loops to the face. |
| Public method | [AddLoop](169a75b9-2b82-09ec-a6f1-a9b82e8f32fe.htm) | Creates an empty loop in a given face of the geometry being built. Other BRepBuilder methods are used to add co-edges to the loop. |
| Public method | [AllowRemovalOfProblematicFaces](727b6da1-e4d9-8077-c974-e7c1fb8ce34c.htm) | Allow BRepBuilder to remove problematic faces (e.g., due to inaccurate edge geometry). If this option is enabled and BRepBuilder removes some faces, the output geometry's type will be OpenShell regardless of the expected type specified when the BRepBuilder was created. |
| Public method | [CanAddGeometry](8bf14f8a-bbf4-c661-1588-1626e574238b.htm) | A validator function that checks the state of this BRepBuilder object. Returns true if this BRepBuilder object is accepting b-rep data, false otherwise. |
| Public method | [Dispose](efbfadf8-519d-7f66-8553-e887ed3058f1.htm) | (Inherited from  [ShapeBuilder](66c1678c-2e01-e0de-1386-5a0e1eb3ccff.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [Finish](4e7da30b-68cf-5572-39d1-979dffef8d5a.htm) | Complete construction of the geometry. The geometry will be validated and, if valid, stored in this Builder. Otherwise it will be deleted. |
| Public method | [FinishFace](2d5b2123-3d60-f87c-2f5f-b61fd2db62ce.htm) | Indicates that the caller has finished defining the given face. |
| Public method | [FinishLoop](cf38cd16-7b71-62d3-8c4f-56694125a4be.htm) | Indicates that the caller has finished defining the given loop. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetResult](b1cb34d1-a485-8926-f437-23edb67cdc32.htm) | Get the Geometry object built by this BRepBuilder. This will clear the built Geometry stored in the BRepBuilder. This function will throw if this BRepBuilder hasn't completed building the b-rep. Use IsResultAvailable() to verify that this BRepBuilder contains a valid result. |
| Public method | [GetResult(ExternalGeometryId, BRepBuilderPersistentIds)](b72c5abd-629e-96aa-0b87-95b5cc763f80.htm) | Get the Geometry object built by this BRepBuilder. This will clear the built Geometry stored in the BRepBuilder. This function will throw if this BRepBuilder hasn't completed building the b-rep. Use IsResultAvailable() to verify that this BRepBuilder contains a valid result. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method Static member | [IsPermittedSurfaceType](040692f6-8493-74dc-4d6c-8b8668a2fe27.htm) | A validator function that checks whether the surface object is of type supported as face surface by BRepBuilder. |
| Public method | [IsResultAvailable](e4316883-9ea0-b9a5-7cc5-3ba58d1c7418.htm) | A validator function that checks the state of this BRepBuilder object. Returns true if this BRepBuilder object has successfully built a b-rep. |
| Public method | [IsValidEdgeId](3572f388-f282-9c72-fdec-9147b2687638.htm) | A validator function that checks whether the edge id corresponds to an edge previously added to this BRepBuilder object. |
| Public method | [IsValidFaceId](476756cc-99d9-b891-9583-3fe7dff48c75.htm) | A validator function that checks whether the face id corresponds to a face previously added to this BRepBuilder object. |
| Public method | [IsValidLoopId](8688abac-8e16-f7f7-d6ad-e84d8620d503.htm) | A validator function that checks whether the loop id corresponds to a loop previously added to this BRepBuilder object. |
| Public method | [IsValidPersistentIdsMap](4169de01-5062-fd9c-024f-c7958fc85402.htm) | A validator function that makes sure that all BRepBuilderGeometryIds in the input map can be found in this BRepBuilder object. |
| Public method | [RemovedSomeFaces](e5cb0e49-8c1a-9bd0-7867-c6a18b2d258a.htm) | Returns 'true' if BRepBuilder removed some problematic faces from the output geometry, 'false' if not. If allowRemovalOfProblematicFaces was not called to enable removal of problematic faces, this function will return 'false'. Note that if some faces were removed, the output geometry's type will be OpenShell regardless of the expected type that was specified when the BRepBuilder was created. |
| Public method | [SetAllowShortEdges](2e0f0e48-a219-7abe-96c4-b755cb5b687b.htm) | Make BRepBuilder allow edges that it would normally disallow as being too short for Revit geometry. |
| Public method | [SetFaceMaterialId](8b7c7bed-57ef-a1e0-0fe2-529fe742e64a.htm) | Sets material id to a face. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](6a5c7474-6ea6-4886-d356-204405406596.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [ShapeBuilder](66c1678c-2e01-e0de-1386-5a0e1eb3ccff.htm)  .) |

# See Also

[BRepBuilder Class](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)