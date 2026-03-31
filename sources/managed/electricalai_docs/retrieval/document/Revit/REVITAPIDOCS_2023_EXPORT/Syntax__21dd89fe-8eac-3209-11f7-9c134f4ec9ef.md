[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetAutoCalcHookLengths Method

---



|  |
| --- |
| [RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)   [See Also](#seeAlsoToggle) |

Identifies if the hook lengths of a hook type are automatically calculated for this bar type

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetAutoCalcHookLengths( 	ElementId hookId, 	bool autoCalculated ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetAutoCalcHookLengths ( _ 	hookId As ElementId, _ 	autoCalculated As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetAutoCalcHookLengths( 	ElementId^ hookId,  	bool autoCalculated ) ``` |

#### Parameters

hookId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     id of the hook type

autoCalculated
:   Type:  System Boolean    
     True if the hook lengths should be automatically calculated, otherwise false When it is false, default hook length and default hook offset length will be reported

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)