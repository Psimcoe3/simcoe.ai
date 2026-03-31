[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveNext Method

---



|  |
| --- |
| [MEPBuildingConstructionSetIterator Class](1c1d2aad-c8ff-1e00-5c78-bc4affed0cac.htm)   [See Also](#seeAlsoToggle) |

Move the iterator one item forward.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
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

Returns True if the iterator was successfully moved forward one item and the Current property will return a valid item. False will be returned it the iterator has reached the end of the set.

#### Implements

 [IEnumerator MoveNext](http://msdn2.microsoft.com/en-us/library/ycwa4b0c)

# Remarks

MoveNext must be called before the Current property is valid with a new or Reset iterator in line with the expected behavior of IEnumerator.

# See Also

[MEPBuildingConstructionSetIterator Class](1c1d2aad-c8ff-1e00-5c78-bc4affed0cac.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)