[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsRectBoundary Property

---



|  |
| --- |
| [Opening Class](720de864-9f4e-c606-c7f4-2e7a0b2da46f.htm)   [See Also](#seeAlsoToggle) |

Retrieves the information whether the opening has a rectangular boundary.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsRectBoundary { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsRectBoundary As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsRectBoundary { 	bool get (); } ``` |

# Remarks

If the opening has a rectangular boundary, we can get the geometry information from BoundaryRect property. Otherwise we should get the geometry information from BoundaryCurves property.

# See Also

[Opening Class](720de864-9f4e-c606-c7f4-2e7a0b2da46f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)