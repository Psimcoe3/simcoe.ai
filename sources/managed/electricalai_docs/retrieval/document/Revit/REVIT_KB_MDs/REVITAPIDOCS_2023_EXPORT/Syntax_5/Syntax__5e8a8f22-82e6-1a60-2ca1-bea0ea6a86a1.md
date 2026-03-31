[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SectionTypeId Property

---



|  |
| --- |
| [AnalyticalMember Class](57c87ac5-a82e-5c7e-2f06-6dbf1f697566.htm)   [See Also](#seeAlsoToggle) |

The id of the type from the structural Family assigned to the Analytical Member.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public ElementId SectionTypeId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SectionTypeId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ SectionTypeId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

The type must be of category "Structural Framing" (OST\_StructuralFraming) or "Structural Columns" (OST\_StructuralColumns)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: sectionTypeId is the id of some element that is not a FamilySymbol or is not of the category "Structural Framing" (OST\_StructuralFraming) or "Structural Columns" (OST\_StructuralColumns) |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[AnalyticalMember Class](57c87ac5-a82e-5c7e-2f06-6dbf1f697566.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)