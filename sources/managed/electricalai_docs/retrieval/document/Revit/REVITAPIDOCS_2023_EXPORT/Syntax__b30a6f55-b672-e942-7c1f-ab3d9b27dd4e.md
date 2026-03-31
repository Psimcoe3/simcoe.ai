[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetHookRotationAngle Method

---



|  |
| --- |
| [RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)   [See Also](#seeAlsoToggle) |

Sets the out of plane hook rotation angle at the specified end.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public void SetHookRotationAngle( 	double hookRotationAngle, 	int iEnd ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetHookRotationAngle ( _ 	hookRotationAngle As Double, _ 	iEnd As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetHookRotationAngle( 	double hookRotationAngle,  	int iEnd ) ``` |

#### Parameters

hookRotationAngle
:   Type:  System Double    
     The out of plane hook rotation angle at the specified end.

iEnd
:   Type:  System Int32    
     0 for the start , 1 for the end.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | iEnd must be 0 or 1. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)