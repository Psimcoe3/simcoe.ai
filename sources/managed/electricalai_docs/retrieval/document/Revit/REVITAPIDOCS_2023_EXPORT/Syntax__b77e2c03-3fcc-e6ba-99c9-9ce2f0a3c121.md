[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SegmentLengthRoundingMethod Property

---



|  |
| --- |
| [RebarRoundingManager Class](db93e1af-7588-f7f9-b505-490979327dac.htm)   [See Also](#seeAlsoToggle) |

Identifies the segment length rounding method

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public RoundingMethod SegmentLengthRoundingMethod { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SegmentLengthRoundingMethod As RoundingMethod 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property RoundingMethod SegmentLengthRoundingMethod { 	RoundingMethod get (); 	void set (RoundingMethod value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: IsActiveOnElement property is false. |

# See Also

[RebarRoundingManager Class](db93e1af-7588-f7f9-b505-490979327dac.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)