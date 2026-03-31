---
created: 2026-01-28T20:59:36 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Forms_html
author: 
---

# Help | Forms | Autodesk

> ## Excerpt
> Similar to family creation, the conceptual design environment provides the ability to create new forms. The following types of forms can be created: extrusions, revolves, sweeps, swept blends, lofts, and surface forms. Rather than using the Blend, Extrusion, Revolution, Sweep, and SweptBlend classes used in Family creation, Mass families use the Form class for all types of forms.

---
### Creating Forms

Similar to family creation, the conceptual design environment provides the ability to create new forms. The following types of forms can be created: extrusions, revolves, sweeps, swept blends, lofts, and surface forms. Rather than using the Blend, Extrusion, Revolution, Sweep, and SweptBlend classes used in Family creation, Mass families use the Form class for all types of forms.

An extrusion form is created from a closed curve loop that is planar. A revolve form is created from a profile and a line in the same plane as the profile which is the axis around which the shape is revolved to create a 3D form. A sweep form is created from a 2D profile that is swept along a planar path. A swept blend is created from multiple profiles, each one planar, that is swept along a single curve. A loft form is created from 2 or more profiles located on separate planes. A single surface form is created from a profile, similarly to an extrusion, but is given no height.

The following example creates a simple extruded form. Note that since the ModelCurves used to create the form are not converted to reference lines, they will be consumed by the resulting form.

<table summary="" id="GUID-F7F3AE4B-3A6E-45C5-B511-9066A9C3E4C2__TABLE_5A3AE538FDA94FC99A35193CBC72BB39"><tbody><tr><td><b>Code Region 14-3: Creating an extrusion form</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Form</span><span> </span><span>CreateExtrusionForm</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Form</span><span> extrusionForm </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// Create one profile</span><span>
    </span><span>ReferenceArray</span><span> ref_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>

    XYZ ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>90</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelcurve </span><span>=</span><span> </span><span>MakeLine</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>90</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>90</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    modelcurve </span><span>=</span><span> </span><span>MakeLine</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>90</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    modelcurve </span><span>=</span><span> </span><span>MakeLine</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    </span><span>// The extrusion form direction</span><span>
    XYZ direction </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>50</span><span>);</span><span>

    extrusionForm </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewExtrusionForm</span><span>(</span><span>true</span><span>,</span><span> ref_ar</span><span>,</span><span> direction</span><span>);</span><span>

    </span><span>int</span><span> profileCount </span><span>=</span><span> extrusionForm</span><span>.</span><span>ProfileCount</span><span>;</span><span>

    </span><span>return</span><span> extrusionForm</span><span>;</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>ModelCurve</span><span> </span><span>MakeLine</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> XYZ ptA</span><span>,</span><span> XYZ ptB</span><span>)</span><span>
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

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-ACA912B3-A871-4886-8600-A95C293FB2D5-low.png)**Figure 56: Resulting extrusion form**

The following example shows how to create loft form using a series of CurveByPoints objects.

<table summary="" id="GUID-F7F3AE4B-3A6E-45C5-B511-9066A9C3E4C2__TABLE_4B7E9847580045DAAA8AA079CADCCFEF"><tbody><tr><td><b>Code Region 14-4: Creating a loft form</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Form</span><span> </span><span>CreateLoftForm</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Form</span><span> loftForm </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>ReferencePointArray</span><span> rpa </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferencePointArray</span><span>();</span><span>
        </span><span>ReferenceArrayArray</span><span> ref_ar_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArrayArray</span><span>();</span><span>
        </span><span>ReferenceArray</span><span> ref_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>
        </span><span>ReferencePoint</span><span> rp </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        XYZ xyz </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>// make first profile curve for loft</span><span>
        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>50</span><span>,</span><span> </span><span>10</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        </span><span>CurveByPoints</span><span> cbp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpa</span><span>);</span><span>
        ref_ar</span><span>.</span><span>Append</span><span>(</span><span>cbp</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>
        ref_ar_ar</span><span>.</span><span>Append</span><span>(</span><span>ref_ar</span><span>);</span><span>
        rpa</span><span>.</span><span>Clear</span><span>();</span><span>
        ref_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>

        </span><span>// make second profile curve for loft</span><span>
        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>50</span><span>,</span><span> </span><span>30</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        cbp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpa</span><span>);</span><span>
        ref_ar</span><span>.</span><span>Append</span><span>(</span><span>cbp</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>
        ref_ar_ar</span><span>.</span><span>Append</span><span>(</span><span>ref_ar</span><span>);</span><span>
        rpa</span><span>.</span><span>Clear</span><span>();</span><span>
        ref_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>

        </span><span>// make third profile curve for loft</span><span>
        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>75</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>75</span><span>,</span><span> </span><span>50</span><span>,</span><span> </span><span>5</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>75</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        cbp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpa</span><span>);</span><span>
        ref_ar</span><span>.</span><span>Append</span><span>(</span><span>cbp</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>
        ref_ar_ar</span><span>.</span><span>Append</span><span>(</span><span>ref_ar</span><span>);</span><span>

        loftForm </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewLoftForm</span><span>(</span><span>true</span><span>,</span><span> ref_ar_ar</span><span>);</span><span>

        </span><span>return</span><span> loftForm</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-8F7F53FC-51B6-4547-86C4-709C11B72FCA-low.png)**Figure 57: Resulting loft form**

