[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCellCalculatedValue Method (Int32)

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Gets the calculated value for the specified column

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public TableCellCalculatedValueData GetCellCalculatedValue( 	int nCol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCellCalculatedValue ( _ 	nCol As Integer _ ) As TableCellCalculatedValueData ``` |

 

| Visual C++ |
| --- |
| ``` public: TableCellCalculatedValueData^ GetCellCalculatedValue( 	int nCol ) ``` |

#### Parameters

nCol
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given column number nCol is invalid. |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[GetCellCalculatedValue Overload](61835ee6-0ae1-c0a5-d29b-a08f866bbd53.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)