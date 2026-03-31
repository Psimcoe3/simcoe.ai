[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UserModifiable Property

---



|  |
| --- |
| [FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the interactive user can modify the value of this parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool UserModifiable { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property UserModifiable As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool UserModifiable { 	bool get (); } ``` |

# Remarks

Note that for shared parameters IsReadOnly can return false for shared parameters whose UserModifiable property is also false, because the value of those parameters can be modified by the API. If a parameter is governed by a formula, IsReadOnly would return true, even if the flag for UserModifiable was set to true when the shared parameter was created.

# See Also

[FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)