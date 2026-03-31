[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WorkshopInstructions Property

---



|  |
| --- |
| [RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)   [See Also](#seeAlsoToggle) |

Identifies the workshop instructions of the current Rebar element.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public RebarWorkInstructions WorkshopInstructions { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property WorkshopInstructions As RebarWorkInstructions 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property RebarWorkInstructions WorkshopInstructions { 	RebarWorkInstructions get (); 	void set (RebarWorkInstructions value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)