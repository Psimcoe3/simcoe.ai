[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AssociatedLoadId Property

---



|  |
| --- |
| [BoundaryConditions Class](58a98f0e-e2e5-4c8b-bea1-8228b30f1685.htm)   [See Also](#seeAlsoToggle) |

The Id of the internal load element associated with a boundary conditions.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public ElementId AssociatedLoadId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AssociatedLoadId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ AssociatedLoadId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

ElementId may be set if the internal load exists and it's type fit the BoundaryConditions type only (Point, Line and Area).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: elementId is not a valid Element identifier. -or- When setting this property: Throws when the ElementId does not refer to the internal load with appropriate type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[BoundaryConditions Class](58a98f0e-e2e5-4c8b-bea1-8228b30f1685.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)