[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [WireSetIterator Class](5713c3b7-0345-03e6-b44c-08fb029d7d3d.htm)   [See Also](#seeAlsoToggle) |

Retrieves the item that is the current focus of the iterator.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
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

[WireSetIterator Class](5713c3b7-0345-03e6-b44c-08fb029d7d3d.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)