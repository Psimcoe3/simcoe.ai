---
created: 2026-01-28T20:48:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_User_Selection_html
author: 
---

# Help | User Selection | Autodesk

> ## Excerpt
> The Selection class also has methods for allowing the user to select new objects, or even a point on screen. This allows the user to select one or more Elements (or other objects, such as an edge or a face) using the cursor and then returns control to your application. These functions do not automatically add the new selection to the active selection collection.

---
The Selection class also has methods for allowing the user to select new objects, or even a point on screen. This allows the user to select one or more Elements (or other objects, such as an edge or a face) using the cursor and then returns control to your application. These functions do not automatically add the new selection to the active selection collection.

-   The PickObject() method prompts the user to select an object in the Revit model.
-   The PickObjects() method prompts the user to select multiple objects in the Revit model.
-   The PickElementsByRectangle() method prompts the user to select multiple elements using a rectangle.
-   The PickPoint() method prompts the user to pick a point in the active sketch plane.
-   The PickBox() method invokes a general purpose two-click editor that lets the user to specify a rectangular area on the screen.

The type of object to be selected is specified when calling PickObject() or PickObjects. Types of objects that can be specified are: Element, PointOnElement, Edge or Face.

The StatusbarTip property shows a message in the status bar when your application prompts the user to pick objects or elements. Each of the Pick functions has an overload that has a String parameter in which a custom status message can be provided.

