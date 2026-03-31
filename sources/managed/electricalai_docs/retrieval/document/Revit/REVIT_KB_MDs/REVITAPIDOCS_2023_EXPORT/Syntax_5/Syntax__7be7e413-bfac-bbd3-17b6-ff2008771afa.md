[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCenterlineCurves Method (Boolean, Boolean, Boolean, MultiplanarOption, Int32)

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

A chain of curves representing the centerline of the rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public IList<Curve> GetCenterlineCurves( 	bool adjustForSelfIntersection, 	bool suppressHooks, 	bool suppressBendRadius, 	MultiplanarOption multiplanarOption, 	int barPositionIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCenterlineCurves ( _ 	adjustForSelfIntersection As Boolean, _ 	suppressHooks As Boolean, _ 	suppressBendRadius As Boolean, _ 	multiplanarOption As MultiplanarOption, _ 	barPositionIndex As Integer _ ) As IList(Of Curve) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Curve^>^ GetCenterlineCurves( 	bool adjustForSelfIntersection,  	bool suppressHooks,  	bool suppressBendRadius,  	MultiplanarOption multiplanarOption,  	int barPositionIndex ) ``` |

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

multiplanarOption
:   Type:  [Autodesk.Revit.DB.Structure MultiplanarOption](37cc5a15-0771-41dd-4456-6820c7cef725.htm)    
     If the Rebar is a multi-planar shape, this parameter controls whether to generate only the curves in the primary plane (IncludeOnlyPlanarCurves), or to generate all curves, (IncludeAllMultiplanarCurves) including the out-of-plane connector segments as well as multi-planar copies of the primary plane curves. This argument is ignored for planar shapes.

barPositionIndex
:   Type:  System Int32    
     An index between 0 and (NumberOfBarPositions-1). Use the barPositionIndex to obtain all the curves at a specific index in the distribution. You can use GetNumberOfBarPositions() to verify if a specific rebar has more than one bar positions. Use GetDistributionType() to probe if the bars in a specific rebar have a varying shape. If so, you can retrieve the centerline curve geometry of that particular bar, by passing the appropriate index. When the distribution type of a rebar set is uniform, the form of the bars does not vary from one index to another.

#### Return Value

The centerline curves or empty array if the curves cannot be computed because the parameters values are inconsistent with the constraints of the RebarShape definition.

# Remarks

This method will return the centerline curves for bar at barPositionIndex even if this bar isn't included.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex is not in the range [ 0, NumberOfBarPositions-1 ]. -or- A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)