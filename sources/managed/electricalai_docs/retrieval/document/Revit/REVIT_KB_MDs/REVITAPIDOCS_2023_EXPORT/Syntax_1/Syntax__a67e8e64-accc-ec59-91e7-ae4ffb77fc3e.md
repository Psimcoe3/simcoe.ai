[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RotationZ Property

---



|  |
| --- |
| [AnalyticalLinkType Class](9362135d-6ea6-ff5a-e026-b6c247a497a1.htm)   [See Also](#seeAlsoToggle) |

Fixity of rotation around Z.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public AnalyticalFixityState RotationZ { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RotationZ As AnalyticalFixityState 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property AnalyticalFixityState RotationZ { 	AnalyticalFixityState get (); 	void set (AnalyticalFixityState value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The fixity state rotationZ is not valid for Analytical Link Type parameters. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[AnalyticalLinkType Class](9362135d-6ea6-ff5a-e026-b6c247a497a1.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)