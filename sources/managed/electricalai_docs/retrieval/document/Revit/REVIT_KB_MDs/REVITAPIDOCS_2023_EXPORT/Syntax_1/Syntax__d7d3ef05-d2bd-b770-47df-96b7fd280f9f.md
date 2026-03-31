[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEditable Property

---



|  |
| --- |
| [Family Class](f51d019d-6ff3-692b-d1d2-b497cab564de.htm)   [See Also](#seeAlsoToggle) |

True if the family supports editing, false otherwise.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsEditable { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsEditable As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsEditable { 	bool get (); } ``` |

# Remarks

The family will not be editable if it is in-place, not saveable, or represents the primary family inside a family document.

# See Also

[Family Class](f51d019d-6ff3-692b-d1d2-b497cab564de.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)