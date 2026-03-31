---
created: 2026-01-28T21:08:32 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Connectors_html
author: 
---

# Help | Connectors | Autodesk

> ## Excerpt
> Connectors are associated with a domain - ducts, piping or electrical - which is obtained from the Domain property of a Connector. Connectors are present on mechanical equipment as well as on ducts and pipes.

---
Connectors are associated with a domain - ducts, piping or electrical - which is obtained from the Domain property of a Connector. Connectors are present on mechanical equipment as well as on ducts and pipes.

To traverse a system, you can examine connectors on the base equipment of the system and determine what is attached to the connector by checking the IsConnected property and then the AllRefs property. When looking for a physical connection, it is important to check the ConnectionType of the connector. There are both physical and logical connectors in Revit, but only the physical connectors are visible in the application. The following imagine shows the two types of physical connectors - end connections and curve connectors.

## Connector Creation

Several static methods exist to create connectors. They require a reference to a planar face that will host the connector and, optionally, an edge of that planar face that defines the connector location.

These connectors are created in the family document, and their data is exposed on elements in a project via FamilyInstance.MEPModel.ConnectorManager.

-   CreateCableTrayConnector
-   CreateConduitConnector
-   CreateDuctConnector
-   CreateElectricalConnector
-   CreatePipeConnector

Connectors on MEPCurve and FabricationPart are created by default when a new MEPCurve element is created and cannot be rehosted. Their data are accessed via MEPCurve.ConnectorManager or FabricationPart.ConnectorManager.

## Connector Modification

The `ConnectorElement.ChangeHostReference` method changes the connector host reference by allowing you to specify a reference to a different plane reference, and optionally to an edge. If only a plane reference is specified, the connector position will be able to subsequently move along the plane. If an edge is also specified, then the connector location is fixed in place.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-BBDF045B-E39B-4A5A-9D87-8AFCA7E1F5F3-low.png)**Figure 167: Physical connectors**

The following sample shows how to determine the owner of a connector, and what, if anything it attaches to, along with the connection type.

<table summary="" id="GUID-A41D6151-06A8-4BCB-84B1-6B0338ACC6EA__TABLE_E9824E5167E64B28B657C8145321BEE4"><tbody><tr><td><b>Code Region 30-5: Determine what is attached to a connector</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetElementAtConnector</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Connector</span><span> connector</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>MEPSystem</span><span> mepSystem </span><span>=</span><span> connector</span><span>.</span><span>MEPSystem</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> mepSystem</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Connector is owned by: "</span><span> </span><span>+</span><span> connector</span><span>.</span><span>Owner</span><span>.</span><span>Name</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>connector</span><span>.</span><span>IsConnected</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ConnectorSet</span><span> connectorSet </span><span>=</span><span> connector</span><span>.</span><span>AllRefs</span><span>;</span><span>
            </span><span>ConnectorSetIterator</span><span> csi </span><span>=</span><span> connectorSet</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
            </span><span>while</span><span> </span><span>(</span><span>csi</span><span>.</span><span>MoveNext</span><span>())</span><span>
            </span><span>{</span><span>
                </span><span>Connector</span><span> connected </span><span>=</span><span> csi</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Connector</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> connected</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>// look for physical connections</span><span>
                    </span><span>if</span><span> </span><span>(</span><span>connected</span><span>.</span><span>ConnectorType</span><span> </span><span>==</span><span> </span><span>ConnectorType</span><span>.</span><span>End</span><span> </span><span>||</span><span>
                        connected</span><span>.</span><span>ConnectorType</span><span> </span><span>==</span><span> </span><span>ConnectorType</span><span>.</span><span>Curve</span><span> </span><span>||</span><span>
                        connected</span><span>.</span><span>ConnectorType</span><span> </span><span>==</span><span> </span><span>ConnectorType</span><span>.</span><span>Physical</span><span>)</span><span>
                    </span><span>{</span><span>
                        message </span><span>+=</span><span> </span><span>"\nConnector is connected to: "</span><span> </span><span>+</span><span> connected</span><span>.</span><span>Owner</span><span>.</span><span>Name</span><span>;</span><span>
                        message </span><span>+=</span><span> </span><span>"\nConnection type is: "</span><span> </span><span>+</span><span> connected</span><span>.</span><span>ConnectorType</span><span>;</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            message </span><span>+=</span><span> </span><span>"\nConnector is not connected to anything."</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> message</span><span>);</span><span>            
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following dialog box is the result of running this code example on the connector from a piece of plumbing equipment.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-938B934C-71EB-42CE-8B02-FE2392B5CC3F-low.png)**Figure 168: Connector Information**
