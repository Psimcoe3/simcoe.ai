---
created: 2026-01-28T21:01:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_collections_html
author: 
---

# Help | Curve collections | Autodesk

> ## Excerpt
> The Revit API uses different types of collections of curves as inputs.

---
The Revit API uses different types of collections of curves as inputs.

**Note**: Newer API methods use .NET collections of Curves in place of CurveArray and CurveArrArray.

## CurveLoop

A CurveLoop represents a specific chain of curves joined end-to-end. It can represent a closed loop or an open one. The members of the CurveLoop may be directly iterated, as the class implements `IEnumerable<Curve>`. The iteration provides copies of the curves directly contained in the loop; modification of the curves will not affect the curves that are contained in the loop. CurveLoops can be created using:

-   CurveLoop.Create() - creates a new CurveLoop from a list of curves.
-   CurveLoop.CreateViaCopy() - creates a new CurveLoop as a copy of an existing CurveLoop.
-   CurveLoop.CreateViaThicken(Curve, double, XYZ) - creates a new closed CurveLoop by thickening the input curve with respect to a given plane.
-   CurveLoop.CreateViaThicken(CurveLoop, double, XYZ) -creates a new closed curve loop by thickening the input open curve loop with respect to a given plane.
-   CurveLoop.CreateViaTransform() - creates a new CurveLoop as a transformed copy of the input CurveLoop. Note that the thickness parameter for the overloaded CreateViaThicken() method must result in a curve which exceed Revit's short curve tolerance (Application.ShortCurveTolerance), otherwise an exception will be thrown.

`CurveLoop.Transform()` performs similarly to CreateViaTransform(), but it transforms the curves contained within the CurveLoop rather than creating a transformed copy.

`CurveLoop.NumberOfCurves` returns the number of curves in the curve loop.

`CurveLoop.CreateViaOffset()` creates a new curve loop that is an offset of the existing curve loop. This can be done in two ways:

-   With a single offset distance
-   With an array of offset distances. The size of this array must match the size of the curve loop. The curve at position i will be offset with the double at position i in the array.

### CurveArray

This collection class represents an arbitrary collection of curves. Create it using its constructor.

### CurveArrArray

This collection class is a collection of CurveArrays. When this is used, the organization of the sub-elements of this array have meaning for the method this is passed to; for example, in NewExtrusion() multiple CurveArrays should represent different closed loops.
