[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [ExportLinetypeTableIterator Class](901e037c-f870-f85f-8002-3223ff6c2061.htm)   [See Also](#seeAlsoToggle) |

Gets the item at the current position of the iterator.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual KeyValuePair<ExportLinetypeKey, ExportLinetypeInfo> Current { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property Current As KeyValuePair(Of ExportLinetypeKey, ExportLinetypeInfo) 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property KeyValuePair<ExportLinetypeKey^, ExportLinetypeInfo^> Current { 	KeyValuePair<ExportLinetypeKey^, ExportLinetypeInfo^> get (); } ``` |

#### Implements

 [IEnumerator T Current](http://msdn2.microsoft.com/en-us/library/58e146b7)

# Remarks

There is no current item if the iterator has not started yet or has been done.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | There is no current item in the iterator. |

# See Also

[ExportLinetypeTableIterator Class](901e037c-f870-f85f-8002-3223ff6c2061.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)