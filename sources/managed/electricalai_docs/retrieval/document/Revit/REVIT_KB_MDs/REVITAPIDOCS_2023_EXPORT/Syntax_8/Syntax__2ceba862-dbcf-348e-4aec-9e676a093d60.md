[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasInvalidData Property

---



|  |
| --- |
| [MeshFromGeometryOperationResult Class](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm)   [See Also](#seeAlsoToggle) |

Whether the provided data for which this result was obtained were internally inconsistent and could not be used in its entirety. For example, for extrusion operation, profile loops were degenerate or improperly oriented with respect to the extrsuion direction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool HasInvalidData { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HasInvalidData As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool HasInvalidData { 	bool get (); } ``` |

# Remarks

This variable does not capture presence or absence of intersections between different profile loops.

# See Also

[MeshFromGeometryOperationResult Class](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)