[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidValue Method

---



|  |
| --- |
| [AssetPropertyDoubleArray3d Class](f0623332-e4b1-3b6f-7247-8ee16a27251c.htm)   [See Also](#seeAlsoToggle) |

Checks that the value is a valid value for this property.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public bool IsValidValue( 	XYZ xyz ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidValue ( _ 	xyz As XYZ _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidValue( 	XYZ^ xyz ) ``` |

#### Parameters

xyz
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The value to be checked.

#### Return Value

True if the value is valid for the property.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Cannot check validity for a property not being edited in AppearanceAssetEditScope. |

# See Also

[AssetPropertyDoubleArray3d Class](f0623332-e4b1-3b6f-7247-8ee16a27251c.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)