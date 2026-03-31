[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCenterlineCurves Method

---



|  |
| --- |
| [RebarInSystem Class](c0bd03fa-78f4-eb67-54e8-e28368e94beb.htm)   [See Also](#seeAlsoToggle) |

A chain of curves representing the centerline of the rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public IList<Curve> GetCenterlineCurves( 	bool adjustForSelfIntersection, 	bool suppressHooks, 	bool suppressBendRadius ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCenterlineCurves ( _ 	adjustForSelfIntersection As Boolean, _ 	suppressHooks As Boolean, _ 	suppressBendRadius As Boolean _ ) As IList(Of Curve) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Curve^>^ GetCenterlineCurves( 	bool adjustForSelfIntersection,  	bool suppressHooks,  	bool suppressBendRadius ) ``` |

#### Parameters

adjustForSelfIntersection
:   Type:  System Boolean    
     If the curves overlap, as in a planar stirrup, this parameter controls whether they should be adjusted to avoid intersection (as in fine views), or kept in a single plane for simplicity (as in coarse views).

suppressHooks
:   Type:  System Boolean    
     Identifies if the chain will include hooks curves.

suppressBendRadius
:   Type:  System Boolean    
     Identifies if the connected chain will include unfilleted curves.

#### Return Value

The centerline curves or empty array if the curves cannot be computed because the parameters values are inconsistent with the constraints of the RebarShape definition.

# Remarks

This method will return the centerline curves for the first bar in set even if this bar isn't included.

# See Also

[RebarInSystem Class](c0bd03fa-78f4-eb67-54e8-e28368e94beb.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)