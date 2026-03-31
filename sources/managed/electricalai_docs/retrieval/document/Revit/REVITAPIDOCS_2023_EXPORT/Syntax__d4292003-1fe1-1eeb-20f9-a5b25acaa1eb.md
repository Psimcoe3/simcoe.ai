[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TopElevation Property

---



|  |
| --- |
| [StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm)   [See Also](#seeAlsoToggle) |

The top elevation of the stairs run.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double TopElevation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property TopElevation As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double TopElevation { 	double get (); 	void set (double value); } ``` |

# Remarks

The top elevation has following restrictions:

* The top elevation is relative to the base elevation of the stairs to which the stairs run belongs.
* When setting this property the value will be rounded automatically to a multiple of the riser height.
* When setting this property for common run, the run's height will change according to the new base/top elevation. So the value must be greater than base elevation to keep run valid.
* When setting this property for sketched run, whose height is fixed, the run's base elevation will be adjusted to keep the same run height.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for topElevation must be no more than 30000 feet in absolute value. -or- When setting this property: The topElevation doesn't meet the minimal height restriction of the stairs run. -or- When setting this property: The topElevation is less than the extension below base of the stairs run. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The stairs run is sketched so the data being set is not applicable. |

# See Also

[StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)