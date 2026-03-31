[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFaceMaterialId Method

---



|  |
| --- |
| [BRepBuilder Class](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)   [See Also](#seeAlsoToggle) |

Sets material id to a face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void SetFaceMaterialId( 	BRepBuilderGeometryId faceId, 	ElementId materialId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFaceMaterialId ( _ 	faceId As BRepBuilderGeometryId, _ 	materialId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFaceMaterialId( 	BRepBuilderGeometryId^ faceId,  	ElementId^ materialId ) ``` |

#### Parameters

faceId
:   Type:  [Autodesk.Revit.DB BRepBuilderGeometryId](f7d0b679-926a-9f1d-8f2a-dda9c2f3fe7a.htm)    
     Id of the face to which material id will be added. faceId was returned by a call to AddFace().

materialId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The material id associated with the face, or invalidElementId if none. It is not verified that materialId corresponds to a valid Material element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The supplied face id doesn't correspond to a face stored in this BRepBuilder object. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This BRepBuilder object isn't accepting new data, either because it has already been used to build geometry, or because of an error. Consult the State property of the BRepBuilder object for more details. |

# See Also

[BRepBuilder Class](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)