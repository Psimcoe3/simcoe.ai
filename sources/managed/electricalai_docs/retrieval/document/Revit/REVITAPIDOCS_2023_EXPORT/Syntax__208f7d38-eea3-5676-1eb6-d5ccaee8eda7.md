[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanBeIntersectionElement Method

---



|  |
| --- |
| [DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)   [See Also](#seeAlsoToggle) |

Checks if the element can be an intersection reference.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool CanBeIntersectionElement( 	ElementId id ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanBeIntersectionElement ( _ 	id As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanBeIntersectionElement( 	ElementId^ id ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element to be checked.

#### Return Value

True if the element can be an intersection reference., false otherwise.

# Remarks

The element must be a level, grid, reference plane, or a curve element whose category is lines and reference lines.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)