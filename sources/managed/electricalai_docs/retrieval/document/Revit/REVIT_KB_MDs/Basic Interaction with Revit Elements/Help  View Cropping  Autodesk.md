---
created: 2026-01-28T20:53:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Cropping_html
author: 
---

# Help | View Cropping | Autodesk

> ## Excerpt
> The crop region for some views may be modified using the Revit API. The ViewCropRegionShapeManager.CanHaveShape property indicates whether the view is allowed to manage the crop region shape while the ShapeSet property indicates whether a shape has been set. The following example crops a view around the boundary of a room.

---
The crop region for some views may be modified using the Revit API. The ViewCropRegionShapeManager.CanHaveShape property indicates whether the view is allowed to manage the crop region shape while the ShapeSet property indicates whether a shape has been set. The following example crops a view around the boundary of a room.

<table summary="" id="GUID-E3DBA0F4-2B15-4A6D-B485-36D15DE0A916__TABLE_72AEEE429B1140D0A36F8742EAFCBE84"><tbody><tr><td><b>Code Region: Cropping a view</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CropAroundRoom</span><span>(</span><span>Room</span><span> room</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(</span><span>view </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>IList</span><span>&lt;</span><span>IList</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>BoundarySegment</span><span>&gt;&gt;</span><span> segments </span><span>=</span><span> room</span><span>.</span><span>GetBoundarySegments</span><span>(</span><span>new</span><span> </span><span>SpatialElementBoundaryOptions</span><span>());</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> segments</span><span>)</span><span>  </span><span>//the room may not be bound</span><span>
        </span><span>{</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>IList</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>BoundarySegment</span><span>&gt;</span><span> segmentList </span><span>in</span><span> segments</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>CurveLoop</span><span> loop </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveLoop</span><span>();</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>BoundarySegment</span><span> boundarySegment </span><span>in</span><span> segmentList</span><span>)</span><span>
                </span><span>{</span><span>
                    loop</span><span>.</span><span>Append</span><span>(</span><span>boundarySegment</span><span>.</span><span>GetCurve</span><span>());</span><span>
                </span><span>}</span><span>

                </span><span>ViewCropRegionShapeManager</span><span> vcrShapeMgr </span><span>=</span><span> view</span><span>.</span><span>GetCropRegionShapeManager</span><span>();</span><span>
                vcrShapeMgr</span><span>.</span><span>SetCropShape</span><span>(</span><span>loop</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>  </span><span>// if more than one set of boundary segments for room, crop around the first one</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
