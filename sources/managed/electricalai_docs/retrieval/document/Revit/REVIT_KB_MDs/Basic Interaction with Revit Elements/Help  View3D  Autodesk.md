---
created: 2026-01-28T20:51:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_View3D_html
author: 
---

# Help | View3D | Autodesk

> ## Excerpt
> View3D is a freely-oriented three-dimensional view.

---
View3D is a freely-oriented three-dimensional view.

There are two kinds of 3D views, perspective and isometric, also referred to as orthographic in the Revit user interface. The difference is based on the projection ray relationship. The View3D.IsPerspective property indicates whether a 3D view is perspective or isometric.

### Perspective view

The following picture illustrates how a perspective view is created.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-EF11532A-32D3-40C1-9410-5AADA6FD8701-low.png)**Figure 96: Perspective projection**

-   The straight projection rays pass through each point in the model and intersect the projection plane to form the projection contents.
-   To facilitate the transformation from the world coordinate onto the view plane, the viewing coordinate system is based on the viewer.
-   Its origin, represented by the View.Origin property, is the viewer position.
-   The viewer's world coordinates are retrieved using the ViewOrientation3D.EyePosition property (retrieved from View3D.GetOrientation()). Therefore, in 3D views, View.Origin is always equal to the corresponding ViewOrientation3D.EyePosition.
-   As described in the diagram above, the _viewing_ coordinate system is determined as follows:
    -   The X-axis is determined by View.RightDirection.
    -   The Y-axis is determined by View.UpDirection.
    -   The Z-axis is determined by View.ViewDirection.
-   The view direction is from the target point to the viewer in the 3D space, and from the screen to the viewer in the screen space.

The static method View3D.CreatePerspective() method can be used to create new perspective views. The viewFamilyTypeId parameter needs to be a three dimensional ViewType.

The following code sample illustrates how to create a perspective 3D view.

<table summary="" id="GUID-A7FA8DBC-830E-482D-9B66-147399524442__TABLE_4626954938FB490F91459BC22476D840"><tbody><tr><td><b>Code Region: Creating a Perspective 3D view</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreatePerspective</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find a 3D view type</span><span>
    </span><span>IEnumerable</span><span>&lt;</span><span>ViewFamilyType</span><span>&gt;</span><span> viewFamilyTypes </span><span>=</span><span> </span><span>from</span><span> elem </span><span>in</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>).</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>ViewFamilyType</span><span>))</span><span>
        </span><span>let</span><span> type </span><span>=</span><span> elem </span><span>as</span><span> </span><span>ViewFamilyType</span><span>
        </span><span>where</span><span> type</span><span>.</span><span>ViewFamily</span><span> </span><span>==</span><span> </span><span>ViewFamily</span><span>.</span><span>ThreeDimensional</span><span>
        </span><span>select</span><span> type</span><span>;</span><span>
    </span><span>// Create a new Perspective View3D</span><span>
    </span><span>View3D</span><span> view3D </span><span>=</span><span> </span><span>View3D</span><span>.</span><span>CreatePerspective</span><span>(</span><span>document</span><span>,</span><span> viewFamilyTypes</span><span>.</span><span>First</span><span>().</span><span>Id</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> view3D</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// By default, the 3D view uses a default orientation.</span><span>
        </span><span>// Change the orientation by creating and setting a ViewOrientation3D </span><span>
        XYZ eye </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>10</span><span>);</span><span> 
        XYZ up </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>);</span><span> 
        XYZ forward </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span> 
        view3D</span><span>.</span><span>SetOrientation</span><span>(</span><span>new</span><span> </span><span>ViewOrientation3D</span><span>(</span><span>eye</span><span>,</span><span> up</span><span>,</span><span> forward</span><span>));</span><span>

        </span><span>// turn off the far clip plane with standard parameter API</span><span>
        </span><span>Parameter</span><span> farClip </span><span>=</span><span> view3D</span><span>.</span><span>LookupParameter</span><span>(</span><span>"Far Clip Active"</span><span>);</span><span>
        farClip</span><span>.</span><span>Set</span><span>(</span><span>0</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The perspective view crop box is part of a pyramid with the apex at the viewer position. It is the geometry between the two parallel clip planes. The crop box bounds the portion of the model that is clipped out and projected onto the view plane.

-   The crop box is represented by the View.CropBox property, which returns a BoundingBoxXYZ object.
-   The CropBox.Min and CropBox.Max points are marked in the previous picture. Note that the CropBox.Min point in a perspective view is generated by projecting the crop box front clip plane onto the back clip plane.

Crop box coordinates are based on the viewing coordinate system. Use Transform.OfPoint() to transform CropBox.Min and CropBox.Max to the world coordinate system. For more detail about Transform, refer to [Geometry Helper Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Helper_Classes_html) in the [Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html) section.

The project plane plus the front and back clip plane are all plumb to the view direction. The line between CropBox.Max and CropBox.Min is parallel to the view direction. With these factors, the crop box geometry can be calculated.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-CCAE0F1D-6889-4225-900A-45CF0D207B15-low.png)**Figure 97: Perspective 3D view**

