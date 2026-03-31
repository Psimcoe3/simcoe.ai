[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ValidateCurve Method (Curve, DirectShapeTargetViewType)

---



|  |
| --- |
| [ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)   [See Also](#seeAlsoToggle) |

Validates curve to be added to the view-specific shape being constructed. Called by AddCurve() to validate input. This function may be used to pre-validate the geometry being added to avoid AddCurve() throwing an InvalidArgumentException

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static bool ValidateCurve( 	Curve GCurve, 	DirectShapeTargetViewType targetViewType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ValidateCurve ( _ 	GCurve As Curve, _ 	targetViewType As DirectShapeTargetViewType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ValidateCurve( 	Curve^ GCurve,  	DirectShapeTargetViewType targetViewType ) ``` |

#### Parameters

GCurve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     Curve object to be validated.

targetViewType
:   Type:  [Autodesk.Revit.DB DirectShapeTargetViewType](1c5cd94e-3804-54da-73af-505655b0948f.htm)    
     View type for which this curve is intended.

#### Return Value

True is %GCurve% is acceptable as a part of view-specific shape representation.

# Remarks

Validation conditions depend on the type of view for which the shape representation is intended. For plan views, a curve is expected to be planar and non-degenerate (e.g., NOT a circle of zero radius).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)

[ValidateCurve Overload](b4a33128-d93f-0ac3-61d6-de0f4b771872.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)