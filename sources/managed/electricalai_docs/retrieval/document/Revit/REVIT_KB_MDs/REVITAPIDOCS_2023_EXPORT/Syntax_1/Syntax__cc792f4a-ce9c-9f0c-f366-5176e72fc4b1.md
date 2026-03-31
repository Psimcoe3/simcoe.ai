[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MergeCells Method

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Merges cells for the given area.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void MergeCells( 	TableMergedCell mergedCell ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub MergeCells ( _ 	mergedCell As TableMergedCell _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void MergeCells( 	TableMergedCell^ mergedCell ) ``` |

#### Parameters

mergedCell
:   Type:  [Autodesk.Revit.DB TableMergedCell](f13b08fa-b8f9-a637-da3d-e9688e6fc041.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given TableMergedCell mergedCell is outside of acceptable range. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation is forbidden for cells in standard schedule body sections. |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)