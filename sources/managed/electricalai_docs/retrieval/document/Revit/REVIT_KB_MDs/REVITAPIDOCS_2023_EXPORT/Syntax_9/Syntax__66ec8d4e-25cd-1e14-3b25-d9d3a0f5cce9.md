[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetStackedWallMemberIds Method

---



|  |
| --- |
| [Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)   [See Also](#seeAlsoToggle) |

Get the sub walls which belongs to the wall.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> GetStackedWallMemberIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetStackedWallMemberIds As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ GetStackedWallMemberIds() ``` |

#### Return Value

If the wall is a stacked wall, the Ids of the sub will be returned in bottom-top order.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This wall isn't a consistent stacked wall. |

# See Also

[Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)