[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VaporPressure Property

---



|  |
| --- |
| [ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)   [See Also](#seeAlsoToggle) |

The vapor pressure of the asset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double VaporPressure { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property VaporPressure As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double VaporPressure { 	double get (); 	void set (double value); } ``` |

# Remarks

Values are in kilograms per feet, squared-second (kg/(ft Â· sÂ²)) and must be non-negative.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for vaporPressure must be non-negative. |

# See Also

[ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)