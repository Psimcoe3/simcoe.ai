[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TiltAngle Property

---



|  |
| --- |
| [PhotometricWebLightDistribution Class](6faac766-fc06-f872-22e8-ca3c94b40389.htm)   [See Also](#seeAlsoToggle) |

The tilt angle.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double TiltAngle { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property TiltAngle As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double TiltAngle { 	double get (); 	void set (double value); } ``` |

#### Field Value

The tilt angle as a numerical value in degrees between -180.0 and 180.0.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The angle is not valid because it is not between -180.0 and 180.0. |

# See Also

[PhotometricWebLightDistribution Class](6faac766-fc06-f872-22e8-ca3c94b40389.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)