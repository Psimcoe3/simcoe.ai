[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateFixedReferenceSweptGeometry Method (CurveLoop, Int32, Double, IList(CurveLoop), XYZ, SolidOptions)

---



|  |
| --- |
| [GeometryCreationUtilities Class](e829700d-48ff-0914-b288-5ceb93d8ee86.htm)   [See Also](#seeAlsoToggle) |

Creates a solid by sweeping one or more closed coplanar curve loops along a path while keeping the profile plane oriented so that a line in the plane that is initially perpendicular to a given fixed direction remains perpendicular as the profile is swept along the path.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static Solid CreateFixedReferenceSweptGeometry( 	CurveLoop sweepPath, 	int pathAttachmentCrvIdx, 	double pathAttachmentParam, 	IList<CurveLoop> profileLoops, 	XYZ fixedReferenceDirection, 	SolidOptions solidOptions ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateFixedReferenceSweptGeometry ( _ 	sweepPath As CurveLoop, _ 	pathAttachmentCrvIdx As Integer, _ 	pathAttachmentParam As Double, _ 	profileLoops As IList(Of CurveLoop), _ 	fixedReferenceDirection As XYZ, _ 	solidOptions As SolidOptions _ ) As Solid ``` |

 

| Visual C++ |
| --- |
| ``` public: static Solid^ CreateFixedReferenceSweptGeometry( 	CurveLoop^ sweepPath,  	int pathAttachmentCrvIdx,  	double pathAttachmentParam,  	IList<CurveLoop^>^ profileLoops,  	XYZ^ fixedReferenceDirection,  	SolidOptions^ solidOptions ) ``` |

#### Parameters

sweepPath
:   Type:  [Autodesk.Revit.DB CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     The sweep path, consisting of a set of contiguous curves. The path may be open or closed, but should not otherwise have any self-intersections. The path may be planar or non-planar. With the exception of path curves that lie in a plane parallel to %fixedReferenceDirection%, the curve's tangent should be nowhere parallel to %fixedReferenceDirection%. If the sweep path has corners, the solid segments that meet at a corner may not meet smoothly.

pathAttachmentCrvIdx
:   Type:  System Int32    
     The index of the curve in the sweep path where the profile loops are situated. Indexing starts at 0. Together with pathAttachmentParam, this specifies the profile's attachment point.

pathAttachmentParam
:   Type:  System Double    
     Parameter of the path curve specified by pathAttachmentCrvIdx. The profile curves must lie in the plane orthogonal to the path at this attachment point.

profileLoops
:   Type:  System.Collections.Generic IList   [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     The curve loops defining the planar domain to be swept along the path. No conditions are imposed on the orientations of the loops; this function will use copies of the input loops that have been oriented as necessary to conform to Revit's orientation conventions. Restrictions:

    * The loops must lie in the plane orthogonal to the path at the attachment point as defined above.
    * The curve loop(s) must be closed and should define a single planar domain (one outer loop and, optionally, one or more inner loops).
    * The curve loops must be without intersections, self-intersections, or degeneracies.
    * No loop may contain just one closed curve - split such loops into two or more curves beforehand.

fixedReferenceDirection
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     A unit vector specifying the fixed direction used to control how the profile plane is swept along the path; see the description and remarks above. The profile CurveLoops do not satisfy the input requirements.

solidOptions
:   Type:  [Autodesk.Revit.DB SolidOptions](75d6caeb-62d1-d31f-47fe-618ac7cedf19.htm)    
     The optional information to control the properties of the Solid.

#### Return Value

The requested solid.

# Remarks

The profile loops must lie in a plane orthogonal to the sweep path at some attachment point along the path. An example where this method is useful is in constructing railings. If the fixed direction is the upward vertical, a line in the profile plane that is initially horizontal will remain horizontal as the profile is swept along the path. This property can be used to ensure that the top of the railing remains horizontal all along the railing. The STEP ISO 10303-42 and IFC standards define a "Fixed Reference Sweep" similar to this sweep method, though there are some minor technical differences:

* The STEP ISO reference describes a specific parameterization of the swept surface, whereas we do not guarantee any particular parameterization (partly because we simplify the surface when possible).
* Neither reference mentions what should be done if the sweep pathâ€™s tangent is tangent to the reference direction at some point(s) or along the entire directrix.
* Both references impose unnecessary conditions, and they're inconsistent: STEP says "the swept\_curve is required to be a curve lying in the plane z = 0" while IFC says "The SweptArea shall lie in the plane z = 0" (SweptArea is the profile being swept).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input argument sweepPath should at least contain one curve. -or- The input argument pathAttachmentCrvIdx is not valid. -or- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | fixedReferenceDirection is not length 1.0. |

# See Also

[GeometryCreationUtilities Class](e829700d-48ff-0914-b288-5ceb93d8ee86.htm)

[CreateFixedReferenceSweptGeometry Overload](ec46c241-cb1a-2e5b-d834-fca5e1047ffa.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)