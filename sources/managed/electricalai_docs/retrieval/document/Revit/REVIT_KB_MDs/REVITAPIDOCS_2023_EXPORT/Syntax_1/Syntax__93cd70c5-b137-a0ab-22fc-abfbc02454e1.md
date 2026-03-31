[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveNext Method

---



|  |
| --- |
| [EdgeArrayArrayIterator Class](1457335d-14ea-97dd-e7ef-8b294b23119b.htm)   [See Also](#seeAlsoToggle) |

Move the iterator one item forward.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

Returns True if the iterator was successfully moved forward one item and the Current property will return a valid item. False will be returned it the iterator has reached the end of the array.

#### Implements

 [IEnumerator MoveNext](http://msdn2.microsoft.com/en-us/library/ycwa4b0c)

# Remarks

MoveNext must be called before the Current property is valid with a new or Reset iterator in line with the expected behavior of IEnumerator.

# See Also

[EdgeArrayArrayIterator Class](1457335d-14ea-97dd-e7ef-8b294b23119b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)