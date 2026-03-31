[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Contains Method

---



|  |
| --- |
| [SelectionFilterElement Class](b0aaf230-e034-8466-c1e4-1d91e7162d19.htm)   [See Also](#seeAlsoToggle) |

Returns true if the given ElementId is a member of this filter's set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool Contains( 	ElementId id ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Contains ( _ 	id As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Contains( 	ElementId^ id ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ElementId to look for.

#### Return Value

True if the given ElementId is a member of the filter, otherwise false.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Invalid ElementId |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SelectionFilterElement Class](b0aaf230-e034-8466-c1e4-1d91e7162d19.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)