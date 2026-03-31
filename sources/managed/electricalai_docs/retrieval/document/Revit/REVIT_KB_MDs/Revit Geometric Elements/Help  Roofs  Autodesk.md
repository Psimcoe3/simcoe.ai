---
created: 2026-01-28T21:04:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Roofs_html
author: 
---

# Help | Roofs | Autodesk

> ## Excerpt
> Representation of roofs in the Revit API.

---
Representation of roofs in the Revit API.

Roofs in the Revit Platform API all derive from the RoofBase object. There are two classes:

-   FootPrintRoof - represents a roof made from a building footprint
-   ExtrusionRoof - represents roof made from an extruded profile

Both have a RoofType property that gets or sets the type of roof. This example shows how you can create a footprint roof based on some selected walls:

<table summary="" id="GUID-33E6A6BD-96AA-4FAF-B660-1DD0C06CCD29__TABLE_9CC9AA615AA2427880945521FA9EACFA"><tbody><tr><td><b>Code Region 11-3: Creating a footprint roof</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateRoof</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Before invoking this sample, select some walls to add a roof over.</span><span>
    </span><span>// Make sure there is a level named "Roof" in the document.</span><span>

    </span><span>// find the Roof level</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Level</span><span>));</span><span>
    </span><span>var</span><span> elements </span><span>=</span><span> </span><span>from</span><span> element </span><span>in</span><span> collector </span><span>where</span><span> element</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Roof"</span><span> </span><span>select</span><span> element</span><span>;</span><span>
    </span><span>Level</span><span> level </span><span>=</span><span> elements</span><span>.</span><span>Cast</span><span>&lt;</span><span>Level</span><span>&gt;().</span><span>ElementAt</span><span>&lt;</span><span>Level</span><span>&gt;(</span><span>0</span><span>);</span><span>

    collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>RoofType</span><span>));</span><span>
    </span><span>RoofType</span><span> roofType </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>RoofType</span><span>;</span><span> 

    </span><span>// Get the handle of the application</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>;</span><span>

    </span><span>// Define the footprint for the roof based on user selection</span><span>
    </span><span>CurveArray</span><span> footprint </span><span>=</span><span> application</span><span>.</span><span>Create</span><span>.</span><span>NewCurveArray</span><span>();</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>selectedIds</span><span>.</span><span>Count</span><span> </span><span>!=</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Element</span><span> element </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
            </span><span>Wall</span><span> wall </span><span>=</span><span> element </span><span>as</span><span> </span><span>Wall</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>wall </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>LocationCurve</span><span> wallCurve </span><span>=</span><span> wall</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
                footprint</span><span>.</span><span>Append</span><span>(</span><span>wallCurve</span><span>.</span><span>Curve</span><span>);</span><span>
                </span><span>continue</span><span>;</span><span>
            </span><span>}</span><span>

            </span><span>ModelCurve</span><span> modelCurve </span><span>=</span><span> element </span><span>as</span><span> </span><span>ModelCurve</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>modelCurve </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                footprint</span><span>.</span><span>Append</span><span>(</span><span>modelCurve</span><span>.</span><span>GeometryCurve</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"You should select a curve loop, or a wall loop, or loops combination \nof walls and curves to create a footprint roof."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>ModelCurveArray</span><span> footPrintToModelCurveMapping </span><span>=</span><span> </span><span>new</span><span> </span><span>ModelCurveArray</span><span>();</span><span>
    </span><span>FootPrintRoof</span><span> footprintRoof </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFootPrintRoof</span><span>(</span><span>footprint</span><span>,</span><span> level</span><span>,</span><span> roofType</span><span>,</span><span> </span><span>out</span><span> footPrintToModelCurveMapping</span><span>);</span><span>
    </span><span>ModelCurveArrayIterator</span><span> iterator </span><span>=</span><span> footPrintToModelCurveMapping</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
    iterator</span><span>.</span><span>Reset</span><span>();</span><span>
    </span><span>while</span><span> </span><span>(</span><span>iterator</span><span>.</span><span>MoveNext</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>ModelCurve</span><span> modelCurve </span><span>=</span><span> iterator</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>ModelCurve</span><span>;</span><span>
        footprintRoof</span><span>.</span><span>set_DefinesSlope</span><span>(</span><span>modelCurve</span><span>,</span><span> </span><span>true</span><span>);</span><span>
        footprintRoof</span><span>.</span><span>set_SlopeAngle</span><span>(</span><span>modelCurve</span><span>,</span><span> </span><span>0.5</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

For an example of how to create an ExtrusionRoof, see the NewRoof sample application included with the Revit API SDK.

### Gutter and Fascia

Gutter and Fascia elements are derived from the HostedSweep class, which represents a roof. They can be created, deleted or modified via the API. To create these elements, use one of the Document.Create.NewFascia() or Document.Create.NewGutter() overrides. For an example of how to create new gutters and fascia, see the NewHostedSweep application included in the SDK samples. Below is a code snippet showing you can modify a gutter element's properties.

<table summary="" id="GUID-33E6A6BD-96AA-4FAF-B660-1DD0C06CCD29__TABLE_F7ADB54D499C440AB8A9183491470E2D"><tbody><tr><td><b>Code Region 11-4: Modifying a gutter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ModifyGutter</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> elem </span><span>in</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>().</span><span>Select</span><span>(</span><span>q </span><span>=&gt;</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>q</span><span>)))</span><span>
        </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>elem </span><span>is</span><span> </span><span>Gutter</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>Gutter</span><span> gutter </span><span>=</span><span> elem </span><span>as</span><span> </span><span>Gutter</span><span>;</span><span>
                        </span><span>// convert degrees to rads:</span><span>
                        gutter</span><span>.</span><span>Angle</span><span> </span><span>=</span><span> </span><span>45.00</span><span> </span><span>*</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>180</span><span>;</span><span>
                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Changed gutter angle"</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
