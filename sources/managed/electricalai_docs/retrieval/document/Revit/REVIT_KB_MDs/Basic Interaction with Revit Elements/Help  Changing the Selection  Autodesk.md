---
created: 2026-01-28T20:48:40 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_Changing_the_Selection_html
author: 
---

# Help | Changing the Selection | Autodesk

> ## Excerpt
> To modify the selected elements:

---
To modify the selected elements:

1.  Create a new List of ElementIds.
2.  Put ElementIds in it.
3.  Call SetElementIds() with the new list.

The following example illustrates how to change the selected Elements by getting the current selection and filtering out just walls to set as the new selection.

It is also possible to select references by using `SetReferences()`. The references can be an element or a sub element in the host or a linked document. `GetReferences()` returns the references that are currently selected.

<table summary="" id="GUID-541141C8-F390-424E-88BD-54F667C823F8__TABLE_41B2C4147FA34DF794CABDD1932F8C2B"><tbody><tr><td><b>Code Region 7-1: Changing selected elements</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ChangeSelection</span><span>(</span><span>UIDocument</span><span> uidoc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get selected elements from current document.</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

    </span><span>// Display current number of selected elements</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Number of selected elements: "</span><span> </span><span>+</span><span> selectedIds</span><span>.</span><span>Count</span><span>.</span><span>ToString</span><span>());</span><span>

    </span><span>// Go through the selected items and filter out walls only.</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedWallIds </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> elements </span><span>=</span><span> uidoc</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>elements </span><span>is</span><span> </span><span>Wall</span><span>)</span><span>
        </span><span>{</span><span>
            selectedWallIds</span><span>.</span><span>Add</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// Set the created element set as current select element set.</span><span>
    uidoc</span><span>.</span><span>Selection</span><span>.</span><span>SetElementIds</span><span>(</span><span>selectedWallIds</span><span>);</span><span>

    </span><span>// Give the user some information.</span><span>
    </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>!=</span><span> selectedWallIds</span><span>.</span><span>Count</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> selectedWallIds</span><span>.</span><span>Count</span><span>.</span><span>ToString</span><span>()</span><span> </span><span>+</span><span> </span><span>" Walls are selected!"</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"No Walls have been selected!"</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
