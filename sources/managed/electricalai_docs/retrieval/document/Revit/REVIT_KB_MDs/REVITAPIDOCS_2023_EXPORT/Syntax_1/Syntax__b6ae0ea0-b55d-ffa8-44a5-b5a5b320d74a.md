[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IgnoreExtensibleStorageSchemaConflict Property

---



|  |
| --- |
| [OpenOptions Class](c0004971-3810-eeb8-72bd-e116886ec3c8.htm)   [See Also](#seeAlsoToggle) |

Specifies whether to ignore the error of schema conflict.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public bool IgnoreExtensibleStorageSchemaConflict { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IgnoreExtensibleStorageSchemaConflict As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IgnoreExtensibleStorageSchemaConflict { 	bool get (); 	void set (bool value); } ``` |

# Remarks

The default is false. Setting this to true will ignore the exception of schema conflict while opening the model. Data in the existing schema with the same ID will be erased from the model.

# See Also

[OpenOptions Class](c0004971-3810-eeb8-72bd-e116886ec3c8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)