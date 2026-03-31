---
created: 2026-01-28T20:48:49 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_Filtered_User_Selection_html
author: 
---

# Help | Filtered User Selection | Autodesk

> ## Excerpt
> PickObject(), PickObjects() and PickElementsByRectangle() all have overloads that take an ISelectionFilter as a parameter. ISelectionFilter is an interface that can be implemented to filter objects during a selection operation. It has two methods that can be overridden: AllowElement() which is used to specify if an element is allowed to be selected, and AllowReference() which is used to specify if a reference to a piece of geometry is allowed to be selected.

---
PickObject(), PickObjects() and PickElementsByRectangle() all have overloads that take an ISelectionFilter as a parameter. ISelectionFilter is an interface that can be implemented to filter objects during a selection operation. It has two methods that can be overridden: AllowElement() which is used to specify if an element is allowed to be selected, and AllowReference() which is used to specify if a reference to a piece of geometry is allowed to be selected.

The following example illustrates how to use an ISelectionFilter interface to limit the user's selection to elements in the Mass category. It does not allow any references to geometry to be selected.

<table summary="" id="GUID-ECB1EE82-EA91-451C-995C-7683C1F676CB__TABLE_441BBE03B59F4A7398ED1A104D1C6250"><tbody><tr><td><b>Code Region 7-4: Using ISelectionFilter to limit element selection</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> </span><span>GetManyRefByRectangle</span><span>(</span><span>UIDocument</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>ReferenceArray</span><span> ra </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>
        </span><span>ISelectionFilter</span><span> selFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>MassSelectionFilter</span><span>();</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> eList </span><span>=</span><span> doc</span><span>.</span><span>Selection</span><span>.</span><span>PickElementsByRectangle</span><span>(</span><span>selFilter</span><span>,</span><span> 
                </span><span>"Select multiple faces"</span><span>)</span><span> </span><span>as</span><span> </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;;</span><span>
        </span><span>return</span><span> eList</span><span>;</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>class</span><span> </span><span>MassSelectionFilter</span><span> </span><span>:</span><span> </span><span>ISelectionFilter</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowElement</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
        </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>element</span><span>.</span><span>Category</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Mass"</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>true</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>return</span><span> </span><span>false</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowReference</span><span>(</span><span>Reference</span><span> refer</span><span>,</span><span> XYZ point</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>false</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The next example demonstrates the use of ISelectionFilter to allow only planar faces to be selected.

<table summary="" id="GUID-ECB1EE82-EA91-451C-995C-7683C1F676CB__TABLE_CBF97B8571924E25937696B04827FB08"><tbody><tr><td><b>Code Region 7-5: Using ISelectionFilter to limit geometry selection</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SelectPlanarFaces</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ISelectionFilter</span><span> selFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>PlanarFacesSelectionFilter</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Reference</span><span>&gt;</span><span> faces </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>PickObjects</span><span>(</span><span>ObjectType</span><span>.</span><span>Face</span><span>,</span><span> 
                selFilter</span><span>,</span><span> </span><span>"Select multiple planar faces"</span><span>);</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>class</span><span> </span><span>PlanarFacesSelectionFilter</span><span> </span><span>:</span><span> </span><span>ISelectionFilter</span><span>
</span><span>{</span><span>
        </span><span>Document</span><span> doc </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>public</span><span> </span><span>PlanarFacesSelectionFilter</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
        </span><span>{</span><span>
                doc </span><span>=</span><span> document</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowElement</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>true</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowReference</span><span>(</span><span>Reference</span><span> refer</span><span>,</span><span> XYZ point</span><span>)</span><span>
        </span><span>{</span><span>   
                </span><span>if</span><span> </span><span>(</span><span>doc</span><span>.</span><span>GetElement</span><span>(</span><span>refer</span><span>).</span><span>GetGeometryObjectFromReference</span><span>(</span><span>refer</span><span>)</span><span> </span><span>is</span><span> </span><span>PlanarFace</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>// Only return true for planar faces. Non-planar faces will not be selectable </span><span>
                        </span><span>return</span><span> </span><span>true</span><span>;</span><span> 
                </span><span>}</span><span>
                </span><span>return</span><span> </span><span>false</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

For more information about retrieving Elements from selected Elements, see [Walkthrough: Retrieve Selected Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Walkthrough_Retrieve_Selected_Elements_html) in the [Getting Started](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_html) section.
