[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetParameterValue Method

---



|  |
| --- |
| [Subelement Class](2d15bb45-70af-5f84-e899-322742591251.htm)   [See Also](#seeAlsoToggle) |

Obtains the current parameter value of this subelement given a parameter id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public ParameterValue GetParameterValue( 	ElementId parameterId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetParameterValue ( _ 	parameterId As ElementId _ ) As ParameterValue ``` |

 

| Visual C++ |
| --- |
| ``` public: ParameterValue^ GetParameterValue( 	ElementId^ parameterId ) ``` |

#### Parameters

parameterId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Parameter id.

#### Return Value

Parameter value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | parameterId does not identify a valid parameter of this subelement. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Subelement Class](2d15bb45-70af-5f84-e899-322742591251.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)