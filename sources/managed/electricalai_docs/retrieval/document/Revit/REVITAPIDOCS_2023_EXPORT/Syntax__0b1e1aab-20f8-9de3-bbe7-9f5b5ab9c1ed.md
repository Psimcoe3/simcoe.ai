[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ChangeSize Method

---



|  |
| --- |
| [FabricationNetworkChangeService Class](ddd58cb0-54bc-a864-9688-b890a7140112.htm)   [See Also](#seeAlsoToggle) |

Changes the size of the selection of fabrication parts.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.2

# Syntax

| C# |
| --- |
| ``` public FabricationNetworkChangeServiceResult ChangeSize( 	ISet<ElementId> selection, 	ISet<FabricationPartSizeMap> fabricationPartSizeMaps ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ChangeSize ( _ 	selection As ISet(Of ElementId), _ 	fabricationPartSizeMaps As ISet(Of FabricationPartSizeMap) _ ) As FabricationNetworkChangeServiceResult ``` |

 

| Visual C++ |
| --- |
| ``` public: FabricationNetworkChangeServiceResult ChangeSize( 	ISet<ElementId^>^ selection,  	ISet<FabricationPartSizeMap^>^ fabricationPartSizeMaps ) ``` |

#### Parameters

selection
:   Type:  System.Collections.Generic ISet   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The set of element identifiers of fabrication parts to change the size for.

fabricationPartSizeMaps
:   Type:  System.Collections.Generic ISet   [FabricationPartSizeMap](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.htm)    
     The map containing the original sizes for the straights to the new sizes.

# Remarks

After this method has been invoked, call:

* [GetStraightsThatWereNotChanged](644c47d9-806b-cd68-bf3e-0f8997c89f50.htm)  to get a set of fabrication part straight element identifiers that were not changed.
* [GetElementsThatFailed](7bc30db4-1cae-1acb-c346-d164d5b90822.htm)  to get a set of fabrication part element identifiers that had failures.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The selection contains invalid elements to change. -or- The fabrication size map is empty. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | No fabrication configuration is loaded. |

# See Also

[FabricationNetworkChangeService Class](ddd58cb0-54bc-a864-9688-b890a7140112.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)