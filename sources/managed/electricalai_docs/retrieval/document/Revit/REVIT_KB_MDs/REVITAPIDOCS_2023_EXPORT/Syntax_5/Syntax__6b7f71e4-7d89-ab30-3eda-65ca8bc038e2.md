[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceBackgroundPatternId Property

---



|  |
| --- |
| [Material Class](2ec33007-7a2a-f86a-009b-d4c5d235a307.htm)   [See Also](#seeAlsoToggle) |

The id of the FillPatternElement used as the background pattern of faces with this material in normal views.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public ElementId SurfaceBackgroundPatternId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SurfaceBackgroundPatternId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ SurfaceBackgroundPatternId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

The FillPattern used for a background pattern must have a 'Drafting' target.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The element id must represent a valid FillPatternElement. -or- When setting this property: The FillPattern target must be a drafting pattern. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[Material Class](2ec33007-7a2a-f86a-009b-d4c5d235a307.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)