<table summary="" id="GUID-97372731-5ACA-4EB7-ABDF-7E6B56640DA2__TABLE_F2441DC827DC4D3481B67DC8C3B6EF26"><tbody><tr><td><b>Code Region 7-2: Adding selected elements with PickObject() and PickElementsByRectangle()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SelectElements</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>Selection</span><span> choices </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>;</span><span>
    </span><span>// Pick one object from Revit.</span><span>
    </span><span>Reference</span><span> hasPickOne </span><span>=</span><span> choices</span><span>.</span><span>PickObject</span><span>(</span><span>ObjectType</span><span>.</span><span>Element</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>hasPickOne </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"One element selected."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Use the rectangle picking tool to identify model elements to select.</span><span>
    </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> pickedElements </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>PickElementsByRectangle</span><span>(</span><span>"Select by rectangle"</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>pickedElements</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span> 
        </span><span>// Collect Ids of all picked elements</span><span>
        </span><span>IList</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> idsToSelect </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;(</span><span>pickedElements</span><span>.</span><span>Count</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> element </span><span>in</span><span> pickedElements</span><span>)</span><span>
        </span><span>{</span><span>
            idsToSelect</span><span>.</span><span>Add</span><span>(</span><span>element</span><span>.</span><span>Id</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>// Update the current selection</span><span>
        uidoc</span><span>.</span><span>Selection</span><span>.</span><span>SetElementIds</span><span>(</span><span>idsToSelect</span><span>);</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>string</span><span>.</span><span>Format</span><span>(</span><span>"{0} elements added to Selection."</span><span>,</span><span> idsToSelect</span><span>.</span><span>Count</span><span>));</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The PickPoint() method has 2 overloads with an ObjectSnapTypes parameter which is used to specify the type of snap types used for the selection. More than one can be specified, as shown in the next example.

<table summary="" id="GUID-97372731-5ACA-4EB7-ABDF-7E6B56640DA2__TABLE_772F9E8F0AC743EF8613D7CF268C9035"><tbody><tr><td><b>Code Region 7-3: Snap points</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>PickPoint</span><span>(</span><span>UIDocument</span><span> uidoc</span><span>)</span><span>
</span><span>{</span><span>

        </span><span>ObjectSnapTypes</span><span> snapTypes </span><span>=</span><span> </span><span>ObjectSnapTypes</span><span>.</span><span>Endpoints</span><span> </span><span>|</span><span> </span><span>ObjectSnapTypes</span><span>.</span><span>Intersections</span><span>;</span><span>
        XYZ point </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>PickPoint</span><span>(</span><span>snapTypes</span><span>,</span><span> </span><span>"Select an end point or intersection"</span><span>);</span><span>

        </span><span>string</span><span> strCoords </span><span>=</span><span> </span><span>"Selected point is "</span><span> </span><span>+</span><span> point</span><span>.</span><span>ToString</span><span>();</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> strCoords</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The PickBox() method takes a PickBoxStyle enumerator. The options are Crossing, the style used when selecting objects completely or partially inside the box, Enclosing, the style used selecting objects that are completely enclosed by the box, and Directional, in which the style of the box depends on the direction in which the box is being drawn. It uses the Crossing style if it is being drawn from right to left, or the Enclosing style when drawn in the opposite direction.

PickBox() returns a PickedBox which contains the Min and Max points selected. The following example demonstrates the use of PickBox() in Point Cloud selection.

<table summary="" id="GUID-97372731-5ACA-4EB7-ABDF-7E6B56640DA2__TABLE_F4E420FBF48D45BFA285281678FB7B98"><tbody><tr><td><b>Code Region: PickBox</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>PromptForPointCloudSelection</span><span>(</span><span>UIDocument</span><span> uiDoc</span><span>,</span><span> </span><span>PointCloudInstance</span><span> pcInstance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span> uiDoc</span><span>.</span><span>Application</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>Selection</span><span> currentSel </span><span>=</span><span> uiDoc</span><span>.</span><span>Selection</span><span>;</span><span>

    </span><span>PickedBox</span><span> pickedBox </span><span>=</span><span> currentSel</span><span>.</span><span>PickBox</span><span>(</span><span>PickBoxStyle</span><span>.</span><span>Enclosing</span><span>,</span><span> </span><span>"Select region of cloud for highlighting"</span><span>);</span><span>

    XYZ min </span><span>=</span><span> pickedBox</span><span>.</span><span>Min</span><span>;</span><span>
    XYZ max </span><span>=</span><span> pickedBox</span><span>.</span><span>Max</span><span>;</span><span>

    </span><span>//Transform points into filter</span><span>
    </span><span>View</span><span> view </span><span>=</span><span> uiDoc</span><span>.</span><span>ActiveView</span><span>;</span><span>
    XYZ right </span><span>=</span><span> view</span><span>.</span><span>RightDirection</span><span>;</span><span>
    XYZ up </span><span>=</span><span> view</span><span>.</span><span>UpDirection</span><span>;</span><span>

    </span><span>List</span><span>&lt;</span><span>Plane</span><span>&gt;</span><span> planes </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Plane</span><span>&gt;();</span><span>

    </span><span>// X boundaries</span><span>
    </span><span>bool</span><span> directionCorrect </span><span>=</span><span> </span><span>IsPointAbovePlane</span><span>(</span><span>right</span><span>,</span><span> min</span><span>,</span><span> max</span><span>);</span><span>
    planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>right</span><span>,</span><span> directionCorrect </span><span>?</span><span> min </span><span>:</span><span> max</span><span>));</span><span>
    planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(-</span><span>right</span><span>,</span><span> directionCorrect </span><span>?</span><span> max </span><span>:</span><span> min</span><span>));</span><span>

    </span><span>// Y boundaries</span><span>
    directionCorrect </span><span>=</span><span> </span><span>IsPointAbovePlane</span><span>(</span><span>up</span><span>,</span><span> min</span><span>,</span><span> max</span><span>);</span><span>
    planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>up</span><span>,</span><span> directionCorrect </span><span>?</span><span> min </span><span>:</span><span> max</span><span>));</span><span>
    planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(-</span><span>up</span><span>,</span><span> directionCorrect </span><span>?</span><span> max </span><span>:</span><span> min</span><span>));</span><span>

    </span><span>// Create filter</span><span>
    </span><span>PointCloudFilter</span><span> filter </span><span>=</span><span> </span><span>PointCloudFilterFactory</span><span>.</span><span>CreateMultiPlaneFilter</span><span>(</span><span>planes</span><span>);</span><span>
    </span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>uiDoc</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Highlight"</span><span>);</span><span>
    t</span><span>.</span><span>Start</span><span>();</span><span>
    pcInstance</span><span>.</span><span>SetSelectionFilter</span><span>(</span><span>filter</span><span>);</span><span>
    pcInstance</span><span>.</span><span>FilterAction</span><span> </span><span>=</span><span> </span><span>SelectionFilterAction</span><span>.</span><span>Highlight</span><span>;</span><span>
    t</span><span>.</span><span>Commit</span><span>();</span><span>
    uiDoc</span><span>.</span><span>RefreshActiveView</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Selection Events

The `SelectionChanged` event notifies your code after the selection changes. `SelectionChangedEventArgs` provides access to the references and element ids that are selected.
