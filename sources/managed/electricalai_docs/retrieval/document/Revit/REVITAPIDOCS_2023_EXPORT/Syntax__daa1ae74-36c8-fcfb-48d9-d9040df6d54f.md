[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetEndParameter Method

---



|  |
| --- |
| [CurveUV Class](2d1d9c1f-afb6-fc09-f461-54cf0d511bf0.htm)   [See Also](#seeAlsoToggle) |

Gets the raw parameter value at the start or end of this curve.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public double GetEndParameter( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetEndParameter ( _ 	index As Integer _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetEndParameter( 	int index ) ``` |

#### Parameters

index
:   Type:  System Int32    
     Use 0 for the start parameter, 1 for the end parameter of the curve.

#### Return Value

The raw parameter value at the start or end of this curve.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for index is not 0 or 1. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This curve is unbound and does not have start and end points. |

# See Also

[CurveUV Class](2d1d9c1f-afb6-fc09-f461-54cf0d511bf0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)