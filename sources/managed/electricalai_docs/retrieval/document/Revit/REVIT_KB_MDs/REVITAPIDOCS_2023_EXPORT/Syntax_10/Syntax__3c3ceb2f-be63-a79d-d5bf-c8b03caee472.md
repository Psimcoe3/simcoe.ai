[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Efficacy Property

---



|  |
| --- |
| [InitialWattageIntensity Class](2bcbaf81-375c-2732-d67a-563d8302cd1e.htm)   [See Also](#seeAlsoToggle) |

The efficacy value.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double Efficacy { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Efficacy As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Efficacy { 	double get (); 	void set (double value); } ``` |

#### Field Value

The efficacy value in lm/W as a numerical value greater than 0.0 and less than 1.0e+10.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The efficacy value is not valid because it is not between 0 and 1e+30. |

# See Also

[InitialWattageIntensity Class](2bcbaf81-375c-2732-d67a-563d8302cd1e.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)