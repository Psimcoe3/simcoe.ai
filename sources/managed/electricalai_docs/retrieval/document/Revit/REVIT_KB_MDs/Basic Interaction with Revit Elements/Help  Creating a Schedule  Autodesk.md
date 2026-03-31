---
created: 2026-01-28T20:52:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_ViewSchedule_Creating_a_Schedule_html
author: 
---

# Help | Creating a Schedule | Autodesk

> ## Excerpt
> The ViewSchedule class has several methods for creating new schedules depending on the type of schedule. All of the methods have a Document parameter that is the document to which the new schedule or schedule-like view will be added. The newly created schedule views will appear under the Schedules/Quantities node in the Project Browser.

---
The ViewSchedule class has several methods for creating new schedules depending on the type of schedule. All of the methods have a Document parameter that is the document to which the new schedule or schedule-like view will be added. The newly created schedule views will appear under the Schedules/Quantities node in the Project Browser.

A standard single-category or multi-category schedule can be created with the static ViewSchedule.CreateSchedule() method.

<table summary="" id="GUID-7DB8EEA6-2C4A-4BC3-A783-1C85B6776D53__TABLE_1058380D6C044FA285D73731EEB5CE50"><tbody><tr><td><b>Code Region: Create a single-category schedule with 2 fields</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateSingleCategorySchedule</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create single-category"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// Create schedule</span><span>
        </span><span>ViewSchedule</span><span> vs </span><span>=</span><span> </span><span>ViewSchedule</span><span>.</span><span>CreateSchedule</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Windows</span><span>));</span><span>

        doc</span><span>.</span><span>Regenerate</span><span>();</span><span>

        </span><span>// Add fields to the schedule</span><span>
        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_HEIGHT</span><span>));</span><span>
        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_WIDTH</span><span>));</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>/// &lt;summary&gt;</span><span>
</span><span>/// Adds a single parameter field to the schedule</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddRegularFieldToSchedule</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>ElementId</span><span> paramId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>

    </span><span>// Find a matching SchedulableField</span><span>
    </span><span>SchedulableField</span><span> schedulableField </span><span>=</span><span>
        definition</span><span>.</span><span>GetSchedulableFields</span><span>().</span><span>FirstOrDefault</span><span>&lt;</span><span>SchedulableField</span><span>&gt;(</span><span>sf </span><span>=&gt;</span><span> sf</span><span>.</span><span>ParameterId</span><span> </span><span>==</span><span> paramId</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>schedulableField </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Add the found field</span><span>
        definition</span><span>.</span><span>AddField</span><span>(</span><span>schedulableField</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The second parameters the ID of the category whose elements will be included in the schedule, or InvalidElementId for a multi-category schedule.

A second CreateSchedule() method can be used to create an area schedule and takes an additional parameter that is the ID of an area scheme for the schedule.

<table summary="" id="GUID-7DB8EEA6-2C4A-4BC3-A783-1C85B6776D53__TABLE_6F5EB09B9E8A43F1BC877E8A73C125DD"><tbody><tr><td><b>Code Region: Creating an area schedule</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateAreaSchedule</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    collector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_AreaSchemes</span><span>);</span><span>
    </span><span>//Get first ElementId of AreaScheme.</span><span>
    </span><span>ElementId</span><span> areaSchemeId </span><span>=</span><span> collector</span><span>.</span><span>FirstElementId</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>areaSchemeId </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> areaSchemeId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// If you want to create an area schedule, you must use CreateSchedule method with three arguments. </span><span>
        </span><span>// The value of the second argument must be ElementId of BuiltInCategory.OST_Areas category</span><span>
        </span><span>// and the value of third argument must be ElementId of an AreaScheme.</span><span>
        </span><span>ViewSchedule</span><span> areaSchedule </span><span>=</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ViewSchedule</span><span>.</span><span>CreateSchedule</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Areas</span><span>),</span><span> areaSchemeId</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

A key schedule displays abstract "key" elements that can be used to populate parameters of ordinary model elements and can be created with the static ViewSchedule.CreateKeySchedule() method whose second parameter is the ID of the category of elements with which the schedule's keys will be associated.A material takeoff is a schedule that displays information about the materials that make up elements in the model. Unlike regular schedules where each row (before grouping) represents a single element, each row in a material takeoff represents a single <element, material> pair. The ViewSchedule.CreateMaterialTakeoff() method has the same parameters as the ViewSchedule.CreateSchedule() method and allows for both single- and multi-category material takeoff schedules.

View lists, sheet lists, and keynote legends are associated with a designated category and therefore their creation methods do take a category ID as a parameter. A view list is a schedule of views in the project. It is a schedule of the Views category and is created using ViewSchedule.CreateViewList().

A sheet list is a schedule of sheets in the project. It is a schedule of the Sheets category and is created using the ViewSchedule.CreateSheetList() method.

A keynote legend is a schedule of the Keynote Tags category and is created using ViewSchedule.CreateKeynoteLegend().

Revision schedules are added to titleblock families and become visible as part of titleblocks on sheets. The ViewSchedule.CreateRevisionSchedule() method will throw an exception if the document passed in is not a titleblock family.

A note block is a schedule of the Generic Annotations category that shows elements of a single family rather than all elements in a category.

The second parameter is the ID of the family whose elements will be included in the schedule.

<table summary="" id="GUID-7DB8EEA6-2C4A-4BC3-A783-1C85B6776D53__TABLE_88434DF564D2433E8B5700903A47A3E2"><tbody><tr><td><b>Code Region: Creating a note block schedule</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateNoteBlock</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Creating Note Block"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>//Get first ElementId of a Note Block family.</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> noteblockFamilies </span><span>=</span><span> </span><span>ViewSchedule</span><span>.</span><span>GetValidFamiliesForNoteBlock</span><span>(</span><span>doc</span><span>);</span><span>
        </span><span>ElementId</span><span> symbolId </span><span>=</span><span> noteblockFamilies</span><span>.</span><span>First</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
        </span><span>ViewSchedule</span><span> noteBlockSchedule </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(!</span><span>symbolId</span><span>.</span><span>Equals</span><span>(</span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>))</span><span>
        </span><span>{</span><span>
            transaction</span><span>.</span><span>Start</span><span>();</span><span>

            </span><span>//Create a note-block view schedule.</span><span>
            noteBlockSchedule </span><span>=</span><span> </span><span>ViewSchedule</span><span>.</span><span>CreateNoteBlock</span><span>(</span><span>doc</span><span>,</span><span> symbolId</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> noteBlockSchedule</span><span>)</span><span>
        </span><span>{</span><span>
            transaction</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            transaction</span><span>.</span><span>RollBack</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
