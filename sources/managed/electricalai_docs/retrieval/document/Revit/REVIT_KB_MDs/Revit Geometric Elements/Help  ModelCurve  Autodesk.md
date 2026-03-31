---
created: 2026-01-28T21:03:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_ModelCurve_html
author: 
---

# Help | ModelCurve | Autodesk

> ## Excerpt
> ModelCurve represents model lines in the project. It exists in 3D space and is visible in all views.

---
ModelCurve represents model lines in the project. It exists in 3D space and is visible in all views.

The following pictures illustrate the four ModelCurve derived classes:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-1CE68863-4E07-4852-A896-5ACE5235B7AE-low.png)**Figure 92:ModelLine and ModelArc**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-E914167B-553C-4B5B-A87E-1AAB487A12B5-low.png)**Figure 93: ModelEllipse and ModelNurbSpline**

### Creating a ModelCurve

The key to creating a ModelCurve is to create the Geometry.Curve and SketchPlane where the Curve is located. Based on the Geometry.Curve type you input, the corresponding ModelCurve returned can be downcast to its correct type.

The following sample illustrates how to create a new model curve (ModelLine and ModelArc):

<table summary="" id="GUID-79FE567A-0CE4-40A1-BB44-05DAA921C5B6__TABLE_479155D66CC048248E4AE6F8E176FD81"><tbody><tr><td><b>Code Region 17-2: Creating a new model curve</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateModelCurves</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// get handle to application from document</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>;</span><span>

    </span><span>// Create a geometry line in Revit application</span><span>
    XYZ startPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ endPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Line</span><span> geomLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>startPoint</span><span>,</span><span> endPoint</span><span>);</span><span>

    </span><span>// Create a geometry arc in Revit application</span><span>
    XYZ end0 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ end1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    XYZ pointOnCurve </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Arc</span><span> geomArc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>end0</span><span>,</span><span> end1</span><span>,</span><span> pointOnCurve</span><span>);</span><span>

    </span><span>// Create a geometry plane in Revit application</span><span>
    XYZ origin </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ normal </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Plane</span><span> geomPlane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>normal</span><span>,</span><span> origin</span><span>);</span><span>

    </span><span>// Create a sketch plane in current document</span><span>
    </span><span>SketchPlane</span><span> sketch </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> geomPlane</span><span>);</span><span>

    </span><span>// Create a ModelLine element using the created geometry line and sketch plane</span><span>
    </span><span>ModelLine</span><span> line </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geomLine</span><span>,</span><span> sketch</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>;</span><span>

    </span><span>// Create a ModelArc element using the created geometry arc and sketch plane</span><span>
    </span><span>ModelArc</span><span> arc </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geomArc</span><span>,</span><span> sketch</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelArc</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Members

GeometryCurve

The GeometryCurve property is used to get or set the model curve's geometry curve. Except for ModelHermiteSpline, you can get different Geometry.Curves from the four ModelCurves;

-   Line
-   Arc
-   Ellipse
-   Nurbspline.

The following code sample illustrates how to get a specific Curve from a ModelCurve.

<table summary="" id="GUID-79FE567A-0CE4-40A1-BB44-05DAA921C5B6__TABLE_CFEBA8C139D3438389227DE1A8D0D11F"><tbody><tr><td><b>Code Region 17-3: Getting a specific Curve from a ModelCurve</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetCurve</span><span>(</span><span>ModelCurve</span><span> modelCurve</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>//get the geometry modelCurve of the model modelCurve</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> geoCurve </span><span>=</span><span> modelCurve</span><span>.</span><span>GeometryCurve</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>geoCurve </span><span>is</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Line</span><span>)</span><span>
    </span><span>{</span><span>
            </span><span>Line</span><span> geoLine </span><span>=</span><span> geoCurve </span><span>as</span><span> </span><span>Line</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The GeometryCurve property return value is a general Geometry.Curve object, therefore, you must use an As operator to convert the object type.

Note: The following information applies to GeometryCurve:

-   In Revit you cannot create a Hermite curve but you can import it from other software such as AutoCAD. Geometry.Curve is the only geometry class that represents the Hermite curve.
-   The SetPlaneAndCurve() method and the Curve and SketchPlane property setters are used in different situations.
    -   When the new Curve lies in the same SketchPlane, or the new SketchPlane lies on the same planar face with the old SketchPlane, use the Curve or SketchPlane property setters.
    -   If new Curve does not lay in the same SketchPlane, or the new SketchPlane does not lay on the same planar face with the old SketchPlane, you must simultaneously change the Curve value and the SketchPlane value using SetPlaneAndCurve() to avoid internal data inconsistency.
        
        #### Line Styles
        

Line styles are represented by the GraphicsStyle class. All line styles for a ModelCurve are available from the GetLineStyleIds() method which returns a set of ElementIds of GraphicsStyle elements.
