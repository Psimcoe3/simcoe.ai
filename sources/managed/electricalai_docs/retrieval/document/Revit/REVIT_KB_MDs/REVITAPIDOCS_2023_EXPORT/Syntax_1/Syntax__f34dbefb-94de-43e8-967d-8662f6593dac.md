[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBoundaryPoints Method

---



|  |
| --- |
| [TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.htm)   [See Also](#seeAlsoToggle) |

Gets the points which are on the boundary of the topography surface.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public IList<XYZ> GetBoundaryPoints() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBoundaryPoints As IList(Of XYZ) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<XYZ^>^ GetBoundaryPoints() ``` |

#### Return Value

The collection of boundary points.

# Remarks

This applies to TopographySurface, SiteSubRegion, and the topography surface associated with a BuildingPad element. For a SiteSubRegion, this returns the points from a representation of the region's boundary. For the topography surface associated with a BuildingPad element, this returns the points from the sketch of this topography surface.

# See Also

[TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)