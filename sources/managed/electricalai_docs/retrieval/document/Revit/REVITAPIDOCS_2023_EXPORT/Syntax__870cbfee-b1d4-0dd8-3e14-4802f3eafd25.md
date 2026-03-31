[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetReinforcementSettings Method

---



|  |
| --- |
| [ReinforcementSettings Class](ca904bb8-c5f4-26bb-6220-9f8d5d1ebd1f.htm)   [See Also](#seeAlsoToggle) |

Obtains the ReinforcementSettings object for the specified project document.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ReinforcementSettings GetReinforcementSettings( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetReinforcementSettings ( _ 	document As Document _ ) As ReinforcementSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: static ReinforcementSettings^ GetReinforcementSettings( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     A project document.

#### Return Value

The ReinforcementSettings object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[ReinforcementSettings Class](ca904bb8-c5f4-26bb-6220-9f8d5d1ebd1f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)