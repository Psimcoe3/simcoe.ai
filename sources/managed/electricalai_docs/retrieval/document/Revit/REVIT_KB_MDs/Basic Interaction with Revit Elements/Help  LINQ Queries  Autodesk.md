---
created: 2026-01-28T20:48:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_LINQ_Queries_html
author: 
---

# Help | LINQ Queries | Autodesk

> ## Excerpt
> In .NET, the FilteredElementCollector class supports the IEnumerable interface for Elements. You can use this class with LINQ queries and operations to process lists of elements. Note that because the ElementFilters and the shortcut methods offered by this class process elements in native code before their managed wrappers are generated, better performance will be obtained by using as many native filters as possible on the collector before attempting to process the results using LINQ queries.

---
In .NET, the FilteredElementCollector class supports the IEnumerable interface for Elements. You can use this class with LINQ queries and operations to process lists of elements. Note that because the ElementFilters and the shortcut methods offered by this class process elements in native code before their managed wrappers are generated, better performance will be obtained by using as many native filters as possible on the collector before attempting to process the results using LINQ queries.

The following example uses an ElementClassFilter to get all FamilyInstance elements in the document, and then uses a LINQ query to narrow down the results to those FamilyInstances with a specific name.

<table summary="" id="GUID-2D0664C5-840E-49F5-B0B9-72F72C2A01A3__TABLE_696F17085098416F9F1EF7F109F66CD6"><tbody><tr><td><b>Code Region 6-15: Using LINQ query</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>LinqSample</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Use ElementClassFilter to find family instances whose name is 60" x 30" Student </span><span>
    </span><span>ElementClassFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>FamilyInstance</span><span>));</span><span>

    </span><span>// Apply the filter to the elements in the active document</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>);</span><span>

    </span><span>// Use Linq query to find family instances whose name is 60" x 30" Student</span><span>
    </span><span>var</span><span> query </span><span>=</span><span> </span><span>from</span><span> element </span><span>in</span><span> collector
                            </span><span>where</span><span> element</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"60\" x 30\" Student"</span><span>
                            </span><span>select</span><span> element</span><span>;</span><span>

    </span><span>// Cast found elements to family instances, </span><span>
    </span><span>// this cast to FamilyInstance is safe because ElementClassFilter for FamilyInstance was used</span><span>
    </span><span>List</span><span>&lt;</span><span>FamilyInstance</span><span>&gt;</span><span> familyInstances </span><span>=</span><span> query</span><span>.</span><span>Cast</span><span>&lt;</span><span>FamilyInstance</span><span>&gt;().</span><span>ToList</span><span>&lt;</span><span>FamilyInstance</span><span>&gt;();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
