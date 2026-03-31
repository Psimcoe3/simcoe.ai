---
created: 2026-01-28T20:35:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Walkthrough: Retrieve Filtered Elements | Autodesk

> ## Excerpt
> You can use a filter to select only elements that meet certain criteria. For more information on creating and using element filters, see Element Retrieval.

---
You can use a filter to select only elements that meet certain criteria. For more information on creating and using element filters, see [Element Retrieval](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_Element_Retrieval_html).

This example retrieves all the doors in the document and returns the list of door elements.

<table summary="" id="GUID-5231B53E-DD08-4F05-8BF2-E23E11C314D4__TABLE_1BDED93854BC4A5B9D4795804F23BAE6"><tbody><tr><td><b>Code Region 2-8: Retrieve filtered elements</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> </span><span>CreateLogicAndFilter</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find all door instances in the project by finding all elements that both belong to the door </span><span>
    </span><span>// category and are family instances.</span><span>
    </span><span>ElementClassFilter</span><span> familyInstanceFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>FamilyInstance</span><span>));</span><span>

    </span><span>// Create a category filter for Doors</span><span>
    </span><span>ElementCategoryFilter</span><span> doorsCategoryfilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementCategoryFilter</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Doors</span><span>);</span><span>

    </span><span>// Create a logic And filter for all Door FamilyInstances</span><span>
    </span><span>LogicalAndFilter</span><span> doorInstancesFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>LogicalAndFilter</span><span>(</span><span>familyInstanceFilter</span><span>,</span><span> doorsCategoryfilter</span><span>);</span><span>

    </span><span>// Apply the filter to the elements in the active document</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> doors </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>doorInstancesFilter</span><span>).</span><span>ToElements</span><span>();</span><span>

    </span><span>return</span><span> doors</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
