[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDoubleOverrideValue Method

---



|  |
| --- |
| [RebarContainerParameterManager Class](a0e5db38-c482-7232-df45-b0cdbcebac7d.htm)   [See Also](#seeAlsoToggle) |

Get the double value for an overriden parameter.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public double GetDoubleOverrideValue( 	ElementId paramId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDoubleOverrideValue ( _ 	paramId As ElementId _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetDoubleOverrideValue( 	ElementId^ paramId ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the parameter

#### Return Value

The override value of the parameter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId is not the id of a parameter in the current document, or its value type is not double. -or- paramId is not a Rebar Container parameter -or- paramId has no override |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarContainerParameterManager Class](a0e5db38-c482-7232-df45-b0cdbcebac7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)