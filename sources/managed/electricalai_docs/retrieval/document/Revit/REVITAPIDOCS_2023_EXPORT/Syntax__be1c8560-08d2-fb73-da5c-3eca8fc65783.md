[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAcceptableParamIdAndCategoryId Method (Int32, ElementId, ElementId)

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Identifies if the given parameter id and category id can be assigned to a cell in the given row in this table.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsAcceptableParamIdAndCategoryId( 	int nRow, 	ElementId paramId, 	ElementId categoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsAcceptableParamIdAndCategoryId ( _ 	nRow As Integer, _ 	paramId As ElementId, _ 	categoryId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsAcceptableParamIdAndCategoryId( 	int nRow,  	ElementId^ paramId,  	ElementId^ categoryId ) ``` |

#### Parameters

nRow
:   Type:  System Int32    
     row index

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

categoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

#### Return Value

True if the ParamId and CategoryId are all valid.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given row number nRow is invalid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[IsAcceptableParamIdAndCategoryId Overload](c49add8b-f5b4-93a7-ec26-1125c56c90cf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)