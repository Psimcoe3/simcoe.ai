[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Voltage Property

---



|  |
| --- |
| [AnalyticalPowerSourceData Class](844cf629-c023-47a8-55f1-b1d702780658.htm)   [See Also](#seeAlsoToggle) |

The voltage value of the analytical power source.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public double Voltage { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Voltage As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Voltage { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for voltage is not a number -or- When setting this property: The given value for voltage is not finite |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for voltage must be positive. |

# See Also

[AnalyticalPowerSourceData Class](844cf629-c023-47a8-55f1-b1d702780658.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)