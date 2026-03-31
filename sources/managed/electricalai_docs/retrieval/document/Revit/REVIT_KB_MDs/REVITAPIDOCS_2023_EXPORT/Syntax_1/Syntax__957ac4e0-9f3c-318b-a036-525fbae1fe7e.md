[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportColor Property

---



|  |
| --- |
| [STLExportOptions Class](c8870dfe-9259-4981-4545-a6c0d0440552.htm)   [See Also](#seeAlsoToggle) |

True to export color information, false otherwise. Default value is false.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public bool ExportColor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExportColor As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ExportColor { 	bool get (); 	void set (bool value); } ``` |

# Remarks

Color information can be exported only in binary STL format, in the case of ASCII STL format this property will be ignored.

# See Also

[STLExportOptions Class](c8870dfe-9259-4981-4545-a6c0d0440552.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)