---
created: 2026-01-28T21:00:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_Grids_html
author: 
---

# Help | Grids | Autodesk

> ## Excerpt
> The Grid class represents a single grid line within Autodesk Revit.

---
The Grid class represents a single grid line within Autodesk Revit.

Grids are represented by the Grid class which is derived from the DatumPlane class, which is derived from the Element class. It contains all grid properties and methods. The inherited Name property is used to retrieve the content of the grid line's bubble.

### Curve

The Grid class Curve property gets the object that represents the grid line geometry.

-   If the IsCurved property returns true, the Curve property will be an Arc class object.
-   If the IsCurved property returns false, the Curve property will be a Line class object.

For more information, refer to [Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html).

The following code is a simple example using the Grid class. The result appears in a message box after invoking the command.

<table summary="" id="GUID-A1329448-D2AD-4810-94D3-70324DF17D8D__TABLE_2F66636D4B7643B682C58653C7249B83"><tbody><tr><td><b>Code Region 15-3: Using the Grid class</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetInfo_Grid</span><span>(</span><span>Grid</span><span> grid</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Grid : "</span><span>;</span><span>

    </span><span>// Show IsCurved property</span><span>
    message </span><span>+=</span><span> </span><span>"\nIf grid is Arc : "</span><span> </span><span>+</span><span> grid</span><span>.</span><span>IsCurved</span><span>;</span><span>

    </span><span>// Show Curve information</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> curve </span><span>=</span><span> grid</span><span>.</span><span>Curve</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>grid</span><span>.</span><span>IsCurved</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// if the curve is an arc, give center and radius information</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Arc</span><span> arc </span><span>=</span><span> curve </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Arc</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nArc's radius: "</span><span> </span><span>+</span><span> arc</span><span>.</span><span>Radius</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nArc's center:  ("</span><span> </span><span>+</span><span> </span><span>XYZString</span><span>(</span><span>arc</span><span>.</span><span>Center</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>// if the curve is a line, give length information</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Line</span><span> line </span><span>=</span><span> curve </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Line</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nLine's Length: "</span><span> </span><span>+</span><span> line</span><span>.</span><span>Length</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>// Get curve start point</span><span>
    message </span><span>+=</span><span> </span><span>"\nStart point: "</span><span> </span><span>+</span><span> </span><span>XYZString</span><span>(</span><span>curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>));</span><span>
    </span><span>// Get curve end point</span><span>
    message </span><span>+=</span><span> </span><span>"; End point: "</span><span> </span><span>+</span><span> </span><span>XYZString</span><span>(</span><span>curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>));</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span><span>

</span><span>// output the point's three coordinates</span><span>
</span><span>private</span><span> </span><span>string</span><span> </span><span>XYZString</span><span>(</span><span>XYZ point</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>return</span><span> </span><span>"("</span><span> </span><span>+</span><span> point</span><span>.</span><span>X </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Creating a Grid

Two overloaded Create() methods are available in the Grid class to create a new grid in the Revit Platform API. Using the following method with different parameters, you can create a curved or straight grid:

<table summary="" id="GUID-A1329448-D2AD-4810-94D3-70324DF17D8D__TABLE_4F94646184914C36B127FC7AC09C8B8B"><tbody><tr><td><b>Code Region 15-4: Grid.Create()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Grid</span><span> </span><span>Create</span><span>(</span><span> </span><span>Document</span><span> document</span><span>,</span><span> </span><span>Arc</span><span> arc </span><span>);</span><span>
</span><span>public</span><span> </span><span>Grid</span><span> </span><span>Create</span><span>(</span><span> </span><span>Document</span><span> document</span><span>,</span><span> </span><span>Line</span><span> line </span><span>);</span></code></pre></td></tr></tbody></table>

Note: The arc or the line used to create a grid must be in a horizontal plane.

The following code sample illustrates how to create a new grid with a line or an arc.

<table summary="" id="GUID-A1329448-D2AD-4810-94D3-70324DF17D8D__TABLE_468EBA2D159D45D695F10F4AB43E4906"><tbody><tr><td><b>Code Region 15-5: Creating a grid with a line or an arc</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>CreateGrid</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create the geometry line which the grid locates</span><span>
    XYZ start </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ </span><span>end</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>30</span><span>,</span><span> </span><span>30</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Line</span><span> geomLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>start</span><span>,</span><span> </span><span>end</span><span>);</span><span>

    </span><span>// Create a grid using the geometry line</span><span>
    </span><span>Grid</span><span> lineGrid </span><span>=</span><span> </span><span>Grid</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> geomLine</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> lineGrid</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create a new straight grid failed."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Modify the name of the created grid</span><span>
    lineGrid</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"New Name1"</span><span>;</span><span>

    </span><span>// Create the geometry arc which the grid locates</span><span>
    XYZ end0 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ end1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>40</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ pointOnCurve </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>7</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Arc</span><span> geomArc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>end0</span><span>,</span><span> end1</span><span>,</span><span> pointOnCurve</span><span>);</span><span>

    </span><span>// Create a grid using the geometry arc</span><span>
    </span><span>Grid</span><span> arcGrid </span><span>=</span><span> </span><span>Grid</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> geomArc</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> arcGrid</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create a new curved grid failed."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Modify the name of the created grid</span><span>
    arcGrid</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"New Name2"</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: In Revit, the grids are named automatically in a numerical or alphabetical sequence when they are created.
