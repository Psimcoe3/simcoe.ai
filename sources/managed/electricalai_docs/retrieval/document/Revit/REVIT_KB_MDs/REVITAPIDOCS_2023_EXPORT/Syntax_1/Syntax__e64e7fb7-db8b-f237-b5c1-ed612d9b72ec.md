[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OutsideAirPerArea Property

---



|  |
| --- |
| [EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)   [See Also](#seeAlsoToggle) |

The rate of flow of outside air available per unit area.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public double OutsideAirPerArea { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property OutsideAirPerArea As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double OutsideAirPerArea { 	double get (); 	void set (double value); } ``` |

# Remarks

Stored in cubic feet per hour per square foot.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The outside airPerArea does not fall within an appropriate range. |

# See Also

[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)