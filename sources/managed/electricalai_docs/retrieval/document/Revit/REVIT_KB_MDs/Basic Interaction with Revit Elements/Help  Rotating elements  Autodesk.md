---
created: 2026-01-28T20:50:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Rotating_elements_html
author: 
---

# Help | Rotating elements | Autodesk

> ## Excerpt
> The ElementTransformUtils class provides two static methods to rotate one or several elements in the project.

---
The ElementTransformUtils class provides two static methods to rotate one or several elements in the project.

**Table 20: Rotate Methods**

|  |  |
| --- | --- |
| Member | Description |
| `RotateElement(Document, ElementId, Line, double)` | Rotate an element in the document by a specified number of radians around a given axis. |
| `RotateElements(Document, ICollection<ElementId>, Line, double)` | Rotate several elements by IDs in the project by a specified number of radians around a given axis. |

In these methods, the angle of rotation is in radians. The positive radian means rotating counterclockwise around the specified axis, while the negative radian means clockwise, as the following pictures illustrates.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-2CDF32C7-BA19-499B-81BE-02A982E310D7-low.png)**Figure 31: Counterclockwise rotation**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-11A64EB3-0D9F-4A33-8DB7-CBA34CFBD04C-low.png)**Figure 32: Clockwise rotation**

Note that pinned elements cannot be rotated.

<table summary="" id="GUID-B1C87D72-CAA5-4311-929C-CFC9B5480D24__TABLE_D006222F789C45FAAA18D7CBAEEB9DEF"><tbody><tr><td><b>Code Region 10-5: Using RotateElement()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>RotateColumn</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    XYZ point1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>20</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ point2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>20</span><span>,</span><span> </span><span>30</span><span>);</span><span>
    </span><span>// The axis should be a bound line.</span><span>
    </span><span>Line</span><span> axis </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>point1</span><span>,</span><span> point2</span><span>);</span><span>
    </span><span>ElementTransformUtils</span><span>.</span><span>RotateElement</span><span>(</span><span>document</span><span>,</span><span> element</span><span>.</span><span>Id</span><span>,</span><span> axis</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>3.0</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

If the element Location can be downcast to a LocationCurve or a LocationPoint, you can rotate the curve or the point directly.

<table summary="" id="GUID-B1C87D72-CAA5-4311-929C-CFC9B5480D24__TABLE_DB1024D1257A48B3B4BFD58C5246E884"><tbody><tr><td><b>Code Region 10-6: Rotating based on location curve</b></td></tr><tr><td><pre><code><span>bool</span><span> </span><span>LocationRotate</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> rotated </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>// Rotate the element via its location curve.</span><span>
    </span><span>LocationCurve</span><span> curve </span><span>=</span><span> element</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> curve</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Curve</span><span> line </span><span>=</span><span> curve</span><span>.</span><span>Curve</span><span>;</span><span>
        XYZ aa </span><span>=</span><span> line</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>
        XYZ cc </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>aa</span><span>.</span><span>X</span><span>,</span><span> aa</span><span>.</span><span>Y</span><span>,</span><span> aa</span><span>.</span><span>Z </span><span>+</span><span> </span><span>10</span><span>);</span><span>
        </span><span>Line</span><span> axis </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>aa</span><span>,</span><span> cc</span><span>);</span><span>
        rotated </span><span>=</span><span> curve</span><span>.</span><span>Rotate</span><span>(</span><span>axis</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>2.0</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> rotated</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

<table summary="" id="GUID-B1C87D72-CAA5-4311-929C-CFC9B5480D24__TABLE_8F36FBC62F844D8FA44A062AA2308CF2"><tbody><tr><td><b>Code Region 10-7: Rotating based on location point</b></td></tr><tr><td><pre><code><span>bool</span><span> </span><span>LocationPointRotate</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>bool</span><span> rotated </span><span>=</span><span> </span><span>false</span><span>;</span><span>
        </span><span>LocationPoint</span><span> location </span><span>=</span><span> element</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationPoint</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> location</span><span>)</span><span>
        </span><span>{</span><span>
                XYZ aa </span><span>=</span><span> location</span><span>.</span><span>Point</span><span>;</span><span>
                XYZ cc </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>aa</span><span>.</span><span>X</span><span>,</span><span> aa</span><span>.</span><span>Y</span><span>,</span><span> aa</span><span>.</span><span>Z </span><span>+</span><span> </span><span>10</span><span>);</span><span>
                </span><span>Line</span><span> axis </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>aa</span><span>,</span><span> cc</span><span>);</span><span>           
                rotated </span><span>=</span><span> location</span><span>.</span><span>Rotate</span><span>(</span><span>axis</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>2.0</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> rotated</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
