---
created: 2026-01-28T21:08:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Element_Creation_Creating_Systems_html
author: 
---

# Help | Creating Systems | Autodesk

> ## Excerpt
> Create electrical, mechanical and piping systems.

---
Create electrical, mechanical and piping systems.

MechanicalSystem and PipingSystem have static overloaded Create() methods to create new mechanical or piping systems. This is the preferred method for creating new MEP Systems. The simplest Create() overload for both classes creates a new system in a given document with a given type Id (which should be the Id for a DuctSystemType for a MechanicalSystem or the Id of a PipeSystemType for a PipingSystem. Both classes have a second Create() overload that also takes a name for the system. Once created, elements can be added to the system using the MEPSystem.Add() method.

MechanicalSystem and PipingSystem can also be created from the Creation.Document class using NewMechanicalSystem() and NewPipingSystem(). NewPipingSystem() and NewMechanicalSystem() both take a Connector that is the base equipment connector, such as a hot water heater for a piping system, or a fan for a mechanical system. They also take a ConnectorSet of connectors that will be added to the system, such as faucets on sinks in a piping system. The last piece of information required to create a new system is either a PipeSystemType for NewPipingSystem() or a DuctSystemType for NewMechanicalSystem().

Electrical systems can be created using the ElectricalSystem.Create method, which has two overloads. One creates a new ElectricalSystem element from an unused Connector. The other creates a new ElectricalSystem element from a set of electrical components. Both overloads require an ElectricalSystemType.

In the following sample, a new SupplyAir duct system is created from a selected piece of mechanical equipment (such as a fan) and all selected Air Terminals.

<table summary="" id="GUID-A3BD9AE5-8A17-4976-B47D-2A969EE6F58E__TABLE_B73A4F64958E4B84A9F29925ED840E45"><tbody><tr><td><b>Code Region: Creating a new mechanical system</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateSystem</span><span>(</span><span>UIDocument</span><span> uiDocument</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// create a connector set for new mechanical system</span><span>
    </span><span>ConnectorSet</span><span> connectorSet </span><span>=</span><span> </span><span>new</span><span> </span><span>ConnectorSet</span><span>();</span><span>
    </span><span>// Base equipment connector</span><span>
    </span><span>Connector</span><span> baseConnector </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// Select a Parallel Fan Powered VAV and some Supply Diffusers</span><span>
    </span><span>// prior to running this example</span><span>
    </span><span>ConnectorSetIterator</span><span> csi </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uiDocument</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>
    </span><span>Document</span><span> document </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> e </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>e </span><span>is</span><span> </span><span>FamilyInstance</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FamilyInstance</span><span> </span><span>fi</span><span> </span><span>=</span><span> e </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
            </span><span>Family</span><span> family </span><span>=</span><span> </span><span>fi</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>
            </span><span>// Assume the selected Mechanical Equipment is the base equipment for new system</span><span>
            </span><span>if</span><span> </span><span>(</span><span>family</span><span>.</span><span>FamilyCategory</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Mechanical Equipment"</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>//Find the "Out" and "SupplyAir" connector on the base equipment</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> </span><span>fi</span><span>.</span><span>MEPModel</span><span>)</span><span>
                </span><span>{</span><span>
                    csi </span><span>=</span><span> </span><span>fi</span><span>.</span><span>MEPModel</span><span>.</span><span>ConnectorManager</span><span>.</span><span>Connectors</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
                    </span><span>while</span><span> </span><span>(</span><span>csi</span><span>.</span><span>MoveNext</span><span>())</span><span>
                    </span><span>{</span><span>
                        </span><span>Connector</span><span> conn </span><span>=</span><span> csi</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Connector</span><span>;</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>conn</span><span>.</span><span>Direction</span><span> </span><span>==</span><span> </span><span>FlowDirectionType</span><span>.</span><span>Out</span><span> </span><span>&amp;&amp;</span><span> conn</span><span>.</span><span>DuctSystemType</span><span> </span><span>==</span><span> </span><span>DuctSystemType</span><span>.</span><span>SupplyAir</span><span>)</span><span>
                        </span><span>{</span><span>
                            baseConnector </span><span>=</span><span> conn</span><span>;</span><span>
                            </span><span>break</span><span>;</span><span>
                        </span><span>}</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>family</span><span>.</span><span>FamilyCategory</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Air Terminals"</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// add selected Air Terminals to connector set for new mechanical system</span><span>
                csi </span><span>=</span><span> </span><span>fi</span><span>.</span><span>MEPModel</span><span>.</span><span>ConnectorManager</span><span>.</span><span>Connectors</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
                csi</span><span>.</span><span>MoveNext</span><span>();</span><span>
                connectorSet</span><span>.</span><span>Insert</span><span>(</span><span>csi</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Connector</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>MechanicalSystem</span><span> mechanicalSys </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> baseConnector </span><span>&amp;&amp;</span><span> connectorSet</span><span>.</span><span>Size</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// create a new SupplyAir mechanical system</span><span>
        mechanicalSys </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>.</span><span>Create</span><span>.</span><span>NewMechanicalSystem</span><span>(</span><span>baseConnector</span><span>,</span><span> connectorSet</span><span>,</span><span> </span><span>DuctSystemType</span><span>.</span><span>SupplyAir</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
