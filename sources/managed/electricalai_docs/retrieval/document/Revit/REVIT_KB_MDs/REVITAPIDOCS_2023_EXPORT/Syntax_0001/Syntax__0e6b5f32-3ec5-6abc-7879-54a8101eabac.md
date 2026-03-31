[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Flux Property

---



|  |
| --- |
| [InitialFluxIntensity Class](9c36e906-74c5-adc1-d147-42f65f0c9613.htm)   [See Also](#seeAlsoToggle) |

The flux intensity value.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double Flux { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Flux As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Flux { 	double get (); 	void set (double value); } ``` |

#### Field Value

The flux value in lm as a numerical value between 0 and 1e+30.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The flux intensity value is not valid because it is not between 0 and 1e+30. |

# See Also

[InitialFluxIntensity Class](9c36e906-74c5-adc1-d147-42f65f0c9613.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)