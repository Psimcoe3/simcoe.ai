---
created: 2026-01-28T21:03:28 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_3D_Sketch_html
author: 
---

# Help | 3D Sketch | Autodesk

> ## Excerpt
> 3D Sketch is used to edit a family or create a 3D object. In the Revit Platform API, you can complete the 3D Sketch using the following classes.

---
3D Sketch is used to edit a family or create a 3D object. In the Revit Platform API, you can complete the 3D Sketch using the following classes.

-   Extrusion
-   Revolution
-   Blend
-   Sweep

In other words, there are four operations through which a 2D model turns into a 3D model. For more details about sketching in 2D, refer to [The 2D Sketch Class](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_The_2D_Sketch_Class_html).

## Extrusion

Revit uses extrusions to define 3D geometry for families. You create an extrusion by defining a 2D sketch on a plane; Revit then extrudes the sketch between a start and an end point.

Query the Extrusion Form object for a generic form to use in family modeling and massing. The Extrusion class has the following properties:

**Table 40: Extrusion Properties**

<table summary="" id="GUID-F689E2FE-9527-4F43-80D3-5D698C60FDAA__TABLE_929F191532B5417F961889012940AD7C"><tbody><tr><td><b>Property</b></td><td><b>Description</b></td></tr><tr><td>ExtrusionStart</td><td>Returns the Extrusion Start point. It is a Double type.</td></tr><tr><td>ExtrusionEnd</td><td>Returns the Extrusion End point. It is a Double type.</td></tr><tr><td>Sketch</td><td>Returns the Extrusion Sketch. It contains a sketch plane and some curves.</td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-8F322D1A-5035-4E9E-88F6-2AFAD258E59E-low.png)**Figure 81: Extrusion result**

## Revolution

The Revolve command creates geometry that revolves around an axis. You can use the revolve command to create door knobs or other knobs on furniture, a dome roof, or columns.

Query the Revolution Form object for a generic form to use in family modeling and massing. The Revolution class has the following properties:

**Table 41: Revolution Properties**

<table summary="" id="GUID-F689E2FE-9527-4F43-80D3-5D698C60FDAA__TABLE_95839C754E6E4BFFA4BDF5BC23791566"><tbody><tr><td><b>Property</b></td><td><b>Description</b></td></tr><tr><td>Axis</td><td>Returns the Axis. It is a ModelLine object.</td></tr><tr><td>EndAngle</td><td>Returns the End Angle. It is a Double type.</td></tr><tr><td>Sketch</td><td>Returns the Extrusion Sketch. It contains a SketchPlane and some curves.</td></tr></tbody></table>

EndAngle is consistent with the same parameter in the Revit UI. The following pictures illustrate the Revolution corresponding parameter, the sketch, and the result.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-2CF60823-4258-4838-ADA8-61F52C4B3515-low.png)**Figure 82: Corresponding parameter**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-10A03254-96BC-4023-99C5-B22AF43A0702-low.png)**Figure 83: Revolution sketch**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-803C819E-E85C-462B-BF33-CC49E9FC3C86-low.png)**Figure 84: Revolution result**

Note:

-   The Start Angle is not accessible using the Revit Platform API.
-   If the End Angle is positive, the Rotation direction is clockwise. If it is negative, the Rotation direction is counterclockwise

## Blend

The Blend command blends two profiles together. For example, if you sketch a large rectangle and a smaller rectangle on top of it, Revit blends the two shapes together.

Query the Blend Form object for a generic form to use in family modeling and massing. The Blend class has the following properties:

**Table 42: Blend Properties**

<table summary="" id="GUID-F689E2FE-9527-4F43-80D3-5D698C60FDAA__TABLE_B61C260FD3084F47AAAC96D0786FF74A"><tbody><tr><td><b>Property</b></td><td><b>Description</b></td></tr><tr><td>BottomSketch</td><td>Returns the Bottom Sketch. It is a Sketch object.</td></tr><tr><td>TopSketch</td><td>Returns the Top Sketch Blend. It is a Sketch object.</td></tr><tr><td>FirstEnd</td><td>Returns the First End. It is a Double type.</td></tr><tr><td>SecondEnd</td><td>Returns the Second End. It is a Double type.</td></tr></tbody></table>

The FirstEnd and SecondEnd property values are consistent with the same parameters in the Revit UI. The following pictures illustrate the Blend corresponding parameters, the sketches, and the result.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-BF73A304-626D-43C2-9A53-8C396270369F-low.png)**Figure 85: Blend parameters in the UI**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-14B5134B-B412-429C-8CBF-A542C16659C0-low.png)**Figure 86: Blend top sketch and bottom sketch**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F637CA72-BA0E-4917-B24D-93947FD69E22-low.png)**Figure 87: Blend result**

## Sweep

The Sweep command sweeps one profile along a created 2D path or selected 3D path. The path may be an open or closed loop, but must pierce the profile plane.

Query the Sweep Form object for a generic form for use in family modeling and massing. The Sweep class has the following properties:

**Table 43: Sweep Properties**

<table summary="" id="GUID-F689E2FE-9527-4F43-80D3-5D698C60FDAA__TABLE_BBD64F51598040BCA47FBADD20FBC654"><tbody><tr><td><b>Property</b></td><td><b>Description</b></td></tr><tr><td>Path3d</td><td>Returns the 3D Path Sketch. It is a Path3D object.</td></tr><tr><td>PathSketch</td><td>Returns the Plan Path Sketch. It is a Sketch object.</td></tr><tr><td>ProfileSketch</td><td>Returns the profile Sketch. It is a Sketch object.</td></tr><tr><td>EnableTrajSegmentation</td><td>Returns the Trajectory Segmentation state. It is a Boolean.</td></tr><tr><td>MaxSegmentAngle</td><td>Returns the Maximum Segment Angle. It is a Double type.</td></tr></tbody></table>

Creating a 2D Path is similar to other forms. The 3D Path is fetched by picking the created 3D curves.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-C9B66D17-E7EF-4CE4-B186-E1862B49461D-low.png)**Figure 88: Pick the Sweep 3D path**

Note: The following information applies to Sweep:

-   The Path3d property is available only when you use Pick Path to get the 3D path.
-   PathSketch is available whether the path is 3D or 2D.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4E2B269D-16CC-417E-A4BF-EBAD946C73DC-low.png)**Figure 89: Sweep profile sketch**

Note: The ProfileSketch is perpendicular to the path.

Segmented sweeps are useful for creating mechanical duct work elbows. Create a segmented sweep by setting two sweep parameters and sketching a path with arcs.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-B63CD7A5-25B1-440A-A31B-AB6FADF08169-low.png)**Figure 90: Corresponding segment settings in the UI**

Note: The following information applies to segmented Sweeps:

-   The parameters affect only arcs in the path.
-   The minimum number of segments for a sweep is two.
-   Change a segmented sweep to a non-segmented sweep by clearing the Trajectory Segmentation check box. The EnableTrajSegmentation property returns false.
-   If the EnableTrajSegmentation property is false, the value of MaxSegmentAngle is the default 360°.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-2AACA3CE-F284-4412-9887-B84FB87CC6BA-low.png)**Figure 91: Sweep result**
