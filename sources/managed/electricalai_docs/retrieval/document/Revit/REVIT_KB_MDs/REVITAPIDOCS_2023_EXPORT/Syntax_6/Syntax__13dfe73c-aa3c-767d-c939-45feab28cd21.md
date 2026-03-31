[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetOverriddenParameterReadonly Method

---



|  |
| --- |
| [RebarContainerParameterManager Class](a0e5db38-c482-7232-df45-b0cdbcebac7d.htm)   [See Also](#seeAlsoToggle) |

Sets this overridden parameter to be readonly.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void SetOverriddenParameterReadonly( 	ElementId paramId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetOverriddenParameterReadonly ( _ 	paramId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetOverriddenParameterReadonly( 	ElementId^ paramId ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Overridden parameter id

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId has no override |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarContainerParameterManager Class](a0e5db38-c482-7232-df45-b0cdbcebac7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)