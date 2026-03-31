[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddConnectedAsset Method

---



|  |
| --- |
| [AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.htm)   [See Also](#seeAlsoToggle) |

Adds a new connected asset attached to this asset property, if it allows it.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public void AddConnectedAsset( 	string schema ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddConnectedAsset ( _ 	schema As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddConnectedAsset( 	String^ schema ) ``` |

#### Parameters

schema
:   Type:  System String    
     The schema name.

# Remarks

Cannot add a connected asset if one is already connected. Use RemoveConnectedAsset() to avoid an exception being thrown. A new preset asset is created and connected to the property. For "UnifiedBitmap", it contains an empty property unifiedbitmap\_Bitmap.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The schema name is not valid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The asset property is not editable. -or- Cannot check validity for a property not being edited in AppearanceAssetEditScope. -or- Asset property is already connected to one asset. |

# See Also

[AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)