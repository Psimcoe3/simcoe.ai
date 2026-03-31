[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementId Property

---



|  |
| --- |
| [LinkLoadResult Class](f846bfb0-b047-9332-567f-75ae880d8359.htm)   [See Also](#seeAlsoToggle) |

The id of the created or loaded linked model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId ElementId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ElementId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ElementId { 	ElementId^ get (); } ``` |

# Remarks

This may be invalidElementId if there were errors (for example, LinkLoadResultType.SameModelAsHost causes no link to be created).

# See Also

[LinkLoadResult Class](f846bfb0-b047-9332-567f-75ae880d8359.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)