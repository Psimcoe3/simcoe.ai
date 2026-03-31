---
created: 2026-01-28T21:01:38 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Mathematical_representations_of_curve_types_html
author: 
---

# Help | Mathematical representations of curve types | Autodesk

> ## Excerpt
> This section describes the curve types encountered in Revit geometry, their properties, and their mathematical representations.

---
This section describes the curve types encountered in Revit geometry, their properties, and their mathematical representations.

### Bound lines

Bound lines are defined by their endpoints. In the Revit API, obtain the endpoints of the line from the Curve-level GetEndPoint() method.

The equation for a point on a bound line in terms of the normalized parameter “u” and the line endpoints is

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_bound_line.png)

### Unbound lines

Unbound lines are handled specially in the Revit API. Most curve properties cannot be used, however, Evaluate() and ComputeDerivatives() can be used to obtain locations along the curve when a raw parameter is provided.

The equation for a point for an unbound line in terms of the raw parameter “u” and the line origin and normalized direction vector is

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_unbound_line.png)

### Arcs and Circles

Arcs and Circles are represented in the Revit API by the Arc class. They are defined in terms of their radius, center and vector normal to the plane of the arc, which are accessible in the Revit API directly from the Arc class as properties.

Circles have the IsBound property set to true. This means they can only be evaluated by using a raw parameter (range from 0 to 2π), and the equation for a point on the circle in terms of the raw parameter is

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_arcs.png)where the assumption is made that the circle lies in the XY plane.

Arcs begin and end at a certain angle. These angles can be obtained by the raw parameter values at each end of the arc, and angular values between these values can be plugged into the same equation as above.

### Cylindrical Helixes

Cylindrical helixes are represented in the Revit API by the CylindricalHelix class. They are defined in terms of the base point of the axis of the cylinder around which the helix is wound, radius, x and y vectors, pitch, and start and end angles.

### Ellipse and elliptical arcs

Ellipses and elliptical arcs segments are represented in the Revit API by the Ellipse class. Similar to arcs and circles, they are defined in a given plane in terms of their X and Y radii, center, and vector normal to the plane of the ellipse.

Full ellipses have the IsBound property set to true. Similar to circles, they can be evaluated via raw parameter between 0 and 2π:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_ellipse.png)

### NurbSpline

NURBS (nonuniform rational B-splines) are used for spline segments sketched by the user as curves or portions of 3D object sketches. They are also used to represent some types of imported geometry data.

The data for the NurbSpline include:

-   The control points array, of length n+1
-   The weights array, also of length n+1
-   The curve degree, whose value is equal to one less than the curve order (k)
-   The knot vector, of length n + k +1

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_nurb_spline.png)NurbSplines as used in Revit’s sketching tools can be generated from the control points and degree alone using an algorithm. The calculations performed by Revit’s algorithm can be duplicated externally, see this sample below:

```
public void Nurb(ModelCurve curve)
{
    NurbSpline spline = curve.GeometryCurve as NurbSpline;
    DoubleArray knots = spline.Knots;

    // Convert to generic collection
    List<double> knotList = new List<double>();
    for(int i = 0; i < knots.Size; i++)
    {
        knotList.Add(knots.get_Item(i));
    }

    // Preparation - get distance between each control point
    IList<XYZ> controlPoints = spline.CtrlPoints;
    int numControlPoints = controlPoints.Count;
    double[] chordLengths = new double[numControlPoints - 1];
    for(int iControlPoint = 1; iControlPoint < numControlPoints; ++iControlPoint)
    {
        double chordLength = 
        controlPoints[iControlPoint].DistanceTo(controlPoints[iControlPoint - 1]);
        chordLengths[iControlPoint - 1] = chordLength;
    }

    int degree = spline.Degree;
    int order = degree + 1;
    int numKnots = numControlPoints + order;
    double[] computedKnots = new double[numKnots];
    int iKnot = 0;

    // Start knot with multiplicity degree + 1.
    double startKnot = 0.0;
    double knot = startKnot;
    for(iKnot = 0; iKnot < order; ++iKnot)
    {
        computedKnots[iKnot] = knot;
    }

    // Interior knots based on chord lengths
    double prevKnot = knot;

    for(/*blank*/; iKnot <= numControlPoints; ++iKnot) 
        // Last loop computes end knot but does not set interior knot.
    {
        double knotIncrement = 0.0;
        for (int jj = iKnot - order; jj < iKnot - 1; ++jj)
        {
            knotIncrement += chordLengths[jj];
        }

        knotIncrement /= degree;
        knot = prevKnot + knotIncrement;
        if (iKnot < numControlPoints)
            computedKnots[iKnot] = knot;
        else
            break;   // Leave "knot" set to the end knot; do not increment "ii".

        prevKnot = knot;
    }

    // End knot with multiplicity degree + 1.
    for(/*blank*/; iKnot < numKnots; ++iKnot)
    {
        computedKnots[iKnot] = knot;
    }
}
```

#### HermiteSpline

Hermite splines are used for curves which are interpolated between a set of control points, like Curve by Points and flexible ducts and pipes in MEP. They are also used to represent some types of imported geometry data. In the Revit API, the HermiteSpline class offers access to the arrays of points, tangent vectors and parameters through the ControlPoints, Tangents, and Parameters properties.

The equation for the curve between two nodes in a Hermite spline is

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_hermite_1.png)where P<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-F3A27DD5-F786-42CD-80CA-9C39F86EC25F">k</sub> and P<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-7C381E19-3D6D-4BB7-B855-C0FB538F5985">k+1</sub> represent the points at each node, M<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-BA44375E-AF0B-4F7B-8966-415E75538858">k</sub> and M<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-11714EEB-B3F2-4DA9-B387-653E9A7E994E">k+1</sub> the tangent vectors, and u<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-DE8A2F53-B16E-4BD3-A45D-0C3D548B6E17">k</sub> and u<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-8248DE2A-A4D1-4609-943D-C67DF8C78ABE">k+1</sub> the parameters at the nodes, and the basis functions are:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_hermite_2.png) ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_hermite3.png)![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_hermite4.png)

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_hermite5.png)
