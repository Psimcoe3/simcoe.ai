[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Rating Property

---



|  |
| --- |
| [ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)   [See Also](#seeAlsoToggle) |

The Rating value of the Electrical System.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public double Rating { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Rating As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Rating { 	double get (); 	void set (double value); } ``` |

# Remarks

This property is used to retrieve the Rating value of the Electrical System.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for rating is not a number -or- When setting this property: The given value for rating is not finite |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for rating must be non-negative. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Mechanical Electrical Piping. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This property only available when System Type is Power! |

# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)