The previous picture shows the projection plane on screen after cropping. The crop region is the rectangle intersection of the projection plane and crop box.

-   Geometry information is retrieved using the View.CropRegion property. This property returns a BoundingBoxUV instance.
-   The View.OutLine.Max property points to the upper right corner.
-   The View.OutLine.Min property points to the lower left corner.
-   Like the crop box, the crop region coordinates are based on the viewing coordinate system. The following expressions are equal.

```
View.CropBox.Max.X(Y) / View.OutLine.Max.X(Y) == View.CropBox.Min.X(Y) / View.OutLine.Min.X(Y)
```

Since the size of an object's perspective projection varies inversely with the distance from that object to the center of the projection, scale is meaningless for perspective views. The perspective 3D view Scale property always returns zero.

#### Managing the camera target

The camera represents the direction that the viewer of the perspective view is looking. If the user or an API application adjusts the crop region to expose a wider field of view or an unsymmetrical field of view, the distortion of the perspective view can become too drastic. The camera target can be forced to the center of the viewing region by calling the View3D method RestCameraTarget() which positions the target at the center of the field of view. Before calling, check to see if the camera can be reset in this view with the method View3D.CanResetCameraTarget() which indicates whether the camera target may be reset. The main situation where a target cannot be reset is if the View3D is currently in Isometric projection. Attempting to reset the camera target in an isometric view will throw an Autodesk.Revit.Exceptions.InvalidOperationException.

### Isometric view

A new isometric view can be created with the static View3D.CreateIsometric() method.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-6B8688A8-D480-4C35-84A2-5CA5CF8D1577-low.png)**Figure 98: Parallel projection**

Isometric views are generated using parallel projection rays by projecting the model onto a plane that is normal to the rays. The viewing coordinate system is similar to the perspective view, but the crop box is a parallelepiped with faces that are parallel or normal to the projection rays. The View.CropBox property points to two diagonal corners whose coordinates are based on the viewing coordinate system.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-A25AEAB3-BBF1-41E9-8B40-B1D40168A7AE-low.png)**Figure 99: Scale the window on view plane to screen viewport**

The model is projected onto a view plane and then scaled onto the screen. The View.Scale property represents the ratio of actual model size to the view size. The related expressions are as follows:

```
public void ViewScale(View view)
{
    view.CropBox.Max.X(Y) / view.OutLine.Max.X(Y) == view.CropBox.Min.X(Y) / view.OutLine.Min.X(Y) == view.Scale;
}
```

The viewFamilyTypeId parameter needs to be a three dimensional ViewType. Revit determines the following:

-   Position of the viewer.
-   How to create the viewing coordinate system using the view direction.
-   How to create the crop box to crop the model.

Once the view is created, you can resize the crop box to view different portions of the model. You can also change the default orientation. The API does not support modifying the viewing coordinate system.

The following code sample illustrates how to create an isometric 3D view.

