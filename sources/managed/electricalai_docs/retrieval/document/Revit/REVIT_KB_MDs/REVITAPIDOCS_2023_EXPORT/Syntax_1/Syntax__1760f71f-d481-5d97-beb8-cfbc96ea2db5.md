[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ToWorksetIds Method

---



|  |
| --- |
| [FilteredWorksetCollector Class](30e91d82-33a2-2561-db2a-28098a96b3ec.htm)   [See Also](#seeAlsoToggle) |

Returns the complete set of workset ids that pass the filter(s).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ICollection<WorksetId> ToWorksetIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ToWorksetIds As ICollection(Of WorksetId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<WorksetId^>^ ToWorksetIds() ``` |

#### Return Value

The complete set of workset ids.

# Remarks

This will reset the collector to the beginning and extract all worksets that pass the applied filter(s). If you have an active iterator to this same collector it will be stopped by this call.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The collector does not have a filter applied. Extraction or iteration of worksets is not permitted without a filter. |

# See Also

[FilteredWorksetCollector Class](30e91d82-33a2-2561-db2a-28098a96b3ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)