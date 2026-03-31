---
created: 2026-01-28T20:48:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Getting_filtered_elements_or_element_ids_html
author: 
---

# Help | Getting filtered elements or element ids | Autodesk

> ## Excerpt
> Once one or more filters have been applied to the FilteredElementCollector, the filtered set of elements can be retrieved in one of three ways:

---
Once one or more filters have been applied to the FilteredElementCollector, the filtered set of elements can be retrieved in one of three ways:

1.  Obtain a collection of Elements or ElementIds.
    -   ToElements() - returns all elements that pass all applied filters
    -   ToElementIds() - returns ElementIds of all elements which pass all applied filters
2.  Obtain the first Element or ElementId that matches the filter.
    -   FirstElement() - returns first element to pass all applied filters
    -   FirstElementId() - returns id of first element to pass all applied filters
3.  Obtain an ElementId or Element iterator.
    -   GetElementIdIterator() - returns FilteredElementIdIterator to the element ids passing the filters
    -   GetElementIterator() - returns FilteredElementIterator to the elements passing the filters
    -   GetEnumerator() - returns an `IEnumerator<Element>` that iterates through collection of passing elements

You should only use one of the methods from these groups at a time; the collector will reset if you call another method to extract elements. Thus, if you have previously obtained an iterator, it will be stopped and traverse no more elements if you call another method to extract elements.

Which method is best depends on the application. If just one matching element is required, FirstElement() or FirstElementId() is the best choice. If all the matching elements are required, use ToElements(). If a variable number are needed, use an iterator.

If the application will be deleting elements or making significant changes to elements in the filtered list, ToElementIds() or an element id iterator are the best options. This is because deleting elements or making significant changes to an element can invalidate an element handle. With element ids, the call to Document.GetElement() with the ElementId will always return a valid Element (or a null reference if the element has been deleted).

Using the ToElements() method to get the filter results as a collection of elements allows for the use of foreach to examine each element in the set, as is shown below:

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_207AA8B68C604D5FAD2D32200DBC38AF"><tbody><tr><td><b>Code Region 6-9: Using ToElements() to get filter results</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ToElementsSample</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use ElementClassFilter to find all loads in the document</span><span>
        </span><span>// Using typeof(LoadBase) will yield all AreaLoad, LineLoad and PointLoad</span><span>
        </span><span>ElementClassFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>LoadBase</span><span>));</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> allLoads </span><span>=</span><span> collector</span><span>.</span><span>ToElements</span><span>();</span><span>

        </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"The loads in the current document are:\n"</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> loadElem </span><span>in</span><span> allLoads</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>LoadBase</span><span> load </span><span>=</span><span> loadElem </span><span>as</span><span> </span><span>LoadBase</span><span>;</span><span>
                prompt </span><span>+=</span><span> load</span><span>.</span><span>GetType</span><span>().</span><span>Name</span><span> </span><span>+</span><span>  </span><span>": "</span><span> </span><span>+</span><span> 
                                load</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

When just one passing element is needed, use FirstElement():

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_E6B708B8CDF14FEA9D8CFF9164C1E3D9"><tbody><tr><td><b>Code Region 6-10: Get the first passing element</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetFirstElement</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Create a filter to find all columns</span><span>
        </span><span>StructuralInstanceUsageFilter</span><span> columnFilter </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>StructuralInstanceUsageFilter</span><span>(</span><span>StructuralInstanceUsage</span><span>.</span><span>Column</span><span>);</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        collector</span><span>.</span><span>WherePasses</span><span>(</span><span>columnFilter</span><span>);</span><span>

        </span><span>// Get the first column from the filtered results</span><span>
        </span><span>// Element will be a FamilyInstance</span><span>
        </span><span>FamilyInstance</span><span> column </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

