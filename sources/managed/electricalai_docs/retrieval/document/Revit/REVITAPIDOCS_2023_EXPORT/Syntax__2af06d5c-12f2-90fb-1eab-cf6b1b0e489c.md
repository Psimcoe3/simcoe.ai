[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BasicLossFactor Constructor (Double)

---



|  |
| --- |
| [BasicLossFactor Class](4ae30f40-0afb-176a-1b90-61ac2ac2727f.htm)   [See Also](#seeAlsoToggle) |

Creates a basic loss factor object with the given value.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public BasicLossFactor( 	double lossFactorIn ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	lossFactorIn As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: BasicLossFactor( 	double lossFactorIn ) ``` |

#### Parameters

lossFactorIn
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The loss factor as a numerical value between 0.0 and 4.0

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The loss factor is not valid because it is not between 0.0 and 4.0. |

# See Also

[BasicLossFactor Class](4ae30f40-0afb-176a-1b90-61ac2ac2727f.htm)

[BasicLossFactor Overload](563324f5-ce5b-0731-e00f-f48d5e7fdacb.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)