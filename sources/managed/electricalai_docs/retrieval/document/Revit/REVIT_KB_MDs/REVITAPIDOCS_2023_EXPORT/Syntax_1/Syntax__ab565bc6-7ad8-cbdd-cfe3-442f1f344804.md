[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EmitLength Property

---



|  |
| --- |
| [LineLightShape Class](3fce7f00-ae7a-04db-a6e8-dab9794bd6a7.htm)   [See Also](#seeAlsoToggle) |

The emit length.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double EmitLength { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property EmitLength As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double EmitLength { 	double get (); 	void set (double value); } ``` |

#### Field Value

The emit length as a numerical value in feet between 1.0e-9 and 30000.0

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The shape dimension is not valid because it is not between 1.0e-9 and 30000.0. |

# See Also

[LineLightShape Class](3fce7f00-ae7a-04db-a6e8-dab9794bd6a7.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)