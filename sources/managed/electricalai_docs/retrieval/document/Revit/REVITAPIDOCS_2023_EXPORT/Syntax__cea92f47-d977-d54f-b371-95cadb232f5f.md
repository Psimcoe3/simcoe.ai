[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AdvancedLossFactor Constructor (Double, Double, Double, Double, Double, Double, Double)

---



|  |
| --- |
| [AdvancedLossFactor Class](30e62a9d-eb01-8830-f897-dc8f32b486da.htm)   [See Also](#seeAlsoToggle) |

Creates an advanced loss factor object with the given values.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public AdvancedLossFactor( 	double ballastLossFactorIn, 	double lampLumenDepreciationIn, 	double lampTiltLossFactorIn, 	double luminaireDirtDepreciationIn, 	double surfaceDepreciationLossFactorIn, 	double temperatureLossFactorIn, 	double voltageLossFactorIn ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	ballastLossFactorIn As Double, _ 	lampLumenDepreciationIn As Double, _ 	lampTiltLossFactorIn As Double, _ 	luminaireDirtDepreciationIn As Double, _ 	surfaceDepreciationLossFactorIn As Double, _ 	temperatureLossFactorIn As Double, _ 	voltageLossFactorIn As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: AdvancedLossFactor( 	double ballastLossFactorIn,  	double lampLumenDepreciationIn,  	double lampTiltLossFactorIn,  	double luminaireDirtDepreciationIn,  	double surfaceDepreciationLossFactorIn,  	double temperatureLossFactorIn,  	double voltageLossFactorIn ) ``` |

#### Parameters

ballastLossFactorIn
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The ballast loss factor as a numerical value between 0.0 and 1.0.

lampLumenDepreciationIn
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The lamp lumen depreciation loss factor as a numerical value between 0.0 and 1.0.

lampTiltLossFactorIn
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The lamp tilt loss factor as a numerical value between 0.0 and 1.0.

luminaireDirtDepreciationIn
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The luminaire dirt depreciation loss factor as a numerical value between 0.0 and 1.0.

surfaceDepreciationLossFactorIn
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The surface depreciation loss factor as a numerical value between 0.0 and 1.0.

temperatureLossFactorIn
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The temperature loss factor as a numerical value between 0.0 and 2.0.

voltageLossFactorIn
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The voltage loss factor as a numerical value between 0.0 and 2.0.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The loss factor is not valid because it is not between 0.0 and 1.0. -or- The loss factor is not valid because it is not between 0.0 and 2.0. |

# See Also

[AdvancedLossFactor Class](30e62a9d-eb01-8830-f897-dc8f32b486da.htm)

[AdvancedLossFactor Overload](54815132-7111-d9f3-4d86-7368e0bd820f.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)