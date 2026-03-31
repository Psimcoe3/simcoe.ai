[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCellSpec Method

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Gets the spec describing values of a cell, if applicable.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public ForgeTypeId GetCellSpec( 	int nRow, 	int nCol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCellSpec ( _ 	nRow As Integer, _ 	nCol As Integer _ ) As ForgeTypeId ``` |

 

| Visual C++ |
| --- |
| ``` public: ForgeTypeId^ GetCellSpec( 	int nRow,  	int nCol ) ``` |

#### Parameters

nRow
:   Type:  System Int32    
     The row index of the cell

nCol
:   Type:  System Int32    
     The column index of the cell

#### Return Value

Identifier of the spec, or empty if the cell does not contain a number with units.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given row number nRow is invalid. -or- The given column number nCol is invalid. |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)