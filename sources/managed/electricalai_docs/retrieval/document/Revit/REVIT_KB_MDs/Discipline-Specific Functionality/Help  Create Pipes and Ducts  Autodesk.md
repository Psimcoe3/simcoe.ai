---
created: 2026-01-28T21:08:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Element_Creation_Create_Pipes_and_Ducts_html
author: 
---

# Help | Create Pipes and Ducts | Autodesk

> ## Excerpt
> There are 3 ways to create new ducts, flex ducts, pipes and flex pipes. They can be created between two points, between two connectors, or between a point and a connector.

---
There are 3 ways to create new ducts, flex ducts, pipes and flex pipes. They can be created between two points, between two connectors, or between a point and a connector.

The following code creates a new pipe between two points using the Pipe.Create() method. New flex pipes, ducts and flex ducts can all be created similarly.

<table summary="" id="GUID-0B91BAE8-59FD-4D4B-84E6-53B6A21DE00A__TABLE_629FE6ABDA5B4E2AB6D5B0C751A762BE"><tbody><tr><td><b>Code Region: Creating a new Pipe using static Create() method</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Pipe</span><span> </span><span>CreateNewPipe</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>ElementId</span><span> systemTypeId</span><span>,</span><span> </span><span>ElementId</span><span> levelId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// find a pipe type</span><span>

    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>PipeType</span><span>));</span><span>
    </span><span>PipeType</span><span> pipeType </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>PipeType</span><span>;</span><span>

    </span><span>Pipe</span><span> pipe </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> pipeType</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// create pipe between 2 points</span><span>
        XYZ p1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ p2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>

        pipe </span><span>=</span><span> </span><span>Pipe</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> systemTypeId</span><span>,</span><span> pipeType</span><span>.</span><span>Id</span><span>,</span><span> levelId</span><span>,</span><span> p1</span><span>,</span><span> p2</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> pipe</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The code region below demonstrates how to create a FlexPipe using the static FlexPipe.Create() method. Pipes, ducts and flex ducts can all be created between two points similarly.

<table summary="" id="GUID-0B91BAE8-59FD-4D4B-84E6-53B6A21DE00A__TABLE_F0DB25A497FD4C038875DAFA6DEDBB62"><tbody><tr><td><b>Code Region: Creating a new FlexPipe using static Create() method</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>FlexPipe</span><span> </span><span>CreateFlexPipe</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Level</span><span> level</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// find a pipe type</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FlexPipeType</span><span>));</span><span>
    </span><span>ElementId</span><span> pipeTypeId </span><span>=</span><span> collector</span><span>.</span><span>FirstElementId</span><span>();</span><span>

    </span><span>// find a pipe system type</span><span>
    </span><span>FilteredElementCollector</span><span> sysCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    sysCollector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>PipingSystemType</span><span>));</span><span>
    </span><span>ElementId</span><span> pipeSysTypeId </span><span>=</span><span> sysCollector</span><span>.</span><span>FirstElementId</span><span>();</span><span>

    </span><span>FlexPipe</span><span> pipe </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>pipeTypeId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span> </span><span>&amp;&amp;</span><span> pipeSysTypeId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// create flex pipe with 3 points</span><span>
        </span><span>List</span><span>&lt;</span><span>XYZ</span><span>&gt;</span><span> points </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>XYZ</span><span>&gt;();</span><span>
        points</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>
        points</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>));</span><span>
        points</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>

        pipe </span><span>=</span><span> </span><span>FlexPipe</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> pipeSysTypeId</span><span>,</span><span> pipeTypeId</span><span>,</span><span> level</span><span>.</span><span>Id</span><span>,</span><span> points</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> pipe</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

After creating a pipe, you might want to change the diameter. The Diameter property of Pipe is read-only. To change the diameter, get the RBS\_PIPE\_DIAMETER\_PARAM built-in parameter.

<table summary="" id="GUID-0B91BAE8-59FD-4D4B-84E6-53B6A21DE00A__TABLE_FEBF3895FB4F4222B6C2BB56524CDDBE"><tbody><tr><td><b>Code Region: Changing pipe diameter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ChangePipeSize</span><span>(</span><span>Pipe</span><span> pipe</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Parameter</span><span> parameter </span><span>=</span><span> pipe</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>RbsPipeDiameterParam</span><span>);</span><span>

        </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Pipe diameter: "</span><span> </span><span>+</span><span> parameter</span><span>.</span><span>AsValueString</span><span>();</span><span>

        parameter</span><span>.</span><span>Set</span><span>(</span><span>0.5</span><span>);</span><span> </span><span>// set to 6"</span><span>

        </span><span>// Regenerate the docucment before trying to read a parameter that has been edited</span><span>
        pipe</span><span>.</span><span>Document</span><span>.</span><span>Regenerate</span><span>();</span><span>

        message </span><span>+=</span><span> </span><span>"\nPipe diameter after set: "</span><span> </span><span>+</span><span> parameter</span><span>.</span><span>AsValueString</span><span>();</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Another common way to create a new duct or pipe is between two existing connectors, as the following example demonstrates. In this example, it is assumed that 2 elements with connectors have been selected in Revit, one being a piece of mechanical equipment and the other a duct fitting with a connector that lines up with the SupplyAir connector on the equipment.

