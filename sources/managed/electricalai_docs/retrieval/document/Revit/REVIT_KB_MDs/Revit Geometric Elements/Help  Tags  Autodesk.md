---
created: 2026-01-28T21:00:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_Tags_html
author: 
---

# Help | Tags | Autodesk

> ## Excerpt
> A tag is an annotation used to identify drawing elements. The API exposes the IndependentTag and RoomTag classes to cover most tags used in the Revit application. For more details about RoomTag, see Rooms.

---
A tag is an annotation used to identify drawing elements. The API exposes the IndependentTag and RoomTag classes to cover most tags used in the Revit application. For more details about RoomTag, see [Rooms](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Architecture_Rooms_html).

Note: The IndependentTag class represents the tag element in Revit and other specific tags such as keynote, beam system tag, electronic circuit symbol, and so on. In Revit internal code, the specific tags have corresponding classes derived from IndependentTag. As a result, specific features are not exposed by the API and cannot be created using IndependentTag.Create. They can be distinguished by the following categories:

**Table 37: Tag Name and Category**

<table summary="" id="GUID-E3445694-9F2C-4E0C-849A-60A505982FFB__TABLE_6D07D3FC37E142B1B1D0E8593FB75D73"><tbody><tr><td><b>Tag Name</b></td><td><b>BuiltInCategory</b></td></tr><tr><td>Keynote Tag</td><td>OST_KeynoteTags</td></tr><tr><td>Beam System Tag</td><td>OST_BeamSystemTags</td></tr><tr><td>Electronic Circuit Tag</td><td>OST_ElectricalCircuitTags</td></tr><tr><td>Span Direction Tag</td><td>OST_SpanDirectionSymbol</td></tr><tr><td>Path Reinforcement Span Tag</td><td>OST_PathReinSpanSymbol</td></tr><tr><td>Rebar System Span Tag</td><td>OST_IOSRebarSystemSpanSymbolCtrl</td></tr></tbody></table>

Every category in the family library has a pre-made tag. Some tags are automatically loaded with the default Revit application template, while others are loaded manually. The IndependentTag objects return different categories based on the host element if it is created using the By Category option. For example, the Wall and Floor IndependentTag are respectively OST\_WallTags and OST\_FloorTags.

If the tag is created using the Multi-Category or Material style, their categories are respectively OST\_MultiCategoryTags and OST\_MaterialTags.

Note: Note that IndependentTag.Create only works in the 2D view or in a locked 3D view, otherwise an exception is thrown. The following code is an example of IndependentTag creation. Run it when the level view is the active view.

Note: You can't change the text displayed in the IndependentTag directly. You need to change the parameter that is used to populate tag text in the Family Type for the Element that's being tagged. In the example below, that parameter is "Type Mark", although this setting can be changed in the Family Editor in the Revit UI.

The `LeadersPresentationMode` property specifies how leaders should be displayed on a tag. It has the following values:

-   ShowAll
-   HideAll
-   ShowOnlyOne
-   ShowSpecificLeaders

`IsLeaderVisible()` returns whether the leader that points to the specified reference is visible or not, and `SetIsLeaderVisible()` sets the visibility of the leader that points to the specified reference.

<table summary="" id="GUID-E3445694-9F2C-4E0C-849A-60A505982FFB__TABLE_6481FF8D46C043F198E27ABA78B514CC"><tbody><tr><td><b>Code Region 16-5: Creating an IndependentTag</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>IndependentTag</span><span> </span><span>CreateIndependentTag</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Reference</span><span> reference</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// make sure active view is not a 3D view</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>View</span><span> view </span><span>=</span><span> document</span><span>.</span><span>ActiveView</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>view </span><span>is</span><span> </span><span>View3D</span><span>)</span><span>
        </span><span>return</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// define tag mode and tag orientation for new tag</span><span>
    </span><span>TagMode</span><span> tagMode </span><span>=</span><span> </span><span>TagMode</span><span>.</span><span>TM_ADDBY_CATEGORY</span><span>;</span><span>
    </span><span>TagOrientation</span><span> tagorn </span><span>=</span><span> </span><span>TagOrientation</span><span>.</span><span>Horizontal</span><span>;</span><span>

    </span><span>// Add the tag to the middle of the wall</span><span>
    </span><span>Wall</span><span> wall </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>reference</span><span>)</span><span> </span><span>as</span><span> </span><span>Wall</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>wall </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>return</span><span> </span><span>null</span><span>;</span><span>

    </span><span>LocationCurve</span><span> wallLoc </span><span>=</span><span> wall</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
    XYZ wallStart </span><span>=</span><span> wallLoc</span><span>.</span><span>Curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>
    XYZ wallEnd </span><span>=</span><span> wallLoc</span><span>.</span><span>Curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>);</span><span>
    XYZ wallMid </span><span>=</span><span> wallLoc</span><span>.</span><span>Curve</span><span>.</span><span>Evaluate</span><span>(</span><span>0.5</span><span>,</span><span> </span><span>true</span><span>);</span><span>

    </span><span>IndependentTag</span><span> newTag </span><span>=</span><span> </span><span>IndependentTag</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> view</span><span>.</span><span>Id</span><span>,</span><span> reference</span><span>,</span><span> </span><span>true</span><span>,</span><span> tagMode</span><span>,</span><span> tagorn</span><span>,</span><span> wallMid</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> newTag</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create IndependentTag Failed."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// newTag.TagText is read-only, so we change the Type Mark type parameter to </span><span>
    </span><span>// set the tag text.  The label parameter for the tag family determines</span><span>
    </span><span>// what type parameter is used for the tag text.</span><span>

    </span><span>WallType</span><span> type </span><span>=</span><span> wall</span><span>.</span><span>WallType</span><span>;</span><span>

    </span><span>Parameter</span><span> foundParameter </span><span>=</span><span> type</span><span>.</span><span>LookupParameter</span><span>(</span><span>"Type Mark"</span><span>);</span><span>
    </span><span>bool</span><span> result </span><span>=</span><span> foundParameter</span><span>.</span><span>Set</span><span>(</span><span>"Hello"</span><span>);</span><span>

    </span><span>// set leader mode free</span><span>
    </span><span>// otherwise leader end point move with elbow point</span><span>

    newTag</span><span>.</span><span>LeaderEndCondition</span><span> </span><span>=</span><span> </span><span>LeaderEndCondition</span><span>.</span><span>Free</span><span>;</span><span>
    XYZ elbowPnt </span><span>=</span><span> wallMid </span><span>+</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5.0</span><span>,</span><span> </span><span>5.0</span><span>,</span><span> </span><span>0.0</span><span>);</span><span>
    newTag</span><span>.</span><span>SetLeaderElbow</span><span>(</span><span>reference</span><span>,</span><span> elbowPnt</span><span>);</span><span>
    XYZ headerPnt </span><span>=</span><span> wallMid </span><span>+</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10.0</span><span>,</span><span> </span><span>10.0</span><span>,</span><span> </span><span>0.0</span><span>);</span><span>
    newTag</span><span>.</span><span>TagHeadPosition</span><span> </span><span>=</span><span> headerPnt</span><span>;</span><span>

    </span><span>return</span><span> newTag</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-6FE76534-FEA8-4573-A2D7-747AB527B335-low.png)**Figure 74: Create IndependentTag using sample code**
