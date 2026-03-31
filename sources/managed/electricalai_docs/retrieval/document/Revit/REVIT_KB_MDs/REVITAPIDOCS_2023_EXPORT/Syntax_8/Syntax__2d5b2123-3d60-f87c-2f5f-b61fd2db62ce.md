[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FinishFace Method

---



|  |
| --- |
| [BRepBuilder Class](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)   [See Also](#seeAlsoToggle) |

Indicates that the caller has finished defining the given face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void FinishFace( 	BRepBuilderGeometryId faceId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub FinishFace ( _ 	faceId As BRepBuilderGeometryId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void FinishFace( 	BRepBuilderGeometryId^ faceId ) ``` |

#### Parameters

faceId
:   Type:  [Autodesk.Revit.DB BRepBuilderGeometryId](f7d0b679-926a-9f1d-8f2a-dda9c2f3fe7a.htm)    
     Id of the face.

# Remarks

No functions that modify the given face's definition should be called after calling this function (e.g.,  [AddLoop(BRepBuilderGeometryId)](169a75b9-2b82-09ec-a6f1-a9b82e8f32fe.htm)  ,  [SetFaceMaterialId(BRepBuilderGeometryId, ElementId)](8b7c7bed-57ef-a1e0-0fe2-529fe742e64a.htm)  ). The BRepBuilder may take the opportunity to validate some of the face's data and report any problems it finds.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The supplied face id doesn't correspond to a face stored in this BRepBuilder object. -or- FinishFace() has already been called on faceId. -or- The face has no edge loops. -or- FinishLoop() must be called on all the edge loops of faceId. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[BRepBuilder Class](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)