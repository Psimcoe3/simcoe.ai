---
created: 2026-01-28T20:50:55 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Mirroring_Elements_html
author: 
---

# Help | Mirroring Elements | Autodesk

> ## Excerpt
> The ElementTransformUtils class provides two static methods to mirror one or more elements in the project.

---
The ElementTransformUtils class provides two static methods to mirror one or more elements in the project.

**Table 21: Mirror Methods**

|  |  |
| --- | --- |
| Member | Description |
| `MirrorElement(Document, ElementId, Plane)` | Mirror one element about a geometric plane. |
| `MirrorElements(Document, ICollection<ElementId>, Plane, Boolean)` | Mirror several elements about a geometric plane. Can be performed on original geometry or a copy. |

After performing the mirror operation, you can access the new elements from the Selection ElementSet.

ElementTransformUtils.CanMirrorElement() and ElementTransformUtils.CanMirrorElements() can be used to determine if one or more elements can be mirrored prior to attempting to mirror an element.

The following code illustrates how to mirror a wall using a plane calculated based on a side face of the wall.

<table summary="" id="GUID-E49EB503-604A-43B7-A3F2-4069DD09EBE2__TABLE_885C80106AF447449B7395C57BE99E37"><tbody><tr><td><b>Code Region 10-8: Mirroring a wall</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MirrorWall</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Reference</span><span> reference </span><span>=</span><span> </span><span>HostObjectUtils</span><span>.</span><span>GetSideFaces</span><span>(</span><span>wall</span><span>,</span><span> </span><span>ShellLayerType</span><span>.</span><span>Exterior</span><span>).</span><span>First</span><span>();</span><span>

        </span><span>// get one of the wall's major side faces</span><span>
        </span><span>Face</span><span> face </span><span>=</span><span> wall</span><span>.</span><span>GetGeometryObjectFromReference</span><span>(</span><span>reference</span><span>)</span><span> </span><span>as</span><span> </span><span>Face</span><span>;</span><span> 

        UV bboxMin </span><span>=</span><span> face</span><span>.</span><span>GetBoundingBox</span><span>().</span><span>Min</span><span>;</span><span>
        </span><span>// create a plane based on this side face with an offset of 10 in the X &amp; Y directions</span><span>

        </span><span>Plane</span><span> plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>face</span><span>.</span><span>ComputeNormal</span><span>(</span><span>bboxMin</span><span>),</span><span> 
                face</span><span>.</span><span>Evaluate</span><span>(</span><span>bboxMin</span><span>).</span><span>Add</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>)));</span><span>

        </span><span>ElementTransformUtils</span><span>.</span><span>MirrorElement</span><span>(</span><span>document</span><span>,</span><span> wall</span><span>.</span><span>Id</span><span>,</span><span> plane</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Every FamilyInstance has a Mirrored property. It indicates whether a FamilyInstance (for example a column) is mirrored.