<table summary="" id="GUID-0B91BAE8-59FD-4D4B-84E6-53B6A21DE00A__TABLE_82FB37180A8B4D1BB713AB2CE9F8F78F"><tbody><tr><td><b>Code Region: Adding a duct between two connectors</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Duct</span><span> </span><span>CreateDuctBetweenConnectors</span><span>(</span><span>UIDocument</span><span> uiDocument</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// prior to running this example</span><span>
    </span><span>// select some mechanical equipment with a supply air connector</span><span>
    </span><span>// and an elbow duct fitting with a connector in line with that connector</span><span>
    </span><span>ElementId</span><span> levelId </span><span>=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>;</span><span>
    </span><span>Connector</span><span> connector1 </span><span>=</span><span> </span><span>null</span><span>,</span><span> connector2 </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ConnectorSetIterator</span><span> csi </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uiDocument</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>
    </span><span>Document</span><span> document </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>// First find the selected equipment and get the correct connector</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> e </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>e </span><span>is</span><span> </span><span>FamilyInstance</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FamilyInstance</span><span> </span><span>fi</span><span> </span><span>=</span><span> e </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
            </span><span>Family</span><span> family </span><span>=</span><span> </span><span>fi</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>family</span><span>.</span><span>FamilyCategory</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Mechanical Equipment"</span><span>)</span><span>
            </span><span>{</span><span>
                csi </span><span>=</span><span> </span><span>fi</span><span>.</span><span>MEPModel</span><span>.</span><span>ConnectorManager</span><span>.</span><span>Connectors</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
                </span><span>while</span><span> </span><span>(</span><span>csi</span><span>.</span><span>MoveNext</span><span>())</span><span>
                </span><span>{</span><span>
                    </span><span>Connector</span><span> conn </span><span>=</span><span> csi</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Connector</span><span>;</span><span>
                    </span><span>if</span><span> </span><span>(</span><span>conn</span><span>.</span><span>Direction</span><span> </span><span>==</span><span> </span><span>FlowDirectionType</span><span>.</span><span>Out</span><span> </span><span>&amp;&amp;</span><span> 
                        conn</span><span>.</span><span>DuctSystemType</span><span> </span><span>==</span><span> </span><span>DuctSystemType</span><span>.</span><span>SupplyAir</span><span>)</span><span>
                    </span><span>{</span><span>
                        connector1 </span><span>=</span><span> conn</span><span>;</span><span>
                        levelId </span><span>=</span><span> family</span><span>.</span><span>LevelId</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>// next find the second selected item to connect to</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> e </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>e </span><span>is</span><span> </span><span>FamilyInstance</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FamilyInstance</span><span> </span><span>fi</span><span> </span><span>=</span><span> e </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
            </span><span>Family</span><span> family </span><span>=</span><span> </span><span>fi</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>family</span><span>.</span><span>FamilyCategory</span><span>.</span><span>Name</span><span> </span><span>!=</span><span> </span><span>"Mechanical Equipment"</span><span>)</span><span>
            </span><span>{</span><span>
                csi </span><span>=</span><span> </span><span>fi</span><span>.</span><span>MEPModel</span><span>.</span><span>ConnectorManager</span><span>.</span><span>Connectors</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
                </span><span>while</span><span> </span><span>(</span><span>csi</span><span>.</span><span>MoveNext</span><span>())</span><span>
                </span><span>{</span><span>
                    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> connector2</span><span>)</span><span>
                    </span><span>{</span><span>
                        </span><span>Connector</span><span> conn </span><span>=</span><span> csi</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Connector</span><span>;</span><span>

                        </span><span>// make sure to choose the connector in line with the first connector</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>Math</span><span>.</span><span>Abs</span><span>(</span><span>conn</span><span>.</span><span>Origin</span><span>.</span><span>Y </span><span>-</span><span> connector1</span><span>.</span><span>Origin</span><span>.</span><span>Y</span><span>)</span><span> </span><span>&lt;</span><span> </span><span>0.001</span><span>)</span><span>
                        </span><span>{</span><span>
                            connector2 </span><span>=</span><span> conn</span><span>;</span><span>
                            </span><span>break</span><span>;</span><span>
                        </span><span>}</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>Duct</span><span> duct </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> connector1 </span><span>&amp;&amp;</span><span> </span><span>null</span><span> </span><span>!=</span><span> connector2 </span><span>&amp;&amp;</span><span> levelId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// find a duct type</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>uiDocument</span><span>.</span><span>Document</span><span>);</span><span>
        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>DuctType</span><span>));</span><span>

        </span><span>// Use Linq query to make sure it is one of the rectangular duct types</span><span>
        </span><span>var</span><span> query </span><span>=</span><span> </span><span>from</span><span> element </span><span>in</span><span> collector
                    </span><span>where</span><span> element</span><span>.</span><span>Name</span><span>.</span><span>Contains</span><span>(</span><span>"Mitered Elbows"</span><span>)</span><span> </span><span>==</span><span> </span><span>true</span><span>
                    </span><span>select</span><span> element</span><span>;</span><span>

        </span><span>// use extension methods to get first duct type</span><span>
        </span><span>DuctType</span><span> ductType </span><span>=</span><span> collector</span><span>.</span><span>Cast</span><span>&lt;</span><span>DuctType</span><span>&gt;().</span><span>First</span><span>&lt;</span><span>DuctType</span><span>&gt;();</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> ductType</span><span>)</span><span>
        </span><span>{</span><span>
            duct </span><span>=</span><span> </span><span>Duct</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> ductType</span><span>.</span><span>Id</span><span>,</span><span> levelId</span><span>,</span><span> connector1</span><span>,</span><span> connector2</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> duct</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Lining and Insulation

Pipe and duct insulation and lining can be added as separate objects associated with ducts and pipes. The ids of insulation elements associated with a duct or pipe can be retrieved using the static method InsulationLiningBase.GetInsulationIds() while the ids of lining elements can be retreived using the static method InsulationLiningBase.GetLiningIds().

To create new insulations associated with a given duct, pipe, fitting, accessory, or content use the corresponding static method: DuctInsulation.Create() or PipeInsulation.Create(). DuctLining.Create() can be used to create a new instance of a lining applied to the inside of a given duct, fitting or accessory.
