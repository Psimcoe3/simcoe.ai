[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetNamingRule Method

---



|  |
| --- |
| [PDFExportOptions Class](e4236fc8-f8e7-fc74-1b81-9e3a4d9e966b.htm)   [See Also](#seeAlsoToggle) |

Sets the naming rule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void SetNamingRule( 	IList<TableCellCombinedParameterData> namingRule ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetNamingRule ( _ 	namingRule As IList(Of TableCellCombinedParameterData) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetNamingRule( 	IList<TableCellCombinedParameterData^>^ namingRule ) ``` |

#### Parameters

namingRule
:   Type:  System.Collections.Generic IList   [TableCellCombinedParameterData](f2303148-6e5e-d143-3725-3ac12c04ea86.htm)    
     The naming rule.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The namingRule is empty or contains illegal characters. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PDFExportOptions Class](e4236fc8-f8e7-fc74-1b81-9e3a4d9e966b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)