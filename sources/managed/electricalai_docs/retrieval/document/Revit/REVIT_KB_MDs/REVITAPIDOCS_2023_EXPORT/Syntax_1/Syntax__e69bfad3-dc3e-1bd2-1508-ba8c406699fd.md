[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [ConduitSizeIterator Class](d7607991-c8de-5ad1-b615-24ec9c30d39d.htm)   [See Also](#seeAlsoToggle) |

Gets the item at the current position of the iterator.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public virtual ConduitSize Current { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property Current As ConduitSize 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property ConduitSize^ Current { 	ConduitSize^ get (); } ``` |

#### Implements

 [IEnumerator T Current](http://msdn2.microsoft.com/en-us/library/58e146b7)

# Remarks

There is no current item if the iterator has not started yet or has been done.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | There is no current item in the iterator. |

# See Also

[ConduitSizeIterator Class](d7607991-c8de-5ad1-b615-24ec9c30d39d.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)