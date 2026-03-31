---
created: 2026-01-28T21:02:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Example_Retrieve_Geometry_Data_from_a_Beam_html
author: 
---

# Help | Example: Retrieve Geometry Data from a Beam | Autodesk

> ## Excerpt
> This section illustrates how to get solids and curves from a beam. You can retrieve column and brace geometry data in a similar way. The GeometryElement may contain the desired geometry as a Solid or GeometryInstance depending on whether a beam is joined or standalone, and this code covers both cases.

---
This section illustrates how to get solids and curves from a beam. You can retrieve column and brace geometry data in a similar way. The GeometryElement may contain the desired geometry as a Solid or GeometryInstance depending on whether a beam is joined or standalone, and this code covers both cases.

Note: If you want to get the beam and brace driving curve, call the FamilyInstance Location property where a LocationCurve is available.

The sample code is shown as follows:

<table summary="" id="GUID-F092BCCC-77E9-4DA9-9264-10F0DB354BF5__TABLE_495DE8D32C344CB5AAF759615E6F5C68"><tbody><tr><td><b>Code Region 20-10: Getting solids and curves from a beam</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetCurvesFromABeam</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FamilyInstance</span><span> beam</span><span>,</span><span>
                                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Options</span><span> options</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geomElem </span><span>=</span><span> beam</span><span>.</span><span>get_Geometry</span><span>(</span><span>options</span><span>);</span><span>

    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>CurveArray</span><span> curves </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>
    </span><span>System</span><span>.</span><span>Collections</span><span>.</span><span>Generic</span><span>.</span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Solid</span><span>&gt;</span><span> solids </span><span>=</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>Collections</span><span>.</span><span>Generic</span><span>.</span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Solid</span><span>&gt;();</span><span> 

    </span><span>//Find all solids and insert them into solid array</span><span>
    </span><span>AddCurvesAndSolids</span><span>(</span><span>geomElem</span><span>,</span><span> </span><span>ref</span><span> curves</span><span>,</span><span> </span><span>ref</span><span> solids</span><span>);</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>void</span><span> </span><span>AddCurvesAndSolids</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geomElem</span><span>,</span><span>
                                </span><span>ref</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>CurveArray</span><span> curves</span><span>,</span><span>
                                </span><span>ref</span><span> </span><span>System</span><span>.</span><span>Collections</span><span>.</span><span>Generic</span><span>.</span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Solid</span><span>&gt;</span><span> solids</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryObject</span><span> geomObj </span><span>in</span><span> geomElem</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> curve </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> curve</span><span>)</span><span>
        </span><span>{</span><span>
            curves</span><span>.</span><span>Append</span><span>(</span><span>curve</span><span>);</span><span>
            </span><span>continue</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Solid</span><span> solid </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Solid</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> solid</span><span>)</span><span>
        </span><span>{</span><span>
            solids</span><span>.</span><span>Add</span><span>(</span><span>solid</span><span>);</span><span>
            </span><span>continue</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>//If this GeometryObject is Instance, call AddCurvesAndSolids</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span> geomInst </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> geomInst</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> transformedGeomElem
                </span><span>=</span><span> geomInst</span><span>.</span><span>GetInstanceGeometry</span><span>(</span><span>geomInst</span><span>.</span><span>Transform</span><span>);</span><span>
            </span><span>AddCurvesAndSolids</span><span>(</span><span>transformedGeomElem</span><span>,</span><span> </span><span>ref</span><span> curves</span><span>,</span><span> </span><span>ref</span><span> solids</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The above example uses the FamilyInstance.Geometry property to access the true geometry of the beam. To obtain the original geometry of a family instance before it is modified by joins, cuts, coping, extensions, or other post-processing, use the FamilyInstance.GetOriginalGeometry() method.

Note: For more information about how to retrieve the Geometry.Options type object, refer to [Geometry Helper Classes.](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Helper_Classes_html)
