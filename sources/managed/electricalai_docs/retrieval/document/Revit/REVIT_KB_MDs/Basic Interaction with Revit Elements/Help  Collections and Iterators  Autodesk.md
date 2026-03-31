---
created: 2026-01-28T20:50:27 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Collections_Collections_and_Iterators_html
author: 
---

# Help | Collections and Iterators | Autodesk

> ## Excerpt
> In the Revit Platform API, Collections and Iterators are generic and type safe.

---
In the Revit Platform API, Collections and Iterators are generic and type safe.

All collections implement the IEnumerable interface and all relevant iterators implement the IEnumerator interface. As a result, all methods and properties are implemented in the Revit Platform API and can play a role in the relevant collections.

Implementing all of the collections is similar. The following example uses ModelCurveArray to demonstrate how to use the main collection properties:

<table summary="" id="GUID-D6F6C00C-B0FF-42E5-9A45-16B4E2D3DC63__TABLE_C8AF48AF0E86477182C069DAE70F94FD"><tbody><tr><td><b>Code Region 9-2: Using collections</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>UsingCollections</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span> 
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

    </span><span>// Store the ModelLine references</span><span>
    </span><span>ModelCurveArray</span><span> lineArray </span><span>=</span><span> </span><span>new</span><span> </span><span>ModelCurveArray</span><span>();</span><span>

    </span><span>// … Store operation</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> id </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>(</span><span>131943</span><span>);</span><span> </span><span>//assume 131943 is a model line element id</span><span>
    lineArray</span><span>.</span><span>Append</span><span>(</span><span>document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>);</span><span>

    </span><span>// use Size property of Array</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Before Insert: "</span><span> </span><span>+</span><span> lineArray</span><span>.</span><span>Size</span><span> </span><span>+</span><span> </span><span>" in lineArray."</span><span>);</span><span>

    </span><span>// use IsEmpty property of Array</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>lineArray</span><span>.</span><span>IsEmpty</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// use Item(int) property of Array</span><span>
        </span><span>ModelCurve</span><span> modelCurve </span><span>=</span><span> lineArray</span><span>.</span><span>get_Item</span><span>(</span><span>0</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelCurve</span><span>;</span><span>

        </span><span>// erase the specific element from the set of elements</span><span>
        selectedIds</span><span>.</span><span>Remove</span><span>(</span><span>modelCurve</span><span>.</span><span>Id</span><span>);</span><span>

        </span><span>// create a new model line and insert to array of model line</span><span>
        </span><span>SketchPlane</span><span> sketchPlane </span><span>=</span><span> modelCurve</span><span>.</span><span>SketchPlane</span><span>;</span><span>

        XYZ startPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>  </span><span>// the start point of the line</span><span>
        XYZ endPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>  </span><span>// the end point of the line</span><span>
        </span><span>// create geometry line</span><span>
        </span><span>Line</span><span> geometryLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>startPoint</span><span>,</span><span> endPoint</span><span>);</span><span>

        </span><span>// create the ModelLine</span><span>
        </span><span>ModelLine</span><span> line </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geometryLine</span><span>,</span><span> sketchPlane</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>;</span><span>

        lineArray</span><span>.</span><span>Insert</span><span>(</span><span>line</span><span>,</span><span> lineArray</span><span>.</span><span>Size</span><span> </span><span>-</span><span> </span><span>1</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"After Insert: "</span><span> </span><span>+</span><span> lineArray</span><span>.</span><span>Size</span><span> </span><span>+</span><span> </span><span>" in lineArray."</span><span>);</span><span>

    </span><span>// use the Clear() method to remove all elements in lineArray</span><span>
    lineArray</span><span>.</span><span>Clear</span><span>();</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"After Clear: "</span><span> </span><span>+</span><span> lineArray</span><span>.</span><span>Size</span><span> </span><span>+</span><span> </span><span>" in lineArray."</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
