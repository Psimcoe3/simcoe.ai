---
created: 2026-01-28T21:10:03 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Boundary_Conditions_html
author: 
---

# Help | Boundary Conditions | Autodesk

> ## Excerpt
> There are three types of BoundaryConditions:

---
## BoundaryConditions

There are three types of BoundaryConditions:

-   Point
-   Curve
-   Area

The type and pertinent geometry information is retrieved using the following code:

<table summary="" id="GUID-AACCD68F-865F-462A-A11C-A2D70EF13F4B__TABLE_41F84092478B4443ACD16353C6947A88"><tbody><tr><td><b>Code Region 29-9: Getting boundary condition type and geometry</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetInfo_BoundaryConditions</span><span>(</span><span>BoundaryConditions</span><span> boundaryConditions</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>string</span><span> message </span><span>=</span><span> </span><span>"BoundaryConditions : "</span><span>;</span><span>

    boundaryConditions</span><span>.</span><span>GetBoundaryConditionsType</span><span>();</span><span>
    </span><span>switch</span><span> </span><span>(</span><span>boundaryConditions</span><span>.</span><span>GetBoundaryConditionsType</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>case</span><span> </span><span>BoundaryConditionsType</span><span>.</span><span>Point</span><span>:</span><span>
            XYZ point </span><span>=</span><span> boundaryConditions</span><span>.</span><span>Point</span><span>;</span><span>
            message </span><span>+=</span><span> </span><span>"\nThis BoundaryConditions is a Point Boundary Conditions."</span><span>;</span><span>
            message </span><span>+=</span><span> </span><span>"\nLocation point: ("</span><span> </span><span>+</span><span> point</span><span>.</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                        </span><span>+</span><span> point</span><span>.</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>BoundaryConditionsType</span><span>.</span><span>Line</span><span>:</span><span>
            message </span><span>+=</span><span> </span><span>"\nThis BoundaryConditions is a Line Boundary Conditions."</span><span>;</span><span>
            </span><span>Curve</span><span> curve </span><span>=</span><span> boundaryConditions</span><span>.</span><span>GetCurve</span><span>();</span><span>
            </span><span>// Get curve start point</span><span>
            message </span><span>+=</span><span> </span><span>"\nLocation Line: start point: ("</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                    </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
            </span><span>// Get curve end point</span><span>
            message </span><span>+=</span><span> </span><span>";  end point:("</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                    </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>BoundaryConditionsType</span><span>.</span><span>Area</span><span>:</span><span>
            message </span><span>+=</span><span> </span><span>"\nThis BoundaryConditions is an Area Boundary Conditions."</span><span>;</span><span>
            </span><span>IList</span><span>&lt;</span><span>CurveLoop</span><span>&gt;</span><span> loops </span><span>=</span><span> boundaryConditions</span><span>.</span><span>GetLoops</span><span>();</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>CurveLoop</span><span> curveLoop </span><span>in</span><span> loops</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>Curve</span><span> areaCurve </span><span>in</span><span> curveLoop</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>// Get curve start point</span><span>
                    message </span><span>+=</span><span> </span><span>"\nCurve start point:("</span><span> </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                            </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
                    </span><span>// Get curve end point</span><span>
                    message </span><span>+=</span><span> </span><span>"; Curve end point:("</span><span> </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                            </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>default</span><span>:</span><span>
            </span><span>break</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
