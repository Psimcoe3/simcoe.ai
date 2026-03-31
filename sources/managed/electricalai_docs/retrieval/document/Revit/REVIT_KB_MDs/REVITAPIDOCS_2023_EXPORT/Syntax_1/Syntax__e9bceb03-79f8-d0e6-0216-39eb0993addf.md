[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsBoundaryPoint Method

---



|  |
| --- |
| [TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.htm)   [See Also](#seeAlsoToggle) |

Identifies whether the given point is an existing boundary point of the current topography surface.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsBoundaryPoint( 	XYZ point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsBoundaryPoint ( _ 	point As XYZ _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsBoundaryPoint( 	XYZ^ point ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The point to be checked.

#### Return Value

Returns true if a given point is an existing boundary point. For TopographySurface and SiteSubRegion elements, it returns false if the given point is an existing interior point of current topography surface. For the topography surface associated with a BuildingPad element, it always returns true if the point is a part of the element (all points are boundary points for the topography surface associated with a BuildingPad element).

# Remarks

This applies to TopographySurface, SiteSubRegion, and the topography surface associated with a BuildingPad element. The given point will be evaluated in XYZ. If a point matches the XY location, but not the elevation, an ArgumentException will be thrown if this point does not exist in current topography surface.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input point does not exist in the current topography surface. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)