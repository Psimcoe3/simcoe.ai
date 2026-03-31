---
created: 2026-01-28T21:19:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Point_Clouds_Point_Cloud_Client_html
author: 
---

# Help | Point Cloud Client | Autodesk

> ## Excerpt
> The point cloud client API supports read and modification of point cloud instances within Revit.

---
The point cloud client API supports read and modification of point cloud instances within Revit.

The points supplied by the point cloud instances come from the point cloud engine, which is either a built-in engine within Revit, or [a third party engine loaded as an application](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Point_Clouds_Point_Cloud_Engine_html). A client point cloud API application doesn’t need to be concerned with the details of how the engine stores and serves points to Revit. Instead, the client API can be used to create point clouds, manipulate their properties, and read the points found matching a given filter.

The main classes related to point clouds are:

-   **PointCloudType** - type of point cloud loaded into a Revit document. Each PointCloudType maps to a single file or identifier (depending upon the type of Point Cloud Engine which governs it).
-   **PointCloudInstance** - an instance of a point cloud in a location in the Revit project.
-   **PointCloudFilter** - a filter determining the volume of interest when extracting points.
-   **PointCollection** - a collection of points obtained from an instance and a filter.
-   **PointIterator** - an iterator for the points in a PointCollection.
-   **CloudPoint** - an individual point cloud point, representing an X, Y, Z location in the coordinates of the cloud, and a color.
-   **PointCloudOverrides** - and its related settings classes specify graphic overrides that are stored by a view to be applied to a PointCloudInstance element, or a scan within the element.

### Point cloud file paths

Two important path locations dealing with point clouds are available as read-only data:

1.  PointCloudType.GetPath() - The path of the link source from which the points are loaded
2.  Application.PointCloudsRootPath - The root path for point cloud files which is used by Revit to calculate relative paths to point cloud files

### Creating a Point Cloud

To create a new point cloud in a Revit document, create a PointCloudType and then use it to create a PointCloudInstance. The static PointCloudType.Create() method requires the engine identifier, as it was registered with Revit by a third party, or the file extension of the point cloud file, if it is a supported file type. It also requires a file name or the identification string for a non-file based engine. In the following sample, a pcg file is used to create a point cloud in a Revit document.

<table summary="" id="GUID-B80DBCF1-56A8-4864-A0CD-181466E0EDE8__TABLE_DB4694291F3E4A2C870574D205436A48"><tbody><tr><td><b>Code Region: Create a point cloud from an rcs file</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>PointCloudInstance</span><span> </span><span>CreatePointCloud</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>PointCloudType</span><span> type </span><span>=</span><span> </span><span>PointCloudType</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"rcs"</span><span>,</span><span> </span><span>"c:\\32_cafeteria.rcs"</span><span>);</span><span>
    </span><span>return</span><span> </span><span>(</span><span>PointCloudInstance</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> type</span><span>.</span><span>Id</span><span>,</span><span> </span><span>Transform</span><span>.</span><span>Identity</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/PointCloudInstance.png)

**Figure: Point Cloud from 32\_cafeteria.rcs**

### Accessing Points in a Point Cloud

There are two ways to access the points in a point cloud:

1.  Iterate the resulting points directly from the PointCollection return using the `IEnumerable<CloudPoint>` interface
2.  Get a pointer to the point storage of the collection and access the points directly in memory in an unsafe interface

Either way, the first step to access a collection of points from the PointCloudInstance is to use the method

-   PointCloudInstance.GetPoints(PointCloudFilter filter, double averageDistance, int numPoints)

Note that as a result of search algorithms used by Revit and the point cloud engine, the exact requested number of points may not be returned.

Although the second option involves dealing with pointers directly, there may be performance improvements when traversing large buffers of points. However, this option is only possible from C# and C++/CLI.

The following two examples show how to iterate part of a point cloud using on one of these two methods.

