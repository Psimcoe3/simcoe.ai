[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [VertexIndexPairArrayIterator Class](e490a9ba-4c2b-7113-f118-4e1299ffe5c6.htm)   [See Also](#seeAlsoToggle) |

Retrieves the item that is the current focus of the iterator.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual Object Current { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property Current As Object 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property Object^ Current { 	Object^ get (); } ``` |

#### Implements

 [IEnumerator Current](http://msdn2.microsoft.com/en-us/library/khfze649)

# Remarks

A new or Reset iterator must have MoveNext called on it before Current will return a valid item as per expected behavior of IEnumerator.

# See Also

[VertexIndexPairArrayIterator Class](e490a9ba-4c2b-7113-f118-4e1299ffe5c6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)