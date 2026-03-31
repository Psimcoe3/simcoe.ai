---
created: 2026-01-28T21:04:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Stairs_Annotations_html
author: 
---

# Help | Stairs Annotations | Autodesk

> ## Excerpt
> The StairsPath class can be used to annotate the slope direction and walk line of a stair. The static StairsPath.Create() method will create a new stairs path for the specified stairs with the specified stairs path type in a specific plan view in which the stairs must be visible.

---
The StairsPath class can be used to annotate the slope direction and walk line of a stair. The static StairsPath.Create() method will create a new stairs path for the specified stairs with the specified stairs path type in a specific plan view in which the stairs must be visible.

The StairsPath class has the same properties that are available in the Properties window when editing a stairs path in the Revit UI, such as properties to set the up and down text along or whether the text should be shown at all. Additionally offsets for the up and down text can be specified as can an offset for the stairs path from the stairs centerline.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/StairsPathProperties.jpg)The following example finds a StairsPathType and a FloorPlan in the project and uses them to create a new StairsPath for a given Stairs.

<table summary="" id="GUID-180FDD83-9C51-432E-808B-7868B3C2D97E__TABLE_B273DBEDFE7E47FFBC2DCD6B772DB254"><tbody><tr><td><b>Code Region: Create a StairsPath</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateStairsPath</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Transaction</span><span> transNewPath </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"New Stairs Path"</span><span>);</span><span>
    transNewPath</span><span>.</span><span>Start</span><span>();</span><span>

    </span><span>// Find StairsPathType</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> stairsPathIds </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>StairsPathType</span><span>)).</span><span>ToElementIds</span><span>();</span><span>

    </span><span>// Find a FloorPlan</span><span>
    </span><span>ElementId</span><span> planViewId </span><span>=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>;</span><span>
    </span><span>FilteredElementCollector</span><span> viewCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> viewIds </span><span>=</span><span> viewCollector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>View</span><span>)).</span><span>ToElementIds</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> viewId </span><span>in</span><span> viewIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>View</span><span> view </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>viewId</span><span>)</span><span> </span><span>as</span><span> </span><span>View</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>view</span><span>.</span><span>ViewType</span><span> </span><span>==</span><span> </span><span>ViewType</span><span>.</span><span>FloorPlan</span><span>)</span><span>
        </span><span>{</span><span>
            planViewId </span><span>=</span><span> view</span><span>.</span><span>Id</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>LinkElementId</span><span> stairsLinkId </span><span>=</span><span> </span><span>new</span><span> </span><span>LinkElementId</span><span>(</span><span>stairs</span><span>.</span><span>Id</span><span>);</span><span>
    </span><span>StairsPath</span><span>.</span><span>Create</span><span>(</span><span>stairs</span><span>.</span><span>Document</span><span>,</span><span> stairsLinkId</span><span>,</span><span> stairsPathIds</span><span>.</span><span>First</span><span>(),</span><span> planViewId</span><span>);</span><span>
    transNewPath</span><span>.</span><span>Commit</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

A StairsPath has a StairsPathType. Stair path types are available from 2 predefined system families: Automatic Up/Down Direction and Fixed Up Direction. The properties available for these two types are available as properties in the StairsPathType class, such as FullStepArrow and DistanceToCutMark.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/StairsPathTypeProperties.jpg)The CutMarkType class represents a cut mark type in the Revit UI and it has properties to represent the same properties available when editing a cut mark type in the UI, such as CutLineAngle and CutLineExtension . It is associated with a StairsType object and can be retrieved using the BuiltInParameter STAIRSTYPE\_CUTMARK\_TYPE as shown below.

<table summary="" id="GUID-180FDD83-9C51-432E-808B-7868B3C2D97E__TABLE_901096B517C4435EB41D7F20744325A0"><tbody><tr><td><b>Code Region: Getting the CutMarkType for Stairs</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>CutMarkType</span><span> </span><span>GetCutMark</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>CutMarkType</span><span> cutMarkType </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>StairsType</span><span> stairsType </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>stairs</span><span>.</span><span>GetTypeId</span><span>())</span><span> </span><span>as</span><span> </span><span>StairsType</span><span>;</span><span>
    </span><span>Parameter</span><span> paramCutMark </span><span>=</span><span> stairsType</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>StairstypeCutmarkType</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>paramCutMark</span><span>.</span><span>StorageType</span><span> </span><span>==</span><span> </span><span>StorageType</span><span>.</span><span>ElementId</span><span>)</span><span>  </span><span>// should be an element id</span><span>
    </span><span>{</span><span>
        </span><span>ElementId</span><span> cutMarkId </span><span>=</span><span> paramCutMark</span><span>.</span><span>AsElementId</span><span>();</span><span>
        cutMarkType </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>cutMarkId</span><span>)</span><span> </span><span>as</span><span> </span><span>CutMarkType</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> cutMarkType</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
