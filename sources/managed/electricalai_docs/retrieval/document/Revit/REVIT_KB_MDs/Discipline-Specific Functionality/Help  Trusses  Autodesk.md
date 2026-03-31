---
created: 2026-01-28T21:09:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Trusses_html
author: 
---

# Help | Trusses | Autodesk

> ## Excerpt
> The Truss class represents all types of trusses in Revit. The TrussType property indicates the type of truss.

---
## Truss

The Truss class represents all types of trusses in Revit. The TrussType property indicates the type of truss.

<table summary="" id="GUID-B255F988-71FD-4687-B105-28DF77869B85__TABLE_7E6CBE88EA35497E997B0C47FFC40112"><tbody><tr><td><b>Code Region 29-7: Creating a truss over two columns</b></td></tr><tr><td><pre><code><span>Truss</span><span> </span><span>CreateTruss</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> column1</span><span>,</span><span> </span><span>FamilyInstance</span><span> column2</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Truss</span><span> truss </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Add Truss"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>transaction</span><span>.</span><span>Start</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>//sketchPlane</span><span>
            XYZ origin </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            XYZ xDirection </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            XYZ yDirection </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            XYZ zDirection </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>);</span><span>
            </span><span>Plane</span><span> plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> </span><span>Frame</span><span>(</span><span>origin</span><span>,</span><span> xDirection</span><span>,</span><span> yDirection</span><span>,</span><span> zDirection</span><span>));</span><span>
            </span><span>SketchPlane</span><span> sketchPlane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span> </span><span>(</span><span>document</span><span>,</span><span> plane</span><span>);</span><span>

            </span><span>//new base Line - use line that spans two selected columns</span><span>
            </span><span>AnalyticalMember</span><span> frame1 </span><span>=</span><span> </span><span>(</span><span>AnalyticalMember</span><span>)</span><span>document</span><span>.</span><span>GetElement</span><span>(</span><span>AnalyticalToPhysicalAssociationManager</span><span>.</span><span>GetAnalyticalToPhysicalAssociationManager</span><span>(</span><span>document</span><span>).</span><span>GetAssociatedElementId</span><span>(</span><span>column1</span><span>.</span><span>Id</span><span>));</span><span>
            XYZ centerPoint1 </span><span>=</span><span> </span><span>(</span><span>frame1</span><span>.</span><span>GetCurve</span><span>()</span><span> </span><span>as</span><span> </span><span>Line</span><span>).</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>

            </span><span>AnalyticalMember</span><span> frame2 </span><span>=</span><span> </span><span>(</span><span>AnalyticalMember</span><span>)</span><span>document</span><span>.</span><span>GetElement</span><span>(</span><span>AnalyticalToPhysicalAssociationManager</span><span>.</span><span>GetAnalyticalToPhysicalAssociationManager</span><span>(</span><span>document</span><span>).</span><span>GetAssociatedElementId</span><span>(</span><span>column2</span><span>.</span><span>Id</span><span>));</span><span>
            XYZ centerPoint2 </span><span>=</span><span> </span><span>(</span><span>frame2</span><span>.</span><span>GetCurve</span><span>()</span><span> </span><span>as</span><span> </span><span>Line</span><span>).</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>

            XYZ startPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>centerPoint1</span><span>.</span><span>X</span><span>,</span><span> centerPoint1</span><span>.</span><span>Y</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            XYZ endPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>centerPoint2</span><span>.</span><span>X</span><span>,</span><span> centerPoint2</span><span>.</span><span>Y</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Line</span><span> baseLine </span><span>=</span><span> </span><span>null</span><span>;</span><span>

            </span><span>try</span><span>
            </span><span>{</span><span>
                baseLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>startPoint</span><span>,</span><span> endPoint</span><span>);</span><span>
            </span><span>}</span><span>
            </span><span>catch</span><span> </span><span>(</span><span>System</span><span>.</span><span>ArgumentException</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Selected columns are too close to create truss."</span><span>);</span><span>
            </span><span>}</span><span>

            </span><span>// use the active view for where the truss's tag will be placed; View used in</span><span>
            </span><span>// NewTruss should be plan or elevation view parallel to the truss's base line </span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>View</span><span> view </span><span>=</span><span> document</span><span>.</span><span>ActiveView</span><span>;</span><span>

            </span><span>// Get a truss type for the truss</span><span>
            </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
            collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>));</span><span>
            collector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Truss</span><span>);</span><span>

            </span><span>TrussType</span><span> trussType </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>TrussType</span><span>;</span><span>

            </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> trussType</span><span>)</span><span>
            </span><span>{</span><span>
                truss </span><span>=</span><span> </span><span>Truss</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> trussType</span><span>.</span><span>Id</span><span>,</span><span> sketchPlane</span><span>.</span><span>Id</span><span>,</span><span> baseLine</span><span>);</span><span>
                transaction</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span>
            </span><span>{</span><span>
                transaction</span><span>.</span><span>RollBack</span><span>();</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"No truss types found in document."</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> truss</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
