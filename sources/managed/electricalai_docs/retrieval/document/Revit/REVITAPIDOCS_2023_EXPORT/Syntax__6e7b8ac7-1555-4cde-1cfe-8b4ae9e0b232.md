[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidRoughness Method

---



|  |
| --- |
| [DuctLiningType Class](4586ac5e-f45d-89b0-842f-e66ae617ae30.htm)   [See Also](#seeAlsoToggle) |

Identifies if the input roughness is valid.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsValidRoughness( 	double roughness ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidRoughness ( _ 	roughness As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidRoughness( 	double roughness ) ``` |

#### Parameters

roughness
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The roughness to check.

#### Return Value

True if the value is acceptable, false otherwise.

# Remarks

Roughness should be at least equal to or larger than 0.

# See Also

[DuctLiningType Class](4586ac5e-f45d-89b0-842f-e66ae617ae30.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)