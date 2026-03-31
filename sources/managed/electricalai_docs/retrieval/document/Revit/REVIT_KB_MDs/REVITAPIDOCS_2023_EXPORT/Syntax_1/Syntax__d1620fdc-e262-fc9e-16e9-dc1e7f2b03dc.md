[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [DuctSizeIterator Class](24b02501-a69a-a52e-9b24-0ea7b79b5866.htm)   [See Also](#seeAlsoToggle) |

Gets the item at the current position of the iterator.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual MEPSize Current { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property Current As MEPSize 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property MEPSize^ Current { 	MEPSize^ get (); } ``` |

#### Implements

 [IEnumerator T Current](http://msdn2.microsoft.com/en-us/library/58e146b7)

# Remarks

There is no current item if the iterator has not started yet or has been done.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | There is no current item in the iterator. |

# See Also

[DuctSizeIterator Class](24b02501-a69a-a52e-9b24-0ea7b79b5866.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)