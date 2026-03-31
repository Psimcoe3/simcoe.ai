[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSymbolTypeId Method

---



|  |
| --- |
| [FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)   [See Also](#seeAlsoToggle) |

Gets the identifier of the symbol indicating the unit quantifying the value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ForgeTypeId GetSymbolTypeId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSymbolTypeId As ForgeTypeId ``` |

 

| Visual C++ |
| --- |
| ``` public: ForgeTypeId^ GetSymbolTypeId() ``` |

#### Return Value

The symbol identifier. An empty identifier string indicates no symbol.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | UseDefault is true in this FormatOptions. |

# See Also

[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)