[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveTemperature Method

---



|  |
| --- |
| [FluidType Class](6de7a895-6747-7273-55cf-19f917a30c84.htm)   [See Also](#seeAlsoToggle) |

Removes a fluid temperature via the temperature value from the set.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void RemoveTemperature( 	double temperature ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveTemperature ( _ 	temperature As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveTemperature( 	double temperature ) ``` |

#### Parameters

temperature
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The temperature value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the temperature that will be removed doesn't exist in the fluid type or the temperature that will be removed is in use. |

# See Also

[FluidType Class](6de7a895-6747-7273-55cf-19f917a30c84.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)