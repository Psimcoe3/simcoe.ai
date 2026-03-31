[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetExportFontInfo Method

---



|  |
| --- |
| [ExportFontTable Class](b3b4f237-f7f3-ced4-be3d-721f7ac05832.htm)   [See Also](#seeAlsoToggle) |

Gets a copy of the font info associated to the input font key.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ExportFontInfo GetExportFontInfo( 	ExportFontKey exportFontKey ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetExportFontInfo ( _ 	exportFontKey As ExportFontKey _ ) As ExportFontInfo ``` |

 

| Visual C++ |
| --- |
| ``` public: ExportFontInfo^ GetExportFontInfo( 	ExportFontKey^ exportFontKey ) ``` |

#### Parameters

exportFontKey
:   Type:  [Autodesk.Revit.DB ExportFontKey](bd33456d-7898-f32c-312e-b94af14c0007.htm)    
     The export font Key.

#### Return Value

Returns the fontInfo for this key.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | An entry with the given key is not present in the table. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportFontTable Class](b3b4f237-f7f3-ced4-be3d-721f7ac05832.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)