<table summary="" id="GUID-B80DBCF1-56A8-4864-A0CD-181466E0EDE8__TABLE_386801A0786842078EFB34D4B4DCAA7F"><tbody><tr><td><b>Code Region: Reading point cloud points by iteration</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetPointCloudDataByIteration</span><span>(</span><span>PointCloudInstance</span><span> pcInstance</span><span>,</span><span> </span><span>PointCloudFilter</span><span> pointCloudFilter</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// read points by iteration</span><span>
    </span><span>double</span><span> averageDistance </span><span>=</span><span> </span><span>0.001</span><span>;</span><span>
    </span><span>PointCollection</span><span> points </span><span>=</span><span> pcInstance</span><span>.</span><span>GetPoints</span><span>(</span><span>pointCloudFilter</span><span>,</span><span> averageDistance</span><span>,</span><span> </span><span>10000</span><span>);</span><span> </span><span>// Get points.  Number of points is determined by the needs of the client</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>CloudPoint</span><span> point </span><span>in</span><span> points</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Process each point</span><span>
        </span><span>System</span><span>.</span><span>Drawing</span><span>.</span><span>Color</span><span> color </span><span>=</span><span> </span><span>System</span><span>.</span><span>Drawing</span><span>.</span><span>ColorTranslator</span><span>.</span><span>FromWin32</span><span>(</span><span>point</span><span>.</span><span>Color</span><span>);</span><span>
        </span><span>String</span><span> pointDescription </span><span>=</span><span> </span><span>String</span><span>.</span><span>Format</span><span>(</span><span>"({0}, {1}, {2}, {3}"</span><span>,</span><span> point</span><span>.</span><span>X</span><span>,</span><span> point</span><span>.</span><span>Y</span><span>,</span><span> point</span><span>.</span><span>Z</span><span>,</span><span> color</span><span>.</span><span>ToString</span><span>());</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

<table summary="" id="GUID-B80DBCF1-56A8-4864-A0CD-181466E0EDE8__TABLE_72DCC06A0A54449CBFBFCD95C5F54FC0"><tbody><tr><td><b>Code Region: Reading point cloud points by pointer</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>unsafe</span><span> </span><span>void</span><span> </span><span>GetPointCloudDataByPointer</span><span>(</span><span>PointCloudInstance</span><span> pcInstance</span><span>,</span><span> </span><span>PointCloudFilter</span><span> pointCloudFilter</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>double</span><span> averageDistance </span><span>=</span><span> </span><span>0.001</span><span>;</span><span>
    </span><span>PointCollection</span><span> points </span><span>=</span><span> pcInstance</span><span>.</span><span>GetPoints</span><span>(</span><span>pointCloudFilter</span><span>,</span><span> averageDistance</span><span>,</span><span> </span><span>10000</span><span>);</span><span>
    </span><span>CloudPoint</span><span>*</span><span> pointBuffer </span><span>=</span><span> </span><span>(</span><span>CloudPoint</span><span>*)</span><span>points</span><span>.</span><span>GetPointBufferPointer</span><span>().</span><span>ToPointer</span><span>();</span><span>
    </span><span>int</span><span> totalCount </span><span>=</span><span> points</span><span>.</span><span>Count</span><span>;</span><span>
    </span><span>for</span><span> </span><span>(</span><span>int</span><span> numberOfPoints </span><span>=</span><span> </span><span>0</span><span>;</span><span> numberOfPoints </span><span>&lt;</span><span> totalCount</span><span>;</span><span> numberOfPoints</span><span>++)</span><span>
    </span><span>{</span><span>
        </span><span>CloudPoint</span><span> point </span><span>=</span><span> </span><span>*(</span><span>pointBuffer </span><span>+</span><span> numberOfPoints</span><span>);</span><span>
        </span><span>// Process each point</span><span>
        </span><span>System</span><span>.</span><span>Drawing</span><span>.</span><span>Color</span><span> color </span><span>=</span><span> </span><span>System</span><span>.</span><span>Drawing</span><span>.</span><span>ColorTranslator</span><span>.</span><span>FromWin32</span><span>(</span><span>point</span><span>.</span><span>Color</span><span>);</span><span>
        </span><span>String</span><span> pointDescription </span><span>=</span><span> </span><span>String</span><span>.</span><span>Format</span><span>(</span><span>"({0}, {1}, {2}, {3}"</span><span>,</span><span> point</span><span>.</span><span>X</span><span>,</span><span> point</span><span>.</span><span>Y</span><span>,</span><span> point</span><span>.</span><span>Z</span><span>,</span><span> color</span><span>.</span><span>ToString</span><span>());</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Filters

Filters are used both to limit the volume which is searched when reading points, and also to govern the display of point clouds. A PointCloudFilter can be created based upon a collection of planar boundaries. The filter will check whether a point is located on the “positive” side of each input plane, as indicated by the positive direction of the plane normal. Therefore, such filter implicitly defines a volume, which is the intersection of the positive half-spaces corresponding to all the planes. This volume does not have to be closed, but it will always be convex.

The display of point clouds can be controlled by assigning a filter to:

-   PointCloudInstance.SetSelectionFilter()

Display of the filtered points will be based on the value of the property:

-   PointCloudInstance.FilterAction

If it is set to None, the selection filter is ignored. If it is set to Highlight, points that pass the filter are highlighted. If it is set to Isolate, only points that pass the filter will be visible.

The following example will highlight a subset of the points in a point cloud based on its bounding box.

<table summary="" id="GUID-B80DBCF1-56A8-4864-A0CD-181466E0EDE8__TABLE_E6BC7B0EA75A43AC9E567DD0EF1C5F08"><tbody><tr><td><b>Code Region: Reading point cloud points by pointer</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>PointCloudFilter</span><span> </span><span>ReadPointCloud</span><span>(</span><span>PointCloudInstance</span><span> pointCloudInstance</span><span>)</span><span>
</span><span>{</span><span>
 </span><span>// Filter will match 1/8 of the overall point cloud</span><span>
 </span><span>// Use the bounding box (filter coordinates are in the coordinates of the model)</span><span>
 </span><span>BoundingBoxXYZ</span><span> boundingBox </span><span>=</span><span> pointCloudInstance</span><span>.</span><span>get_BoundingBox</span><span>(</span><span>null</span><span>);</span><span>
 </span><span>List</span><span>&lt;</span><span>Plane</span><span>&gt;</span><span> planes </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Plane</span><span>&gt;();</span><span>
 XYZ midpoint </span><span>=</span><span> </span><span>(</span><span>boundingBox</span><span>.</span><span>Min</span><span> </span><span>+</span><span> boundingBox</span><span>.</span><span>Max</span><span>)</span><span> </span><span>/</span><span> </span><span>2.0</span><span>;</span><span>

 </span><span>// X boundaries</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> boundingBox</span><span>.</span><span>Min</span><span>));</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(-</span><span>XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> midpoint</span><span>));</span><span>

 </span><span>// Y boundaries</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>XYZ</span><span>.</span><span>BasisY</span><span>,</span><span> boundingBox</span><span>.</span><span>Min</span><span>));</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(-</span><span>XYZ</span><span>.</span><span>BasisY</span><span>,</span><span> midpoint</span><span>));</span><span>

 </span><span>// Z boundaries</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>XYZ</span><span>.</span><span>BasisZ</span><span>,</span><span> boundingBox</span><span>.</span><span>Min</span><span>));</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(-</span><span>XYZ</span><span>.</span><span>BasisZ</span><span>,</span><span> midpoint</span><span>));</span><span>

 </span><span>// Create filter</span><span>
 </span><span>PointCloudFilter</span><span> filter </span><span>=</span><span> </span><span>PointCloudFilterFactory</span><span>.</span><span>CreateMultiPlaneFilter</span><span>(</span><span>planes</span><span>);</span><span>
 pointCloudInstance</span><span>.</span><span>FilterAction</span><span> </span><span>=</span><span> </span><span>SelectionFilterAction</span><span>.</span><span>Highlight</span><span>;</span><span>

 </span><span>return</span><span> filter</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

This is the result when the sample above is run on a small pipe point cloud:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/PointCloudHighlight.jpg)**Figure: Point cloud with selection filter**

The Selection.PickBox() method which invokes a general purpose two-click editor that lets the user to specify a rectangular area on the screen can be used in conjunction with a PointCloudFilter by using the resulting PickedBox to generate the planar boundaries of the filter.

### Scans

An .rcp file can contain multiple scans. The method PointCloudInstance.GetScans() returns a list of scan names which can be used to set visibility and fixed color overrides independently for each scan in the PointCloudInstance. PointCloudInstance.ContainsScan() indicates whether the given scan name is contained in the point cloud instance while PointCloudInstance.GetScanOrigin() will return the origin of the given scan in model coordinates.

### Regions

Scan regions are specific to Autodesk ReCap™. If a point cloud was created in ReCap, it may have regions. PointCloudInstance.GetRegions() returns a list of region names which can be used to set visibility and fixed color overrides independently for each region in the PointCloudInstance.

`PointCloudType.GetReCapProject()` provides a direct entry point to get access to an object from the ReCap SDK (`ReCapWrapper.RCProject`) from Revit. This object represents the point cloud from the RC file path stored in `PointCloudType`. The ReCap assembly ReCapWrapper.dll will need to be included into code using this method. The coordinate system in RCProject is defined by the Point Cloud. Please refer to ReCap SDK documentation for `RCProject.getCoordinateSystem()`. If you need points converted to the modeling coordinate system in Revit, you can obtain the transformation matrix from `PointCloudInstance.GetTransform()`.

### Overrides

Point cloud override settings assigned to a given view can be modified using the Revit API. These settings correspond to the settings on the Point Clouds tab of the Visibility/Graphics Overrides task pane in the Revit UI. Overrides can be applied to an entire point cloud instance, or to specific scans within that instance. Options for the overrides include setting visibility for scans in the point cloud instance, setting it to a fixed color, or to color gradients based on elevation, normals, or intensity. The property PointCloudInstance.SupportsOverrides identifies point clouds which support override settings (clouds which are based on .rcp or .rcs files).

The following classes are involved in setting the overrides for point clouds:

-   **PointCloudOverrides** - Used to get or set the PointCloudOverrideSettings for a PointCloudInstance, one of its scans, or for a particular region within the PointCloudInstance.
-   **PointCloudOverrideSettings** - Used to get or set the visibility, color mode, and PointCloudColorSettings.
-   **PointCloudColorSettings** - Used to assign specific colors for certain color modes to a PointCloudInstance element, or one of its scans. Does not apply if the PointCloudColorMode is NoOverride or Normals.