In some cases, FirstElement() is not sufficient. This next example shows how to use extension methods to get the first non-template 3D view (which is useful for input to the ReferenceIntersector constructors).

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_BAB9F3774BDD45609D959578662FA8B9"><tbody><tr><td><b>Code Region 6-11: Get first passing element using extension methods</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>UseExtensionMethods</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use filter to find a non-template 3D view</span><span>
        </span><span>// This example does not use FirstElement() since first filterd view3D might be a template</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>Func</span><span>&lt;</span><span>View3D</span><span>,</span><span> </span><span>bool</span><span>&gt;</span><span> isNotTemplate </span><span>=</span><span> v3 </span><span>=&gt;</span><span> </span><span>!(</span><span>v3</span><span>.</span><span>IsTemplate</span><span>);</span><span>

        </span><span>// apply ElementClassFilter</span><span>
        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>View3D</span><span>));</span><span>

        </span><span>// use extension methods to get first non-template View3D</span><span>
        </span><span>View3D</span><span> view3D </span><span>=</span><span> collector</span><span>.</span><span>Cast</span><span>&lt;</span><span>View3D</span><span>&gt;().</span><span>First</span><span>&lt;</span><span>View3D</span><span>&gt;(</span><span>isNotTemplate</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following example demonstrates the use of the FirstElementId() method to get one passing element (a 3d view in this case) and the use of ToElementIds() to get the filter results as a collection of element ids (in order to delete a set of elements in this case).

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_2D746E4434264430A42E85A14C20ECC7"><tbody><tr><td><b>Code Region 6-12: Using Getting filter results as element ids</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetElementIds</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>

        </span><span>// Use shortcut OfClass to get View elements</span><span>
        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>View3D</span><span>));</span><span>

        </span><span>// Get the Id of the first view</span><span>
        </span><span>ElementId</span><span> viewId </span><span>=</span><span> collector</span><span>.</span><span>FirstElementId</span><span>();</span><span>

        </span><span>// Test if the view is valid for element filtering</span><span>
        </span><span>if</span><span> </span><span>(</span><span>FilteredElementCollector</span><span>.</span><span>IsViewValidForElementIteration</span><span>(</span><span>document</span><span>,</span><span> viewId</span><span>))</span><span>
        </span><span>{</span><span>
                </span><span>FilteredElementCollector</span><span> viewCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>,</span><span> viewId</span><span>);</span><span>

                </span><span>// Get all FamilyInstance items in the view</span><span>
                viewCollector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilyInstance</span><span>));</span><span>
                </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> familyInstanceIds </span><span>=</span><span> viewCollector</span><span>.</span><span>ToElementIds</span><span>();</span><span>

                document</span><span>.</span><span>Delete</span><span>(</span><span>familyInstanceIds</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The GetElementIterator() method is used in the following example that iterates through the filtered elements to check the flow state of some pipes.

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_F8DE91F5939B480C9B3B12273F7F3E55"><tbody><tr><td><b>Code Region 6-13: Getting the results as an element iterator</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetIterator</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>

        </span><span>// Apply a filter to get all pipes in the document</span><span>
        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Plumbing</span><span>.</span><span>Pipe</span><span>));</span><span>

        </span><span>// Get results as an element iterator and look for a pipe with</span><span>
        </span><span>// a specific flow state</span><span>
        </span><span>FilteredElementIterator</span><span> elemItr </span><span>=</span><span> collector</span><span>.</span><span>GetElementIterator</span><span>();</span><span>
        elemItr</span><span>.</span><span>Reset</span><span>();</span><span>
        </span><span>while</span><span> </span><span>(</span><span>elemItr</span><span>.</span><span>MoveNext</span><span>())</span><span>
        </span><span>{</span><span>
                </span><span>Pipe</span><span> pipe </span><span>=</span><span> elemItr</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Pipe</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>pipe</span><span>.</span><span>FlowState</span><span> </span><span>==</span><span> </span><span>PipeFlowState</span><span>.</span><span>LaminarState</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Model has at least one pipe with Laminar flow state."</span><span>);</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Alternatively, the filter results can be returned as an element id iterator:

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_E6A4097E7F4F4B639C7BA1B84E99138B"><tbody><tr><td><b>Code Region 6-14: Getting the results as an element id iterator</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetIdIterator</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use a RoomFilter to find all room elements in the document. </span><span>
        </span><span>RoomFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>RoomFilter</span><span>();</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>);</span><span>

        </span><span>// Get results as ElementId iterator</span><span>
        </span><span>FilteredElementIdIterator</span><span> roomIdItr </span><span>=</span><span> collector</span><span>.</span><span>GetElementIdIterator</span><span>();</span><span>
        roomIdItr</span><span>.</span><span>Reset</span><span>();</span><span>
        </span><span>while</span><span> </span><span>(</span><span>roomIdItr</span><span>.</span><span>MoveNext</span><span>())</span><span>
        </span><span>{</span><span>
                </span><span>ElementId</span><span> roomId </span><span>=</span><span> roomIdItr</span><span>.</span><span>Current</span><span>;</span><span>
                </span><span>// Warn rooms smaller than 50 SF</span><span>
                </span><span>Room</span><span> room </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>roomId</span><span>)</span><span> </span><span>as</span><span> </span><span>Room</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>room</span><span>.</span><span>Area</span><span> </span><span>&lt;</span><span> </span><span>50.0</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"Room is too small: id = "</span><span> </span><span>+</span><span> roomId</span><span>.</span><span>ToString</span><span>();</span><span>
                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

In some cases, it may be useful to test a single element against a given filter, rather than getting all elements that pass the filter. There are two overloads for ElementFilter.PassesFilter() that test a given Element, or ElementId, against the filter, returning true if the element passes the filter.
