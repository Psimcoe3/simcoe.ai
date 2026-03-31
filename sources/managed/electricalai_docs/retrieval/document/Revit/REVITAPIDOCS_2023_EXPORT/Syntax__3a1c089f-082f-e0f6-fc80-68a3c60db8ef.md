[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundingBoxIntersectsFilter Constructor (Outline)

---



|  |
| --- |
| [BoundingBoxIntersectsFilter Class](1fbe1cff-ed94-4815-564b-05fd9e8f61fe.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to match elements with a bounding box that intersects the given Outline.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public BoundingBoxIntersectsFilter( 	Outline outline ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	outline As Outline _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: BoundingBoxIntersectsFilter( 	Outline^ outline ) ``` |

#### Parameters

outline
:   Type:  [Autodesk.Revit.DB Outline](1ffe9215-0dd5-358f-495d-e983f9e7d295.htm)    
     The Outline used to find elements with a bounding box that intersect it.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | outline is an empty Outline. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[BoundingBoxIntersectsFilter Class](1fbe1cff-ed94-4815-564b-05fd9e8f61fe.htm)

[BoundingBoxIntersectsFilter Overload](05ca6834-0efa-3970-3e1b-9c62c7cee423.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)