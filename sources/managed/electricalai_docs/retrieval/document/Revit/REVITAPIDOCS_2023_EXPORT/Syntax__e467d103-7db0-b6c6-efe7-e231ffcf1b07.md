[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsTransparentIn3D Property

---



|  |
| --- |
| [Opening Class](720de864-9f4e-c606-c7f4-2e7a0b2da46f.htm)   [See Also](#seeAlsoToggle) |

Indicates if the opening is transparent in 3D view when loaded into the project.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsTransparentIn3D { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsTransparentIn3D As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsTransparentIn3D { 	bool get (); 	void set (bool value); } ``` |

# Remarks

This property is only valid in Revit family documents.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when access this property in an opening belonging to a Revit project document. |

# See Also

[Opening Class](720de864-9f4e-c606-c7f4-2e7a0b2da46f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)