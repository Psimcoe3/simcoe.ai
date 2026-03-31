---
created: 2026-01-28T21:08:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Element_Creation_Creating_Wires_html
author: 
---

# Help | Creating Wires | Autodesk

> ## Excerpt
> New electrical wires can be created using the Revit API.

---
New electrical wires can be created using the Revit API.

The static Wire.Create() allows for new wires to be created in the document. The Create() method requires the id of the view in which the newly created wire will be visible. It must be the id of a floor plan or reflected ceiling plan view. The WiringType for the wire can be either Arc, for wiring that is concealed within walls, ceilings, or floors, or Chamfer, for wiring that is exposed.

The location of the wire is specified by a list of XYZ points defining the vertices of the wire, and optionally a start and/or end connector. The endpoint connectors can be null, however, if the start connector is specified, the connector's origin will be added to the wire's vertices as the start point. Likewise, if the end connector is specified, the connector's origin will be added to the wire's vertices as the end point. The static method Wire.AreVertexPointsValid() will check a list of XYZ points and start and end connectors to ensure they are suitable for a wire.

The shape of the wire is determined by it's wiring type and the total number of points supplied via the vertex points and endpoint connectors. If the wiring type is WiringType.Arc:

-   If there are 2 total points supplied, the wire is a straight-line wire.
-   If there are 3 total points supplied, the wire is a circular arc wire.
-   If there are 4 or more points, the wire is a spline wire.

If the wiring type is WiringType.Chamfer, a polyline wire will be created connecting all the points.

The following example creates a new straight-line wire in the active view with no connectors specified.

<table summary="" id="GUID-E529A8B2-2104-44F4-8C94-95109EFE35AA__TABLE_5421C731BF84459E860D8DA820244CCA"><tbody><tr><td><b>Code Region: Creating a new wire</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Wire</span><span> </span><span>CreateWire</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Wire</span><span> wire </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> wireTypes </span><span>=</span><span> collector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Wire</span><span>).</span><span>WhereElementIsElementType</span><span>().</span><span>ToElements</span><span>();</span><span>
    </span><span>WireType</span><span> wireType </span><span>=</span><span> wireTypes</span><span>.</span><span>First</span><span>()</span><span> </span><span>as</span><span> </span><span>WireType</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>wireType </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>IList</span><span>&lt;</span><span>XYZ</span><span>&gt;</span><span> wireVertices </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>XYZ</span><span>&gt;();</span><span>
        wireVertices</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>
        wireVertices</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>2</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>

        wire </span><span>=</span><span> </span><span>Wire</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> wireType</span><span>.</span><span>Id</span><span>,</span><span> document</span><span>.</span><span>ActiveView</span><span>.</span><span>Id</span><span>,</span><span> </span><span>WiringType</span><span>.</span><span>Arc</span><span>,</span><span> wireVertices</span><span>,</span><span> </span><span>null</span><span>,</span><span> </span><span>null</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> wire</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Connectors

To connect a wire to elements after creation, call Wire.ConnectTo(), passing in a start and end connector. If the wire is already connected when this method is used, the old connection will be disconnected and the wire will be connected to the new target.

### Vertices

Once a wire is created, vertices can be retrieved using the Wire.GetVertex() method. This method takes an index of the requested vertex which should be between 0 and Wire.NumberOfVertices (which includes the start and end points of the wire).

Use Wire.AppendVertex() to add a vertex to the end of the list, or Wire.InsertVertex() to add a vertex at a specific point in the list. The Wire.IsVertexPointValid() method checks if the given vertex point can be added to this wire. IsVertexPointValid() will return false if the point cannot be added because there is already a vertex at this position on the view plane (within tolerance). Note that a vertex cannot be inserted before the start vertex if the start vertex already connects to an element. Similarly, a vertex cannot be appended to the end of the list if the end point is already connected to an element.

Wire.RemoveVertex() will remove a vertex from the list. If the wire vertex is already connected to an element, this method will fail to remove the vertex. In order to remove this vertex, it should be disconnected first, then removed, and then reconnected (if required).
