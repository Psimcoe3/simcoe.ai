[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetCellParamIdAndCategoryId Method (Int32, ElementId, ElementId)

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Sets a column's category and parameter Id

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetCellParamIdAndCategoryId( 	int nCol, 	ElementId paramId, 	ElementId categoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetCellParamIdAndCategoryId ( _ 	nCol As Integer, _ 	paramId As ElementId, _ 	categoryId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetCellParamIdAndCategoryId( 	int nCol,  	ElementId^ paramId,  	ElementId^ categoryId ) ``` |

#### Parameters

nCol
:   Type:  System Int32

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

categoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given column number nCol is invalid. -or- The paramId or categoryId is not acceptable. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation is forbidden for cells in standard schedule body sections. |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[SetCellParamIdAndCategoryId Overload](0195eb8d-b061-f29a-05cb-0c4eca0cf5c0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)