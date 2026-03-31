---
created: 2026-01-28T20:59:41 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Rationalizing_a_Surface_html
author: 
---

# Help | Rationalizing a Surface | Autodesk

> ## Excerpt
> Faces of forms can be divided with UV grids. You can access the data for a divided surface using the DividedSurface.GetReferencesWithDividedSurface() and DividedSurface.GetDividedSurfaceForReference() methods (as is shown in a subsequent example) as well as create new divided surfaces on forms as shown below.

---
### Dividing a surface

Faces of forms can be divided with UV grids. You can access the data for a divided surface using the DividedSurface.GetReferencesWithDividedSurface() and DividedSurface.GetDividedSurfaceForReference() methods (as is shown in a subsequent example) as well as create new divided surfaces on forms as shown below.

<table summary="" id="GUID-63B37608-4112-4424-B46A-ED61ACE95E7F__TABLE_E2A8ED204BD749508E94E0BE00E8E29C"><tbody><tr><td><b>Code Region 14-7: Dividing a surface</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>DivideSurface</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Form</span><span> form</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>Options</span><span> opt </span><span>=</span><span> application</span><span>.</span><span>Create</span><span>.</span><span>NewGeometryOptions</span><span>();</span><span>
    opt</span><span>.</span><span>ComputeReferences</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>

    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geomElem </span><span>=</span><span> form</span><span>.</span><span>get_Geometry</span><span>(</span><span>opt</span><span>);</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geomObj </span><span>in</span><span> geomElem</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Solid</span><span> solid </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> face </span><span>in</span><span> solid</span><span>.</span><span>Faces</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>face</span><span>.</span><span>Reference</span><span> </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>DividedSurface</span><span> ds </span><span>=</span><span> </span><span>DividedSurface</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span>face</span><span>.</span><span>Reference</span><span>);</span><span>
                </span><span>// create a divided surface with fixed number of U and V grid lines</span><span>
                </span><span>SpacingRule</span><span> srU </span><span>=</span><span> ds</span><span>.</span><span>USpacingRule</span><span>;</span><span>
                srU</span><span>.</span><span>SetLayoutFixedNumber</span><span>(</span><span>16</span><span>,</span><span> </span><span>SpacingRuleJustification</span><span>.</span><span>Center</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>

                </span><span>SpacingRule</span><span> srV </span><span>=</span><span> ds</span><span>.</span><span>VSpacingRule</span><span>;</span><span>
                srV</span><span>.</span><span>SetLayoutFixedNumber</span><span>(</span><span>24</span><span>,</span><span> </span><span>SpacingRuleJustification</span><span>.</span><span>Center</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>

                </span><span>break</span><span>;</span><span>  </span><span>// just divide one face of form</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-68B498E3-3756-47BF-8392-1F12F2F8D4ED-low.png)**Figure 60: Face of form divided by UV grids**

Accessing the USpacing and VSpacing properties of DividedSurface, you can define the SpacingRule for the U and V gridlines by specifying either a fixed number of grids (as in the example above), a fixed distance between grids, or a minimum or maximum spacing between grids. Additional information is required for each spacing rule, such as justification and grid rotation.

### Patterning a surface

A divided surface can be patterned. Any of the built-in tile patterns can be applied to a divided surface. A tile pattern is an ElementType that is assigned to the DividedSurface. The tile pattern is applied to the surface according to the UV grid layout, so changing the USpacing and VSpacing properties of the DividedSurface will affect how the patterned surface appears.

The following example demonstrates how to cover a divided surface with the OctagonRotate pattern. The corresponding figure shows how this looks when applied to the divided surface in the previous example. Note this example also demonstrates how to get a DividedSurface on a form.

<table summary="" id="GUID-63B37608-4112-4424-B46A-ED61ACE95E7F__TABLE_D7B4F3CCEFF24BCDB0978FAD61F01EDA"><tbody><tr><td><b>Code Region 14-8: Patterning a surface</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>TileSurface</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Form</span><span> form</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// cover surface with OctagonRotate tile pattern</span><span>
    </span><span>TilePatterns</span><span> tilePatterns </span><span>=</span><span> document</span><span>.</span><span>Settings</span><span>.</span><span>TilePatterns</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Reference</span><span> r </span><span>in</span><span> </span><span>DividedSurface</span><span>.</span><span>GetReferencesWithDividedSurfaces</span><span>(</span><span>form</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>DividedSurface</span><span> ds </span><span>=</span><span> </span><span>DividedSurface</span><span>.</span><span>GetDividedSurfaceForReference</span><span>(</span><span>document</span><span>,</span><span> r</span><span>);</span><span>
        ds</span><span>.</span><span>ChangeTypeId</span><span>(</span><span>tilePatterns</span><span>.</span><span>GetTilePattern</span><span>(</span><span>TilePatternsBuiltIn</span><span>.</span><span>OctagonRotate</span><span>).</span><span>Id</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-D0E6AFAA-9929-440C-87BF-F515C1579166-low.png)**Figure 61: Tile pattern applied to divided surface**

In addition to applying built-in tile patterns to a divided surface, you can create your own massing panel families using the "Curtain Panel Pattern Based.rft" template. These panel families can then be loaded into massing families and applied to divided surfaces using the DividedSurface.ChangeTypeId() method.

The following properties of Family are specific to curtain panel families:

-   IsCurtainPanelFamily
-   CurtainPanelHorizontalSpacing - horizontal spacing of driving mesh
-   CurtainPanelVerticalSpacing - vertical spacing of driving mesh
-   CurtainPanelTilePattern - choice of tile pattern

The following example demonstrates how to edit a massing panel family which can then be applied to a form in a conceptual mass document. To run this example, first create a new family document using the "Curtain Panel Pattern Based.rft" template.

<table summary="" id="GUID-63B37608-4112-4424-B46A-ED61ACE95E7F__TABLE_23DFE5C86CCC470A844C29687B220FDF"><tbody><tr><td><b>Code Region 14-9: Editing a curtain panel family</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>EditCurtainPanel</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Family</span><span> family </span><span>=</span><span> document</span><span>.</span><span>OwnerFamily</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>family</span><span>.</span><span>IsCurtainPanelFamily</span><span> </span><span>==</span><span> </span><span>true</span><span> </span><span>&amp;&amp;</span><span>
        family</span><span>.</span><span>CurtainPanelTilePattern</span><span> </span><span>==</span><span> </span><span>TilePatternsBuiltIn</span><span>.</span><span>Rectangle</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// first change spacing of grids in family document</span><span>
        family</span><span>.</span><span>CurtainPanelHorizontalSpacing</span><span> </span><span>=</span><span> </span><span>20</span><span>;</span><span>
        family</span><span>.</span><span>CurtainPanelVerticalSpacing</span><span> </span><span>=</span><span> </span><span>30</span><span>;</span><span>

        </span><span>// create new points and lines on grid</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>;</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>ReferencePoint</span><span>)).</span><span>ToElements</span><span>();</span><span>
        </span><span>int</span><span> ctr </span><span>=</span><span> </span><span>0</span><span>;</span><span>
        </span><span>ReferencePoint</span><span> rp0 </span><span>=</span><span> </span><span>null</span><span>,</span><span> rp1 </span><span>=</span><span> </span><span>null</span><span>,</span><span> rp2 </span><span>=</span><span> </span><span>null</span><span>,</span><span> rp3 </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> e </span><span>in</span><span> collection</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ReferencePoint</span><span> rp </span><span>=</span><span> e </span><span>as</span><span> </span><span>ReferencePoint</span><span>;</span><span>
            </span><span>switch</span><span> </span><span>(</span><span>ctr</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>case</span><span> </span><span>0</span><span>:</span><span>
                    rp0 </span><span>=</span><span> rp</span><span>;</span><span>
                    </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>1</span><span>:</span><span>
                    rp1 </span><span>=</span><span> rp</span><span>;</span><span>
                    </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>2</span><span>:</span><span>
                    rp2 </span><span>=</span><span> rp</span><span>;</span><span>
                    </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>3</span><span>:</span><span>
                    rp3 </span><span>=</span><span> rp</span><span>;</span><span>
                    </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
            ctr</span><span>++;</span><span>
        </span><span>}</span><span>

        </span><span>ReferencePointArray</span><span> rpAr </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferencePointArray</span><span>();</span><span>
        rpAr</span><span>.</span><span>Append</span><span>(</span><span>rp0</span><span>);</span><span>
        rpAr</span><span>.</span><span>Append</span><span>(</span><span>rp2</span><span>);</span><span>
        </span><span>CurveByPoints</span><span> curve1 </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpAr</span><span>);</span><span>
        </span><span>PointLocationOnCurve</span><span> pointLocationOnCurve25 </span><span>=</span><span> </span><span>new</span><span> </span><span>PointLocationOnCurve</span><span>(</span><span>PointOnCurveMeasurementType</span><span>.</span><span>NormalizedCurveParameter</span><span>,</span><span> </span><span>0.25</span><span>,</span><span> </span><span>PointOnCurveMeasureFrom</span><span>.</span><span>Beginning</span><span>);</span><span>
        </span><span>PointOnEdge</span><span> poeA </span><span>=</span><span> app</span><span>.</span><span>Create</span><span>.</span><span>NewPointOnEdge</span><span>(</span><span>curve1</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>,</span><span> pointLocationOnCurve25</span><span>);</span><span>
        </span><span>ReferencePoint</span><span> rpA </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>poeA</span><span>);</span><span>
        </span><span>PointLocationOnCurve</span><span> pointLocationOnCurve75 </span><span>=</span><span> </span><span>new</span><span> </span><span>PointLocationOnCurve</span><span>(</span><span>PointOnCurveMeasurementType</span><span>.</span><span>NormalizedCurveParameter</span><span>,</span><span> </span><span>0.75</span><span>,</span><span> </span><span>PointOnCurveMeasureFrom</span><span>.</span><span>Beginning</span><span>);</span><span>
        </span><span>PointOnEdge</span><span> poeB </span><span>=</span><span> app</span><span>.</span><span>Create</span><span>.</span><span>NewPointOnEdge</span><span>(</span><span>curve1</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>,</span><span> pointLocationOnCurve75</span><span>);</span><span>
        </span><span>ReferencePoint</span><span> rpB </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>poeB</span><span>);</span><span>

        rpAr</span><span>.</span><span>Clear</span><span>();</span><span>
        rpAr</span><span>.</span><span>Append</span><span>(</span><span>rp1</span><span>);</span><span>
        rpAr</span><span>.</span><span>Append</span><span>(</span><span>rp3</span><span>);</span><span>
        </span><span>CurveByPoints</span><span> curve2 </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpAr</span><span>);</span><span>
        </span><span>PointOnEdge</span><span> poeC </span><span>=</span><span> app</span><span>.</span><span>Create</span><span>.</span><span>NewPointOnEdge</span><span>(</span><span>curve2</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>,</span><span> pointLocationOnCurve25</span><span>);</span><span>
        </span><span>ReferencePoint</span><span> rpC </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>poeC</span><span>);</span><span>
        </span><span>PointOnEdge</span><span> poeD </span><span>=</span><span> app</span><span>.</span><span>Create</span><span>.</span><span>NewPointOnEdge</span><span>(</span><span>curve2</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>,</span><span> pointLocationOnCurve75</span><span>);</span><span>
        </span><span>ReferencePoint</span><span> rpD </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>poeD</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Please open a curtain family document before calling this command."</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-8EECE3F0-4C1F-4B31-9133-D3D64676E7FE-low.png)**Figure 62: Curtain panel family**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-263500A5-C732-4E47-B9AA-D878AF9E9729-low.png)**Figure 63: Curtain panel assigned to divided surface**
