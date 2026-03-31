[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ComputeClosestPoints Method

---



|  |
| --- |
| [Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)   [See Also](#seeAlsoToggle) |

Find the closest points between two curves. Closest points mean closest pairs of points, each pair consisting of a point on this, say P1, and a point on other curve, say P2. P1 and P2 are closest locally. Each pairs of closest points will be represented by the corresponding parameter values with respect to the two curves and the 3d points. A closest pair is also known as a pair of critical points of the distance function between points of the two curves. If the input parameter returnAllCriticalPoints is set to false, then the function will return only pairs with minimum distance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public void ComputeClosestPoints( 	Curve otherCurve, 	bool withinThisCurveBounds, 	bool withinOtherCurveBounds, 	bool returnAllCriticalPnts, 	out IList<ClosestPointsPairBetweenTwoCurves> resultList ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ComputeClosestPoints ( _ 	otherCurve As Curve, _ 	withinThisCurveBounds As Boolean, _ 	withinOtherCurveBounds As Boolean, _ 	returnAllCriticalPnts As Boolean, _ 	<OutAttribute> ByRef resultList As IList(Of ClosestPointsPairBetweenTwoCurves) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ComputeClosestPoints( 	Curve^ otherCurve,  	bool withinThisCurveBounds,  	bool withinOtherCurveBounds,  	bool returnAllCriticalPnts,  	[OutAttribute] IList<ClosestPointsPairBetweenTwoCurves^>^% resultList ) ``` |

#### Parameters

otherCurve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The specified curve used to compute closest points to this curve.

withinThisCurveBounds
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     If this parameter is true only the solutions that are between this curve bounds will be returned. This curve must be bound if this parameter is true.

withinOtherCurveBounds
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     If this parameter is true only the solutions that are between other curve bounds will be returned. The other curve must be bound if this parameter is true.

returnAllCriticalPnts
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     The input parameter returnAllCriticalPnts is used to tell if all the critical points of the distance function are to be returned.

resultList
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [ClosestPointsPairBetweenTwoCurves](3af783ff-1aca-2c81-659d-edbaa72065d7.htm)   %    
     Output parameter that will contain the results collection.

# Remarks

The output list of closest points contains one entry for each pair of closest points. The following is the meaning of every ClosestPointsPairBetweenTwoCurves's members:

* XYZPointOnFirstCurve is the closest point on the first curve;
* XYZPointOnSecondCurve is the closest point on the second curve;
* ParameterOnFirstCurve is the raw (not normalized) parameter on the first curve
* ParameterOnSecondCurve is the raw (not normalized) parameter on the second curve
* Distance is the distance from the closest point on the first curve to the closest point on the second curve.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when otherCurve argument is null. Thrown when resultArray is null. |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | Thrown when withinThisCurveBounds is true and this curve is unbounded. Thrown when withinOtherCurveBounds is true and other curve is unbounded. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the method failed. For example the problem has infinitely many solutions such as two parallel lines or two concentric circles, or in other singular cases that the method currently cannot handle, such as evaluating the closest points between a spline and a line, and the spline contains a flat segment (all points on the segment have zero curvature), and the closest points lie within that flat segment. |

# See Also

[Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)