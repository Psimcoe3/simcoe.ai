[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Start Method

---



|  |
| --- |
| [AppearanceAssetEditScope Class](743c74ba-12de-4d77-a677-325229525955.htm)   [See Also](#seeAlsoToggle) |

Starts the edit scope.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public Asset Start( 	ElementId assetElementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Start ( _ 	assetElementId As ElementId _ ) As Asset ``` |

 

| Visual C++ |
| --- |
| ``` public: Asset^ Start( 	ElementId^ assetElementId ) ``` |

#### Parameters

assetElementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The appearance asset element whose asset should be edited.

#### Return Value

The appearance asset to be used for editing.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AppearanceAssetEditScope Class](743c74ba-12de-4d77-a677-325229525955.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)