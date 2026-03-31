[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateCurve Method

---



|  |
| --- |
| [Ellipse Class](b966b82f-0627-c94a-9f37-994d00bdff18.htm)   [See Also](#seeAlsoToggle) |

Creates a new geometric ellipse or elliptical arc object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017\_subscription\_update

# Syntax

| C# |
| --- |
| ``` public static Curve CreateCurve( 	XYZ center, 	double xRadius, 	double yRadius, 	XYZ xAxis, 	XYZ yAxis, 	double startParameter, 	double endParameter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateCurve ( _ 	center As XYZ, _ 	xRadius As Double, _ 	yRadius As Double, _ 	xAxis As XYZ, _ 	yAxis As XYZ, _ 	startParameter As Double, _ 	endParameter As Double _ ) As Curve ``` |

 

| Visual C++ |
| --- |
| ``` public: static Curve^ CreateCurve( 	XYZ^ center,  	double xRadius,  	double yRadius,  	XYZ^ xAxis,  	XYZ^ yAxis,  	double startParameter,  	double endParameter ) ``` |

#### Parameters

center
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The center.

xRadius
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The x vector radius of the ellipse.

yRadius
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The y vector radius of the ellipse.

xAxis
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The x axis to define the ellipse plane. Must be normalized.

yAxis
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The y axis to define the ellipse plane. Must be normalized.

startParameter
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The raw parameter value at the start of the ellipse.

endParameter
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The raw parameter value at the end of the ellipse.

#### Return Value

The new ellipse or elliptical arc.

# Remarks

If the angle range is equal to or greater than 2 \* PI, the curve will be automatically converted to an unbounded ellipse. If xRadius and yRadius are almost equal, the curve will be returned as an arc.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for xRadius must be greater than 0 and no more than 30000 feet. -or- The given value for yRadius must be greater than 0 and no more than 30000 feet. -or- xAxis is not length 1.0. -or- yAxis is not length 1.0. |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | The vectors xAxis and yAxis are not perpendicular. -or- Start parameter must be less than end parameter. -or- Curve length is too small for Revit's tolerance (as identified by Application.ShortCurveTolerance). |

# See Also

[Ellipse Class](b966b82f-0627-c94a-9f37-994d00bdff18.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)