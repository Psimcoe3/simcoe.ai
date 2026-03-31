[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CustomInitialColor Constructor (Double)

---



|  |
| --- |
| [CustomInitialColor Class](b08ddf7b-2264-9067-2be7-cfc771872db5.htm)   [See Also](#seeAlsoToggle) |

Creates a custom initial color set to the given color

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public CustomInitialColor( 	double temperature ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	temperature As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: CustomInitialColor( 	double temperature ) ``` |

#### Parameters

temperature
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The color temperature in Kelvin as a numerical value between 1800 and 20000

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The color temperature is not valid because it is not in the range of 1800 to 20000. |

# See Also

[CustomInitialColor Class](b08ddf7b-2264-9067-2be7-cfc771872db5.htm)

[CustomInitialColor Overload](d80da4e1-f97c-4a82-409b-17db89c39e92.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)