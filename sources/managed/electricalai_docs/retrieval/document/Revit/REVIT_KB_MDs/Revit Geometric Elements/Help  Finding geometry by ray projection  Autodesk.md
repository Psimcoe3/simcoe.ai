---
created: 2026-01-28T21:03:06 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Finding_geometry_by_ray_projection_html
author: 
---

# Help | Finding geometry by ray projection | Autodesk

> ## Excerpt
> The ReferenceIntersector class can be used to find elements that are intersected by a given ray.

---
The ReferenceIntersector class can be used to find elements that are intersected by a given ray.

## ReferenceIntersector

This class allows an application to use Revit's picking tools to find elements and geometry. This class uses a ray from a point in a specified direction to find the geometry that is hit by the ray.

The class intersects 3D geometry only and requires a 3D view on creation. It is possible to use a 3D view which has been cut by a section box, or which has view-specific geometry and graphics options set. The visibility settings on the input view will determine if a particular element is returned (for example, hidden elements will never be returned by this tool, nor will elements whose geometry is outside the section box of the view).

The ReferenceIntersector class supports filtering the output based on element or reference type. The output can be customized based on which constructor is used or by using methods and properties of the class prior to calling a method to perform the ray projection.

There are 4 constructors.

|  |  |
| --- | --- |
| Name | Description |
| `ReferenceIntersector(View3D)` | Constructs a ReferenceIntersector which is set to return intersections from all elements and representing all reference target types. |
| `ReferenceIntersector(ElementFilter, FindReferenceTarget, View3D)` | Constructs a ReferenceIntersector which is set to return intersections from any element which passes the filter. |
| `ReferenceIntersector(ElementId, FindReferenceTarget, View3D)` | Constructs a ReferenceIntersector which is set to return intersections from a single target element only. |
| `ReferenceIntersector(ICollection<ElementId>, FindReferenceTarget, View3D)` | Constructs a ReferenceIntersector which is set to return intersections from any of a set of target elements. |

The FindReferenceTarget enumeration includes the options: Element, Mesh, Edge, Curve, Face or All.

### Finding elements

There are two methods to project a ray, both of which take as input the origin of the ray and its direction. Only references for elements that are in front of the ray will be returned. The Find() method returns a collection of ReferenceWithContext objects which match the ReferenceIntersector's criteria. This object contains the intersected reference, which can be both the elements and geometric references which intersect the ray. Some element references returned will have a corresponding geometric object which is also intersected (for example, rays passing through openings in walls will intersect the wall and the opening element). If interested only in true physical intersections an application should discard all references whose Reference is of type Element.

The FindNearest() method behaves similarly to the Find() method, but only returns the intersected reference nearest to the ray origin.

The ReferenceWithContext returned includes a proximity parameter. This is the distance between the origin of the ray and the intersection point. An application can use this distance to exclude items too far from the origin for a particular geometric analysis. An application can also use this distance to take on some interesting problems involving analyzing the in place geometry of the model.

Note: These methods will not return intersections with elements which are not in the active design option.

#### Elements in linked files

The FindReferencesInRevitLinks property offers an option to return element results encountered in Revit Links. If set to false, no Reference to any Element from a Revit Link will be found by the ReferenceIntersector, and all References returned will be to an element in the host document only. If set to true, the results may include both References to Elements in hosts and References to Elements from a link instance.

If a list of target ElementIds is set in the ReferenceIntersector, references will be returned only if the ElementId matches the id of the intersected RevitLinkInstance. If there is a match, any intersecting elements in the link will be returned (their ids will not be compared with the target ids list).

If there is an ElementFilter applied, the elements in the link will be evaluated against the stored ElementFilter. Note that results may not be as expected if the filter applied is geometric (such as a BoundingBox filter or ElementIntersects filter). This is because the filter will be evaluated for linked elements in the coordinates of the linked model, which may not match the coordinates of the elements as they appear in the host model. Also, ElementFilters that accept a Document and/or ElementId as input during their instantiation will not correctly pass elements that appear in the link, because the filter will not be able to match link elements to the filter's criteria.

### Find elements near elements

One major use for this tool is to find elements in close proximity to other elements. This allows an application to use the tool as its "eyes" and determine relationships between elements which don't have a built-in relationship already.

For example, the ray-tracing capability can be used to find columns embedded in walls. As columns and walls don't maintain a relationship directly, this class allows us to find potential candidates by tracing rays just outside the extents of the wall, and looking for intersections with columns.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/find_refs_1.png)

**Example: Find columns embedded in walls**

### Measure distances

This class could also be used to measure the vertical distance from a skylight to the nearest floor.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/DistanceToFloor.jpg)

**Example: measure with ReferenceIntersector.FindNearest()**

