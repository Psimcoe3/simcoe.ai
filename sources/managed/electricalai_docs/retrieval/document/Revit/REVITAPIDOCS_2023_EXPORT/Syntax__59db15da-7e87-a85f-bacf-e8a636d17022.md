[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFamilyPointPlacementReferences Method

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [See Also](#seeAlsoToggle) |

Returns the Point Placement References for the Family Instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public IList<FamilyPointPlacementReference> GetFamilyPointPlacementReferences() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFamilyPointPlacementReferences As IList(Of FamilyPointPlacementReference) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<FamilyPointPlacementReference^>^ GetFamilyPointPlacementReferences() ``` |

# Remarks

If a family instance has point placement references then they are returned by this method, otherwise an empty collection is returned. Examples of FamilyInstance objects that contain placement references are Panels and Flexible Components.

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)