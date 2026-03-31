[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ToElementIds Method

---



|  |
| --- |
| [FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)   [See Also](#seeAlsoToggle) |

Returns the complete set of element ids that pass the filter(s).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> ToElementIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ToElementIds As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ ToElementIds() ``` |

#### Return Value

The complete set of element ids.

# Remarks

This will reset the collector to the beginning and extract all elements that pass the applied filter(s). If you have an active iterator to this same collector it will be stopped by this call.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The collector does not have a filter applied. Extraction or iteration of elements is not permitted without a filter. |

# See Also

[FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)