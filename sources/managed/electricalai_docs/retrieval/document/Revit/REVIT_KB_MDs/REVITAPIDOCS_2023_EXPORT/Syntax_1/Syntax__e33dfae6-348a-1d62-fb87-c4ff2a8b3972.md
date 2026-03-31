[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsClosed Property

---



|  |
| --- |
| [Mesh Class](bf9cd59c-03c3-9e7f-1e2b-6aaf5c425b69.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the mesh is closed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public bool IsClosed { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsClosed As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsClosed { 	bool get (); } ``` |

# Remarks

Every time this property is accessed, it is computed from scratch, so accessing it multiple times will come at a performance cost. A mesh is closed when each of its edges has two (or more) faces. If an edge has more than two faces (meaning that it's a non-manifold edge), the mesh still may be closed.

# See Also

[Mesh Class](bf9cd59c-03c3-9e7f-1e2b-6aaf5c425b69.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)