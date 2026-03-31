[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InitialLuminousIntensity Constructor (Double)

---



|  |
| --- |
| [InitialLuminousIntensity Class](8ca18b8f-437f-6159-30cc-ecbb97c41d70.htm)   [See Also](#seeAlsoToggle) |

Creates an initial luminous intensity object with the given document and luminosity values.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public InitialLuminousIntensity( 	double luminosity ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	luminosity As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: InitialLuminousIntensity( 	double luminosity ) ``` |

#### Parameters

luminosity
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The luminosity value in cd as a numerical value between 0 and 1e+30.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The luminosity value is not valid because it is not between 0 and 1e+30. |

# See Also

[InitialLuminousIntensity Class](8ca18b8f-437f-6159-30cc-ecbb97c41d70.htm)

[InitialLuminousIntensity Overload](d58e54ab-9f95-3fe7-eeac-8827a1c0acdc.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)