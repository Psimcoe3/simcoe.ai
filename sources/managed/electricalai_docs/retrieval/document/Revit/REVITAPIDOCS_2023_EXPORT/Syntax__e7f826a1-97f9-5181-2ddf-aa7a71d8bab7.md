[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetIgnoredCategoryIds Method

---



|  |
| --- |
| [RouteAnalysisSettings Class](e6742b6a-9c35-5344-736b-7bf9af6f4254.htm)   [See Also](#seeAlsoToggle) |

Sets the ElementIds for Category elements which are ignored by route calculation.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public void SetIgnoredCategoryIds( 	ICollection<ElementId> categoryIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetIgnoredCategoryIds ( _ 	categoryIds As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetIgnoredCategoryIds( 	ICollection<ElementId^>^ categoryIds ) ``` |

#### Parameters

categoryIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ids of Categories to be ignored by route calculation.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One or more ElementIds in categoryIds are not valid Category element ids. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RouteAnalysisSettings Class](e6742b6a-9c35-5344-736b-7bf9af6f4254.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)