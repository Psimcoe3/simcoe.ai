---
created: 2026-01-28T20:58:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_FamilySymbol_html
author: 
---

# Help | FamilySymbol | Autodesk

> ## Excerpt
> The FamilySymbol class represents a single Type within a Family.

---
The FamilySymbol class represents a single Type within a Family.

Each family can contain one or more family symbols. Each FamilyInstance has an associated FamilySymbol which can be accessed from its Symbol property.

### Thermal Properties

Certain types of families (doors, windows, and curtain wall panels) contain thermal properties as shown in the Type Properties window below for a window.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/FamilyThermalProperties2-76173.jpg)The thermal properties for a FamilySymbol are represented by the FamilyThermalProperties class and are retrieved using the FamilySymbol.GetThermalProperties() method. The FamilyThermalProperties for a FamilySymbol can be set using SetThermalProperties(). The properties of the FamilyThermalProperties class itself are read-only.

The units for the calculated values are shown in the table below.

<table summary="" id="GUID-F3F98CE6-4009-4046-BCA1-A7899CAB625C__TABLE_BB97EDC937124B74A3749A88B15045D6"><tbody><tr><td><b>Property</b></td><td><b>Unit</b></td></tr><tr><td>HeatTransferCoefficient</td><td>watts per meter-squared kelvin<p>(W/(m^2*K)</p></td></tr><tr><td>ThermalResistance</td><td>meter-squared kelvin per watt<p>((m^2*K)/Watt)</p></td></tr></tbody></table>

The AnalyticConstructionTypeId property is the construction gbXML type and returns the value that corresponds to the 'id' property of a constructionType node in Constructions.xml. The static FamilyThermalProperties.Find() method will find the FamilyThermalProperties by the 'id' property of a constructionType node in Constructions.xml.

### FamilyType Parameters

Some parameters for a FamilySymbol may be FamilyType parameters. For these parameters, the Family.GetFamilyTypeParameterValues() method can be used to get all applicable values for the parameter. The values returned are ElementIds of all family types that match the category specified by the definition of the given parameter. The elements are either of class ElementType or NestedFamilyTypeReference. The second variant is for the types that are nested in families and therefore not accessible otherwise. The NestedFamilyTypeReference element stores only basic information about the nested FamilyType, such as the name of the Type, name of the Family, and a Category. These elements are very low-level and thus bypassed by standard element filters, so the main way to get them is via the Family.GetFamilyTypeParameterValues() method.

The following example demonstrates how to get all the family type parameter values for a FamilyType parameter of a FamilySymbol. The value for the parameter is then changed to another value. This change affects all FamilyInstances using the loaded FamilySymbol.

<table summary="" id="GUID-F3F98CE6-4009-4046-BCA1-A7899CAB625C__TABLE_5421C731BF84459E860D8DA820244CCA"><tbody><tr><td><b>Code Region: Get nested FamilyTypes</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetNestedFamilyTypes</span><span>(</span><span>FamilyInstance</span><span> instance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// find one FamilyType parameter and all values applicable to it</span><span>
    </span><span>Parameter</span><span> aTypeParam </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> values </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>Family</span><span> family </span><span>=</span><span> instance</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>Parameter</span><span> param </span><span>in</span><span> instance</span><span>.</span><span>Symbol</span><span>.</span><span>Parameters</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>ForgeTypeId</span><span> forgeTypeId </span><span>=</span><span> param</span><span>.</span><span>Definition</span><span>.</span><span>GetDataType</span><span>();</span><span>
        </span><span>if</span><span> </span><span>(</span><span>Category</span><span>.</span><span>IsBuiltInCategory</span><span>(</span><span>forgeTypeId</span><span>))</span><span>
        </span><span>{</span><span>
            aTypeParam </span><span>=</span><span> param</span><span>;</span><span>
            values </span><span>=</span><span> family</span><span>.</span><span>GetFamilyTypeParameterValues</span><span>(</span><span>param</span><span>.</span><span>Id</span><span>);</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>if</span><span> </span><span>(</span><span>aTypeParam </span><span>==</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Warning"</span><span>,</span><span> </span><span>"The selected family has no FamilyType parameter defined."</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>values </span><span>==</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"A FamilyType parameter does not have any applicable values!?"</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>ElementId</span><span> newValue </span><span>=</span><span> values</span><span>.</span><span>Last</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
        </span><span>if</span><span> </span><span>(</span><span>newValue </span><span>!=</span><span> aTypeParam</span><span>.</span><span>AsElementId</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>instance</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Setting parameter value"</span><span>))</span><span>
            </span><span>{</span><span>
                trans</span><span>.</span><span>Start</span><span>();</span><span>
                aTypeParam</span><span>.</span><span>Set</span><span>(</span><span>newValue</span><span>);</span><span>
                trans</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
