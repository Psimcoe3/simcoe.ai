[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveNext Method

---



|  |
| --- |
| [FilteredElementIdIterator Class](dfd0acee-d626-d5b2-fa2a-f9fc4edb49e8.htm)   [See Also](#seeAlsoToggle) |

Increments the iterator to the next element id passing the filter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public virtual bool MoveNext() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function MoveNext As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool MoveNext() ``` |

#### Return Value

True if there is another available element id passing the filter in this iterator. False if the iterator has completed all available element ids.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The FilteredElementCollector that yielded this iterator has been reset by another operation. No further iteration is permitted with this iterator. -or- The iterator cannot proceed due to changes made to the Element table in Revit's database (typically, this can be the result of an Element deletion). |

# See Also

[FilteredElementIdIterator Class](dfd0acee-d626-d5b2-fa2a-f9fc4edb49e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)