---
created: 2026-01-28T21:03:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_The_2D_Sketch_Class_html
author: 
---

# Help | The 2D Sketch Class | Autodesk

> ## Excerpt
> The Sketch class represents enclosed curves in a plane used to create a 3D model. The key features are represented by the SketchPlane and CurveLoop properties.

---
The Sketch class represents enclosed curves in a plane used to create a 3D model. The key features are represented by the SketchPlane and CurveLoop properties.

When accessing the Family's 3D modeling information, Sketch objects are important to forming the geometry. For more details, refer to [3D Sketch](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_3D_Sketch_html).

SketchPlane is the basis for all 2D sketch classes such as ModelCurve and Sketch. SketchPlane is also the basis for 2D Annotation Elements such as DetailCurve. Both ModelCurve and DetailCurve have the SketchPlane property and need a SketchPlane in the corresponding creation method. SketchPlane is always invisible in the Revit UI.

Every ModelCurve must lie in one SketchPlane. In other words, wherever you draw a ModelCurve either in the UI or by using the API, a SketchPlane must exist. Therefore, at least one SketchPlane exists in a 2D view where a ModelCurve is drawn.

The 2D view contains the CeilingPlan, FloorPlan, and Elevation ViewTypes. By default, a SketchPlane is automatically created for all of these views. The 2D view-related SketchPlane Name returns the view name such as Level 1 or North.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-9B03E831-1E6C-4CE2-9149-3F7B309A5B5D-low.png)**Figure 77: Pick a Plane to identify a new Work Plane**

When you specify a new work plane, you can select Pick a plane as illustrated in the previous picture. After you pick a plane, select a plane on a particular element such as a wall as the following picture shows. In this case, the SketchPlane.Name property returns a string related to that element. For example, in the following picture, the SketchPlane.Name property returns 'Generic - 8' the same as the Wall.Name property.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-67D74CA2-D850-422F-A4FF-E762D683DFC9-low.png)**Figure 78: Pick a Plane on a wall as Work Plane**

Note: A SketchPlane is different from a work plane because a work plane is visible and can be selected. It does not have a specific class in the current API, but is represented by the Element class. A work plane must be defined based on a specific SketchPlane. Both the work plane and SketchPlane Category property return null. Although SketchPlane is always invisible, there is always a SketchPlane that corresponds to a work plane. A work plane is used to express a SketchPlane in text and pictures.

The following information applies to SketchPlane members:

-   ID, UniqueId, Name, and Plane properties return a value;
-   Parameters property is empty
-   Location property returns a Location object
-   Other properties return null.

Plane contains the SketchPlane geometric information. SketchPlane sets up a plane coordinate system with Plane as the following picture illustrates:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-415773EF-49A7-4158-B9DD-42A218063E81-low.png)**Figure 79: SketchPlane and Plane coordinate system**

The following code sample illustrates how to create a new SketchPlane:

<table summary="" id="GUID-CE1C6B63-772E-4AE0-897D-E6E06F90ADD7__TABLE_24FD6CD153D048A38D1ECE7471BAF3FD"><tbody><tr><td><b>Code Region 17-1: Creating a new SketchPlane</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>SketchPlane</span><span> </span><span>CreateSketchPlane</span><span>(</span><span>UIApplication</span><span> application</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>//try to create a new sketch plane</span><span>
    XYZ newNormal </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>  </span><span>// the normal vector</span><span>
    XYZ newOrigin </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>  </span><span>// the origin point</span><span>
    </span><span>// create geometry plane</span><span>
    </span><span>Plane</span><span> geometryPlane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>newNormal</span><span>,</span><span> newOrigin</span><span>);</span><span>

    </span><span>// create sketch plane</span><span>
    </span><span>SketchPlane</span><span> sketchPlane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span>(</span><span>application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>,</span><span>geometryPlane</span><span>);</span><span>

    </span><span>return</span><span> sketchPlane</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
