---
created: 2026-01-28T21:01:28 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_Parameterization_html
author: 
---

# Help | Curve Parameterization | Autodesk

> ## Excerpt
> Curves in the Revit API can be described as mathematical functions of an input parameter “u”, where the location of the curve at any given point in XYZ space is a function of “u”.

---
Curves in the Revit API can be described as mathematical functions of an input parameter “u”, where the location of the curve at any given point in XYZ space is a function of “u”.

Curves can be bound or unbound. Unbound curves have no endpoints, representing either an infinite abstraction (an unbound line) or a cyclic curve (a circle or ellipse).

In Revit, the parameter “u” can be represented in two ways:

-   A ‘normalized’ parameter. The start value of the parameter is 0.0, and the end value is 1.0. For some curve types, this makes evaluation of the curve along its extents very easy, for example, the midpoint of a line is at parameter 0.5. (Note that for more complex curve equations like Splines this assumption cannot always be made).
-   A ‘raw’ parameter. The start and end value of the parameter can be any value. For a given curve, the value of the minimum and maximum raw parameter can be obtained through Curve.GetEndParameter(int) . Raw parameters are useful because their units are the same as the Revit default units (feet). So to obtain a location 5 feet along the curve from the start point, you can take the raw parameter at the start and add 5 to it. Raw parameters are also the only way to evaluate unbound curves.

The methods Curve.ComputeNormalizedParameter() and Curve.ComputeRawParameter() automatically scale between the two parameter types. The method Curve.IsInside() evaluates a raw parameter to see if it lies within the bounds of the curve.

You can use the parameter to evaluate a variety of properties of the curve at any given location:

-   The XYZ location of the given curve. This is returned from Curve.Evaluate(). Either the raw or normalized parameter can be supplied. If you are also calling ComputeDerivatives(), this is also the .Origin property of the Transform returned by that method.
-   The first derivative/tangent vector of the given curve. This is the .BasisX property of the Transform returned by Curve.ComputeDerivatives().
-   The second derivative/normal vector of the given curve. This is the .BasisY property of the Transform returned by Curve.ComputeDerivatives().
-   The _binormal_ vector of the given curve, defined as the cross-product of the tangent and normal vector. This is the .BasisZ property of the Transform returned by Curve.ComputeDerivatives().

All of the vectors returned are non-normalized (but you can normalize any vector in the Revit API with XYZ.Normalize()). Note that there will be no value set for the normal and binormal vector when the curve is a straight line. You can calculate a normal vector to the straight line in a given plane using the tangent vector.

The API sample “DirectionCalculation” uses the tangent vector to the wall location curve to find exterior walls that face south:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/directioncalculation_sample.png)Finding and highlighting south facing exterior walls
