[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetUnitTypeId Method

---



|  |
| --- |
| [Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)   [See Also](#seeAlsoToggle) |

Gets the identifier of the unit quantifying the parameter value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public ForgeTypeId GetUnitTypeId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetUnitTypeId As ForgeTypeId ``` |

 

| Visual C++ |
| --- |
| ``` public: ForgeTypeId^ GetUnitTypeId() ``` |

#### Return Value

Identifier of the unit of the parameter.

# Remarks

The property only applies to parameters of value types.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if this parameter is not of value type. |

# See Also

[Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)