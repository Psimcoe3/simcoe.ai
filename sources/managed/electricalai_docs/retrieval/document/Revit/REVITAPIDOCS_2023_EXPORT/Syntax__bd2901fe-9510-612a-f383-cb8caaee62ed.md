[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMesh Method

---



|  |
| --- |
| [MeshFromGeometryOperationResult Class](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm)   [See Also](#seeAlsoToggle) |

This returns a valid mesh only for the first call. Later calls will throw an exception as the mesh is no longer valid in this object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public Mesh GetMesh() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMesh As Mesh ``` |

 

| Visual C++ |
| --- |
| ``` public: Mesh^ GetMesh() ``` |

#### Return Value

Mesh which built.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The Mesh has already been accessed by a previous GetMesh() call, and is no longer available for use. |

# See Also

[MeshFromGeometryOperationResult Class](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)