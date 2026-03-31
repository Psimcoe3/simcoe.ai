[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLayoutAsSingle Method

---



|  |
| --- |
| [RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)   [See Also](#seeAlsoToggle) |

Sets the Layout Rule property of rebar set to Single.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void SetLayoutAsSingle() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLayoutAsSingle ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLayoutAsSingle() ``` |

# Remarks

Only one bar will remain, which is at the position of rebar plane

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RebarShapeDrivenAccessor doesn't contain a valid rebar reference. |

# See Also

[RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)