[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EmitDiameter Property

---



|  |
| --- |
| [CircleLightShape Class](6dda7b94-a8cc-2947-31a7-0e0d60766c71.htm)   [See Also](#seeAlsoToggle) |

The emit diameter.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double EmitDiameter { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property EmitDiameter As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double EmitDiameter { 	double get (); 	void set (double value); } ``` |

#### Field Value

The emit diameter as a numerical value in feet between 1.0e-9 and 30000.0

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The shape dimension is not valid because it is not between 1.0e-9 and 30000.0. |

# See Also

[CircleLightShape Class](6dda7b94-a8cc-2947-31a7-0e0d60766c71.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)