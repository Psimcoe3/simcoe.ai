---
created: 2026-01-28T21:34:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_html
author: 
---

# Help | Filtering | Autodesk

> ## Excerpt
> The Revit API provides a mechanism for filtering and iterating elements in a Revit document. This is the best way to get a set of related elements, such as all walls or doors in the document. Filters can also be used to find a very specific set of elements, such as all beams of a specific size.

---
The Revit API provides a mechanism for filtering and iterating elements in a Revit document. This is the best way to get a set of related elements, such as all walls or doors in the document. Filters can also be used to find a very specific set of elements, such as all beams of a specific size.

The basic steps to get elements passing a specified filter are as follows:

1.  Create a new FilteredElementCollector
2.  Apply one or more filters to it
3.  Get filtered elements or element ids (using one of several methods)

The following sample covers the basic steps to filtering and iterating elements in the document.

<table summary="" id="GUID-85E4A43E-88B5-43C6-908C-2D138C9F611D__TABLE_9B881B8A742C4C1885A86B5BE0CEFA42"><tbody><tr><td><b>Code Region 6-1: Use element filtering to get all wall instances in document</b></td></tr><tr><td><pre><code><span>// Find all Wall instances in the document by using category filter</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>GetAllWalls</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ElementCategoryFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementCategoryFilter</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Walls</span><span>);</span><span>

    </span><span>// Apply the filter to the elements in the active document</span><span>
    </span><span>// Use shortcut WhereElementIsNotElementType() to find wall instances only</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> walls </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>WhereElementIsNotElementType</span><span>().</span><span>ToElements</span><span>();</span><span>
    </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"The walls in the current document are:\n"</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> walls</span><span>)</span><span>
    </span><span>{</span><span>
            prompt </span><span>+=</span><span> e</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
