---
created: 2026-01-28T20:52:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_PanelScheduleView_html
author: 
---

# Help | PanelScheduleView | Autodesk

> ## Excerpt
> PanelScheduleView represents a panel schedule which displays information about a panel, the circuits connected to the panel, and their corresponding loads.

---
PanelScheduleView represents a panel schedule which displays information about a panel, the circuits connected to the panel, and their corresponding loads.

You can create a schedule that lists the circuits connected to a panel, and displays information about each circuit such as location on the panel, circuit name and apparent loads. Panel schedules display four main information sections: a header, circuit table, a loads summary and a footer. A new Panel Schedule view for the selected panel is displayed in the drawing area, and panel schedules are added to the project browser under the Panel Schedules folder. A panel schedule shows the following data:

-   Panel Name
-   Distribution System supported by the panel
-   Number of phases available from the panel
-   Number of wires specified for the distribution system assigned to this panel
-   Rating of the mains feeding the panel
-   Type of mounting (Surface or Recessed)
-   Type of case enclosing the panel
-   Room where the panel is installed
-   Name assigned to a load circuit
-   Rated trip current for a circuit breaker
-   Number of poles on the circuit breaker
-   Circuit number
-   Phases
-   Apparent load (VA) for each of the phases
-   Total apparent load for all three phases
-   Manufacturer
-   Notation of any changes made to the panel
-   Root Means Square amperage Additional circuit and panel information to display can be specified in the panel schedule templates, represented in the Revit API by the PanelScheduleTemplate class.

PanelScheduleView is derived from the TableView class as is ViewSchedule. Some of the common functionality between schedules and panel schedules can be found in the [Schedule Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_Schedule_Classes_html "Schedule views use several supporting classes.") topic.

### Panel schedule creation

There are two static overloads for creating a PanelScheduleView. One overload of PanelScheduleView.CreateInstanceView() only requires the document in which to create the panel schedule and the id of the electrical panel element associated with the schedule. This method uses the default panel schedule template to create the new view. The other overload takes the id of a specific PanelScheduleTemplate to use.

The following example creates a new panel schedule from a user-selected electrical panel using the default template and switches the active view to the new panel schedule view.

<table summary="" id="GUID-060A778F-29B5-4F03-974F-3DABEF2CF131__TABLE_5421C731BF84459E860D8DA820244CCA"><tbody><tr><td><b>Code Region: Create a panel schedule</b></td></tr><tr><td><pre><code><span>// Create a new panel schedule and switch to that view</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>CreatePanelSchedule</span><span>(</span><span>UIDocument</span><span> uiDocument</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>Reference</span><span> selected </span><span>=</span><span> uiDocument</span><span>.</span><span>Selection</span><span>.</span><span>PickObject</span><span>(</span><span>ObjectType</span><span>.</span><span>Element</span><span>,</span><span> </span><span>"Select an electrical panel"</span><span>);</span><span>

    </span><span>Element</span><span> panel </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>selected</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> panel</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>PanelScheduleView</span><span> psv </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create a new panel schedule"</span><span>))</span><span>
        </span><span>{</span><span>
            trans</span><span>.</span><span>Start</span><span>();</span><span>
            psv </span><span>=</span><span> </span><span>PanelScheduleView</span><span>.</span><span>CreateInstanceView</span><span>(</span><span>doc</span><span>,</span><span> panel</span><span>.</span><span>Id</span><span>);</span><span>
            trans</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> psv</span><span>)</span><span>
        </span><span>{</span><span>
            uiDocument</span><span>.</span><span>ActiveView</span><span> </span><span>=</span><span> psv</span><span>;</span><span>    </span><span>// make new view the active view</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Please select one electrical panel."</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Working with panel schedules

After a schedule is created, you may want to modify it. Several methods are helpful for moving data in the schedule. To move data around, use PanelScheduleView.GetCellsBySlotNumber() to get the range of cells for a specified slot number. PanelScheduleView.MoveSlotTo() moves the circuits in the source slot to the specific slot. Prior to moving the circuits, call PanelScheduleView.CanMoveSlotTo() to ensure the move is allowable.

If the moving circuit is in a group, all circuits in the group will be moved accordingly. The IsSlotGrouped() method will check if the slot is in a group. This method returns 0 if the slot is not in a group. If it is in a group, the returned value with be the group number (a value greater than 0).
