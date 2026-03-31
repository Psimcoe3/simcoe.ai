[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddNewAssetAsColor Method

---



|  |
| --- |
| [AssetPropertyList Class](8f1e901e-d1a6-e8f1-0e10-d8b28e0ad073.htm)   [See Also](#seeAlsoToggle) |

Adds a new AssetPropertyDouble4 property to the list containing a value matching the input color.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public void AddNewAssetAsColor( 	Color value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddNewAssetAsColor ( _ 	value As Color _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddNewAssetAsColor( 	Color^ value ) ``` |

#### Parameters

value
:   Type:  [Autodesk.Revit.DB Color](3735f9b9-d477-09ea-25bd-67f34134595f.htm)    
     The color value to add.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The asset property is not editable. |

# See Also

[AssetPropertyList Class](8f1e901e-d1a6-e8f1-0e10-d8b28e0ad073.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)