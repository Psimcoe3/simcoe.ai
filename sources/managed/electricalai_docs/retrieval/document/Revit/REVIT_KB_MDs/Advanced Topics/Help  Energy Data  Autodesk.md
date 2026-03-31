---
created: 2026-01-28T21:15:07 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Energy_Data_html
author: 
---

# Help | Energy Data | Autodesk

> ## Excerpt
> The EnergyDataSettings object contains settings for gbXML Export and Heating and Cooling Load Calculations and project level settings for Conceptual Energy Analysis.

---
The EnergyDataSettings object contains settings for gbXML Export and Heating and Cooling Load Calculations and project level settings for Conceptual Energy Analysis.

The EnergyDataSettings object is derived from the Element base object. It is unique in each project, similar to ProjectInformation. Though EnergyDataSettings is a subclass of the Element class, most of the members inherited from the Element return null or an empty set except for Name, Id, UniqueId, and Parameters.

The following code sample uses the EnergyDataSettings class. The result appears in a TaskDialog after invoking the command.

<table summary="" id="GUID-C42BBD66-25E9-48C6-ABF6-001303791615__TABLE_885CE8BC60714083A07723EAA8EED263"><tbody><tr><td><b>Code Region 28-7: Using the EnergyDataSettings class</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetInfo_EnergyData</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>EnergyDataSettings</span><span> energyData </span><span>=</span><span> </span><span>EnergyDataSettings</span><span>.</span><span>GetFromDocument</span><span>(</span><span>document</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> energyData</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>string</span><span> message </span><span>=</span><span> </span><span>"energyData : "</span><span>;</span><span>
                message </span><span>+=</span><span> </span><span>"\nBuildingType : "</span><span> </span><span>+</span><span> energyData</span><span>.</span><span>BuildingType</span><span>;</span><span>
                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> message</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
