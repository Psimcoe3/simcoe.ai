[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundingBoxIsInsideFilter Constructor (Outline, Double)

---



|  |
| --- |
| [BoundingBoxIsInsideFilter Class](eb8735d7-28fc-379d-9de9-1e02326851f5.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to match elements with a bounding box that is contained by the given Outline.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public BoundingBoxIsInsideFilter( 	Outline outline, 	double tolerance ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	outline As Outline, _ 	tolerance As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: BoundingBoxIsInsideFilter( 	Outline^ outline,  	double tolerance ) ``` |

#### Parameters

outline
:   Type:  [Autodesk.Revit.DB Outline](1ffe9215-0dd5-358f-495d-e983f9e7d295.htm)    
     The Outline used to find elements with a bounding box that are contained by it.

tolerance
:   Type:  System Double    
     The tolerance value to use instead of zero. See the tolerance property for details.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | outline is an empty Outline. -or- The given value for tolerance is not finite -or- The given value for tolerance is not a number |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[BoundingBoxIsInsideFilter Class](eb8735d7-28fc-379d-9de9-1e02326851f5.htm)

[BoundingBoxIsInsideFilter Overload](f7883323-6e5a-a1b8-486a-7664de5c0b92.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)