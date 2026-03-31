[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetCellType Method (Int32, Int32, CellType)

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Sets a cell's Type

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetCellType( 	int nRow, 	int nCol, 	CellType type ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetCellType ( _ 	nRow As Integer, _ 	nCol As Integer, _ 	type As CellType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetCellType( 	int nRow,  	int nCol,  	CellType type ) ``` |

#### Parameters

nRow
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

nCol
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

type
:   Type:  [Autodesk.Revit.DB CellType](8eaa9e7d-b5ba-6693-f9ac-ee57e789e280.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given row number nRow is invalid. -or- The given column number nCol is invalid. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation is forbidden for cells in standard schedule body sections. |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[SetCellType Overload](8fab3a52-4dad-3414-6698-df7ebc227681.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)