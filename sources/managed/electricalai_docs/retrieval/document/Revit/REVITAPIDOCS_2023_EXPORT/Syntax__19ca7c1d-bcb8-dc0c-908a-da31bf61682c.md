[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaterialId Property

---



|  |
| --- |
| [NonContinuousRailInfo Class](1ba1192c-2cfc-7996-e087-6b515ea4fb15.htm)   [See Also](#seeAlsoToggle) |

The material id associated with the non-continuous rail, or invalidElementId if none.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

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

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The materialId is not a valid value to be used as a non-continuous rail material Id. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[NonContinuousRailInfo Class](1ba1192c-2cfc-7996-e087-6b515ea4fb15.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)