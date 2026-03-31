[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HostStructuralRebar Property

---



|  |
| --- |
| [ReinforcementSettings Class](ca904bb8-c5f4-26bb-6220-9f8d5d1ebd1f.htm)   [See Also](#seeAlsoToggle) |

Host Structural Rebar within Area and Path Reinforcement with touching AtomHostStructuralRebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool HostStructuralRebar { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property HostStructuralRebar As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool HostStructuralRebar { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: Cannot change the RebarShapeDefinesHooks property in these settings because the document contains one or more AreaReinforcement or PathReinforcement elements. |

# See Also

[ReinforcementSettings Class](ca904bb8-c5f4-26bb-6220-9f8d5d1ebd1f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)