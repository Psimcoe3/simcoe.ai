[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LocallyUnloaded Property

---



|  |
| --- |
| [RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)   [See Also](#seeAlsoToggle) |

Checks whether a Revit link in a local model is unloaded only for the current user.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool LocallyUnloaded { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property LocallyUnloaded As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool LocallyUnloaded { 	bool get (); } ``` |

# Remarks

Revit links can be unloaded for both the current user and for all users. If a Revit link is in a non-workshared file or in central model, this property is false.

# See Also

[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)