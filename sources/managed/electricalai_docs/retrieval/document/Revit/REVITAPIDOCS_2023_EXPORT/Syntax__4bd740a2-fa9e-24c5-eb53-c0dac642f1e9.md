[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidHorizontalBoundary Method

---



|  |
| --- |
| [BoundaryValidation Class](82d6e0c5-f102-ce90-9521-3c2e74fbd495.htm)   [See Also](#seeAlsoToggle) |

Identifies whether the given curve loops compose a valid horizontal boundary.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static bool IsValidHorizontalBoundary( 	IList<CurveLoop> curveLoops ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidHorizontalBoundary ( _ 	curveLoops As IList(Of CurveLoop) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidHorizontalBoundary( 	IList<CurveLoop^>^ curveLoops ) ``` |

#### Parameters

curveLoops
:   Type:  System.Collections.Generic IList   [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     The curve loops to be checked.

#### Return Value

True if the given curve loops are valid as described above, false otherwise.

# Remarks

The curve loops are valid if projections of the loops onto a horizontal(XY) plane do not intersect each other; each curve loop is closed; input curves do not contain any helical curve; and each loop is planar and lies on a plane parallel to the horizontal(XY) plane, but not necessarily the same plane.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[BoundaryValidation Class](82d6e0c5-f102-ce90-9521-3c2e74fbd495.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)