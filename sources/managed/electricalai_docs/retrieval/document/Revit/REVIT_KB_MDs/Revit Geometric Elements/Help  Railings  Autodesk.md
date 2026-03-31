---
created: 2026-01-28T21:04:15 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Railings_html
author: 
---

# Help | Railings | Autodesk

> ## Excerpt
> The Autodesk.Revit.DB.Architecture.Railing class represents a railing element in an Autodesk Revit project. Although railings are associated with stairs, they can be associated with another host (such as a floor) or placed in space.

---
The Autodesk.Revit.DB.Architecture.Railing class represents a railing element in an Autodesk Revit project. Although railings are associated with stairs, they can be associated with another host (such as a floor) or placed in space.

A Railing may be associated with up to five continuous rails and a RailingType which contains information about balusters and any number of non-continuous rails. Continuous rails may either be a top rail or a hand rail.

Railings represent the entire structure which includes continuous rails, non-continuous rails, balusters, and corner posts. Continuous rails refer to the top rail (TopRail class is a subclass of ContinuousRail) and the two possible hand rails (HandRail class is a subclass of ContinuousRail), each of which may appear on the left, right, or both left and right which counts as 2 of the 5 possible continuous rails. The continuous rails are directly accessible from the Railing via the TopRail property and the GetHandRails() method.

A non-continuous rail is a rail which runs parallel to the Railing’s path elevated by a height not greater than the railing’s height. A default-generated railing’s non-continuous rails are broken into sections by the balusters. A Railing may have zero or more rails and must have at least one baluster. The non-continuous rails and baluster placement are accessible via the RailingType.

Railings associated with stairs can be retrieved from the Stairs class with the GetAssociatedRailings() method. There are only a few properties and methods specific to railings such as the TopRail property which returns the ElementId of the top rail and Flipped which indicates if the Railing is flipped. The Railing.Flip() method flips the railing (for a stair-hosted railing, flip changes the railing position between placement on the treads or stringers), while the RemoveHost() method will remove the association between the railing and its host.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/Railing.jpg)

The following example retrieves all of the railings associated with a Stairs object and flips each railing that is the default railing that the system generates.

<table summary="" id="GUID-9AE06169-CC2A-423B-B737-C26B3B9D4544__TABLE_8F3098B661784895AB4C934C8A55AE9A"><tbody><tr><td><b>Code Region: Working with Railings</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>FlipDefaultRailings</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> railingIds </span><span>=</span><span> stairs</span><span>.</span><span>GetAssociatedRailings</span><span>();</span><span>
    </span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>stairs</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Flip Railings"</span><span>);</span><span>
    trans</span><span>.</span><span>Start</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> railingId </span><span>in</span><span> railingIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Railing</span><span> railing </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>railingId</span><span>)</span><span> </span><span>as</span><span> </span><span>Railing</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>railing</span><span>.</span><span>IsDefault</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
        </span><span>{</span><span>
            railing</span><span>.</span><span>Flip</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    trans</span><span>.</span><span>Commit</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The Railing class has a Create method which automatically creates new railings with the specified railing type on all sides of a stairs element. Railing creation is demonstrated in the [Creating and Editing Stairs](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Creating_and_Editing_Stairs_html) section.

The RailingType class represents the railing type used in the generation of a railing. It contains a number of properties about the railing, such as the height, lateral offset and type of the primary and secondary handrails as well as the top rail.

<table summary="" id="GUID-9AE06169-CC2A-423B-B737-C26B3B9D4544__TABLE_C0752DE658B944D0849B99896A1EE101"><tbody><tr><td><b>Code Region: RailingType</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetRailingType</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> railingIds </span><span>=</span><span> stairs</span><span>.</span><span>GetAssociatedRailings</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> railingId </span><span>in</span><span> railingIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Railing</span><span> railing </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>railingId</span><span>)</span><span> </span><span>as</span><span> </span><span>Railing</span><span>;</span><span>
        </span><span>RailingType</span><span> railingType </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>railing</span><span>.</span><span>GetTypeId</span><span>())</span><span> </span><span>as</span><span> </span><span>RailingType</span><span>;</span><span>

        </span><span>// Format railing type info for display</span><span>
        </span><span>string</span><span> info </span><span>=</span><span> </span><span>"Railing Type:  "</span><span> </span><span>+</span><span> railingType</span><span>.</span><span>Name</span><span>;</span><span>
        info </span><span>+=</span><span> </span><span>"\nPrimary Handrail Height:  "</span><span> </span><span>+</span><span> railingType</span><span>.</span><span>PrimaryHandrailHeight</span><span>;</span><span>
        info </span><span>+=</span><span> </span><span>"\nTop Rail Height:  "</span><span> </span><span>+</span><span> railingType</span><span>.</span><span>TopRailHeight</span><span>;</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Non-continuous Railings

```
RailingType.RailStructure
```

provide access to a collection of information about non-continuous rails that are part of a RailingType. The Autodesk.Revit.DB.Architecture.NonContinuousRailStructure returns a collection of Autodesk.Revit.DB.Architecture.NonContinuousRailInfo objects, each of which represents the properties needed to define a single non-continuous rail.

## Baluster Placement

```
RailingType.BalusterPlacement
```

provides access to the baluster and post placement information for a given railing type. The Autodesk.Revit.DB.Architecture.BalusterPlacement that it returns may contain instances of:

-   Autodesk.Revit.DB.Architecture.BalusterPattern which represents the baluster pattern properties, containing 1 or more objects of the type BalusterInfo.
-   Autodesk.Revit.DB.Architecture.PostPattern which represents the post pattern properties, containing up to 3 objects of the type BalusterInfo
-   Autodesk.Revit.DB.Architecture.BalusterInfo which represents the properties governing an instance of a single railing baluster or post

To get the name used to reference the Host or Top Rail, use:

-   BalusterInfo.GetReferenceNameForHost()
-   BalusterInfo.GetReferenceNameForTopRail()
