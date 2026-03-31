[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSpecificFittingAngleStatus Method

---



|  |
| --- |
| [ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)   [See Also](#seeAlsoToggle) |

Gets the status of given specific fitting angle.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool GetSpecificFittingAngleStatus( 	double angle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSpecificFittingAngleStatus ( _ 	angle As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool GetSpecificFittingAngleStatus( 	double angle ) ``` |

#### Parameters

angle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The specific fitting angle (in degree) that must be one of 90, 60, 45, 30, 22.5 or 11.25 degrees.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for angle must be 90, 60, 45, 30, 22.5 or 11.25 degrees. |

# See Also

[ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)