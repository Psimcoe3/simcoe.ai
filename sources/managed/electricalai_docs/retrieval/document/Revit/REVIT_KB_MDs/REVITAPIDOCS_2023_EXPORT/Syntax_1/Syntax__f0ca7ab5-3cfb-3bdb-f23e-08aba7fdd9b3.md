[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCurrent Method

---



|  |
| --- |
| [FilteredWorksetIterator Class](c80ff08f-7511-ebed-dc44-233d18ad8e87.htm)   [See Also](#seeAlsoToggle) |

The current workset found by the iterator.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public Workset GetCurrent() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCurrent As Workset ``` |

 

| Visual C++ |
| --- |
| ``` public: Workset^ GetCurrent() ``` |

#### Return Value

The workset.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | There are no more worksets in the iterator. -or- The FilteredWorksetCollector that yielded this iterator has been reset by another operation. No further iteration is permitted with this iterator. |

# See Also

[FilteredWorksetIterator Class](c80ff08f-7511-ebed-dc44-233d18ad8e87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)