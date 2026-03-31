[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetOrderedFilters Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Gets the filters applied to the view in the order they are applied.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> GetOrderedFilters() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetOrderedFilters As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ GetOrderedFilters() ``` |

#### Return Value

The ElementIds of the Filters.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The element "this View" does not belong to a project document. -or- The view type does not support Visibility/Graphics Overriddes. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)