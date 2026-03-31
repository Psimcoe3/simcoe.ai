[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsActive Property

---



|  |
| --- |
| [EditScope Class](bac11282-3a3b-953e-8bc4-960c62da4946.htm)   [See Also](#seeAlsoToggle) |

Tells if the EditScope is active. In other words, the EditScope has started but not committed/canceled yet.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsActive { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsActive As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsActive { 	bool get (); } ``` |

# Remarks

Starting the edit scope is not permitted when it is active. Canceling/committing is not allowed when the edit scope is not active.

# See Also

[EditScope Class](bac11282-3a3b-953e-8bc4-960c62da4946.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)