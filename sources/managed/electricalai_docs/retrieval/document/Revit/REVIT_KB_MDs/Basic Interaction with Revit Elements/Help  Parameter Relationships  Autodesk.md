---
created: 2026-01-28T20:49:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Parameter_Relationships_html
author: 
---

# Help | Parameter Relationships | Autodesk

> ## Excerpt
> Parameters can be affected by each other.

---
Parameters can be affected by each other.

There are relationships between Parameters where the value of one Parameter can affect:

-   whether another Parameter can be set, or is read-only
-   what parameters are valid for the element
-   the computed value of another parameter

Additionally, some parameters are always read-only.

Some parameters are computed in Revit, such as wall Length and Area parameter. These parameters are always read-only because they depend on the element's internal state.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-B11C1A73-B5DE-4429-B728-C739D963AE1A-low.png)**Figure 29: Wall computed parameters**

In this code sample, the Sill Height parameter for an opening is adjusted, which results in the Head Height parameter being re-computed:

<table summary="" id="GUID-5FCE711C-A73C-434C-AD3E-5B07BEA27CB4__TABLE_A0B3C4D039D749799C1D8E68567358A4"><tbody><tr><td><b>Code Region: Parameter relationship example</b></td></tr><tr><td><pre><code><span>// opening should be an opening such as a window or a door</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>ShowParameterRelationship</span><span>(</span><span>FamilyInstance</span><span> opening</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// get the original Sill Height and Head Height parameters for the opening</span><span>
        </span><span>Parameter</span><span> sillPara </span><span>=</span><span> opening</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>InstanceSillHeightParam</span><span>);</span><span>
        </span><span>Parameter</span><span> headPara </span><span>=</span><span> opening</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>InstanceHeadHeightParam</span><span>);</span><span>
        </span><span>double</span><span> sillHeight </span><span>=</span><span> sillPara</span><span>.</span><span>AsDouble</span><span>();</span><span>
        </span><span>double</span><span> origHeadHeight </span><span>=</span><span> headPara</span><span>.</span><span>AsDouble</span><span>();</span><span>

        </span><span>// Change the Sill Height only and notice that Head Height is recalculated</span><span>
        sillPara</span><span>.</span><span>Set</span><span>(</span><span>sillHeight </span><span>+</span><span> </span><span>2.0</span><span>);</span><span>
        </span><span>double</span><span> newHeadHeight </span><span>=</span><span> headPara</span><span>.</span><span>AsDouble</span><span>();</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Info"</span><span>,</span><span> </span><span>"Old head height: "</span><span> </span><span>+</span><span> origHeadHeight </span><span>+</span><span> </span><span>"; new head height: "</span><span> 
                </span><span>+</span><span> newHeadHeight</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Global parameters also have relationships with other parameters. See the [GlobalParameter Basics](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_GlobalParameter_Basics_html "The GlobalParameter class represents a global parameter in a project document and can be used to create and modify global parameters.") topic for more information.
