---
created: 2026-01-28T20:59:32 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Point_and_curve_objects_html
author: 
---

# Help | Point and curve objects | Autodesk

> ## Excerpt
> A reference point is an element that specifies a location in the XYZ work space of the conceptual design environment. You create reference points to design and plot lines, splines, and forms. A ReferencePoint can be added to a ReferencePointArray, then used to create a CurveByPoints, which in turn can be used to create a form.

---
A reference point is an element that specifies a location in the XYZ work space of the conceptual design environment. You create reference points to design and plot lines, splines, and forms. A ReferencePoint can be added to a ReferencePointArray, then used to create a CurveByPoints, which in turn can be used to create a form.

The following example demonstrates how to create a CurveByPoints object. See the "Creating a loft form" example in the next section to see how to create a form from multiple CurveByPoints objects.

<table summary="" id="GUID-B3D21FAA-9A8C-4E77-A019-D2E8439B473F__TABLE_5C3183FF19444C16A6E2D6E12EE80288"><tbody><tr><td><b>Code Region 14-1: Creating a new CurveByPoints</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateCurve</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ReferencePointArray</span><span> rpa </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferencePointArray</span><span>();</span><span>

    XYZ xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>ReferencePoint</span><span> rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
    rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

    xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>30</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
    rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

    xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>60</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
    rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

    xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>30</span><span>);</span><span>
    rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
    rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

    xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>150</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
    rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

    </span><span>CurveByPoints</span><span> curve </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpa</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-91A84A22-3B88-45F4-B7CE-8D75F685A95A-low.png)**Figure 54: CurveByPoints curve**

Reference points can be created based on XYZ coordinates as in the example above, or they can be created relative to other geometry so that the points will move when the referenced geometry changes. These points are created using the subclasses of the PointElementReference class. The subclasses are:

-   PointOnEdge
-   PointOnEdgeEdgeIntersection
-   PointOnEdgeFaceIntersection
-   PointOnFace
-   PointOnPlane

For example, the last two lines of code in the previous example create a reference point in the middle of the CurveByPoints.

Forms can be created using model lines or reference lines. Model lines are "consumed" by the form during creation and no longer exist as separate entities. Reference lines, on the other hand, persist after the form is created and can alter the form if they are moved. Although the API does not have a ReferenceLine class, you can change a model line to a reference line using the ModelCurve.ChangeToReferenceLine() method.

<table summary="" id="GUID-B3D21FAA-9A8C-4E77-A019-D2E8439B473F__TABLE_BD498E16085F44D5ADBF55E5B2E98957"><tbody><tr><td><b>Code Region 14-2: Using Reference Lines to create Form</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>FormArray</span><span> </span><span>CreateRevolveForm</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FormArray</span><span> revolveForms </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// Create one profile</span><span>
    </span><span>ReferenceArray</span><span> ref_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>

    XYZ ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    XYZ ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    </span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelcurve </span><span>=</span><span> </span><span>MakeModelCurveFromTwoPoints</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    modelcurve </span><span>=</span><span> </span><span>MakeModelCurveFromTwoPoints</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    modelcurve </span><span>=</span><span> </span><span>MakeModelCurveFromTwoPoints</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    </span><span>// Create axis for revolve form</span><span>
    ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>5</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>5</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    </span><span>ModelCurve</span><span> axis </span><span>=</span><span> </span><span>MakeModelCurveFromTwoPoints</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>

    </span><span>// make axis a Reference Line</span><span>
    axis</span><span>.</span><span>ChangeToReferenceLine</span><span>();</span><span>

    </span><span>// Typically this operation produces only a single form, </span><span>
    </span><span>// but some combinations of arguments will create multiple froms from a single profile.</span><span>
    revolveForms </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewRevolveForms</span><span>(</span><span>true</span><span>,</span><span> ref_ar</span><span>,</span><span> axis</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>4</span><span>);</span><span>

    </span><span>return</span><span> revolveForms</span><span>;</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>ModelCurve</span><span> </span><span>MakeModelCurveFromTwoPoints</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> XYZ ptA</span><span>,</span><span> XYZ ptB</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span> doc</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>// Create plane by the points</span><span>
    </span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    XYZ norm </span><span>=</span><span> ptA</span><span>.</span><span>CrossProduct</span><span>(</span><span>ptB</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>norm</span><span>.</span><span>IsZeroLength</span><span>())</span><span> norm </span><span>=</span><span> XYZ</span><span>.</span><span>BasisZ</span><span>;</span><span>
    </span><span>Plane</span><span> plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>norm</span><span>,</span><span> ptB</span><span>);</span><span>
    </span><span>SketchPlane</span><span> skplane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> plane</span><span>);</span><span>
    </span><span>// Create line here</span><span>
    </span><span>ModelCurve</span><span> modelcurve </span><span>=</span><span> doc</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewModelCurve</span><span>(</span><span>line</span><span>,</span><span> skplane</span><span>);</span><span>
    </span><span>return</span><span> modelcurve</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F5F29826-D2EA-4007-8C3F-8F30975261C4-low.png)**Figure 55: Resulting Revolve Form**
