---
created: 2026-01-28T21:03:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Extrusion_Analysis_of_a_Solid_html
author: 
---

# Help | Extrusion Analysis of a Solid | Autodesk

> ## Excerpt
> The utility class ExtrusionAnalyzer allows you to attempt to “fit” a given piece of geometry into the shape of an extruded profile. An instance of this class is a single-time use class which should be supplied a solid geometry, a plane, and a direction. After the ExtrusionAnalyzer has been initialized, you can access the results through the following members:

---
The utility class ExtrusionAnalyzer allows you to attempt to “fit” a given piece of geometry into the shape of an extruded profile. An instance of this class is a single-time use class which should be supplied a solid geometry, a plane, and a direction. After the ExtrusionAnalyzer has been initialized, you can access the results through the following members:

-   The GetExtrusionBase() method returns the calculated base profile of the extruded solid aligned to the input plane.
-   The CalculateFaceAlignment() method can be used to identify all faces from the original geometry which do and do not align with the faces of the calculated extrusion. This could be useful to figure out if a wall, for example, has a slanted join at the top as would be the case if there is a join with a roof. If a face is unaligned, something is joined to the geometry that is affecting it.
-   To determine the element that produced the non-aligned face, pass the face to Element.GetGeneratingElementIds(). For more details on this utility, see the following section.

The ExtrusionAnalyzer utility works best for geometry which are at least somewhat “extrusion-like”, for example, the geometry of a wall which may or may not be affected by end joins, floor joins, roof joins, openings cut by windows and doors, or other modifications. Rarely for specific shape and directional combinations the analyzer may be unable to determine a coherent face to act as the base of the extrusion – an InvalidOperationException will be thrown in these situations.

In this example, the extrusion analyzer is used to calculate and outline a shadow formed from the input solid and the sun direction.

<table summary="" id="GUID-02A61B4E-285B-4AF9-AE9D-9543DEA43530__TABLE_70304500F5FF4BAF81A0D4E7573C5348"><tbody><tr><td><b>Code Region: Use Extrusion Analyzer to calculate and draw a shadow outline.</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Draw the shadow of the indicated solid with the sun direction specified.</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>/// &lt;remarks&gt;The shadow will be outlined with model curves added to the document.</span><span>
</span><span>/// A transaction must be open in the document.&lt;/remarks&gt;</span><span>
</span><span>/// &lt;param name="document"&gt;The document.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="solid"&gt;The target solid.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="targetLevel"&gt;The target level where to measure and draw the shadow.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="sunDirection"&gt;The direction from the sun (or light source).&lt;/param&gt;</span><span>
</span><span>/// &lt;returns&gt;The curves created for the shadow.&lt;/returns&gt;</span><span>
</span><span>/// &lt;throws cref="Autodesk.Revit.Exceptions.InvalidOperationException"&gt;Thrown by ExtrusionAnalyzer when the geometry and </span><span>
</span><span>/// direction combined do not permit a successful analysis.&lt;/throws&gt;</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> </span><span>DrawShadow</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Solid</span><span> solid</span><span>,</span><span> </span><span>Level</span><span> targetLevel</span><span>,</span><span> XYZ sunDirection</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create target plane from level.        </span><span>
    </span><span>Plane</span><span> plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>XYZ</span><span>.</span><span>BasisZ</span><span>,</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> targetLevel</span><span>.</span><span>ProjectElevation</span><span>));</span><span>

    </span><span>// Create extrusion analyzer.</span><span>
    </span><span>ExtrusionAnalyzer</span><span> analyzer </span><span>=</span><span> </span><span>ExtrusionAnalyzer</span><span>.</span><span>Create</span><span>(</span><span>solid</span><span>,</span><span> plane</span><span>,</span><span> sunDirection</span><span>);</span><span>

    </span><span>// Get the resulting face at the base of the calculated extrusion.</span><span>
    </span><span>Face</span><span> result </span><span>=</span><span> analyzer</span><span>.</span><span>GetExtrusionBase</span><span>();</span><span>

    </span><span>// Convert edges of the face to curves.</span><span>
    </span><span>CurveArray</span><span> curves </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewCurveArray</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>EdgeArray</span><span> edgeLoop </span><span>in</span><span> result</span><span>.</span><span>EdgeLoops</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Edge</span><span> edge </span><span>in</span><span> edgeLoop</span><span>)</span><span>
        </span><span>{</span><span>
            curves</span><span>.</span><span>Append</span><span>(</span><span>edge</span><span>.</span><span>AsCurve</span><span>());</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// Get the model curve factory object.</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>ItemFactoryBase</span><span> itemFactory</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>document</span><span>.</span><span>IsFamilyDocument</span><span>)</span><span>
        itemFactory </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>;</span><span>
    </span><span>else</span><span>
        itemFactory </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>;</span><span>

    </span><span>// Add a sketch plane for the curves.    </span><span>
    </span><span>CurveLoop</span><span> loop </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveLoop</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Curve</span><span> currentCurve </span><span>in</span><span> curves</span><span>)</span><span>
    </span><span>{</span><span>
        loop</span><span>.</span><span>Append</span><span>(</span><span>currentCurve</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>SketchPlane</span><span> sketchPlane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> loop</span><span>.</span><span>GetPlane</span><span>());</span><span>
    document</span><span>.</span><span>Regenerate</span><span>();</span><span>

    </span><span>// Add the shadow curves</span><span>
    </span><span>ModelCurveArray</span><span> curveElements </span><span>=</span><span> itemFactory</span><span>.</span><span>NewModelCurveArray</span><span>(</span><span>curves</span><span>,</span><span> sketchPlane</span><span>);</span><span>

    </span><span>// Return the ids of the curves created</span><span>
    </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> curveElementIds </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ModelCurve</span><span> curveElement </span><span>in</span><span> curveElements</span><span>)</span><span>
    </span><span>{</span><span>
        curveElementIds</span><span>.</span><span>Add</span><span>(</span><span>curveElement</span><span>.</span><span>Id</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> curveElementIds</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The utility above above can be used to compute the shadow of a given mass with respect to the current sun and shadows settings for the view:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/shadowcalculator.png)