### Form modification

Once created, forms can be modified by changing a sub element (i.e. a face, edge, curve or vertex) of the form, or an entire profile. The methods to modify a form include:

-   AddEdge
-   AddProfile
-   DeleteProfile
-   DeleteSubElement
-   MoveProfile
-   MoveSubElement
-   RotateProfile
-   RotateSubElement
-   ScaleSubElement

Additionally, you can modify a form by adding an edge or a profile, which can then be modified using the methods listed above.

The following example moves the first profile curve of the given form by a specified offset. The corresponding figure shows the result of applying this code to the loft form from the previous example.

<table summary="" id="GUID-F7F3AE4B-3A6E-45C5-B511-9066A9C3E4C2__TABLE_B301A0AAE76F4957A9DE864937880216"><tbody><tr><td><b>Code Region 14-5: Moving a profile</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MoveForm</span><span>(</span><span>Form</span><span> form</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>int</span><span> profileCount </span><span>=</span><span> form</span><span>.</span><span>ProfileCount</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>form</span><span>.</span><span>ProfileCount</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>int</span><span> profileIndex </span><span>=</span><span> </span><span>0</span><span>;</span><span>   </span><span>// modify the first form only</span><span>
                </span><span>if</span><span> </span><span>(</span><span>form</span><span>.</span><span>CanManipulateProfile</span><span>(</span><span>profileIndex</span><span>))</span><span>
                </span><span>{</span><span>
                XYZ offset </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>25</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                form</span><span>.</span><span>MoveProfile</span><span>(</span><span>profileIndex</span><span>,</span><span> offset</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-BCA27D2B-71B9-40CE-A94E-2858C22B8A08-low.png)**Figure 58: Modified loft form**

The next sample demonstrates how to move a single vertex of a given form. The corresponding figure demonstrate the effect of this code on the previous extrusion form example

<table summary="" id="GUID-F7F3AE4B-3A6E-45C5-B511-9066A9C3E4C2__TABLE_D0B6539478A3427EAE436C52B9694A11"><tbody><tr><td><b>Code Region 14-6: Moving a sub element</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MoveSubElement</span><span>(</span><span>Form</span><span> form</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> document </span><span>=</span><span> form</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>form</span><span>.</span><span>ProfileCount</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>int</span><span> profileIndex </span><span>=</span><span> </span><span>0</span><span>;</span><span>   </span><span>// get first profile</span><span>
        </span><span>ReferenceArray</span><span> ra </span><span>=</span><span> form</span><span>.</span><span>get_CurveLoopReferencesOnProfile</span><span>(</span><span>profileIndex</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Reference</span><span> r </span><span>in</span><span> ra</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ReferenceArray</span><span> ra2 </span><span>=</span><span> form</span><span>.</span><span>GetControlPoints</span><span>(</span><span>r</span><span>);</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>Reference</span><span> r2 </span><span>in</span><span> ra2</span><span>)</span><span>
            </span><span>{</span><span>
                    </span><span>Point</span><span> vertex </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>r2</span><span>).</span><span>GetGeometryObjectFromReference</span><span>(</span><span>r2</span><span>)</span><span> </span><span>as</span><span> </span><span>Point</span><span>;</span><span>

                    XYZ offset </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>15</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                    form</span><span>.</span><span>MoveSubElement</span><span>(</span><span>r2</span><span>,</span><span> offset</span><span>);</span><span>
                    </span><span>break</span><span>;</span><span>  </span><span>// just move the first point</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-6C10E6B0-0BA6-4EDD-B976-8309A1CD1B73-low.png)**Figure 59: Modified extrusion form**
