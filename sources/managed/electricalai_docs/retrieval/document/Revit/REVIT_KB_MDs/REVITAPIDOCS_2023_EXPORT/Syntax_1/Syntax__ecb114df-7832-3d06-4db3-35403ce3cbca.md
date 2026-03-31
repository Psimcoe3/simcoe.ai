[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveNext Method

---



|  |
| --- |
| [RebarContainerIterator Class](a1aff36e-7cd3-d0b8-f192-c47f4dfb8e7d.htm)   [See Also](#seeAlsoToggle) |

Increments the iterator to the next item.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

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

True if there is a next available item in this iterator. False if the iterator has completed all available items.

# Remarks

After an enumerator is created or after the Reset method is called, an enumerator is positioned before the first element of the collection, and the first call to the MoveNext method moves the enumerator over the first element of the collection.

# See Also

[RebarContainerIterator Class](a1aff36e-7cd3-d0b8-f192-c47f4dfb8e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)