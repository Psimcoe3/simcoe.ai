[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMultistoryStairsPlacementLevels Method

---



|  |
| --- |
| [Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)   [See Also](#seeAlsoToggle) |

Gets the ids of the base levels of the stairs upon which this railing is placed.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public ISet<ElementId> GetMultistoryStairsPlacementLevels() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMultistoryStairsPlacementLevels As ISet(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ISet<ElementId^>^ GetMultistoryStairsPlacementLevels() ``` |

#### Return Value

The ids of levels the railing is placed on. The returned set consists of a subset of the base level ids of the corresponding stairs in the  [MultistoryStairs](8b07cbff-013c-889f-8807-703e63a91923.htm)  .

# Remarks

The method is valid only for railings hosted by stairs in  [MultistoryStairs](8b07cbff-013c-889f-8807-703e63a91923.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The railing is not hosted by stairs in  [MultistoryStairs](8b07cbff-013c-889f-8807-703e63a91923.htm)  . |

# See Also

[Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)