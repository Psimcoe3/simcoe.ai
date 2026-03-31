---
created: 2026-01-28T21:08:40 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Family_Creation_html
author: 
---

# Help | Family Creation | Autodesk

> ## Excerpt
> When creating mechanical equipment in a Revit family document, you will need to add connectors to allow the equipment to connect to a system. Duct, electrical and pipe connectors can all be added similarly, using a reference plane where the connector will be placed and a system type for the connector.

---
When creating mechanical equipment in a Revit family document, you will need to add connectors to allow the equipment to connect to a system. Duct, electrical and pipe connectors can all be added similarly, using a reference plane where the connector will be placed and a system type for the connector.

The overloaded static methods provided by the ConnectorElement class are:

-   CreateCableTrayConnector
-   CreateConduitConnector
-   CreateDuctConnector
-   CreateElectricalConnector
-   CreatePipeConnector

Each of the methods above has a second overload that takes an additional Edge parameter that allows creation of connector elements centered on internal loops of a given face. The following code demonstrates how to add two pipe connectors to faces on an extrusion and set some properties on them.

<table summary="" id="GUID-81E296BE-A292-4979-B57E-730683178E6C__TABLE_D944BABE67A4400DB87E2D09E5772F32"><tbody><tr><td><b>Code Region 30-6: Adding a pipe connector</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreatePipeConnectors</span><span>(</span><span>UIDocument</span><span> uiDocument</span><span>,</span><span> </span><span>Extrusion</span><span> extrusion</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// get the faces of the extrusion</span><span>
        </span><span>Options</span><span> geoOptions </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewGeometryOptions</span><span>();</span><span>
        geoOptions</span><span>.</span><span>View</span><span> </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>.</span><span>ActiveView</span><span>;</span><span>
        geoOptions</span><span>.</span><span>ComputeReferences</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>

        </span><span>List</span><span>&lt;</span><span>PlanarFace</span><span>&gt;</span><span> planarFaces </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>PlanarFace</span><span>&gt;();</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geoElement </span><span>=</span><span> extrusion</span><span>.</span><span>get_Geometry</span><span>(</span><span>geoOptions</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geoObject </span><span>in</span><span> geoElement</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Solid</span><span> geoSolid </span><span>=</span><span> geoObject </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> geoSolid</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> geoFace </span><span>in</span><span> geoSolid</span><span>.</span><span>Faces</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>if</span><span> </span><span>(</span><span>geoFace </span><span>is</span><span> </span><span>PlanarFace</span><span>)</span><span>
                                </span><span>{</span><span>
                                        planarFaces</span><span>.</span><span>Add</span><span>(</span><span>geoFace </span><span>as</span><span> </span><span>PlanarFace</span><span>);</span><span>
                                </span><span>}</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>if</span><span> </span><span>(</span><span>planarFaces</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>1</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Create the Supply Hydronic pipe connector</span><span>
                </span><span>ConnectorElement</span><span> connSupply </span><span>=</span><span> </span><span>ConnectorElement</span><span>.</span><span>CreatePipeConnector</span><span>(</span><span>uiDocument</span><span>.</span><span>Document</span><span>,</span><span>
                                                                                   </span><span>PipeSystemType</span><span>.</span><span>SupplyHydronic</span><span>,</span><span>
                                                                                   planarFaces</span><span>[</span><span>0</span><span>].</span><span>Reference</span><span>);</span><span>
                </span><span>Parameter</span><span> param </span><span>=</span><span> connSupply</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>ConnectorRadius</span><span>);</span><span>
                param</span><span>.</span><span>Set</span><span>(</span><span>1.0</span><span>);</span><span> </span><span>// 1' radius</span><span>
                param </span><span>=</span><span> connSupply</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>RbsPipeFlowDirectionParam</span><span>);</span><span>
                param</span><span>.</span><span>Set</span><span>(</span><span>2</span><span>);</span><span>

                </span><span>// Create the Return Hydronic pipe connector</span><span>
                </span><span>ConnectorElement</span><span> connReturn </span><span>=</span><span>  </span><span>ConnectorElement</span><span>.</span><span>CreatePipeConnector</span><span>(</span><span>uiDocument</span><span>.</span><span>Document</span><span>,</span><span>
                                                                                    </span><span>PipeSystemType</span><span>.</span><span>ReturnHydronic</span><span>,</span><span>
                                                                                    planarFaces</span><span>[</span><span>1</span><span>].</span><span>Reference</span><span>);</span><span>
                param </span><span>=</span><span> connReturn</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>ConnectorRadius</span><span>);</span><span>
                param</span><span>.</span><span>Set</span><span>(</span><span>0.5</span><span>);</span><span> </span><span>// 6" radius</span><span>
                param </span><span>=</span><span> connReturn</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>RbsPipeFlowDirectionParam</span><span>);</span><span>
                param</span><span>.</span><span>Set</span><span>(</span><span>1</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following illustrates the result of running this example using in a new family document created using a Mechanical Equipment template and passing in an extrusion 2'×2'×1'. Note that the connectors are placed at the centroid of the planar faces.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-9971E21F-AE7B-4FF3-9251-A91C6DEAA663-low.png)**Figure 169: Two connectors created on an extrusion**
