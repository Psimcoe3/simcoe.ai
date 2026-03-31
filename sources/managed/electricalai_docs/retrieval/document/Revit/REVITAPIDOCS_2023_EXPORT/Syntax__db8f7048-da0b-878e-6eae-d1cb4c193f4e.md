[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BaseFinishingTurns Property

---



|  |
| --- |
| [RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)   [See Also](#seeAlsoToggle) |

For a spiral, the number of finishing turns at the lower end of the spiral.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public int BaseFinishingTurns { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BaseFinishingTurns As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int BaseFinishingTurns { 	int get (); 	void set (int value); } ``` |

# Remarks

Applies only to instances where RebarShape.Definition is of type RebarShapeDefinitionByArc, and its Type property is equal to the value RebarShapeDefinitionByArcType.Spiral.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: turns must be between 0 and 100. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RebarContainerItem is not an instance of a spiral shape. |

# See Also

[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)