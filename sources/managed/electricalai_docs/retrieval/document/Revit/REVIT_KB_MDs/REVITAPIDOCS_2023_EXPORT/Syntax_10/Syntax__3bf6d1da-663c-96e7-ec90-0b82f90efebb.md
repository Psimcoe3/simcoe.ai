[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetMapOfSizesForStraights Method

---



|  |
| --- |
| [FabricationNetworkChangeService Class](ddd58cb0-54bc-a864-9688-b890a7140112.htm)   [See Also](#seeAlsoToggle) |

Set the mapping for sizes of fabrication part straights to change the sizes to.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.2

# Syntax

| C# |
| --- |
| ``` public void SetMapOfSizesForStraights( 	ISet<FabricationPartSizeMap> fabricationPartSizeMaps ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetMapOfSizesForStraights ( _ 	fabricationPartSizeMaps As ISet(Of FabricationPartSizeMap) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetMapOfSizesForStraights( 	ISet<FabricationPartSizeMap^>^ fabricationPartSizeMaps ) ``` |

#### Parameters

fabricationPartSizeMaps
:   Type:  System.Collections.Generic ISet   [FabricationPartSizeMap](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.htm)    
     The map containing the original straights size to the mapped sizes.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationNetworkChangeService Class](ddd58cb0-54bc-a864-9688-b890a7140112.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)