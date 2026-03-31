---
created: 2026-01-28T21:00:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_Design_Options_html
author: 
---

# Help | Design Options | Autodesk

> ## Excerpt
> Design options provide a way to explore alternative designs in a project.

---
Design options provide a way to explore alternative designs in a project.

Design options provide the flexibility to adapt to changes in project scope or to develop alternative designs for review. You can begin work with the main project model and then develop variations along the way to present to a client. Most elements can be added into a design option. Elements that cannot be added into a design option are considered part of the main model and have no design alternatives.

The main use for Design options is as a property of the Element class. See the following example.

<table summary="" id="GUID-F84EFE35-C0B3-417D-A3B8-0DE98E9A61B5__TABLE_3BF9E42C9F8F4B649AB43B632966E4C6"><tbody><tr><td><b>Code Region 15-7: Using design options</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>Getinfo_DesignOption</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the selected Elements in the Active Document</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> element </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>//Use the DesignOption property of Element</span><span>
        </span><span>if</span><span> </span><span>(</span><span>element</span><span>.</span><span>DesignOption</span><span> </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>element</span><span>.</span><span>DesignOption</span><span>.</span><span>Name</span><span>.</span><span>ToString</span><span>());</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following rules apply to Design Options

-   The value of the DesignOption property is null if the element is in the Main Model. Otherwise, the name you created in the Revit UI is returned.
-   Only one active DesignOption Element can exist in an ActiveDocument.
    -   The primary option is considered the default active DesignOption. For example, a design option set is named Wall and there are two design options in this set named "brick wall" and "glass wall". If "brick wall" is the primary option, only this option and elements that belong to it are retrieved by the Element Iterator. "Glass wall" is inactive.
