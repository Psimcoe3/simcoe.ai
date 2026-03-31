[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PrimaryBarOrientation Property

---



|  |
| --- |
| [PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)   [See Also](#seeAlsoToggle) |

Orientation of primary bars of Path Reinforcement.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public ReinforcementBarOrientation PrimaryBarOrientation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PrimaryBarOrientation As ReinforcementBarOrientation 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ReinforcementBarOrientation PrimaryBarOrientation { 	ReinforcementBarOrientation get (); 	void set (ReinforcementBarOrientation value); } ``` |

# Remarks

The orientation corresponds to the bars' rotation in the Path Reinforcement element. It indicates the postion of the major segment of the primary Rebar Shape relative to the edges of a rectangular region which bounds the Path Reinforcement, where the top/exterior and bottom/interior come from the cover boundaries of the host, the near side edge is defined by the Path Reinforcement sketch line, and the far side edge is derived from bar length (defaulting to 5').

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: This orientation is not allowed for primary bars. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)