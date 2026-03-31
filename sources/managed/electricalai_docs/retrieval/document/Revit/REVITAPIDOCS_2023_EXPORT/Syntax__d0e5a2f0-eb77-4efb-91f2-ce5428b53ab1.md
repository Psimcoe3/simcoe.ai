[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ContainsPoint Method

---



|  |
| --- |
| [TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.htm)   [See Also](#seeAlsoToggle) |

Identifies whether the given point exists in the topography surface.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool ContainsPoint( 	XYZ point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ContainsPoint ( _ 	point As XYZ _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool ContainsPoint( 	XYZ^ point ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The point to be checked.

#### Return Value

True if the input point exists in the topography surface, otherwise false.

# Remarks

The given point will be evaluated in XYZ. If a point matches the XY location, but not the elevation, this function still returns false. This applies to TopographySurface and SiteSubRegion elements.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)