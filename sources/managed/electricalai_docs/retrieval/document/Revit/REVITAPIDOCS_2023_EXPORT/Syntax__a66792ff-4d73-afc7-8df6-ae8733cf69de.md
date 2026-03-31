[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAllStairsIds Method

---



|  |
| --- |
| [MultistoryStairs Class](8b07cbff-013c-889f-8807-703e63a91923.htm)   [See Also](#seeAlsoToggle) |

Gets the ids of all the stairs in this multistory stairs.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public ISet<ElementId> GetAllStairsIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAllStairsIds As ISet(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ISet<ElementId^>^ GetAllStairsIds() ``` |

#### Return Value

The ids of the stairs elements that govern groups of stairs, and the stairs elements that represent individual stairs.

# Remarks

Stairs elements returned by this method will either be members of groups of identical stairs instances which share the same level height, or individual Stairs instances which are not connected to a group with the same level height. Use  [IsPinned(Stairs)](c9dea1f0-00e3-e5ab-d66d-84e6250accab.htm)  to identify if a Stairs is a member of a group or not.

# See Also

[MultistoryStairs Class](8b07cbff-013c-889f-8807-703e63a91923.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)