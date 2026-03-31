[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetCellFormatOptions Method

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Sets a cell's FormatOptions.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetCellFormatOptions( 	int nRow, 	int nCol, 	FormatOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetCellFormatOptions ( _ 	nRow As Integer, _ 	nCol As Integer, _ 	options As FormatOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetCellFormatOptions( 	int nRow,  	int nCol,  	FormatOptions^ options ) ``` |

#### Parameters

nRow
:   Type:  System Int32    
     The row index of the cell

nCol
:   Type:  System Int32    
     The column index of the cell

options
:   Type:  [Autodesk.Revit.DB FormatOptions](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)    
     The format option to assign

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given row number nRow is invalid. -or- The given column number nCol is invalid. -or- The display unit in options is not a valid display unit for the unit type of the cell, or the rounding method in options is not set to Nearest. See UnitUtils.IsValidDisplayUnit(UnitType, DisplayUnitType), UnitUtils.GetValidDisplayUnits(UnitType) and FormatOptions.RoundingMethod. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)