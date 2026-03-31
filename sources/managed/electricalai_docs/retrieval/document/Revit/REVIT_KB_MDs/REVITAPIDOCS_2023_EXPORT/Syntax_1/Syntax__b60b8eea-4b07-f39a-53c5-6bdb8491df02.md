[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Add Method

---



|  |
| --- |
| [ExportFontTable Class](b3b4f237-f7f3-ced4-be3d-721f7ac05832.htm)   [See Also](#seeAlsoToggle) |

Inserts a (key,info) pair into Export font table.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Add( 	ExportFontKey exportFontKey, 	ExportFontInfo exportFontInfo ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Add ( _ 	exportFontKey As ExportFontKey, _ 	exportFontInfo As ExportFontInfo _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Add( 	ExportFontKey^ exportFontKey,  	ExportFontInfo^ exportFontInfo ) ``` |

#### Parameters

exportFontKey
:   Type:  [Autodesk.Revit.DB ExportFontKey](bd33456d-7898-f32c-312e-b94af14c0007.htm)    
     The export font key to be added.

exportFontInfo
:   Type:  [Autodesk.Revit.DB ExportFontInfo](c3dc100c-0e4d-419d-5cbd-1d59f149490c.htm)    
     The export font info to be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The key already exists in the table. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportFontTable Class](b3b4f237-f7f3-ced4-be3d-721f7ac05832.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)