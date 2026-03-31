[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InsertNewAssetAsColor Method

---



|  |
| --- |
| [AssetPropertyList Class](8f1e901e-d1a6-e8f1-0e10-d8b28e0ad073.htm)   [See Also](#seeAlsoToggle) |

Insert a new AssetPropertyDouble4 containing the input value to this list.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public void InsertNewAssetAsColor( 	Color value, 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub InsertNewAssetAsColor ( _ 	value As Color, _ 	index As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void InsertNewAssetAsColor( 	Color^ value,  	int index ) ``` |

#### Parameters

value
:   Type:  [Autodesk.Revit.DB Color](3735f9b9-d477-09ea-25bd-67f34134595f.htm)    
     The color value to insert.

index
:   Type:  System Int32    
     An integer index.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | index is out of range. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The asset property is not editable. |

# See Also

[AssetPropertyList Class](8f1e901e-d1a6-e8f1-0e10-d8b28e0ad073.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)