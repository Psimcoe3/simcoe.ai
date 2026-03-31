[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddFace Method

---



|  |
| --- |
| [BRepBuilder Class](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)   [See Also](#seeAlsoToggle) |

Creates an empty face in the geometry being built. Other BRepBuilder methods are used to add loops to the face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public BRepBuilderGeometryId AddFace( 	BRepBuilderSurfaceGeometry surfaceGeom, 	bool bFaceIsReversed ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddFace ( _ 	surfaceGeom As BRepBuilderSurfaceGeometry, _ 	bFaceIsReversed As Boolean _ ) As BRepBuilderGeometryId ``` |

 

| Visual C++ |
| --- |
| ``` public: BRepBuilderGeometryId^ AddFace( 	BRepBuilderSurfaceGeometry^ surfaceGeom,  	bool bFaceIsReversed ) ``` |

#### Parameters

surfaceGeom
:   Type:  [Autodesk.Revit.DB BRepBuilderSurfaceGeometry](c21d4101-cc15-1990-ee9f-994b487bf95d.htm)    
     The face's support surface.

bFaceIsReversed
:   Type:  System Boolean    
     True if the face's orientation is opposite to that of the surface, false if the orientations agree. The faces of each shell must be consistently oriented. For a solid (BRepType == Solid), the oriented face normals must point out of the solid; for a void (BRepType == Void), the face normals must point into the void. See the description of the bCoEdgeIsReversed input for AddCoEdge() for a discussion of the loop and co-edge orientation conventions to use with the BRepBuilder.

#### Return Value

An id that can be used to identify the face while the BRepBuilder is actively building geometry (e.g., to add a loop to a face).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This BRepBuilder object isn't accepting new data, either because it has already been used to build geometry, or because of an error. Consult the State property of the BRepBuilder object for more details. |

# See Also

[BRepBuilder Class](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)