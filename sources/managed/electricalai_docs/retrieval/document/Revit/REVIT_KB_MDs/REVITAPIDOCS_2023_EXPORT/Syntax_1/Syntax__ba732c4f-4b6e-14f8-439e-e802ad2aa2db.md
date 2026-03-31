[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCellCombinedParameters Method (Int32, Int32)

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Returns an array of combined parameter data for the specified cell

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IList<TableCellCombinedParameterData> GetCellCombinedParameters( 	int nRow, 	int nCol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCellCombinedParameters ( _ 	nRow As Integer, _ 	nCol As Integer _ ) As IList(Of TableCellCombinedParameterData) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<TableCellCombinedParameterData^>^ GetCellCombinedParameters( 	int nRow,  	int nCol ) ``` |

#### Parameters

nRow
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

nCol
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given row number nRow is invalid. -or- The given column number nCol is invalid. |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[GetCellCombinedParameters Overload](88da4041-cbf5-8bc9-3d9b-21c3cdeb8b2b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)