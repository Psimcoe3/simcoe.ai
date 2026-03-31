---
created: 2026-01-28T21:04:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Stairs_Components_html
author: 
---

# Help | Stairs Components | Autodesk

> ## Excerpt
> The Stairs class represents a stairs element in Revit and contains properties that represent information about the treads, risers, number of stories, as well as the height of the stairs and base and top elevation. Methods of the Stairs class can be used to get the stairs landing components, stairs run components and stairs supports.

---
The Stairs class represents a stairs element in Revit and contains properties that represent information about the treads, risers, number of stories, as well as the height of the stairs and base and top elevation. Methods of the Stairs class can be used to get the stairs landing components, stairs run components and stairs supports.

The following example finds all of the Stairs that are by component and outputs some information on each of the Stairs to a Task Dialog. Note that this example uses a category filter with the BuiltInCategory.OST\_Stairs which will return ElementIds for all stairs, therefore requiring a test to see if each ElementId represents a Stairs By Component before being cast to a Stairs class when retrieved from the document.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_31B401EAF671410BB9A4BDB631C1455A"><tbody><tr><td><b>Code Region: Getting stairs information</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Stairs</span><span> </span><span>GetStairInfo</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Stairs</span><span> stairs </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> stairsIds </span><span>=</span><span> collector</span><span>.</span><span>WhereElementIsNotElementType</span><span>().</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Stairs</span><span>).</span><span>ToElementIds</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> stairId </span><span>in</span><span> stairsIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>Stairs</span><span>.</span><span>IsByComponent</span><span>(</span><span>document</span><span>,</span><span> stairId</span><span>)</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
        </span><span>{</span><span>
            stairs </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>stairId</span><span>)</span><span> </span><span>as</span><span> </span><span>Stairs</span><span>;</span><span>

            </span><span>// Format the information</span><span>
            </span><span>String</span><span> info </span><span>=</span><span> </span><span>"\nNumber of stories:  "</span><span> </span><span>+</span><span> stairs</span><span>.</span><span>NumberOfStories</span><span>;</span><span>
            info </span><span>+=</span><span> </span><span>"\nHeight of stairs:  "</span><span> </span><span>+</span><span> stairs</span><span>.</span><span>Height</span><span>;</span><span>
            info </span><span>+=</span><span> </span><span>"\nNumber of treads:  "</span><span> </span><span>+</span><span> stairs</span><span>.</span><span>ActualTreadsNumber</span><span>;</span><span>
            info </span><span>+=</span><span> </span><span>"\nTread depth:  "</span><span> </span><span>+</span><span> stairs</span><span>.</span><span>ActualTreadDepth</span><span>;</span><span>

            </span><span>// Show the information to the user.</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> stairs</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The StairsType class represents the type for a Stairs element. It contains information about the Stairs, such as the type of all runs and landings in the stairs object, types and offsets for supports on the left, right and middle of the stairs, and numerous other properties related to stair generation such as the maximum height of each riser on the stair element. The following example gets the StairsType for a Stairs element and displays some information about it in a TaskDialog.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_C972319DB4D349ADAEC16C60C3936137"><tbody><tr><td><b>Code Region: Getting StairsType Info</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetStairsType</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>StairsType</span><span> stairsType </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>stairs</span><span>.</span><span>GetTypeId</span><span>())</span><span> </span><span>as</span><span> </span><span>StairsType</span><span>;</span><span>

    </span><span>// Format stairs type info for display</span><span>
    </span><span>string</span><span> info </span><span>=</span><span> </span><span>"Stairs Type:  "</span><span> </span><span>+</span><span> stairsType</span><span>.</span><span>Name</span><span>;</span><span>
    info </span><span>+=</span><span> </span><span>"\nLeft Lateral Offset:  "</span><span> </span><span>+</span><span> stairsType</span><span>.</span><span>LeftLateralOffset</span><span>;</span><span>
    info </span><span>+=</span><span> </span><span>"\nRight Lateral Offset:  "</span><span> </span><span>+</span><span> stairsType</span><span>.</span><span>RightLateralOffset</span><span>;</span><span>
    info </span><span>+=</span><span> </span><span>"\nMax Riser Height:  "</span><span> </span><span>+</span><span> stairsType</span><span>.</span><span>MaxRiserHeight</span><span>;</span><span>
    info </span><span>+=</span><span> </span><span>"\nMin Run Width:  "</span><span> </span><span>+</span><span> stairsType</span><span>.</span><span>MinRunWidth</span><span>;</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Runs

