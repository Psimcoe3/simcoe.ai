---
created: 2026-01-28T20:51:11 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Deleting_Elements_html
author: 
---

# Help | Deleting Elements | Autodesk

> ## Excerpt
> The Revit Platform API provides Delete() methods to delete one or more elements in the project.

---
The Revit Platform API provides Delete() methods to delete one or more elements in the project.

**Table 23: Delete Members**

<table summary="" id="GUID-D8D01E04-2F08-49B2-8614-AED24F560F5C__TABLE_C698AFE08C52448B82FC7C02E23844D6"><tbody><tr><td><b>Member</b></td><td><b>Description</b></td></tr><tr><td>Delete(ElementId)</td><td>Delete an element from the project using the element ID</td></tr><tr><td>Delete(<a href="http://msdn2.microsoft.com/en-us/library/92t2ye13" target="_blank">ICollection</a>)</td><td>Delete several elements from the project by their IDs.</td></tr></tbody></table>

The first method deletes a single element based on its Id, as shown in the example below.

<table summary="" id="GUID-D8D01E04-2F08-49B2-8614-AED24F560F5C__TABLE_E9BC67116341441CA2E5B8222497A865"><tbody><tr><td><b>Code Region: Deleting an element based on ElementId</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>DeleteElement</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Delete an element via its id</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> elementId </span><span>=</span><span> element</span><span>.</span><span>Id</span><span>;</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>&gt;</span><span> deletedIdSet </span><span>=</span><span> document</span><span>.</span><span>Delete</span><span>(</span><span>elementId</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>==</span><span> deletedIdSet</span><span>.</span><span>Count</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Deleting the selected element in Revit failed."</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"The selected element has been removed and "</span><span>;</span><span>
        prompt </span><span>+=</span><span> deletedIdSet</span><span>.</span><span>Count</span><span> </span><span>-</span><span> </span><span>1</span><span>;</span><span>
        prompt </span><span>+=</span><span> </span><span>" more dependent elements have also been removed."</span><span>;</span><span>

        </span><span>// Give the user some information</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: When an element is deleted, any child elements associated with that element are also deleted, as indicated in the sample above.

The API also provides a way to delete several elements.

<table summary="" id="GUID-D8D01E04-2F08-49B2-8614-AED24F560F5C__TABLE_DCF65C320D43485F9FCFFD209929E9BA"><tbody><tr><td><b>Code Region: Deleting multiple elements based on Id</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>DeleteSelected</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Delete all the selected elements via the set of elements</span><span>
        </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span> 
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> elements </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>&gt;</span><span> deletedIdSet </span><span>=</span><span> document</span><span>.</span><span>Delete</span><span>(</span><span>elements</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>==</span><span> deletedIdSet</span><span>.</span><span>Count</span><span>)</span><span>
        </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Deleting the selected elements in Revit failed."</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"The selected element has been removed."</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: After you delete the elements, any references to the deleted elements become invalid and throw an exception if they are accessed.

## Element Dependencies

Element.GetDependentElements() returns a list of ids of elements which are "children" of this element; that is, those elements which will be deleted along with this element. The method optionally takes an ElementFilter which can be used to reduce the output list to the collection of elements matching specific criteria.
