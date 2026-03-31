[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetUnderlayBaseLevel Method

---



|  |
| --- |
| [ViewPlan Class](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)   [See Also](#seeAlsoToggle) |

Sets the level whose elevation will determine the bottom of the underlay range. The elevation of the next highest level will be used to determine the top of the underlay range.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetUnderlayBaseLevel( 	ElementId levelId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetUnderlayBaseLevel ( _ 	levelId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetUnderlayBaseLevel( 	ElementId^ levelId ) ``` |

#### Parameters

levelId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element id of a level in the project or else InvalidElementId.

# Remarks

If the level specified is the highest level, the underlay range will be unbounded. The underlay range will consist of everything above the specified level.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The ElementId levelId does not correspond to a Level in the project. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ViewPlan Class](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)