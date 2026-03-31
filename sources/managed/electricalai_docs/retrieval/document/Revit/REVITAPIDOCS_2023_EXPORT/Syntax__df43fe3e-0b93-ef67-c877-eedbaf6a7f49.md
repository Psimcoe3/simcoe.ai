[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidParameterDefinitionId Method

---



|  |
| --- |
| [ColorFillScheme Class](c405eb5b-14fa-0fea-a750-dcd9925a90b0.htm)   [See Also](#seeAlsoToggle) |

Checks whether the input parameter id can be applied to the scheme.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public bool IsValidParameterDefinitionId( 	ElementId parameterId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidParameterDefinitionId ( _ 	parameterId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidParameterDefinitionId( 	ElementId^ parameterId ) ``` |

#### Parameters

parameterId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

#### Return Value

Returns true if the input parameter id can be set to this scheme, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ColorFillScheme Class](c405eb5b-14fa-0fea-a750-dcd9925a90b0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)