<table summary="" id="GUID-B3EE488D-2287-49A2-A772-C7164B84A648__TABLE_80A6EAC1CDED452AA6744F03F90081B4"><tbody><tr><td><b>Code Region: Measuring Distance using Ray Projection</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>RayProjection</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
    </span><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> revit</span><span>,</span><span> </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Document</span><span> doc </span><span>=</span><span> revit</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>

        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> revit</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

        </span><span>// If skylight is selected, process it.</span><span>
        </span><span>FamilyInstance</span><span> skylight </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>selectedIds</span><span>.</span><span>Count</span><span> </span><span>==</span><span> </span><span>1</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>Element</span><span> e </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
                </span><span>if</span><span> </span><span>(</span><span>e </span><span>is</span><span> </span><span>FamilyInstance</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>FamilyInstance</span><span> instance </span><span>=</span><span> e </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
                    </span><span>bool</span><span> isWindow </span><span>=</span><span> </span><span>(</span><span>instance</span><span>.</span><span>Category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span> </span><span>==</span><span> </span><span>(</span><span>int</span><span>)</span><span>BuiltInCategory</span><span>.</span><span>OST_Windows</span><span>);</span><span>
                    </span><span>bool</span><span> isHostedByRoof </span><span>=</span><span> </span><span>(</span><span>instance</span><span>.</span><span>Host</span><span>.</span><span>Category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span> </span><span>==</span><span> </span><span>(</span><span>int</span><span>)</span><span>BuiltInCategory</span><span>.</span><span>OST_Roofs</span><span>);</span><span>

                    </span><span>if</span><span> </span><span>(</span><span>isWindow </span><span>&amp;&amp;</span><span> isHostedByRoof</span><span>)</span><span>
                    </span><span>{</span><span>
                        skylight </span><span>=</span><span> instance</span><span>;</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>if</span><span> </span><span>(</span><span>skylight </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            message </span><span>=</span><span> </span><span>"Please select one skylight."</span><span>;</span><span>
            </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Cancelled</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>// Calculate the height</span><span>
        </span><span>Line</span><span> line </span><span>=</span><span> </span><span>CalculateLineAboveFloor</span><span>(</span><span>doc</span><span>,</span><span> skylight</span><span>);</span><span>

        </span><span>// Create a model curve to show the distance</span><span>
        </span><span>Plane</span><span> plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>),</span><span> line</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>));</span><span>
        </span><span>SketchPlane</span><span> sketchPlane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> plane</span><span>);</span><span>

        </span><span>ModelCurve</span><span> curve </span><span>=</span><span> doc</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>line</span><span>,</span><span> sketchPlane</span><span>);</span><span>

        </span><span>// Show a message with the length value</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Distance"</span><span>,</span><span> </span><span>"Distance to floor: "</span><span> </span><span>+</span><span> </span><span>String</span><span>.</span><span>Format</span><span>(</span><span>"{0:f2}"</span><span>,</span><span> line</span><span>.</span><span>Length</span><span>));</span><span>

        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Determines the line segment that connects the skylight to the nearest floor.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;returns&gt;The line segment.&lt;/returns&gt;</span><span>
    </span><span>private</span><span> </span><span>Line</span><span> </span><span>CalculateLineAboveFloor</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>FamilyInstance</span><span> skylight</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Find a 3D view to use for the ReferenceIntersector constructor</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
        </span><span>Func</span><span>&lt;</span><span>View3D</span><span>,</span><span> </span><span>bool</span><span>&gt;</span><span> isNotTemplate </span><span>=</span><span> v3 </span><span>=&gt;</span><span> </span><span>!(</span><span>v3</span><span>.</span><span>IsTemplate</span><span>);</span><span>
        </span><span>View3D</span><span> view3D </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>View3D</span><span>)).</span><span>Cast</span><span>&lt;</span><span>View3D</span><span>&gt;().</span><span>First</span><span>&lt;</span><span>View3D</span><span>&gt;(</span><span>isNotTemplate</span><span>);</span><span>

        </span><span>// Use the center of the skylight bounding box as the start point.</span><span>
        </span><span>BoundingBoxXYZ</span><span> box </span><span>=</span><span> skylight</span><span>.</span><span>get_BoundingBox</span><span>(</span><span>view3D</span><span>);</span><span>
        XYZ center </span><span>=</span><span> box</span><span>.</span><span>Min</span><span>.</span><span>Add</span><span>(</span><span>box</span><span>.</span><span>Max</span><span>).</span><span>Multiply</span><span>(</span><span>0.5</span><span>);</span><span>

        </span><span>// Project in the negative Z direction down to the floor.</span><span>
        XYZ rayDirection </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>-</span><span>1</span><span>);</span><span>

        </span><span>ElementClassFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>Floor</span><span>));</span><span>

        </span><span>ReferenceIntersector</span><span> refIntersector </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceIntersector</span><span>(</span><span>filter</span><span>,</span><span> </span><span>FindReferenceTarget</span><span>.</span><span>Face</span><span>,</span><span> view3D</span><span>);</span><span>
        </span><span>ReferenceWithContext</span><span> referenceWithContext </span><span>=</span><span> refIntersector</span><span>.</span><span>FindNearest</span><span>(</span><span>center</span><span>,</span><span> rayDirection</span><span>);</span><span>

        </span><span>Reference</span><span> reference </span><span>=</span><span> referenceWithContext</span><span>.</span><span>GetReference</span><span>();</span><span>
        XYZ intersection </span><span>=</span><span> reference</span><span>.</span><span>GlobalPoint</span><span>;</span><span>

        </span><span>// Create line segment from the start point and intersection point.</span><span>
        </span><span>Line</span><span> result </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>center</span><span>,</span><span> intersection</span><span>);</span><span>
        </span><span>return</span><span> result</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Ray bouncing/analysis

The references returned by ReferenceIntersector.Find() include the intersection point on the geometry. Knowing the intersection point on the face, the face's material, and the ray direction allows an application to analyze reflection and refraction within the building. The following image demonstrates the use of the intersection point to reflect rays intersected by model elements; model curves were added to represent the path of each ray.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/find_refs_3.png)**Example: Rays bouncing off intersected faces**

### Find intersections/collisions

Another use of the ReferenceIntersector class would be to detect intersections (such as beams or pipes) which intersect/interference with the centerline of a given beam or pipe.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/find_refs_4.png)

**Example: Reroute elements around interferences**
