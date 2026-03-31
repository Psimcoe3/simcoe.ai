---
created: 2026-01-28T21:00:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_Phase_html
author: 
---

# Help | Phase | Autodesk

> ## Excerpt
> Some architectural projects, such as renovations, proceed in phases. Phases have the following characteristics:

---
Some architectural projects, such as renovations, proceed in phases. Phases have the following characteristics:

-   Phases represent distinct time periods in a project lifecycle.
-   The lifetime of an element within a building is controlled by phases.
-   Each element has a construction phase but only the elements with a finite lifetime have a destruction phase.

All phases in a project can be retrieved from the Document object. A Phase object contains three pieces of useful information: Name, ID and UniqueId. The remaining properties always return null or an empty collection.

Each new modeling component added to a project has a Created Phase ID and a Demolished Phase ID property. The Element.AllowPhases() method indicates whether its phase ID properties can be modified.

The Created Phase ID property has the following characteristics:

-   It identifies the phase in which the component was added.
-   The default value is the same ID as the current view Phase value.
-   Change the Created Phase ID parameter by selecting a new value corresponding to the drop-down list.

The Demolished Phase ID property has the following characteristics:

-   It identifies in which phase the component is demolished.
-   The default value is none.
-   Demolishing a component with the demolition tool updates the property to the current Phase ID value in the view where you demolished the element.
-   You can demolish a component by setting the Demolished Phase ID property to a different value.
-   If you delete a phase using the Revit Platform API, all modeling components in the current phase still exist. The Created Phase ID parameter value for these components is changed to the next item in the drop-down list in the Properties dialog box. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-3840696A-98D6-4898-8004-EFB85A3247E1-low.png)**Figure 65: Phase-created component parameter value**

The following code sample displays all supported phases in the current document. The phase names are displayed in a message box.

<table summary="" id="GUID-DD43AD1E-37D1-4F61-8A23-52C9DEFF2D3F__TABLE_FBF013133CA740FFB96BD77DB7FE0870"><tbody><tr><td><b>Code Region 15-6: Displaying all supported phases</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>Getinfo_Phase</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Get the phase array which contains all the phases.</span><span>
        </span><span>PhaseArray</span><span> phases </span><span>=</span><span> doc</span><span>.</span><span>Phases</span><span>;</span><span>
        </span><span>// Format the string which identifies all supported phases in the current document.</span><span>
        </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>!=</span><span> phases</span><span>.</span><span>Size</span><span>)</span><span>
        </span><span>{</span><span>
                prompt </span><span>=</span><span> </span><span>"All the phases in current document list as follow:"</span><span>;</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>Phase</span><span> ii </span><span>in</span><span> phases</span><span>)</span><span>
                </span><span>{</span><span>
                        prompt </span><span>+=</span><span> </span><span>"\n\t"</span><span> </span><span>+</span><span> ii</span><span>.</span><span>Name</span><span>;</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
                prompt </span><span>=</span><span> </span><span>"There are no phases in current document."</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>// Give the user the information.</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Validating phase data of an element

`Element.IsDemolishedPhaseOrderValid()` and `Element.IsCreatedPhaseOrderValid()` validate the order of phases on a given element, ensuring that an object is not assigned a phase where it is demolished before it was created.
