[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ObjectSnapTypes Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

This enumerated type contains object snap types allowed to be set during PickPoint operations.

**Namespace:**   [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` [FlagsAttribute] public enum ObjectSnapTypes ``` |

 

| Visual Basic |
| --- |
| ``` <FlagsAttribute> _ Public Enumeration ObjectSnapTypes ``` |

 

| Visual C++ |
| --- |
| ``` [FlagsAttribute] public enum class ObjectSnapTypes ``` |

# Members

| Member name | Description |
| --- | --- |
| None | Snaps to nothing. |
| Endpoints | Snaps to the endpoint of an element or component. |
| Midpoints | Snaps to the midpoint of an element or component. |
| Nearest | Snaps to the nearest element or component. |
| WorkPlaneGrid | Snaps to a work plane grid. |
| Intersections | Snaps to intersections. |
| Centers | Snaps to the center of an arc. |
| Perpendicular | Snaps to perpendicular elements or components. |
| Tangents | Snaps tangent to an arc. |
| Quadrants | Snaps to quadrant points. For arcs, jump snaps are enabled. |
| Points | Snaps to site points. |

# See Also

[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.htm)