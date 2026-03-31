[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BaseElevation Property

---



|  |
| --- |
| [StairsLanding Class](cae109cd-bc50-6c36-300e-35d3457c0982.htm)   [See Also](#seeAlsoToggle) |

The base elevation of the landing.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double BaseElevation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BaseElevation As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double BaseElevation { 	double get (); 	void set (double value); } ``` |

#### Field Value

The base elevation is relative elevation against base elevation of the stairs to which the stairs run belongs to. When setting this property the base elevation will be rounded automatically to a multiple of the riser height.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for height must be no more than 30000 feet in absolute value. -or- When setting this property: The height is less than half of the riser height of the stairs. |

# See Also

[StairsLanding Class](cae109cd-bc50-6c36-300e-35d3457c0982.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)