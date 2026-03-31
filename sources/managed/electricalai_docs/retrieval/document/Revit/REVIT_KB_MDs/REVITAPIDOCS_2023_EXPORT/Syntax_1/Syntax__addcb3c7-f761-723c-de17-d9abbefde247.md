[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsPermitted Property

---



|  |
| --- |
| [EditScope Class](bac11282-3a3b-953e-8bc4-960c62da4946.htm)   [See Also](#seeAlsoToggle) |

Tells if the edit scope is permitted to start.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsPermitted { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsPermitted As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsPermitted { 	bool get (); } ``` |

# Remarks

The edit scope is not permitted to start for one of the following possible reasons: The document is in read-only state, or the document is currently modifiable, or there already is another edit mode active in the document.

# See Also

[EditScope Class](bac11282-3a3b-953e-8bc4-960c62da4946.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)