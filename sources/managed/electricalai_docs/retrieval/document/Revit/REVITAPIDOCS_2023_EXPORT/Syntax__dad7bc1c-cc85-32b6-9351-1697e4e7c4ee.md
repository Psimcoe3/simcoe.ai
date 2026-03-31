[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InitialWattageIntensity Constructor (Double, Double)

---



|  |
| --- |
| [InitialWattageIntensity Class](2bcbaf81-375c-2732-d67a-563d8302cd1e.htm)   [See Also](#seeAlsoToggle) |

Creates an initial wattage intensity object with the given values.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public InitialWattageIntensity( 	double efficacy, 	double wattage ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	efficacy As Double, _ 	wattage As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: InitialWattageIntensity( 	double efficacy,  	double wattage ) ``` |

#### Parameters

efficacy
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The universal unit efficacy value as a numerical value between 0 and 1e+30.

wattage
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The universal unit wattage value as a numerical value between 0 and 1e+30.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The efficacy value is not valid because it is not between 0 and 1e+30. -or- The wattage value is not valid because it is not between 0 and 1e+30. |

# See Also

[InitialWattageIntensity Class](2bcbaf81-375c-2732-d67a-563d8302cd1e.htm)

[InitialWattageIntensity Overload](988d7ac2-7d51-e92d-f670-c7505a6d2878.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)