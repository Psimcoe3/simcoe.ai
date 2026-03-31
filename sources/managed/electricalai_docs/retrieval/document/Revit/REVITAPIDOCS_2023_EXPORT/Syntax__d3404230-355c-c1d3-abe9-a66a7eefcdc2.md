[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaterialId Property

---



|  |
| --- |
| [TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.htm)   [See Also](#seeAlsoToggle) |

The id of the material applied to this element.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ElementId MaterialId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MaterialId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ MaterialId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

This applies to TopographySurface and SiteSubRegion elements.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The materialId cannot map to a valid material element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)