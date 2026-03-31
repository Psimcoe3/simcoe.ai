---
created: 2026-01-28T20:48:28 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Element_Intersection_Filters_html
author: 
---

# Help | Element Intersection Filters | Autodesk

> ## Excerpt
> The element filters:

---
The element filters:

-   ElementIntersectsElementFilter
-   ElementIntersectsSolidFilter

pass elements whose actual 3D geometry intersects the 3D geometry of the target object.

With ElementIntersectsElementFilter, the target object is another element. The intersection is determined with the same logic used by Revit to determine if an interference exists during generation of an Interference Report. (This means that some combinations of elements will never pass this filter, such as concrete members which are automatically joined at their intersections, or site elements which are also excluded from interference checks). Also, elements which have no solid geometry, such as Rebar, will not pass this filter.

With ElementIntersectsSolidFilter, the target object is any solid. This solid could have been obtained from an existing element, created from scratch using the routines in GeometryCreationUtilities, or the result of a secondary operation such as a Boolean operation. Similar to the ElementIntersectsElementFilter, this filter will not pass elements which lack solid geometry.

Both filters can be inverted to match elements outside the target object volume.

Both filters are slow filters, and thus are best combined with one or more quick filters such as class or category filters.

<table summary="" id="GUID-2DE34D37-912E-475F-B3E0-BE40D88C8875__TABLE_074B6F03965549DE90BF60FFB33347F3"><tbody><tr><td><b>Code region: using ElementIntersectsSolidFilter to match elements which block disabled egress to doors</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Finds any Revit physical elements which interfere with the target </span><span>
</span><span>/// solid region surrounding a door.&lt;/summary&gt;</span><span>
</span><span>/// &lt;remarks&gt;This routine is useful for detecting interferences which are </span><span>
</span><span>/// violations of the Americans with Disabilities Act or other local disabled </span><span>
</span><span>/// access codes.&lt;/remarks&gt;</span><span>
</span><span>/// &lt;param name="doorInstance"&gt;The door instance.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="doorAccessibilityRegion"&gt;The accessibility region calculated</span><span>
</span><span>/// to surround the approach of the door.</span><span>
</span><span>/// Because the geometric parameters of this region are code- and </span><span>
</span><span>/// door-specific, calculation of the geometry of the region is not </span><span>
</span><span>/// demonstrated in this example.&lt;/param&gt;</span><span>
</span><span>/// &lt;returns&gt;A collection of interfering element ids.&lt;/returns&gt;</span><span>
</span><span>private</span><span> </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> </span><span>FindElementsInterferingWithDoor</span><span>(</span><span>FamilyInstance</span><span> doorInstance</span><span>,</span><span> </span><span>Solid</span><span> doorAccessibilityRegion</span><span>)</span><span>
</span><span>{</span><span>
   </span><span>// Setup the filtered element collector for all document elements.</span><span>
   </span><span>FilteredElementCollector</span><span> interferingCollector </span><span>=</span><span> 
      </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doorInstance</span><span>.</span><span>Document</span><span>);</span><span>

   </span><span>// Only accept element instances</span><span>
   interferingCollector</span><span>.</span><span>WhereElementIsNotElementType</span><span>();</span><span>

   </span><span>// Exclude intersections with the door itself or the host wall for the door.</span><span>
   </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> excludedElements </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
   excludedElements</span><span>.</span><span>Add</span><span>(</span><span>doorInstance</span><span>.</span><span>Id</span><span>);</span><span>
   excludedElements</span><span>.</span><span>Add</span><span>(</span><span>doorInstance</span><span>.</span><span>Host</span><span>.</span><span>Id</span><span>);</span><span>
   </span><span>ExclusionFilter</span><span> exclusionFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ExclusionFilter</span><span>(</span><span>excludedElements</span><span>);</span><span>
   interferingCollector</span><span>.</span><span>WherePasses</span><span>(</span><span>exclusionFilter</span><span>);</span><span>

   </span><span>// Set up a filter which matches elements whose solid geometry intersects </span><span>
   </span><span>// with the accessibility region</span><span>
   </span><span>ElementIntersectsSolidFilter</span><span> intersectionFilter </span><span>=</span><span> 
      </span><span>new</span><span> </span><span>ElementIntersectsSolidFilter</span><span>(</span><span>doorAccessibilityRegion</span><span>);</span><span>
   interferingCollector</span><span>.</span><span>WherePasses</span><span>(</span><span>intersectionFilter</span><span>);</span><span>

   </span><span>// Return all elements passing the collector</span><span>
   </span><span>return</span><span> interferingCollector</span><span>.</span><span>ToElementIds</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
