[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidSymbol Method (ForgeTypeId)

---



|  |
| --- |
| [FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)   [See Also](#seeAlsoToggle) |

Checks whether a symbol is valid for the unit in this FormatOptions.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsValidSymbol( 	ForgeTypeId symbolTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidSymbol ( _ 	symbolTypeId As ForgeTypeId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidSymbol( 	ForgeTypeId^ symbolTypeId ) ``` |

#### Parameters

symbolTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     Identifier of the symbol to check.

#### Return Value

True if the symbol is valid, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | UseDefault is true in this FormatOptions. |

# See Also

[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)

[IsValidSymbol Overload](a965e857-57c6-25cb-1622-f2d80425e999.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)