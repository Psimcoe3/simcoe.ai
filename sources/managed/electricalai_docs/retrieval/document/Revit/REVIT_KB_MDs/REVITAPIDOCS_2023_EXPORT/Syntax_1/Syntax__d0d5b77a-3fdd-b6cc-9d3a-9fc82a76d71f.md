[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetSymbolTypeId Method

---



|  |
| --- |
| [FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)   [See Also](#seeAlsoToggle) |

Sets the symbol that should be displayed to indicate the unit quantifying the value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetSymbolTypeId( 	ForgeTypeId symbolTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetSymbolTypeId ( _ 	symbolTypeId As ForgeTypeId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetSymbolTypeId( 	ForgeTypeId^ symbolTypeId ) ``` |

#### Parameters

symbolTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     The symbol identifier. An empty identifier string indicates no symbol.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | symbolTypeId is not a valid symbol for the unit in this FormatOptions. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | UseDefault is true in this FormatOptions. |

# See Also

[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)