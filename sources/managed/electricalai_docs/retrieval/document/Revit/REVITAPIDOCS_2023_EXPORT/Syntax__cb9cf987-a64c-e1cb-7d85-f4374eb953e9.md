[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GroundPlaneLevelId Property

---



|  |
| --- |
| [SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.htm)   [See Also](#seeAlsoToggle) |

Identifies the element id of the Ground Plane level for the SunAndShadowSettings element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElementId GroundPlaneLevelId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property GroundPlaneLevelId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ GroundPlaneLevelId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: the element level is not a valid Ground Plane Level element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)