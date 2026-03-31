[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetNormal Method

---



|  |
| --- |
| [Mesh Class](bf9cd59c-03c3-9e7f-1e2b-6aaf5c425b69.htm)   [See Also](#seeAlsoToggle) |

Returns a normal unit vector at the given index.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public XYZ GetNormal( 	int idx ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetNormal ( _ 	idx As Integer _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetNormal( 	int idx ) ``` |

#### Parameters

idx
:   Type:  System Int32    
     A zero-based index. It must be consistent with the DistributionOfNormals.

#### Return Value

XYZ value representing a normal unit vector.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value is not a valid index of a normal of the mesh. A valid value is not negative and is smaller than the number of normals in the mesh. |

# See Also

[Mesh Class](bf9cd59c-03c3-9e7f-1e2b-6aaf5c425b69.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)