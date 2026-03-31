---
created: 2026-01-28T21:02:37 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Solid_analysis_html
author: 
---

# Help | Solid analysis | Autodesk

> ## Excerpt
> The method Solid.IntersectWithCurve() calculates the intersection between a closed volume solid and a curve. The SolidCurveIntersectionOptions class can specify whether the results from the IntersectWithCurve() method will include curve segments inside the solid volume or outside. The curve segments inside the solid will include curve segments coincident with the face(s) of the solid. Both the curve segments and the parameters of the segments are available in the results.

---
## Intersection between solid and curve

The method Solid.IntersectWithCurve() calculates the intersection between a closed volume solid and a curve. The SolidCurveIntersectionOptions class can specify whether the results from the IntersectWithCurve() method will include curve segments inside the solid volume or outside. The curve segments inside the solid will include curve segments coincident with the face(s) of the solid. Both the curve segments and the parameters of the segments are available in the results.

The following example uses the IntersectWithCurve() method to calculate the length of rebar that lies within a column.

<table summary="" id="GUID-2601C028-7E6D-462A-9234-46FFA3E2D31E__TABLE_1152331007A245129FE54F60B2FA7A6B"><tbody><tr><td><b>Code Region: Finding intersection between solid and curve</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>FindColumnRebarIntersections</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> column</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// We will be computing the total length of the rebar inside the column</span><span>
    </span><span>double</span><span> totalRebarLengthInColumn </span><span>=</span><span> </span><span>0</span><span>;</span><span>

    </span><span>// Find rebar hosted by this column</span><span>
    </span><span>RebarHostData</span><span> rebarHostData </span><span>=</span><span> </span><span>RebarHostData</span><span>.</span><span>GetRebarHostData</span><span>(</span><span>column</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>rebarHostData </span><span>==</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>IList</span><span>&lt;</span><span>Rebar</span><span>&gt;</span><span> rebars </span><span>=</span><span> rebarHostData</span><span>.</span><span>GetRebarsInHost</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>rebars</span><span>.</span><span>Count</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>// Retrieve geometry of the column</span><span>
    </span><span>Options</span><span> geomOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>Options</span><span>();</span><span>
    geomOptions</span><span>.</span><span>ComputeReferences</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    geomOptions</span><span>.</span><span>DetailLevel</span><span> </span><span>=</span><span> </span><span>ViewDetailLevel</span><span>.</span><span>Fine</span><span>;</span><span>
    </span><span>GeometryElement</span><span> elemGeometry </span><span>=</span><span> column</span><span>.</span><span>get_Geometry</span><span>(</span><span>geomOptions</span><span>);</span><span>

    </span><span>// Examine all geometry primitives of the column</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> elemPrimitive </span><span>in</span><span> elemGeometry</span><span>)</span><span>
    </span><span>{</span><span>

        </span><span>// Skip objects that are not geometry instances</span><span>
        </span><span>GeometryInstance</span><span> gInstance </span><span>=</span><span> elemPrimitive </span><span>as</span><span> </span><span>GeometryInstance</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>gInstance </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>continue</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>// Retrieve geometry of each found geometry instance</span><span>
        </span><span>GeometryElement</span><span> instGeometry </span><span>=</span><span> gInstance</span><span>.</span><span>GetInstanceGeometry</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> instPrimitive </span><span>in</span><span> instGeometry</span><span>)</span><span>
        </span><span>{</span><span>

            </span><span>// Skip non-solid sobject</span><span>
            </span><span>Solid</span><span> solid </span><span>=</span><span> instPrimitive </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>solid </span><span>==</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>continue</span><span>;</span><span>
            </span><span>}</span><span>

            </span><span>SolidCurveIntersectionOptions</span><span> intersectOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>SolidCurveIntersectionOptions</span><span>();</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>Rebar</span><span> rebar </span><span>in</span><span> rebars</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// Get the centerlines for the rebar to find their intersection with the column</span><span>
                </span><span>bool</span><span> selfIntersection </span><span>=</span><span> </span><span>false</span><span>;</span><span>
                </span><span>bool</span><span> suppresHooks </span><span>=</span><span> </span><span>false</span><span>;</span><span>
                </span><span>bool</span><span> suppresBends </span><span>=</span><span> </span><span>false</span><span>;</span><span>
                </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> curves </span><span>=</span><span> rebar</span><span>.</span><span>GetCenterlineCurves</span><span>(</span><span>selfIntersection</span><span>,</span><span> suppresHooks</span><span>,</span><span> suppresBends</span><span>,</span><span> </span><span>MultiplanarOption</span><span>.</span><span>IncludeOnlyPlanarCurves</span><span>,</span><span> </span><span>0</span><span>);</span><span>

                </span><span>// Examine every segment of every curve of the centerline</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>Curve</span><span> curve </span><span>in</span><span> curves</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>SolidCurveIntersection</span><span> intersection </span><span>=</span><span> solid</span><span>.</span><span>IntersectWithCurve</span><span>(</span><span>curve</span><span>,</span><span> intersectOptions</span><span>);</span><span>
                    </span><span>for</span><span> </span><span>(</span><span>int</span><span> segment </span><span>=</span><span> </span><span>0</span><span>;</span><span> segment </span><span>&lt;=</span><span> intersection</span><span>.</span><span>SegmentCount</span><span> </span><span>-</span><span> </span><span>1</span><span>;</span><span> segment</span><span>++)</span><span>
                    </span><span>{</span><span>
                        </span><span>// Calculate length of the rebar that is inside the column</span><span>
                        </span><span>Curve</span><span> curveInside </span><span>=</span><span> intersection</span><span>.</span><span>GetCurveSegment</span><span>(</span><span>segment</span><span>);</span><span>
                        </span><span>double</span><span> rebarLengthInColumn </span><span>=</span><span> curveInside</span><span>.</span><span>Length</span><span>;</span><span>
                        totalRebarLengthInColumn </span><span>=</span><span> totalRebarLengthInColumn </span><span>+</span><span> rebarLengthInColumn</span><span>;</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>

            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>
