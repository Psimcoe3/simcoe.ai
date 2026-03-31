[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetHookOrientation Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Defines the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetHookOrientation( 	int iEnd, 	RebarHookOrientation hookOrientation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetHookOrientation ( _ 	iEnd As Integer, _ 	hookOrientation As RebarHookOrientation _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetHookOrientation( 	int iEnd,  	RebarHookOrientation hookOrientation ) ``` |

#### Parameters

iEnd
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     0 for the start hook, 1 for the end hook.

hookOrientation
:   Type:  [Autodesk.Revit.DB.Structure RebarHookOrientation](e8365754-0811-8d4e-864a-55bf34af3a87.htm)    
     Only two values are permitted: Value = Right: The hook is on your right as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up." Value = Left: The hook is on your left as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up."

# Remarks

If RebarShapeDefinesHooks property of ReinforcementSettings is true (non-European shapes), setHookOrientation method does nothing.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | iEnd must be 0 or 1. -or- A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)