Stairs by component are composed of runs, landings and supports. Each of these items can be retrieved from the Stairs class. A run is represented in the Revit API by the StairsRun class. The following example gets each run for a Stairs object and makes sure that it begins and ends with a riser.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_0B79D7FFCBD849BBA8A55B8F082124A1"><tbody><tr><td><b>Code Region: Working with StairsRun</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>AddStartandEndRisers</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> runIds </span><span>=</span><span> stairs</span><span>.</span><span>GetStairsRuns</span><span>();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> runId </span><span>in</span><span> runIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>StairsRun</span><span> run </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>runId</span><span>)</span><span> </span><span>as</span><span> </span><span>StairsRun</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> run</span><span>)</span><span>
        </span><span>{</span><span>
            run</span><span>.</span><span>BeginsWithRiser</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
            run</span><span>.</span><span>EndsWithRiser</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The StairsRun class provides access to run properties such as the StairsRunStyle (straight, winder, etc.), BaseElevation, TopElevation, and properties about the risers. There are also methods in the StairsRun class to access the supports hosted by the run, either all, or just those on the left or right side of the run boundaries. The GetStairsPath() method will return the curves representing the stairs path on the run, which are projected onto the base level of the stairs. The GetFootprintBoundary() method returns the run's boundary curves which are also projected onto the stairs' base level.

There are three static methods of the StairsRun class for creating new runs. These are covered in the [Creating and Editing Stairs](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Creating_and_Editing_Stairs_html) section.

The StairsRunType class represents the type of a StairsRun. It contains many properties about the treads and risers of the run as well as other information about the run. The following example gets the StairsRunType for the first run in a Stairs element and displays the riser and tread thicknesses along with the type's name.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_E1A09621684D4548A06A48C661799474"><tbody><tr><td><b>Code Region: Getting StairsRunType Info</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetRunType</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> runIds </span><span>=</span><span> stairs</span><span>.</span><span>GetStairsRuns</span><span>();</span><span>

    </span><span>ElementId</span><span> firstRunId </span><span>=</span><span> runIds</span><span>.</span><span>First</span><span>();</span><span>

    </span><span>StairsRun</span><span> firstRun </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>firstRunId</span><span>)</span><span> </span><span>as</span><span> </span><span>StairsRun</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> firstRun</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>StairsRunType</span><span> runType </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>firstRun</span><span>.</span><span>GetTypeId</span><span>())</span><span> </span><span>as</span><span> </span><span>StairsRunType</span><span>;</span><span>
        </span><span>// Format landing type info for display</span><span>
        </span><span>string</span><span> info </span><span>=</span><span> </span><span>"Stairs Run Type:  "</span><span> </span><span>+</span><span> runType</span><span>.</span><span>Name</span><span>;</span><span>
        info </span><span>+=</span><span> </span><span>"\nRiser Thickness:  "</span><span> </span><span>+</span><span> runType</span><span>.</span><span>RiserThickness</span><span>;</span><span>
        info </span><span>+=</span><span> </span><span>"\nTread Thickness:  "</span><span> </span><span>+</span><span> runType</span><span>.</span><span>TreadThickness</span><span>;</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Landings

Landings are represented by the StairsLanding class. The following example finds the thickness for each landing of a Stairs object.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_60B7CA2A99E04769B1EDC89B16D26FB6"><tbody><tr><td><b>Code Region: Working with StairsLanding</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetStairLandings</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> landingIds </span><span>=</span><span> stairs</span><span>.</span><span>GetStairsLandings</span><span>();</span><span>
    </span><span>string</span><span> info </span><span>=</span><span> </span><span>"Number of landings:  "</span><span> </span><span>+</span><span> landingIds</span><span>.</span><span>Count</span><span>;</span><span>

    </span><span>int</span><span> landingIndex </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> landingId </span><span>in</span><span> landingIds</span><span>)</span><span>
    </span><span>{</span><span>
        landingIndex</span><span>++;</span><span>
        </span><span>StairsLanding</span><span> landing </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>landingId</span><span>)</span><span> </span><span>as</span><span> </span><span>StairsLanding</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> landing</span><span>)</span><span>
        </span><span>{</span><span>
            info </span><span>+=</span><span> </span><span>"\nThickness of Landing "</span><span> </span><span>+</span><span> landingIndex </span><span>+</span><span> </span><span>":  "</span><span> </span><span>+</span><span> landing</span><span>.</span><span>Thickness</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Similar to StairsRun, StairsLanding has a GetStairsPath() method which returns the curves representing the stairs path on the landing projected onto the base level of the stairs and a GetFootprintBoundary() method which returns the landing's boundary curves, also projected onto the stairs' base level. Also similar to StairsRun, there is a method to get all of the supports hosted by the landing.

The StairsLanding class has a method to create a new landing between two runs. It is covered in the [Creating and Editing Stairs](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Creating_and_Editing_Stairs_html) section.

The StairsLandingType class represents a landing type in the Revit API. The StairsLandingType class has only a couple of properties specific to it, namely IsMonolithic which is true if the stairs landing is monolithic, and Thickness, representing the thickness of the stairs landing.

### StairsComponentConnection

Both StairsRun and StairsLanding have a GetConnections() method which provides information about connections among stairs components (run to run, or run to landing). The method returns a collection of StairsComponentConnection objects which have properties about each connection, including the connection type (to a landing, the start of a stairs run, or the end of a stairs run) and the Id of the connected stairs component.

### Supports

The Revit API does not expose a class for stairs supports. When getting the supports for Stairs, StairsRun, or a StairsLanding, the supports will be generic Revit Elements. The following example gets the names of all the supports for a Stairs object.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_C3E772C35A984044B3CE88EBDE20362A"><tbody><tr><td><b>Code Region: Getting Stairs Supports</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetStairSupports</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> supportIds </span><span>=</span><span> stairs</span><span>.</span><span>GetStairsSupports</span><span>();</span><span>
    </span><span>string</span><span> info </span><span>=</span><span> </span><span>"Number of supports:  "</span><span> </span><span>+</span><span> supportIds</span><span>.</span><span>Count</span><span>;</span><span>

    </span><span>int</span><span> supportIndex </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> supportId </span><span>in</span><span> supportIds</span><span>)</span><span>
    </span><span>{</span><span>
        supportIndex</span><span>++;</span><span>
        </span><span>Element</span><span> support </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>supportId</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> support</span><span>)</span><span>
        </span><span>{</span><span>
            info </span><span>+=</span><span> </span><span>"\nName of support "</span><span> </span><span>+</span><span> supportIndex </span><span>+</span><span> </span><span>":  "</span><span> </span><span>+</span><span> support</span><span>.</span><span>Name</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