<table summary="" id="GUID-A7FA8DBC-830E-482D-9B66-147399524442__TABLE_30E1090D72FA497FA5A324DCFAE10B2F"><tbody><tr><td><b>Code Region: Creating an Isometric 3D view</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateIso</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find a 3D view type</span><span>

    </span><span>IEnumerable</span><span>&lt;</span><span>ViewFamilyType</span><span>&gt;</span><span> viewFamilyTypes </span><span>=</span><span> </span><span>from</span><span> elem </span><span>in</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>).</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>ViewFamilyType</span><span>))</span><span>
        </span><span>let</span><span> type </span><span>=</span><span> elem </span><span>as</span><span> </span><span>ViewFamilyType</span><span>
        </span><span>where</span><span> type</span><span>.</span><span>ViewFamily</span><span> </span><span>==</span><span> </span><span>ViewFamily</span><span>.</span><span>ThreeDimensional</span><span>
        </span><span>select</span><span> type</span><span>;</span><span>

    </span><span>// Create a new View3D</span><span>
    </span><span>View3D</span><span> view3D </span><span>=</span><span> </span><span>View3D</span><span>.</span><span>CreateIsometric</span><span>(</span><span>document</span><span>,</span><span> viewFamilyTypes</span><span>.</span><span>First</span><span>().</span><span>Id</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> view3D</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// By default, the 3D view uses a default orientation.</span><span>
        </span><span>// Change the orientation by creating and setting a ViewOrientation3D </span><span>
        XYZ eye </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>10</span><span>);</span><span>
        XYZ up </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>);</span><span>
        XYZ forward </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>

        </span><span>ViewOrientation3D</span><span> viewOrientation3D </span><span>=</span><span> </span><span>new</span><span> </span><span>ViewOrientation3D</span><span>(</span><span>eye</span><span>,</span><span> up</span><span>,</span><span> forward</span><span>);</span><span>
        view3D</span><span>.</span><span>SetOrientation</span><span>(</span><span>viewOrientation3D</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### **Switching between isometric and perspective**

Most of the time a View3D can be toggled between Isometric and Perspective, provided that there are no view-specific elements in the view. The View3D class provides methods for toggling the view to and from Isometric and Perspective mode. Before toggling, use the CanToggleBetweenPerspectiveAndIsometric() method which indicates whether toggling is ok.

To toggle the view call one of the two View3D class methods: ToggleToPerspective() or ToggleToIsometric(). In the case that the view cannot be toggled (perhaps due to the presence of view specific elements in the view) either of these methods will throw Autodesk.Revit.Exceptions.InvalidOperationException.

### 3D Views SectionBox

Each view has a crop box. The crop box focuses on a portion of the model to project and show in the view. For 3D views, there is another box named section box.

-   The section box determines which model portion appears in a 3D view.
-   The section box is used to clip the 3D model's visible portion.
-   The part outside the box is invisible even if it is in the crop box.
-   The section box is different from the crop box in that it can be rotated and moved with the model.

The section box is particularly useful for large models. For example, if you want to render a large building, use a section box. The section box limits the model portion used for calculation. To display the section box, in the 3D view Element Properties dialog box, select Section Box in the Extents section. You can also set it using the IsSectionBoxActive property. In the example below, if the active view is a 3D view, it sets whether the section box is active.

<table summary="" id="GUID-A7FA8DBC-830E-482D-9B66-147399524442__TABLE_6A5B9A2A9AF540C09BB6F98B19FBBFA9"><tbody><tr><td><b>Code Region: Showing/Hiding the Section Box</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ShowHideSectionBox</span><span>(</span><span>UIDocument</span><span> document</span><span>,</span><span> </span><span>bool</span><span> active</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(</span><span>document</span><span>.</span><span>ActiveView</span><span> </span><span>is</span><span> </span><span>View3D</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>View3D</span><span> view3d </span><span>=</span><span> document</span><span>.</span><span>ActiveView</span><span> </span><span>as</span><span> </span><span>View3D</span><span>;</span><span>
        view3d</span><span>.</span><span>IsSectionBoxActive</span><span> </span><span>=</span><span> active</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-016E48BA-138E-4686-B864-D4A978DC406C-low.png)**Figure 100: Section box**

The View3D.GetSectionBox() and View3D.SetSectionBox() methods are used to get and change the box extents. In some cases, calling View3D.SetSectionBox() can have a side effect. Setting the property to certain values can change the box capacity and display it in the view. To avoid displaying the section box, set the IsSectionBoxActive property to false.

The following code sample illustrates how to change the extents of the section box.

<table summary="" id="GUID-A7FA8DBC-830E-482D-9B66-147399524442__TABLE_09F636AB451849709EE1780DB34758D5"><tbody><tr><td><b>Code Region: Changing the extents of the section box</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ExpandSectionBox</span><span>(</span><span>View3D</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// The original section box</span><span>
    </span><span>BoundingBoxXYZ</span><span> sectionBox </span><span>=</span><span> view</span><span>.</span><span>GetSectionBox</span><span>();</span><span>

    </span><span>// Expand the section box (doubling in size in all directions while preserving the same center and orientation)</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>XYZ deltaXYZ </span><span>=</span><span> sectionBox</span><span>.</span><span>Max</span><span> </span><span>-</span><span> sectionBox</span><span>.</span><span>Min</span><span>;</span><span>
    sectionBox</span><span>.</span><span>Max</span><span> </span><span>+=</span><span> deltaXYZ </span><span>/</span><span> </span><span>2</span><span>;</span><span>
    sectionBox</span><span>.</span><span>Min</span><span> </span><span>-=</span><span> deltaXYZ </span><span>/</span><span> </span><span>2</span><span>;</span><span>

    </span><span>//After resetting the section box, it will be shown in the view.</span><span>
    </span><span>//It only works when the Section Box is active</span><span>
    view</span><span>.</span><span>SetSectionBox</span><span>(</span><span>sectionBox</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The coordinates of Max and Min points of BoundingBoxXYZ returned from the GetSectionBox() method are not in global coordinates. To convert the coordinates of Max and Min to global coordinates, you need to convert each point via the transform obtained from BoundingBoxXYZ.Transform property.

<table summary="" id="GUID-A7FA8DBC-830E-482D-9B66-147399524442__TABLE_B392BA0ED1584FFA80F3FBAD71070C28"><tbody><tr><td><b>Code Region: Convert Max and Min to global coordinates</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ConvertMaxMinToGlobal</span><span>(</span><span>View3D</span><span> view</span><span>,</span><span> </span><span>out</span><span> XYZ max</span><span>,</span><span> </span><span>out</span><span> XYZ min</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>BoundingBoxXYZ</span><span> sectionbox </span><span>=</span><span> view</span><span>.</span><span>GetSectionBox</span><span>();</span><span>
    </span><span>Transform</span><span> transform </span><span>=</span><span> sectionbox</span><span>.</span><span>Transform</span><span>;</span><span>
    max </span><span>=</span><span> transform</span><span>.</span><span>OfPoint</span><span>(</span><span>sectionbox</span><span>.</span><span>Max</span><span>);</span><span>
    min </span><span>=</span><span> transform</span><span>.</span><span>OfPoint</span><span>(</span><span>sectionbox</span><span>.</span><span>Min</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

#### View locking

The View3D class has methods and properties corresponding to the locking feature available in the Revit user interface.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/3DLocking.jpg) The View3D.SaveOrientationAndLock() method will save the orientation and lock the view while View3D.RestoreOrientationAndLock() will restore the view's orientation and lock it. View3D.Unlock() will unlock the view if it is currently locked. The IsLocked property will return whether the 3D view is currently locked.

#### Grid Visibility

Grid visiility in 3D Views can be accessed with:

-   View3D.GetLevelsThatShowGrids()
-   View3D.ShowGridsOnLevel(ElementId levelId)
-   View3D.HideGridsOnLevel(ElementId levelId)
-   View3D.ShowGridsOnLevels(ElementIdset levelIds)
