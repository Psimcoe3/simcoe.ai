[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsGreaterThan Method

---



|  |
| --- |
| [MathComparisonUtils Class](ddb32a4c-b742-0286-36b5-e5f2ce0d1daf.htm)   [See Also](#seeAlsoToggle) |

Checks if value1 is strictly greater than value2, using the internal tolerance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static bool IsGreaterThan( 	double value1, 	double value2 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsGreaterThan ( _ 	value1 As Double, _ 	value2 As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsGreaterThan( 	double value1,  	double value2 ) ``` |

#### Parameters

value1
:   Type:  System Double    
     The first value.

value2
:   Type:  System Double    
     The second value.

#### Return Value

True if value1 is strictly greater than value2, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for value1 is not finite -or- The given value for value2 is not finite |

# See Also

[MathComparisonUtils Class](ddb32a4c-b742-0286-36b5-e5f2ce0d1daf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)