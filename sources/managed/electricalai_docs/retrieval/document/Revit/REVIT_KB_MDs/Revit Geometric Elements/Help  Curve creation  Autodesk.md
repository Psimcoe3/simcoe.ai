---
created: 2026-01-28T21:01:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_creation_html
author: 
---

# Help | Curve creation | Autodesk

> ## Excerpt
> Curves are often needed as inputs to Revit API methods. They can be created a number of ways.

---
Curves are often needed as inputs to Revit API methods. They can be created a number of ways.

Curves have a number of derived types with static methods for curve creation. The base Curve class also has methods for creating new Curves from existing curves.

Curve creation methods prevent creation of curves that are shorter than Revit's tolerance. This tolerance is exposed through the Application.ShortCurveTolerance property.

### Curve

The Curve class has several methods for creating new curves from existing curves.

-   Clone() - creates a copy of this Curve.
-   CreateOffset() - creates a new curve offset from this one.
-   CreateReversed() - creates a new curve with the opposite orientation of the existing curve
-   Curve.CreateTransformed() - creates a new instance of a curve as a transformation of this curve.
    
    ### Line
    

There are two static methods for creating a new Line.

-   CreateBound() - creates a new bound linear curve between two points.
-   CreateUnbound() - creates a new unbound linear curve given an origin and a direction.

<table summary="" id="GUID-A1BCB8D4-5628-45AF-B399-AF573CBBB1D0__TABLE_0860632902034A54B3FF48179F4DC114"><tbody><tr><td><b>Code Region: Create an unbound linear curve</b></td></tr><tr><td><pre><code><span>// define start point and direction for unbound line</span><span>
XYZ startPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
XYZ directionPt </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>10</span><span>);</span><span>

</span><span>// create line</span><span>
</span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateUnbound</span><span>(</span><span>startPoint</span><span>,</span><span> directionPt</span><span>);</span></code></pre></td></tr></tbody></table>

### Arc

The overloaded static Create() method allows for an Arc to be created in one of three ways:

-   based on 3 points

<table summary="" id="GUID-A1BCB8D4-5628-45AF-B399-AF573CBBB1D0__TABLE_F482D6FE1A2C44C18A55CEC422A75C31"><tbody><tr><td><b>Code Region: Create arc with 3 points</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ThreePointArc</span><span>()</span><span>
</span><span>{</span><span>
</span><span>// Create a new arc using two ends and a point on the curve</span><span>
    XYZ end0 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>    </span><span>// start point of the arc</span><span>
    XYZ end1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>10</span><span>);</span><span> </span><span>// end point of the arc</span><span>
    XYZ pointOnCurve </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>   </span><span>// point along arc</span><span>

    </span><span>Arc</span><span> arc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>end0</span><span>,</span><span> end1</span><span>,</span><span> pointOnCurve</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

-   based on a plane, radius, and angles

<table summary="" id="GUID-A1BCB8D4-5628-45AF-B399-AF573CBBB1D0__TABLE_2B3F36E3793947179C063DDB5AE29C8B"><tbody><tr><td><b>Code Region: Create arc with plane</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Arc</span><span> </span><span>CreateArcByGivingPlane</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Plane</span><span> plane</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Create an arc which is placed on the plane and whose center is the plane's origin</span><span>
        </span><span>double</span><span> radius </span><span>=</span><span> </span><span>10</span><span>;</span><span>
        </span><span>double</span><span> startAngle </span><span>=</span><span> </span><span>0</span><span>;</span><span>      </span><span>// The unit is radian</span><span>
        </span><span>double</span><span> endAngle </span><span>=</span><span> </span><span>2</span><span> </span><span>*</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>;</span><span>        </span><span>// this arc will be a circle</span><span>
        </span><span>return</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>plane</span><span>,</span><span> radius</span><span>,</span><span> startAngle</span><span>,</span><span> endAngle</span><span>);</span><span>
    </span><span>}</span></code></pre></td></tr></tbody></table>

-   based on center, radius, angles and two axes

<table summary="" id="GUID-A1BCB8D4-5628-45AF-B399-AF573CBBB1D0__TABLE_B584F1155A84425D98290E33ACEE7654"><tbody><tr><td><b>Code Region: Create arc with axes</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateArcByCenterRadius</span><span>()</span><span>
</span><span>{</span><span>
    </span><span>// Create a new arc defined by its center, radius, angles and 2 axes</span><span>
    </span><span>double</span><span> radius </span><span>=</span><span> </span><span>10</span><span>;</span><span>
    </span><span>double</span><span> startAngle </span><span>=</span><span> </span><span>0</span><span>;</span><span>      </span><span>// In radian</span><span>
    </span><span>double</span><span> endAngle </span><span>=</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>;</span><span>        </span><span>// In radian</span><span>
    XYZ center </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ xAxis </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>   </span><span>// The x axis to define the arc plane. Must be normalized</span><span>
    XYZ yAxis </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>   </span><span>// The y axis to define the arc plane. Must be normalized</span><span>

    </span><span>Arc</span><span> arc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>center</span><span>,</span><span> radius</span><span>,</span><span> startAngle</span><span>,</span><span> endAngle</span><span>,</span><span> xAxis</span><span>,</span><span> yAxis</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note for the latter two options, if the angle range is equal to or greater than 2 \* PI, the curve will be automatically converted to an unbounded circle.

### Ellipse

The static CreateCurve() method creates an Ellipse given the center, the x vector and y vector radii of the ellipse, the x and y axes to define the plane of the ellipse and the start and end parameters. If the x-radius and y-radius are almost equal it will return an arc, otherwise it will return an ellipse.

### Cylindrical Helix

The static Create() method of CylindricalHelix creates a new CylindricalHelix from the base point of the axis, a radius, x vector, z vector, pitch, a start angle to specify the start point of the helix and an end angle to specify the end point of the helix. The z vector is the axis direction and should be perpendicular to the x vector. A positive pitch yields a right-handed helix while a negative pitch yields a left-handed helix.

### NURBS

The NurbSpline class represents a NURBS, or Non-Uniform Rational B-Spline, curve. The overloaded static CreateCurve() method offers multiple ways to create a NURBS curve. The first way is using the same calculations that Revit uses when sketching splines in the user interface. It takes a list of control points and weights to create a new NurbSpline. Knots and degree of the spline are computed from the given control points and weights.

A second option also requires a list of control points and weights, but also a list of knots as well as the degree of the NurbSpline. The degree must be 1 or greater. There must be at least degree+1 control points. The size of knots must equal the sum of degree, the size of the control points array and 1. The first degree+1 knots should be identical, as should the last degree+1 knots. The knots in the middle of the sequence must be non-decreasing.

A third option only requires control points and weights. There must be at least 2 control points and the number of weights must be equal to the number of control points. The values of all weights must be positive.

In all cases, the created curve may be a NURBSpline or a simpler curve such as line or arc. This is consistent with Revit expectations that the simplest possible representation of curve should be used in Revit elements.

### Hermite Spline

The overloaded static HermiteSpline.Create() method provides two options for creating Hermite splines. The simplest way creates a Hermite spline with default tangency at its endpoints and requires only a list of control points and a flag indicating whether or not the Hermite spline is periodic. The second option creates a Hermite spline with specified tangency at its endpoints. It has an additional parameter of a HermiteSplineTangents object to specify the tangents at the start and/or end of the curve.
