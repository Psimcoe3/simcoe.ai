


<!-- ===== BEGIN: Help  Revit Geometric Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:58:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Revit Geometric Elements | Autodesk

> ## Excerpt
> 

---
### Was this information helpful?

-   Yes
-   No


<!-- ===== END: Help  Revit Geometric Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Walls, Floors, Ceilings, Roofs and Openings  Autodesk.md ===== -->

---
created: 2026-01-28T21:04:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html
author: 
---

# Help | Walls, Floors, Ceilings, Roofs and Openings | Autodesk

> ## Excerpt
> Elements and the corresponding ElementTypes representing built-in place construction.

---
Elements and the corresponding ElementTypes representing built-in place construction.

The following sections cover the classes associated with built-in place construction such as walls, floors, ceilings, roofs and openings and their corresponding properties.

**Pages in this section**

-   [Walls](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Walls_html)
-   [Floors, Ceilings and Foundations](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Floors_Ceilings_and_Foundations_html)
-   [Roofs](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Roofs_html)
-   [Curtains](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Curtains_html)
-   [Other Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Other_Elements_html)
-   [CompoundStructure](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_CompoundStructure_html)
-   [Opening](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Opening_html)
-   [Thermal Properties](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Thermal_Properties_html)

**Parent page:** [Revit Geometric Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_html)


<!-- ===== END: Help  Walls, Floors, Ceilings, Roofs and Openings  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Walls  Autodesk.md ===== -->

---
created: 2026-01-28T21:04:46 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Walls_html
author: 
---

# Help | Walls | Autodesk

> ## Excerpt
> There are four kinds of Walls represented by the WallType.WallKind enumeration:

---
There are four kinds of Walls represented by the WallType.WallKind enumeration:

-   Stacked
-   Curtain
-   Basic
-   Unknown

The Wall and WallType class work with the Basic wall type while providing limited function to the Stacked and Curtain walls. On occasion you need to check a Wall to determine the wall type. For example, you cannot get sub-walls from a Stacked Wall using the API. WallKind is read only and set by System Family.

The Wall.Flipped property and Wall.flip() method gain access to and control Wall orientation. In the following examples, a Wall is compared before and after calling the flip() method.

-   The Orientation property before is (0.0, 1.0, 0.0).
-   The Orientation property after the flip call is (0.0, -1.0, 0.0).
-   The Wall Location Line (WALL\_KEY\_REF\_PARAM) parameter is 3, which represents Finish Face: Interior in the following table.
-   Taking the line as reference, the Wall is moved but the Location is not changed.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4BFD801E-18BC-4021-8371-C29AF13CF7EE-low.png)**Figure 33: Original wall**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-85CF3DAD-C029-41C5-ACC6-1FEC8CA304E4-low.png)**Figure 34: Wall after flip**

**Table 24: Wall Location Line**

<table summary="" id="GUID-DBFA35F2-854F-458C-8BD4-B886F91981EE__TABLE_D1C2E830D5A34AF387D50C37DC8FF5AC"><tbody><tr><td><b>Location Line Value</b></td><td><b>Description</b></td></tr><tr><td>0</td><td>Wall Centerline</td></tr><tr><td>1</td><td>Core Centerline</td></tr><tr><td>2</td><td>Finish Face: Exterior</td></tr><tr><td>3</td><td>Finish Face: Interior</td></tr><tr><td>4</td><td>Core Face: Exterior</td></tr><tr><td>5</td><td>Core Face: Interior</td></tr></tbody></table>

There are five static override methods in the Wall class to create a Wall:

**Table 25: Create() Overrides**

<table summary="" id="GUID-DBFA35F2-854F-458C-8BD4-B886F91981EE__TABLE_5F0A5294142A40DD9C8382976D7EF4D9"><tbody><tr><td><b>Name</b></td><td><b>Description</b></td></tr><tr><td>Create(Document, Curve, WallType, Level, Double, Double, Boolean, Boolean)</td><td>Creates a new rectangular profile wall within the project using the specified wall type, height, and offset.</td></tr><tr><td>Create(Document, IList Curve , Boolean)</td><td>Creates a non rectangular profile wall within the project using the default wall style.</td></tr><tr><td>Create(Document, Curve, ElementId, Boolean)</td><td>Creates a new rectangular profile wall within the project on the level specified by ElementId using the default wall style.</td></tr><tr><td>Create(Document, IList Curve , ElementId, ElementId, Boolean)</td><td>Creates a non rectangular profile wall within the project using the specified wall type.</td></tr><tr><td>Create(Document, IList Curve , ElementId, ElementId, Boolean, XYZ)</td><td>Creates a non rectangular profile wall within the project using the specified wall type and normal vector.</td></tr></tbody></table>

The WallType Wall Function (WALL\_ATTR\_EXTERIOR) parameter influences the created wall instance Room Bounding and Structural Usage parameter. The WALL\_ATTR\_EXTERIOR value is an integer:

**Table 26: Wall Function**

<table summary="" id="GUID-DBFA35F2-854F-458C-8BD4-B886F91981EE__TABLE_9BB324360ECB41C9887D12CF817A6B8B"><tbody><tr><td><b>Wall Function</b></td><td><b>Interior</b></td><td><b>Exterior</b></td><td><b>Foundation</b></td><td><b>Retaining</b></td><td><b>Soffit</b></td></tr><tr><td>Value</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr></tbody></table>

The following rules apply to Walls created by the API:

-   If the input structural parameter is true or the Wall Function (WALL\_ATTR\_EXTERIOR) parameter is Foundation, the Wall StructuralUsage parameter is Bearing; otherwise it is NonBearing.
-   The created Wall Room Bounding (WALL\_ATTR\_ROOM\_BOUNDING) parameter is false if the Wall Function (WALL\_ATTR\_EXTERIOR) parameter is Retaining.

For more information about structure-related functions such as the AnalyticalModel property, refer to [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html).

## Wall Profile Sketch

These methods provide access to add and remove profile sketches:

-   Wall.CreateProfileSketch()
-   Wall.RemoveProfileSketch()

`Wall.CanHaveProfileSketch()` returns True if the wall supports profile sketch. Arc walls and elliptical walls are two wall geometries that do not support having an edited profile. Once a sketch is added, the profile sketch can be edited using `SketchEditScope`

## Slanted and Tapered Walls

`Wall.CrossSection` lets you get and set a wall to a value of the `WallCrossSection` enum (`SingleSlanted`, `Vertical`, `Tapered`). Wall.IsWallCrossSectionValid() checks if a cross section is valid for a specific wall.

`Autodesk.Revit.DB.WidthMeasuredAt` and `Autodesk.Revit.DB.InsertOrientation` define the shape of the wall and behavior of inserts for non-vertical walls.


<!-- ===== END: Help  Walls  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Floors, Ceilings and Foundations  Autodesk.md ===== -->

---
created: 2026-01-28T21:04:51 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Floors_Ceilings_and_Foundations_html
author: 
---

# Help | Floors, Ceilings and Foundations | Autodesk

> ## Excerpt
> Classes associated with floors, ceilings and foundations.

---
Classes associated with floors, ceilings and foundations.

Floor, Ceiling and Foundation-related API items include:

**Table 28: Floors, Ceilings and Foundations in the API**

<table summary="" id="GUID-3CEBFF98-2EAB-4EF8-90ED-525F4EFAF0B4__TABLE_6927EDD93D5D4FC7AEA1214BFAB78CD9"><tbody><tr><td><b>Object</b></td><td><b>Element Type</b></td><td><b>ElementType Type</b></td><td><b>Element Creation</b></td><td><b>Other</b></td></tr><tr><td>Floor</td><td>Floor</td><td>FloorType</td><td>Floor.Create()</td><td>FloorType.IsFoundationSlab = false</td></tr><tr><td>Ceiling</td><td>Ceiling</td><td>CeilingType</td><td>Ceiling.Create()</td><td>Category = OST_Ceilings</td></tr><tr><td>Wall Foundation</td><td>WallFoundation</td><td>WallFoundationType</td><td>No</td><td>Category = OST_StructuralFoundation</td></tr><tr><td>Isolated Foundation</td><td>FamilyInstance</td><td>FamilySymbol</td><td>NewFamilyInstance()</td><td>Category = OST_StructuralFoundation</td></tr><tr><td>Foundation Slab</td><td>Floor</td><td>FloorType</td><td>Floor.Create()</td><td>Category = OST_StructuralFoundation<p>FloorType.IsFoundationSlab = true</p></td></tr></tbody></table>

Note: Floor and Ceiling derive from the class CeilingAndFloor.

The following rules apply to Floor:

-   Elements created from the Foundation Design bar have the same category, OST\_StructuralFoundation, but correspond to different Classes.
-   The FloorType IsFoundationSlab property sets the FloorType category to OST\_StructuralFoundation or not.

When you retrieve FloorType to create a Floor or Foundation Slab with Floor.Create(), use the following methods:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-26C2760B-04F0-4690-AF22-6EB1A0CDD933-low.png)**Figure 35: Create foundation and floor/slab**

Currently, the API does not provide access to the Floor Slope Arrow in the Floor class. However, when using the structural features of Revit, you can create a sloped slab with Floor.Create():

<table summary="" id="GUID-3CEBFF98-2EAB-4EF8-90ED-525F4EFAF0B4__TABLE_C83EA49039D54AAFAC50A3E5FB45B783"><tbody><tr><td><b>Code Region 11-1: Floor.Create()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>Floor</span><span> </span><span>Create</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>IList</span><span>&lt;</span><span>CurveLoop</span><span>&gt;</span><span> profile</span><span>,</span><span> </span><span>ElementId</span><span> floorTypeId</span><span>,</span><span> </span><span>ElementId</span><span> levelId</span><span>)</span><span>

</span><span>public</span><span> </span><span>static</span><span> </span><span>Floor</span><span> </span><span>Create</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>IList</span><span>&lt;</span><span>CurveLoop</span><span>&gt;</span><span> profile</span><span>,</span><span> </span><span>ElementId</span><span> floorTypeId</span><span>,</span><span> </span><span>ElementId</span><span> levelId</span><span>,</span><span> </span><span>bool</span><span> isStructural</span><span>,</span><span> </span><span>Line</span><span> slopeArrow</span><span>,</span><span> </span><span>double</span><span> slope
</span><span>)</span></code></pre></td></tr></tbody></table>

The Slope Arrow is created using the slopedArrow parameter.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-5589AB8C-03FB-4FE6-BB20-065A37058854-low.png)**Figure 36: slopeArrow parameter in Floor.Create()**

The unit for the slope parameter in Floor.Create() is rise/run.

The Floor.FloorType property is an alternative to using the Floor.GetTypeId() method. For more information about structure-related members such as the GetSpanDirectionSymbolIds() method and the SpanDirectionAngle property, refer to the [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html) section.

When editing an Isolated Foundation in Revit, you can perform the following actions:

-   You can pick a host, such as a floor. However, the FamilyInstance object Host property always returns null.
-   When deleting the host floor, the Foundation is not deleted with it.
-   The Foundation host is available from the Host (INSTANCE\_FREE\_HOST\_PARAM) parameter.
-   Use another related Offset (INSTANCE\_FREE\_HOST\_OFFSET\_PARAM) parameter to control the foundation offset from the host Element.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-6FECE5EE-DCFE-42E5-B3F8-868B44E774D5-low.png)**Figure 37: Pick Host for FoundationSlab (FamilyInstance)**

Wall foundations are represented by the WallFoundation class in the API. The API provides limited access to both WallFoundation and WallFoundationType except when using the GetAnalyticalModel() method (refer to [Analytical Model](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Analytical_Model_html) in the [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html) section). For example, the attached wall is not available with the architectural features of Revit. Using the structural features of Revit, the relationship between the Wall class and the WallFoundation class is shown using the GetAnalyticalModelSupports() method in the AnalyticalModel class. For more details, refer to [Analytical Model](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Analytical_Model_html) in the [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html) section.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-03EA5485-1F1B-429D-8917-02B86A50E627-low.png)**Figure 38: Wall Foundation**

## Modifying Slabs

You can modify the form of slab-based elements using the SlabShapeEditor class. This class allows you to:

-   Manipulate one or more of the points or edges on a selected slab-based element
-   Add points on the element to change the element's geometry
-   Add linear edges and split the existing face of a slab into smaller sub-regions
-   Remove the shape modifier and reset the element geometry back to the unmodified shape.

Here's an example of reverting a selected modified floor back to its original shape:

<table summary="" id="GUID-3CEBFF98-2EAB-4EF8-90ED-525F4EFAF0B4__TABLE_E365960730F7410487731E02F9030D3B"><tbody><tr><td><b>Code Region 11-2: Reverting a slab's shape</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ResetSlabShapes</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>Selection</span><span> choices </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> elem </span><span>in</span><span> choices</span><span>.</span><span>GetElementIds</span><span>().</span><span>Select</span><span>(</span><span>q </span><span>=&gt;</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>q</span><span>)))</span><span>
        </span><span>{</span><span>
                </span><span>Floor</span><span> floor </span><span>=</span><span> elem </span><span>as</span><span> </span><span>Floor</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>floor </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>SlabShapeEditor</span><span> slabShapeEditor </span><span>=</span><span> floor</span><span>.</span><span>SlabShapeEditor</span><span>;</span><span>
                        slabShapeEditor</span><span>.</span><span>ResetSlabShape</span><span>();</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

For more detailed examples of using the SlabShapeEditor and related classes, see the SlabShapeEditing sample application included in the Revit SDK.


<!-- ===== END: Help  Floors, Ceilings and Foundations  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Roofs  Autodesk.md ===== -->

---
created: 2026-01-28T21:04:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Roofs_html
author: 
---

# Help | Roofs | Autodesk

> ## Excerpt
> Representation of roofs in the Revit API.

---
Representation of roofs in the Revit API.

Roofs in the Revit Platform API all derive from the RoofBase object. There are two classes:

-   FootPrintRoof - represents a roof made from a building footprint
-   ExtrusionRoof - represents roof made from an extruded profile

Both have a RoofType property that gets or sets the type of roof. This example shows how you can create a footprint roof based on some selected walls:

<table summary="" id="GUID-33E6A6BD-96AA-4FAF-B660-1DD0C06CCD29__TABLE_9CC9AA615AA2427880945521FA9EACFA"><tbody><tr><td><b>Code Region 11-3: Creating a footprint roof</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateRoof</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Before invoking this sample, select some walls to add a roof over.</span><span>
    </span><span>// Make sure there is a level named "Roof" in the document.</span><span>

    </span><span>// find the Roof level</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Level</span><span>));</span><span>
    </span><span>var</span><span> elements </span><span>=</span><span> </span><span>from</span><span> element </span><span>in</span><span> collector </span><span>where</span><span> element</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Roof"</span><span> </span><span>select</span><span> element</span><span>;</span><span>
    </span><span>Level</span><span> level </span><span>=</span><span> elements</span><span>.</span><span>Cast</span><span>&lt;</span><span>Level</span><span>&gt;().</span><span>ElementAt</span><span>&lt;</span><span>Level</span><span>&gt;(</span><span>0</span><span>);</span><span>

    collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>RoofType</span><span>));</span><span>
    </span><span>RoofType</span><span> roofType </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>RoofType</span><span>;</span><span> 

    </span><span>// Get the handle of the application</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>;</span><span>

    </span><span>// Define the footprint for the roof based on user selection</span><span>
    </span><span>CurveArray</span><span> footprint </span><span>=</span><span> application</span><span>.</span><span>Create</span><span>.</span><span>NewCurveArray</span><span>();</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>selectedIds</span><span>.</span><span>Count</span><span> </span><span>!=</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Element</span><span> element </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
            </span><span>Wall</span><span> wall </span><span>=</span><span> element </span><span>as</span><span> </span><span>Wall</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>wall </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>LocationCurve</span><span> wallCurve </span><span>=</span><span> wall</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
                footprint</span><span>.</span><span>Append</span><span>(</span><span>wallCurve</span><span>.</span><span>Curve</span><span>);</span><span>
                </span><span>continue</span><span>;</span><span>
            </span><span>}</span><span>

            </span><span>ModelCurve</span><span> modelCurve </span><span>=</span><span> element </span><span>as</span><span> </span><span>ModelCurve</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>modelCurve </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                footprint</span><span>.</span><span>Append</span><span>(</span><span>modelCurve</span><span>.</span><span>GeometryCurve</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"You should select a curve loop, or a wall loop, or loops combination \nof walls and curves to create a footprint roof."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>ModelCurveArray</span><span> footPrintToModelCurveMapping </span><span>=</span><span> </span><span>new</span><span> </span><span>ModelCurveArray</span><span>();</span><span>
    </span><span>FootPrintRoof</span><span> footprintRoof </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFootPrintRoof</span><span>(</span><span>footprint</span><span>,</span><span> level</span><span>,</span><span> roofType</span><span>,</span><span> </span><span>out</span><span> footPrintToModelCurveMapping</span><span>);</span><span>
    </span><span>ModelCurveArrayIterator</span><span> iterator </span><span>=</span><span> footPrintToModelCurveMapping</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
    iterator</span><span>.</span><span>Reset</span><span>();</span><span>
    </span><span>while</span><span> </span><span>(</span><span>iterator</span><span>.</span><span>MoveNext</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>ModelCurve</span><span> modelCurve </span><span>=</span><span> iterator</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>ModelCurve</span><span>;</span><span>
        footprintRoof</span><span>.</span><span>set_DefinesSlope</span><span>(</span><span>modelCurve</span><span>,</span><span> </span><span>true</span><span>);</span><span>
        footprintRoof</span><span>.</span><span>set_SlopeAngle</span><span>(</span><span>modelCurve</span><span>,</span><span> </span><span>0.5</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

For an example of how to create an ExtrusionRoof, see the NewRoof sample application included with the Revit API SDK.

### Gutter and Fascia

Gutter and Fascia elements are derived from the HostedSweep class, which represents a roof. They can be created, deleted or modified via the API. To create these elements, use one of the Document.Create.NewFascia() or Document.Create.NewGutter() overrides. For an example of how to create new gutters and fascia, see the NewHostedSweep application included in the SDK samples. Below is a code snippet showing you can modify a gutter element's properties.

<table summary="" id="GUID-33E6A6BD-96AA-4FAF-B660-1DD0C06CCD29__TABLE_F7ADB54D499C440AB8A9183491470E2D"><tbody><tr><td><b>Code Region 11-4: Modifying a gutter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ModifyGutter</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> elem </span><span>in</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>().</span><span>Select</span><span>(</span><span>q </span><span>=&gt;</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>q</span><span>)))</span><span>
        </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>elem </span><span>is</span><span> </span><span>Gutter</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>Gutter</span><span> gutter </span><span>=</span><span> elem </span><span>as</span><span> </span><span>Gutter</span><span>;</span><span>
                        </span><span>// convert degrees to rads:</span><span>
                        gutter</span><span>.</span><span>Angle</span><span> </span><span>=</span><span> </span><span>45.00</span><span> </span><span>*</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>180</span><span>;</span><span>
                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Changed gutter angle"</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Roofs  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Curtains  Autodesk.md ===== -->

---
created: 2026-01-28T21:05:00 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Curtains_html
author: 
---

# Help | Curtains | Autodesk

> ## Excerpt
> Curtain walls, curtain systems, and curtain roofs are host elements for CurtainGrid objects. A curtain wall can have only one CurtainGrid, while curtain systems and curtain roofs may contain one or more CurtainGrids. For an example of how to create a CurtainSystem, see the CurtainSystem sample application included with the Revit SDK. For an example of creating a curtain wall and populating it with grid lines, see the CurtainWallGrid sample application.

---
Curtain walls, curtain systems, and curtain roofs are host elements for CurtainGrid objects. A curtain wall can have only one CurtainGrid, while curtain systems and curtain roofs may contain one or more CurtainGrids. For an example of how to create a CurtainSystem, see the CurtainSystem sample application included with the Revit SDK. For an example of creating a curtain wall and populating it with grid lines, see the CurtainWallGrid sample application.

**Parent page:** [Walls, Floors, Ceilings, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html)


<!-- ===== END: Help  Curtains  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Other Elements  Autodesk.md ===== -->

---
created: 2026-01-28T21:05:05 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Other_Elements_html
author: 
---

# Help | Other Elements | Autodesk

> ## Excerpt
> Some Elements are not HostObjects (and don't have a specific class), but are special cases that can host other objects. For example, ramp and its associated element type, do not have specific classes in the API and instead are represented as Element and ElementType in the OST_Ramps category.

---
Some Elements are not HostObjects (and don't have a specific class), but are special cases that can host other objects. For example, ramp and its associated element type, do not have specific classes in the API and instead are represented as Element and ElementType in the OST\_Ramps category.

**Parent page:** [Walls, Floors, Ceilings, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html)


<!-- ===== END: Help  Other Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  CompoundStructure  Autodesk.md ===== -->

---
created: 2026-01-28T21:05:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_CompoundStructure_html
author: 
---

# Help | CompoundStructure | Autodesk

> ## Excerpt
> Describes the internal structure of a wall, floor, roof or ceiling.

---
Describes the internal structure of a wall, floor, roof or ceiling.

Walls, floors, ceilings and roofs are all children of the API class HostObject. HostObject (and its related type class HostObjAttributes) provide read only access to the CompoundStructure. A compound structure consists a collection of ordered layers, proceeding from exterior to interior for a wall, or from top to bottom for a floor, roof or ceiling. The properties of these layers determine the thickness, material, and function of the overall structure of the associated wall, floor, roof or ceiling.

Layers can be accessed via the GetLayers() method and completely replaced using SetLayers().

Normally these layers are parallel and extend the entire host object with a fixed layer width. However, for walls the structure can also be “vertically compound”, where the layers vary at specified vertical distances from the top and bottom of the wall. Use CompoundStructure.IsVerticallyCompound to identify these. For vertically compound structures, the structure describes a vertical section via a rectangle which is divided into polygonal regions whose sides are all vertical or horizontal segments. A map associates each of these regions with the index of a layer in the CompoundStructure which determines the properties of that region.

It is possible to use the compound structure to find the geometric location of different layer boundaries. The method CompoundStructure.GetOffsetForLocationLine() provides the offset from the center location line to any of the location line options (core centerline, finish faces on either side, or core sides).

With the offset to the location line available, you can obtain the location of each layer boundary by starting from a known location and obtaining the widths of each bounding layer using CompoundStructure.GetLayerWidth().

Some notes about the use of CompoundStructure:

-   The total width of the element is the sum of each CompoundStructureLayer's widths. You cannot change the element's total width directly but you can change it via changing the CompoundStructureLayer width. The index of the designated variable length layer (if assigned) can be obtained from CompoundStructure.VariableLayerIndex.
    
-   You must set the CompoundStructure back to the HostObjAttributes instance (using the HostObjAttributes.SetCompoundStructure() method) in order for any change to be stored.
    
-   Changes to the HostObjAttributes affects every instance in the current document. If you need a new combination of layers,you will need to create a new HostObjAttributes (use ElementType.Duplicate()) and assign the new CompoundStructure to it.
    
-   The CompoundStructureLayer DeckProfileId, and DeckEmbeddingType, properties only work with Slab in the structural features of Revit. For more details, refer to [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html).
    
    ### Material
    

Each CompoundStructureLayer in HostObjAttributes is typically displayed with some type of material. If CompoundStructureLayer.MaterialId returns -1, it means the Material is Category-related. For more details, refer to [Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_html). Getting the CompoundStructureLayer Material is illustrated in the following sample code:

<table summary="" id="GUID-93FA05F8-0A12-430E-9988-D0D0595F8AAD__TABLE_82B43B7300BD450796CC03B312C78A95"><tbody><tr><td><b>Code Region 11-5: Getting the CompoundStructureLayer Material</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetWallLayerMaterial</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// get WallType of wall</span><span>
        </span><span>WallType</span><span> aWallType </span><span>=</span><span> wall</span><span>.</span><span>WallType</span><span>;</span><span>
        </span><span>// Only Basic Wall has compoundStructure</span><span>
        </span><span>if</span><span> </span><span>(</span><span>WallKind</span><span>.</span><span>Basic</span><span> </span><span>==</span><span> aWallType</span><span>.</span><span>Kind</span><span>)</span><span>
        </span><span>{</span><span>

                </span><span>// Get CompoundStructure</span><span>
                </span><span>CompoundStructure</span><span> comStruct </span><span>=</span><span> aWallType</span><span>.</span><span>GetCompoundStructure</span><span>();</span><span>
                </span><span>Categories</span><span> allCategories </span><span>=</span><span> document</span><span>.</span><span>Settings</span><span>.</span><span>Categories</span><span>;</span><span>

                </span><span>// Get the category OST_Walls default Material; </span><span>
                </span><span>// use if that layer's default Material is &lt;By Category&gt;</span><span>
                </span><span>Category</span><span> wallCategory </span><span>=</span><span> allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Walls</span><span>);</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> wallMaterial </span><span>=</span><span> wallCategory</span><span>.</span><span>Material</span><span>;</span><span>

                </span><span>foreach</span><span> </span><span>(</span><span>CompoundStructureLayer</span><span> structLayer </span><span>in</span><span> comStruct</span><span>.</span><span>GetLayers</span><span>())</span><span>
                </span><span>{</span><span>
                        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> layerMaterial </span><span>=</span><span> 
                                document</span><span>.</span><span>GetElement</span><span>(</span><span>structLayer</span><span>.</span><span>MaterialId</span><span>)</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>

                        </span><span>// If CompoundStructureLayer's Material is specified, use default</span><span>
                        </span><span>// Material of its Category</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> layerMaterial</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>switch</span><span> </span><span>(</span><span>structLayer</span><span>.</span><span>Function</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Finish1</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span>                                       
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsFinish1</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Finish2</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span>                                      
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsFinish2</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Membrane</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span>
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsMembrane</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Structure</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span>  
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsStructure</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Substrate</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span> 
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsSubstrate</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Insulation</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span> 
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsInsulation</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>default</span><span>:</span><span>
                                                </span><span>// It is impossible to reach here</span><span>
                                                </span><span>break</span><span>;</span><span>
                                </span><span>}</span><span>
                                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> layerMaterial</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>// CompoundStructureLayer's default Material is its SubCategory</span><span>
                                        layerMaterial </span><span>=</span><span> wallMaterial</span><span>;</span><span>
                                </span><span>}</span><span>
                        </span><span>}</span><span>
                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Layer Material: "</span><span> </span><span>+</span><span> layerMaterial</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Sometimes just the material from the "structural" layer is needed. Rather than looking at each layer for the one whose function is MaterialFunctionAssignment.Structure, use the CompoundStructure.StructuralMaterialIndex property to find the index of the layer whose material defines the structural properties of the type for the purposes of analysis.

Note: When calling SetLayers(), the StructuralMaterialIndex value will be cleared and need to be reset.


<!-- ===== END: Help  CompoundStructure  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Opening  Autodesk.md ===== -->

---
created: 2026-01-28T21:05:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Opening_html
author: 
---

# Help | Opening | Autodesk

> ## Excerpt
> In the Revit Platform API, the Opening object is derived from the Element object and contains all of the Element object properties and methods. To retrieve all Openings in a project, use Document.ElementIterator to find the Elements.Opening objects.

---
In the Revit Platform API, the Opening object is derived from the Element object and contains all of the Element object properties and methods. To retrieve all Openings in a project, use Document.ElementIterator to find the Elements.Opening objects.

## General Properties

This section explains how to use the Opening properties.

-   IsRectBoundary - Identifies whether the opening has a rectangular boundary.
    
    -   If true, it means the Opening has a rectangular boundary and you can get an `IList<XYZ>` collection from the Opening BoundaryRect property. Otherwise, the property returns null.
    -   If false, you can get a CurveArray object from the BoundaryCurves property.
-   BoundaryCurves - If the opening boundary is not a rectangle, this property retrieves geometry information; otherwise it returns null. The property returns a CurveArray object containing the curves that represent the Opening object boundary.For more details about Curve, refer to [Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html).
    
-   BoundaryRect - If the opening boundary is a rectangle, you can get the geometry information using this property; otherwise it returns null.
    
    -   The property returns an `IList<XYZ>` collection containing the XYZ coordinates.
    -   The `IList<XYZ>` collection usually contains the rectangle boundary minimum (lower left) and the maximum (upper right) coordinates.
-   Host - The host property retrieves the Opening host element. The host element is the element cut by the Opening object.
    
    Note: Note If the Opening object's category is Shaft Openings, the Opening host is null.
    

The following example illustrates how to retrieve the existing Opening properties.

<table summary="" id="GUID-CA1FB5D9-49BE-40D6-B9AA-BFDE21B10C8D__TABLE_6359220C1A1B44E8843360E673ED5623"><tbody><tr><td><b>Code Region 11-6: Retrieving existing opening properties</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>Getinfo_Opening</span><span>(</span><span>Opening</span><span> opening</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Opening:"</span><span>;</span><span>

    </span><span>//get the host element of this opening</span><span>
    message </span><span>+=</span><span> </span><span>"\nThe id of the opening's host element is : "</span><span> </span><span>+</span><span> opening</span><span>.</span><span>Host</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>;</span><span>

    </span><span>//get the information whether the opening has a rect boundary</span><span>
    </span><span>//If the opening has a rect boundary, we can get the geometry information from BoundaryRect property.</span><span>
    </span><span>//Otherwise we should get the geometry information from BoundaryCurves property</span><span>
    </span><span>if</span><span> </span><span>(</span><span>opening</span><span>.</span><span>IsRectBoundary</span><span>)</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"\nThe opening has a rectangular boundary."</span><span>;</span><span>
        </span><span>//array contains two XYZ objects: the max and min coords of boundary</span><span>
        </span><span>IList</span><span>&lt;</span><span>XYZ</span><span>&gt;</span><span> boundaryRect </span><span>=</span><span> opening</span><span>.</span><span>BoundaryRect</span><span>;</span><span>

        </span><span>//get the coordinate value of the min coordinate point</span><span>
        XYZ point </span><span>=</span><span> opening</span><span>.</span><span>BoundaryRect</span><span>[</span><span>0</span><span>];</span><span>
        message </span><span>+=</span><span> </span><span>"\nMin coordinate point:("</span><span> </span><span>+</span><span> point</span><span>.</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                                </span><span>+</span><span> point</span><span>.</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>

        </span><span>//get the coordinate value of the Max coordinate point</span><span>
        point </span><span>=</span><span> opening</span><span>.</span><span>BoundaryRect</span><span>[</span><span>1</span><span>];</span><span>
        message </span><span>+=</span><span> </span><span>"\nMax coordinate point: ("</span><span> </span><span>+</span><span> point</span><span>.</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                                </span><span>+</span><span> point</span><span>.</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"\nThe opening doesn't have a rectangular boundary."</span><span>;</span><span>
        </span><span>// Get curve number</span><span>
        </span><span>int</span><span> curves </span><span>=</span><span> opening</span><span>.</span><span>BoundaryCurves</span><span>.</span><span>Size</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nNumber of curves is : "</span><span> </span><span>+</span><span> curves</span><span>;</span><span>
        </span><span>for</span><span> </span><span>(</span><span>int</span><span> i </span><span>=</span><span> </span><span>0</span><span>;</span><span> i </span><span>&lt;</span><span> curves</span><span>;</span><span> i</span><span>++)</span><span>
        </span><span>{</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> curve </span><span>=</span><span> opening</span><span>.</span><span>BoundaryCurves</span><span>.</span><span>get_Item</span><span>(</span><span>i</span><span>);</span><span>
            </span><span>// Get curve start point</span><span>
            message </span><span>+=</span><span> </span><span>"\nCurve start point: "</span><span> </span><span>+</span><span> </span><span>XYZToString</span><span>(</span><span>curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>));</span><span>
            </span><span>// Get curve end point</span><span>
            message </span><span>+=</span><span> </span><span>"; Curve end point: "</span><span> </span><span>+</span><span> </span><span>XYZToString</span><span>(</span><span>curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>));</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span><span>

</span><span>// output the point's three coordinates</span><span>
</span><span>string</span><span> </span><span>XYZToString</span><span>(</span><span>XYZ point</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>return</span><span> </span><span>"("</span><span> </span><span>+</span><span> point</span><span>.</span><span>X </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Create Opening

In the Revit Platform API, use the Document.NewOpening() method to create an opening in your project. There are four method overloads you can use to create openings in different host elements:

<table summary="" id="GUID-CA1FB5D9-49BE-40D6-B9AA-BFDE21B10C8D__TABLE_D5371F4390C94C50ADF221D5615F7BB0"><tbody><tr><td><b>Code Region 11-7: NewOpening()</b></td></tr><tr><td><pre><code><span>//Create a new Opening in a beam, brace and column. </span><span>
</span><span>public</span><span> </span><span>Opening</span><span> </span><span>NewOpening</span><span>(</span><span>Element</span><span> famInstElement</span><span>,</span><span> </span><span>CurveArray</span><span> profile</span><span>,</span><span> eRefFace iFace</span><span>);</span><span> </span></code></pre></td></tr><tr><td><pre><code><span>//Create a new Opening in a roof, floor and ceiling. </span><span>
</span><span>public</span><span> </span><span>Opening</span><span> </span><span>NewOpening</span><span>(</span><span>Element</span><span> hostElement</span><span>,</span><span> </span><span>CurveArray</span><span> profile</span><span>,</span><span> </span><span>bool</span><span> bPerpendicularFace</span><span>);</span></code></pre></td></tr><tr><td><pre><code><span>//Create a new Opening Element. </span><span>
</span><span>public</span><span> </span><span>Opening</span><span> </span><span>NewOpening</span><span>(</span><span>Level</span><span> bottomLevel</span><span>,</span><span> </span><span>Level</span><span> topLevel</span><span>,</span><span> </span><span>CurveArray</span><span>  profile</span><span>);</span></code></pre></td></tr><tr><td><pre><code><span>//Create an opening in a straight wall or arc wall. </span><span>
</span><span>public</span><span> </span><span>Opening</span><span> </span><span>NewOpening</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> XYZ pntStart</span><span>,</span><span> XYZ pntEnd</span><span>);</span></code></pre></td></tr></tbody></table>

-   Create an Opening in a Beam, Brace, or Column - Use to create an opening in a family instance. The iFace parameter indicates the face on which the opening is placed.
    
-   Create a Roof, Floor, or Ceiling Opening - Use to create an opening in a roof, floor, or ceiling.
    
-   The bPerpendicularFace parameter indicates whether the opening is perpendicular to the face or vertical.
    
-   If the parameter is true, the opening is perpendicular to the host element face. See the following picture: ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-EED350DF-2DD4-4562-998D-C020C739D6F8-low.png)**Figure 39: Opening cut perpendicular to the host element face**
    
    ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-BF04D2D0-A6EA-4D99-9936-615D1C13DB8D-low.png)**Figure 40: Opening cut vertically to the host element**
    
-   Create a New Opening Element - Use to create a shaft opening in your project. However, make sure the topLevel is higher than the bottomLevel; otherwise an exception is thrown.
    
-   Create an Opening in a Straight Wall or Arc Wall - Use to create a rectangle opening in a wall. The coordinates of pntStart and pntEnd should be corner coordinates that can shape a rectangle. For example, the lower left corner and upper right corner of a rectangle. Otherwise an exception is thrown.
    

Note: Using the Opening command you can only create a rectangle shaped wall opening. To create some holes in a wall, edit the wall profile instead of the Opening command.


<!-- ===== END: Help  Opening  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Thermal Properties  Autodesk.md ===== -->

---
created: 2026-01-28T21:05:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Thermal_Properties_html
author: 
---

# Help | Thermal Properties | Autodesk

> ## Excerpt
> Certain assembly types such as Wall, Floor, Ceiling, Roof and Building Pad have calculated and settable thermal properties which are represented by the ThermalProperties class.

---
Certain assembly types such as Wall, Floor, Ceiling, Roof and Building Pad have calculated and settable thermal properties which are represented by the ThermalProperties class.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ThermalProperties-76171.jpg)The ThermalProperties class has properties for the values shown above. Absorptance and Roughness are modifiable while HeatTransferCoefficient, ThermalResistance, and ThermalMass are read-only. The units for these calculated values are shown in the table below.

<table summary="" id="GUID-3039C4C4-B35C-4EFA-B93E-99833E12444D__TABLE_FB19236D5E804DC38F27F878579F1DAF"><tbody><tr><td><b>Property</b></td><td><b>Unit</b></td></tr><tr><td>HeatTransferCoefficient</td><td>watts per meter-squared kelvin<p>(W/(m^2*K)</p></td></tr><tr><td>ThermalResistance</td><td>meter-squared kelvin per watt<p>((m^2*K)/Watt)</p></td></tr><tr><td>ThermalMass</td><td>kilogram feet-squared per second squared kelvin<p>(kg ft^2/(s^2 K))</p></td></tr></tbody></table>

Thermal properties can be retrieved using the ThermalProperties property on the following types:

-   WallType
-   FloorType
-   CeilingType
-   RoofType
-   BuildingPadType


<!-- ===== END: Help  Thermal Properties  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Family Instances  Autodesk.md ===== -->

---
created: 2026-01-28T21:05:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_html
author: 
---

# Help | Family Instances | Autodesk

> ## Excerpt
> In this section, you will learn about the following:

---
In this section, you will learn about the following:

-   The relationship between family and family instance
-   Family and family instance features
-   How to load or create family and family instance features
-   The relationship between family instance and family symbol


<!-- ===== END: Help  Family Instances  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Identifying Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:58:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Identifying_Elements_html
author: 
---

# Help | Identifying Elements | Autodesk

> ## Excerpt
> In Revit, the easiest way to judge whether an element is a FamilyInstance or not is by using the properties dialog box.

---
In Revit, the easiest way to judge whether an element is a FamilyInstance or not is by using the properties dialog box.

-   If the family name starts with System Family and the Load button is disabled, it belongs to System Family. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-96BC987E-5C38-45EF-9621-2D6EF89989B1-low.png)**Figure 41: System Family**
    
-   A general FamilyInstance, which belongs to the Component Family, does not start with System Family.
    
-   For example, in the following picture the family name for the desk furniture is Desk. In addition, the Load button is enabled. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-67F1CF63-64EF-40E4-BF92-284873CDDB31-low.png)**Figure 42: Component Family**
    
-   There are some exceptions, for example: Mass and in-place member. The Family and Type fields are blank. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-A2B06CEE-7E4A-494B-8DE8-7131068F182B-low.png)**Figure 43: Mass or in-place member example**
    

Families in the Revit Platform API are represented by three objects:

-   Family
-   FamilySymbol
-   FamilyInstance

Each object plays a significant role in the family structure.

The Family object represents an entire family such as Single-Flush doors. For example, the Single-Flush door Family corresponds to the Single-Flush.rfa file. The Family object contains several FamilySymbols that are used to get all family symbols to facilitate swapping instances from one symbol to another.

The FamilySymbol object represents a specific set of family settings corresponding to a Type in the Revit UI, such as 34"×80".

The FamilyInstance object represents an actual Type (FamilySymbol) instance in the Revit project. For example, in the following picture, the FamilyInstance is a single door in the project.

-   Each FamilyInstance has one FamilySymbol. The door is an instance of a 34"×80".
-   Each FamilySymbol belongs to one Family. The 34"×80" symbol belongs to a Single-Flush family.
-   Each Family contains one or more FamilySymbols. The Single-Flush family contains a 34"×80" symbol, a 34"×84" symbol, a 36"×84" and so on.

Note: While most component elements are exposed through the API classes FamilySymbol and FamilyInstance, some have been wrapped with specific API classes. For example, AnnotationSymbolType wraps FamilySymbol and AnnotationSymbol wraps FamilyInstance.


<!-- ===== END: Help  Identifying Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Family  Autodesk.md ===== -->

---
created: 2026-01-28T20:58:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Family_html
author: 
---

# Help | Family | Autodesk

> ## Excerpt
> The Family class represents an entire Revit family. It contains the FamilySymbols used by FamilyInstances.

---
The Family class represents an entire Revit family. It contains the FamilySymbols used by FamilyInstances.

### Loading Families

The Document class contains the LoadFamily() and LoadFamilySymbol() methods.

-   LoadFamily() loads an entire family and all of its types or symbols into the project.
-   LoadFamilySymbol() loads only the specified family symbol from a family file into the project.

Note: To improve the performance of your application and reduce memory usage, if possible load specific FamilySymbols instead of entire Family objects.

-   The family file path is retrieved using the Options.Application object GetLibraryPaths() method.
-   The Options.Application object is retrieved using the Application object Options property.
-   In LoadFamilySymbol(), the input argument Name is the same string value returned by the FamilySymbol object Name property.

For more information, refer to [Code Samples](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Code_Samples_html).

### Categories

The Family.FamilyCategory property indicates the category of the Family such as Columns, Furniture, Structural Framing, or Windows.


<!-- ===== END: Help  Family  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  FamilyInstances  Autodesk.md ===== -->

---
created: 2026-01-28T20:58:34 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_FamilyInstances_html
author: 
---

# Help | FamilyInstances | Autodesk

> ## Excerpt
> FamilyInstance objects include Beams, Braces, Columns, Furniture, Massing, and more. The FamilyInstance object provides more detailed properties so that the family instance type and appearance in the project can be changed.

---
FamilyInstance objects include Beams, Braces, Columns, Furniture, Massing, and more. The FamilyInstance object provides more detailed properties so that the family instance type and appearance in the project can be changed.

Location-related properties show the physical and geometric characteristics of FamilyInstance objects, such as orientation, rotation and location.

#### Orientation

The face orientation or hand orientation can be changed for some FamilyInstance objects. For example, a door can face the outside or the inside of a room or wall and it can be placed with the handle on the left side or the right side. The following table compares door, window, and desk family instances.

**Table 29: Compare Family Instances**

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_371C55EC78FA4B73AB166155DE3B21DF"><tbody><tr><td><b>Boolean Property</b></td><td><b>Door</b></td><td><b>Window (Fixed: 36"w × 72"h)</b></td><td><b>Desk</b></td></tr><tr><td>CanFlipFacing</td><td>True</td><td>True</td><td>False</td></tr><tr><td>CanFlipHand</td><td>True</td><td>False</td><td>False</td></tr></tbody></table>

If CanFlipFacing or CanFlipHand is true, you can call the flipFacing() or flipHand() methods respectively. These methods can change the facing orientation or hand orientation respectively. Otherwise, the methods do nothing and return False.

When changing orientation, remember that some types of windows can change both hand orientation and facing orientation, such as a Casement 3x3 with Trim family.

There are four different facing orientation and hand orientation combinations for doors. See the following picture for the combinations and the corresponding Boolean values are in the following table.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-AC8B1DB7-860B-46D3-A0BD-DBF120980580-low.png)**Figure 44: Doors with different Facing and Hand Orientations**

**Table 30: Different Instances of the Same Type**

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_53EE227C6EAD4D4E8E1EC76AD87D8D6E"><tbody><tr><td><b>Boolean Property</b></td><td><b>Door 1</b></td><td><b>Door 2</b></td><td><b>Door 3</b></td><td><b>Door 4</b></td></tr><tr><td>FacingFlipped</td><td>False</td><td>True</td><td>False</td><td>True</td></tr><tr><td>HandFlipped</td><td>False</td><td>True</td><td>True</td><td>False</td></tr></tbody></table>

#### Orientation - Work Plane

The work plane orientation for a FamilyInstance can be changed, as well. If CanFlipWorkPlane is true, you can set the IsWorkPlaneFlipped property. Attempting to set this property for a FamilyInstance that does not allow the work plane to be flipped will result in an exception.

#### Rotation - Mirrored

The Mirrored property indicates whether the FamilyInstance object has been mirrored.

**Table 31: Door Mirrored Property**

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_836BD5C4044E42CC828DE4947CEE0260"><tbody><tr><td><b>Boolean Property</b></td><td><b>Door 1</b></td><td><b>Door 2</b></td><td><b>Door 3</b></td><td><b>Door 4</b></td></tr><tr><td>Mirrored</td><td>False</td><td>False</td><td>True</td><td>True</td></tr></tbody></table>

In the previous door example, the Mirrored property for Door 1 and Door 2 is False, while for both Door 3 and Door 4 it is True. This is because when you create a door in the Revit project, the default result is either Door 1 or Door 2. To create a door like Door 3 or Door 4, you must flip the Door 1 and Door 2 hand orientation respectively. The flip operation is like a mirror transformation, which is why the Door 3 and Door 4 Mirrored property is True.

For more information about using the Mirror() method in Revit, refer to the [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html) chapter.

#### Rotation - CanRotate and rotate()

The family instance Boolean CanRotate property is used to test whether the family instance can be rotated 180 degrees. This depends on the family to which the instance belongs. For example, in the following picture, the CanRotate properties for Window 1 (Casement 3×3 with Trim: 36"×72") and Door 1 (Double-Glass 2: 72"×82") are true, while Window 2 (Fixed: 36"w × 72"h) is false.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-8E93FD79-81F8-4B3D-B09F-9C9A4A1A556C-low.png)**Figure 45: Changes after rotate()**

If CanRotate is true, you can call the family instance rotate() method, which flips the family instance by 180 degrees. Otherwise, the method does nothing and returns False. The previous picture also shows the Window 1 and Door 1 states after executing the rotate() method.

Recall from the [Rotating elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Rotating_elements_html) section earlier in this document, that family instances (and other elements) can be rotated a user-specified angle usingElementTransformUtils.RotateElement() and ElementTransformUtils.RotateElements().

#### Location

The Location property determines the physical location of an instance in a project. An instance can have a point location or a line location.

The following characteristics apply to Location:

-   A point location is a LocationPoint class object - A footing, a door, or a table has a point location
    
-   A line location is a LocationCurve class object - A beam has a line location.
    
-   They are both subclasses of the Location class.
    

For more information about Location, refer to [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html).

### Host and HostFace

Host and HostFace are both FamilyInstance properties.

#### Host

A FamilyInstance object has a Host property that returns its hosting element.

Some FamilyInstance objects do not have host elements, such as Tables and other furniture, so the Host property returns nothing because no host elements are created. However, other objects, such as doors and windows, must have host elements. In this case the Host property returns a wall Element in which the window or the door is located. See the following picture.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-837ECA51-19DE-4B19-A304-A5C26F24EBD0-low.png)**Figure 46: Doors and windows hosted in a wall**

HostFace The HostFace property gets the reference to the host face of the family instance, or if the instance is placed on a work plane, the reference to the geometry face underlying the work plane. This property will return a null reference if the work plane is not referencing other geometry, or if the instance is not hosted on a face or work plane.

### Subcomponent and Supercomponent

The FamilyInstance.GetSubComponentIds() method returns the ElementIds of family instances loaded into that family. When an instance of 'Table-Dining Round w Chairs.rfa' is placed in a project, the ElementIds of the set of chairs are returned by the GetSubComponentIds() method.

The SuperComponent property returns the family instance's parent component. In 'Table-Dining Round w Chairs.rfa', the family instance supercomponent for each nested chair is the instance of 'Table-Dining Round w Chairs.rfa'.

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_5421C731BF84459E860D8DA820244CCA"><tbody><tr><td><b>Code Region 12-1: Getting SubComponents and SuperComponent from FamilyInstance</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetSubAndSuperComponents</span><span>(</span><span>FamilyInstance</span><span> familyInstance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> subElemSet </span><span>=</span><span> familyInstance</span><span>.</span><span>GetSubComponentIds</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>subElemSet </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>string</span><span> subElems </span><span>=</span><span> </span><span>""</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> ee </span><span>in</span><span> subElemSet</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FamilyInstance</span><span> f </span><span>=</span><span> familyInstance</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>ee</span><span>)</span><span> </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
            subElems </span><span>=</span><span> subElems </span><span>+</span><span> f</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Subcomponent count = "</span><span> </span><span>+</span><span> subElemSet</span><span>.</span><span>Count</span><span> </span><span>+</span><span> </span><span>"\n"</span><span> </span><span>+</span><span> subElems</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>FamilyInstance</span><span> </span><span>super</span><span> </span><span>=</span><span> familyInstance</span><span>.</span><span>SuperComponent</span><span> </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>super</span><span> </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"SUPER component: "</span><span> </span><span>+</span><span> </span><span>super</span><span>.</span><span>Name</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Geometry

Sometimes the geometry of a FamilyInstance object is modified by joins, cuts, coping, extensions, or other post-processing that occurs in Revit. The FamilyInstance.HasModifiedGeometry() method identifies if the geometry of this FamilyInstance has been modified from the automatically generated default. The GetOriginalGeometry() method will return the original geometry of the instance prior to any modifications that may have occurred. To get the current geometry of the instance, use the Geometry property inherited from the Element class.

### Spatial Element Calculation Points

The FamilyInstance has several members for reading the information about spatial calculation point(s) directly from the family instance. The HasSpatialElementCalculationPoint property identifies if this instance has a single SpatialElementCalculationPoint used as the search point for Revit to identify if the instance is inside a room or space. If true, the GetSpatialElementCalculationPoint() method will return the location of the calculation point for this instance as an XYZ point.

The HasSpatialElementFromToCalculationPoints property identifies if this instance has a pair of SpatialElementCalculationPoints used as the search points for Revit to identify if the instance lies between up to two rooms or spaces. The points determine which room or space is considered the "from" and which is considered the "to" for a family instance which connects two rooms or spaces, such as a door or window. When this property is true, the GetSpatialElementFromToCalculationPoints() method returns the locations for the calculation points for this instance as a list of XYZ points.

### Other Properties

The properties in this section are specific to the architectural and structural engineering features of Revit. They are covered thoroughly in their respective chapters.

#### Room Information

FamilyInstance properties include Room, FromRoom, and ToRoom. For more information about Room, refer to [Architecture](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Architecture_html).

#### Space Information

FamilyInstance has a Space property for identifying the space that holds an instance in MEP.

#### Structural Analytical Model

The GetAnalyticalModel() method retrieves the family instance structural analytical model.

For more information about AnalyticalModel refer to [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html).

### Creating FamilyInstance Objects

Typically a FamilyInstance object is created using one of the twelve overload methods of Autodesk.Revit.Creation.Document called NewFamilyInstance(). The choice of which overload to use depends not only on the category of the instance, but also other characteristics of the placement like whether it should be hosted, placed relative to a reference level, or placed directly on a particular face. The details are included in Table 32 - Options for creating instance with NewFamilyInstance() below.

Some FamilyInstance objects require more than one location to be created. In these cases, it is more appropriate to use the more detailed creation method provided by this object (see Table 33 - Options for creating instances with other methods below). If the instance is not created, an exception is thrown. The type/symbol used must be loaded into the project before the method is called.

All overloads for NewFamilyInstance() check to ensure that the input FamilySymbol is active (FamilySymbol.IsActive). If the input FamilySymbol is inactive, the method will throw an ArgumentException. Symbols that are not used in the document may be deactivated to conserve memory and regeneration time. When the symbol is inactive, its geometry is empty and cannot be accessed. In order to access the geometry of a symbol that is not active in the document, the symbol should first be activated by calling FamilySymbol.Activate().

**Table 32 - Options for creating instance with NewFamilyInstance()**

| Category | NewFamilyInstance() parameters | Comments |
| --- | --- | --- |
| Air Terminals
Boundary Conditions

Casework

Communication Devices

Data Devices

Electrical Equipment

Electrical Fixtures

Entourage

Fire Alarm Devices

Furniture

Furniture Systems

Generic Models

Lighting Devices

Lighting Fixtures

Mass

Mechanical Equipment

Nurse Call Devices

Parking

Planting

Plumbing Fixtures

Security Devices

Site

Specialty Equipment

Sprinklers

Structural Connections

Structural Foundations

Structural Stiffeners

Telephone Devices

 | XYZ, FamilySymbol, StructuralType | Creates the instance in an arbitrary location without reference to a level or host element. |
| XYZ, FamilySymbol, Element, StructuralType | If it is to be hosted on a wall, floor or ceiling |
| XYZ, FamilySymbol, XYZ, Element, StructuralType | If it is to be hosted on a wall, floor, or ceiling, and needs to be oriented in a non-default direction |
| XYZ, FamilySymbol, Element, Level, StructuralType | If it is to be hosted on a wall, floor or ceiling and associated to a reference level |
| XYZ, FamilySymbol, Level, StructuralType | If it is to be associated to a reference level |
| Face, XYZ, XYZ, FamilySymbol | If it is face-based and needs to be oriented in a non-default direction |
| Reference, XYZ, XYZ, FamilySymbol | If it is face-based and needs to be oriented in a non-default direction, accepts a reference to a face rather than a Face |
| Face, Line, FamilySymbol | If it is face-based and linear |
| Reference, Line, FamilySymbol | If it is face-based and linear, but accepts a reference to a face, rather than a Face |
| Columns

Structural Columns

 | XYZ, FamilySymbol, Level, StructuralType | Creates the column so that its base lies on the reference level. The column will extend to the next available level in the model, or will extend the default column height if there are no suitable levels above the reference level. |
| Doors

Windows

 | XYZ, FamilySymbol, Element, StructuralType | Doors and windows must be hosted by a wall. Use this method if they can be placed with the default orientation. |
| XYZ, FamilySymbol, XYZ, Element, StructuralType | If the created instance needs to be oriented in a non-default direction |
| XYZ, FamilySymbol, Element, Level, StructuralType | If the instance needs to be associated to a reference level |
| Structural Framing (Beams, Braces) | Curve, FamilySymbol, Level, StructuralType | Creates a level based brace or beam given its curve. This is the recommended method to create Beams and Braces |
| XYZ, FamilySymbol, StructuralType | Creates instance in an arbitrary location<sub id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__GUID-B882C985-E755-421D-8E90-11D3A7A18E08">1</sub> |
| XYZ, FamilySymbol, Element, Level, StructuralType | If it is hosted on an element (floor etc.) and associated to a reference level<sub id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__GUID-C97A8C8D-95F2-409B-BC49-56A6BC147C05">1</sub> |
| XYZ, FamilySymbol, Level, StructuralType | If it is associated to a reference level<sub id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__GUID-67E647D0-AE0D-4DCD-89D0-650BE40053C4">1</sub> |
| XYZ, FamilySymbol, Element, StructuralType | If it is hosted on an element (floor etc.)<sub id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__GUID-4EC2265A-86DF-4E48-BA74-22B54662042C">1</sub> |
| Detail Component | Line, FamilySymbol, View | Applies only to 2D family line based detail symbols |
| Generic Annotations | XYZ, FamilySymbol, View | Applies only to 2D family symbols |

<sub id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__GUID-ACE8C585-6799-491F-8D93-A417B8E8CD1C">1</sub> The structural instance will be of zero-length after creation. Extend it by setting its curve (FamilyInstance.Location as LocationCurve) using LocationCurve.Curve property.

You can simplify your code and improve performance by creating more than one family instance at a time using Document.NewFamilyInstances(). This method has a single parameter, which is a list of FamilyInstanceCreationData objects describing the family instances to create.

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_9699E0DCC4A34998A166B3D7E492F468"><tbody><tr><td><b>Code Region 12-2: Batch creating family instances</b></td></tr><tr><td><pre><code><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> </span><span>BatchCreateColumns</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Level</span><span> level</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>FamilyInstanceCreationData</span><span>&gt;</span><span> fiCreationDatas </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>FamilyInstanceCreationData</span><span>&gt;();</span><span>

        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> elementSet </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>//Try to get a FamilySymbol</span><span>
        </span><span>FamilySymbol</span><span> familySymbol </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>)).</span><span>ToElements</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> collection</span><span>)</span><span>
        </span><span>{</span><span>
                familySymbol </span><span>=</span><span> e </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familySymbol</span><span>.</span><span>Category</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>"Structural Columns"</span><span> </span><span>==</span><span> familySymbol</span><span>.</span><span>Category</span><span>.</span><span>Name</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>break</span><span>;</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familySymbol</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>//Create 10 FamilyInstanceCreationData items for batch creation </span><span>
                </span><span>for</span><span> </span><span>(</span><span>int</span><span> i </span><span>=</span><span> </span><span>1</span><span>;</span><span> i </span><span>&lt;</span><span> </span><span>11</span><span>;</span><span> i</span><span>++)</span><span>
                </span><span>{</span><span>
                        XYZ location </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>i </span><span>*</span><span> </span><span>10</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>FamilyInstanceCreationData</span><span> fiCreationData </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>FamilyInstanceCreationData</span><span>(</span><span>location</span><span>,</span><span> familySymbol</span><span>,</span><span> level</span><span>,</span><span> 
                                        </span><span>StructuralType</span><span>.</span><span>Column</span><span>);</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> fiCreationData</span><span>)</span><span>
                        </span><span>{</span><span>
                                fiCreationDatas</span><span>.</span><span>Add</span><span>(</span><span>fiCreationData</span><span>);</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>

                </span><span>if</span><span> </span><span>(</span><span>fiCreationDatas</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
                        </span><span>// Create Columns</span><span>
            elementSet </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFamilyInstances2</span><span>(</span><span>fiCreationDatas</span><span>);</span><span>
        </span><span>}</span><span>
                </span><span>else</span><span>
                </span><span>{</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Batch creation failed."</span><span>);</span><span>
                </span><span>}</span><span>
    </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"No column types found."</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> elementSet</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Instances of some family types are better created through methods other than Autodesk.Revit.Creation.Document.NewFamilyInstance(). These are listed in the table below.

**Table 33 - Options for creating instances with other methods**

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_587C92BF32B044B5846AD0FD32897503"><tbody><tr><td><b>Category</b></td><td><b>Creation method</b></td><td><b>Comments</b></td></tr><tr><td>Air Terminal Tags<p>Area Load Tags</p><p>Area Tags</p><p>Casework Tags</p><p>Ceiling Tags</p><p>Communication Device Tags</p><p>Curtain Panel Tags</p><p>Data Device Tags</p><p>Detail Item Tags</p><p>Door Tags</p><p>Duct Accessory Tags</p><p>Duct Fitting Tags</p><p>Duct Tags</p><p>Electrical Equipment Tags</p><p>Electrical Fixture Tags</p><p>Fire Alarm Device Tags</p><p>Flex Duct Tags</p><p>Flex Pipe Tags</p><p>Floor Tags</p><p>Furniture System Tags</p><p>Furniture Tags</p><p>Generic Model Tags</p><p>Internal Area Load Tags</p><p>Internal Line Load Tags</p><p>Internal Point Load Tags</p><p>Keynote Tags</p><p>Lighting Device Tags</p><p>Lighting Fixture Tags</p><p>Line Load Tags</p><p>Mass Floor Tags</p><p>Mass Tags</p><p>Mechanical Equipment Tags</p><p>Nurse Call Device Tags</p><p>Parking Tags</p><p>Pipe Accessory Tags</p><p>Pipe Fitting Tags</p><p>Pipe Tags</p><p>Planting Tags</p><p>Plumbing Fixture Tags</p><p>Point Load Tags</p><p>Property Line Segment Tags</p><p>Property Tags</p><p>Railing Tags</p><p>Revision Cloud Tags</p><p>Roof Tags</p><p>Room Tags</p><p>Security Device Tags</p><p>Site Tags</p><p>Space Tags</p><p>Specialty Equipment Tags</p><p>Spinkler Tags</p><p>Stair Tags</p><p>Structural Area Reinforcement Tags</p><p>Structural Beam System Tags</p><p>Structural Column Tags</p><p>Structural Connection Tags</p><p>Structural Foundation Tags</p><p>Structural Framing Tags</p><p>Structural Path Reinforcement Tags</p><p>Structural Rebar Tags</p><p>Structural Stiffener Tags</p><p>Structural Truss Tags</p><p>Telephone Device Tags</p><p>Wall Tags</p><p>Window Tags</p><p>Wire Tag</p><p>Zone Tags</p></td><td>IndependentTag.Create(Document, ElementId, Reference, Boolean, TagMode, TagOrientation, XYZ)</td><td>TagMode should be TM_ADDBY_CATEGORY and there should be a related tag family loaded when try to create a tag, otherwise exception will be thrown</td></tr><tr><td>Material Tags</td><td>IndependentTag.Create(Document, ElementId, Reference, Boolean, TagMode, TagOrientation, XYZ)</td><td>TagMode should be TM_ADDBY_MATERIAL and there should be a material tag family loaded, otherwise exception will be thrown</td></tr><tr><td>Multi-Category Tags</td><td>IndependentTag.Create(Document, ElementId, Reference, Boolean, TagMode, TagOrientation, XYZ)</td><td>TagMode should be TM_ADDBY_MULTICATEGORY, and there should be a multi-category tag family loaded, otherwise exception will be thrown</td></tr><tr><td>Title Blocks</td><td>ViewSheet.Create(Document, ElementId)</td><td>The titleblock will be added to the newly created sheet.</td></tr></tbody></table>

Families and family symbols are loaded using the Document.LoadFamily() or Document.LoadFamilySymbol() methods. Some families, such as Beams, have more than one endpoint and are inserted in the same way as a single point instance. Once the linear family instances are inserted, their endpoints can be changed using the Element.Location property. For more information, refer to [Code Samples](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Code_Samples_html).


<!-- ===== END: Help  FamilyInstances  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Code Samples  Autodesk.md ===== -->

---
created: 2026-01-28T20:58:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Code_Samples_html
author: 
---

# Help | Code Samples | Autodesk

> ## Excerpt
> Code samples for working with Family Instances.

---
Code samples for working with Family Instances.

Review the following code samples for more information about working with Family Instances. Please note that in the NewFamilyInstance() method, a StructuralType argument is required to specify the type of the family instance to be created. Here are some examples:

**Table 34: The value of StructuralType argument in the NewFamilyInstance() method**

<table summary="" id="GUID-A452F78B-7B95-4493-899D-8A09D009F5C5__TABLE_4B2C9E355A404441B3E452343BAC24F3"><tbody><tr><td><b>Type of Family Instance</b></td><td><b>Value of StructuralType</b></td></tr><tr><td>Doors, tables, etc.</td><td>NonStructural</td></tr><tr><td>Beams</td><td>Beam</td></tr><tr><td>Braces</td><td>Brace</td></tr><tr><td>Columns</td><td>Column</td></tr><tr><td>Footings</td><td>Footing</td></tr></tbody></table>

### Create Tables

The following function demonstrates how to load a family of Tables into a Revit project and create instances from all symbols in this family.

The LoadFamily() method returns false if the specified family was previously loaded. Therefore, in the following case, do not load the family, Table-Dining Round w Chairs.rfa, before this function is called. In this example, the tables are created at Level 1 by default.

<table summary="" id="GUID-A452F78B-7B95-4493-899D-8A09D009F5C5__TABLE_CCCB052A20BB4FDF905FD5EEB09854F5"><tbody><tr><td><b>Code Region 12-3: Creating tables</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>CreateTables</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>String</span><span> fileName </span><span>=</span><span> </span><span>@</span><span>"C:\ProgramData\Autodesk\RVT 2014\Libraries\US Imperial\Furniture\Tables\Table-Dining Round w Chairs.rfa"</span><span>;</span><span>

    </span><span>// try to load family</span><span>
    </span><span>Family</span><span> family </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>document</span><span>.</span><span>LoadFamily</span><span>(</span><span>fileName</span><span>,</span><span> </span><span>out</span><span> family</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Unable to load "</span><span> </span><span>+</span><span> fileName</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Loop through table symbols and add a new table for each</span><span>
    </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> familySymbolIds </span><span>=</span><span> family</span><span>.</span><span>GetFamilySymbolIds</span><span>();</span><span>
    </span><span>double</span><span> x </span><span>=</span><span> </span><span>0.0</span><span>,</span><span> y </span><span>=</span><span> </span><span>0.0</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> familySymbolIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>FamilySymbol</span><span> symbol </span><span>=</span><span> family</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
        XYZ location </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>x</span><span>,</span><span> y</span><span>,</span><span> </span><span>10.0</span><span>);</span><span>

        </span><span>FamilyInstance</span><span> instance </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFamilyInstance</span><span>(</span><span>location</span><span>,</span><span> symbol</span><span>,</span><span> </span><span>StructuralType</span><span>.</span><span>NonStructural</span><span>);</span><span>
        x </span><span>+=</span><span> </span><span>10.0</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The result of loading the Tables family and placing one instance of each FamilySymbol:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-5FE17FC0-A248-47AE-A08A-1BBA3156193B-low.png)**Figure 47: Load family and create tables in the Revit project**

### Create a Beam

In this sample, a family symbol is loaded instead of a family, because loading a single FamilySymbol is faster than loading a Family that contains many FamilySymbols.

<table summary="" id="GUID-A452F78B-7B95-4493-899D-8A09D009F5C5__TABLE_0F194E1AB6F9406183FDBBB0C07DAE48"><tbody><tr><td><b>Code Region 12-4: Creating a beam</b></td></tr><tr><td><pre><code><span>FamilyInstance</span><span> </span><span>CreateBeam</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>

    </span><span>// get the given view's level for beam creation</span><span>
    </span><span>Level</span><span> level </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>view</span><span>.</span><span>LevelId</span><span>)</span><span> </span><span>as</span><span> </span><span>Level</span><span>;</span><span>

    </span><span>// get a family symbol</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>)).</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_StructuralFraming</span><span>);</span><span>

    </span><span>FamilySymbol</span><span> gotSymbol </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>

    </span><span>// create new beam 10' long starting at origin</span><span>
    XYZ startPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ endPoint </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>

    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> beamLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>startPoint</span><span>,</span><span> endPoint</span><span>);</span><span>

    </span><span>// create a new beam</span><span>
    </span><span>FamilyInstance</span><span> instance </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFamilyInstance</span><span>(</span><span>beamLine</span><span>,</span><span> gotSymbol</span><span>,</span><span> level</span><span>,</span><span> </span><span>StructuralType</span><span>.</span><span>Beam</span><span>);</span><span>

    </span><span>return</span><span> instance</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Create Doors

Create a long wall about 180' in length and select it before running this sample. The host object must support inserting instances; otherwise the NewFamilyInstance() method will fail. If a host element is not provided for an instance that must be created in a host, or the instance cannot be inserted into the specified host element, the method NewFamilyInstance() does nothing.

<table summary="" id="GUID-A452F78B-7B95-4493-899D-8A09D009F5C5__TABLE_5592C01551724E6984533F0AF3B62C54"><tbody><tr><td><b>Code Region 12-5: Creating doors</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>CreateDoorsInWall</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// get wall's level for door creation</span><span>
    </span><span>Level</span><span> level </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>wall</span><span>.</span><span>LevelId</span><span>)</span><span> </span><span>as</span><span> </span><span>Level</span><span>;</span><span>

    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>))</span><span>
                                                </span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Doors</span><span>)</span><span>
                                                </span><span>.</span><span>ToElements</span><span>();</span><span>
    </span><span>IEnumerator</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> symbolItor </span><span>=</span><span> collection</span><span>.</span><span>GetEnumerator</span><span>();</span><span>

    </span><span>double</span><span> x </span><span>=</span><span> </span><span>0</span><span>,</span><span> y </span><span>=</span><span> </span><span>0</span><span>,</span><span> z </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>while</span><span> </span><span>(</span><span>symbolItor</span><span>.</span><span>MoveNext</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>FamilySymbol</span><span> symbol </span><span>=</span><span> symbolItor</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
        XYZ location </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>x</span><span>,</span><span> y</span><span>,</span><span> z</span><span>);</span><span>
        </span><span>FamilyInstance</span><span> instance </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFamilyInstance</span><span>(</span><span>location</span><span>,</span><span> symbol</span><span>,</span><span> wall</span><span>,</span><span> level</span><span>,</span><span> </span><span>StructuralType</span><span>.</span><span>NonStructural</span><span>);</span><span>
        x </span><span>+=</span><span> </span><span>10</span><span>;</span><span>
        y </span><span>+=</span><span> </span><span>10</span><span>;</span><span>
        z </span><span>+=</span><span> </span><span>1.5</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The result of the previous code in Revit is shown in the following picture. Notice that if the specified location is not at the specified level, the NewFamilyInstance() method uses the location elevation instead of the level elevation.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-3175405A-CD58-4A39-8DC8-696E76652DBB-low.png)Figure 48: Insert doors into a wall

### Create FamilyInstances Using Reference Directions

Use reference directions to insert an item in a specific direction.

<table summary="" id="GUID-A452F78B-7B95-4493-899D-8A09D009F5C5__TABLE_C986FBDF6F0949709645D46A44A8B99C"><tbody><tr><td><b>Code Region 12-6: Creating FamilyInstances using reference directions</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateWithRefDir</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get a floor to place the beds</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>Floor</span><span> floor </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Floor</span><span>)).</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>Floor</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>floor </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Find a Bed-Box family</span><span>
        </span><span>Family</span><span> family </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>FilteredElementCollector</span><span> famCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        famCollector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Family</span><span>));</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> famCollector</span><span>.</span><span>ToElements</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> element </span><span>in</span><span> collection</span><span>)</span><span>
        </span><span>{</span><span>

            </span><span>if</span><span> </span><span>(</span><span>element</span><span>.</span><span>Name</span><span>.</span><span>CompareTo</span><span>(</span><span>"Bed-Box"</span><span>)</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
            </span><span>{</span><span>
                family </span><span>=</span><span> element </span><span>as</span><span> </span><span>Family</span><span>;</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>if</span><span> </span><span>(</span><span>family </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// Enumerate the beds in the Bed-Box family</span><span>
            </span><span>FilteredElementCollector</span><span> fsCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
            </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> fsCollection </span><span>=</span><span> fsCollector</span><span>.</span><span>WherePasses</span><span>(</span><span>new</span><span> </span><span>FamilySymbolFilter</span><span>(</span><span>family</span><span>.</span><span>Id</span><span>)).</span><span>ToElements</span><span>();</span><span>
            </span><span>IEnumerator</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> symbolItor </span><span>=</span><span> fsCollection</span><span>.</span><span>GetEnumerator</span><span>();</span><span>

            </span><span>int</span><span> x </span><span>=</span><span> </span><span>0</span><span>,</span><span> y </span><span>=</span><span> </span><span>0</span><span>;</span><span>
            </span><span>int</span><span> i </span><span>=</span><span> </span><span>0</span><span>;</span><span>
            </span><span>while</span><span> </span><span>(</span><span>symbolItor</span><span>.</span><span>MoveNext</span><span>())</span><span>
            </span><span>{</span><span>
                </span><span>FamilySymbol</span><span> symbol </span><span>=</span><span> symbolItor</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
                XYZ location </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>x</span><span>,</span><span> y</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ direction </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>();</span><span>
                </span><span>switch</span><span> </span><span>(</span><span>i </span><span>%</span><span> </span><span>3</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>case</span><span> </span><span>0</span><span>:</span><span>
                        direction </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                        </span><span>break</span><span>;</span><span>
                    </span><span>case</span><span> </span><span>1</span><span>:</span><span>
                        direction </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>1</span><span>);</span><span>
                        </span><span>break</span><span>;</span><span>
                    </span><span>case</span><span> </span><span>2</span><span>:</span><span>
                        direction </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>);</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>}</span><span>
                </span><span>FamilyInstance</span><span> instance </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFamilyInstance</span><span>(</span><span>location</span><span>,</span><span> symbol</span><span>,</span><span> direction</span><span>,</span><span> floor</span><span>,</span><span> </span><span>StructuralType</span><span>.</span><span>NonStructural</span><span>);</span><span>
                x </span><span>+=</span><span> </span><span>10</span><span>;</span><span>
                i</span><span>++;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The result of the previous code appears in the following picture:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-86B0A1C3-988D-4C4B-BA8E-3C8C9BDEAAE0-low.png)**Figure 49: Create family instances using different reference directions**


<!-- ===== END: Help  Code Samples  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  FamilySymbol  Autodesk.md ===== -->

---
created: 2026-01-28T20:58:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_FamilySymbol_html
author: 
---

# Help | FamilySymbol | Autodesk

> ## Excerpt
> The FamilySymbol class represents a single Type within a Family.

---
The FamilySymbol class represents a single Type within a Family.

Each family can contain one or more family symbols. Each FamilyInstance has an associated FamilySymbol which can be accessed from its Symbol property.

### Thermal Properties

Certain types of families (doors, windows, and curtain wall panels) contain thermal properties as shown in the Type Properties window below for a window.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/FamilyThermalProperties2-76173.jpg)The thermal properties for a FamilySymbol are represented by the FamilyThermalProperties class and are retrieved using the FamilySymbol.GetThermalProperties() method. The FamilyThermalProperties for a FamilySymbol can be set using SetThermalProperties(). The properties of the FamilyThermalProperties class itself are read-only.

The units for the calculated values are shown in the table below.

<table summary="" id="GUID-F3F98CE6-4009-4046-BCA1-A7899CAB625C__TABLE_BB97EDC937124B74A3749A88B15045D6"><tbody><tr><td><b>Property</b></td><td><b>Unit</b></td></tr><tr><td>HeatTransferCoefficient</td><td>watts per meter-squared kelvin<p>(W/(m^2*K)</p></td></tr><tr><td>ThermalResistance</td><td>meter-squared kelvin per watt<p>((m^2*K)/Watt)</p></td></tr></tbody></table>

The AnalyticConstructionTypeId property is the construction gbXML type and returns the value that corresponds to the 'id' property of a constructionType node in Constructions.xml. The static FamilyThermalProperties.Find() method will find the FamilyThermalProperties by the 'id' property of a constructionType node in Constructions.xml.

### FamilyType Parameters

Some parameters for a FamilySymbol may be FamilyType parameters. For these parameters, the Family.GetFamilyTypeParameterValues() method can be used to get all applicable values for the parameter. The values returned are ElementIds of all family types that match the category specified by the definition of the given parameter. The elements are either of class ElementType or NestedFamilyTypeReference. The second variant is for the types that are nested in families and therefore not accessible otherwise. The NestedFamilyTypeReference element stores only basic information about the nested FamilyType, such as the name of the Type, name of the Family, and a Category. These elements are very low-level and thus bypassed by standard element filters, so the main way to get them is via the Family.GetFamilyTypeParameterValues() method.

The following example demonstrates how to get all the family type parameter values for a FamilyType parameter of a FamilySymbol. The value for the parameter is then changed to another value. This change affects all FamilyInstances using the loaded FamilySymbol.

<table summary="" id="GUID-F3F98CE6-4009-4046-BCA1-A7899CAB625C__TABLE_5421C731BF84459E860D8DA820244CCA"><tbody><tr><td><b>Code Region: Get nested FamilyTypes</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetNestedFamilyTypes</span><span>(</span><span>FamilyInstance</span><span> instance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// find one FamilyType parameter and all values applicable to it</span><span>
    </span><span>Parameter</span><span> aTypeParam </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> values </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>Family</span><span> family </span><span>=</span><span> instance</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>Parameter</span><span> param </span><span>in</span><span> instance</span><span>.</span><span>Symbol</span><span>.</span><span>Parameters</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>ForgeTypeId</span><span> forgeTypeId </span><span>=</span><span> param</span><span>.</span><span>Definition</span><span>.</span><span>GetDataType</span><span>();</span><span>
        </span><span>if</span><span> </span><span>(</span><span>Category</span><span>.</span><span>IsBuiltInCategory</span><span>(</span><span>forgeTypeId</span><span>))</span><span>
        </span><span>{</span><span>
            aTypeParam </span><span>=</span><span> param</span><span>;</span><span>
            values </span><span>=</span><span> family</span><span>.</span><span>GetFamilyTypeParameterValues</span><span>(</span><span>param</span><span>.</span><span>Id</span><span>);</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>if</span><span> </span><span>(</span><span>aTypeParam </span><span>==</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Warning"</span><span>,</span><span> </span><span>"The selected family has no FamilyType parameter defined."</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>values </span><span>==</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"A FamilyType parameter does not have any applicable values!?"</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>ElementId</span><span> newValue </span><span>=</span><span> values</span><span>.</span><span>Last</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
        </span><span>if</span><span> </span><span>(</span><span>newValue </span><span>!=</span><span> aTypeParam</span><span>.</span><span>AsElementId</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>instance</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Setting parameter value"</span><span>))</span><span>
            </span><span>{</span><span>
                trans</span><span>.</span><span>Start</span><span>();</span><span>
                aTypeParam</span><span>.</span><span>Set</span><span>(</span><span>newValue</span><span>);</span><span>
                trans</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  FamilySymbol  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Family Documents  Autodesk.md ===== -->

---
created: 2026-01-28T20:58:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_html
author: 
---

# Help | Family Documents | Autodesk

> ## Excerpt
> This section discusses families and how to:

---
This section discusses families and how to:

-   Create and modify Family documents
-   Access family types and parameters


<!-- ===== END: Help  Family Documents  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  About family documents  Autodesk.md ===== -->

---
created: 2026-01-28T20:58:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_About_family_documents_html
author: 
---

# Help | About family documents | Autodesk

> ## Excerpt
> The Family object represents an entire Revit family. A Family Document is a Document that represents a Family rather than a Revit project.

---
### Family

The Family object represents an entire Revit family. A Family Document is a Document that represents a Family rather than a Revit project.

Using the Family Creation functionality of the Revit API, you can create and edit families and their types. This functionality is particularly useful when you have pre-existing data available from an external system that you want to convert to a Revit family library.

API access to system family editing is not available.

### Categories

As noted in the previous section, the Family.FamilyCategory property indicates the category of the Family such as Columns, Furniture, Structural Framing, or Windows.

The following code can be used to determine the category of the family in an open Revit Family document.

<table summary="" id="GUID-DC143EB8-43CB-48AB-938E-7ADE3A9D2E63__TABLE_B6FD7EC439184ADBA192B4D5489B8B33"><tbody><tr><td><b>Code Region 13-1: Category of open Revit Family Document</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetName</span><span>(</span><span>Document</span><span> familyDoc</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>string</span><span> categoryName </span><span>=</span><span> familyDoc</span><span>.</span><span>OwnerFamily</span><span>.</span><span>FamilyCategory</span><span>.</span><span>Name</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The FamilyCategory can also be set, allowing the category of a family that is being edited to be changed.

### Parameters

Family parameters can be accessed from the OwnerFamily property of a Family Document as the following example shows.

<table summary="" id="GUID-DC143EB8-43CB-48AB-938E-7ADE3A9D2E63__TABLE_F1CC348A35C04D17A2CFC7F39639E941"><tbody><tr><td><b>Code Region 13-2: Category of open Revit Family Document</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetFamilyDocumentCategory</span><span>(</span><span>Document</span><span> familyDoc</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// get the owner family of the family document.</span><span>
        </span><span>Family</span><span> family </span><span>=</span><span> familyDoc</span><span>.</span><span>OwnerFamily</span><span>;</span><span> 
        </span><span>Parameter</span><span> param </span><span>=</span><span> family</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>FamilyWorkPlaneBased</span><span>);</span><span>
        </span><span>// this param is a Yes/No parameter in UI, but an integer value in API</span><span>
        </span><span>// 1 for true and 0 for false</span><span>
        </span><span>int</span><span> isTrue </span><span>=</span><span> param</span><span>.</span><span>AsInteger</span><span>();</span><span> 
        </span><span>// param.Set(1); // set value to true.</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Creating a Family Document

The ability to modify Revit Family documents and access family types and parameters is available from the Document class if the Document is a Family document, as determined by the IsFamilyDocument property. To edit an existing family while working in a Project document, use the EditFamily() functions available from the Document class, and then use LoadFamily() to reload the family back into the owner document after editing is complete. To create a new family document use Application.NewFamilyDocument():

<table summary="" id="GUID-DC143EB8-43CB-48AB-938E-7ADE3A9D2E63__TABLE_C37ED16E984740C4A6727147592EB25D"><tbody><tr><td><b>Code Region 13-3: Creating a new Family document</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateFamily</span><span>(</span><span>Application</span><span> application</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// create a new family document using Generic Model.rft template</span><span>
        </span><span>string</span><span> templateFileName </span><span>=</span><span> </span><span>@</span><span>"C:\Documents and Settings\All Users\Application Data\Autodesk\RST 2011\Imperial Templates\Generic Model.rft"</span><span>;</span><span>

        </span><span>Document</span><span> familyDocument </span><span>=</span><span> application</span><span>.</span><span>NewFamilyDocument</span><span>(</span><span>templateFileName</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> familyDocument</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Cannot open family document"</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Nested Family Symbols

You can filter a Family Document for FamilySymbols to get all of the FamilySymbols loaded into the Family. In this code sample, all the nested FamilySymbols in the Family for a given FamilyInstance are listed.

<table summary="" id="GUID-DC143EB8-43CB-48AB-938E-7ADE3A9D2E63__TABLE_2EBB4BE77E4C4D0E890F1236C7290DFC"><tbody><tr><td><b>Code Region 13-4: Getting nested Family symbols in a Family</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetLoadedSymbols</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> familyInstance</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familyInstance</span><span>.</span><span>Symbol</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Get family associated with this</span><span>
                </span><span>Family</span><span> family </span><span>=</span><span> familyInstance</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>

                </span><span>// Get Family document for family</span><span>
                </span><span>Document</span><span> familyDoc </span><span>=</span><span> document</span><span>.</span><span>EditFamily</span><span>(</span><span>family</span><span>);</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familyDoc </span><span>&amp;&amp;</span><span> familyDoc</span><span>.</span><span>IsFamilyDocument</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>String</span><span> loadedFamilies </span><span>=</span><span> </span><span>"FamilySymbols in "</span><span> </span><span>+</span><span> family</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>":\n"</span><span>;</span><span>
                        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
                        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> 
                                collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>)).</span><span>ToElements</span><span>();</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> collection</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>FamilySymbol</span><span> fs </span><span>=</span><span> e </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
                                loadedFamilies </span><span>+=</span><span> </span><span>"\t"</span><span> </span><span>+</span><span> fs</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
                        </span><span>}</span><span>

                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>loadedFamilies</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  About family documents  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Creating elements in families  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:02 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_Creating_elements_in_families_html
author: 
---

# Help | Creating elements in families | Autodesk

> ## Excerpt
> Share

---
Share

The FamilyItemFactory class provides the ability to create elements in family documents. It is accessed through the Document.FamilyCreate property. FamilyItemFactory is derived from the ItemFactoryBase class which is a utility to create elements in both Revit project documents and family documents.

**Pages in this section**

-   [Create a form element](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_Creating_elements_in_families_Create_a_form_element_html)
-   [Create an annotation](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_Creating_elements_in_families_Create_an_annotation_html)

**Parent page:** [Family Documents](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_html)

### Was this information helpful?

-   Yes
-   No


<!-- ===== END: Help  Creating elements in families  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Create a form element  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:07 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_Creating_elements_in_families_Create_a_form_element_html
author: 
---

# Help | Create a form element | Autodesk

> ## Excerpt
> The FamilyItemFactory class provides the ability to create form elements in families, such as extrusions, revolutions, sweeps, and blends. See the section on 3D Sketch for more information on these 3D sketch forms.

---
The FamilyItemFactory class provides the ability to create form elements in families, such as extrusions, revolutions, sweeps, and blends. See the section on [3D Sketch](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_3D_Sketch_html) for more information on these 3D sketch forms.

The following example demonstrates how to create a new Extrusion element. It creates a simple rectangular profile and then moves the newly created Extrusion to a new location.

<table summary="" id="GUID-FBF9B994-ADCB-4679-B50B-2E9A1E09AA48__TABLE_21A660DE8C3548309D47015C25B61CCD"><tbody><tr><td><b>Code Region: Creating a new Extrusion</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Extrusion</span><span> </span><span>CreateExtrusion</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>SketchPlane</span><span> sketchPlane</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Extrusion</span><span> rectExtrusion </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// make sure we have a family document</span><span>
    </span><span>if</span><span> </span><span>(</span><span>true</span><span> </span><span>==</span><span> document</span><span>.</span><span>IsFamilyDocument</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// define the profile for the extrusion</span><span>
        </span><span>CurveArrArray</span><span> curveArrArray </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArrArray</span><span>();</span><span>
        </span><span>CurveArray</span><span> curveArray1 </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>
        </span><span>CurveArray</span><span> curveArray2 </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>
        </span><span>CurveArray</span><span> curveArray3 </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>

        </span><span>// create a rectangular profile</span><span>
        XYZ p0 </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
        XYZ p1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ p2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ p3 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        </span><span>Line</span><span> line1 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p0</span><span>,</span><span> p1</span><span>);</span><span>
        </span><span>Line</span><span> line2 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p1</span><span>,</span><span> p2</span><span>);</span><span>
        </span><span>Line</span><span> line3 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p2</span><span>,</span><span> p3</span><span>);</span><span>
        </span><span>Line</span><span> line4 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p3</span><span>,</span><span> p0</span><span>);</span><span>
        curveArray1</span><span>.</span><span>Append</span><span>(</span><span>line1</span><span>);</span><span>
        curveArray1</span><span>.</span><span>Append</span><span>(</span><span>line2</span><span>);</span><span>
        curveArray1</span><span>.</span><span>Append</span><span>(</span><span>line3</span><span>);</span><span>
        curveArray1</span><span>.</span><span>Append</span><span>(</span><span>line4</span><span>);</span><span>

        curveArrArray</span><span>.</span><span>Append</span><span>(</span><span>curveArray1</span><span>);</span><span>

        </span><span>// create solid rectangular extrusion</span><span>
        rectExtrusion </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewExtrusion</span><span>(</span><span>true</span><span>,</span><span> curveArrArray</span><span>,</span><span> sketchPlane</span><span>,</span><span> </span><span>10</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> rectExtrusion</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// move extrusion to proper place</span><span>
            XYZ transPoint1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>16</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            </span><span>ElementTransformUtils</span><span>.</span><span>MoveElement</span><span>(</span><span>document</span><span>,</span><span> rectExtrusion</span><span>.</span><span>Id</span><span>,</span><span> transPoint1</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create new Extrusion failed."</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Please open a Family document before invoking this command."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> rectExtrusion</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following sample shows how to create a new Sweep from a solid ovoid profile in a Family Document.

<table summary="" id="GUID-FBF9B994-ADCB-4679-B50B-2E9A1E09AA48__TABLE_4FB266F3F8BA46A093E6C4D0F40CACB7"><tbody><tr><td><b>Code Region: Creating a new Sweep</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Sweep</span><span> </span><span>CreateSweep</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>SketchPlane</span><span> sketchPlane</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Sweep</span><span> sweep </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// make sure we have a family document</span><span>
    </span><span>if</span><span> </span><span>(</span><span>true</span><span> </span><span>==</span><span> document</span><span>.</span><span>IsFamilyDocument</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Define a profile for the sweep</span><span>
        </span><span>CurveArrArray</span><span> arrarr </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArrArray</span><span>();</span><span>
        </span><span>CurveArray</span><span> arr </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>

        </span><span>// Create an ovoid profile</span><span>
        XYZ pnt1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ pnt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>2</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ pnt3 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        arr</span><span>.</span><span>Append</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>pnt2</span><span>,</span><span> </span><span>1.0d</span><span>,</span><span> </span><span>0.0d</span><span>,</span><span> </span><span>180.0d</span><span>,</span><span> XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> XYZ</span><span>.</span><span>BasisY</span><span>));</span><span>
        arr</span><span>.</span><span>Append</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>pnt1</span><span>,</span><span> pnt3</span><span>,</span><span> pnt2</span><span>));</span><span>
        arrarr</span><span>.</span><span>Append</span><span>(</span><span>arr</span><span>);</span><span>
        </span><span>SweepProfile</span><span> profile </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewCurveLoopsProfile</span><span>(</span><span>arrarr</span><span>);</span><span>

        </span><span>// Create a path for the sweep</span><span>
        XYZ pnt4 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ pnt5 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        </span><span>Curve</span><span> curve </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pnt4</span><span>,</span><span> pnt5</span><span>);</span><span>

        </span><span>CurveArray</span><span> curves </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>
        curves</span><span>.</span><span>Append</span><span>(</span><span>curve</span><span>);</span><span>

        </span><span>// create a solid ovoid sweep</span><span>
        sweep </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewSweep</span><span>(</span><span>true</span><span>,</span><span> curves</span><span>,</span><span> sketchPlane</span><span>,</span><span> profile</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>ProfilePlaneLocation</span><span>.</span><span>Start</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> sweep</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// move to proper place</span><span>
            XYZ transPoint1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>11</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            </span><span>ElementTransformUtils</span><span>.</span><span>MoveElement</span><span>(</span><span>document</span><span>,</span><span> sweep</span><span>.</span><span>Id</span><span>,</span><span> transPoint1</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Failed to create a new Sweep."</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Please open a Family document before invoking this command."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> sweep</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

!\[\](../../../../images/GUID-169B9078-7508-4982-B10D-333FF97CA345-low.png)

**Figure 50: Ovoid sweep created by previous example**

The FreeFormElement class allows for the creation of non-parametric geometry created from an input solid outline. A FreeFormElement can participate in joins and void cuts with other combinable elements. Planar faces of the element can be offset interactively and programmatically in the face normal direction.

### Assigning Subcategories to forms

After creating a new form in a family, you may want to change the subcategory for the form. For example, you may have a Door family and want to create multiple subcategories of doors and assign different subcategories to different door types in your family.

The following example shows how to create a new subcategory, assign it a material, and then assign the subcategory to a form.

<table summary="" id="GUID-FBF9B994-ADCB-4679-B50B-2E9A1E09AA48__TABLE_9321DBB7592F4F1B9D92D156C09A5409"><tbody><tr><td><b>Code Region: Assigning a subcategory</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>AssignSubCategory</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>GenericForm</span><span> extrusion</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// create a new subcategory</span><span>
    </span><span>Category</span><span> cat </span><span>=</span><span> document</span><span>.</span><span>OwnerFamily</span><span>.</span><span>FamilyCategory</span><span>;</span><span>
    </span><span>Category</span><span> subCat </span><span>=</span><span> document</span><span>.</span><span>Settings</span><span>.</span><span>Categories</span><span>.</span><span>NewSubcategory</span><span>(</span><span>cat</span><span>,</span><span> </span><span>"NewSubCat"</span><span>);</span><span>

    </span><span>// create a new material and assign it to the subcategory</span><span>
    </span><span>ElementId</span><span> materialId </span><span>=</span><span> </span><span>Material</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Wood Material"</span><span>);</span><span>
    subCat</span><span>.</span><span>Material</span><span> </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>materialId</span><span>)</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>

    </span><span>// assign the subcategory to the element</span><span>
    extrusion</span><span>.</span><span>Subcategory</span><span> </span><span>=</span><span> subCat</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Create a form element  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Create an annotation  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:12 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_Creating_elements_in_families_Create_an_annotation_html
author: 
---

# Help | Create an annotation | Autodesk

> ## Excerpt
> New annotations such as Dimensions and ModelText and TextNote objects can also be created in families, as well as curve annotation elements such as SymbolicCurve, ModelCurve, and DetailCurve. See Annotation Elements for more information on Annotation elements.

---
New annotations such as Dimensions and ModelText and TextNote objects can also be created in families, as well as curve annotation elements such as SymbolicCurve, ModelCurve, and DetailCurve. See [Annotation Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_html) for more information on Annotation elements.

Additionally, a new Alignment can be added, referencing a View that determines the orientation of the alignment, and two geometry references.

The following example demonstrates how to create a new arc length Dimension.

<table summary="" id="GUID-01EE5DD8-6C69-41DB-BBCA-C5C624E826CB__TABLE_954B297407434A96A5A0F1364C67961B"><tbody><tr><td><b>Code Region: Creating a Dimension</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Dimension</span><span> </span><span>CreateArcDimension</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>SketchPlane</span><span> sketchPlane</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>Application</span><span> appCreate </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>;</span><span>
    </span><span>Line</span><span> gLine1 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>2</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    </span><span>Line</span><span> gLine2 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>2</span><span>,</span><span> </span><span>4</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    </span><span>Arc</span><span> arctoDim </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>1</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>3</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    </span><span>Arc</span><span> arcofDim </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>3</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0.8</span><span>,</span><span> </span><span>2.8</span><span>,</span><span> </span><span>0</span><span>));</span><span>

    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>FamilyItemFactory</span><span> creationFamily </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>;</span><span>
    </span><span>ModelCurve</span><span> modelCurve1 </span><span>=</span><span> creationFamily</span><span>.</span><span>NewModelCurve</span><span>(</span><span>gLine1</span><span>,</span><span> sketchPlane</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelCurve2 </span><span>=</span><span> creationFamily</span><span>.</span><span>NewModelCurve</span><span>(</span><span>gLine2</span><span>,</span><span> sketchPlane</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelCurve3 </span><span>=</span><span> creationFamily</span><span>.</span><span>NewModelCurve</span><span>(</span><span>arctoDim</span><span>,</span><span> sketchPlane</span><span>);</span><span>
    </span><span>//get their reference</span><span>
    </span><span>Reference</span><span> ref1 </span><span>=</span><span> modelCurve1</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>;</span><span>
    </span><span>Reference</span><span> ref2 </span><span>=</span><span> modelCurve2</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>;</span><span>
    </span><span>Reference</span><span> arcRef </span><span>=</span><span> modelCurve3</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>;</span><span>

    </span><span>Dimension</span><span> newArcDim </span><span>=</span><span> creationFamily</span><span>.</span><span>NewArcLengthDimension</span><span>(</span><span>document</span><span>.</span><span>ActiveView</span><span>,</span><span> arcofDim</span><span>,</span><span> arcRef</span><span>,</span><span> ref1</span><span>,</span><span> ref2</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>newArcDim </span><span>==</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Failed to create new arc length dimension."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> newArcDim</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

!\[\](../../../../images/GUID-813DEE5B-AD67-4892-934A-EF192F72A5BB-low.png)

**Figure 51: Resulting arc length dimension**

Some types of dimensions can be labeled with a FamilyParameter. Dimensions that cannot be labeled will throw an Autodesk.Revit.Exceptions.InvalidOperationException if you try to get or set the Label property. In the following example, a new linear dimension is created between two lines and labeled as "width".

<table summary="" id="GUID-01EE5DD8-6C69-41DB-BBCA-C5C624E826CB__TABLE_F95E9433967249F6BBC1BA5A604287A9"><tbody><tr><td><b>Code Region: Labeling a dimension</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Dimension</span><span> </span><span>CreateLinearDimension</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// first create two lines</span><span>
    XYZ pt1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>5</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ pt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pt1</span><span>,</span><span> pt2</span><span>);</span><span>
    </span><span>Plane</span><span> plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>pt1</span><span>.</span><span>CrossProduct</span><span>(</span><span>pt2</span><span>),</span><span> pt2</span><span>);</span><span>
    </span><span>SketchPlane</span><span> skplane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span> </span><span>(</span><span>document</span><span>,</span><span> plane</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelcurve1 </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewModelCurve</span><span>(</span><span>line</span><span>,</span><span> skplane</span><span>);</span><span>

    pt1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>5</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    pt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pt1</span><span>,</span><span> pt2</span><span>);</span><span>
    plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>pt1</span><span>.</span><span>CrossProduct</span><span>(</span><span>pt2</span><span>),</span><span> pt2</span><span>);</span><span>
    skplane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span> </span><span>(</span><span>document</span><span>,</span><span> plane</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelcurve2 </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewModelCurve</span><span>(</span><span>line</span><span>,</span><span> skplane</span><span>);</span><span>

    </span><span>// now create a linear dimension between them</span><span>
    </span><span>ReferenceArray</span><span> ra </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>
    ra</span><span>.</span><span>Append</span><span>(</span><span>modelcurve1</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>
    ra</span><span>.</span><span>Append</span><span>(</span><span>modelcurve2</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    pt1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    pt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pt1</span><span>,</span><span> pt2</span><span>);</span><span>

    </span><span>Dimension</span><span> dim </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewLinearDimension</span><span>(</span><span>document</span><span>.</span><span>ActiveView</span><span>,</span><span> line</span><span>,</span><span> ra</span><span>);</span><span>

    </span><span>// create a label for the dimension called "width"</span><span>
    </span><span>FamilyParameter</span><span> param </span><span>=</span><span> document</span><span>.</span><span>FamilyManager</span><span>.</span><span>AddParameter</span><span>(</span><span>"width"</span><span>,</span><span> 
        </span><span>GroupTypeId</span><span>.</span><span>Constraints</span><span>,</span><span>
        </span><span>SpecTypeId</span><span>.</span><span>Length</span><span>,</span><span> </span><span>false</span><span>);</span><span>

    dim</span><span>.</span><span>FamilyLabel</span><span> </span><span>=</span><span> param</span><span>;</span><span>

    </span><span>return</span><span> dim</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

!\[\](../../../../images/GUID-802D577E-3791-4286-A288-0B7858C6459C-low.png)

**Figure 52: Labeled linear dimension**


<!-- ===== END: Help  Create an annotation  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Visibility of family elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_Visibility_of_family_elements_html
author: 
---

# Help | Visibility of family elements | Autodesk

> ## Excerpt
> The FamilyElementVisibility class can be used to control the visibility of family elements in the project document. For example, if you have a door family, you may only want the door swing to be visible in plan views in the project document in which doors are placed, not 3D views. By setting the visibility on the curves of the door swing, you can control their visibility. FamilyElementVisibility is applicable to the following family element classes which have the SetVisibility() function:

---
The FamilyElementVisibility class can be used to control the visibility of family elements in the project document. For example, if you have a door family, you may only want the door swing to be visible in plan views in the project document in which doors are placed, not 3D views. By setting the visibility on the curves of the door swing, you can control their visibility. FamilyElementVisibility is applicable to the following family element classes which have the SetVisibility() function:

-   GenericForm, which is the base class for form classes such as Sweep and Extrusion
    
-   SymbolicCurve
    
-   ModelText
    
-   CurveByPoints
    
-   ModelCurve
    
-   ReferencePoint
    
-   ImportInstance
    

In the example below, the resulting family document will display the text "Hello World" with a line under it. When the family is loaded into a Revit project document and an instance is placed, in plan view, only the line will be visible. In 3D view, both the line and text will be displayed, unless the Detail Level is set to Course, in which case the line will disappear.

<table summary="" id="GUID-3148B66A-44F4-4D68-BDAA-0791CDD121E3__TABLE_5940D4D71B734F87AD0BE5D62C49D102"><tbody><tr><td><b>Code Region 13-10: Setting family element visibility</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateAndSetVisibility</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> familyDocument</span><span>,</span><span> </span><span>SketchPlane</span><span> sketchPlane</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// create a new ModelCurve in the family document</span><span>
    XYZ p0 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ p1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Line</span><span> line1 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p0</span><span>,</span><span> p1</span><span>);</span><span>

    </span><span>ModelCurve</span><span> modelCurve1 </span><span>=</span><span> familyDocument</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewModelCurve</span><span>(</span><span>line1</span><span>,</span><span> sketchPlane</span><span>);</span><span>

    </span><span>// create a new ModelText along ModelCurve line</span><span>
    </span><span>ModelText</span><span> text </span><span>=</span><span> familyDocument</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewModelText</span><span>(</span><span>"Hello World"</span><span>,</span><span> </span><span>null</span><span>,</span><span> sketchPlane</span><span>,</span><span> p0</span><span>,</span><span> </span><span>HorizontalAlign</span><span>.</span><span>Center</span><span>,</span><span> </span><span>0.1</span><span>);</span><span>

    </span><span>// set visibility for text</span><span>
    </span><span>FamilyElementVisibility</span><span> textVisibility </span><span>=</span><span> </span><span>new</span><span> </span><span>FamilyElementVisibility</span><span>(</span><span>FamilyElementVisibilityType</span><span>.</span><span>Model</span><span>);</span><span>
    textVisibility</span><span>.</span><span>IsShownInTopBottom</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    text</span><span>.</span><span>SetVisibility</span><span>(</span><span>textVisibility</span><span>);</span><span>

    </span><span>// set visibility for line</span><span>
    </span><span>FamilyElementVisibility</span><span> curveVisibility </span><span>=</span><span> </span><span>new</span><span> </span><span>FamilyElementVisibility</span><span>(</span><span>FamilyElementVisibilityType</span><span>.</span><span>Model</span><span>);</span><span>
    curveVisibility</span><span>.</span><span>IsShownInCoarse</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    modelCurve1</span><span>.</span><span>SetVisibility</span><span>(</span><span>curveVisibility</span><span>);</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Visibility of family elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Managing family types and parameters  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_Managing_family_types_and_parameters_html
author: 
---

# Help | Managing family types and parameters | Autodesk

> ## Excerpt
> Family documents provide access to the FamilyManager property. The FamilyManager class provides access to family types and parameters. Using this class you can add and remove types, add and remove family and shared parameters, set the value for parameters in different family types, and define formulas to drive parameter values.

---
Family documents provide access to the FamilyManager property. The FamilyManager class provides access to family types and parameters. Using this class you can add and remove types, add and remove family and shared parameters, set the value for parameters in different family types, and define formulas to drive parameter values.

### Getting Types in a Family

The FamilyManager can be used to iterate through the types in a family, as the following example demonstrates.

<table summary="" id="GUID-F57B09C0-1AFD-4BE5-8288-A187EC983797__TABLE_2945ADD5B47740C7B630C19EB1AEB007"><tbody><tr><td><b>Code Region 13-11: Getting the types in a family</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetFamilyTypesInFamily</span><span>(</span><span>Document</span><span> familyDoc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(</span><span>familyDoc</span><span>.</span><span>IsFamilyDocument</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>FamilyManager</span><span> familyManager </span><span>=</span><span> familyDoc</span><span>.</span><span>FamilyManager</span><span>;</span><span>

        </span><span>// get types in family</span><span>
        </span><span>string</span><span> types </span><span>=</span><span> </span><span>"Family Types: "</span><span>;</span><span>
        </span><span>FamilyTypeSet</span><span> familyTypes </span><span>=</span><span> familyManager</span><span>.</span><span>Types</span><span>;</span><span>
        </span><span>FamilyTypeSetIterator</span><span> familyTypesItor </span><span>=</span><span> familyTypes</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
        familyTypesItor</span><span>.</span><span>Reset</span><span>();</span><span>
        </span><span>while</span><span> </span><span>(</span><span>familyTypesItor</span><span>.</span><span>MoveNext</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>FamilyType</span><span> familyType </span><span>=</span><span> familyTypesItor</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>FamilyType</span><span>;</span><span>
            types </span><span>+=</span><span> </span><span>"\n"</span><span> </span><span>+</span><span> familyType</span><span>.</span><span>Name</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>types</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-60AB2EDC-BC4E-4E08-8922-38ECF4B7F991-low.png)**Figure 53: Family types in Concrete-Rectangular-Column family**

### Editing FamilyTypes

FamilyManager provides the ability to iterate through existing types in a family, and add and modify types and their parameters.

The following example shows how to add a new type, set its parameters and then assign the new type to a FamilyInstance. Type editing is done on the current type by using the Set() function. The current type is available from the CurrentType property. The CurrentType property can be used to set the current type before editing, or use the NewType() function which creates a new type and sets it to the current type for editing.

Note that once the new type is created and modified, Document.LoadFamily() is used to load the family back into the Revit project to make the new type available.

<table summary="" id="GUID-F57B09C0-1AFD-4BE5-8288-A187EC983797__TABLE_06358C4D5C5F41C382BE2BD5EBB8E9E9"><tbody><tr><td><b>Code Region 13-12: Editing Family Types</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>EditFamilyTypes</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> familyInstance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// example works best when familyInstance is a rectangular concrete element</span><span>

    </span><span>if</span><span> </span><span>((</span><span>null</span><span> </span><span>==</span><span> document</span><span>)</span><span> </span><span>||</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> familyInstance</span><span>.</span><span>Symbol</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>   </span><span>// invalid arguments</span><span>
    </span><span>}</span><span>

    </span><span>// Get family associated with this</span><span>
    </span><span>Family</span><span> family </span><span>=</span><span> familyInstance</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> family</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>    </span><span>// could not get the family</span><span>
    </span><span>}</span><span>

    </span><span>// Get Family document for family</span><span>
    </span><span>Document</span><span> familyDoc </span><span>=</span><span> document</span><span>.</span><span>EditFamily</span><span>(</span><span>family</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> familyDoc</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>    </span><span>// could not open a family for edit</span><span>
    </span><span>}</span><span>

    </span><span>FamilyManager</span><span> familyManager </span><span>=</span><span> familyDoc</span><span>.</span><span>FamilyManager</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> familyManager</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>  </span><span>// cuould not get a family manager</span><span>
    </span><span>}</span><span>

    </span><span>// Start transaction for the family document</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> newFamilyTypeTransaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>familyDoc</span><span>,</span><span> </span><span>"Add Type to Family"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>int</span><span> changesMade </span><span>=</span><span> </span><span>0</span><span>;</span><span>
        newFamilyTypeTransaction</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// add a new type and edit its parameters</span><span>
        </span><span>FamilyType</span><span> newFamilyType </span><span>=</span><span> familyManager</span><span>.</span><span>NewType</span><span>(</span><span>"2X2"</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>newFamilyType </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// look for 'b' and 'h' parameters and set them to 2 feet</span><span>
            </span><span>FamilyParameter</span><span> familyParam </span><span>=</span><span> familyManager</span><span>.</span><span>get_Parameter</span><span>(</span><span>"b"</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familyParam</span><span>)</span><span>
            </span><span>{</span><span>
                familyManager</span><span>.</span><span>Set</span><span>(</span><span>familyParam</span><span>,</span><span> </span><span>2.0</span><span>);</span><span>
                changesMade </span><span>+=</span><span> </span><span>1</span><span>;</span><span>
            </span><span>}</span><span>

            familyParam </span><span>=</span><span> familyManager</span><span>.</span><span>get_Parameter</span><span>(</span><span>"h"</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familyParam</span><span>)</span><span>
            </span><span>{</span><span>
                familyManager</span><span>.</span><span>Set</span><span>(</span><span>familyParam</span><span>,</span><span> </span><span>2.0</span><span>);</span><span>
                changesMade </span><span>+=</span><span> </span><span>1</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>if</span><span> </span><span>(</span><span>2</span><span> </span><span>==</span><span> changesMade</span><span>)</span><span>   </span><span>// set both paramaters?</span><span>
        </span><span>{</span><span>
            newFamilyTypeTransaction</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>   </span><span>// could not make the change -&gt; should roll back </span><span>
        </span><span>{</span><span>
            newFamilyTypeTransaction</span><span>.</span><span>RollBack</span><span>();</span><span>
        </span><span>}</span><span>

        </span><span>// if could not make the change or could not commit it, we return</span><span>
        </span><span>if</span><span> </span><span>(</span><span>newFamilyTypeTransaction</span><span>.</span><span>GetStatus</span><span>()</span><span> </span><span>!=</span><span> </span><span>TransactionStatus</span><span>.</span><span>Committed</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>return</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// now update the Revit project with Family which has a new type</span><span>
    </span><span>LoadOpts</span><span> loadOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>LoadOpts</span><span>();</span><span>

    </span><span>// This overload is necessary for reloading an edited family</span><span>
    </span><span>// back into the source document from which it was extracted</span><span>
    family </span><span>=</span><span> familyDoc</span><span>.</span><span>LoadFamily</span><span>(</span><span>document</span><span>,</span><span> loadOptions</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> family</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// find the new type and assign it to FamilyInstance</span><span>
        </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> familySymbolIds </span><span>=</span><span> family</span><span>.</span><span>GetFamilySymbolIds</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> familySymbolIds</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FamilySymbol</span><span> familySymbol </span><span>=</span><span> family</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
            </span><span>if</span><span> </span><span>((</span><span>null</span><span> </span><span>!=</span><span> familySymbol</span><span>)</span><span> </span><span>&amp;&amp;</span><span> familySymbol</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"2X2"</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> changeSymbol </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Change Symbol Assignment"</span><span>))</span><span>
                </span><span>{</span><span>
                    changeSymbol</span><span>.</span><span>Start</span><span>();</span><span>
                    familyInstance</span><span>.</span><span>Symbol</span><span> </span><span>=</span><span> familySymbol</span><span>;</span><span>
                    changeSymbol</span><span>.</span><span>Commit</span><span>();</span><span>
                </span><span>}</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>class</span><span> </span><span>LoadOpts</span><span> </span><span>:</span><span> </span><span>IFamilyLoadOptions</span><span>
</span><span>{</span><span>
    </span><span>public</span><span> </span><span>bool</span><span> </span><span>OnFamilyFound</span><span>(</span><span>bool</span><span> familyInUse</span><span>,</span><span> </span><span>out</span><span> </span><span>bool</span><span> overwriteParameterValues</span><span>)</span><span>
    </span><span>{</span><span>
        overwriteParameterValues </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>return</span><span> </span><span>true</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>bool</span><span> </span><span>OnSharedFamilyFound</span><span>(</span><span>Family</span><span> sharedFamily</span><span>,</span><span> </span><span>bool</span><span> familyInUse</span><span>,</span><span> </span><span>out</span><span> </span><span>FamilySource</span><span> source</span><span>,</span><span> </span><span>out</span><span> </span><span>bool</span><span> overwriteParameterValues</span><span>)</span><span>
    </span><span>{</span><span>
        source </span><span>=</span><span> </span><span>FamilySource</span><span>.</span><span>Family</span><span>;</span><span>
        overwriteParameterValues </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>return</span><span> </span><span>true</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The FamilyManager class provides access to all the family parameters. This includes family built-in parameters, category built-in parameters and shared parameters associated to the family types. There are two ways to get the family parameters:

-   Parameters property - gets all parameters in the family
-   GetParameters() - gets all the parameters in the family in order in which they appear in the Revit UI When using the GetParameters() method, the Revit UI order is determined first by group and next by the order of the individual parameters.

Family parameters can be reordered (within their groups) from the API for a given family (with the exception of the Rebar Shape family which does not support reordering parameters). This allows for parameters to be presented to the user in the most logical order. Sorting only affects visible parameters within the same parameter group. Parameters that belong to different groups will remain separated, and the groups' order will not be affected.

The simplest way to reorder parameters is using the FamilyManager.SortParameters() method, which takes a parameter indicating the desired sort order. The sample below sorts the parameters in ascending order.

| Code Region: Sort family parameters |
| --- |
| 
```
private void DisplayParametersInAscendingOrder(Document familyDoc)
{
    FamilyManager familyManager = familyDoc.FamilyManager;
    familyManager.SortParameters(ParametersOrder.Ascending);
}
```

 |

Note: The sort is a one-time operation. When new parameters are added they will not be automatically sorted.

For more control over how parameters are sorted, use the FamilyManager.ReorderParameters() method which takes a list of family parameters in the new order. This list must include all the parameters returned by the GetParameters() method, including any invisible parameters, or an exception will be thrown.


<!-- ===== END: Help  Managing family types and parameters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Conceptual Design  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:27 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_html
author: 
---

# Help | Conceptual Design | Autodesk

> ## Excerpt
> This chapter discusses the conceptual design functionality of the Revit API for the creation of complex geometry in a family document. Form-making is supported by the addition of new objects: points and spline curves that pass through these points. The resulting surfaces can be divided, patterned, and panelized to create buildable forms with persistent parametric relationships.

---
This chapter discusses the conceptual design functionality of the Revit API for the creation of complex geometry in a family document. Form-making is supported by the addition of new objects: points and spline curves that pass through these points. The resulting surfaces can be divided, patterned, and panelized to create buildable forms with persistent parametric relationships.

**Pages in this section**

-   [Point and curve objects](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Point_and_curve_objects_html)
-   [Forms](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Forms_html)
-   [Rationalizing a Surface](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Rationalizing_a_Surface_html)
-   [Adaptive Components](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Adaptive_Components_html)
-   [Create a .addin manifest file](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Create_a_addin_manifest_file_html)

**Parent page:** [Revit Geometric Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_html)


<!-- ===== END: Help  Conceptual Design  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Point and curve objects  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:32 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Point_and_curve_objects_html
author: 
---

# Help | Point and curve objects | Autodesk

> ## Excerpt
> A reference point is an element that specifies a location in the XYZ work space of the conceptual design environment. You create reference points to design and plot lines, splines, and forms. A ReferencePoint can be added to a ReferencePointArray, then used to create a CurveByPoints, which in turn can be used to create a form.

---
A reference point is an element that specifies a location in the XYZ work space of the conceptual design environment. You create reference points to design and plot lines, splines, and forms. A ReferencePoint can be added to a ReferencePointArray, then used to create a CurveByPoints, which in turn can be used to create a form.

The following example demonstrates how to create a CurveByPoints object. See the "Creating a loft form" example in the next section to see how to create a form from multiple CurveByPoints objects.

<table summary="" id="GUID-B3D21FAA-9A8C-4E77-A019-D2E8439B473F__TABLE_5C3183FF19444C16A6E2D6E12EE80288"><tbody><tr><td><b>Code Region 14-1: Creating a new CurveByPoints</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateCurve</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ReferencePointArray</span><span> rpa </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferencePointArray</span><span>();</span><span>

    XYZ xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>ReferencePoint</span><span> rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
    rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

    xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>30</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
    rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

    xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>60</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
    rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

    xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>30</span><span>);</span><span>
    rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
    rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

    xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>150</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
    rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

    </span><span>CurveByPoints</span><span> curve </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpa</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-91A84A22-3B88-45F4-B7CE-8D75F685A95A-low.png)**Figure 54: CurveByPoints curve**

Reference points can be created based on XYZ coordinates as in the example above, or they can be created relative to other geometry so that the points will move when the referenced geometry changes. These points are created using the subclasses of the PointElementReference class. The subclasses are:

-   PointOnEdge
-   PointOnEdgeEdgeIntersection
-   PointOnEdgeFaceIntersection
-   PointOnFace
-   PointOnPlane

For example, the last two lines of code in the previous example create a reference point in the middle of the CurveByPoints.

Forms can be created using model lines or reference lines. Model lines are "consumed" by the form during creation and no longer exist as separate entities. Reference lines, on the other hand, persist after the form is created and can alter the form if they are moved. Although the API does not have a ReferenceLine class, you can change a model line to a reference line using the ModelCurve.ChangeToReferenceLine() method.

<table summary="" id="GUID-B3D21FAA-9A8C-4E77-A019-D2E8439B473F__TABLE_BD498E16085F44D5ADBF55E5B2E98957"><tbody><tr><td><b>Code Region 14-2: Using Reference Lines to create Form</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>FormArray</span><span> </span><span>CreateRevolveForm</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FormArray</span><span> revolveForms </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// Create one profile</span><span>
    </span><span>ReferenceArray</span><span> ref_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>

    XYZ ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    XYZ ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    </span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelcurve </span><span>=</span><span> </span><span>MakeModelCurveFromTwoPoints</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    modelcurve </span><span>=</span><span> </span><span>MakeModelCurveFromTwoPoints</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    modelcurve </span><span>=</span><span> </span><span>MakeModelCurveFromTwoPoints</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    </span><span>// Create axis for revolve form</span><span>
    ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>5</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>5</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    </span><span>ModelCurve</span><span> axis </span><span>=</span><span> </span><span>MakeModelCurveFromTwoPoints</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>

    </span><span>// make axis a Reference Line</span><span>
    axis</span><span>.</span><span>ChangeToReferenceLine</span><span>();</span><span>

    </span><span>// Typically this operation produces only a single form, </span><span>
    </span><span>// but some combinations of arguments will create multiple froms from a single profile.</span><span>
    revolveForms </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewRevolveForms</span><span>(</span><span>true</span><span>,</span><span> ref_ar</span><span>,</span><span> axis</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>4</span><span>);</span><span>

    </span><span>return</span><span> revolveForms</span><span>;</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>ModelCurve</span><span> </span><span>MakeModelCurveFromTwoPoints</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> XYZ ptA</span><span>,</span><span> XYZ ptB</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span> doc</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>// Create plane by the points</span><span>
    </span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    XYZ norm </span><span>=</span><span> ptA</span><span>.</span><span>CrossProduct</span><span>(</span><span>ptB</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>norm</span><span>.</span><span>IsZeroLength</span><span>())</span><span> norm </span><span>=</span><span> XYZ</span><span>.</span><span>BasisZ</span><span>;</span><span>
    </span><span>Plane</span><span> plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>norm</span><span>,</span><span> ptB</span><span>);</span><span>
    </span><span>SketchPlane</span><span> skplane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> plane</span><span>);</span><span>
    </span><span>// Create line here</span><span>
    </span><span>ModelCurve</span><span> modelcurve </span><span>=</span><span> doc</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewModelCurve</span><span>(</span><span>line</span><span>,</span><span> skplane</span><span>);</span><span>
    </span><span>return</span><span> modelcurve</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F5F29826-D2EA-4007-8C3F-8F30975261C4-low.png)**Figure 55: Resulting Revolve Form**


<!-- ===== END: Help  Point and curve objects  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Forms  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:36 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Forms_html
author: 
---

# Help | Forms | Autodesk

> ## Excerpt
> Similar to family creation, the conceptual design environment provides the ability to create new forms. The following types of forms can be created: extrusions, revolves, sweeps, swept blends, lofts, and surface forms. Rather than using the Blend, Extrusion, Revolution, Sweep, and SweptBlend classes used in Family creation, Mass families use the Form class for all types of forms.

---
### Creating Forms

Similar to family creation, the conceptual design environment provides the ability to create new forms. The following types of forms can be created: extrusions, revolves, sweeps, swept blends, lofts, and surface forms. Rather than using the Blend, Extrusion, Revolution, Sweep, and SweptBlend classes used in Family creation, Mass families use the Form class for all types of forms.

An extrusion form is created from a closed curve loop that is planar. A revolve form is created from a profile and a line in the same plane as the profile which is the axis around which the shape is revolved to create a 3D form. A sweep form is created from a 2D profile that is swept along a planar path. A swept blend is created from multiple profiles, each one planar, that is swept along a single curve. A loft form is created from 2 or more profiles located on separate planes. A single surface form is created from a profile, similarly to an extrusion, but is given no height.

The following example creates a simple extruded form. Note that since the ModelCurves used to create the form are not converted to reference lines, they will be consumed by the resulting form.

<table summary="" id="GUID-F7F3AE4B-3A6E-45C5-B511-9066A9C3E4C2__TABLE_5A3AE538FDA94FC99A35193CBC72BB39"><tbody><tr><td><b>Code Region 14-3: Creating an extrusion form</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Form</span><span> </span><span>CreateExtrusionForm</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Form</span><span> extrusionForm </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// Create one profile</span><span>
    </span><span>ReferenceArray</span><span> ref_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>

    XYZ ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>90</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelcurve </span><span>=</span><span> </span><span>MakeLine</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>90</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>90</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    modelcurve </span><span>=</span><span> </span><span>MakeLine</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    ptA </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>90</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    ptB </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    modelcurve </span><span>=</span><span> </span><span>MakeLine</span><span>(</span><span>document</span><span>,</span><span> ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    ref_ar</span><span>.</span><span>Append</span><span>(</span><span>modelcurve</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    </span><span>// The extrusion form direction</span><span>
    XYZ direction </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>50</span><span>);</span><span>

    extrusionForm </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewExtrusionForm</span><span>(</span><span>true</span><span>,</span><span> ref_ar</span><span>,</span><span> direction</span><span>);</span><span>

    </span><span>int</span><span> profileCount </span><span>=</span><span> extrusionForm</span><span>.</span><span>ProfileCount</span><span>;</span><span>

    </span><span>return</span><span> extrusionForm</span><span>;</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>ModelCurve</span><span> </span><span>MakeLine</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> XYZ ptA</span><span>,</span><span> XYZ ptB</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span> doc</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>// Create plane by the points</span><span>
    </span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>ptA</span><span>,</span><span> ptB</span><span>);</span><span>
    XYZ norm </span><span>=</span><span> ptA</span><span>.</span><span>CrossProduct</span><span>(</span><span>ptB</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>norm</span><span>.</span><span>IsZeroLength</span><span>())</span><span> norm </span><span>=</span><span> XYZ</span><span>.</span><span>BasisZ</span><span>;</span><span>
    </span><span>Plane</span><span> plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>norm</span><span>,</span><span> ptB</span><span>);</span><span>
    </span><span>SketchPlane</span><span> skplane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> plane</span><span>);</span><span>
    </span><span>// Create line here</span><span>
    </span><span>ModelCurve</span><span> modelcurve </span><span>=</span><span> doc</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewModelCurve</span><span>(</span><span>line</span><span>,</span><span> skplane</span><span>);</span><span>
    </span><span>return</span><span> modelcurve</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-ACA912B3-A871-4886-8600-A95C293FB2D5-low.png)**Figure 56: Resulting extrusion form**

The following example shows how to create loft form using a series of CurveByPoints objects.

<table summary="" id="GUID-F7F3AE4B-3A6E-45C5-B511-9066A9C3E4C2__TABLE_4B7E9847580045DAAA8AA079CADCCFEF"><tbody><tr><td><b>Code Region 14-4: Creating a loft form</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Form</span><span> </span><span>CreateLoftForm</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Form</span><span> loftForm </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>ReferencePointArray</span><span> rpa </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferencePointArray</span><span>();</span><span>
        </span><span>ReferenceArrayArray</span><span> ref_ar_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArrayArray</span><span>();</span><span>
        </span><span>ReferenceArray</span><span> ref_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>
        </span><span>ReferencePoint</span><span> rp </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        XYZ xyz </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>// make first profile curve for loft</span><span>
        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>50</span><span>,</span><span> </span><span>10</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        </span><span>CurveByPoints</span><span> cbp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpa</span><span>);</span><span>
        ref_ar</span><span>.</span><span>Append</span><span>(</span><span>cbp</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>
        ref_ar_ar</span><span>.</span><span>Append</span><span>(</span><span>ref_ar</span><span>);</span><span>
        rpa</span><span>.</span><span>Clear</span><span>();</span><span>
        ref_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>

        </span><span>// make second profile curve for loft</span><span>
        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>50</span><span>,</span><span> </span><span>30</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        cbp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpa</span><span>);</span><span>
        ref_ar</span><span>.</span><span>Append</span><span>(</span><span>cbp</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>
        ref_ar_ar</span><span>.</span><span>Append</span><span>(</span><span>ref_ar</span><span>);</span><span>
        rpa</span><span>.</span><span>Clear</span><span>();</span><span>
        ref_ar </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>

        </span><span>// make third profile curve for loft</span><span>
        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>75</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>75</span><span>,</span><span> </span><span>50</span><span>,</span><span> </span><span>5</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        xyz </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewXYZ</span><span>(</span><span>75</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        rp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>xyz</span><span>);</span><span>
        rpa</span><span>.</span><span>Append</span><span>(</span><span>rp</span><span>);</span><span>

        cbp </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpa</span><span>);</span><span>
        ref_ar</span><span>.</span><span>Append</span><span>(</span><span>cbp</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>
        ref_ar_ar</span><span>.</span><span>Append</span><span>(</span><span>ref_ar</span><span>);</span><span>

        loftForm </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewLoftForm</span><span>(</span><span>true</span><span>,</span><span> ref_ar_ar</span><span>);</span><span>

        </span><span>return</span><span> loftForm</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-8F7F53FC-51B6-4547-86C4-709C11B72FCA-low.png)**Figure 57: Resulting loft form**

### Form modification

Once created, forms can be modified by changing a sub element (i.e. a face, edge, curve or vertex) of the form, or an entire profile. The methods to modify a form include:

-   AddEdge
-   AddProfile
-   DeleteProfile
-   DeleteSubElement
-   MoveProfile
-   MoveSubElement
-   RotateProfile
-   RotateSubElement
-   ScaleSubElement

Additionally, you can modify a form by adding an edge or a profile, which can then be modified using the methods listed above.

The following example moves the first profile curve of the given form by a specified offset. The corresponding figure shows the result of applying this code to the loft form from the previous example.

<table summary="" id="GUID-F7F3AE4B-3A6E-45C5-B511-9066A9C3E4C2__TABLE_B301A0AAE76F4957A9DE864937880216"><tbody><tr><td><b>Code Region 14-5: Moving a profile</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MoveForm</span><span>(</span><span>Form</span><span> form</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>int</span><span> profileCount </span><span>=</span><span> form</span><span>.</span><span>ProfileCount</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>form</span><span>.</span><span>ProfileCount</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>int</span><span> profileIndex </span><span>=</span><span> </span><span>0</span><span>;</span><span>   </span><span>// modify the first form only</span><span>
                </span><span>if</span><span> </span><span>(</span><span>form</span><span>.</span><span>CanManipulateProfile</span><span>(</span><span>profileIndex</span><span>))</span><span>
                </span><span>{</span><span>
                XYZ offset </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>25</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                form</span><span>.</span><span>MoveProfile</span><span>(</span><span>profileIndex</span><span>,</span><span> offset</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-BCA27D2B-71B9-40CE-A94E-2858C22B8A08-low.png)**Figure 58: Modified loft form**

The next sample demonstrates how to move a single vertex of a given form. The corresponding figure demonstrate the effect of this code on the previous extrusion form example

<table summary="" id="GUID-F7F3AE4B-3A6E-45C5-B511-9066A9C3E4C2__TABLE_D0B6539478A3427EAE436C52B9694A11"><tbody><tr><td><b>Code Region 14-6: Moving a sub element</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MoveSubElement</span><span>(</span><span>Form</span><span> form</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> document </span><span>=</span><span> form</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>form</span><span>.</span><span>ProfileCount</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>int</span><span> profileIndex </span><span>=</span><span> </span><span>0</span><span>;</span><span>   </span><span>// get first profile</span><span>
        </span><span>ReferenceArray</span><span> ra </span><span>=</span><span> form</span><span>.</span><span>get_CurveLoopReferencesOnProfile</span><span>(</span><span>profileIndex</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Reference</span><span> r </span><span>in</span><span> ra</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ReferenceArray</span><span> ra2 </span><span>=</span><span> form</span><span>.</span><span>GetControlPoints</span><span>(</span><span>r</span><span>);</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>Reference</span><span> r2 </span><span>in</span><span> ra2</span><span>)</span><span>
            </span><span>{</span><span>
                    </span><span>Point</span><span> vertex </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>r2</span><span>).</span><span>GetGeometryObjectFromReference</span><span>(</span><span>r2</span><span>)</span><span> </span><span>as</span><span> </span><span>Point</span><span>;</span><span>

                    XYZ offset </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>15</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                    form</span><span>.</span><span>MoveSubElement</span><span>(</span><span>r2</span><span>,</span><span> offset</span><span>);</span><span>
                    </span><span>break</span><span>;</span><span>  </span><span>// just move the first point</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-6C10E6B0-0BA6-4EDD-B976-8309A1CD1B73-low.png)**Figure 59: Modified extrusion form**


<!-- ===== END: Help  Forms  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Rationalizing a Surface  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:41 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Rationalizing_a_Surface_html
author: 
---

# Help | Rationalizing a Surface | Autodesk

> ## Excerpt
> Faces of forms can be divided with UV grids. You can access the data for a divided surface using the DividedSurface.GetReferencesWithDividedSurface() and DividedSurface.GetDividedSurfaceForReference() methods (as is shown in a subsequent example) as well as create new divided surfaces on forms as shown below.

---
### Dividing a surface

Faces of forms can be divided with UV grids. You can access the data for a divided surface using the DividedSurface.GetReferencesWithDividedSurface() and DividedSurface.GetDividedSurfaceForReference() methods (as is shown in a subsequent example) as well as create new divided surfaces on forms as shown below.

<table summary="" id="GUID-63B37608-4112-4424-B46A-ED61ACE95E7F__TABLE_E2A8ED204BD749508E94E0BE00E8E29C"><tbody><tr><td><b>Code Region 14-7: Dividing a surface</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>DivideSurface</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Form</span><span> form</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>Options</span><span> opt </span><span>=</span><span> application</span><span>.</span><span>Create</span><span>.</span><span>NewGeometryOptions</span><span>();</span><span>
    opt</span><span>.</span><span>ComputeReferences</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>

    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geomElem </span><span>=</span><span> form</span><span>.</span><span>get_Geometry</span><span>(</span><span>opt</span><span>);</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geomObj </span><span>in</span><span> geomElem</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Solid</span><span> solid </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> face </span><span>in</span><span> solid</span><span>.</span><span>Faces</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>face</span><span>.</span><span>Reference</span><span> </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>DividedSurface</span><span> ds </span><span>=</span><span> </span><span>DividedSurface</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span>face</span><span>.</span><span>Reference</span><span>);</span><span>
                </span><span>// create a divided surface with fixed number of U and V grid lines</span><span>
                </span><span>SpacingRule</span><span> srU </span><span>=</span><span> ds</span><span>.</span><span>USpacingRule</span><span>;</span><span>
                srU</span><span>.</span><span>SetLayoutFixedNumber</span><span>(</span><span>16</span><span>,</span><span> </span><span>SpacingRuleJustification</span><span>.</span><span>Center</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>

                </span><span>SpacingRule</span><span> srV </span><span>=</span><span> ds</span><span>.</span><span>VSpacingRule</span><span>;</span><span>
                srV</span><span>.</span><span>SetLayoutFixedNumber</span><span>(</span><span>24</span><span>,</span><span> </span><span>SpacingRuleJustification</span><span>.</span><span>Center</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>

                </span><span>break</span><span>;</span><span>  </span><span>// just divide one face of form</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-68B498E3-3756-47BF-8392-1F12F2F8D4ED-low.png)**Figure 60: Face of form divided by UV grids**

Accessing the USpacing and VSpacing properties of DividedSurface, you can define the SpacingRule for the U and V gridlines by specifying either a fixed number of grids (as in the example above), a fixed distance between grids, or a minimum or maximum spacing between grids. Additional information is required for each spacing rule, such as justification and grid rotation.

### Patterning a surface

A divided surface can be patterned. Any of the built-in tile patterns can be applied to a divided surface. A tile pattern is an ElementType that is assigned to the DividedSurface. The tile pattern is applied to the surface according to the UV grid layout, so changing the USpacing and VSpacing properties of the DividedSurface will affect how the patterned surface appears.

The following example demonstrates how to cover a divided surface with the OctagonRotate pattern. The corresponding figure shows how this looks when applied to the divided surface in the previous example. Note this example also demonstrates how to get a DividedSurface on a form.

<table summary="" id="GUID-63B37608-4112-4424-B46A-ED61ACE95E7F__TABLE_D7B4F3CCEFF24BCDB0978FAD61F01EDA"><tbody><tr><td><b>Code Region 14-8: Patterning a surface</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>TileSurface</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Form</span><span> form</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// cover surface with OctagonRotate tile pattern</span><span>
    </span><span>TilePatterns</span><span> tilePatterns </span><span>=</span><span> document</span><span>.</span><span>Settings</span><span>.</span><span>TilePatterns</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Reference</span><span> r </span><span>in</span><span> </span><span>DividedSurface</span><span>.</span><span>GetReferencesWithDividedSurfaces</span><span>(</span><span>form</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>DividedSurface</span><span> ds </span><span>=</span><span> </span><span>DividedSurface</span><span>.</span><span>GetDividedSurfaceForReference</span><span>(</span><span>document</span><span>,</span><span> r</span><span>);</span><span>
        ds</span><span>.</span><span>ChangeTypeId</span><span>(</span><span>tilePatterns</span><span>.</span><span>GetTilePattern</span><span>(</span><span>TilePatternsBuiltIn</span><span>.</span><span>OctagonRotate</span><span>).</span><span>Id</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-D0E6AFAA-9929-440C-87BF-F515C1579166-low.png)**Figure 61: Tile pattern applied to divided surface**

In addition to applying built-in tile patterns to a divided surface, you can create your own massing panel families using the "Curtain Panel Pattern Based.rft" template. These panel families can then be loaded into massing families and applied to divided surfaces using the DividedSurface.ChangeTypeId() method.

The following properties of Family are specific to curtain panel families:

-   IsCurtainPanelFamily
-   CurtainPanelHorizontalSpacing - horizontal spacing of driving mesh
-   CurtainPanelVerticalSpacing - vertical spacing of driving mesh
-   CurtainPanelTilePattern - choice of tile pattern

The following example demonstrates how to edit a massing panel family which can then be applied to a form in a conceptual mass document. To run this example, first create a new family document using the "Curtain Panel Pattern Based.rft" template.

<table summary="" id="GUID-63B37608-4112-4424-B46A-ED61ACE95E7F__TABLE_23DFE5C86CCC470A844C29687B220FDF"><tbody><tr><td><b>Code Region 14-9: Editing a curtain panel family</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>EditCurtainPanel</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Family</span><span> family </span><span>=</span><span> document</span><span>.</span><span>OwnerFamily</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>family</span><span>.</span><span>IsCurtainPanelFamily</span><span> </span><span>==</span><span> </span><span>true</span><span> </span><span>&amp;&amp;</span><span>
        family</span><span>.</span><span>CurtainPanelTilePattern</span><span> </span><span>==</span><span> </span><span>TilePatternsBuiltIn</span><span>.</span><span>Rectangle</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// first change spacing of grids in family document</span><span>
        family</span><span>.</span><span>CurtainPanelHorizontalSpacing</span><span> </span><span>=</span><span> </span><span>20</span><span>;</span><span>
        family</span><span>.</span><span>CurtainPanelVerticalSpacing</span><span> </span><span>=</span><span> </span><span>30</span><span>;</span><span>

        </span><span>// create new points and lines on grid</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>;</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>ReferencePoint</span><span>)).</span><span>ToElements</span><span>();</span><span>
        </span><span>int</span><span> ctr </span><span>=</span><span> </span><span>0</span><span>;</span><span>
        </span><span>ReferencePoint</span><span> rp0 </span><span>=</span><span> </span><span>null</span><span>,</span><span> rp1 </span><span>=</span><span> </span><span>null</span><span>,</span><span> rp2 </span><span>=</span><span> </span><span>null</span><span>,</span><span> rp3 </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> e </span><span>in</span><span> collection</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ReferencePoint</span><span> rp </span><span>=</span><span> e </span><span>as</span><span> </span><span>ReferencePoint</span><span>;</span><span>
            </span><span>switch</span><span> </span><span>(</span><span>ctr</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>case</span><span> </span><span>0</span><span>:</span><span>
                    rp0 </span><span>=</span><span> rp</span><span>;</span><span>
                    </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>1</span><span>:</span><span>
                    rp1 </span><span>=</span><span> rp</span><span>;</span><span>
                    </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>2</span><span>:</span><span>
                    rp2 </span><span>=</span><span> rp</span><span>;</span><span>
                    </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>3</span><span>:</span><span>
                    rp3 </span><span>=</span><span> rp</span><span>;</span><span>
                    </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
            ctr</span><span>++;</span><span>
        </span><span>}</span><span>

        </span><span>ReferencePointArray</span><span> rpAr </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferencePointArray</span><span>();</span><span>
        rpAr</span><span>.</span><span>Append</span><span>(</span><span>rp0</span><span>);</span><span>
        rpAr</span><span>.</span><span>Append</span><span>(</span><span>rp2</span><span>);</span><span>
        </span><span>CurveByPoints</span><span> curve1 </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpAr</span><span>);</span><span>
        </span><span>PointLocationOnCurve</span><span> pointLocationOnCurve25 </span><span>=</span><span> </span><span>new</span><span> </span><span>PointLocationOnCurve</span><span>(</span><span>PointOnCurveMeasurementType</span><span>.</span><span>NormalizedCurveParameter</span><span>,</span><span> </span><span>0.25</span><span>,</span><span> </span><span>PointOnCurveMeasureFrom</span><span>.</span><span>Beginning</span><span>);</span><span>
        </span><span>PointOnEdge</span><span> poeA </span><span>=</span><span> app</span><span>.</span><span>Create</span><span>.</span><span>NewPointOnEdge</span><span>(</span><span>curve1</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>,</span><span> pointLocationOnCurve25</span><span>);</span><span>
        </span><span>ReferencePoint</span><span> rpA </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>poeA</span><span>);</span><span>
        </span><span>PointLocationOnCurve</span><span> pointLocationOnCurve75 </span><span>=</span><span> </span><span>new</span><span> </span><span>PointLocationOnCurve</span><span>(</span><span>PointOnCurveMeasurementType</span><span>.</span><span>NormalizedCurveParameter</span><span>,</span><span> </span><span>0.75</span><span>,</span><span> </span><span>PointOnCurveMeasureFrom</span><span>.</span><span>Beginning</span><span>);</span><span>
        </span><span>PointOnEdge</span><span> poeB </span><span>=</span><span> app</span><span>.</span><span>Create</span><span>.</span><span>NewPointOnEdge</span><span>(</span><span>curve1</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>,</span><span> pointLocationOnCurve75</span><span>);</span><span>
        </span><span>ReferencePoint</span><span> rpB </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>poeB</span><span>);</span><span>

        rpAr</span><span>.</span><span>Clear</span><span>();</span><span>
        rpAr</span><span>.</span><span>Append</span><span>(</span><span>rp1</span><span>);</span><span>
        rpAr</span><span>.</span><span>Append</span><span>(</span><span>rp3</span><span>);</span><span>
        </span><span>CurveByPoints</span><span> curve2 </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewCurveByPoints</span><span>(</span><span>rpAr</span><span>);</span><span>
        </span><span>PointOnEdge</span><span> poeC </span><span>=</span><span> app</span><span>.</span><span>Create</span><span>.</span><span>NewPointOnEdge</span><span>(</span><span>curve2</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>,</span><span> pointLocationOnCurve25</span><span>);</span><span>
        </span><span>ReferencePoint</span><span> rpC </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>poeC</span><span>);</span><span>
        </span><span>PointOnEdge</span><span> poeD </span><span>=</span><span> app</span><span>.</span><span>Create</span><span>.</span><span>NewPointOnEdge</span><span>(</span><span>curve2</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>,</span><span> pointLocationOnCurve75</span><span>);</span><span>
        </span><span>ReferencePoint</span><span> rpD </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewReferencePoint</span><span>(</span><span>poeD</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Please open a curtain family document before calling this command."</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-8EECE3F0-4C1F-4B31-9133-D3D64676E7FE-low.png)**Figure 62: Curtain panel family**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-263500A5-C732-4E47-B9AA-D878AF9E9729-low.png)**Figure 63: Curtain panel assigned to divided surface**


<!-- ===== END: Help  Rationalizing a Surface  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Adaptive Components  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:46 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Adaptive_Components_html
author: 
---

# Help | Adaptive Components | Autodesk

> ## Excerpt
> Adaptive Components are designed to handle cases where components need to flexibly adapt to many unique contextual conditions. For example, adaptive components could be used in repeating systems generated by arraying multiple components that conform to user-defined constraints.

---
Adaptive Components are designed to handle cases where components need to flexibly adapt to many unique contextual conditions. For example, adaptive components could be used in repeating systems generated by arraying multiple components that conform to user-defined constraints.

The following code shows how to create an instance of an adaptive component family into a massing family and set the position of each point mathematically.

<table summary="" id="GUID-82974C89-F47A-44D7-B6CC-087EE9C3E09C__TABLE_12B8B51DFFB047E19755BB38A90B48C4"><tbody><tr><td><b>Code Region: Creating an Instance of an Adaptive Component Family</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateAdaptiveComponentInstance</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilySymbol</span><span> symbol</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create a new instance of an adaptive component family</span><span>
    </span><span>FamilyInstance</span><span> instance </span><span>=</span><span> </span><span>AdaptiveComponentInstanceUtils</span><span>.</span><span>CreateAdaptiveComponentInstance</span><span>(</span><span>document</span><span>,</span><span> symbol</span><span>);</span><span>

    </span><span>// Get the placement points of this instance</span><span>
    </span><span>IList</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> placePointIds </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
    placePointIds </span><span>=</span><span> </span><span>AdaptiveComponentInstanceUtils</span><span>.</span><span>GetInstancePlacementPointElementRefIds</span><span>(</span><span>instance</span><span>);</span><span>
    </span><span>double</span><span> x </span><span>=</span><span> </span><span>0</span><span>;</span><span>

    </span><span>// Set the position of each placement point</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> placePointIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>ReferencePoint</span><span> point </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>ReferencePoint</span><span>;</span><span>
        point</span><span>.</span><span>Position</span><span> </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>XYZ</span><span>(</span><span>10</span><span>*</span><span>x</span><span>,</span><span> </span><span>10</span><span>*</span><span>Math</span><span>.</span><span>Cos</span><span>(</span><span>x</span><span>),</span><span> </span><span>0</span><span>);</span><span>
        x </span><span>+=</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>/</span><span>6</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

To batch create adaptive components, you can use the overload of the FamilyInstanceCreationData constructor that takes two parameters - a FamilySymbol and a list of XYZ adaptive points where the adaptive instance is to be initialized . In conjunction with the Autodesk.Revit.Creation.ItemFactoryBase.NewFamilyInstances2() method which takes a list of FamilyInstanceCreationData objects, multiple adaptive components can be added at once. This may be more efficient than placing individual adaptive components one-by-one.


<!-- ===== END: Help  Adaptive Components  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Create a .addin manifest file  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Create_a_addin_manifest_file_html
author: 
---

# Help | Create a .addin manifest file | Autodesk

> ## Excerpt
> The HelloWorld.dll file appears in the project output directory. If you want to invoke the application in Revit, create a manifest file to register it into Revit.

---
The HelloWorld.dll file appears in the project output directory. If you want to invoke the application in Revit, create a manifest file to register it into Revit.

To create a manifest file

1.  Create a new text file in Notepad.
2.  Add the following text:

#### Code Region 30-10: Creating a .addin manifest file for an external command

```
<?xml version="1.0" encoding="utf-8" standalone="no"?>
    <RevitAddIns>
    <AddIn Type="Command">
        <Name>HelloWorld</Name>
        <FullClassName>HelloWorld.HelloWorld</FullClassName>
        <Text>HelloWorld</Text>
        <Description>Show Hello World.</Description>
        <VisibilityMode>AlwaysVisible</VisibilityMode>
        <Assembly>C:\Samples\HelloWorld\HelloWorld\bin\Debug\HelloWorld.dll</Assembly>
        <AddInId>239BD853-36E4-461f-9171-C5ACEDA4E723</AddInId>
        <VendorId>ADSK</VendorId>
        <VendorDescription>Autodesk, Inc, www.autodesk.com</VendorDescription>
      </AddIn>
    </RevitAddIns>
```

Note: The FullClassName includes the Root namespace found on the Application tab of the properties for the project.

3.  Save the file as HelloWorld.addin and put it in the following location:
    -   C:\\ProgramData\\Autodesk\\Revit\\Addins{{RelYear}}\\

Refer to [Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html) for more details using manifest files.


<!-- ===== END: Help  Create a .addin manifest file  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Datum and Information Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:59:55 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_html
author: 
---

# Help | Datum and Information Elements | Autodesk

> ## Excerpt
> This chapter introduces Datum Elements and Information Elements in Revit.

---
This chapter introduces Datum Elements and Information Elements in Revit.

-   Datum Elements include levels, grids, and ModelCurves.
-   Information Elements include phases, design options, and EnergyDataSettings.

For more information about Revit Element classifications, refer to [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html).

If you need more information, refer to the related chapter:

-   For LoadBase, LoadCase, LoadCombination, LoadNature and LoadUsage, refer to [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html)
-   For ModelCurve, refer to [Sketching](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_html)
-   For Material and FillPattern, refer to [Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_html)
-   For EnergyDataSettings, refer to [Energy Data](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Energy_Data_html)


<!-- ===== END: Help  Datum and Information Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Levels  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:00 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_Levels_html
author: 
---

# Help | Levels | Autodesk

> ## Excerpt
> A level is a finite horizontal plane that acts as a reference for level-hosted elements, such as walls, roofs, floors, and ceilings.

---
A level is a finite horizontal plane that acts as a reference for level-hosted elements, such as walls, roofs, floors, and ceilings.

In the Revit Platform API, the Level class is derived from the DatumPlane class, which is derived from the Element class. The inherited Name property is used to retrieve the user-visible level name beside the level bubble in the Revit UI. To retrieve all levels in a project, use an ElementClassFilter with the Level class.

## Elevation

The Level class has the following properties:

-   The Elevation property is used to retrieve or change the elevation above or below ground level.
-   The ProjectElevation property is used to retrieve the elevation relative to the project origin regardless of the Elevation Base parameter value.
-   The Elevation Base value is a Level type parameter.
    -   Its BuiltInParameter is LEVEL\_RELATIVE\_BASE\_TYPE.
    -   Its StorageType is Integer
    -   0 corresponds to Project and 1 corresponds to Shared.

The following code sample illustrates how to retrieve all levels in a project using a Level class filter.

<table summary="" id="GUID-AA1B1CD4-3988-4F90-9C19-CE0DC1EC2039__TABLE_B0CB7899667846E8B42DA126C2134E9F"><tbody><tr><td><b>Code Region 15-1: Retrieving all Levels</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>Getinfo_Level</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>StringBuilder</span><span> levelInformation </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>();</span><span>
        </span><span>int</span><span> levelNumber </span><span>=</span><span> </span><span>0</span><span>;</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Level</span><span>)).</span><span>ToElements</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> collection</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Level</span><span> level </span><span>=</span><span> e </span><span>as</span><span> </span><span>Level</span><span>;</span><span>

                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> level</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>// keep track of number of levels</span><span>
                        levelNumber</span><span>++;</span><span>

                        </span><span>//get the name of the level</span><span>
                        levelInformation</span><span>.</span><span>Append</span><span>(</span><span>"\nLevel Name: "</span><span> </span><span>+</span><span> level</span><span>.</span><span>Name</span><span>);</span><span>

                        </span><span>//get the elevation of the level</span><span>
                        levelInformation</span><span>.</span><span>Append</span><span>(</span><span>"\n\tElevation: "</span><span> </span><span>+</span><span> level</span><span>.</span><span>Elevation</span><span>);</span><span>

                        </span><span>// get the project elevation of the level</span><span>
                        levelInformation</span><span>.</span><span>Append</span><span>(</span><span>"\n\tProject Elevation: "</span><span> </span><span>+</span><span> level</span><span>.</span><span>ProjectElevation</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>//number of total levels in current document</span><span>
        levelInformation</span><span>.</span><span>Append</span><span>(</span><span>"\n\n There are "</span><span> </span><span>+</span><span> levelNumber </span><span>+</span><span> </span><span>" levels in the document!"</span><span>);</span><span>

        </span><span>//show the level information in the messagebox</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>levelInformation</span><span>.</span><span>ToString</span><span>());</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Creating a Level

Using the Level command, you can define a vertical height or story within a building and you can create a level for each existing story or other building references. Levels must be added in a section or elevation view. Additionally, you can create a new level using the Revit Platform API.

The following code sample illustrates how to create a new level.

<table summary="" id="GUID-AA1B1CD4-3988-4F90-9C19-CE0DC1EC2039__TABLE_5B1F57D7695E4CDFB78261D5F533C977"><tbody><tr><td><b>Code Region 15-2: Creating a new Level</b></td></tr><tr><td><pre><code><span>Level</span><span> </span><span>CreateLevel</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// The elevation to apply to the new level</span><span>
    </span><span>double</span><span> elevation </span><span>=</span><span> </span><span>20.0</span><span>;</span><span> 

    </span><span>// Begin to create a level</span><span>
    </span><span>Level</span><span> level </span><span>=</span><span> </span><span>Level</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> elevation</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> level</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create a new level failed."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Change the level name</span><span>
    level</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"New level"</span><span>;</span><span>

    </span><span>return</span><span> level</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: After creating a new level, Revit does not create the associated plan view for this level. If necessary, you can create it yourself.

## Finding levels based on elevation

You can find levels based on their elevation with a `FilteredElementCollector`. You can also use one of these static methods which return the id of the Level which is closest to the specified elevation. The level can be at, above, or below the target elevation. If there is more than one Level at the same distance from the elevation, the Level with the lowest id will be returned

-   Level.GetNearestLevelId(Document document, double elevation)
-   Level.GetNearestLevelId(Document document, double elevation, out double offset)


<!-- ===== END: Help  Levels  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Grids  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_Grids_html
author: 
---

# Help | Grids | Autodesk

> ## Excerpt
> The Grid class represents a single grid line within Autodesk Revit.

---
The Grid class represents a single grid line within Autodesk Revit.

Grids are represented by the Grid class which is derived from the DatumPlane class, which is derived from the Element class. It contains all grid properties and methods. The inherited Name property is used to retrieve the content of the grid line's bubble.

### Curve

The Grid class Curve property gets the object that represents the grid line geometry.

-   If the IsCurved property returns true, the Curve property will be an Arc class object.
-   If the IsCurved property returns false, the Curve property will be a Line class object.

For more information, refer to [Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html).

The following code is a simple example using the Grid class. The result appears in a message box after invoking the command.

<table summary="" id="GUID-A1329448-D2AD-4810-94D3-70324DF17D8D__TABLE_2F66636D4B7643B682C58653C7249B83"><tbody><tr><td><b>Code Region 15-3: Using the Grid class</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetInfo_Grid</span><span>(</span><span>Grid</span><span> grid</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Grid : "</span><span>;</span><span>

    </span><span>// Show IsCurved property</span><span>
    message </span><span>+=</span><span> </span><span>"\nIf grid is Arc : "</span><span> </span><span>+</span><span> grid</span><span>.</span><span>IsCurved</span><span>;</span><span>

    </span><span>// Show Curve information</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> curve </span><span>=</span><span> grid</span><span>.</span><span>Curve</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>grid</span><span>.</span><span>IsCurved</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// if the curve is an arc, give center and radius information</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Arc</span><span> arc </span><span>=</span><span> curve </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Arc</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nArc's radius: "</span><span> </span><span>+</span><span> arc</span><span>.</span><span>Radius</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nArc's center:  ("</span><span> </span><span>+</span><span> </span><span>XYZString</span><span>(</span><span>arc</span><span>.</span><span>Center</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>// if the curve is a line, give length information</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Line</span><span> line </span><span>=</span><span> curve </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Line</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nLine's Length: "</span><span> </span><span>+</span><span> line</span><span>.</span><span>Length</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>// Get curve start point</span><span>
    message </span><span>+=</span><span> </span><span>"\nStart point: "</span><span> </span><span>+</span><span> </span><span>XYZString</span><span>(</span><span>curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>));</span><span>
    </span><span>// Get curve end point</span><span>
    message </span><span>+=</span><span> </span><span>"; End point: "</span><span> </span><span>+</span><span> </span><span>XYZString</span><span>(</span><span>curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>));</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span><span>

</span><span>// output the point's three coordinates</span><span>
</span><span>private</span><span> </span><span>string</span><span> </span><span>XYZString</span><span>(</span><span>XYZ point</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>return</span><span> </span><span>"("</span><span> </span><span>+</span><span> point</span><span>.</span><span>X </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Creating a Grid

Two overloaded Create() methods are available in the Grid class to create a new grid in the Revit Platform API. Using the following method with different parameters, you can create a curved or straight grid:

<table summary="" id="GUID-A1329448-D2AD-4810-94D3-70324DF17D8D__TABLE_4F94646184914C36B127FC7AC09C8B8B"><tbody><tr><td><b>Code Region 15-4: Grid.Create()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Grid</span><span> </span><span>Create</span><span>(</span><span> </span><span>Document</span><span> document</span><span>,</span><span> </span><span>Arc</span><span> arc </span><span>);</span><span>
</span><span>public</span><span> </span><span>Grid</span><span> </span><span>Create</span><span>(</span><span> </span><span>Document</span><span> document</span><span>,</span><span> </span><span>Line</span><span> line </span><span>);</span></code></pre></td></tr></tbody></table>

Note: The arc or the line used to create a grid must be in a horizontal plane.

The following code sample illustrates how to create a new grid with a line or an arc.

<table summary="" id="GUID-A1329448-D2AD-4810-94D3-70324DF17D8D__TABLE_468EBA2D159D45D695F10F4AB43E4906"><tbody><tr><td><b>Code Region 15-5: Creating a grid with a line or an arc</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>CreateGrid</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create the geometry line which the grid locates</span><span>
    XYZ start </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ </span><span>end</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>30</span><span>,</span><span> </span><span>30</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Line</span><span> geomLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>start</span><span>,</span><span> </span><span>end</span><span>);</span><span>

    </span><span>// Create a grid using the geometry line</span><span>
    </span><span>Grid</span><span> lineGrid </span><span>=</span><span> </span><span>Grid</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> geomLine</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> lineGrid</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create a new straight grid failed."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Modify the name of the created grid</span><span>
    lineGrid</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"New Name1"</span><span>;</span><span>

    </span><span>// Create the geometry arc which the grid locates</span><span>
    XYZ end0 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ end1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>40</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ pointOnCurve </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>7</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Arc</span><span> geomArc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>end0</span><span>,</span><span> end1</span><span>,</span><span> pointOnCurve</span><span>);</span><span>

    </span><span>// Create a grid using the geometry arc</span><span>
    </span><span>Grid</span><span> arcGrid </span><span>=</span><span> </span><span>Grid</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> geomArc</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> arcGrid</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create a new curved grid failed."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Modify the name of the created grid</span><span>
    arcGrid</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"New Name2"</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: In Revit, the grids are named automatically in a numerical or alphabetical sequence when they are created.


<!-- ===== END: Help  Grids  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Phase  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_Phase_html
author: 
---

# Help | Phase | Autodesk

> ## Excerpt
> Some architectural projects, such as renovations, proceed in phases. Phases have the following characteristics:

---
Some architectural projects, such as renovations, proceed in phases. Phases have the following characteristics:

-   Phases represent distinct time periods in a project lifecycle.
-   The lifetime of an element within a building is controlled by phases.
-   Each element has a construction phase but only the elements with a finite lifetime have a destruction phase.

All phases in a project can be retrieved from the Document object. A Phase object contains three pieces of useful information: Name, ID and UniqueId. The remaining properties always return null or an empty collection.

Each new modeling component added to a project has a Created Phase ID and a Demolished Phase ID property. The Element.AllowPhases() method indicates whether its phase ID properties can be modified.

The Created Phase ID property has the following characteristics:

-   It identifies the phase in which the component was added.
-   The default value is the same ID as the current view Phase value.
-   Change the Created Phase ID parameter by selecting a new value corresponding to the drop-down list.

The Demolished Phase ID property has the following characteristics:

-   It identifies in which phase the component is demolished.
-   The default value is none.
-   Demolishing a component with the demolition tool updates the property to the current Phase ID value in the view where you demolished the element.
-   You can demolish a component by setting the Demolished Phase ID property to a different value.
-   If you delete a phase using the Revit Platform API, all modeling components in the current phase still exist. The Created Phase ID parameter value for these components is changed to the next item in the drop-down list in the Properties dialog box. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-3840696A-98D6-4898-8004-EFB85A3247E1-low.png)**Figure 65: Phase-created component parameter value**

The following code sample displays all supported phases in the current document. The phase names are displayed in a message box.

<table summary="" id="GUID-DD43AD1E-37D1-4F61-8A23-52C9DEFF2D3F__TABLE_FBF013133CA740FFB96BD77DB7FE0870"><tbody><tr><td><b>Code Region 15-6: Displaying all supported phases</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>Getinfo_Phase</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Get the phase array which contains all the phases.</span><span>
        </span><span>PhaseArray</span><span> phases </span><span>=</span><span> doc</span><span>.</span><span>Phases</span><span>;</span><span>
        </span><span>// Format the string which identifies all supported phases in the current document.</span><span>
        </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>!=</span><span> phases</span><span>.</span><span>Size</span><span>)</span><span>
        </span><span>{</span><span>
                prompt </span><span>=</span><span> </span><span>"All the phases in current document list as follow:"</span><span>;</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>Phase</span><span> ii </span><span>in</span><span> phases</span><span>)</span><span>
                </span><span>{</span><span>
                        prompt </span><span>+=</span><span> </span><span>"\n\t"</span><span> </span><span>+</span><span> ii</span><span>.</span><span>Name</span><span>;</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
                prompt </span><span>=</span><span> </span><span>"There are no phases in current document."</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>// Give the user the information.</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Validating phase data of an element

`Element.IsDemolishedPhaseOrderValid()` and `Element.IsCreatedPhaseOrderValid()` validate the order of phases on a given element, ensuring that an object is not assigned a phase where it is demolished before it was created.


<!-- ===== END: Help  Phase  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Design Options  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_Design_Options_html
author: 
---

# Help | Design Options | Autodesk

> ## Excerpt
> Design options provide a way to explore alternative designs in a project.

---
Design options provide a way to explore alternative designs in a project.

Design options provide the flexibility to adapt to changes in project scope or to develop alternative designs for review. You can begin work with the main project model and then develop variations along the way to present to a client. Most elements can be added into a design option. Elements that cannot be added into a design option are considered part of the main model and have no design alternatives.

The main use for Design options is as a property of the Element class. See the following example.

<table summary="" id="GUID-F84EFE35-C0B3-417D-A3B8-0DE98E9A61B5__TABLE_3BF9E42C9F8F4B649AB43B632966E4C6"><tbody><tr><td><b>Code Region 15-7: Using design options</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>Getinfo_DesignOption</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the selected Elements in the Active Document</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> element </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>//Use the DesignOption property of Element</span><span>
        </span><span>if</span><span> </span><span>(</span><span>element</span><span>.</span><span>DesignOption</span><span> </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>element</span><span>.</span><span>DesignOption</span><span>.</span><span>Name</span><span>.</span><span>ToString</span><span>());</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following rules apply to Design Options

-   The value of the DesignOption property is null if the element is in the Main Model. Otherwise, the name you created in the Revit UI is returned.
-   Only one active DesignOption Element can exist in an ActiveDocument.
    -   The primary option is considered the default active DesignOption. For example, a design option set is named Wall and there are two design options in this set named "brick wall" and "glass wall". If "brick wall" is the primary option, only this option and elements that belong to it are retrieved by the Element Iterator. "Glass wall" is inactive.


<!-- ===== END: Help  Design Options  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Annotation Elements  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_html
author: 
---

# Help | Annotation Elements | Autodesk

> ## Excerpt
> This section covers Revit Annotation Elements, such as dimensions, text notes, keynotes, tags, and symbols.

---
This section covers Revit Annotation Elements, such as dimensions, text notes, keynotes, tags, and symbols.

Note that:

-   Dimensions are view-specific elements that display sizes and distances in a project.
-   Detail curves are created for detailed drawings. They are visible only in the view in which they are drawn. Often they are drawn over the model view.
-   Tags are an annotation used to identify elements in a drawing. Properties associated with a tag can appear in schedules.
-   AnnotationSymbol has multiple leader options when loaded into a project.

For more information about Revit Element classification, refer to [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html).


<!-- ===== END: Help  Annotation Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Dimensions and Constraints  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_Dimensions_and_Constraints_html
author: 
---

# Help | Dimensions and Constraints | Autodesk

> ## Excerpt
> The Dimension class represents permanent dimensions and dimension-related constraint elements. Temporary dimensions created while editing an element in the UI are not accessible. Spot elevation and spot coordinate are represented by the SpotDimension class.

---
The Dimension class represents permanent dimensions and dimension-related constraint elements. Temporary dimensions created while editing an element in the UI are not accessible. Spot elevation and spot coordinate are represented by the SpotDimension class.

The following code sample illustrates, near the end, how to distinguish permanent dimensions from constraint elements.

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_494C6C114DD54245AD084F2CE53B7F60"><tbody><tr><td><b>Code Region 16-1: Distinguishing permanent dimensions from constraints</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetInfo_Dimension</span><span>(</span><span>Dimension</span><span> dimension</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Dimension : "</span><span>;</span><span>
    </span><span>// Get Dimension name</span><span>
    message </span><span>+=</span><span> </span><span>"\nDimension name is : "</span><span> </span><span>+</span><span> dimension</span><span>.</span><span>Name</span><span>;</span><span>

    </span><span>// Get Dimension Curve</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> curve </span><span>=</span><span> dimension</span><span>.</span><span>Curve</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>curve </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> curve</span><span>.</span><span>IsBound</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Get curve start point</span><span>
        message </span><span>+=</span><span> </span><span>"\nCurve start point:("</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
        </span><span>// Get curve end point</span><span>
        message </span><span>+=</span><span> </span><span>"; Curve end point:("</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>// Get Dimension type name</span><span>
    message </span><span>+=</span><span> </span><span>"\nDimension type name is : "</span><span> </span><span>+</span><span> dimension</span><span>.</span><span>DimensionType</span><span>.</span><span>Name</span><span>;</span><span>

    </span><span>// Get Dimension view name</span><span>
    message </span><span>+=</span><span> </span><span>"\nDimension view name is : "</span><span> </span><span>+</span><span> dimension</span><span>.</span><span>View</span><span>.</span><span>Name</span><span>;</span><span>

    </span><span>// Get Dimension reference count</span><span>
    message </span><span>+=</span><span> </span><span>"\nDimension references count is "</span><span> </span><span>+</span><span> dimension</span><span>.</span><span>References</span><span>.</span><span>Size</span><span>;</span><span>

    </span><span>if</span><span> </span><span>((</span><span>int</span><span>)</span><span>BuiltInCategory</span><span>.</span><span>OST_Dimensions </span><span>==</span><span> dimension</span><span>.</span><span>Category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>)</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"\nDimension is a permanent dimension."</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>((</span><span>int</span><span>)</span><span>BuiltInCategory</span><span>.</span><span>OST_Constraints </span><span>==</span><span> dimension</span><span>.</span><span>Category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>)</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"\nDimension is a constraint element."</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Dimensions

There are five kinds of permanent dimensions:

-   Linear dimension
-   Radial dimension
-   Diameter Dimension
-   Angular dimension
-   Arc length dimension

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/Dims.png)**Figure 66: Permanent dimensions**

The BuiltInCategory for all permanent dimensions is OST\_Dimensions. There is not an easy way to distinguish the four dimensions using the API.

Except for radial and diameter dimensions, every dimension has one dimension line. Dimension lines are available from the Dimension.Curve property which is always unbound. In other words, the dimension line does not have a start-point or end-point. Based on the previous picture:

-   A Line object is returned for a linear dimension.
-   An arc object is returned for a radial dimension or angular dimension.
-   A radial dimension returns null.
-   A diamter diimension returns null.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4C8DCD73-DFD8-4185-A1EA-2C890D176FBF-low.png)**Figure 67: Dimension references**

A dimension is created by selecting geometric references as the previous picture shows. Geometric references are represented as a Reference class in the API. The following dimension references are available from the References property. For more information about Reference, please see [Geometry Helper Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Helper_Classes_html) in the [Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html) section.

-   Radial and diameter dimensions - One Reference object for the curve is returned
-   Angular and arc length dimensions - Two Reference objects are returned.
-   Linear dimensions - Two or more Reference objects are returned. In the following picture, the linear dimension has five Reference objects.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-A976B817-2D4B-471B-BF79-27E9262A8A85-low.png)**Figure 68: Linear dimension references**

Dimensions, like other Annotation Elements, are view-specific. They display only in the view where they are added. The Dimension.View property returns the specific view.

### Constraint Elements

Dimension objects with Category Constraints (BuitInCategory.OST\_Constraints) represent two kinds of dimension-related constraints:

-   Linear and radial dimension constraints
-   Equality constraints

In the following picture, two kinds of locked constraints correspond to linear and radial dimension. In the application, they appear as padlocks with green dashed lines. (The green dashed line is available from the Dimension.Curve property.) Both linear and radial dimension constraints return two Reference objects from the Dimension.References property.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-370D4754-3BC7-4A6C-8531-41B7A5B424D9-low.png)**Figure 69: Linear and Radial dimension constraints**

Constraint elements are not view-specific and can display in different views. Therefore, the View property always returns null. In the following picture, the constraint elements in the previous picture are also visible in the 3D view.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-8365F25E-7304-413D-BABE-1C495BD8ADAD-low.png)**Figure 70: Linear and Radial dimension constraints in 3D view**

Although equality constraints are based on dimensions, they are also represented by the Dimension class. There is no direct way to distinguish linear dimension constraints from equality constraints in the API using a category or DimensionType. Equality constraints return three or more References while linear dimension constraints return two or more References.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-FB6F70CD-8913-4C3A-A036-2108550BA25C-low.png)**Figure 71: Equality constraints**

Note: Not all constraint elements are represented by the Dimension class but all belong to a Constraints (OST\_Constraints) category such as alignment constraint. ### Spot Dimensions

Spot coordinates and spot elevations are represented by the SpotDimension class and are distinguished by category. Like the permanent dimension, spot dimensions are view-specific. The type and category for each spot dimension are listed in the following table:

**Table 35: Spot dimension Type and Category**

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_6C4FFE8D1C7A414F830F2B214A20E229"><tbody><tr><td><b>Type</b></td><td><b>Category</b></td></tr><tr><td>Spot Coordinates</td><td>OST_SpotCoordinates</td></tr><tr><td>Spot Elevations</td><td>OST_SpotElevations</td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-BDB09C60-D4AC-4F6A-8100-6BA2FA165228-low.png)**Figure 72: SpotCoordinates and SpotElevations**

The SpotDimension Location can be downcast to LocationPoint so that the point coordinate that the spot dimension points to is available from the LocationPoint.Point property.

-   SpotDimensions have no dimension curve so their Curve property always returns null.
-   The SpotDimension References property returns one Reference representing the point or the edge referenced by the spot dimension.
-   To control the text and tag display style, modify the SpotDimension and SpotDimensionType Parameters.

Information about the leader of a spot dimension is accessible with:

-   SpotDimension.LeaderElbowPosition
-   SpotDimension.LeaderHasElbow

### Comparison

The following table compares different kinds of dimensions and constraints in the API:

**Table 36: Dimension Category Comparison**

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_BB38A40A891647BCA63FD2814EEEC0C4"><tbody><tr><td><b><i>Dimension or Constraint</i></b></td><td><b><i>Dimension or Constraint</i></b></td><td><b><i>API Class</i></b></td><td><b><i>BuiltInCategory</i></b></td><td><b><i>Curve</i></b></td><td><b><i>Geometry Helper Classes</i></b></td><td><b><i>View</i></b></td><td><b><i>Location</i></b></td></tr><tr><td>Permanent Dimension</td><td>linear dimension</td><td>Dimension</td><td>OST_Dimensions</td><td>A Line</td><td>=2</td><td>Specific view</td><td>null</td></tr><tr><td>Permanent Dimension</td><td>radial dimension</td><td>Dimension</td><td>OST_Dimensions</td><td>Null</td><td>1</td><td>Specific view</td><td>null</td></tr><tr><td>Permanent Dimension</td><td>diameter dimension</td><td>Dimension</td><td>OST_Dimensions</td><td>Null</td><td>1</td><td>Specific view</td><td>null</td></tr><tr><td>Permanent Dimension</td><td>angular dimension</td><td>Dimension</td><td>OST_Dimensions</td><td>An Arc</td><td>2</td><td>Specific view</td><td>null</td></tr><tr><td>Permanent Dimension</td><td>arc length dimension</td><td>Dimension</td><td>OST_Dimensions</td><td>An Arc</td><td>2</td><td>Specific view</td><td>null</td></tr><tr><td>Dimension Constraint</td><td>linear dimension constraint</td><td>Dimension</td><td>OST_Constraints</td><td>An Arc</td><td>2</td><td>&nbsp;</td><td>null</td></tr><tr><td>Dimension Constraint</td><td>angular dimension</td><td>Dimension</td><td>OST_Constraints</td><td>An Arc</td><td>2</td><td>&nbsp;</td><td>null</td></tr><tr><td>Equality Constraint</td><td>Equality Constraint</td><td>Dimension</td><td>OST_Constraints</td><td>A Line</td><td>=3</td><td>&nbsp;</td><td>null</td></tr></tbody></table>

### Create and Delete

The NewDimension() method is available in the Creation.Document class. This method can create a linear dimension only.

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_721E2A5AFB174B41A2CFBF054DC78750"><tbody><tr><td><b>Code Region 16-2: NewDimension()</b></td></tr><tr><td><p><code>public Dimension NewDimension (View view, Line line, ReferenceArray references)</code></p></td></tr><tr><td><p><code>public Dimension NewDimension (View view, Line line, ReferenceArray references, DimensionType dimensionType)</code></p></td></tr></tbody></table>

Using the NewDimension() method input parameters, you can define the visible View, dimension line, and References (two or more). However, there is no easy way to distinguish a linear dimension DimensionType from other types. The overloaded NewDimension() method with the DimensionType parameter is rarely used.

The following code illustrates how to use the NewDimension() method to duplicate a dimension.

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_7BD6B8CE504A44C6863806DCEB8FED48"><tbody><tr><td><b>Code Region 16-3: Duplicating a dimension with NewDimension()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>DuplicateDimension</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Dimension</span><span> dimension</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Line</span><span> line </span><span>=</span><span> dimension</span><span>.</span><span>Curve</span><span> </span><span>as</span><span> </span><span>Line</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> line</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>View</span><span> view </span><span>=</span><span> dimension</span><span>.</span><span>View</span><span>;</span><span>
                </span><span>ReferenceArray</span><span> references </span><span>=</span><span> dimension</span><span>.</span><span>References</span><span>;</span><span>
                </span><span>Dimension</span><span> newDimension </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewDimension</span><span>(</span><span>view</span><span>,</span><span> line</span><span>,</span><span> references</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Though only linear dimensions are created, you can delete all dimensions and constraints represented by Dimension and SpotDimension using the Document.Delete() method.

### Manipulating Dimension Text and Leader

Access to several attributes of the dimension are available with:

-   DimensionType.Prefix
-   DimensionType.Suffix
-   Dimension.TextPosition
-   Dimension.LeaderEndPosition
-   Dimension.HasLeader

Dimension and DimensionSegment classes provide similar properties and methods for querying and adjusting the position of the text relative to the dimension curve.

Dimension.Origin returns the XYZ value of the midpoint of the dimension curve, with DimensionSegment.Origin will return the midpoint of the line that makes up the segment.

Determine if text position of a Dimension or DimensionSegment is adjustable by calling the method IsTextPositionAdjustable() which will indicate whether the text and leader positions may be set.

Query or modify the position of text or the leader (of a dimension or dimension segment) by using the properties TextPosition and LeaderEndPosition.

Reset the text to its default position on a dimension by calling the method ResetTextPosition().

Note: TextPosition and LeaderEndPosition are not necessarily applicable to all dimensions (e.g., spot dimensions, multi-segment dimensions using the equality constraint, when dimension style is ordinate). If these values are not applicable they will return Null and not allow setting a value.

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_C549BB7C6DA14A06ABF34AC24C3077E6"><tbody><tr><td><b>Code Region: Reposition dimension text</b></td></tr><tr><td><pre><code><span>// Moves all of the text in this dimension one unit in the Y direction</span><span>
</span><span>public</span><span> </span><span>bool</span><span> </span><span>DimensionTextReposition</span><span>(</span><span>Dimension</span><span> dimToModify</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> modified </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>dimToModify </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>return</span><span> </span><span>false</span><span>;</span><span>

    </span><span>// Check to see if we have a non-multisegment dimension and if text position is adjustable</span><span>
    </span><span>if</span><span> </span><span>(</span><span>dimToModify</span><span>.</span><span>NumberOfSegments</span><span> </span><span>==</span><span> </span><span>0</span><span> </span><span>&amp;&amp;</span><span> dimToModify</span><span>.</span><span>IsTextPositionAdjustable</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>// Get the current text XYZ position</span><span>
        XYZ currentTextPosition </span><span>=</span><span> dimToModify</span><span>.</span><span>TextPosition</span><span>;</span><span>
        </span><span>// Calculate a new XYZ position by transforming the current text position</span><span>
        XYZ newTextPosition </span><span>=</span><span> </span><span>Transform</span><span>.</span><span>CreateTranslation</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0.0</span><span>,</span><span> </span><span>1.0</span><span>,</span><span> </span><span>0.0</span><span>)).</span><span>OfPoint</span><span>(</span><span>currentTextPosition</span><span>);</span><span>
        </span><span>// Set the new text position</span><span>
        dimToModify</span><span>.</span><span>TextPosition</span><span> </span><span>=</span><span> newTextPosition</span><span>;</span><span>

        modified </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>dimToModify</span><span>.</span><span>NumberOfSegments</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>DimensionSegment</span><span> currentSegment </span><span>in</span><span> dimToModify</span><span>.</span><span>Segments</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>currentSegment </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> currentSegment</span><span>.</span><span>IsTextPositionAdjustable</span><span>())</span><span>
            </span><span>{</span><span>
                modified </span><span>=</span><span> </span><span>true</span><span>;</span><span>
                </span><span>// Get the current text XYZ position</span><span>
                XYZ currentTextPosition </span><span>=</span><span> currentSegment</span><span>.</span><span>TextPosition</span><span>;</span><span>
                </span><span>// Calculate a new XYZ position by transforming the current text position</span><span>
                XYZ newTextPosition </span><span>=</span><span> </span><span>Transform</span><span>.</span><span>CreateTranslation</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>)).</span><span>OfPoint</span><span>(</span><span>currentTextPosition</span><span>);</span><span>
                </span><span>// Set the new text position for the segment's text</span><span>
                currentSegment</span><span>.</span><span>TextPosition</span><span> </span><span>=</span><span> newTextPosition</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>return</span><span> modified</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Dimensions and Constraints  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Detail Curve  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:27 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_Detail_Curve_html
author: 
---

# Help | Detail Curve | Autodesk

> ## Excerpt
> Detail curve is an important Detail component usually used in the detail or drafting view. Detail curves are accessible in the DetailCurve class and its derived classes.

---
Detail curve is an important Detail component usually used in the detail or drafting view. Detail curves are accessible in the DetailCurve class and its derived classes.

DetailCurve is view-specific as are other annotation elements. However, there is no DetailCurve.View property. When creating a detail curve, you must compare the detail curve to the model curve view.

|| |--- | |Code Region 16-4: NewDetailCurve() and NewModelCurve()| |`public DetailCurve NewDetailCurve (View, Curve)`| |`public ModelCurve NewModelCurve (Curve, SketchPlane)`|

Generally only 2D views such as level view and elevation view are acceptable, otherwise an exception is thrown.

Except for view-related features, DetailCurve is very similar to ModelCurve. For more information about ModelCurve properties and usage, see [ModelCurve](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_ModelCurve_html) in the [Sketching](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_html) section.


<!-- ===== END: Help  Detail Curve  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Tags  Autodesk.md ===== -->

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


<!-- ===== END: Help  Tags  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Text  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:37 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_Text_html
author: 
---

# Help | Text | Autodesk

> ## Excerpt
> Text and associated leaders can be accessed from the TextNote class.
Note

---
Text and associated leaders can be accessed from the TextNote class. Note

A TextNote can have plain text or formatted text. The overloaded TextNote.Create() method provides options for creating unwrapped and line-wrapping text note elements. The width for the area of the text content can be specified on creation, but is restricted by a minimum and maximum width that is based on properties of the text and its type. The overloaded methods GetMinimumAllowedWidth() and GetMaximumAllowedWidth(), inherited from TextElement, return the constraints for either a specific TextNote or for a given document and text type id.

The following example creates a new TextNote at a user specified point and with a given width and TextNoteOptions.

<table summary="" id="GUID-20EA0F3C-7EAD-44DD-96A6-DB2933741561__TABLE_E9824E5167E64B28B657C8145321BEE4"><tbody><tr><td><b>Code Region: Create a TextNote</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>TextNote</span><span> </span><span>AddNewTextNote</span><span>(</span><span>UIDocument</span><span> uiDoc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> uiDoc</span><span>.</span><span>Document</span><span>;</span><span>
    XYZ textLoc </span><span>=</span><span> uiDoc</span><span>.</span><span>Selection</span><span>.</span><span>PickPoint</span><span>(</span><span>"Pick a point for sample text."</span><span>);</span><span>
    </span><span>ElementId</span><span> defaultTextTypeId </span><span>=</span><span> doc</span><span>.</span><span>GetDefaultElementTypeId</span><span>(</span><span>ElementTypeGroup</span><span>.</span><span>TextNoteType</span><span>);</span><span>
    </span><span>double</span><span> noteWidth </span><span>=</span><span> </span><span>.</span><span>2</span><span>;</span><span>

    </span><span>// make sure note width works for the text type</span><span>
    </span><span>double</span><span> minWidth </span><span>=</span><span> </span><span>TextNote</span><span>.</span><span>GetMinimumAllowedWidth</span><span>(</span><span>doc</span><span>,</span><span> defaultTextTypeId</span><span>);</span><span>
    </span><span>double</span><span> maxWidth </span><span>=</span><span> </span><span>TextNote</span><span>.</span><span>GetMaximumAllowedWidth</span><span>(</span><span>doc</span><span>,</span><span> defaultTextTypeId</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>noteWidth </span><span>&lt;</span><span> minWidth</span><span>)</span><span>
    </span><span>{</span><span>
        noteWidth </span><span>=</span><span> minWidth</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>noteWidth </span><span>&gt;</span><span> maxWidth</span><span>)</span><span>
    </span><span>{</span><span>
        noteWidth </span><span>=</span><span> maxWidth</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TextNoteOptions</span><span> opts </span><span>=</span><span> </span><span>new</span><span> </span><span>TextNoteOptions</span><span>(</span><span>defaultTextTypeId</span><span>);</span><span>
    opts</span><span>.</span><span>HorizontalAlignment</span><span> </span><span>=</span><span> </span><span>HorizontalTextAlignment</span><span>.</span><span>Left</span><span>;</span><span>
    opts</span><span>.</span><span>Rotation</span><span> </span><span>=</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>4</span><span>;</span><span>

    </span><span>TextNote</span><span> textNote </span><span>=</span><span> </span><span>TextNote</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> doc</span><span>.</span><span>ActiveView</span><span>.</span><span>Id</span><span>,</span><span> textLoc</span><span>,</span><span> noteWidth</span><span>,</span><span> </span><span>"New sample text"</span><span>,</span><span> opts</span><span>);</span><span>

    </span><span>return</span><span> textNote</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Whether a TextNote has plain or formatted text, the unformatted text can always be retrieved from the TextNote.Text property.

## FormattedText

When first created, the TextNote will have plain text. Use the TextNote.GetFormattedText() method to get a FormattedText object for the TextNote. The FormattedText class can be used to apply various formatting to the text such as bold, underline, superscript or all caps. The TextNote is not updated until SetFormattedText() is called with the modified FormattedText.

The text in the FormattedText can be formatted in whole or in part using a TextRange. A TextRange specifies a start index and length based on the text in the FormattedText object. When the overload of a formatting method (such as SetItalicStatus() or SetAllCapsStatus()) uses a TextRange, only the characters within the range will be modified. A TextRange can be defined explicitly using its constructor, or can be retrieved using the FormattedText.Find() method to get the range for a given search string. The Find() method specifies a start index for the search, as well as whether to match the case of the search string or whether to do a whole word search. If the text in the search string is not found or if the given start index is beyond the end of the length of the entire text, an empty TextRange will be returned. Before using the returned range to set formatting on the text, ensure that it is not empty to avoid an exception.

The following example demonstrates how to format text from a TextNote and set it back to the TextNote. It uses the Find() method to bold and underline specific words in the text.

<table summary="" id="GUID-20EA0F3C-7EAD-44DD-96A6-DB2933741561__TABLE_D876E5F2B13B43758BA1616D20458D9A"><tbody><tr><td><b>Code Region: Format text in a TextNote</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FormatText</span><span>(</span><span>TextNote</span><span> textNote</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// TextNote created with "New sample text"</span><span>
    </span><span>FormattedText</span><span> formatText </span><span>=</span><span> textNote</span><span>.</span><span>GetFormattedText</span><span>();</span><span>

    </span><span>// italicize "New"</span><span>
    </span><span>TextRange</span><span> range </span><span>=</span><span> </span><span>new</span><span> </span><span>TextRange</span><span>(</span><span>0</span><span>,</span><span> </span><span>3</span><span>);</span><span>
    formatText</span><span>.</span><span>SetItalicStatus</span><span>(</span><span>range</span><span>,</span><span> </span><span>true</span><span>);</span><span>

    </span><span>// make "sample" bold</span><span>
    range </span><span>=</span><span> formatText</span><span>.</span><span>Find</span><span>(</span><span>"sample"</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>false</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>range</span><span>.</span><span>Length</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
        formatText</span><span>.</span><span>SetBoldStatus</span><span>(</span><span>range</span><span>,</span><span> </span><span>true</span><span>);</span><span>

    </span><span>// make "text" underlined</span><span>
    range </span><span>=</span><span> formatText</span><span>.</span><span>Find</span><span>(</span><span>"text"</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>false</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>range</span><span>.</span><span>Length</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
        formatText</span><span>.</span><span>SetUnderlineStatus</span><span>(</span><span>range</span><span>,</span><span> </span><span>true</span><span>);</span><span>

    </span><span>// make all text uppercase</span><span>
    formatText</span><span>.</span><span>SetAllCapsStatus</span><span>(</span><span>true</span><span>);</span><span>

    textNote</span><span>.</span><span>SetFormattedText</span><span>(</span><span>formatText</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

New text can be added to existing text in a FormattedText object. The SetPlainText() method will either replace some existing text if the overload that has a TextRange parameter is used, or will replace the entire text if not. To insert text without replacing existing text, use a TextRange with a Length of 0. The new text will be inserted at the index specified by the TextRange.Start property. Note that when inserting text, it may pick up the formatting of the adjacent text, similar to how pasting unformatted text into a Word document will result in text with the current formatting for the insertion point. If formatting has been applied to the entire FormattedText as in the case of the SetAllCapsStatus(true) call in the example above, that formatting will be applied to any new text that is inserted.

In the following example, new text is appended to the end of existing text by first finding the end of the current text and setting that as the Start of the range to be added. It also demonstrates how to create a list (which can be bulleted, numbered or lettered). Note that it also calls GetAllCapsStatus() for the range of the new text and turns off caps if the status is not FormatStatus.None (other options are All and Mixed).

<table summary="" id="GUID-20EA0F3C-7EAD-44DD-96A6-DB2933741561__TABLE_22EAB389169945059F11CCED3E82C731"><tbody><tr><td><b>Code Region: Inserting new text</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>AppendText</span><span>(</span><span>TextNote</span><span> textNote</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FormattedText</span><span> formatText </span><span>=</span><span> textNote</span><span>.</span><span>GetFormattedText</span><span>();</span><span>

    </span><span>TextRange</span><span> range </span><span>=</span><span> formatText</span><span>.</span><span>AsTextRange</span><span>();</span><span>

    range</span><span>.</span><span>Start</span><span> </span><span>=</span><span> range</span><span>.</span><span>End</span><span> </span><span>-</span><span> </span><span>1</span><span>;</span><span>
    </span><span>// set Length to 0 to insert</span><span>
    range</span><span>.</span><span>Length</span><span> </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>string</span><span> someNewText </span><span>=</span><span> </span><span>"\rThis is a new paragraph\vThis is a new line without a paragraph break\r"</span><span>;</span><span>
    formatText</span><span>.</span><span>SetPlainText</span><span>(</span><span>range</span><span>,</span><span> someNewText</span><span>);</span><span>

    </span><span>// get range for entire text</span><span>
    range </span><span>=</span><span> formatText</span><span>.</span><span>AsTextRange</span><span>();</span><span>
    range</span><span>.</span><span>Start</span><span> </span><span>=</span><span> range</span><span>.</span><span>End</span><span> </span><span>-</span><span> </span><span>1</span><span>;</span><span>
    range</span><span>.</span><span>Length</span><span> </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>string</span><span> someListText </span><span>=</span><span> </span><span>"\rBulleted List item 1\rItem 2\vSecond line for Item 2\rThird bullet point"</span><span>;</span><span>
    formatText</span><span>.</span><span>SetPlainText</span><span>(</span><span>range</span><span>,</span><span> someListText</span><span>);</span><span>
    range</span><span>.</span><span>Start</span><span>++;</span><span>
    range</span><span>.</span><span>Length</span><span> </span><span>=</span><span> someListText</span><span>.</span><span>Length</span><span>;</span><span>
    formatText</span><span>.</span><span>SetListType</span><span>(</span><span>range</span><span>,</span><span> </span><span>ListType</span><span>.</span><span>Bullet</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>formatText</span><span>.</span><span>GetAllCapsStatus</span><span>(</span><span>range</span><span>)</span><span> </span><span>!=</span><span> </span><span>FormatStatus</span><span>.</span><span>None</span><span>)</span><span>
    </span><span>{</span><span>
        formatText</span><span>.</span><span>SetAllCapsStatus</span><span>(</span><span>range</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    </span><span>}</span><span>

    textNote</span><span>.</span><span>SetFormattedText</span><span>(</span><span>formatText</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The code above shows how to use \\r to create a line break, and \\v for a vertical tab that does not break the paragraph. In the text for the bulleted list, a "\\v" is used to create a two line bullet point. A new bullet is only inserted when using "\\r".

## Text Editor

The TextEditorOptions class can be used to control the appearance and functionality of the text editor in Revit. These settings are saved in the Revit.ini file and are not tied to the document.

The Revit.ini file is in the folder returned by the property Autodesk.Revit.ApplicationServices.Application.CurrentUsersDataFolderPath (such as %appdata%\\Autodesk\\Revit\\Autodesk Revit 2019)

<table summary="" id="GUID-20EA0F3C-7EAD-44DD-96A6-DB2933741561__TABLE_2E781709FC9148A4AA725B45242F3C38"><tbody><tr><td><b>Code Region: Setting text editor options</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SetEditorOptions</span><span>()</span><span>
</span><span>{</span><span>
    </span><span>TextEditorOptions</span><span> editorOptions </span><span>=</span><span> </span><span>TextEditorOptions</span><span>.</span><span>GetTextEditorOptions</span><span>();</span><span>
    editorOptions</span><span>.</span><span>ShowBorder</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    editorOptions</span><span>.</span><span>ShowOpaqueBackground</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Leaders

Revit supports two kinds of Leaders: straight leaders and arc leaders. Leaders can be added to a TextNote using the AddLeader() method, specifying the leader type using the TextNoteLeaderType enumerated type:

**Table 39: Leader Types**

Note: Straight leaders and arc leaders cannot be added to a Text type at the same time.

The TextNote.LeaderCount property returns the number of leaders and the GetLeaders() method returns all leaders currently attached to the text component. LeaderLeftAttachment and LeaderRightAttachment indicate the attachment position of the leaders on the corresponding side of the TextNote. Options for the LeaderAttachment are TopLine, MidPoint, and BottomLine. Use the RemoveLeaders() method to remove all leaders from the TextNote.


<!-- ===== END: Help  Text  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Annotation Symbol  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_Annotation_Symbol_html
author: 
---

# Help | Annotation Symbol | Autodesk

> ## Excerpt
> An annotation symbol is a symbol applied to a family to uniquely identify that family in a project.

---
An annotation symbol is a symbol applied to a family to uniquely identify that family in a project.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-75864163-28D5-496D-9077-98DFECA07E75-low.png)**Figure 76: Annotation Symbol with two leaders**

### Create and Delete

Annotation symbols can be created using the following overload of the Creation.Document.NewFamilyInstance() method:

<table summary="" id="GUID-83D2CDC1-19FE-4BEE-B915-015D7B0BD72D__TABLE_8B7650612D22449C9FBC0D3E9238C245"><tbody><tr><td><b>Code Region 16-6: Create a new Annotation Symbol</b></td></tr><tr><td><p><code>public FamilyInstance NewFamilyInstance Method (XYZ origin, FamilySymbol symbol, View specView)</code></p></td></tr></tbody></table>

The annotation symbol can be deleted using the Document.Delete() method.

### Add and Remove Leader

Add and remove leaders using the addLeader() and removeLeader() methods.

<table summary="" id="GUID-83D2CDC1-19FE-4BEE-B915-015D7B0BD72D__TABLE_A2E9307AE06C42289884199FEED72D32"><tbody><tr><td><b>Code Region 16-7: Using addLeader() and removeLeader()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>AddAndRemoveLeaders</span><span>(</span><span>AnnotationSymbol</span><span> symbol</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// check if there are any leaders currently attached, and remove them</span><span>
    </span><span>IList</span><span>&lt;</span><span>Leader</span><span>&gt;</span><span> leaders </span><span>=</span><span> symbol</span><span>.</span><span>GetLeaders</span><span>();</span><span>

    </span><span>if</span><span> </span><span>(</span><span>leaders </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> leaders</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>for</span><span> </span><span>(</span><span>int</span><span> i </span><span>=</span><span> leaders</span><span>.</span><span>Count</span><span>;</span><span> i </span><span>&gt;</span><span> </span><span>0</span><span>;</span><span> i</span><span>--)</span><span>
        </span><span>{</span><span>
            symbol</span><span>.</span><span>removeLeader</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// add one new leader instead</span><span>
    symbol</span><span>.</span><span>addLeader</span><span>();</span><span>                                                    
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Annotation Symbol  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Color Fill  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:46 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_Color_Fill_html
author: 
---

# Help | Color Fill | Autodesk

> ## Excerpt
> Autodesk.Revit.DB.ColorFillLegend supports creating, reading and modifying properties of color fill legend annotation elements in a particular view. The static method ColorFillLegend.Create(document, viewId, categoryId, origin) lets you to create a new color fill legend in a view.

---
## Color Fill Legend

`Autodesk.Revit.DB.ColorFillLegend` supports creating, reading and modifying properties of color fill legend annotation elements in a particular view. The static method `ColorFillLegend.Create(document, viewId, categoryId, origin)` lets you to create a new color fill legend in a view.

## Color Fill Scheme

The color fill scheme definition includes:

-   The category (such as Rooms).
-   The parameter whose value will be used to color the elements (such as Name, Floor Finish, or Department).
-   If the coloring will be done by range of values (such as at least 40SF' and less than 80SF') or by specific values (such as equal to 40SF').
-   The list of `ColorFillSchemeEntry` items.

Key members of `Autodesk.Revit.DB.ColorFillScheme` relating to these attributes are:

-   CategoryId
-   ParameterDefinition
-   IsByRange
-   AddEntry()/DeleteEntry()
-   GetEntries()/SetEntries()

### Color Fills Schemes used by a view

A view can define one `ColorFillScheme` for spatial elements (rooms, zones, spaces, and areas), one for pipes, and one for ducts. You can get and set these schemes with

-   View.GetColorFillSchemeId(categoryId)
-   View.SetColorFillSchemeId(categoryId, schemeId)

## Color Fill Scheme Entries

The color fill scheme entry definition includes:

-   The color.
-   The fill pattern.
-   The caption shown in the Color Fill Legend (such as 100 SF' or more).
-   The parameter value that will apply to this entry.

The `Autodesk.Revit.DB.ColorFillSchemeEntry` class provides all functionality needed to create, read, and modify these entries

**Code Region: Creating a Color Fill Legend**

```
private void CreateColorFill(View v)
{
    Document doc = v.Document;
    ElementId roomCatId = new ElementId(BuiltInCategory.OST_Rooms);
    using (Transaction t = new Transaction(v.Document, "Create Color Fill Legend"))
    {
        t.Start();
        if (v.GetColorFillSchemeId(roomCatId) == ElementId.InvalidElementId)
        {
            v.SetColorFillSchemeId(
                roomCatId, 
                new FilteredElementCollector(doc)
                    .OfClass(typeof(ColorFillScheme))
                    .Cast<ColorFillScheme>()
                    .First(q => q.CategoryId == roomCatId).Id);
        }
        ColorFillLegend.Create(v.Document, v.Id, roomCatId, XYZ.Zero);
        t.Commit();
    }
}
```

**Code Sample - Create and Apply a Color Fill Scheme**

```
private void NewColorScheme(View v)
{
    Document doc = v.Document;
    ColorFillScheme scheme = doc.GetElement(
        v.GetColorFillSchemeId(
            new ElementId(BuiltInCategory.OST_Rooms))) as ColorFillScheme;

    using (Transaction t = new Transaction(doc, "New Color Scheme"))
    {
        t.Start();

        ElementId newSchemeId = scheme.Duplicate("Color By Room Finish");
        ColorFillScheme newScheme = doc.GetElement(newSchemeId) as ColorFillScheme;
        newScheme.Title = "Room Finish";
        newScheme.ParameterDefinition = new ElementId(BuiltInParameter.ROOM_FINISH_BASE);        

        v.SetColorFillSchemeId(new ElementId(BuiltInCategory.OST_Rooms), newSchemeId);

        t.Commit();
    }
}
```

**Code Sample - Add an entry to a ColorFillScheme**

```
private void AddColorFillSchemeEntry(ColorFillScheme scheme)
{
    Document doc = scheme.Document;
    ColorFillSchemeEntry entry = new ColorFillSchemeEntry(StorageType.String)
    {
        Color = new Color(25, 0, 0),
        FillPatternId = new FilteredElementCollector(doc)
            .OfClass(typeof(FillPatternElement))
            .Cast<FillPatternElement>()
            .First(a => a.GetFillPattern().IsSolidFill)
            .Id
    };
    entry.SetStringValue("Tile");
    using (Transaction t = new Transaction(doc, "Add Scheme Entry"))
    {
        t.Start();
        scheme.AddEntry(entry);
        t.Commit();
    }
}
```

**Code Sample - Modify entries of a ColorFillScheme**

```
private void ModifyColorFillSchemeEntries(ColorFillScheme scheme)
{
    Document doc = scheme.Document;
    IList<ColorFillSchemeEntry> entries = scheme.GetEntries();
    foreach (ColorFillSchemeEntry entry in entries)
    {
        entry.FillPatternId = new FilteredElementCollector(doc)
        .OfClass(typeof(FillPatternElement))
        .Cast<FillPatternElement>()
        .First(a => a.Name == "Crosshatch")
        .Id;
    }
    using (Transaction t = new Transaction(doc, "Modify entry"))
    {
        t.Start();
        scheme.SetEntries(entries);
        t.Commit();
    }
}
```


<!-- ===== END: Help  Color Fill  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Geometry  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:51 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html
author: 
---

# Help | Geometry | Autodesk

> ## Excerpt
> The Autodesk.Revit.DB namespace contains many classes related to geometry and graphic-related types used to describe the graphical representation in the API. The geometry-related classes include:

---
The Autodesk.Revit.DB namespace contains many classes related to geometry and graphic-related types used to describe the graphical representation in the API. The geometry-related classes include:

-   [GeometryObject class](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_html) - Includes classes derived from the GeometryObject class.
-   [Geometry Helper Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Helper_Classes_html) - Includes classes derived from the APIObject class and value types
-   [Geometry Utility Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Utility_Classes_html) - Includes classes to create non-element geometry and to find intersections of solids
-   [Collection Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Collection_Classes_html) - Includes classes derived from the IEnumerable or IEnumerator interface.

In this section, you learn how to use various graphic-related types, how to retrieve geometry data from an element, how to transform an element, and more.


<!-- ===== END: Help  Geometry  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  GeometryObject Class  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:00 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_html
author: 
---

# Help | GeometryObject Class | Autodesk

> ## Excerpt
> The indexed property Element.Geometry[] can be used to pull the geometry of any model element (3D element). This applies both to system family instances such as walls, floors and roofs, and also to family instances of many categories, e.g. doors, windows, furniture, or masses.

---
The indexed property Element.Geometry\[\] can be used to pull the geometry of any model element (3D element). This applies both to system family instances such as walls, floors and roofs, and also to family instances of many categories, e.g. doors, windows, furniture, or masses.

The property GeometryObject.Id returns an integer value which may be used to identify the GeometryObject in its associated GeometryElement when the value is non-negative and not duplicated by other GeometryObjects in the associated GeometryElement.

The extracted geometry is returned to you as Autodesk.Revit.DB.GeometryElement. You can iterate through the geometry members of that element by using the GetEnumerator() method.

Typically, the objects returned at the top level of the extracted geometry will be one of:

-   [Solids, Faces and Edges](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_html) – a boundary representation made up of faces and edges
-   [Meshes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Meshes_html) – a 3D array of triangles
-   [Curves](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_html) – a bounded 3D curve
-   [Points](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Points_html) – a visible point datum at a given 3D location
-   [PolyLines](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_PolyLines_html) – a series of line segments defined by 3D points
-   [GeometryInstances](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_GeometryInstances_html) – an instance of a geometric element positioned within the element

This figure illustrates the hierarchy of objects found by geometry extraction.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/geometry_hierarchy.png)


<!-- ===== END: Help  GeometryObject Class  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Curves  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_html
author: 
---

# Help | Curves | Autodesk

> ## Excerpt
> Share

---
Share

A curve represents a path in 2 or 3 dimensions in the Revit model. Curves may represent the entire extent of an element’s geometry (e.g. CurveElements) or may appear as a single piece of the geometry of an element (e.g. the centerline of a wall or duct). Curves and collections of curves are used as inputs in many element creation methods in the API.

**Pages in this section**

-   [Curve analysis](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_analysis_html)
-   [Working with Curves](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Working_with_Curves_html)
-   [Curve collections](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_collections_html)
-   [Curve creation](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_creation_html)
-   [Curve Parameterization](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_Parameterization_html)
-   [Curve types](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_types_html)
-   [Mathematical representations of curve types](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Mathematical_representations_of_curve_types_html)

**Parent page:** [GeometryObject Class](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_html)

### Was this information helpful?

-   Yes
-   No


<!-- ===== END: Help  Curves  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Curve analysis  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_analysis_html
author: 
---

# Help | Curve analysis | Autodesk

> ## Excerpt
> There are several Curve methods which are tools suitable for use in geometric analysis.

---
There are several Curve methods which are tools suitable for use in geometric analysis.

In some cases, these APIs do more than you might expect by a quick review of their names.

### Intersect()

The Intersect method allows you compare two curves to find how they differ or how they are similar. It can be used in the manner you might expect, to obtain the point or point(s) where two curves intersect one another, but it can also be used to identify:

-   Collinear lines
-   Overlapping lines
-   Identical curves
-   Totally distinct curves with no intersections

The return value identifies these different results, and the output IntersectionSetResult contains information on the intersection point(s).

### Project()

The Project method projects a point onto the curve and returns information about the nearest point on the curve, its parameter, and the distance from the projection point.

### Tessellate()

This splits the curve into a series of linear segments, accurate within a default tolerance. For Curve.Tessellate(), the tolerance is slightly larger than 1/16”. This tolerance of approximation is the tolerance used internally by Revit as adequate for display purposes.

Note that only lines may be split into output of only two tessellation points; non-linear curves will always output more than two points even if the curve has an extremely large radius which might mathematically equate to a straight line.


<!-- ===== END: Help  Curve analysis  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Working with Curves  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Working_with_Curves_html
author: 
---

# Help | Working with Curves | Autodesk

> ## Excerpt
> The Curve class provides useful methods for working with curves.

---
The Curve class provides useful methods for working with curves.

In addition to [methods that are useful for analysis](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_analysis_html "There are several Curve methods which are tools suitable for use in geometric analysis.") , the Curve class provides properties and methods to modify a curve or get basic information about it.

## Changing bounds

The MakeBound() method can be used to change the bounds of a curve or to create bounds for a previously unbound curve. MakeUnbound() will make the curve unbound. For both methods, if the curve is marked as read-only (because it was extracted directly from a Revit element or collection/aggregation object), calling this method causes the object to be changed to carry a disconnected copy of the original curve. The modification will not affect the original curve or the object that supplied it.

## Graphics style

Curve inherits the GraphicsStyleId read-only property from GeometryObject, which provides the ElementId of the GraphicsStyle assigned to the Curve. The method Curve.SetGraphicsStyleId() can be used to set the GraphicsStyle Id of the Curve. Many methods in the Revit API will not use the graphics style associated to this curve. For example, curves used as portions of the sketch of an element will not read this property. Newly created curve elements will not use this value either, as they inherit their graphical properties from their associated category.

## Curve length

Curve has two properties associated with length. The Length property will return the exact length of the curve. I computes the length of the curve using analytical or numeric integration. There is no performance hit for lines and arcs. For a faster approximation, the ApproximateLength property quickly estimates the length of the curve, but it may deviate by a factor of 2 in some cases. This computation is exact for lines and arcs.


<!-- ===== END: Help  Working with Curves  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Curve collections  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_collections_html
author: 
---

# Help | Curve collections | Autodesk

> ## Excerpt
> The Revit API uses different types of collections of curves as inputs.

---
The Revit API uses different types of collections of curves as inputs.

**Note**: Newer API methods use .NET collections of Curves in place of CurveArray and CurveArrArray.

## CurveLoop

A CurveLoop represents a specific chain of curves joined end-to-end. It can represent a closed loop or an open one. The members of the CurveLoop may be directly iterated, as the class implements `IEnumerable<Curve>`. The iteration provides copies of the curves directly contained in the loop; modification of the curves will not affect the curves that are contained in the loop. CurveLoops can be created using:

-   CurveLoop.Create() - creates a new CurveLoop from a list of curves.
-   CurveLoop.CreateViaCopy() - creates a new CurveLoop as a copy of an existing CurveLoop.
-   CurveLoop.CreateViaThicken(Curve, double, XYZ) - creates a new closed CurveLoop by thickening the input curve with respect to a given plane.
-   CurveLoop.CreateViaThicken(CurveLoop, double, XYZ) -creates a new closed curve loop by thickening the input open curve loop with respect to a given plane.
-   CurveLoop.CreateViaTransform() - creates a new CurveLoop as a transformed copy of the input CurveLoop. Note that the thickness parameter for the overloaded CreateViaThicken() method must result in a curve which exceed Revit's short curve tolerance (Application.ShortCurveTolerance), otherwise an exception will be thrown.

`CurveLoop.Transform()` performs similarly to CreateViaTransform(), but it transforms the curves contained within the CurveLoop rather than creating a transformed copy.

`CurveLoop.NumberOfCurves` returns the number of curves in the curve loop.

`CurveLoop.CreateViaOffset()` creates a new curve loop that is an offset of the existing curve loop. This can be done in two ways:

-   With a single offset distance
-   With an array of offset distances. The size of this array must match the size of the curve loop. The curve at position i will be offset with the double at position i in the array.

### CurveArray

This collection class represents an arbitrary collection of curves. Create it using its constructor.

### CurveArrArray

This collection class is a collection of CurveArrays. When this is used, the organization of the sub-elements of this array have meaning for the method this is passed to; for example, in NewExtrusion() multiple CurveArrays should represent different closed loops.


<!-- ===== END: Help  Curve collections  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Curve creation  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_creation_html
author: 
---

# Help | Curve creation | Autodesk

> ## Excerpt
> Curves are often needed as inputs to Revit API methods. They can be created a number of ways.

---
Curves are often needed as inputs to Revit API methods. They can be created a number of ways.

Curves have a number of derived types with static methods for curve creation. The base Curve class also has methods for creating new Curves from existing curves.

Curve creation methods prevent creation of curves that are shorter than Revit's tolerance. This tolerance is exposed through the Application.ShortCurveTolerance property.

### Curve

The Curve class has several methods for creating new curves from existing curves.

-   Clone() - creates a copy of this Curve.
-   CreateOffset() - creates a new curve offset from this one.
-   CreateReversed() - creates a new curve with the opposite orientation of the existing curve
-   Curve.CreateTransformed() - creates a new instance of a curve as a transformation of this curve.
    
    ### Line
    

There are two static methods for creating a new Line.

-   CreateBound() - creates a new bound linear curve between two points.
-   CreateUnbound() - creates a new unbound linear curve given an origin and a direction.

<table summary="" id="GUID-A1BCB8D4-5628-45AF-B399-AF573CBBB1D0__TABLE_0860632902034A54B3FF48179F4DC114"><tbody><tr><td><b>Code Region: Create an unbound linear curve</b></td></tr><tr><td><pre><code><span>// define start point and direction for unbound line</span><span>
XYZ startPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
XYZ directionPt </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>10</span><span>);</span><span>

</span><span>// create line</span><span>
</span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateUnbound</span><span>(</span><span>startPoint</span><span>,</span><span> directionPt</span><span>);</span></code></pre></td></tr></tbody></table>

### Arc

The overloaded static Create() method allows for an Arc to be created in one of three ways:

-   based on 3 points

<table summary="" id="GUID-A1BCB8D4-5628-45AF-B399-AF573CBBB1D0__TABLE_F482D6FE1A2C44C18A55CEC422A75C31"><tbody><tr><td><b>Code Region: Create arc with 3 points</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ThreePointArc</span><span>()</span><span>
</span><span>{</span><span>
</span><span>// Create a new arc using two ends and a point on the curve</span><span>
    XYZ end0 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>    </span><span>// start point of the arc</span><span>
    XYZ end1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>10</span><span>);</span><span> </span><span>// end point of the arc</span><span>
    XYZ pointOnCurve </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>   </span><span>// point along arc</span><span>

    </span><span>Arc</span><span> arc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>end0</span><span>,</span><span> end1</span><span>,</span><span> pointOnCurve</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

-   based on a plane, radius, and angles

<table summary="" id="GUID-A1BCB8D4-5628-45AF-B399-AF573CBBB1D0__TABLE_2B3F36E3793947179C063DDB5AE29C8B"><tbody><tr><td><b>Code Region: Create arc with plane</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Arc</span><span> </span><span>CreateArcByGivingPlane</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Plane</span><span> plane</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Create an arc which is placed on the plane and whose center is the plane's origin</span><span>
        </span><span>double</span><span> radius </span><span>=</span><span> </span><span>10</span><span>;</span><span>
        </span><span>double</span><span> startAngle </span><span>=</span><span> </span><span>0</span><span>;</span><span>      </span><span>// The unit is radian</span><span>
        </span><span>double</span><span> endAngle </span><span>=</span><span> </span><span>2</span><span> </span><span>*</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>;</span><span>        </span><span>// this arc will be a circle</span><span>
        </span><span>return</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>plane</span><span>,</span><span> radius</span><span>,</span><span> startAngle</span><span>,</span><span> endAngle</span><span>);</span><span>
    </span><span>}</span></code></pre></td></tr></tbody></table>

-   based on center, radius, angles and two axes

<table summary="" id="GUID-A1BCB8D4-5628-45AF-B399-AF573CBBB1D0__TABLE_B584F1155A84425D98290E33ACEE7654"><tbody><tr><td><b>Code Region: Create arc with axes</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateArcByCenterRadius</span><span>()</span><span>
</span><span>{</span><span>
    </span><span>// Create a new arc defined by its center, radius, angles and 2 axes</span><span>
    </span><span>double</span><span> radius </span><span>=</span><span> </span><span>10</span><span>;</span><span>
    </span><span>double</span><span> startAngle </span><span>=</span><span> </span><span>0</span><span>;</span><span>      </span><span>// In radian</span><span>
    </span><span>double</span><span> endAngle </span><span>=</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>;</span><span>        </span><span>// In radian</span><span>
    XYZ center </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ xAxis </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>   </span><span>// The x axis to define the arc plane. Must be normalized</span><span>
    XYZ yAxis </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>   </span><span>// The y axis to define the arc plane. Must be normalized</span><span>

    </span><span>Arc</span><span> arc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>center</span><span>,</span><span> radius</span><span>,</span><span> startAngle</span><span>,</span><span> endAngle</span><span>,</span><span> xAxis</span><span>,</span><span> yAxis</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note for the latter two options, if the angle range is equal to or greater than 2 \* PI, the curve will be automatically converted to an unbounded circle.

### Ellipse

The static CreateCurve() method creates an Ellipse given the center, the x vector and y vector radii of the ellipse, the x and y axes to define the plane of the ellipse and the start and end parameters. If the x-radius and y-radius are almost equal it will return an arc, otherwise it will return an ellipse.

### Cylindrical Helix

The static Create() method of CylindricalHelix creates a new CylindricalHelix from the base point of the axis, a radius, x vector, z vector, pitch, a start angle to specify the start point of the helix and an end angle to specify the end point of the helix. The z vector is the axis direction and should be perpendicular to the x vector. A positive pitch yields a right-handed helix while a negative pitch yields a left-handed helix.

### NURBS

The NurbSpline class represents a NURBS, or Non-Uniform Rational B-Spline, curve. The overloaded static CreateCurve() method offers multiple ways to create a NURBS curve. The first way is using the same calculations that Revit uses when sketching splines in the user interface. It takes a list of control points and weights to create a new NurbSpline. Knots and degree of the spline are computed from the given control points and weights.

A second option also requires a list of control points and weights, but also a list of knots as well as the degree of the NurbSpline. The degree must be 1 or greater. There must be at least degree+1 control points. The size of knots must equal the sum of degree, the size of the control points array and 1. The first degree+1 knots should be identical, as should the last degree+1 knots. The knots in the middle of the sequence must be non-decreasing.

A third option only requires control points and weights. There must be at least 2 control points and the number of weights must be equal to the number of control points. The values of all weights must be positive.

In all cases, the created curve may be a NURBSpline or a simpler curve such as line or arc. This is consistent with Revit expectations that the simplest possible representation of curve should be used in Revit elements.

### Hermite Spline

The overloaded static HermiteSpline.Create() method provides two options for creating Hermite splines. The simplest way creates a Hermite spline with default tangency at its endpoints and requires only a list of control points and a flag indicating whether or not the Hermite spline is periodic. The second option creates a Hermite spline with specified tangency at its endpoints. It has an additional parameter of a HermiteSplineTangents object to specify the tangents at the start and/or end of the curve.


<!-- ===== END: Help  Curve creation  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Curve Parameterization  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:28 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_Parameterization_html
author: 
---

# Help | Curve Parameterization | Autodesk

> ## Excerpt
> Curves in the Revit API can be described as mathematical functions of an input parameter “u”, where the location of the curve at any given point in XYZ space is a function of “u”.

---
Curves in the Revit API can be described as mathematical functions of an input parameter “u”, where the location of the curve at any given point in XYZ space is a function of “u”.

Curves can be bound or unbound. Unbound curves have no endpoints, representing either an infinite abstraction (an unbound line) or a cyclic curve (a circle or ellipse).

In Revit, the parameter “u” can be represented in two ways:

-   A ‘normalized’ parameter. The start value of the parameter is 0.0, and the end value is 1.0. For some curve types, this makes evaluation of the curve along its extents very easy, for example, the midpoint of a line is at parameter 0.5. (Note that for more complex curve equations like Splines this assumption cannot always be made).
-   A ‘raw’ parameter. The start and end value of the parameter can be any value. For a given curve, the value of the minimum and maximum raw parameter can be obtained through Curve.GetEndParameter(int) . Raw parameters are useful because their units are the same as the Revit default units (feet). So to obtain a location 5 feet along the curve from the start point, you can take the raw parameter at the start and add 5 to it. Raw parameters are also the only way to evaluate unbound curves.

The methods Curve.ComputeNormalizedParameter() and Curve.ComputeRawParameter() automatically scale between the two parameter types. The method Curve.IsInside() evaluates a raw parameter to see if it lies within the bounds of the curve.

You can use the parameter to evaluate a variety of properties of the curve at any given location:

-   The XYZ location of the given curve. This is returned from Curve.Evaluate(). Either the raw or normalized parameter can be supplied. If you are also calling ComputeDerivatives(), this is also the .Origin property of the Transform returned by that method.
-   The first derivative/tangent vector of the given curve. This is the .BasisX property of the Transform returned by Curve.ComputeDerivatives().
-   The second derivative/normal vector of the given curve. This is the .BasisY property of the Transform returned by Curve.ComputeDerivatives().
-   The _binormal_ vector of the given curve, defined as the cross-product of the tangent and normal vector. This is the .BasisZ property of the Transform returned by Curve.ComputeDerivatives().

All of the vectors returned are non-normalized (but you can normalize any vector in the Revit API with XYZ.Normalize()). Note that there will be no value set for the normal and binormal vector when the curve is a straight line. You can calculate a normal vector to the straight line in a given plane using the tangent vector.

The API sample “DirectionCalculation” uses the tangent vector to the wall location curve to find exterior walls that face south:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/directioncalculation_sample.png)Finding and highlighting south facing exterior walls


<!-- ===== END: Help  Curve Parameterization  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Curve types  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_types_html
author: 
---

# Help | Curve types | Autodesk

> ## Excerpt
> Revit uses a variety of curve types to represent curve geometry in a document.

---
Revit uses a variety of curve types to represent curve geometry in a document.

Curve types in Revit include:

<table summary="" id="GUID-AB7DD330-5FCA-47B3-BAC3-0E0658164FE8__TABLE_CA3E6D46CACF449C8F24C733188A98CF"><tbody><tr><td><b>Curve type</b></td><td><b>Revit API class</b></td><td><b>Definition</b></td><td><b>Notes</b></td></tr><tr><td>Bound line</td><td>Line</td><td>A line segment defined by its endpoints.</td><td>Obtain endpoints from Curve.GetEndpoint()</td></tr><tr><td>Unbound line</td><td>Line</td><td>An infinite line defined by a location and direction</td><td>Identify these with Curve.IsBound.<p>Evaluate point and tangent vector at raw parameter= 0 to find the input parameters for the equation of the line.</p></td></tr><tr><td>Arc</td><td>Arc</td><td>A bound circular arc</td><td>Begin and end at a certain angle. These angles can be obtained by the raw parameter values at each end of the arc.</td></tr><tr><td>Circle</td><td>Arc</td><td>An unbound circle</td><td>Identify with Curve.IsBound.<p>Use raw parameter for evaluation (from 0 to 2π)</p></td></tr><tr><td>Cylindrical helix</td><td>CylindricalHelix</td><td>A helix wound around a cylinder making constant angle with the axis of the cylinder</td><td>Used only in specific applications in stairs and railings, and should not be used or encountered when accessing curves of other Revit elements and geometry.</td></tr><tr><td>Elliptical arc</td><td>Ellipse</td><td>A bound elliptical segment</td><td></td></tr><tr><td>Ellipse</td><td>Ellipse</td><td>An unbound ellipse</td><td>Identify with Curve.IsBound. Use raw parameter for evaluation (from 0 to 2π)</td></tr><tr><td>NURBS</td><td>NurbSpline</td><td>A non-uniform rational B-spline</td><td>Used for splines sketched in various Revit tools, plus imported geometry</td></tr><tr><td>Hermite</td><td>HermiteSpline</td><td>A spline interpolate between a set of points</td><td>Used for tools like Curve by Points and flexible ducts/pipes, plus imported geometry</td></tr><tr><td colspan="2">CurveUV</td><td>A curve in the 2D parameter space of a surface in 3D space.</td><td>This class helps translate geometry (BReps) from external applications to Revit. Some geometric modelers represent the shape of an edge in a solid (or open shell) by a 3D curve, others use 2D curves in the parameter spaces of the edge’s faces, and others might use both. Revit can benefit from being given the CurveUVs for an edge when translating geometry, and this class accommodates the passing of such information.</td></tr></tbody></table>

Mathematical representations of all of the Revit curve types can be found in: [Mathematical representation of face types](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Mathematical_representation_of_face_types_html).


<!-- ===== END: Help  Curve types  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Mathematical representations of curve types  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:38 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Mathematical_representations_of_curve_types_html
author: 
---

# Help | Mathematical representations of curve types | Autodesk

> ## Excerpt
> This section describes the curve types encountered in Revit geometry, their properties, and their mathematical representations.

---
This section describes the curve types encountered in Revit geometry, their properties, and their mathematical representations.

### Bound lines

Bound lines are defined by their endpoints. In the Revit API, obtain the endpoints of the line from the Curve-level GetEndPoint() method.

The equation for a point on a bound line in terms of the normalized parameter “u” and the line endpoints is

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_bound_line.png)

### Unbound lines

Unbound lines are handled specially in the Revit API. Most curve properties cannot be used, however, Evaluate() and ComputeDerivatives() can be used to obtain locations along the curve when a raw parameter is provided.

The equation for a point for an unbound line in terms of the raw parameter “u” and the line origin and normalized direction vector is

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_unbound_line.png)

### Arcs and Circles

Arcs and Circles are represented in the Revit API by the Arc class. They are defined in terms of their radius, center and vector normal to the plane of the arc, which are accessible in the Revit API directly from the Arc class as properties.

Circles have the IsBound property set to true. This means they can only be evaluated by using a raw parameter (range from 0 to 2π), and the equation for a point on the circle in terms of the raw parameter is

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_arcs.png)where the assumption is made that the circle lies in the XY plane.

Arcs begin and end at a certain angle. These angles can be obtained by the raw parameter values at each end of the arc, and angular values between these values can be plugged into the same equation as above.

### Cylindrical Helixes

Cylindrical helixes are represented in the Revit API by the CylindricalHelix class. They are defined in terms of the base point of the axis of the cylinder around which the helix is wound, radius, x and y vectors, pitch, and start and end angles.

### Ellipse and elliptical arcs

Ellipses and elliptical arcs segments are represented in the Revit API by the Ellipse class. Similar to arcs and circles, they are defined in a given plane in terms of their X and Y radii, center, and vector normal to the plane of the ellipse.

Full ellipses have the IsBound property set to true. Similar to circles, they can be evaluated via raw parameter between 0 and 2π:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_ellipse.png)

### NurbSpline

NURBS (nonuniform rational B-splines) are used for spline segments sketched by the user as curves or portions of 3D object sketches. They are also used to represent some types of imported geometry data.

The data for the NurbSpline include:

-   The control points array, of length n+1
-   The weights array, also of length n+1
-   The curve degree, whose value is equal to one less than the curve order (k)
-   The knot vector, of length n + k +1

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_nurb_spline.png)NurbSplines as used in Revit’s sketching tools can be generated from the control points and degree alone using an algorithm. The calculations performed by Revit’s algorithm can be duplicated externally, see this sample below:

```
public void Nurb(ModelCurve curve)
{
    NurbSpline spline = curve.GeometryCurve as NurbSpline;
    DoubleArray knots = spline.Knots;

    // Convert to generic collection
    List<double> knotList = new List<double>();
    for(int i = 0; i < knots.Size; i++)
    {
        knotList.Add(knots.get_Item(i));
    }

    // Preparation - get distance between each control point
    IList<XYZ> controlPoints = spline.CtrlPoints;
    int numControlPoints = controlPoints.Count;
    double[] chordLengths = new double[numControlPoints - 1];
    for(int iControlPoint = 1; iControlPoint < numControlPoints; ++iControlPoint)
    {
        double chordLength = 
        controlPoints[iControlPoint].DistanceTo(controlPoints[iControlPoint - 1]);
        chordLengths[iControlPoint - 1] = chordLength;
    }

    int degree = spline.Degree;
    int order = degree + 1;
    int numKnots = numControlPoints + order;
    double[] computedKnots = new double[numKnots];
    int iKnot = 0;

    // Start knot with multiplicity degree + 1.
    double startKnot = 0.0;
    double knot = startKnot;
    for(iKnot = 0; iKnot < order; ++iKnot)
    {
        computedKnots[iKnot] = knot;
    }

    // Interior knots based on chord lengths
    double prevKnot = knot;

    for(/*blank*/; iKnot <= numControlPoints; ++iKnot) 
        // Last loop computes end knot but does not set interior knot.
    {
        double knotIncrement = 0.0;
        for (int jj = iKnot - order; jj < iKnot - 1; ++jj)
        {
            knotIncrement += chordLengths[jj];
        }

        knotIncrement /= degree;
        knot = prevKnot + knotIncrement;
        if (iKnot < numControlPoints)
            computedKnots[iKnot] = knot;
        else
            break;   // Leave "knot" set to the end knot; do not increment "ii".

        prevKnot = knot;
    }

    // End knot with multiplicity degree + 1.
    for(/*blank*/; iKnot < numKnots; ++iKnot)
    {
        computedKnots[iKnot] = knot;
    }
}
```

#### HermiteSpline

Hermite splines are used for curves which are interpolated between a set of control points, like Curve by Points and flexible ducts and pipes in MEP. They are also used to represent some types of imported geometry data. In the Revit API, the HermiteSpline class offers access to the arrays of points, tangent vectors and parameters through the ControlPoints, Tangents, and Parameters properties.

The equation for the curve between two nodes in a Hermite spline is

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_hermite_1.png)where P<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-F3A27DD5-F786-42CD-80CA-9C39F86EC25F">k</sub> and P<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-7C381E19-3D6D-4BB7-B855-C0FB538F5985">k+1</sub> represent the points at each node, M<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-BA44375E-AF0B-4F7B-8966-415E75538858">k</sub> and M<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-11714EEB-B3F2-4DA9-B387-653E9A7E994E">k+1</sub> the tangent vectors, and u<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-DE8A2F53-B16E-4BD3-A45D-0C3D548B6E17">k</sub> and u<sub id="GUID-5F1A77E3-0B70-4333-BDB8-6BF83C83AE63__GUID-8248DE2A-A4D1-4609-943D-C67DF8C78ABE">k+1</sub> the parameters at the nodes, and the basis functions are:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_hermite_2.png) ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_hermite3.png)![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_hermite4.png)

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/curve_hermite5.png)


<!-- ===== END: Help  Mathematical representations of curve types  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  GeometryInstances  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:43 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_GeometryInstances_html
author: 
---

# Help | GeometryInstances | Autodesk

> ## Excerpt
> A GeometryInstance represents a set of geometry stored by Revit in a default configuration, and then transformed into the proper location as a result of the properties of the element. The most common situation where GeometryInstances are encountered is in Family instances. Revit uses GeometryInstances to allow it to store a single copy of the geometry for a given family and reuse it in multiple instances.

---
A GeometryInstance represents a set of geometry stored by Revit in a default configuration, and then transformed into the proper location as a result of the properties of the element. The most common situation where GeometryInstances are encountered is in Family instances. Revit uses GeometryInstances to allow it to store a single copy of the geometry for a given family and reuse it in multiple instances.

Note that not all Family instances will include GeometryInstances. When Revit needs to make a unique copy of the family geometry for a given instance (because of the effect of local joins, intersections, and other factors related to the instance placement) no GeometryInstance will be encountered; instead the Solid geometry will be found at the top level of the hierarchy.

A GeometryInstance offers the ability to read its geometry through the GetSymbolGeometry() and GetInstanceGeometry() methods. These methods return another Autodesk.Revit.DB.GeometryElement which can be parsed just like the first level return.

GetSymbolGeometry() returns the geometry represented in the coordinate system of the family. Use this, for example, when you want a picture of the “generic” table without regards to the orientation and placement location within the project. This is also the only overload which returns the actual Revit geometry objects to you, and not copies. This is important because operations which use this geometry as input to creating other elements (for example, dimensioning or placement of face-based families) require the reference to the original geometry.

GetInstanceGeometry() returns the geometry represented in the coordinate system of the project where the instance is placed. Use this, for example, when you want a picture of the specific geometry of the instance in the project (for example, ensuring that tables are placed parallel to the walls of the room). This always returns a copy of the element geometry, so while it would be suitable for implementation of an exporter or a geometric analysis tool, it would not be appropriate to use this for the creation of other Revit elements referencing this geometry.

There are also overloads for both GetInstanceGeometry() and GetSymbolGeometry() that transform the geometry by any arbitrary coordinate system. These methods always return copies similar to GetInstanceGeometry().

The GeometryInstance also stored a transformation from the symbol coordinate space to the instance coordinates. This transform is accessible as the Transform property. It is also the transformation used when extracting a the copy of the geometry via GetInstanceGeometry(). For more details, refer to [Geometry Helper Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Helper_Classes_html).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/instances_transformed.png)**2 family instances placed with different transforms - the same geometry will be acquired from both**

Instances may be nested several levels deep for some families. If you encounter nested instances they may be parsed in a similar manner as the first level instance.

Two samples are presented to explain how geometry of instances can be parsed.

In this sample, curves are extracted from the GeometryInstance method GetInstanceGeometry().

<table summary="" id="GUID-B4F83374-0DF6-4737-91EB-900E676E862B__TABLE_957B57BD7CD6475E8E425AE0B967168A"><tbody><tr><td><b>Code Region: Getting curves from an instance</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetAndTransformCurve</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app</span><span>,</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> element</span><span>,</span><span> </span><span>Options</span><span> geoOptions</span><span>)</span><span>
</span><span>{</span><span>
   </span><span>// Get geometry element of the selected element</span><span>
   </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geoElement </span><span>=</span><span> element</span><span>.</span><span>get_Geometry</span><span>(</span><span>geoOptions</span><span>);</span><span>

   </span><span>// Get geometry object</span><span>
   </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geoObject </span><span>in</span><span> geoElement</span><span>)</span><span>
   </span><span>{</span><span>
      </span><span>// Get the geometry instance which contains the geometry information</span><span>
      </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span> instance </span><span>=</span><span>
             geoObject </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span>;</span><span>
      </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> instance</span><span>)</span><span>
      </span><span>{</span><span>
         </span><span>GeometryElement</span><span> instanceGeometryElement </span><span>=</span><span> instance</span><span>.</span><span>GetInstanceGeometry</span><span>();</span><span>
         </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> o </span><span>in</span><span> instanceGeometryElement</span><span>)</span><span>
         </span><span>{</span><span>
            </span><span>// Try to find curves</span><span>
            </span><span>Curve</span><span> curve </span><span>=</span><span> o </span><span>as</span><span> </span><span>Curve</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>curve </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
               </span><span>// The curve is already transformed into the project coordinate system</span><span>
            </span><span>}</span><span>
         </span><span>}</span><span>
      </span><span>}</span><span>
   </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

In this sample, the solids are obtained from an instance using GetSymbolGeometry(). The constituent points are then transformed into the project coordinate system using the GeometryInstance.Transform.

<table summary="" id="GUID-B4F83374-0DF6-4737-91EB-900E676E862B__TABLE_30A437E3589144C3AFC1AADEB2F10DB2"><tbody><tr><td><b>Code Region: Getting solid information from an instance</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetAndTransformSolidInfo</span><span>(</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Element</span><span> element</span><span>,</span><span> </span><span>Options</span><span> geoOptions</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Get geometry element of the selected element</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geoElement </span><span>=</span><span> element</span><span>.</span><span>get_Geometry</span><span>(</span><span>geoOptions</span><span>);</span><span>

        </span><span>// Get geometry object</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geoObject </span><span>in</span><span> geoElement</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Get the geometry instance which contains the geometry information</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span> instance </span><span>=</span><span>
      geoObject </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> instance</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>GeometryElement</span><span> instanceGeometryElement </span><span>=</span><span> instance</span><span>.</span><span>GetSymbolGeometry</span><span>();</span><span>
                    </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> instObj </span><span>in</span><span> instanceGeometryElement</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>Solid</span><span> solid </span><span>=</span><span> instObj </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
                                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> solid </span><span>||</span><span> </span><span>0</span><span> </span><span>==</span><span> solid</span><span>.</span><span>Faces</span><span>.</span><span>Size</span><span> </span><span>||</span><span> </span><span>0</span><span> </span><span>==</span><span> solid</span><span>.</span><span>Edges</span><span>.</span><span>Size</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>continue</span><span>;</span><span>
                                </span><span>}</span><span>

                                </span><span>Transform</span><span> instTransform </span><span>=</span><span> instance</span><span>.</span><span>Transform</span><span>;</span><span>
                                </span><span>// Get the faces and edges from solid, and transform the formed points</span><span>
                                </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> face </span><span>in</span><span> solid</span><span>.</span><span>Faces</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>Mesh</span><span> mesh </span><span>=</span><span> face</span><span>.</span><span>Triangulate</span><span>();</span><span>
                                        </span><span>foreach</span><span> </span><span>(</span><span>XYZ ii </span><span>in</span><span> mesh</span><span>.</span><span>Vertices</span><span>)</span><span>
                                        </span><span>{</span><span>
                                                XYZ point </span><span>=</span><span> ii</span><span>;</span><span>
                                                XYZ transformedPoint </span><span>=</span><span> instTransform</span><span>.</span><span>OfPoint</span><span>(</span><span>point</span><span>);</span><span>
                                        </span><span>}</span><span>
                                </span><span>}</span><span>
                                </span><span>foreach</span><span> </span><span>(</span><span>Edge</span><span> edge </span><span>in</span><span> solid</span><span>.</span><span>Edges</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>foreach</span><span> </span><span>(</span><span>XYZ ii </span><span>in</span><span> edge</span><span>.</span><span>Tessellate</span><span>())</span><span>
                                        </span><span>{</span><span>
                                                XYZ point </span><span>=</span><span> ii</span><span>;</span><span>
                                                XYZ transformedPoint </span><span>=</span><span> instTransform</span><span>.</span><span>OfPoint</span><span>(</span><span>point</span><span>);</span><span>
                                        </span><span>}</span><span>
                                </span><span>}</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  GeometryInstances  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Meshes  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:47 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Meshes_html
author: 
---

# Help | Meshes | Autodesk

> ## Excerpt
> A mesh is a collection of triangular boundaries which collectively forms a 3D shape. Meshes are typically encountered inside Revit element geometry if those elements were created from certain import operations and also are used in some native Revit elements such as TopographySurface. You can also obtain Meshes as the result of calls to Face.Triangulate() for any given Revit face. The property Mesh.IsClosed checks if each edge in the mesh belongs to at least two faces.

---
A mesh is a collection of triangular boundaries which collectively forms a 3D shape. Meshes are typically encountered inside Revit element geometry if those elements were created from certain import operations and also are used in some native Revit elements such as TopographySurface. You can also obtain Meshes as the result of calls to Face.Triangulate() for any given Revit face. The property `Mesh.IsClosed` checks if each edge in the mesh belongs to at least two faces.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/mesh.png)A mesh representing a torus

The following code sample illustrates how to get the geometry of a Revit face as a Mesh:

<table summary="" id="GUID-A4E51A50-60EF-4D49-9944-4935FA88CD11__TABLE_C299BDB28BE54C97B22ABA4BD31FC845"><tbody><tr><td><b>Code region: Extracting the geometry of a mesh</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetTrianglesFromFace</span><span>(</span><span>Face</span><span> face</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Get mesh</span><span>
        </span><span>Mesh</span><span> mesh </span><span>=</span><span> face</span><span>.</span><span>Triangulate</span><span>();</span><span>
        </span><span>for</span><span> </span><span>(</span><span>int</span><span> i </span><span>=</span><span> </span><span>0</span><span>;</span><span> i </span><span>&lt;</span><span> mesh</span><span>.</span><span>NumTriangles</span><span>;</span><span> i</span><span>++)</span><span>
        </span><span>{</span><span>
               </span><span>MeshTriangle</span><span> triangle </span><span>=</span><span> mesh</span><span>.</span><span>get_Triangle</span><span>(</span><span>i</span><span>);</span><span>
               XYZ vertex1 </span><span>=</span><span> triangle</span><span>.</span><span>get_Vertex</span><span>(</span><span>0</span><span>);</span><span>
               XYZ vertex2 </span><span>=</span><span> triangle</span><span>.</span><span>get_Vertex</span><span>(</span><span>1</span><span>);</span><span>
               XYZ vertex3 </span><span>=</span><span> triangle</span><span>.</span><span>get_Vertex</span><span>(</span><span>2</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: The approximation tolerance used for Revit display purposes is used by the parameterless overload of the Triangulate() method (used above) when constructing the Mesh. The overload of Triangulate() that takes a double allows a level of detail to be set between 0 (coarser) and 1 (finer).


<!-- ===== END: Help  Meshes  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Points  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:52 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Points_html
author: 
---

# Help | Points | Autodesk

> ## Excerpt
> A point represents a visible coordinate in 3D space.

---
A point represents a visible coordinate in 3D space.

Points are typically encountered in mass family elements like ReferencePoint. The Point class provides read access to its coordinates, and an ability to obtain a reference to the point for use as input to other functions.

### Point creation

There are two ways to create Points:

-   Create(XYZ) - creates a Point at the given coordinates.
-   Create(XYZ, ElementId) - creates a Point at given coordinates and assigns it a color based on the GraphicsStyle element (specified by ElementId).


<!-- ===== END: Help  Points  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  PolyLines  Autodesk.md ===== -->

---
created: 2026-01-28T21:01:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_PolyLines_html
author: 
---

# Help | PolyLines | Autodesk

> ## Excerpt
> A polyline is a collection of line segments defined by a set of coordinate points. These are typically encountered in imported geometry. The PolyLine class offers the ability to read the coordinates:

---
A polyline is a collection of line segments defined by a set of coordinate points. These are typically encountered in imported geometry. The PolyLine class offers the ability to read the coordinates:

-   PolyLine.NumberOfCoordinates – the number of points in the polyline
-   PolyLine.GetCoordinate() – gets a coordinate by index
-   PolyLine.GetCoordinates() – gets a collection of all coordinates in the polyline
-   PolyLine.Evaluate() – given a normalized parameter (from 0 to 1) evaluates an XYZ point along the extents of the entire polyline


<!-- ===== END: Help  PolyLines  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Solids, Faces and Edges  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_html
author: 
---

# Help | Solids, Faces and Edges | Autodesk

> ## Excerpt
> A Solid is a Revit API object which represents a collection of faces and edges. Typically in Revit these collections are fully enclosed volumes, but a shell or partially bounded volume can also be encountered. Note that sometimes the Revit geometry will contain unused solids containing zero edges and faces. Check the Edges and Faces members to filter out these solids.

---
A Solid is a Revit API object which represents a collection of faces and edges. Typically in Revit these collections are fully enclosed volumes, but a shell or partially bounded volume can also be encountered. Note that sometimes the Revit geometry will contain unused solids containing zero edges and faces. Check the Edges and Faces members to filter out these solids.

The Revit API offers the ability to read the collections of faces and edges, and also to compute the surface area, volume, and centroid of the solid.


<!-- ===== END: Help  Solids, Faces and Edges  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Edges  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:06 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Edges_html
author: 
---

# Help | Edges | Autodesk

> ## Excerpt
> The Edge class represents the edge of a 3d solid. Edges are defined by intersections of surfaces that form faces of the solid. They have arbitrary parameterization that is normalized from 0 to 1. The EdgeEndPoint class represents the start or the end point of an Edge and SolidUtils.FindAllEdgeEndPointsAtVertex() finds all EdgeEndPoints at a vertex identified by the input EdgeEndPoint.

---
The `Edge` class represents the edge of a 3d solid. Edges are defined by intersections of surfaces that form faces of the solid. They have arbitrary parameterization that is normalized from 0 to 1. The `EdgeEndPoint` class represents the start or the end point of an Edge and `SolidUtils.FindAllEdgeEndPointsAtVertex()` finds all EdgeEndPoints at a vertex identified by the input EdgeEndPoint.

**Parent page:** [Solids, Faces and Edges](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_html)


<!-- ===== END: Help  Edges  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Edge and face parameterization  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:10 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Edge_and_face_parameterization_html
author: 
---

# Help | Edge and face parameterization | Autodesk

> ## Excerpt
> Edges are boundary curves for a given face.

---
Edges are boundary curves for a given face.

Iterate the edges of a Face using the EdgeLoops property. Each loop represents one closed boundary on the face. Edges are always parameterized from 0 to 1. It is possible to extract the Curve representation of an Edge with the Edge.AsCurve() and Edge.AsCurveFollowingFace() functions.

An edge is usually defined by computing intersection of two faces. But Revit doesn’t recompute this intersection when it draws graphics. So the edge stores a list of points - end points for a straight edge and a tessellated list for a curved edge. The points are parametric coordinates on the two faces. These points are available through the TessellateOnFace() method.

Sections produce “cut edges”. These are artificial edges - not representing a part of the model-level geometry, and thus do not provide a Reference.

### Edge direction

Direction is normally clockwise on the first face (first representing an arbitrary face which Revit has identified for a particular edge). But because two different faces meet at one particular edge, and the edge has the same parametric direction regardless of which face you are concerned with, sometimes you need to figure out the direction of the edge on a particular face.

The figure below illustrated how this works. For Face 0, the edges are all parameterized clockwise. For Face 1, the edge shared with Face 0 is not re-parameterized; thus with respect to Face 1 the edge has a reversed direction, and some edges intersect where both edges’ parameters are 0 (or 1).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_edge_direction.png)**Edge parameterization**

The API sample “PanelEdgeLengthAngle” shows how to recognize edges that are reversed for a given face. It uses the tangent vector at the edge endpoints to calculate the angle between adjacent edges, and detect whether or not to flip the tangent vector at each intersection to calculate the proper angle.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/paneledgelengthangle_sample.png)**PanelEdgeLengthAngle results**


<!-- ===== END: Help  Edge and face parameterization  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Faces  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Faces_html
author: 
---

# Help | Faces | Autodesk

> ## Excerpt
> Faces in the Revit API can be described as mathematical functions of two input parameters “u” and “v”, where the location of the face at any given point in XYZ space is a function of the parameters.

---
Faces in the Revit API can be described as mathematical functions of two input parameters “u” and “v”, where the location of the face at any given point in XYZ space is a function of the parameters.

The U and V directions are automatically determined based on the shape of the given face. Lines of constant U or V can be represented as gridlines on the face, as shown in the example below:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_params.png)**U and V gridlines on a cylindrical face**

You can use the UV parameters to evaluate a variety of properties of the face at any given location:

-   Whether the parameter is within the boundaries of the face, using Face.IsInside()
-   The XYZ location of the given face at the specified UV parameter value. This is returned from Face.Evaluate(). If you are also calling ComputeDerivatives(), this is also the .Origin property of the Transform returned by that method.
-   The tangent vector of the given face in the U direction. This is the .BasisX property of the Transform returned by Face.ComputeDerivatives()
-   The tangent vector of the given face in the V direction. This is the .BasisY property of the Transform returned by Face.ComputeDerivatives().
-   The normal vector of the given face. This is the .BasisZ property of the Transform returned by Face.ComputeDerivatives().
-   The second derivative with respect to U. This is the .UUDerivative property of the FaceSecondDerivatives returned by Face.ComputeSecondDerivatives().
-   The second derivative with respect to V. This is the .VVDerivative of the FaceSecondDerivatives returned by Face.ComputeSecondDerivatives().
-   The mixed derivative of the given face. This is the .MixedDerivative of the FaceSecondDerivatives returned by Face.ComputeSecondDerivatives().

All of the vectors returned are non-normalized.


<!-- ===== END: Help  Faces  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Face analysis  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Face_analysis_html
author: 
---

# Help | Face analysis | Autodesk

> ## Excerpt
> There are several Face methods which are tools suitable for use in geometric analysis.

---
There are several Face methods which are tools suitable for use in geometric analysis.

### Intersect()

The Intersect method computes the intersection between the face and a curve. It can be used in to identify:

-   The intersection point(s) between the two objects
-   The edge nearest the intersection point, if there is an edge close to this location
-   Curves totally coincident with a face
-   Curves and faces which do not intersect
    
    ### Project()
    

The Project method projects a point on the input face, and returns information on the projection point, the distance to the face, and the nearest edge to the projection point.

### Triangulate()

The Triangulate method obtains a triangular mesh approximating the face. There are two overloads to this method. The parameterless method is similar to Curve.Tessellate() in that the mesh’s points are accurate within the input tolerance used by Revit (slightly larger than 1/16”). The second Triangulate method accepts a level of detail as an argument ranging from 0 (coarse) to 1 (fine).


<!-- ===== END: Help  Face analysis  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Face Splitting  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Face_Splitting_html
author: 
---

# Help | Face Splitting | Autodesk

> ## Excerpt
> A face may be split into regions by the Split Face command. The Face.HasRegions property will report if the face contains regions created with the Split Face command, while the Face.GetRegions() method will return a list of faces, one for the main face of the object hosting the Split Face (such as wall of floor) and one face for each Split Face region.

---
A face may be split into regions by the Split Face command. The Face.HasRegions property will report if the face contains regions created with the Split Face command, while the Face.GetRegions() method will return a list of faces, one for the main face of the object hosting the Split Face (such as wall of floor) and one face for each Split Face region.

The FaceSplitter class represents an element that splits a face. The FaceSplitter.SplitElementId property provides the id of the element whose face is split by this element. The FaceSplitter class can be used to filter and find these faces by type as shown below.

<table summary="" id="GUID-A7308E03-F3C3-433E-8AD5-3C31EDD81387__TABLE_9599826CA311409FAC73A8C065C7B0AA"><tbody><tr><td><b>Code Region: Find face splitting elements</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FindSplitting</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Options</span><span> opt </span><span>=</span><span> app</span><span>.</span><span>Create</span><span>.</span><span>NewGeometryOptions</span><span>();</span><span>
    opt</span><span>.</span><span>ComputeReferences</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    opt</span><span>.</span><span>IncludeNonVisibleObjects</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>FaceSplitter</span><span>&gt;</span><span> splitElements </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FaceSplitter</span><span>)).</span><span>Cast</span><span>&lt;</span><span>FaceSplitter</span><span>&gt;().</span><span>ToList</span><span>();</span><span>
    </span><span>foreach</span><span>(</span><span>FaceSplitter</span><span> faceSplitter </span><span>in</span><span> splitElements</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> splitElement </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>faceSplitter</span><span>.</span><span>SplitElementId</span><span>);</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geomElem </span><span>=</span><span> faceSplitter</span><span>.</span><span>get_Geometry</span><span>(</span><span>opt</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geomObj </span><span>in</span><span> geomElem</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Line</span><span> line </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Line</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>line </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                XYZ end1 </span><span>=</span><span> line</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>
                XYZ end2 </span><span>=</span><span> line</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>);</span><span>
                </span><span>double</span><span> length </span><span>=</span><span> line</span><span>.</span><span>ApproximateLength</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Face Splitting  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Face types  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Face_types_html
author: 
---

# Help | Face types | Autodesk

> ## Excerpt
> Revit uses a variety of curve types to represent face geometry in a document. These include:

---
Revit uses a variety of curve types to represent face geometry in a document. These include:

<table summary="" id="GUID-12AF716F-7135-405B-8005-26A15EB58025__TABLE_6C2033AA354141EB83F6506DD7E2CF21"><tbody><tr><td><b>Face type</b></td><td><b>Revit API class</b></td><td><b>Definition</b></td><td><b>Notes</b></td></tr><tr><td>Plane</td><td>PlanarFace</td><td>A plane defined by the origin and unit vectors in U and V.</td><td></td></tr><tr><td>Cylinder</td><td>CylindricalFace</td><td>A face defined by extruding a circle along an axis.</td><td>.Radius provides the “radius vectors” – the unit vectors of the circle multiplied by the radius value.</td></tr><tr><td>Cone</td><td>ConicalFace</td><td>A face defined by rotation of a line about an axis.</td><td>.Radius provides the “radius vectors” – the unit vectors of the circle multiplied by the radius value.</td></tr><tr><td>Revolved face</td><td>RevolvedFace</td><td>A face defined by rotation of an arbitrary curve about an axis.</td><td>.Radius provides the unit vectors of the plane of rotation, there is no “radius” involved.</td></tr><tr><td>Ruled surface</td><td>RuledFace</td><td>A face defined by sweeping a line between two profile curves, or one profile curve and one point.</td><td>Both curve(s) and point(s) can be obtained as properties.</td></tr><tr><td>Hermite face</td><td>HermiteFace</td><td>A face defined by Hermite interpolation between points.</td><td></td></tr></tbody></table>

Mathematical representations of all of the Revit face types can be found in: [Mathematical representation of face types](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Mathematical_representation_of_face_types_html).


<!-- ===== END: Help  Face types  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Mathematical representation of face types  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Mathematical_representation_of_face_types_html
author: 
---

# Help | Mathematical representation of face types | Autodesk

> ## Excerpt
> This section describes the face types encountered in Revit geometry, their properties, and their mathematical representations.

---
This section describes the face types encountered in Revit geometry, their properties, and their mathematical representations.

### PlanarFace

A plane defined by origin and unit vectors in U and V. Its parametric equation is

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_planar.png)

### CylindricalFace

A face defined by extruding a circle along an axis. The Revit API provides the following properties:

-   The origin of the face.
-   The axis of extrusion.
-   The “radius vectors” in X and Y. These vectors are the circle’s unit vectors multiplied by the radius of the circle. Note that the unit vectors may represent either a right handed or left handed control frame.

The parametric equation for this face is:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_cylinder.png)

### ConicalFace

A face defined by rotation of a line about an axis. The Revit API provides the following properties:

-   The origin of the face.
-   The axis of the cone.
-   The “radius vectors” in X and Y. These vectors are the unit vectors multiplied by the radius of the circle formed by the revolution. Note that the unit vectors may represent either a right handed or left handed control frame.
-   The half angle of the face.

The parametric equation for this face is:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_cone.png)

### RevolvedFace

A face defined by rotation of an arbitrary curve about an axis. The Revit API provides the following properties:

-   The origin of the face
-   The axis of the face
-   The profile curve
-   The unit vectors for the rotated curve (incorrectly called “Radius”)

The parametric equation for this face is:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_revolved.png)

### RuledFace

A ruled surface is created by sweeping a line between two profile curves or between a curve and a point. The Revit API provides the curve(s) and point(s) as properties.

The parametric equation for this surface is:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_ruled1.png)if both curves are valid. If one of the curves is replaced with a point, the equations simplify to one of:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_ruled2.png) ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_ruled3.png)A ruled face with no curves and two points is degenerate and will not be returned.

### HermiteFace

A cubic Hermite spline face. The Revit API provides:

-   Arrays of the u and v parameters for the spline interpolation points
-   An array of the 3D points at each node (the array is organized in increasing u, then increasing v)
-   An array of the tangent vectors at each node
-   An array of the twist vectors at each node

The parametric representation of this surface, between nodes (u1, v1) and (u2, v2) is:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_hermite1.png)Where ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_hermite2.png), ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_hermite3.png), **M<sub id="GUID-C0153253-8374-4CCD-AF35-A2A84C1D842E__GUID-EC1F315C-F81A-42C1-AA8B-317A3F942532">H</sub>** is the Hermite matrix:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_hermite4.png)And B is coefficient matrix obtained from the face properties at the interpolation points:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_hermite5.png)


<!-- ===== END: Help  Mathematical representation of face types  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Solid analysis  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:37 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Solid_analysis_html
author: 
---

# Help | Solid analysis | Autodesk

> ## Excerpt
> The method Solid.IntersectWithCurve() calculates the intersection between a closed volume solid and a curve. The SolidCurveIntersectionOptions class can specify whether the results from the IntersectWithCurve() method will include curve segments inside the solid volume or outside. The curve segments inside the solid will include curve segments coincident with the face(s) of the solid. Both the curve segments and the parameters of the segments are available in the results.

---
## Intersection between solid and curve

The method Solid.IntersectWithCurve() calculates the intersection between a closed volume solid and a curve. The SolidCurveIntersectionOptions class can specify whether the results from the IntersectWithCurve() method will include curve segments inside the solid volume or outside. The curve segments inside the solid will include curve segments coincident with the face(s) of the solid. Both the curve segments and the parameters of the segments are available in the results.

The following example uses the IntersectWithCurve() method to calculate the length of rebar that lies within a column.

<table summary="" id="GUID-2601C028-7E6D-462A-9234-46FFA3E2D31E__TABLE_1152331007A245129FE54F60B2FA7A6B"><tbody><tr><td><b>Code Region: Finding intersection between solid and curve</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>FindColumnRebarIntersections</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> column</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// We will be computing the total length of the rebar inside the column</span><span>
    </span><span>double</span><span> totalRebarLengthInColumn </span><span>=</span><span> </span><span>0</span><span>;</span><span>

    </span><span>// Find rebar hosted by this column</span><span>
    </span><span>RebarHostData</span><span> rebarHostData </span><span>=</span><span> </span><span>RebarHostData</span><span>.</span><span>GetRebarHostData</span><span>(</span><span>column</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>rebarHostData </span><span>==</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>IList</span><span>&lt;</span><span>Rebar</span><span>&gt;</span><span> rebars </span><span>=</span><span> rebarHostData</span><span>.</span><span>GetRebarsInHost</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>rebars</span><span>.</span><span>Count</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>// Retrieve geometry of the column</span><span>
    </span><span>Options</span><span> geomOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>Options</span><span>();</span><span>
    geomOptions</span><span>.</span><span>ComputeReferences</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    geomOptions</span><span>.</span><span>DetailLevel</span><span> </span><span>=</span><span> </span><span>ViewDetailLevel</span><span>.</span><span>Fine</span><span>;</span><span>
    </span><span>GeometryElement</span><span> elemGeometry </span><span>=</span><span> column</span><span>.</span><span>get_Geometry</span><span>(</span><span>geomOptions</span><span>);</span><span>

    </span><span>// Examine all geometry primitives of the column</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> elemPrimitive </span><span>in</span><span> elemGeometry</span><span>)</span><span>
    </span><span>{</span><span>

        </span><span>// Skip objects that are not geometry instances</span><span>
        </span><span>GeometryInstance</span><span> gInstance </span><span>=</span><span> elemPrimitive </span><span>as</span><span> </span><span>GeometryInstance</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>gInstance </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>continue</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>// Retrieve geometry of each found geometry instance</span><span>
        </span><span>GeometryElement</span><span> instGeometry </span><span>=</span><span> gInstance</span><span>.</span><span>GetInstanceGeometry</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> instPrimitive </span><span>in</span><span> instGeometry</span><span>)</span><span>
        </span><span>{</span><span>

            </span><span>// Skip non-solid sobject</span><span>
            </span><span>Solid</span><span> solid </span><span>=</span><span> instPrimitive </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>solid </span><span>==</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>continue</span><span>;</span><span>
            </span><span>}</span><span>

            </span><span>SolidCurveIntersectionOptions</span><span> intersectOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>SolidCurveIntersectionOptions</span><span>();</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>Rebar</span><span> rebar </span><span>in</span><span> rebars</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// Get the centerlines for the rebar to find their intersection with the column</span><span>
                </span><span>bool</span><span> selfIntersection </span><span>=</span><span> </span><span>false</span><span>;</span><span>
                </span><span>bool</span><span> suppresHooks </span><span>=</span><span> </span><span>false</span><span>;</span><span>
                </span><span>bool</span><span> suppresBends </span><span>=</span><span> </span><span>false</span><span>;</span><span>
                </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> curves </span><span>=</span><span> rebar</span><span>.</span><span>GetCenterlineCurves</span><span>(</span><span>selfIntersection</span><span>,</span><span> suppresHooks</span><span>,</span><span> suppresBends</span><span>,</span><span> </span><span>MultiplanarOption</span><span>.</span><span>IncludeOnlyPlanarCurves</span><span>,</span><span> </span><span>0</span><span>);</span><span>

                </span><span>// Examine every segment of every curve of the centerline</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>Curve</span><span> curve </span><span>in</span><span> curves</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>SolidCurveIntersection</span><span> intersection </span><span>=</span><span> solid</span><span>.</span><span>IntersectWithCurve</span><span>(</span><span>curve</span><span>,</span><span> intersectOptions</span><span>);</span><span>
                    </span><span>for</span><span> </span><span>(</span><span>int</span><span> segment </span><span>=</span><span> </span><span>0</span><span>;</span><span> segment </span><span>&lt;=</span><span> intersection</span><span>.</span><span>SegmentCount</span><span> </span><span>-</span><span> </span><span>1</span><span>;</span><span> segment</span><span>++)</span><span>
                    </span><span>{</span><span>
                        </span><span>// Calculate length of the rebar that is inside the column</span><span>
                        </span><span>Curve</span><span> curveInside </span><span>=</span><span> intersection</span><span>.</span><span>GetCurveSegment</span><span>(</span><span>segment</span><span>);</span><span>
                        </span><span>double</span><span> rebarLengthInColumn </span><span>=</span><span> curveInside</span><span>.</span><span>Length</span><span>;</span><span>
                        totalRebarLengthInColumn </span><span>=</span><span> totalRebarLengthInColumn </span><span>+</span><span> rebarLengthInColumn</span><span>;</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>

            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Solid analysis  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Solid and face creation  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Solid_and_face_creation_html
author: 
---

# Help | Solid and face creation | Autodesk

> ## Excerpt
> Solids and faces are sometimes used as inputs to other utilities. The Revit API provides several routines which can be used to create such geometry from scratch or to derive it from other inputs.

---
Solids and faces are sometimes used as inputs to other utilities. The Revit API provides several routines which can be used to create such geometry from scratch or to derive it from other inputs.

### _Transformed geometry_

The method

-   GeometryElement.GetTransformed()

returns a copy of the input geometry element with a transformation applied. Because this geometry is a copy, its members cannot be used as input references to other Revit elements, but it can be used geometric analysis and extraction.

### _Geometry creation utilities_

The GeometryCreationUtilities class is a utility class that allows construction of basic solid shapes:

-   Extrusion
-   Loft
-   Revolution
-   Sweep
-   Blend
-   SweptBlend

The resulting geometry is not added to the document as a part of any element. However, the created Solid can be used as inputs to other API functions, including:

-   As the input face(s) to the methods in the Analysis Visualization framework (SpatialFieldManager.AddSpatialFieldPrimitive()) – this allows the user to visualize the created shape relative to other elements in the document
-   As the input solid to finding 3D elements by intersection
-   As one or more of the inputs to a Boolean operation
-   As a part of a geometric calculation (using, for example, Face.Project(), Face.Intersect(), or other Face, Solid, and Edge geometry methods)

The following example uses the GeometryCreationUtilities class to create cylindrical shapes based on a location and height. This might be used, for example, to create volumes around the ends of a wall in order to find other walls within close proximity to the wall end points:

<table summary="" id="GUID-602B5423-953C-4EB0-9475-A8B76B726DE8__TABLE_0860632902034A54B3FF48179F4DC114"><tbody><tr><td><b>Code Region: Create cylindrical solid</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MakeCyl</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> XYZ endPoint</span><span>,</span><span> </span><span>double</span><span> height</span><span>,</span><span> </span><span>double</span><span> elevation</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Build cylinder centered at wall end point, extending 3' in diameter</span><span>
    </span><span>CurveLoop</span><span> cylinderLoop </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveLoop</span><span>();</span><span>
    XYZ arcCenter </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>endPoint</span><span>.</span><span>X</span><span>,</span><span> endPoint</span><span>.</span><span>Y</span><span>,</span><span> elevation</span><span>);</span><span>
    </span><span>Application</span><span> application </span><span>=</span><span> wall</span><span>.</span><span>Document</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>Arc</span><span> firstArc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>arcCenter</span><span>,</span><span> </span><span>1.5</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>,</span><span> XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> XYZ</span><span>.</span><span>BasisY</span><span>);</span><span>
    </span><span>Arc</span><span> secondArc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>arcCenter</span><span>,</span><span> </span><span>1.5</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>,</span><span> </span><span>2</span><span> </span><span>*</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>,</span><span> XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> XYZ</span><span>.</span><span>BasisY</span><span>);</span><span>

    cylinderLoop</span><span>.</span><span>Append</span><span>(</span><span>firstArc</span><span>);</span><span>
    cylinderLoop</span><span>.</span><span>Append</span><span>(</span><span>secondArc</span><span>);</span><span>

    </span><span>List</span><span>&lt;</span><span>CurveLoop</span><span>&gt;</span><span> singleLoop </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>CurveLoop</span><span>&gt;();</span><span>
    singleLoop</span><span>.</span><span>Add</span><span>(</span><span>cylinderLoop</span><span>);</span><span>

    </span><span>Solid</span><span> proximityCylinder </span><span>=</span><span> </span><span>GeometryCreationUtilities</span><span>.</span><span>CreateExtrusionGeometry</span><span>(</span><span>singleLoop</span><span>,</span><span> XYZ</span><span>.</span><span>BasisZ</span><span>,</span><span> height</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### _Boolean operations_

The BooleanOperationsUtils class provides methods for combining a pair of solid geometry objects.

The ExecuteBooleanOperation() method takes a copy of the input solids and produces a new solid as a result. Its first argument can be any solid, either obtained directly from a Revit element or created via another operation like GeometryCreationUtils.

The method ExecuteBooleanOperationModifyingOriginalSolid() performs the boolean operation directly on the first input solid. The first input must be a solid which is not obtained directly from a Revit element. The property GeometryObject.IsElementGeometry can identify whether the solid is appropriate as input for this method.

Options to both methods include the operations type: Union, Difference, or Intersect. The following example demonstrates how to get the intersection of two solids and then find the volume.

<table summary="" id="GUID-602B5423-953C-4EB0-9475-A8B76B726DE8__TABLE_F939877456144C2E9923658BD21FEB17"><tbody><tr><td><b>Code Region: Volume of Solid Intersection</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ComputeIntersectionVolume</span><span>(</span><span>Solid</span><span> solidA</span><span>,</span><span> </span><span>Solid</span><span> solidB</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Solid</span><span> intersection </span><span>=</span><span> </span><span>BooleanOperationsUtils</span><span>.</span><span>ExecuteBooleanOperation</span><span>(</span><span>solidA</span><span>,</span><span> solidB</span><span>,</span><span> </span><span>BooleanOperationsType</span><span>.</span><span>Intersect</span><span>);</span><span>

    </span><span>double</span><span> volumeOfIntersection </span><span>=</span><span> intersection</span><span>.</span><span>Volume</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The methods CutWithHalfSpace() and CutWithHalfSpaceModifyingOriginalSolid() produce a solid which is the intersection of the input Solid with the half-space on the positive side of the given Plane. The positive side of the plane is the side to which Plane.Normal points. The first method creates a new Solid with the results, while the second modifies the existing solid (which must be a solid created by the application instead of one obtained from a Revit element).


<!-- ===== END: Help  Solid and face creation  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Geometry Helper Classes  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:46 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Helper_Classes_html
author: 
---

# Help | Geometry Helper Classes | Autodesk

> ## Excerpt
> Several Geometry Helper classes are in the API. The Helper classes are used to describe geometry information for certain elements, such as defining a CropBox for a view using the BoundingBoxXYZ class.

---
Several Geometry Helper classes are in the API. The Helper classes are used to describe geometry information for certain elements, such as defining a CropBox for a view using the BoundingBoxXYZ class.

-   BoundingBoxXYZ - A 3D rectangular box used in cases such as defining a 3D view section area.
    
-   Transform - Transforming the affine 3D space.
    
-   Reference - A stable reference to a geometric object in a Revit model, which is used when creating elements like dimensions.
    
-   Plane - A flat surface in geometry.
    
-   Options - User preferences for parsing geometry.
    
-   XYZ - Object representing coordinates in 3D space.
    
-   UV - Object representing coordinates in 2D space.
    
-   BoundingBoxUV - A 2D rectangle parallel to the coordinate axes.
    
    ## Transform
    

Transforms are limited to 3x4 transformations (Matrix) in the Revit application, transforming an object's place in the model space relative to the rest of the model space and other objects. The transforms are built from the position and orientation in the model space. Three direction Vectors (BasisX, BasisY and BasisZ properties) and Origin point provide all of the transform information. The matrix formed by the four values is as follows:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-362AC8B3-CB53-4DB6-8606-5D90F2C8BFC4-low.png)Applying the transformation to the point is as follows:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-5ABFA7C5-22F5-4A86-9878-CB0812834EB8-low.png)The Transform OfPoint method implements the previous function.

The Geometry.Transform class properties and methods are identified in the following sections.

### Identity

Transform the Identity.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4AD4178C-E897-44E0-93CD-AA8C1FD39AC4-low.png)CreateReflection()

### Reflect a specified plane.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-DCA42587-9FD4-4AE3-95A8-1D45ED472D14-low.png)**Figure 112: Wall Reflection relationship**

As the previous picture shows, one wall is mirrored by a reference plane. The CreateReflection() method needs the geometry plane information for the reference plane.

<table summary="" id="GUID-78445211-E211-4E27-B080-BE9FA3C50631__TABLE_55F4D5B52B234A66AB018E35EB6FEE0E"><tbody><tr><td><b>Code Region 20-8: Using the Reflection property</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Transform</span><span> </span><span>Reflect</span><span>(</span><span>ReferencePlane</span><span> refPlane</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Transform</span><span> mirTrans </span><span>=</span><span> </span><span>Transform</span><span>.</span><span>CreateReflection</span><span>(</span><span>refPlane</span><span>.</span><span>GetPlane</span><span>());</span><span>

    </span><span>return</span><span> mirTrans</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### CreateRotation() and CreateRotationAtPoint()

Rotate by a specified angle around a specified axis at (0,0,0) or at a specified point.

### CreateTranslation()

Translate by a specified vector. Given a vector XYZ data, a transformation is created as follow:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4E661E3C-0609-44C0-A7D5-52E993FEA94C-low.png)

### Determinant

Transformation determinant.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4570D0C0-0834-4A9E-AB7C-751F771AAE5B-low.png)

### HasReflection

This is a Boolean value that indicates whether the transformation produces a reflection.

### Scale

A value that represents the transformation scale.

### Inverse

An inverse transformation. Transformation matrix A is invertible if a transformation matrix B exists such that A_B = B_A = I (identity).

### IsIdentity

Boolean value that indicates whether this transformation is an identity.

### IsTranslation

Boolean value that indicates whether this transformation is a translation.

Geometry.Transform provides methods to perform basal matrix operations.

### Multiply

Multiplies a transformation by a specified transformation and returns the result.

Operator\* - Multiplies two specified transforms.

### ScaleBasis

Scales the basis vectors and returns the result.

### ScaleBasisAndOrigin

Scales the basis vectors and the transformation origin returns the result.

### OfPoint

Applies the transformation to the point. The Origin property is used.

### OfVector

Applies the transform to the vector. The Origin property is not used.

### AlmostEqual

Compares two transformations. AlmostEqual is consistent with the computation mechanism and accuracy in the Revit core code. Additionally, Equal and the == operator are not implemented in the Transform class.

The API provides several shortcuts to complete geometry transformation. The Transformed property in several geometry classes is used to do the work, as shown in the following table.

**Table 48: Transformed Methods**

<table summary="" id="GUID-78445211-E211-4E27-B080-BE9FA3C50631__TABLE_9D788AF115DF454981260EDB01B11D2E"><tbody><tr><td><b>Class Name</b></td><td><b>Function Description</b></td></tr><tr><td>Curve.get_Transformed(Transform transform)</td><td>Applies the specified transformation to a curve</td></tr><tr><td>GeometryElement.GetTransformed(Transform transform)</td><td>Transforms a copy of the geometry in the original element.</td></tr><tr><td>Profile.get_Transformed(Transform transform)</td><td>Transforms the profile and returns the result.</td></tr><tr><td>Mesh.get_Transformed(Transform transform)</td><td>Transforms the mesh and returns the result.</td></tr></tbody></table>

Note: The transformed method clones itself then returns the transformed cloned result.

In addition to these methods, the Instance class (which is the parent class for elements like family instances, link instances, and imported CAD content) has two methods which provide the transform for a given Instance . The GetTransform() method obtains the basic transform for the instance based on how the instance is placed, while GetTotalTransform() provides the transform modified with the true north transform, for instances like import instances.

## Reference

The Reference is very useful in element creation.

-   Dimension creation requires references.
    
-   The reference identifies a path within a geometric representation tree in a flexible manner.
    
-   The tree is used to view specific geometric representation creation.
    

The API exposes four types of references based on different Pick pointer types. They are retrieved from the API in different ways:

1.  For Point - Curve.GetEndPointReference method
    
2.  For Curve (Line, Arc, and etc.) - Curve.Reference property
    
3.  For Face - Face.Reference property
    
4.  For Cut Edge - Edge.Reference property
    

Different reference types cannot be used arbitrarily. For example:

-   The NewLineBoundaryConditions() method requires a reference for Line
    
-   The NewAreaBoundaryConditions() method requires a reference for Face
    
-   The NewPointBoundaryConditions() method requires a reference for Point.
    

The Reference.ConvertToStableRepresentation() method can be used to save a reference to a geometry object, for example a face, edge, or curve, as a string, and later in the same Revit session (or even in a different session where the same document is present) use ParseFromStableRepresentation() method to obtain an identical Reference using the string as input.

## Options

Geometry is typically extracted from the indexed property Element.Geometry. The original geometry of a beam, column or brace, before the instance is modified by joins, cuts, coping, extensions, or other post-processing, can be extracted using the FamilyInstance.GetOriginalGeometry() method. Both Element.Geometry and FamilyInstance.GetOriginalGeometry() accept an options class which you must supply. The options class customizes the type of output you receive based on its properties:

-   ComputeReferences - Indicates whether to compute the geometry reference when retrieving geometry information. The default value is false, so if this property is not set to true, the reference will not be accessible.
    
-   IncludeNonVisibleObjects - Indicates to also return geometry objects which are not visible in a default view.
    
-   View - Gets geometry information from a specific view. Note that if a view is assigned, the detail level for this view will be used in place of "DetailLevel".
    
-   DetailLevel - Indicates the preferred detail level. The default is Medium.
    
    ### ComputeReferences
    

If you set this property to false, the API does not compute a geometry reference. All Reference properties retrieved from the geometry tree return nothing. For more details about references, refer to the Reference section. This option cannot be set to true when used with FamilyInstance.GetOriginalGeometry().

### IncludeNonVisibleObjects

Most of the non-visible geometry is construction and conditional geometry that the user sees when editing the element (i.e., the center plane of a window family instance). The default for this property is false. However, some of this conditionally visible geometry represents real-world objects, such as insulation surrounding ducts in Revit, and it should be extracted.

### View

If users set the View property to a different view, the retrieved geometry information can be different. Review the following examples for more information:

1.  In Revit, draw a stair in 3D view then select the Crop Region, Crop Region Visible, and Section Box properties in the 3D view. In the Crop Region, modify the section box in the 3D view to display a portion of the stair. If you get the geometry information for the stair using the API and set the 3D view as the Options.View property, only a part of the stair geometry can be retrieved. The following pictures show the stair in the Revit application (left) and one drawn with the API (right).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F6123E3E-4B46-4502-915A-5FC399B34045-low.png)**Figure 113: Different section boxes display different geometry**

Draw a stair in Revit then draw a section as shown in the left picture. If you get the information for this stair using the API and set this section view as the Options.View property, only a part of the stair geometry can be retrieved. The stair drawn with the API is shown in the right picture.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-1095389D-A7C6-4AB8-A6C6-FC8CC3C05EAB-low.png)**Figure 114: Retrieve Geometry section view**

### DetailLevel

The API defines three enumerations in Geometry.Options.DetailLevels. The three enumerations correspond to the three Detail Levels in the Revit application, shown as follows.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-81B8A84A-2F7B-4019-8CC8-4DA11B7A176A-low.png)**Figure 115: Three detail levels**

Different geometry information is retrieved based on different settings in the DetailLevel property. For example, draw a beam in the Revit application then get the geometry from the beam using the API to draw it. The following pictures show the drawing results:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-B1C82974-A3D1-4893-9DF9-E9396C7D6352-low.png)**Figure 116: Detail geometry for a beam**

## BoundingBoxXYZ

BoundingBoxXYZ defines a 3D rectangular box that is required to be parallel to any coordinate axis. Similar to the Instance class, the BoundingBoxXYZ stores data in the local coordinate space. It has a Transform property that transforms the data from the box local coordinate space to the model space. In other words, to get the box boundary in the model space (the same one in Revit), transform each data member using the Transform property. The following sections illustrate how to use BoundingBoxXYZ.

### Define the View Boundaries

BoundingBoxXYZ can be used to define the view boundaries through View.CropBox property. The following pictures use a section view to show how BoundingBoxXYZ is used in the Revit application.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-C517106E-BC7F-4E89-90C4-7FFF1D6B3FD2-low.png)**Figure 117: BoundingBoxXYZ in section view**

The dash lines in the previous pictures show the section view boundary exposed as the CropBox property (a BoundingBoxXYZ instance).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-22E284B3-C514-4EB4-B322-91454006173E-low.png)**Figure 118: Created section view**

The previous picture displays the corresponding section view. The wall outside the view boundary is not displayed.

### Define a Section Box

BoundingBoxXYZ is also used to define a section box for a 3D view retrieved from the View3D.GetSectionBox() method. Select the Section Box property in the Properties Dialog box. The section box is shown as follows:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-1EA1F70A-FFC5-4C58-9446-48E73E9C5606-low.png)**Figure 119: 3D view section box**

### Other Uses

-   Defines a box around an element's geometry. (Element.BoundingBox Property). The BoundingBoxXYZ instance retrieved in this way is parallel to the coordinate axes.
    
-   Used in the ViewSection.CreateDetail () method .
    

The following table identifies the main uses for this class.

**Table 49: BoundingBoxXYZ properties**

<table summary="" id="GUID-78445211-E211-4E27-B080-BE9FA3C50631__TABLE_79392360B14C423FB50AC7D57E87889B"><tbody><tr><td><b>Property Name</b></td><td><b>Usage</b></td></tr><tr><td>Max/Min</td><td>Maximum/Minimum coordinates. These two properties define a 3D box parallel to any coordinate axis. The Transform property provides a transform matrix that can transform the box to the appropriate position.</td></tr><tr><td>Transform</td><td>Transform from the box coordinate space to the model space.</td></tr><tr><td>Enabled</td><td>Indicates whether the bounding box is turned on.</td></tr><tr><td>MaxEnabled/ MinEnabled</td><td>Defines whether the maximum/minimum bound is active for a given dimension.<ul><li>If the Enable property is false, these two properties should also return false.</li></ul><pre><code><span>&lt;table</span><span> </span><span>cellpadding</span><span>=</span><span>"4"</span><span> </span><span>cellspacing</span><span>=</span><span>"0"</span><span> </span><span>summary</span><span>=</span><span>""</span><span> </span><span>id</span><span>=</span><span>"GUID-78445211-E211-4E27-B080-BE9FA3C50631__TABLE_4B666584884A4DFCA168F8AADC62FAA6"</span><span> </span><span>class</span><span>=</span><span>"table"</span><span> </span><span>frame</span><span>=</span><span>"border"</span><span> </span><span>border</span><span>=</span><span>"1"</span><span> </span><span>rules</span><span>=</span><span>"all"</span><span>&gt;</span><span>

</span><span>&lt;tbody</span><span> </span><span>class</span><span>=</span><span>"tbody"</span><span>&gt;</span><span>

</span><span>&lt;tr</span><span> </span><span>class</span><span>=</span><span>"row"</span><span>&gt;</span><span>

</span><span>&lt;td</span><span> </span><span>class</span><span>=</span><span>"entry"</span><span> </span><span>valign</span><span>=</span><span>"top"</span><span>&gt;&lt;img</span><span> </span><span>src</span><span>=</span><span>"../../../images/GUID-ADBBC034-E8AA-4A96-AE95-9D9F82DB5080-low.png"</span><span>/&gt;&lt;/td&gt;</span><span>

</span><span>&lt;td</span><span> </span><span>class</span><span>=</span><span>"entry"</span><span> </span><span>valign</span><span>=</span><span>"top"</span><span>&gt;</span><span>If the crop view is turned on, both </span><span>&lt;b&gt;&lt;i&gt;</span><span>MaxEnabled</span><span>&lt;/i&gt;&lt;/b&gt;</span><span> property and </span><span>&lt;b&gt;&lt;i&gt;</span><span>MinEnabled</span><span>&lt;/i&gt;&lt;/b&gt;</span><span> property return true.

</span><span>&lt;/td&gt;</span><span>

</span><span>&lt;/tr&gt;</span><span>

</span><span>&lt;tr</span><span> </span><span>class</span><span>=</span><span>"row"</span><span>&gt;</span><span>

</span><span>&lt;td</span><span> </span><span>class</span><span>=</span><span>"entry"</span><span> </span><span>valign</span><span>=</span><span>"top"</span><span>&gt;&lt;img</span><span> </span><span>src</span><span>=</span><span>"../../../images/GUID-7050609C-8AAF-40C4-A9A8-F8920B6AD022-low.png"</span><span>/&gt;&lt;/td&gt;</span><span>

</span><span>&lt;td</span><span> </span><span>class</span><span>=</span><span>"entry"</span><span> </span><span>valign</span><span>=</span><span>"top"</span><span>&gt;</span><span>If the crop view is turned off, both </span><span>&lt;b&gt;&lt;i&gt;</span><span>MaxEnabled</span><span>&lt;/i&gt;&lt;/b&gt;</span><span> property and </span><span>&lt;b&gt;&lt;i&gt;</span><span>MinEnabled</span><span>&lt;/i&gt;&lt;/b&gt;</span><span> property return false.

</span><span>&lt;/td&gt;</span><span>

</span><span>&lt;/tr&gt;</span><span>

</span><span>&lt;/tbody&gt;</span><span>

</span><span>&lt;/table&gt;</span></code></pre><ul><li>This property indicates whether the view's crop box face can be used to clip the element's view.</li><li>If BoundingBoxXYZ is retrieved from the View3D.GetSectionBox() method, the return value depends on whether the Section Box property is selected in the 3D view Properties dialog box. If so, all Enabled properties return true.</li><li>If BoundingBoxXYZ is retrieved from the Element.BoundingBox property, all the Enabled properties are true.</li></ul></td></tr><tr><td>Bounds</td><td>Wrapper for the Max/Min properties.</td></tr><tr><td>BoundEnabled</td><td>Wrapper for the MaxEnabled/MinEnabled properties.</td></tr></tbody></table>

The following code sample illustrates how to rotate BoundingBoxXYZ to modify the 3D view section box.

<table summary="" id="GUID-78445211-E211-4E27-B080-BE9FA3C50631__TABLE_BB466252BE8B4EE389A296D445E730B1"><tbody><tr><td><b>Code Region 20-9: Rotating BoundingBoxXYZ</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>RotateBoundingBox</span><span>(</span><span>View3D</span><span> view3d</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>view3d</span><span>.</span><span>IsSectionBoxActive</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"The section box for View3D isn't active."</span><span>);</span><span>
        </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>BoundingBoxXYZ</span><span> box </span><span>=</span><span> view3d</span><span>.</span><span>GetSectionBox</span><span>();</span><span>

    </span><span>// Create a rotation transform to apply to the section box </span><span>
    XYZ origin </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ axis </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>);</span><span>

    </span><span>// Rotate 30 degrees</span><span>
    </span><span>Transform</span><span> rotate </span><span>=</span><span> </span><span>Transform</span><span>.</span><span>CreateRotationAtPoint</span><span>(</span><span>axis</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>/</span><span>6.0</span><span>,</span><span> origin</span><span>);</span><span>

    </span><span>// Transform the View3D's section box with the rotation transform</span><span>
    box</span><span>.</span><span>Transform</span><span> </span><span>=</span><span> box</span><span>.</span><span>Transform</span><span>.</span><span>Multiply</span><span>(</span><span>rotate</span><span>);</span><span>

    </span><span>// Set the section box back to the view (requires an open transaction)</span><span>
    view3d</span><span>.</span><span>SetSectionBox</span><span>(</span><span>box</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## BoundingBoxUV

BoundingBoxUV is a value class that defines a 2D rectangle parallel to the coordinate axes. It supports the Min and Max data members. Together they define the BoundingBoxUV's boundary. BoundingBoxUV is retrieved from the View.Outline property which is the boundary view in the paper space view.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-3CDBA6D9-E139-482E-816C-640D56DE5E63-low.png)**Figure 120: View outline**

Two points define a BoundingBoxUV.

-   Min point - The bottom-left endpoint.
    
-   Max point - The upper-right endpoint.
    

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-71827A01-D568-4770-9457-A279F252DBFD-low.png)**Figure 121: BoundingBoxUV Max and Min**

Note: BoundingBoxUV cannot present a gradient rectangle as the following picture

shows.![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-1A52815E-11F5-4305-B68E-B0A63A06718D-low.png)**Figure 122: Gradient rectangle**


<!-- ===== END: Help  Geometry Helper Classes  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Collection Classes  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:51 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Collection_Classes_html
author: 
---

# Help | Collection Classes | Autodesk

> ## Excerpt
> Specialized geometry collection classes in the Revit API.

---
Specialized geometry collection classes in the Revit API.

The API provides the following collection classes based on the items they contain:

**Table 50: Geometry Collection Classes**

<table summary="" id="GUID-C6604197-214A-4810-916C-98F2636B18A4__TABLE_7D8C6229CA594348A856FFDC11DC953B"><tbody><tr><td><b>Class/Type</b></td><td><b>Corresponding Collection Classes</b></td><td><b>Corresponding Iterators</b></td></tr><tr><td>Edge</td><td>EdgeArray,<p>EdgeArrayArray</p></td><td>EdgeArrayIterator,<p>EdgeArrayArrayIterator</p></td></tr><tr><td>Face</td><td>FaceArray</td><td>FaceArrayIterator</td></tr><tr><td>Reference</td><td>ReferenceArray</td><td>ReferenceArrayIterator</td></tr><tr><td>Double value</td><td>DoubleArray</td><td>DoubleArrayIterator</td></tr></tbody></table>

All of these classes use very similar methods and properties to do similar work. For more details, refer to [Collections](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Collections_html).


<!-- ===== END: Help  Collection Classes  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Extrusion Analysis of a Solid  Autodesk.md ===== -->

---
created: 2026-01-28T21:03:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Extrusion_Analysis_of_a_Solid_html
author: 
---

# Help | Extrusion Analysis of a Solid | Autodesk

> ## Excerpt
> The utility class ExtrusionAnalyzer allows you to attempt to “fit” a given piece of geometry into the shape of an extruded profile. An instance of this class is a single-time use class which should be supplied a solid geometry, a plane, and a direction. After the ExtrusionAnalyzer has been initialized, you can access the results through the following members:

---
The utility class ExtrusionAnalyzer allows you to attempt to “fit” a given piece of geometry into the shape of an extruded profile. An instance of this class is a single-time use class which should be supplied a solid geometry, a plane, and a direction. After the ExtrusionAnalyzer has been initialized, you can access the results through the following members:

-   The GetExtrusionBase() method returns the calculated base profile of the extruded solid aligned to the input plane.
-   The CalculateFaceAlignment() method can be used to identify all faces from the original geometry which do and do not align with the faces of the calculated extrusion. This could be useful to figure out if a wall, for example, has a slanted join at the top as would be the case if there is a join with a roof. If a face is unaligned, something is joined to the geometry that is affecting it.
-   To determine the element that produced the non-aligned face, pass the face to Element.GetGeneratingElementIds(). For more details on this utility, see the following section.

The ExtrusionAnalyzer utility works best for geometry which are at least somewhat “extrusion-like”, for example, the geometry of a wall which may or may not be affected by end joins, floor joins, roof joins, openings cut by windows and doors, or other modifications. Rarely for specific shape and directional combinations the analyzer may be unable to determine a coherent face to act as the base of the extrusion – an InvalidOperationException will be thrown in these situations.

In this example, the extrusion analyzer is used to calculate and outline a shadow formed from the input solid and the sun direction.

<table summary="" id="GUID-02A61B4E-285B-4AF9-AE9D-9543DEA43530__TABLE_70304500F5FF4BAF81A0D4E7573C5348"><tbody><tr><td><b>Code Region: Use Extrusion Analyzer to calculate and draw a shadow outline.</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Draw the shadow of the indicated solid with the sun direction specified.</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>/// &lt;remarks&gt;The shadow will be outlined with model curves added to the document.</span><span>
</span><span>/// A transaction must be open in the document.&lt;/remarks&gt;</span><span>
</span><span>/// &lt;param name="document"&gt;The document.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="solid"&gt;The target solid.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="targetLevel"&gt;The target level where to measure and draw the shadow.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="sunDirection"&gt;The direction from the sun (or light source).&lt;/param&gt;</span><span>
</span><span>/// &lt;returns&gt;The curves created for the shadow.&lt;/returns&gt;</span><span>
</span><span>/// &lt;throws cref="Autodesk.Revit.Exceptions.InvalidOperationException"&gt;Thrown by ExtrusionAnalyzer when the geometry and </span><span>
</span><span>/// direction combined do not permit a successful analysis.&lt;/throws&gt;</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> </span><span>DrawShadow</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Solid</span><span> solid</span><span>,</span><span> </span><span>Level</span><span> targetLevel</span><span>,</span><span> XYZ sunDirection</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create target plane from level.        </span><span>
    </span><span>Plane</span><span> plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>XYZ</span><span>.</span><span>BasisZ</span><span>,</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> targetLevel</span><span>.</span><span>ProjectElevation</span><span>));</span><span>

    </span><span>// Create extrusion analyzer.</span><span>
    </span><span>ExtrusionAnalyzer</span><span> analyzer </span><span>=</span><span> </span><span>ExtrusionAnalyzer</span><span>.</span><span>Create</span><span>(</span><span>solid</span><span>,</span><span> plane</span><span>,</span><span> sunDirection</span><span>);</span><span>

    </span><span>// Get the resulting face at the base of the calculated extrusion.</span><span>
    </span><span>Face</span><span> result </span><span>=</span><span> analyzer</span><span>.</span><span>GetExtrusionBase</span><span>();</span><span>

    </span><span>// Convert edges of the face to curves.</span><span>
    </span><span>CurveArray</span><span> curves </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewCurveArray</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>EdgeArray</span><span> edgeLoop </span><span>in</span><span> result</span><span>.</span><span>EdgeLoops</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Edge</span><span> edge </span><span>in</span><span> edgeLoop</span><span>)</span><span>
        </span><span>{</span><span>
            curves</span><span>.</span><span>Append</span><span>(</span><span>edge</span><span>.</span><span>AsCurve</span><span>());</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// Get the model curve factory object.</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>ItemFactoryBase</span><span> itemFactory</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>document</span><span>.</span><span>IsFamilyDocument</span><span>)</span><span>
        itemFactory </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>;</span><span>
    </span><span>else</span><span>
        itemFactory </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>;</span><span>

    </span><span>// Add a sketch plane for the curves.    </span><span>
    </span><span>CurveLoop</span><span> loop </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveLoop</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Curve</span><span> currentCurve </span><span>in</span><span> curves</span><span>)</span><span>
    </span><span>{</span><span>
        loop</span><span>.</span><span>Append</span><span>(</span><span>currentCurve</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>SketchPlane</span><span> sketchPlane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> loop</span><span>.</span><span>GetPlane</span><span>());</span><span>
    document</span><span>.</span><span>Regenerate</span><span>();</span><span>

    </span><span>// Add the shadow curves</span><span>
    </span><span>ModelCurveArray</span><span> curveElements </span><span>=</span><span> itemFactory</span><span>.</span><span>NewModelCurveArray</span><span>(</span><span>curves</span><span>,</span><span> sketchPlane</span><span>);</span><span>

    </span><span>// Return the ids of the curves created</span><span>
    </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> curveElementIds </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ModelCurve</span><span> curveElement </span><span>in</span><span> curveElements</span><span>)</span><span>
    </span><span>{</span><span>
        curveElementIds</span><span>.</span><span>Add</span><span>(</span><span>curveElement</span><span>.</span><span>Id</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> curveElementIds</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The utility above above can be used to compute the shadow of a given mass with respect to the current sun and shadows settings for the view:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/shadowcalculator.png)


<!-- ===== END: Help  Extrusion Analysis of a Solid  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Finding geometry by ray projection  Autodesk.md ===== -->

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


<!-- ===== END: Help  Finding geometry by ray projection  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Geometry Utility Classes  Autodesk.md ===== -->

---
created: 2026-01-28T21:03:11 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Utility_Classes_html
author: 
---

# Help | Geometry Utility Classes | Autodesk

> ## Excerpt
> A number of utility classes are available for working with geometry objects.

---
A number of utility classes are available for working with geometry objects.

### HostObjectUtils

The HostObjectUtils class offers methods as a shortcut to locate certain faces of compound HostObjects. These utilities retrieve the faces which act as the boundaries of the object's CompoundStructure:

-   HostObjectUtils.GetSideFaces() – applicable to Walls and FaceWalls; you can obtain either the exterior or interior finish faces.
-   HostObjectUtils.GetTopFaces() and HostObjectUtils.GetBottomFaces() – applicable to roofs, floors, and ceilings.
    
    ### SolidUtils
    

The SolidUtils class contains methods to perform operations on solids.

-   SolidUtils.Clone() - creates a new Solid which is a copy of the input Solid
-   SolidUtils.SplitVolumes() - takes a solid which includes disjoint enclosed volumes and returns newly created Solid objects representing each volume. If no splitting is necessary, the input solid is returned.
-   SolidUtils.TessellateSolidOrShell() - triangulates a given input Solid (which can be one or more fully closed volumes, or an open shell). Returns a TriangulatedSolidOrShell object which allows access to the stored triangulated boundary component of a solid or a triangulated connected component of a shell.
-   SolidUtils.CreateTransformed() - creates a new solid which is the transformation of the input solid.
    
    ### JoinGeometryUtils
    

The JoinGeometryUtils class contains methods for joining and unjoining elements, and for managing the order in which elements are joined. These utilities are not available for family documents.

-   JoinGeometryUtils.AreElementsJoined() - determines whether two elements are joined
-   JoinGeometryUtils.GetJoinedElements() - returns all elements joined to given element
-   JoinGeometryUtils.JoinGeometry() - creates a join between two elements that share a comon face. The visible edge between the joined elements is removed. and the joined elements then share the same line weight and fill pattern.
-   JoinGeometryUtils.UnjoinGeometry() - removes a join between two joined elements
-   JoinGeometryUtils.SwitchJoinOrder() - reverses the order in which two elements are joined. The cutting element becomes the cut element and vice versa.
-   JoinGeometryUtils . IsCuttingElementInJoin() - determines whether the first of two joined elements is cutting the second element or vice versa.
    
    ### FacetingUtils
    

This class is used to convert a triangulated structure into a structure in which some of the triangles have been consolidated into quadrilaterals.

-   FacetingUtils.ConvertTrianglesToQuads() - this method takes a TriangulationInterface (constructed from a TriangulatedSolidOrShell) as input and returns a collection of triangles and quadrilaterals representing the original triangulated object.


<!-- ===== END: Help  Geometry Utility Classes  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Room and Space Geometry  Autodesk.md ===== -->

---
created: 2026-01-28T21:03:15 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Room_and_Space_Geometry_html
author: 
---

# Help | Room and Space Geometry | Autodesk

> ## Excerpt
> The Revit API provides access to the 3D geometry of spatial elements (rooms and spaces).

---
The Revit API provides access to the 3D geometry of spatial elements (rooms and spaces).

The SpatialElementGeometryCalculator class can be used to calculate the geometry of a spatial element and obtain the relationships between the geometry and the element's boundary elements. There are 2 options which can be provided to this utility:

-   SpatialElementBoundaryLocation – whether to use finish faces or boundary element centerlines for calculation
-   StoredFreeBoundaryFaces – whether to include faces which don’t map directly to a boundary element in the results.

The results of calculating the geometry are contained in the class SpatialElementGeometryResults. From the SpatialElementGeometryResults class, you can obtain:

-   The Solid volume representing the geometry (GetGeometry() method)
-   The boundary face information (a collection SpatialElementBoundarySubfaces)

Each subface offers:

-   The face of the spatial element
-   The matching face of the boundary element
-   The subface (the portion of the spatial element face bounded by this particular boundary element)
-   The subface type (bottom, top, or side)

Some notes about the use of this utility:

-   The calculator maintains an internal cache for geometry it has already processed. If you intend to calculate geometry for several elements in the same project you should use a single instance of this class. Note that the cache will be cleared when any change is made to the document.
-   Floors are almost never included in as boundary elements. Revit uses the 2D outline of the room to form the bottom faces and does not match them to floor geometry.
-   Openings created by wall-cutting features such as doors and windows are not included in the returned faces.
-   The geometry calculations match the capabilities offered by Revit. In some cases where Revit makes assumptions about how to calculate the volumes of boundaries of rooms and spaces, these assumptions will be present in the output of the utility.

The following example calculates a room's geometry and finds its boundary faces

<table summary="" id="GUID-E7B451BB-21DC-4D72-AD26-75F0C2E911E4__TABLE_4F3221B134B3434CA295DA59DA3ACAB9"><tbody><tr><td><b>Code Region: Face Area using SpatialElementGeometryCalculator</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SpaceArea</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>Room</span><span> room</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>SpatialElementGeometryCalculator</span><span> calculator </span><span>=</span><span> </span><span>new</span><span> </span><span>SpatialElementGeometryCalculator</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// compute the room geometry</span><span>
    </span><span>SpatialElementGeometryResults</span><span> results </span><span>=</span><span> calculator</span><span>.</span><span>CalculateSpatialElementGeometry</span><span>(</span><span>room</span><span>);</span><span>

    </span><span>// get the solid representing the room's geometry</span><span>
    </span><span>Solid</span><span> roomSolid </span><span>=</span><span> results</span><span>.</span><span>GetGeometry</span><span>();</span><span> 

    </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> face </span><span>in</span><span> roomSolid</span><span>.</span><span>Faces</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>double</span><span> faceArea </span><span>=</span><span> face</span><span>.</span><span>Area</span><span>;</span><span>

        </span><span>// get the sub-faces for the face of the room</span><span>
        </span><span>IList</span><span>&lt;</span><span>SpatialElementBoundarySubface</span><span>&gt;</span><span> subfaceList </span><span>=</span><span> results</span><span>.</span><span>GetBoundaryFaceInfo</span><span>(</span><span>face</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>SpatialElementBoundarySubface</span><span> subface </span><span>in</span><span> subfaceList</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>subfaceList</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>1</span><span>)</span><span> </span><span>// there are multiple sub-faces that define the face</span><span>
            </span><span>{</span><span>
                </span><span>// get the area of each sub-face</span><span>
                </span><span>double</span><span> subfaceArea </span><span>=</span><span> subface</span><span>.</span><span>GetSubface</span><span>().</span><span>Area</span><span>;</span><span>             

                </span><span>// sub-faces exist in situations such as when a room-bounding wall has been</span><span>
                </span><span>// horizontally split and the faces of each split wall combine to create the </span><span>
                </span><span>// entire face of the room</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following example calculates a room's geometry and finds its the material of faces that belong to the elements that define the room.

<table summary="" id="GUID-E7B451BB-21DC-4D72-AD26-75F0C2E911E4__TABLE_4896E7E727404ECEB22C3F74F8CB3E78"><tbody><tr><td><b>Code Region: Face Material using SpatialElementGeometryCalculator</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MaterialFromFace</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>string</span><span> s </span><span>=</span><span> </span><span>""</span><span>;</span><span>
        </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>doc</span><span>);</span><span>
        </span><span>Room</span><span> room </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>uidoc</span><span>.</span><span>Selection</span><span>.</span><span>PickObject</span><span>(</span><span>ObjectType</span><span>.</span><span>Element</span><span>).</span><span>ElementId</span><span>)</span><span> </span><span>as</span><span> </span><span>Room</span><span>;</span><span>

        </span><span>SpatialElementBoundaryOptions</span><span>  spatialElementBoundaryOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>SpatialElementBoundaryOptions</span><span>();</span><span>
        spatialElementBoundaryOptions</span><span>.</span><span>SpatialElementBoundaryLocation</span><span> </span><span>=</span><span> </span><span>SpatialElementBoundaryLocation</span><span>.</span><span>Finish</span><span>;</span><span>
        </span><span>SpatialElementGeometryCalculator</span><span> calculator </span><span>=</span><span> </span><span>new</span><span> </span><span>SpatialElementGeometryCalculator</span><span>(</span><span>doc</span><span>,</span><span> spatialElementBoundaryOptions</span><span>);</span><span>
        </span><span>SpatialElementGeometryResults</span><span> results </span><span>=</span><span> calculator</span><span>.</span><span>CalculateSpatialElementGeometry</span><span>(</span><span>room</span><span>);</span><span>
        </span><span>Solid</span><span> roomSolid </span><span>=</span><span> results</span><span>.</span><span>GetGeometry</span><span>();</span><span> 

        </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> roomSolidFace </span><span>in</span><span> roomSolid</span><span>.</span><span>Faces</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>SpatialElementBoundarySubface</span><span> subface </span><span>in</span><span> results</span><span>.</span><span>GetBoundaryFaceInfo</span><span>(</span><span>roomSolidFace</span><span>))</span><span>
            </span><span>{</span><span>
                </span><span>Face</span><span> boundingElementface </span><span>=</span><span> subface</span><span>.</span><span>GetBoundingElementFace</span><span>();</span><span>
                </span><span>ElementId</span><span> id </span><span>=</span><span> boundingElementface</span><span>.</span><span>MaterialElementId</span><span>;</span><span>
                s </span><span>+=</span><span>  doc</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>).</span><span>Name</span><span> </span><span>+</span><span> </span><span>", id = "</span><span> </span><span>+</span><span> id</span><span>.</span><span>IntegerValue</span><span>.</span><span>ToString</span><span>()</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"revit"</span><span>,</span><span>s</span><span>);</span><span>                 
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Room and Space Geometry  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Sketching  Autodesk.md ===== -->

---
created: 2026-01-28T21:03:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_html
author: 
---

# Help | Sketching | Autodesk

> ## Excerpt
> Sketches define the shape of many elements in Revit such as:

---
Sketches define the shape of many elements in Revit such as:

-   Ceiling
-   Extrusion
-   Filled Region
-   Floor
-   Opening
-   Stair
-   Railing
-   Roof

In addition to Sketch Elements, ModelCurve is also described in this chapter. For more details about Element Classification, see [Element Classification](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_Element_Classification_html) in the [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html) section.

## Sketches of Ceilings, Floors, Walls, or Openings

### Getting the Sketch

You cannot retrieve a Sketch object by iterating the Document with a FilteredElementCollector. Instead, use these properties to get the element id of the element's sketch.

-   Ceiling.SketchId
-   Floor.SketchId
-   Opening.SketchId
-   Wall.SketchId

For a given sketch, you can get element (Floor, Wall...) that owns the sketch with the `Sketch.OwnerId` property. `Sketch.GetAllElements()` returns all elements (ModelCurve, ReferencePlane, Dimension) that belong to a sketch.

### Editing and Validating the Sketch

Use the `SketchEditScope` class to edit the sketch. While a Sketch editing session is active, you can add, delete or modify Sketch elements (curves, dimensions, reference planes). A transaction will be needed to make the changes. When you finish the session, the Sketch-based element will be updated.

Key methods include:

-   SketchEditScope constructor - Creates a new SketchEditScope
-   Start() - Starts editing a particular sketch. After this is started only elements owned by the Sketch and new elements to be added to the Sketch may be modified
-   StartWithNewSketch() - Because a valid sketch may not initially exist for some Revit elements (such as Walls or Analytical Elements), a valid sketch will need to be created before it can be edited.
-   Commit() - Commits the changes
-   IsSketchEditingSupported() - Checks if a sketch can be edited with a SketchEditScope

#### Boundary Validation

The `BoundaryValidation` class provides methods to validate curve loops for sketching:

-   `IsValidHorizontalBoundary` identifies whether the provided curve loops create a valid horizontal boundary
-   `IsValidBoundaryOnView` checks that a curve loop boundary is valid on the view's sketch plane.
-   `IsValidBoundaryOnSketchPlane` checks that a curve loop boundary is valid on a sketch plane

**Code Region: Edit a Floor Sketch**

```
private void EditSketch(Floor floor)
{
 // Delete all lines in the sketch & create two new arcs that form a circle
 Document doc = floor.Document;
 Sketch sketch = doc.GetElement(floor.SketchId) as Sketch;
 using (SketchEditScope edit = new SketchEditScope(doc, "Edit Floor"))
 {
  edit.Start(floor.SketchId);
  using (Transaction t = new Transaction(doc, "Edit Sketch"))
  {
   t.Start();

   doc.Delete(sketch.GetAllElements());

   doc.Create.NewModelCurve(
    Arc.Create(sketch.SketchPlane.GetPlane(), 5, 0, Math.PI * 2),
    sketch.SketchPlane);

   t.Commit();
  }
  edit.Commit(new failuresPreprocessor());
 }
}

private class failuresPreprocessor : IFailuresPreprocessor
{
 public FailureProcessingResult PreprocessFailures(FailuresAccessor failuresAccessor)
 {
  return FailureProcessingResult.Continue;
 }
}
```


<!-- ===== END: Help  Sketching  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  The 2D Sketch Class  Autodesk.md ===== -->

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


<!-- ===== END: Help  The 2D Sketch Class  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  3D Sketch  Autodesk.md ===== -->

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


<!-- ===== END: Help  3D Sketch  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  ModelCurve  Autodesk.md ===== -->

---
created: 2026-01-28T21:03:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_ModelCurve_html
author: 
---

# Help | ModelCurve | Autodesk

> ## Excerpt
> ModelCurve represents model lines in the project. It exists in 3D space and is visible in all views.

---
ModelCurve represents model lines in the project. It exists in 3D space and is visible in all views.

The following pictures illustrate the four ModelCurve derived classes:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-1CE68863-4E07-4852-A896-5ACE5235B7AE-low.png)**Figure 92:ModelLine and ModelArc**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-E914167B-553C-4B5B-A87E-1AAB487A12B5-low.png)**Figure 93: ModelEllipse and ModelNurbSpline**

### Creating a ModelCurve

The key to creating a ModelCurve is to create the Geometry.Curve and SketchPlane where the Curve is located. Based on the Geometry.Curve type you input, the corresponding ModelCurve returned can be downcast to its correct type.

The following sample illustrates how to create a new model curve (ModelLine and ModelArc):

<table summary="" id="GUID-79FE567A-0CE4-40A1-BB44-05DAA921C5B6__TABLE_479155D66CC048248E4AE6F8E176FD81"><tbody><tr><td><b>Code Region 17-2: Creating a new model curve</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateModelCurves</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// get handle to application from document</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>;</span><span>

    </span><span>// Create a geometry line in Revit application</span><span>
    XYZ startPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ endPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Line</span><span> geomLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>startPoint</span><span>,</span><span> endPoint</span><span>);</span><span>

    </span><span>// Create a geometry arc in Revit application</span><span>
    XYZ end0 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ end1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>10</span><span>);</span><span>
    XYZ pointOnCurve </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Arc</span><span> geomArc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>end0</span><span>,</span><span> end1</span><span>,</span><span> pointOnCurve</span><span>);</span><span>

    </span><span>// Create a geometry plane in Revit application</span><span>
    XYZ origin </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ normal </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Plane</span><span> geomPlane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>normal</span><span>,</span><span> origin</span><span>);</span><span>

    </span><span>// Create a sketch plane in current document</span><span>
    </span><span>SketchPlane</span><span> sketch </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> geomPlane</span><span>);</span><span>

    </span><span>// Create a ModelLine element using the created geometry line and sketch plane</span><span>
    </span><span>ModelLine</span><span> line </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geomLine</span><span>,</span><span> sketch</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>;</span><span>

    </span><span>// Create a ModelArc element using the created geometry arc and sketch plane</span><span>
    </span><span>ModelArc</span><span> arc </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geomArc</span><span>,</span><span> sketch</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelArc</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Members

GeometryCurve

The GeometryCurve property is used to get or set the model curve's geometry curve. Except for ModelHermiteSpline, you can get different Geometry.Curves from the four ModelCurves;

-   Line
-   Arc
-   Ellipse
-   Nurbspline.

The following code sample illustrates how to get a specific Curve from a ModelCurve.

<table summary="" id="GUID-79FE567A-0CE4-40A1-BB44-05DAA921C5B6__TABLE_CFEBA8C139D3438389227DE1A8D0D11F"><tbody><tr><td><b>Code Region 17-3: Getting a specific Curve from a ModelCurve</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetCurve</span><span>(</span><span>ModelCurve</span><span> modelCurve</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>//get the geometry modelCurve of the model modelCurve</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> geoCurve </span><span>=</span><span> modelCurve</span><span>.</span><span>GeometryCurve</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>geoCurve </span><span>is</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Line</span><span>)</span><span>
    </span><span>{</span><span>
            </span><span>Line</span><span> geoLine </span><span>=</span><span> geoCurve </span><span>as</span><span> </span><span>Line</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The GeometryCurve property return value is a general Geometry.Curve object, therefore, you must use an As operator to convert the object type.

Note: The following information applies to GeometryCurve:

-   In Revit you cannot create a Hermite curve but you can import it from other software such as AutoCAD. Geometry.Curve is the only geometry class that represents the Hermite curve.
-   The SetPlaneAndCurve() method and the Curve and SketchPlane property setters are used in different situations.
    -   When the new Curve lies in the same SketchPlane, or the new SketchPlane lies on the same planar face with the old SketchPlane, use the Curve or SketchPlane property setters.
    -   If new Curve does not lay in the same SketchPlane, or the new SketchPlane does not lay on the same planar face with the old SketchPlane, you must simultaneously change the Curve value and the SketchPlane value using SetPlaneAndCurve() to avoid internal data inconsistency.
        
        #### Line Styles
        

Line styles are represented by the GraphicsStyle class. All line styles for a ModelCurve are available from the GetLineStyleIds() method which returns a set of ElementIds of GraphicsStyle elements.


<!-- ===== END: Help  ModelCurve  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Material  Autodesk.md ===== -->

---
created: 2026-01-28T21:03:38 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_html
author: 
---

# Help | Material | Autodesk

> ## Excerpt
> In the Revit Platform API, material data is stored and managed as an Element. Just as in the Revit UI, a material can have several assets associated with it, but only thermal and structural (referred to as Physical in the Revit UI) assets can be assigned using the API.

---
In the Revit Platform API, material data is stored and managed as an Element. Just as in the Revit UI, a material can have several assets associated with it, but only thermal and structural (referred to as Physical in the Revit UI) assets can be assigned using the API.

Some material features are represented by properties on the Material class itself, such as FillPattern, Color, or Render while others are available as properties of either a structural or thermal asset associated with the material.

In this chapter, you learn how to access material elements and how to manage the Material objects in the document. [Element Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Element_Material_html) provides a walkthrough showing how to get a window material.


<!-- ===== END: Help  Material  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  General Material Information  Autodesk.md ===== -->

---
created: 2026-01-28T21:03:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_General_Material_Information_html
author: 
---

# Help | General Material Information | Autodesk

> ## Excerpt
> Before you begin the walkthrough, read through the following section for a better understanding of the Material class.

---
Before you begin the walkthrough, read through the following section for a better understanding of the Material class.

All Material objects can be retrieved using a Material class filter. Material objects are also available in Document, Category, Element, Face, and so on, and are discussed in the pertinent sections in this chapter. Wherever you get a material object, it is represented as the Material class.

### Properties

A material will have one or more aspects pertaining to rendering appearance, structure, or other major material category. Each aspect is represented by properties on the Material class itself or via one of its assets, structural or thermal. The StructuralAsset class represents the properties of a material pertinent to structural analysis. The ThermalAsset class represents the properties of a material pertinent to energy analysis.

<table summary="" id="GUID-F0C7BA6A-8C58-45B4-8639-1E08CBC6781D__TABLE_CEF5B6EF8B0D48DBB98774BC02AAC136"><tbody><tr><td><b>Code Region 19-3: Getting material properties</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ReadMaterialProps</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Material</span><span> material</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ElementId</span><span> strucAssetId </span><span>=</span><span> material</span><span>.</span><span>StructuralAssetId</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>strucAssetId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>PropertySetElement</span><span> pse </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>strucAssetId</span><span>)</span><span> </span><span>as</span><span> </span><span>PropertySetElement</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>pse </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>StructuralAsset</span><span> asset </span><span>=</span><span> pse</span><span>.</span><span>GetStructuralAsset</span><span>();</span><span>

            </span><span>// Check the material behavior and only read if Isotropic</span><span>
            </span><span>if</span><span> </span><span>(</span><span>asset</span><span>.</span><span>Behavior</span><span> </span><span>==</span><span> </span><span>StructuralBehavior</span><span>.</span><span>Isotropic</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// Get the class of material</span><span>
                </span><span>StructuralAssetClass</span><span> assetClass </span><span>=</span><span> asset</span><span>.</span><span>StructuralAssetClass</span><span>;</span><span> </span><span>// Get other material properties</span><span>

                </span><span>// Get other material properties</span><span>
                </span><span>double</span><span> poisson </span><span>=</span><span> asset</span><span>.</span><span>PoissonRatio</span><span>.</span><span>X</span><span>;</span><span>
                </span><span>double</span><span> youngMod </span><span>=</span><span> asset</span><span>.</span><span>YoungModulus</span><span>.</span><span>X</span><span>;</span><span>
                </span><span>double</span><span> thermCoeff </span><span>=</span><span> asset</span><span>.</span><span>ThermalExpansionCoefficient</span><span>.</span><span>X</span><span>;</span><span>
                </span><span>double</span><span> unitweight </span><span>=</span><span> asset</span><span>.</span><span>Density</span><span>;</span><span>
                </span><span>double</span><span> shearMod </span><span>=</span><span> asset</span><span>.</span><span>ShearModulus</span><span>.</span><span>X</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>assetClass </span><span>==</span><span> </span><span>StructuralAssetClass</span><span>.</span><span>Metal</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>double</span><span> dMinStress </span><span>=</span><span> asset</span><span>.</span><span>MinimumYieldStress</span><span>;</span><span>
                </span><span>}</span><span>
                </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>assetClass </span><span>==</span><span> </span><span>StructuralAssetClass</span><span>.</span><span>Concrete</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>double</span><span> dConcComp </span><span>=</span><span> asset</span><span>.</span><span>ConcreteCompression</span><span>;</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Classification

The material classification relevant to structural analysis (i.e. steel, concrete, wood) can be obtained from the StructuralAssetClass property of the StructuralAsset associated with the material.

Note: The API does not provide access to the values of Concrete Type for Concrete material.

The material classification relevant to energy analysis (i.e. solid, liquid, gas) can be obtained from the ThermalMaterialType property of the ThermalAsset associated with the material.

### Other Properties

The material object properties identify a specific type of material including color, fill pattern, and more.

#### Properties and Parameter

Some Material properties are only available as a Parameter. A few, such as Color, are available as a property or as a Parameter using the BuiltInParameter MATERIAL\_PARAM\_COLOR.

#### Rendering Information

Collections of rendering data are organized into objects called Assets. You can obtain all available Appearance-related assets from the Application.Assets property. An appearance asset can be accessed from a material via the Material.AppearanceAssetId property.

The following figure shows the Appearance Library section of the Asset Browser dialog box, which shows how some rendering assets are displayed in the UI.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/AssetBrowser.jpg)**Figure 106: Appearance Library**

The Materials sample application included with the SDK shows how to set the RenderApperance property to a material selected in a dialog. The dialog is populated with all the Asset objects in Application.Assets.

#### Editing properties of an Appearance Asset

Editing properties in an appearance Asset requires establishment of an edit scope. The new class

```
Autodesk.Revit.DB.Visual.AppearanceAssetEditScope
```

allows an application to create and maintain an editing session for an appearance asset. The scope provides access to an editable Asset object whose properties may be changed. Once all of the desired changes have been made to the asset's properties, the edit scope should be committed, which causes the changes to be sent back into the document. (This is the only part of the process when a transaction must be opened).

The methods of this class are

-   AppearanceAssetEditScope.Start() – Starts the edit scope for the asset contained in a particular AppearanceAssetElement. The editable Asset is returned from this method.
-   AppearanceAssetEditScope.Commit() – Finishes the edit scope: all changes made during the edit scope will be committed. Provides an option to force the update of all open views.
-   AppearanceAssetEditScope.Cancel() – Cancels the edit scope and discards any changes.

##### Connected Assets

Connected assets are associated to properties in appearance assets, and represent subordinate objects encapsulating a collection of related properties. One example of a connected asset is the "Unified Bitmap" representing an image and its mapping parameters and values. AssetProperty offers methods to provide the ability to modify, add or delete the asset connected to a property:

-   AssetProperty.GetSingleConnectedAsset() – Gets the single connected asset of this property
-   AssetProperty.RemoveConnectedAsset() – Removes the single connected asset of this property
-   AssetProperty.AddConnectedAsset (String schemaId) – Create a new default asset of schema type and connects it to this property
-   AssetProperty.AddCopyAsConnectedAsset() – Connects the property to a copy of the asset

##### Schemas & Property names

Appearance asset properties are aligned with specific schemas. Each schema contains necessary properties which define how the appearance of the material will be generated. There are 14 standard material schemas:

-   Ceramic
-   Concrete
-   Generic
-   Glazing
-   Hardwood
-   MasonryCMU
-   Metal
-   MetallicPaint
-   Mirror
-   PlasticVinyl
-   SolidGlass
-   Stone
-   WallPaint
-   Water

In addition, there are 5 schemas representing "advanced" materials - these may be encountered as a result of import from other Autodesk products:

-   AdvancedLayered
-   AdvancedMetal
-   AdvancedOpaque
-   AdvancedTransparent
-   AdvancedWood

Finally, there are 10 schemas used for the aspects of the connected assets:

-   BumpMap
-   Checker
-   Gradient
-   Marble
-   Noise
-   Speckle
-   Tile
-   UnifiedBitmap
-   Wave
-   Wood

The method:

```
 AssetProperty.IsValidSchemaIdentifier(String schemaName)
```

identifies if the input name is a valid name for a supported schema.

To assist in creating code accessing and manipulating the properties of a given schema, predefined properties have been introduced to allow a compile-time reference to a property name without requiring you to transcribe it as a string in your code. These predefined property names are available in static classes named similar to the schema names, above, e.g. Autodesk.Revit.DB.Visual.Ceramic.

##### Asset Utilities

The method:

-   Application.GetAssets(AssetType)

returns a list of assets available to the session.

The method:

-   AppearanceAssetElement.Duplicate()

creates a copy of an appearance asset element and the asset contained by it.

The operator:

-   Asset.operator\[ \]

accesses a particular AssetProperty associated to the given asset.

#### FillPattern

All FillPatterns in a document are available using a FilteredElementCollector filtering on class FillPatternElement. A FillPatternElement is an element that contains a FillPattern while the FillPattern class provides access to the pattern name and the set of FillGrids that make up the pattern.

There are two kinds of FillPatterns: Drafting and Model. In the UI, you can only set Drafting fill patterns to Material.CutForegroundPatternId or Material.CutBackgroundPatternId. The fill pattern type is exposed via the FillPattern.Target property. The following example shows how to change the material FillPattern.

<table summary="" id="GUID-F0C7BA6A-8C58-45B4-8639-1E08CBC6781D__TABLE_DF5D0D5974C541FE8D1B4A77E88879FE"><tbody><tr><td><b>Code Region 19-4: Setting the fill pattern</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SetFillPattern</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Material</span><span> material</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> fillPatternElements </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FillPatternElement</span><span>)).</span><span>ToElementIds</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> fillPatternId </span><span>in</span><span> fillPatternElements</span><span>)</span><span>
    </span><span>{</span><span>
        material</span><span>.</span><span>CutForegroundPatternId</span><span> </span><span>=</span><span> fillPatternId</span><span>;</span><span>
        material</span><span>.</span><span>SurfaceForegroundPatternId</span><span> </span><span>=</span><span> fillPatternId</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  General Material Information  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Material Management  Autodesk.md ===== -->

---
created: 2026-01-28T21:03:47 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Material_Management_html
author: 
---

# Help | Material Management | Autodesk

> ## Excerpt
> You can use filtering to retrieve all materials in the document. Every Material object in the Document is identified by a unique name.

---
You can use filtering to retrieve all materials in the document. Every Material object in the Document is identified by a unique name.

The following example illustrates how to use the material name to get material.

<table summary="" id="GUID-8928F399-9E98-4C5B-A778-1E5E8DADF5AF__TABLE_1F839372D0694C90BCB0F8EC95D5B6D8"><tbody><tr><td><b>Code Region 19-5: Getting a material by name</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MaterialByName</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> elementCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    elementCollector</span><span>.</span><span>WherePasses</span><span>(</span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>Material</span><span>)));</span><span>
    </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> materials </span><span>=</span><span> elementCollector</span><span>.</span><span>ToElements</span><span>();</span><span>

    </span><span>Material</span><span> floorMaterial </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>string</span><span> floorMaterialName </span><span>=</span><span> </span><span>"Default Floor"</span><span>;</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> materialElement </span><span>in</span><span> materials</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Material</span><span> material </span><span>=</span><span> materialElement </span><span>as</span><span> </span><span>Material</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>floorMaterialName </span><span>==</span><span> material</span><span>.</span><span>Name</span><span>)</span><span>
        </span><span>{</span><span>
            floorMaterial </span><span>=</span><span> material</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> floorMaterial</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Material found."</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre><p><span>Note:</span> To run the sample code, make sure the material name exists in your document. All material names for the current document are located under the Manage tab (Project Settings panel &gt; Materials.)</p></td></tr></tbody></table>

### Creating Materials

There are two ways to create a new Material object in the API.

-   Duplicate an existing Material
    
-   Add a new Material.
    

When using the Duplicate() method, the returned Material object is the same type as the original.

<table summary="" id="GUID-8928F399-9E98-4C5B-A778-1E5E8DADF5AF__TABLE_654837E6A6BE4A2FB4C0B2CE908A1CAE"><tbody><tr><td><b>Code Region 19-6: Duplicating a material</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>bool</span><span> </span><span>DuplicateMaterial</span><span>(</span><span>Material</span><span> material</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>bool</span><span> duplicated </span><span>=</span><span> </span><span>false</span><span>;</span><span>
        </span><span>//try to duplicate a new instance of Material class using duplicate method</span><span>
        </span><span>//make sure the name of new material is unique in MaterailSet</span><span>
        </span><span>string</span><span> newName </span><span>=</span><span> </span><span>"new"</span><span> </span><span>+</span><span> material</span><span>.</span><span>Name</span><span>;</span><span>
        </span><span>Material</span><span> myMaterial </span><span>=</span><span> material</span><span>.</span><span>Duplicate</span><span>(</span><span>newName</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> myMaterial</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Failed to duplicate a material!"</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
                duplicated </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> duplicated</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Use the static method Material.Create() to add a new Material directly. No matter how it is applied, it is necessary to specify a unique name for the material and any assets belonging to the material. The unique name is the Material object key.

<table summary="" id="GUID-8928F399-9E98-4C5B-A778-1E5E8DADF5AF__TABLE_20E15F95752D446CB62CE19BA3BC5220"><tbody><tr><td><b>Code Region 19-7: Adding a new Material</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateMaterial</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>//Create the material</span><span>
    </span><span>ElementId</span><span> materialId </span><span>=</span><span> </span><span>Material</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"My Material"</span><span>);</span><span>
    </span><span>Material</span><span> material </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>materialId</span><span>)</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>

    </span><span>//Create a new property set that can be used by this material</span><span>
    </span><span>StructuralAsset</span><span> strucAsset </span><span>=</span><span> </span><span>new</span><span> </span><span>StructuralAsset</span><span>(</span><span>"My Property Set"</span><span>,</span><span> </span><span>StructuralAssetClass</span><span>.</span><span>Concrete</span><span>);</span><span>
    strucAsset</span><span>.</span><span>Behavior</span><span> </span><span>=</span><span> </span><span>StructuralBehavior</span><span>.</span><span>Isotropic</span><span>;</span><span>
    strucAsset</span><span>.</span><span>Density</span><span> </span><span>=</span><span> </span><span>232.0</span><span>;</span><span>

    </span><span>//Assign the property set to the material.</span><span>
    </span><span>PropertySetElement</span><span> pse </span><span>=</span><span> </span><span>PropertySetElement</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> strucAsset</span><span>);</span><span>
    material</span><span>.</span><span>SetMaterialAspectByPropertySet</span><span>(</span><span>MaterialAspect</span><span>.</span><span>Structural</span><span>,</span><span> pse</span><span>.</span><span>Id</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Deleting Materials

To delete a material use:

-   Document.Delete()

Document.Delete() is a generic method. See [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html) for details.


<!-- ===== END: Help  Material Management  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Element Material  Autodesk.md ===== -->

---
created: 2026-01-28T21:03:52 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Element_Material_html
author: 
---

# Help | Element Material | Autodesk

> ## Excerpt
> One element can have several elements and components. For example, FamilyInstance has SubComponents and Wall has CompoundStructure which contain several CompoundStructureLayers. (For more details about SubComponents refer to the Family Instances section and refer to Walls, Floors, Roofs and Openings for more information about CompoundStructure.)

---
One element can have several elements and components. For example, FamilyInstance has SubComponents and Wall has CompoundStructure which contain several CompoundStructureLayers. (For more details about SubComponents refer to the Family Instances section and refer to [Walls, Floors, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html) for more information about CompoundStructure.)

In the Revit Platform API, get an element's materials using the following guidelines:

-   If the element contains elements, get the materials separately.
-   If the element contains components, get the material for each component from the parameters or in specific way (see [Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_html) section in [Walls, Floors, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html)).
-   If the component's material returns null, get the material from the corresponding Element.Category sub Category.
    
    ### Material in a Parameter
    

If the Element object has a Parameter with a Definition whose GetDataType() method returns SpecTypeId.Reference.Material, you can get the element material from the Parameter. For example, a structural column FamilySymbol (a FamilyInstance whose Category is BuiltInCategory.OST\_StructuralColumns) has the Structural Material parameter. Get the Material using the ElementId. The following code example illustrates how to get the structural column Material that has one component.

<table summary="" id="GUID-FD067FA5-623D-474B-98FB-686C096F0165__TABLE_31045170AC5541C0B8B41E6A6586AB36"><tbody><tr><td><b>Code Region: Getting an element material from a parameter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetMaterialFromParameter</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> familyInstance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Parameter</span><span> parameter </span><span>in</span><span> familyInstance</span><span>.</span><span>Parameters</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Definition</span><span> definition </span><span>=</span><span> parameter</span><span>.</span><span>Definition</span><span>;</span><span>
        </span><span>// material is stored as element id</span><span>
        </span><span>if</span><span> </span><span>(</span><span>parameter</span><span>.</span><span>StorageType</span><span> </span><span>==</span><span> </span><span>StorageType</span><span>.</span><span>ElementId</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>definition</span><span>.</span><span>ParameterGroup</span><span> </span><span>==</span><span> </span><span>BuiltInParameterGroup</span><span>.</span><span>PG_MATERIALS </span><span>&amp;&amp;</span><span>
                definition</span><span>.</span><span>GetDataType</span><span>()</span><span> </span><span>==</span><span> </span><span>SpecTypeId</span><span>.</span><span>Reference</span><span>.</span><span>Material</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> material </span><span>=</span><span> </span><span>null</span><span>;</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> materialId </span><span>=</span><span> parameter</span><span>.</span><span>AsElementId</span><span>();</span><span>
                </span><span>if</span><span> </span><span>(-</span><span>1</span><span> </span><span>==</span><span> materialId</span><span>.</span><span>IntegerValue</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>//Invalid ElementId, assume the material is "By Category"</span><span>
                    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familyInstance</span><span>.</span><span>Category</span><span>)</span><span>
                    </span><span>{</span><span>
                        material </span><span>=</span><span> familyInstance</span><span>.</span><span>Category</span><span>.</span><span>Material</span><span>;</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>
                </span><span>else</span><span>
                </span><span>{</span><span>
                    material </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>materialId</span><span>)</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>
                </span><span>}</span><span>

                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Element material: "</span><span> </span><span>+</span><span> material</span><span>.</span><span>Name</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: If the material property is set to By Category in the UI, the ElementId for the material is ElementId.InvalidElementId and cannot be used to retrieve the Material object as shown in the sample code. Try retrieving the Material from Category as described in the next section.

Some material properties contained in other compound parameters are not accessible from the API. As an example, in the following figure, for System Family: Railing, the Rail Structure parameter's StorageType is StorageType.None. As a result, you cannot get material information in this situation.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ByCategory.jpg)

**Figure 107: Rail structure property**

### Material and FamilyInstance

Beam, Column and Foundation FamilyInstances have another way to get their material using their StructuralMaterialId property. This property returns an ElementId which identifies the material that defines the instance's structural analysis properties.

<table summary="" id="GUID-FD067FA5-623D-474B-98FB-686C096F0165__TABLE_8B5ABF07F2E64065B30704FA6E86C2BD"><tbody><tr><td><b>Code Region: Getting an element material from a family instance</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Material</span><span> </span><span>GetFamilyInstanceMaterial</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> beam</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Material</span><span> material </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>beam</span><span>.</span><span>StructuralMaterialId</span><span>)</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>

    </span><span>return</span><span> material</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Material and Category

Only model elements can have material.

From the Revit Manage tab, click Settings![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ac.menuaro.gif)Object Styles to display the Object Styles dialog box. Elements whose category is listed in the Model Objects tab have material information.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ModelObjectsMaterial.jpg)**Figure 108: Category material**

Only Model elements can have the Material property assigned. Querying Material for a category that corresponds to other than Model elements (e.g. Annotations or Imported) will therefore always result in a null. For more details about the Element and Category classifications, refer to [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html).

If an element has more than one component, some of the Category.Subcategories correspond to the components.

In the previous Object Styles dialog box, the Windows Category and the Frame/Mullion and Glass subcategories are mapped to components in the windows element. In the following picture, it seems the window symbol Glass Pane Material parameter is the only way to get the window pane material. However, the value is By Category and the corresponding Parameter returns ElementId.InvalidElementId.

In this case, the pane's Material is not null and it depends on the Category OST\_WindowsFrameMullionProjection's Material property which is a subcategory of the window's category, OST\_Windows. If it returns null as well, the pane's Material is determined by the parent category OST\_Windows. For more details, refer to [Element Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Element_Material_html).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4E345BF1-1837-41C7-BF9C-A89A1A76539F-low.png)**Figure 109: Window material**

### CompoundStructureLayer Material

You can get the CompoundStructureLayer object from HostObjAttributes. For more details, refer to [Walls, Floors, Ceilings, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html).

### Retrieve Element Materials

The following diagram shows the workflow to retrieve Element Materials:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-64D41480-87CE-454E-8B14-1EFEFEC8BF09-low.png)**Figure 110: Getting Element Material workflow**

This workflow illustrates the following process:

-   The workflow shows how to get the Material object (not Autodesk.Revit.DB.Structure.StructuralMaterialType enumerated type) that belongs to the element.
-   There are two element classifications when retrieving the Material:
    -   HostObject with CompoundStructure - Get the Material object from the CompoundStructureLayer class MaterialId property.
    -   Others - Get the Material from the Parameters.
-   When you get a null Material object or an invalid ElementId with a value of ElementId.InvalidElementId, try the Material from the corresponding category. Note that a FamilyInstance and its FamilySymbol usually have the same category.
-   The more you know about the Element object, the easier it is to get the material. For example:
    -   If you know the Element is a beam, you can get the instance parameter Structural Material
    -   If you know the element is a window, you can cast it to a FamilyInstance and get the FamilySymbol.
-   After that you can get the Parameters such as Frame Exterior Material or Frame Interior Material to get the Material object. If you get null try to get the Material object from the FamilySymbol Category.
-   Not all Element Materials are available in the API.
    
    ### Walkthrough: Get Window Materials
    

The following code illustrates how to get the Window Materials.

<table summary="" id="GUID-FD067FA5-623D-474B-98FB-686C096F0165__TABLE_FA4B8EFD22EE42ABB74FEB91E3A6A11C"><tbody><tr><td><b>Code Region: Getting window materials walkthrough</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetWindowMaterial</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> window</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FamilySymbol</span><span> windowSymbol </span><span>=</span><span> window</span><span>.</span><span>Symbol</span><span>;</span><span>
    </span><span>Category</span><span> category </span><span>=</span><span> windowSymbol</span><span>.</span><span>Category</span><span>;</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> frameExteriorMaterial </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> frameInteriorMaterial </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> sashMaterial </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>// Check the parameters first</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Parameter</span><span> parameter </span><span>in</span><span> windowSymbol</span><span>.</span><span>Parameters</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>switch</span><span> </span><span>(</span><span>parameter</span><span>.</span><span>Definition</span><span>.</span><span>Name</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>case</span><span> </span><span>"Frame Exterior Material"</span><span>:</span><span>
                frameExteriorMaterial </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>parameter</span><span>.</span><span>AsElementId</span><span>())</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>"Frame Interior Material"</span><span>:</span><span>
                frameInteriorMaterial </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>parameter</span><span>.</span><span>AsElementId</span><span>())</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>"Sash"</span><span>:</span><span>
                sashMaterial </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>parameter</span><span>.</span><span>AsElementId</span><span>())</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>default</span><span>:</span><span>
                </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>// Try category if the material is set by category</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> frameExteriorMaterial</span><span>)</span><span>
        frameExteriorMaterial </span><span>=</span><span> category</span><span>.</span><span>Material</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> frameInteriorMaterial</span><span>)</span><span>
        frameInteriorMaterial </span><span>=</span><span> category</span><span>.</span><span>Material</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> sashMaterial</span><span>)</span><span>
        sashMaterial </span><span>=</span><span> category</span><span>.</span><span>Material</span><span>;</span><span>
    </span><span>// Show the result because the category may have a null Material,</span><span>
    </span><span>// the Material objects need to be checked.</span><span>
    </span><span>string</span><span> materialsInfo </span><span>=</span><span> </span><span>"Frame Exterior Material: "</span><span> </span><span>+</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> frameExteriorMaterial </span><span>?</span><span> frameExteriorMaterial</span><span>.</span><span>Name</span><span> </span><span>:</span><span> </span><span>"null"</span><span>)</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    materialsInfo </span><span>+=</span><span> </span><span>"Frame Interior Material: "</span><span> </span><span>+</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> frameInteriorMaterial </span><span>?</span><span> frameInteriorMaterial</span><span>.</span><span>Name</span><span> </span><span>:</span><span> </span><span>"null"</span><span>)</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    materialsInfo </span><span>+=</span><span> </span><span>"Sash: "</span><span> </span><span>+</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> sashMaterial </span><span>?</span><span> sashMaterial</span><span>.</span><span>Name</span><span> </span><span>:</span><span> </span><span>"null"</span><span>)</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>materialsInfo</span><span>);</span><span>
</span><span>}</span><span> </span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Element Material  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Material quantities  Autodesk.md ===== -->

---
created: 2026-01-28T21:03:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Material_quantities_html
author: 
---

# Help | Material quantities | Autodesk

> ## Excerpt
> There are methods to directly obtain the material volumes and areas computed by Revit for material takeoff schedules:

---
There are methods to directly obtain the material volumes and areas computed by Revit for material takeoff schedules:

-   Element.GetMaterialIds() – obtains a list of materials within an element
-   Element.GetMaterialVolume() – obtains the volume of a particular material in an element
-   Element.GetMaterialArea() – obtains the area of a particular material in an element

The methods apply to categories of elements where Category.HasMaterialQuantities property is true. In practice, this is limited to elements that use compound structure, like walls, roofs, floors, ceilings, a few other basic 3D elements like stairs, plus 3D families where materials can be assigned to geometry of the family, like windows, doors, columns, MEP equipment and fixtures, and generic model families. Note that within these categories there are further restrictions about how material quantities can be extracted. For example, curtain walls and curtain roofs will not report any material quantities themselves; the materials used by these constructs can be extracted from the individual panel elements that make up the curtain system.

Note that the volumes and areas computed by Revit may be approximate in some cases. For example, for individual layers within a wall, minor discrepancies might appear between the volumes visible in the model and those shown in the material takeoff schedule. These discrepancies tend to occur when you use the wall sweep tool to add a sweep or a reveal to a wall, or under certain join conditions.

The SDK sample “MaterialQuantities” combines both the material quantity extraction tools and temporary suppression of cutting elements (opening, windows, and doors) to extract both gross and net material quantities.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/material_quantities.png)


<!-- ===== END: Help  Material quantities  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Painting the Face of an Element  Autodesk.md ===== -->

---
created: 2026-01-28T21:04:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Painting_the_Face_of_an_Element_html
author: 
---

# Help | Painting the Face of an Element | Autodesk

> ## Excerpt
> The Paint tool functionality is available through the Revit API. Faces of elements such as walls, floors, and roofs can be painted with a material to change their appearance. It does not change the structure of the element.

---
The Paint tool functionality is available through the Revit API. Faces of elements such as walls, floors, and roofs can be painted with a material to change their appearance. It does not change the structure of the element.

The methods related to painting elements are part of the Document class. Document.Paint() applies a material to a specified face of an element. Document.RemovePaint() will remove the applied material. Additionally, the IsPainted() and GetPaintedMaterial() methods return information about the face of an element.

<table summary="" id="GUID-BE4672C9-E8BB-4157-8A2C-9067113FC55E__TABLE_655A1D7E49E047EFAAA240A9C52D9D5C"><tbody><tr><td><b>Code Region: Paint faces of a wall</b></td></tr><tr><td><pre><code><span>// Paint any unpainted faces of a given wall</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>PaintWallFaces</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> </span><span>ElementId</span><span> matId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> wall</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>GeometryElement</span><span> geometryElement </span><span>=</span><span> wall</span><span>.</span><span>get_Geometry</span><span>(</span><span>new</span><span> </span><span>Options</span><span>());</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geometryObject </span><span>in</span><span> geometryElement</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>geometryObject </span><span>is</span><span> </span><span>Solid</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Solid</span><span> solid </span><span>=</span><span> geometryObject </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> face </span><span>in</span><span> solid</span><span>.</span><span>Faces</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>doc</span><span>.</span><span>IsPainted</span><span>(</span><span>wall</span><span>.</span><span>Id</span><span>,</span><span> face</span><span>)</span><span> </span><span>==</span><span> </span><span>false</span><span>)</span><span>
                </span><span>{</span><span>
                    doc</span><span>.</span><span>Paint</span><span>(</span><span>wall</span><span>.</span><span>Id</span><span>,</span><span> face</span><span>,</span><span> matId</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Painting the Face of an Element  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Stairs and Railings  Autodesk.md ===== -->

---
created: 2026-01-28T21:04:05 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_html
author: 
---

# Help | Stairs and Railings | Autodesk

> ## Excerpt
> Classes in the Revit API in the Autodesk.Revit.DB.Architecture namespace allow access to stairs and related components such as landings and runs. Stairs can be created or modified using the Revit API. The Stairs class represents stairs created "by component". Stair elements that were created by sketch cannot be accessed as a Stair object in the API. The static method Stairs.IsByComponent() can be used to determine if an ElementId represents stairs that were created by component.

---
### Stairs

Classes in the Revit API in the Autodesk.Revit.DB.Architecture namespace allow access to stairs and related components such as landings and runs. Stairs can be created or modified using the Revit API. The Stairs class represents stairs created "by component". Stair elements that were created by sketch cannot be accessed as a Stair object in the API. The static method Stairs.IsByComponent() can be used to determine if an ElementId represents stairs that were created by component.

**Pages in this section**

-   [Creating and Editing Stairs](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Creating_and_Editing_Stairs_html)
-   [Railings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Railings_html)
-   [Stairs Annotations](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Stairs_Annotations_html)
-   [Stairs Components](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Stairs_Components_html)

**Parent page:** [Revit Geometric Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_html)


<!-- ===== END: Help  Stairs and Railings  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Creating and Editing Stairs  Autodesk.md ===== -->

---
created: 2026-01-28T21:04:10 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Creating_and_Editing_Stairs_html
author: 
---

# Help | Creating and Editing Stairs | Autodesk

> ## Excerpt
> As with other types of elements in the Revit document, a Transaction is necessary to edit stairs and stairs components. However, to create new components such as runs and landings, or to create new stairs themselves, it is necessary to use an Autodesk.Revit.DB.StairsEditScope object which maintains a stairs-editing session.

---
### StairsEditScope

As with other types of elements in the Revit document, a Transaction is necessary to edit stairs and stairs components. However, to create new components such as runs and landings, or to create new stairs themselves, it is necessary to use an Autodesk.Revit.DB.StairsEditScope object which maintains a stairs-editing session.

StairsEditScope acts like a TransactionGroup. After a StairsEditScope is started, you can start transactions and edit the stairs. Individual transactions created inside StairsEditScope will not appear in the undo menu. All transactions committed during the edit mode will be merged into a single one which will bear the name passed into the StairsEditScope constructor.

StairsEditScope has two Start methods. One takes the ElementId for an existing Stairs object for which it starts a stairs-editing session. The second Start method takes the ElementIds for base and top levels and creates a new empty stairs element with a default stairs type in the specified levels and then starts a stairs edit mode for the new stairs.

After runs and landings have been added to the Stairs and editing is complete, call StairsEditScope.Commit() to end the stairs-editing session.

### Adding Runs

The StairsRun class has three static methods for creating new runs for a Stairs object:

-   **CreateSketchedRun** - Creates a sketched run by providing a group of boundary curves and riser curves.
-   **CreateStraightRun** - Creates a straight run.
-   **CreateSpiralRun** - Creates a spiral run by providing the center, start angle and included angle.
    
    ### Adding Landings
    

Either automatic or sketched landings can be added between two runs. The static method StairsLanding.CanCreateAutomaticLanding() will check whether two stairs runs meet restriction to create automatic landing(s). The static StairsLanding.CreateAutomaticLanding() method will return the Ids of all landings created between the two stairs runs.

The static StairsLanding.CreateSketchedLanding method creates a customized landing between two runs by providing the closed boundary curves of the landing. One of the inputs to the CreateSketchedLanding method is a double value for the base elevation. The elevation has following restriction:

-   The base elevation is relative to the base elevation of the stairs.
-   The base elevation will be rounded automatically to a multiple of the riser height.
-   The base elevation should be equal to or greater than half of the riser height.
    
    ### Example
    

The following example creates a new Stairs object, two runs (one sketched, one straight) and a landing between them.

<table summary="" id="GUID-C60041FB-069E-4C89-BE67-A0593E790995__TABLE_34819D8D077E4D78BDCE1BBF877EC614"><tbody><tr><td><b>Code Region: Creating Stairs, Runs and a Landing</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>StairCreation</span><span>
</span><span>{</span><span>
    </span><span>// FailurePreprocessor class required for StairsEditScope</span><span>
    </span><span>class</span><span> </span><span>StairsFailurePreprocessor</span><span> </span><span>:</span><span> </span><span>IFailuresPreprocessor</span><span>
    </span><span>{</span><span>
        </span><span>public</span><span> </span><span>FailureProcessingResult</span><span> </span><span>PreprocessFailures</span><span>(</span><span>FailuresAccessor</span><span> failuresAccessor</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// Use default failure processing</span><span>
            </span><span>return</span><span> </span><span>FailureProcessingResult</span><span>.</span><span>Continue</span><span>;</span><span> 
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>private</span><span> </span><span>ElementId</span><span> </span><span>CreateStairs</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Level</span><span> levelBottom</span><span>,</span><span> </span><span>Level</span><span> levelTop</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>ElementId</span><span> newStairsId </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>using</span><span> </span><span>(</span><span>StairsEditScope</span><span> newStairsScope </span><span>=</span><span> </span><span>new</span><span> </span><span>StairsEditScope</span><span>(</span><span>document</span><span>,</span><span> </span><span>"New Stairs"</span><span>))</span><span>
        </span><span>{</span><span>
            newStairsId </span><span>=</span><span> newStairsScope</span><span>.</span><span>Start</span><span>(</span><span>levelBottom</span><span>.</span><span>Id</span><span>,</span><span> levelTop</span><span>.</span><span>Id</span><span>);</span><span>

            </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> stairsTrans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Add Runs and Landings to Stairs"</span><span>))</span><span>
            </span><span>{</span><span>
                stairsTrans</span><span>.</span><span>Start</span><span>();</span><span>

                </span><span>// Create a sketched run for the stairs</span><span>
                </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> bdryCurves </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>
                </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> riserCurves </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>
                </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> pathCurves </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>
                XYZ pnt1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ pnt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>15</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ pnt3 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ pnt4 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>15</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>

                </span><span>// boundaries       </span><span>
                bdryCurves</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pnt1</span><span>,</span><span> pnt2</span><span>));</span><span>
                bdryCurves</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pnt3</span><span>,</span><span> pnt4</span><span>));</span><span>

                </span><span>// riser curves</span><span>
                </span><span>const</span><span> </span><span>int</span><span> riserNum </span><span>=</span><span> </span><span>20</span><span>;</span><span>
                </span><span>for</span><span> </span><span>(</span><span>int</span><span> ii </span><span>=</span><span> </span><span>0</span><span>;</span><span> ii </span><span>&lt;=</span><span> riserNum</span><span>;</span><span> ii</span><span>++)</span><span>
                </span><span>{</span><span>
                    XYZ end0 </span><span>=</span><span> </span><span>(</span><span>pnt1 </span><span>+</span><span> pnt2</span><span>)</span><span> </span><span>*</span><span> ii </span><span>/</span><span> </span><span>(</span><span>double</span><span>)</span><span>riserNum</span><span>;</span><span>
                    XYZ end1 </span><span>=</span><span> </span><span>(</span><span>pnt3 </span><span>+</span><span> pnt4</span><span>)</span><span> </span><span>*</span><span> ii </span><span>/</span><span> </span><span>(</span><span>double</span><span>)</span><span>riserNum</span><span>;</span><span>
                    XYZ end2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>end1</span><span>.</span><span>X</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                    riserCurves</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>end0</span><span>,</span><span> end2</span><span>));</span><span>
                </span><span>}</span><span>

                </span><span>//stairs path curves</span><span>
                XYZ pathEnd0 </span><span>=</span><span> </span><span>(</span><span>pnt1 </span><span>+</span><span> pnt3</span><span>)</span><span> </span><span>/</span><span> </span><span>2.0</span><span>;</span><span>
                XYZ pathEnd1 </span><span>=</span><span> </span><span>(</span><span>pnt2 </span><span>+</span><span> pnt4</span><span>)</span><span> </span><span>/</span><span> </span><span>2.0</span><span>;</span><span>
                pathCurves</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pathEnd0</span><span>,</span><span> pathEnd1</span><span>));</span><span>

                </span><span>StairsRun</span><span> newRun1 </span><span>=</span><span> </span><span>StairsRun</span><span>.</span><span>CreateSketchedRun</span><span>(</span><span>document</span><span>,</span><span> newStairsId</span><span>,</span><span> levelBottom</span><span>.</span><span>Elevation</span><span>,</span><span> bdryCurves</span><span>,</span><span> riserCurves</span><span>,</span><span> pathCurves</span><span>);</span><span>

                </span><span>// Add a straight run</span><span>
                </span><span>Line</span><span> locationLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>20</span><span>,</span><span> </span><span>-</span><span>5</span><span>,</span><span> newRun1</span><span>.</span><span>TopElevation</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>35</span><span>,</span><span> </span><span>-</span><span>5</span><span>,</span><span> newRun1</span><span>.</span><span>TopElevation</span><span>));</span><span>
                </span><span>StairsRun</span><span> newRun2 </span><span>=</span><span> </span><span>StairsRun</span><span>.</span><span>CreateStraightRun</span><span>(</span><span>document</span><span>,</span><span> newStairsId</span><span>,</span><span> locationLine</span><span>,</span><span> </span><span>StairsRunJustification</span><span>.</span><span>Center</span><span>);</span><span>
                newRun2</span><span>.</span><span>ActualRunWidth</span><span> </span><span>=</span><span> </span><span>10</span><span>;</span><span>

                </span><span>// Add a landing between the runs</span><span>
                </span><span>CurveLoop</span><span> landingLoop </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveLoop</span><span>();</span><span>
                XYZ p1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>15</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span> 
                XYZ p2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>20</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ p3 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>20</span><span>,</span><span> </span><span>-</span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ p4 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>15</span><span>,</span><span> </span><span>-</span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                </span><span>Line</span><span> curve_1 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p1</span><span>,</span><span> p2</span><span>);</span><span>
                </span><span>Line</span><span> curve_2 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p2</span><span>,</span><span> p3</span><span>);</span><span>
                </span><span>Line</span><span> curve_3 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p3</span><span>,</span><span> p4</span><span>);</span><span>
                </span><span>Line</span><span> curve_4 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p4</span><span>,</span><span> p1</span><span>);</span><span>

                landingLoop</span><span>.</span><span>Append</span><span>(</span><span>curve_1</span><span>);</span><span>
                landingLoop</span><span>.</span><span>Append</span><span>(</span><span>curve_2</span><span>);</span><span>
                landingLoop</span><span>.</span><span>Append</span><span>(</span><span>curve_3</span><span>);</span><span>
                landingLoop</span><span>.</span><span>Append</span><span>(</span><span>curve_4</span><span>);</span><span>
                </span><span>StairsLanding</span><span> newLanding </span><span>=</span><span> </span><span>StairsLanding</span><span>.</span><span>CreateSketchedLanding</span><span>(</span><span>document</span><span>,</span><span> newStairsId</span><span>,</span><span> landingLoop</span><span>,</span><span> newRun1</span><span>.</span><span>TopElevation</span><span>);</span><span>

                stairsTrans</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
            </span><span>// A failure preprocessor is to handle possible failures during the edit mode commitment process.</span><span>
            newStairsScope</span><span>.</span><span>Commit</span><span>(</span><span>new</span><span> </span><span>StairsFailurePreprocessor</span><span>());</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> newStairsId</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The stairs resulting from the above example:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/stairs.jpg)

### Multistory Stairs

The MultistoryStairs class allows stairs to span multiple levels. A multistory stairs element may contain multiple stairs whose extents are governed by base and top levels.

This element will contain one or more Stairs elements. Stairs elements are either:

-   a reference instance which is copied to each level covered by groups of identical stairs instances which share the same level height,
-   or individual Stairs instances which are not connected to a group with the same level height.

By default, when adding new levels to the multistory stair, new stairs will be added to the group. For groups of duplicate stairs at different levels, the instances can be found as Subelements of the Stairs element.Stairs in a connected group can be edited together by modifying the associated Stairs instance. For specific floors that need special designs, stairs can be separated from the group with the Unpin method - changes made to the unpinned Stairs will not affect other any other instance in the element. The stairs can later be added back into the group with the Pin method, however any changes made to the stair will be lost since the stair's properties will be overridden by the group specifications.

<table summary="" id="GUID-C60041FB-069E-4C89-BE67-A0593E790995__TABLE_5A15394B6A7F461183B0F3F352AD4E65"><tbody><tr><td><b>Code Region: Create Multistory Stairs</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateMultiStory</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>// create new MultistoryStairs </span><span>
    </span><span>MultistoryStairs</span><span> multistoryStairs </span><span>=</span><span> </span><span>MultistoryStairs</span><span>.</span><span>Create</span><span>(</span><span>stairs</span><span>);</span><span>

    </span><span>// get all levels that can be connected to this multistoryStairs</span><span>
    </span><span>IEnumerable</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> levelIds </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>).</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Level</span><span>)).</span><span>Cast</span><span>&lt;</span><span>Level</span><span>&gt;().</span><span>Where</span><span>(</span><span>q </span><span>=&gt;</span><span> multistoryStairs</span><span>.</span><span>CanConnectLevel</span><span>(</span><span>q</span><span>.</span><span>Id</span><span>))</span><span>
    </span><span>.</span><span>Select</span><span>(</span><span>q </span><span>=&gt;</span><span> q</span><span>.</span><span>Id</span><span>);</span><span>

    </span><span>// Connect the levels to the multistoryStairs</span><span>
    </span><span>// The input to ConnectLevels is a HashSet or SortedSet, so a HashSet is created from the IEnumerable returned by FilteredElementCollector</span><span>
    multistoryStairs</span><span>.</span><span>ConnectLevels</span><span>(</span><span>new</span><span> </span><span>HashSet</span><span>&lt;</span><span>ElementId</span><span>&gt;(</span><span>levelIds</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

When new stairs are created using the StairsEditScope.Start(ElementId, ElementId) method, they have default railings associated with them. However, the Railing.Create() method can be used to create new railings with the specified railing type on all sides of a stairs element for stairs without railings. Unlike run and landing creation which require the use of StairsEditScope, railing creation cannot be performed inside an open stairs editing session.

Since railings cannot be created for Stairs that already have railings associated with them, the following example deletes the existing railings associated with a Stairs object before creating new railings.

<table summary="" id="GUID-C60041FB-069E-4C89-BE67-A0593E790995__TABLE_98420E0FE5DF4223B8A16C10216E7078"><tbody><tr><td><b>Code Region: Create Railings</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateRailing</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Create Railings"</span><span>))</span><span>
    </span><span>{</span><span>
        trans</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// Delete existing railings</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> railingIds </span><span>=</span><span> stairs</span><span>.</span><span>GetAssociatedRailings</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> railingId </span><span>in</span><span> railingIds</span><span>)</span><span>
        </span><span>{</span><span>
            document</span><span>.</span><span>Delete</span><span>(</span><span>railingId</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>// Find RailingType</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> </span><span>RailingTypeIds</span><span> </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>RailingType</span><span>)).</span><span>ToElementIds</span><span>();</span><span>
        </span><span>Railing</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> stairs</span><span>.</span><span>Id</span><span>,</span><span> </span><span>RailingTypeIds</span><span>.</span><span>First</span><span>(),</span><span> </span><span>RailingPlacementPosition</span><span>.</span><span>Treads</span><span>);</span><span>
        trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Creating and Editing Stairs  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Railings  Autodesk.md ===== -->

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


<!-- ===== END: Help  Railings  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Stairs Annotations  Autodesk.md ===== -->

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


<!-- ===== END: Help  Stairs Annotations  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Stairs Components  Autodesk.md ===== -->

---
created: 2026-01-28T21:04:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Stairs_Components_html
author: 
---

# Help | Stairs Components | Autodesk

> ## Excerpt
> The Stairs class represents a stairs element in Revit and contains properties that represent information about the treads, risers, number of stories, as well as the height of the stairs and base and top elevation. Methods of the Stairs class can be used to get the stairs landing components, stairs run components and stairs supports.

---
The Stairs class represents a stairs element in Revit and contains properties that represent information about the treads, risers, number of stories, as well as the height of the stairs and base and top elevation. Methods of the Stairs class can be used to get the stairs landing components, stairs run components and stairs supports.

The following example finds all of the Stairs that are by component and outputs some information on each of the Stairs to a Task Dialog. Note that this example uses a category filter with the BuiltInCategory.OST\_Stairs which will return ElementIds for all stairs, therefore requiring a test to see if each ElementId represents a Stairs By Component before being cast to a Stairs class when retrieved from the document.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_31B401EAF671410BB9A4BDB631C1455A"><tbody><tr><td><b>Code Region: Getting stairs information</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Stairs</span><span> </span><span>GetStairInfo</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Stairs</span><span> stairs </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> stairsIds </span><span>=</span><span> collector</span><span>.</span><span>WhereElementIsNotElementType</span><span>().</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Stairs</span><span>).</span><span>ToElementIds</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> stairId </span><span>in</span><span> stairsIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>Stairs</span><span>.</span><span>IsByComponent</span><span>(</span><span>document</span><span>,</span><span> stairId</span><span>)</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
        </span><span>{</span><span>
            stairs </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>stairId</span><span>)</span><span> </span><span>as</span><span> </span><span>Stairs</span><span>;</span><span>

            </span><span>// Format the information</span><span>
            </span><span>String</span><span> info </span><span>=</span><span> </span><span>"\nNumber of stories:  "</span><span> </span><span>+</span><span> stairs</span><span>.</span><span>NumberOfStories</span><span>;</span><span>
            info </span><span>+=</span><span> </span><span>"\nHeight of stairs:  "</span><span> </span><span>+</span><span> stairs</span><span>.</span><span>Height</span><span>;</span><span>
            info </span><span>+=</span><span> </span><span>"\nNumber of treads:  "</span><span> </span><span>+</span><span> stairs</span><span>.</span><span>ActualTreadsNumber</span><span>;</span><span>
            info </span><span>+=</span><span> </span><span>"\nTread depth:  "</span><span> </span><span>+</span><span> stairs</span><span>.</span><span>ActualTreadDepth</span><span>;</span><span>

            </span><span>// Show the information to the user.</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> stairs</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The StairsType class represents the type for a Stairs element. It contains information about the Stairs, such as the type of all runs and landings in the stairs object, types and offsets for supports on the left, right and middle of the stairs, and numerous other properties related to stair generation such as the maximum height of each riser on the stair element. The following example gets the StairsType for a Stairs element and displays some information about it in a TaskDialog.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_C972319DB4D349ADAEC16C60C3936137"><tbody><tr><td><b>Code Region: Getting StairsType Info</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetStairsType</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>StairsType</span><span> stairsType </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>stairs</span><span>.</span><span>GetTypeId</span><span>())</span><span> </span><span>as</span><span> </span><span>StairsType</span><span>;</span><span>

    </span><span>// Format stairs type info for display</span><span>
    </span><span>string</span><span> info </span><span>=</span><span> </span><span>"Stairs Type:  "</span><span> </span><span>+</span><span> stairsType</span><span>.</span><span>Name</span><span>;</span><span>
    info </span><span>+=</span><span> </span><span>"\nLeft Lateral Offset:  "</span><span> </span><span>+</span><span> stairsType</span><span>.</span><span>LeftLateralOffset</span><span>;</span><span>
    info </span><span>+=</span><span> </span><span>"\nRight Lateral Offset:  "</span><span> </span><span>+</span><span> stairsType</span><span>.</span><span>RightLateralOffset</span><span>;</span><span>
    info </span><span>+=</span><span> </span><span>"\nMax Riser Height:  "</span><span> </span><span>+</span><span> stairsType</span><span>.</span><span>MaxRiserHeight</span><span>;</span><span>
    info </span><span>+=</span><span> </span><span>"\nMin Run Width:  "</span><span> </span><span>+</span><span> stairsType</span><span>.</span><span>MinRunWidth</span><span>;</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Runs

Stairs by component are composed of runs, landings and supports. Each of these items can be retrieved from the Stairs class. A run is represented in the Revit API by the StairsRun class. The following example gets each run for a Stairs object and makes sure that it begins and ends with a riser.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_0B79D7FFCBD849BBA8A55B8F082124A1"><tbody><tr><td><b>Code Region: Working with StairsRun</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>AddStartandEndRisers</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> runIds </span><span>=</span><span> stairs</span><span>.</span><span>GetStairsRuns</span><span>();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> runId </span><span>in</span><span> runIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>StairsRun</span><span> run </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>runId</span><span>)</span><span> </span><span>as</span><span> </span><span>StairsRun</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> run</span><span>)</span><span>
        </span><span>{</span><span>
            run</span><span>.</span><span>BeginsWithRiser</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
            run</span><span>.</span><span>EndsWithRiser</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The StairsRun class provides access to run properties such as the StairsRunStyle (straight, winder, etc.), BaseElevation, TopElevation, and properties about the risers. There are also methods in the StairsRun class to access the supports hosted by the run, either all, or just those on the left or right side of the run boundaries. The GetStairsPath() method will return the curves representing the stairs path on the run, which are projected onto the base level of the stairs. The GetFootprintBoundary() method returns the run's boundary curves which are also projected onto the stairs' base level.

There are three static methods of the StairsRun class for creating new runs. These are covered in the [Creating and Editing Stairs](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Creating_and_Editing_Stairs_html) section.

The StairsRunType class represents the type of a StairsRun. It contains many properties about the treads and risers of the run as well as other information about the run. The following example gets the StairsRunType for the first run in a Stairs element and displays the riser and tread thicknesses along with the type's name.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_E1A09621684D4548A06A48C661799474"><tbody><tr><td><b>Code Region: Getting StairsRunType Info</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetRunType</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> runIds </span><span>=</span><span> stairs</span><span>.</span><span>GetStairsRuns</span><span>();</span><span>

    </span><span>ElementId</span><span> firstRunId </span><span>=</span><span> runIds</span><span>.</span><span>First</span><span>();</span><span>

    </span><span>StairsRun</span><span> firstRun </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>firstRunId</span><span>)</span><span> </span><span>as</span><span> </span><span>StairsRun</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> firstRun</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>StairsRunType</span><span> runType </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>firstRun</span><span>.</span><span>GetTypeId</span><span>())</span><span> </span><span>as</span><span> </span><span>StairsRunType</span><span>;</span><span>
        </span><span>// Format landing type info for display</span><span>
        </span><span>string</span><span> info </span><span>=</span><span> </span><span>"Stairs Run Type:  "</span><span> </span><span>+</span><span> runType</span><span>.</span><span>Name</span><span>;</span><span>
        info </span><span>+=</span><span> </span><span>"\nRiser Thickness:  "</span><span> </span><span>+</span><span> runType</span><span>.</span><span>RiserThickness</span><span>;</span><span>
        info </span><span>+=</span><span> </span><span>"\nTread Thickness:  "</span><span> </span><span>+</span><span> runType</span><span>.</span><span>TreadThickness</span><span>;</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Landings

Landings are represented by the StairsLanding class. The following example finds the thickness for each landing of a Stairs object.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_60B7CA2A99E04769B1EDC89B16D26FB6"><tbody><tr><td><b>Code Region: Working with StairsLanding</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetStairLandings</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> landingIds </span><span>=</span><span> stairs</span><span>.</span><span>GetStairsLandings</span><span>();</span><span>
    </span><span>string</span><span> info </span><span>=</span><span> </span><span>"Number of landings:  "</span><span> </span><span>+</span><span> landingIds</span><span>.</span><span>Count</span><span>;</span><span>

    </span><span>int</span><span> landingIndex </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> landingId </span><span>in</span><span> landingIds</span><span>)</span><span>
    </span><span>{</span><span>
        landingIndex</span><span>++;</span><span>
        </span><span>StairsLanding</span><span> landing </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>landingId</span><span>)</span><span> </span><span>as</span><span> </span><span>StairsLanding</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> landing</span><span>)</span><span>
        </span><span>{</span><span>
            info </span><span>+=</span><span> </span><span>"\nThickness of Landing "</span><span> </span><span>+</span><span> landingIndex </span><span>+</span><span> </span><span>":  "</span><span> </span><span>+</span><span> landing</span><span>.</span><span>Thickness</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Similar to StairsRun, StairsLanding has a GetStairsPath() method which returns the curves representing the stairs path on the landing projected onto the base level of the stairs and a GetFootprintBoundary() method which returns the landing's boundary curves, also projected onto the stairs' base level. Also similar to StairsRun, there is a method to get all of the supports hosted by the landing.

The StairsLanding class has a method to create a new landing between two runs. It is covered in the [Creating and Editing Stairs](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Creating_and_Editing_Stairs_html) section.

The StairsLandingType class represents a landing type in the Revit API. The StairsLandingType class has only a couple of properties specific to it, namely IsMonolithic which is true if the stairs landing is monolithic, and Thickness, representing the thickness of the stairs landing.

### StairsComponentConnection

Both StairsRun and StairsLanding have a GetConnections() method which provides information about connections among stairs components (run to run, or run to landing). The method returns a collection of StairsComponentConnection objects which have properties about each connection, including the connection type (to a landing, the start of a stairs run, or the end of a stairs run) and the Id of the connected stairs component.

### Supports

The Revit API does not expose a class for stairs supports. When getting the supports for Stairs, StairsRun, or a StairsLanding, the supports will be generic Revit Elements. The following example gets the names of all the supports for a Stairs object.

<table summary="" id="GUID-D5F9820D-B548-4600-8739-8029AD3B3B8B__TABLE_C3E772C35A984044B3CE88EBDE20362A"><tbody><tr><td><b>Code Region: Getting Stairs Supports</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetStairSupports</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> supportIds </span><span>=</span><span> stairs</span><span>.</span><span>GetStairsSupports</span><span>();</span><span>
    </span><span>string</span><span> info </span><span>=</span><span> </span><span>"Number of supports:  "</span><span> </span><span>+</span><span> supportIds</span><span>.</span><span>Count</span><span>;</span><span>

    </span><span>int</span><span> supportIndex </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> supportId </span><span>in</span><span> supportIds</span><span>)</span><span>
    </span><span>{</span><span>
        supportIndex</span><span>++;</span><span>
        </span><span>Element</span><span> support </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>supportId</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> support</span><span>)</span><span>
        </span><span>{</span><span>
            info </span><span>+=</span><span> </span><span>"\nName of support "</span><span> </span><span>+</span><span> supportIndex </span><span>+</span><span> </span><span>":  "</span><span> </span><span>+</span><span> support</span><span>.</span><span>Name</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Stairs Components  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Surfaces  Autodesk.md ===== -->

---
created: 2026-01-28T21:04:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Surfaces_html
author: 
---

# Help | Surfaces | Autodesk

> ## Excerpt
> The surface class represents the mathematical representation of a surface.

---
The surface class represents the mathematical representation of a surface.

The surface class is not derived from the GeometryObject class and not bounded by edges or edge loops. A bounded surface in Revit is represented by the [Face](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_html) class.

Surface is the base class for more specific surfaces:

-   Plane
-   CylindricalSurface
-   ConicalSurface
-   RuledSurface
-   RevolvedSurface
-   HermiteSurface
-   OffsetSurface - Represents a surface offset by a fixed distance in the direction of the originating surface normal. The signed offset distance is in the direction of the originating surface’s oriented normal vector at any given point, which can be the same as or opposite to the originating surface’s parametric normal vector.

These subclasses contain Create() methods and read-only properties and are suitable for constructing import geometry. See the [DirectShape](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_DirectShape_html "This element type can store arbitrary geometry obtained from import operations or calculations in either a project or family document.") topic for examples of using Surfaces in geometry creation.


<!-- ===== END: Help  Surfaces  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  DirectShape  Autodesk.md ===== -->

---
created: 2026-01-28T21:04:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_DirectShape_html
author: 
---

# Help | DirectShape | Autodesk

> ## Excerpt
> This element type can store arbitrary geometry created by the Revit API or obtained from import operations or calculations in either a project or family document.

---
This element type can store arbitrary geometry created by the Revit API or obtained from import operations or calculations in either a project or family document.

The DirectShape element and related classes support the ability to store externally created geometric shapes in a Revit document. The geometry can include closed solids or meshes. DirectShape is primarily intended for importing shapes from other data formats such as IFC or STEP where not enough information is available to create a "real" Revit element.

A DirectShape object may be assigned a top-level Model category, such as the Wall category. Sub-categories cannot be assigned to DirectShape elements. The IsValidCategoryId() method can test a category id to make sure it is a top-level built-in category approved for use with DirectShape and the Category.CategoryType enumerated value will indicated if the category type is Model. Assigning a category will affect how that object is displayed in Revit and will grant the object a collection of available parameters and some limited behaviors.

## Creation

The static CreateElement() method will create a new instance-level DirectShape. It requires the document in which the DirectShape will be added and the id of an appropriate built-in category. DirectShape provides the ApplicationId and ApplicationDataId string parameters that provide context for the source of the created shape.

Once the DirectShape is created, the shape can be set using one of the overloaded SetShape() method. The shape can be set either directly from a ShapeBuilder object or from a list of GeometryObjects. If you are using a ShapeBuilder object to construct geometry for the DirectShape anyway, there may be a slight performance advantage to using the ShapeBuilder input, as Revit will bypass repetitive validation of the input geometry. It is also possible to append additional geometry objects to the DirectShape using versions of the AppendShape() method. Note that AppendShape() will not merge or join the incoming geometry with any geometry already present, the geometry will be stored independently.

DirectShapes accept the following geometry types as input:

-   Solid (this can be a closed or open shell)
-   Mesh
-   Curve
-   Point

In addition, you can specify geometry to be used in a view-specific representation of a DirectShape. This geometry is input along with the input of a DirectShapeTargetViewType. When setting a view-specific shape representation, it will only be used in views of that type. Currently the only view-specific representation supported is for Plan views.

`DirectShapeType.SetFamilyName()` provides the ability to set a custom Family name for a DirectShapeType. The validator: `DirectShapeType.CanChangeFamilyName()` provides the ability to check if a DirectShapeType supports a custom Family name because certain categories do not support custom Family names.

The following example demonstrates how to create a simple DirectShape from a sphere created using the GeometryCreationUtilities class. Note the use of a reference Frame in creating the geometry. Prior to using it to create geometry, it is good practice to call the static method Frame.CanDefineRevitGeometry() which tests whether the supplied Frame object may be used to define a Revit curve or surface. In order to satisfy the requirements the Frame must be orthonormal and its origin is expected to lie within the Revit design limits. (When creating geometry, it also can be useful to use the static XYZ. IsWithinLengthLimits() to ensure the point is within Revit design limits.)

<table summary="" id="GUID-DF7B9D4A-5A8A-4E39-8721-B7782CBD7730__TABLE_E9824E5167E64B28B657C8145321BEE4"><tbody><tr><td><b>Code Region: Create a DirectShape</b></td></tr><tr><td><pre><code><span>// Create a DirectShape Sphere</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>CreateSphereDirectShape</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> profile </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>

    </span><span>// first create sphere with 2' radius</span><span>
    XYZ center </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
    </span><span>double</span><span> radius </span><span>=</span><span> </span><span>2.0</span><span>;</span><span>    
    XYZ profile00 </span><span>=</span><span> center</span><span>;</span><span>
    XYZ profilePlus </span><span>=</span><span> center </span><span>+</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> radius</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ profileMinus </span><span>=</span><span> center </span><span>-</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> radius</span><span>,</span><span> </span><span>0</span><span>);</span><span>

    profile</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>profilePlus</span><span>,</span><span> profileMinus</span><span>));</span><span>
    profile</span><span>.</span><span>Add</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>profileMinus</span><span>,</span><span> profilePlus</span><span>,</span><span> center </span><span>+</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>radius</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>)));</span><span>

    </span><span>CurveLoop</span><span> curveLoop </span><span>=</span><span> </span><span>CurveLoop</span><span>.</span><span>Create</span><span>(</span><span>profile</span><span>);</span><span>
    </span><span>SolidOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>SolidOptions</span><span>(</span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>,</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>);</span><span>

    </span><span>Frame</span><span> frame </span><span>=</span><span> </span><span>new</span><span> </span><span>Frame</span><span>(</span><span>center</span><span>,</span><span> XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> </span><span>-</span><span>XYZ</span><span>.</span><span>BasisZ</span><span>,</span><span> XYZ</span><span>.</span><span>BasisY</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>Frame</span><span>.</span><span>CanDefineRevitGeometry</span><span>(</span><span>frame</span><span>)</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Solid</span><span> sphere </span><span>=</span><span> </span><span>GeometryCreationUtilities</span><span>.</span><span>CreateRevolvedGeometry</span><span>(</span><span>frame</span><span>,</span><span> </span><span>new</span><span> </span><span>CurveLoop</span><span>[]</span><span> </span><span>{</span><span> curveLoop </span><span>},</span><span> </span><span>0</span><span>,</span><span> </span><span>2</span><span> </span><span>*</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>,</span><span> options</span><span>);</span><span>
        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create sphere direct shape"</span><span>))</span><span>
        </span><span>{</span><span>
            t</span><span>.</span><span>Start</span><span>();</span><span>
            </span><span>// create direct shape and assign the sphere shape</span><span>
            </span><span>DirectShape</span><span> ds </span><span>=</span><span> </span><span>DirectShape</span><span>.</span><span>CreateElement</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_GenericModel</span><span>));</span><span>

            ds</span><span>.</span><span>ApplicationId</span><span> </span><span>=</span><span> </span><span>"Application id"</span><span>;</span><span>
            ds</span><span>.</span><span>ApplicationDataId</span><span> </span><span>=</span><span> </span><span>"Geometry object id"</span><span>;</span><span>
            ds</span><span>.</span><span>SetShape</span><span>(</span><span>new</span><span> </span><span>GeometryObject</span><span>[]</span><span> </span><span>{</span><span> sphere </span><span>});</span><span>
            t</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The geometry for a DirectShape can also be created using a subclass of the ShapeBuilder class or from a TessellatedShapeBuilder.

## ShapeBuilder

ViewShapeBuilder and WireframeBuilder can be used to create geometry to store in a DirectShape class. The ViewShapeBuilder class builds and verifies a view-specific shape representation. It is limited to curve-based representations for plan views. WireframeBuilder constructs a 3D shape representation consisting of points and curves. Both types of ShapeBuilders can be applied to a DirectShape element using the DirectShape.SetShape() or DirectShape.AppendShape() overload that takes a ShapeBuilder parameter.

## TessellatedShapeBuilder

TessellatedShapeBuilder can be used create solid, shell, or polymeshes bounded by a set of connected planar facets, created by adding TessellatedFace objects one by one. Faces can only be added to the build while a face set is "open". Use the OpenConnectedFaceSet() method to open a face set. After adding all the TessellatedFaces, call CloseConnectedFaceSet() to close the face set. The builder allows for the possibility of multiple face sets - in such cases the first set should represent the outer 'surface' of a body and all following sets represent interior voids. The builder tries to create a geometry valid in Revit despite inconsistencies or omissions in the input data.

After defining all faces and closing the face set, call the Build() method to build the designated geometrical objects from the stored face sets. The Target, Fallback and GraphicsStyleId properties of the TessellatedShapeBuilder can be set prior to calling Build() or default options will be used. The results of Build() are stored in the TessellatedShapeBuilder and can be retrieved by calling GetBuildResult(). The TessellatedShapeBuilderResult.GetGeometricalObjects() method will return a list of GeometryObjects which can be used with the corresponding DirectShape.SetShape() or DirectShape.AppendShape() overload, as shown in the example below.

<table summary="" id="GUID-DF7B9D4A-5A8A-4E39-8721-B7782CBD7730__TABLE_D4E6AFECC0AB4FD0A2BB788053860ED3"><tbody><tr><td><b>Code Region: Create a DirectShape using TessellatedShapeBuilder</b></td></tr><tr><td><pre><code><span>// Create a pyramid-shaped DirectShape using given material for the faces</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>CreateTessellatedShape</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>ElementId</span><span> materialId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>List</span><span>&lt;</span><span>XYZ</span><span>&gt;</span><span> loopVertices </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>XYZ</span><span>&gt;(</span><span>4</span><span>);</span><span>

    </span><span>TessellatedShapeBuilder</span><span> builder </span><span>=</span><span> </span><span>new</span><span> </span><span>TessellatedShapeBuilder</span><span>();</span><span>

    builder</span><span>.</span><span>OpenConnectedFaceSet</span><span>(</span><span>true</span><span>);</span><span>
    </span><span>// create a pyramid with a square base 4' x 4' and 5' high</span><span>
    </span><span>double</span><span> length </span><span>=</span><span> </span><span>4.0</span><span>;</span><span>
    </span><span>double</span><span> height </span><span>=</span><span> </span><span>5.0</span><span>;</span><span>

    XYZ basePt1 </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
    XYZ basePt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>length</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ basePt3 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>length</span><span>,</span><span> length</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ basePt4 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> length</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ apex </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>length </span><span>/</span><span> </span><span>2</span><span>,</span><span> length </span><span>/</span><span> </span><span>2</span><span>,</span><span> height</span><span>);</span><span>

    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt1</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt2</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt3</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt4</span><span>);</span><span>
    builder</span><span>.</span><span>AddFace</span><span>(</span><span>new</span><span> </span><span>TessellatedFace</span><span>(</span><span>loopVertices</span><span>,</span><span> materialId</span><span>));</span><span>

    loopVertices</span><span>.</span><span>Clear</span><span>();</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt1</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>apex</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt2</span><span>);</span><span>
    builder</span><span>.</span><span>AddFace</span><span>(</span><span>new</span><span> </span><span>TessellatedFace</span><span>(</span><span>loopVertices</span><span>,</span><span> materialId</span><span>));</span><span>

    loopVertices</span><span>.</span><span>Clear</span><span>();</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt2</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>apex</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt3</span><span>);</span><span>
    builder</span><span>.</span><span>AddFace</span><span>(</span><span>new</span><span> </span><span>TessellatedFace</span><span>(</span><span>loopVertices</span><span>,</span><span> materialId</span><span>));</span><span>

    loopVertices</span><span>.</span><span>Clear</span><span>();</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt3</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>apex</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt4</span><span>);</span><span>
    builder</span><span>.</span><span>AddFace</span><span>(</span><span>new</span><span> </span><span>TessellatedFace</span><span>(</span><span>loopVertices</span><span>,</span><span> materialId</span><span>));</span><span>

    loopVertices</span><span>.</span><span>Clear</span><span>();</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt4</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>apex</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt1</span><span>);</span><span>
    builder</span><span>.</span><span>AddFace</span><span>(</span><span>new</span><span> </span><span>TessellatedFace</span><span>(</span><span>loopVertices</span><span>,</span><span> materialId</span><span>));</span><span>

    builder</span><span>.</span><span>CloseConnectedFaceSet</span><span>();</span><span>
    builder</span><span>.</span><span>Target</span><span> </span><span>=</span><span> </span><span>TessellatedShapeBuilderTarget</span><span>.</span><span>Solid</span><span>;</span><span>
    builder</span><span>.</span><span>Fallback</span><span> </span><span>=</span><span> </span><span>TessellatedShapeBuilderFallback</span><span>.</span><span>Abort</span><span>;</span><span>
    builder</span><span>.</span><span>Build</span><span>();</span><span>

    </span><span>TessellatedShapeBuilderResult</span><span> result </span><span>=</span><span> builder</span><span>.</span><span>GetBuildResult</span><span>();</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create tessellated direct shape"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>DirectShape</span><span> ds </span><span>=</span><span> </span><span>DirectShape</span><span>.</span><span>CreateElement</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_GenericModel</span><span>));</span><span>
        ds</span><span>.</span><span>ApplicationId</span><span> </span><span>=</span><span> </span><span>"Application id"</span><span>;</span><span>
        ds</span><span>.</span><span>ApplicationDataId</span><span> </span><span>=</span><span> </span><span>"Geometry object id"</span><span>;</span><span>

        ds</span><span>.</span><span>SetShape</span><span>(</span><span>result</span><span>.</span><span>GetGeometricalObjects</span><span>());</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The image below is the result of running the example above with a concrete material id specified.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/Pyramid.png)

## BRepBuilder

The BRepBuilder class offers the ability to construct Revit boundary representation geometry (solids, open shells, etc.) as a result of inputs of surfaces, edges, and boundary loops of edges. If the construction of the boundary representation is successful, the resulting geometry objects can be used directly in any other Revit tool that accepts geometry, or the BRepBuilder can be passed directly to populate a DirectShape via the SetShape() and AppendShape() methods of the DirectShape class. Below is an example of using the SetShape() method to assign a cylinder shape to a new DirectShape object.

<table summary="" id="GUID-DF7B9D4A-5A8A-4E39-8721-B7782CBD7730__TABLE_E5B535EB5616463799438793E978063A"><tbody><tr><td><b>Code Region: Create a DirectShape using BRepBuilder</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateDirectShapeFromCylinder</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Naming convention for faces and edges: we assume that x is to the left and pointing down, y is horizontal and pointing to the right, z is up</span><span>
    </span><span>BRepBuilder</span><span> brepBuilder </span><span>=</span><span> </span><span>new</span><span> </span><span>BRepBuilder</span><span>(</span><span>BRepType</span><span>.</span><span>Solid</span><span>);</span><span>

    </span><span>// The surfaces of the four faces.</span><span>
    </span><span>Frame</span><span> basis </span><span>=</span><span> </span><span>new</span><span> </span><span>Frame</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>));</span><span>
    </span><span>CylindricalSurface</span><span> cylSurf </span><span>=</span><span> </span><span>CylindricalSurface</span><span>.</span><span>Create</span><span>(</span><span>basis</span><span>,</span><span> </span><span>50</span><span>);</span><span>
    </span><span>Plane</span><span> top </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>100</span><span>));</span><span>  </span><span>// normal points outside the cylinder</span><span>
    </span><span>Plane</span><span> bottom </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span> </span><span>// normal points inside the cylinder</span><span>

    </span><span>// Add the four faces</span><span>
    </span><span>BRepBuilderGeometryId</span><span> frontCylFaceId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddFace</span><span>(</span><span>BRepBuilderSurfaceGeometry</span><span>.</span><span>Create</span><span>(</span><span>cylSurf</span><span>,</span><span> </span><span>null</span><span>),</span><span> </span><span>false</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> backCylFaceId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddFace</span><span>(</span><span>BRepBuilderSurfaceGeometry</span><span>.</span><span>Create</span><span>(</span><span>cylSurf</span><span>,</span><span> </span><span>null</span><span>),</span><span> </span><span>false</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> topFaceId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddFace</span><span>(</span><span>BRepBuilderSurfaceGeometry</span><span>.</span><span>Create</span><span>(</span><span>top</span><span>,</span><span> </span><span>null</span><span>),</span><span> </span><span>false</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> bottomFaceId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddFace</span><span>(</span><span>BRepBuilderSurfaceGeometry</span><span>.</span><span>Create</span><span>(</span><span>bottom</span><span>,</span><span> </span><span>null</span><span>),</span><span> </span><span>true</span><span>);</span><span>

    </span><span>// Geometry for the four semi-circular edges and two vertical linear edges</span><span>
    </span><span>BRepBuilderEdgeGeometry</span><span> frontEdgeBottom </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>-</span><span>50</span><span>,</span><span> </span><span>0</span><span>)));</span><span>
    </span><span>BRepBuilderEdgeGeometry</span><span> backEdgeBottom </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>-</span><span>150</span><span>,</span><span> </span><span>0</span><span>)));</span><span>

    </span><span>BRepBuilderEdgeGeometry</span><span> frontEdgeTop </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>-</span><span>50</span><span>,</span><span> </span><span>100</span><span>)));</span><span>
    </span><span>BRepBuilderEdgeGeometry</span><span> backEdgeTop </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>-</span><span>150</span><span>,</span><span> </span><span>100</span><span>)));</span><span>

    </span><span>BRepBuilderEdgeGeometry</span><span> linearEdgeFront </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>));</span><span>
    </span><span>BRepBuilderEdgeGeometry</span><span> linearEdgeBack </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>));</span><span>

    </span><span>// Add the six edges</span><span>
    </span><span>BRepBuilderGeometryId</span><span> frontEdgeBottomId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>frontEdgeBottom</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> frontEdgeTopId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>frontEdgeTop</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> linearEdgeFrontId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>linearEdgeFront</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> linearEdgeBackId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>linearEdgeBack</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> backEdgeBottomId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>backEdgeBottom</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> backEdgeTopId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>backEdgeTop</span><span>);</span><span>

    </span><span>// Loops of the four faces</span><span>
    </span><span>BRepBuilderGeometryId</span><span> loopId_Top </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddLoop</span><span>(</span><span>topFaceId</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> loopId_Bottom </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddLoop</span><span>(</span><span>bottomFaceId</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> loopId_Front </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddLoop</span><span>(</span><span>frontCylFaceId</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> loopId_Back </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddLoop</span><span>(</span><span>backCylFaceId</span><span>);</span><span>

    </span><span>// Add coedges for the loop of the front face</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Front</span><span>,</span><span> linearEdgeBackId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Front</span><span>,</span><span> frontEdgeTopId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Front</span><span>,</span><span> linearEdgeFrontId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Front</span><span>,</span><span> frontEdgeBottomId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishLoop</span><span>(</span><span>loopId_Front</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishFace</span><span>(</span><span>frontCylFaceId</span><span>);</span><span>

    </span><span>// Add coedges for the loop of the back face</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Back</span><span>,</span><span> linearEdgeBackId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Back</span><span>,</span><span> backEdgeBottomId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Back</span><span>,</span><span> linearEdgeFrontId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Back</span><span>,</span><span> backEdgeTopId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishLoop</span><span>(</span><span>loopId_Back</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishFace</span><span>(</span><span>backCylFaceId</span><span>);</span><span>

    </span><span>// Add coedges for the loop of the top face</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Top</span><span>,</span><span> backEdgeTopId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Top</span><span>,</span><span> frontEdgeTopId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishLoop</span><span>(</span><span>loopId_Top</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishFace</span><span>(</span><span>topFaceId</span><span>);</span><span>

    </span><span>// Add coedges for the loop of the bottom face</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Bottom</span><span>,</span><span> frontEdgeBottomId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Bottom</span><span>,</span><span> backEdgeBottomId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishLoop</span><span>(</span><span>loopId_Bottom</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishFace</span><span>(</span><span>bottomFaceId</span><span>);</span><span>

    brepBuilder</span><span>.</span><span>Finish</span><span>();</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> tr </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create a DirectShape"</span><span>))</span><span>
    </span><span>{</span><span>
        tr</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>DirectShape</span><span> ds </span><span>=</span><span> </span><span>DirectShape</span><span>.</span><span>CreateElement</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_GenericModel</span><span>));</span><span>
        ds</span><span>.</span><span>SetShape</span><span>(</span><span>brepBuilder</span><span>);</span><span>
        tr</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## ShapeImporter

The ShapeImporter utility class supports conversion of geometry stored in external formats (such as SAT and Rhino) into a collection of GeometryObjects which can be used to set the shape for a DirectShape. Use ShapeImporter.Convert() to generate the geometry objects (and where possible, corresponding materials and graphics styles in the associated document).

<table summary="" id="GUID-DF7B9D4A-5A8A-4E39-8721-B7782CBD7730__TABLE_D5D17D249DC2417B8E406A17C21F8D63"><tbody><tr><td><b>Code Region: Create a DirectShape from SAT file</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ReadSATFile</span><span>(</span><span>Document</span><span> revitDoc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Allow the user to select a SAT file.</span><span>
    </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Forms</span><span>.</span><span>OpenFileDialog</span><span> ofd </span><span>=</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Forms</span><span>.</span><span>OpenFileDialog</span><span>();</span><span>
    ofd</span><span>.</span><span>Filter</span><span> </span><span>=</span><span> </span><span>"SAT Files (*.sat)|*.sat"</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Forms</span><span>.</span><span>DialogResult</span><span>.</span><span>OK </span><span>==</span><span> ofd</span><span>.</span><span>ShowDialog</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>ShapeImporter</span><span> shapeImporter </span><span>=</span><span> </span><span>new</span><span> </span><span>ShapeImporter</span><span>();</span><span>
        shapeImporter</span><span>.</span><span>InputFormat</span><span> </span><span>=</span><span> </span><span>ShapeImporterSourceFormat</span><span>.</span><span>SAT</span><span>;</span><span> 
        </span><span>IList</span><span>&lt;</span><span>GeometryObject</span><span>&gt;</span><span> shapes </span><span>=</span><span> shapeImporter</span><span>.</span><span>Convert</span><span>(</span><span>revitDoc</span><span>,</span><span> ofd</span><span>.</span><span>FileName</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>shapes</span><span>.</span><span>Count</span><span> </span><span>!=</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> tr </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>revitDoc</span><span>,</span><span> </span><span>"Create a DirectShape"</span><span>))</span><span>
            </span><span>{</span><span>
                tr</span><span>.</span><span>Start</span><span>();</span><span>

                </span><span>DirectShape</span><span> dsImportedSat </span><span>=</span><span> </span><span>DirectShape</span><span>.</span><span>CreateElement</span><span>(</span><span>revitDoc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Walls</span><span>));</span><span>
                dsImportedSat</span><span>.</span><span>SetShape</span><span>(</span><span>shapes</span><span>);</span><span>

                tr</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Reference Curves, Planes, and Points

The methods:

-   DirectShape.AddReferenceCurve()
-   DirectShape.AddReferencePlane()
-   DirectShape.AddReferencePoint()
-   DirectShapeType.AddReferenceCurve()
-   DirectShapeType.AddReferencePlane()
-   DirectShapeType.AddReferencePoint()

enable the creation of reference curves, planes and points inside DirectShape elements. Explicit bounds can be provided for direct shape reference curves and planes. Revit tools that can use named references within families will also be able to select the references inside the DirectShape elements.

The overloads for these methods include an optional `DirectShapeReferenceOptions` input. Use `DirectShapeReferenceOptions.Name` to set the assigned name for the reference. If the name is specified, it is visible when picking the reference's geometry. Otherwise, the default DirectShape element name is displayed. The validator `DirectShapeReferenceOptions.IsValidReferenceName()` validates the name assigned to DirectShapeReferenceOptions.Name.

The validators:

-   DirectShape.IsValidReferenceCurve()
-   DirectShape.IsValidReferencePlaneBoundingBoxUV()
-   DirectShapeType.IsValidReferenceCurve()
-   DirectShapeType.IsValidReferencePlaneBoundingBoxUV()

validates the inputs needed for specifying a plane or curve explicit reference in the DirectShape.

## Options

The DirectShapeOptions class is used to control behavior of a DirectShape object. Use DirectShape.SetOptions() to set the options used by a DirectShape object. The GetOptions() method will return the DirectShapeOptions currently used by the DirectShape object.

DirectShape elements, by default, support element references, including dimensions, alignments, and face hosting, as well as snapping. This default behavior can be changed using the DirectShapeOptions.ReferencingOption property. If it is set to NotReferenceable, the geometry may not be used for dimensioning, snapping, alignment, or face-hosting. The element may still be selected by the user for operations which do not reference individual geometry objects.

DirectShape elements also support the ability to participate in room boundary calculations, if they are of an appropriate category for room boundary calculations, and if the associated "Room Bounding" parameter is set to true. The property DirectShapeOptions.RoomBoundingOption identifies whether the DirectShape supports an option for the "Room Bounding" parameter to permit participation in room boundary calculations. The default value is NotApplicable, but this will be changed automatically to SetByParameter for applicable DirectShapes.

## Tagging Direct Shape Geometry

References (such as dimensions) to DirectShape geometry can be maintained when the geometry changes. To do this, add geometry to the DirectShape using the `AddExternallyTaggedGeometry` method. The sample below shows how to create an instance of the `BRepBuilderPersistentIds` class and use `AddSubTag` to build a map of named `ExternalGeometryId`'s and their corresponding `BRepBuilderGeometryId`'s. When the geometry is modified, use `UpdateExternallyTaggedGeometry` and use the same names for the `ExternalGeometryId`'s that you will associate with the new geometry.

The _CreateDirectShape_ sample creates a direct shape with a face named "face1". After running this command, manually create a dimension that references this face. Then run _ModifyDirectShape_ to create a new face in the direct shape. Because the old and new faces are both named "face1", the dimension will survive the operation and reference the new face. If you change the _ModifyDirectShape_ code to give the face a different name, then the dimension will fail regeneration with the error that "One or more dimension references are or have become invalid.".

```
public DirectShape CreateDirectShape(Document doc)
{
    DirectShape ds;    
    using (Transaction tr = new Transaction(doc, "Create DirectShape"))
    {
        tr.Start();
        ds = DirectShape.CreateElement(doc, new ElementId(BuiltInCategory.OST_GenericModel));
        ds.AddExternallyTaggedGeometry(CreateTriangularFace("face1", 1));
        tr.Commit();
    }
    return ds;
}


public void ModifyDirectShape(DirectShape ds)
{
    using (Transaction tr = new Transaction(ds.Document, "Update DirectShape"))
    {
        tr.Start();
        ds.UpdateExternallyTaggedGeometry(CreateTriangularFace("face1", 10));
        tr.Commit();
    }
}

private ExternallyTaggedBRep CreateTriangularFace(string name, double x)
{
    BRepBuilder brepBuilder = new BRepBuilder(BRepType.OpenShell);

    XYZ pt0 = new XYZ(x, 0, 0);
    XYZ pt1 = new XYZ(x, 10, 0);
    XYZ pt2 = new XYZ(x, 10, 10);

    BRepBuilderGeometryId faceId = brepBuilder.AddFace(BRepBuilderSurfaceGeometry.Create(
        Plane.CreateByOriginAndBasis(pt0, XYZ.BasisZ, XYZ.BasisY), null), true);

    BRepBuilderGeometryId loopId = brepBuilder.AddLoop(faceId);
    brepBuilder.AddCoEdge(loopId, brepBuilder.AddEdge(BRepBuilderEdgeGeometry.Create(pt0, pt1)), false); 
    brepBuilder.AddCoEdge(loopId, brepBuilder.AddEdge(BRepBuilderEdgeGeometry.Create(pt1, pt2)), false); 
    brepBuilder.AddCoEdge(loopId, brepBuilder.AddEdge(BRepBuilderEdgeGeometry.Create(pt2, pt0)), false); 
    brepBuilder.FinishLoop(loopId);

    brepBuilder.FinishFace(faceId);
    brepBuilder.Finish();

    BRepBuilderPersistentIds persistentIds = new BRepBuilderPersistentIds(brepBuilder);
    persistentIds.AddSubTag(new ExternalGeometryId(name), faceId);
    ExternallyTaggedBRep result = brepBuilder.GetResult(new ExternalGeometryId("MyShape"), persistentIds);

    return result;
}
```


<!-- ===== END: Help  DirectShape  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  SubElements  Autodesk.md ===== -->

---
created: 2026-01-28T21:04:37 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_SubElements_html
author: 
---

# Help | SubElements | Autodesk

> ## Excerpt
> Several Revit elements can now contain a subdivision known as a Subelement. Subelements provide a way for parts of an element to behave as though they were real elements without incurring the overhead of adding more full elements to the model.

---
Several Revit elements can now contain a subdivision known as a Subelement. Subelements provide a way for parts of an element to behave as though they were real elements without incurring the overhead of adding more full elements to the model.

Many Revit features - for example parameters, schedules, and tags - were designed to operate on Elements. As a result, the Revit code needs to represent objects as Elements for them to participate in those features. This can lead to scalability problems, because every Element adds overhead and adding many Elements may decrease the performance of the model.

An alternative is to use Subelements. An element can expose a set of "Subelements" that it contains, specifying characteristics like their category and parameters, and certain Revit capabilities will treat those Subelements the same as ordinary Elements. For example, a Subelement may contribute geometry to the main element and may be able to be selected independently of its parent Element. It will possibly have its own (settable) type as well as an assigned category which can be different from its parent Element.

In the API, the new Subelement class is used to refer to either an Element or a specific subelement of a given Element. It is typically directly related to a Reference to either the Element or the specific subelement.


<!-- ===== END: Help  SubElements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Example Retrieve Geometry Data from a Beam  Autodesk.md ===== -->

---
created: 2026-01-28T21:02:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Example_Retrieve_Geometry_Data_from_a_Beam_html
author: 
---

# Help | Example: Retrieve Geometry Data from a Beam | Autodesk

> ## Excerpt
> This section illustrates how to get solids and curves from a beam. You can retrieve column and brace geometry data in a similar way. The GeometryElement may contain the desired geometry as a Solid or GeometryInstance depending on whether a beam is joined or standalone, and this code covers both cases.

---
This section illustrates how to get solids and curves from a beam. You can retrieve column and brace geometry data in a similar way. The GeometryElement may contain the desired geometry as a Solid or GeometryInstance depending on whether a beam is joined or standalone, and this code covers both cases.

Note: If you want to get the beam and brace driving curve, call the FamilyInstance Location property where a LocationCurve is available.

The sample code is shown as follows:

<table summary="" id="GUID-F092BCCC-77E9-4DA9-9264-10F0DB354BF5__TABLE_495DE8D32C344CB5AAF759615E6F5C68"><tbody><tr><td><b>Code Region 20-10: Getting solids and curves from a beam</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetCurvesFromABeam</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FamilyInstance</span><span> beam</span><span>,</span><span>
                                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Options</span><span> options</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geomElem </span><span>=</span><span> beam</span><span>.</span><span>get_Geometry</span><span>(</span><span>options</span><span>);</span><span>

    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>CurveArray</span><span> curves </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>
    </span><span>System</span><span>.</span><span>Collections</span><span>.</span><span>Generic</span><span>.</span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Solid</span><span>&gt;</span><span> solids </span><span>=</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>Collections</span><span>.</span><span>Generic</span><span>.</span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Solid</span><span>&gt;();</span><span> 

    </span><span>//Find all solids and insert them into solid array</span><span>
    </span><span>AddCurvesAndSolids</span><span>(</span><span>geomElem</span><span>,</span><span> </span><span>ref</span><span> curves</span><span>,</span><span> </span><span>ref</span><span> solids</span><span>);</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>void</span><span> </span><span>AddCurvesAndSolids</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geomElem</span><span>,</span><span>
                                </span><span>ref</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>CurveArray</span><span> curves</span><span>,</span><span>
                                </span><span>ref</span><span> </span><span>System</span><span>.</span><span>Collections</span><span>.</span><span>Generic</span><span>.</span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Solid</span><span>&gt;</span><span> solids</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryObject</span><span> geomObj </span><span>in</span><span> geomElem</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> curve </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> curve</span><span>)</span><span>
        </span><span>{</span><span>
            curves</span><span>.</span><span>Append</span><span>(</span><span>curve</span><span>);</span><span>
            </span><span>continue</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Solid</span><span> solid </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Solid</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> solid</span><span>)</span><span>
        </span><span>{</span><span>
            solids</span><span>.</span><span>Add</span><span>(</span><span>solid</span><span>);</span><span>
            </span><span>continue</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>//If this GeometryObject is Instance, call AddCurvesAndSolids</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span> geomInst </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> geomInst</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> transformedGeomElem
                </span><span>=</span><span> geomInst</span><span>.</span><span>GetInstanceGeometry</span><span>(</span><span>geomInst</span><span>.</span><span>Transform</span><span>);</span><span>
            </span><span>AddCurvesAndSolids</span><span>(</span><span>transformedGeomElem</span><span>,</span><span> </span><span>ref</span><span> curves</span><span>,</span><span> </span><span>ref</span><span> solids</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The above example uses the FamilyInstance.Geometry property to access the true geometry of the beam. To obtain the original geometry of a family instance before it is modified by joins, cuts, coping, extensions, or other post-processing, use the FamilyInstance.GetOriginalGeometry() method.

Note: For more information about how to retrieve the Geometry.Options type object, refer to [Geometry Helper Classes.](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Helper_Classes_html)


<!-- ===== END: Help  Example Retrieve Geometry Data from a Beam  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Example Retrieve Geometry Data from a Wall  Autodesk.md ===== -->

---
created: 2026-01-28T21:00:55 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Example_Retrieve_Geometry_Data_from_a_Wall_html
author: 
---

# Help | Example: Retrieve Geometry Data from a Wall | Autodesk

> ## Excerpt
> This walkthrough illustrates how to get geometry data from a wall. The following information is covered:

---
This walkthrough illustrates how to get geometry data from a wall. The following information is covered:

-   Getting the wall geometry edges.
-   Getting the wall geometry faces.

Note Retrieving the geometry data from Element in this example is limited because Instance is not considered. For example, sweeps included in the wall are not available in the sample code. The goal for this walkthrough is to give you a basic idea of how to retrieve geometry data but not cover all conditions. For more information about retrieving geometry data from Element, refer to [Example: Retrieve Geometry Data from a Beam](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Example_Retrieve_Geometry_Data_from_a_Beam_html).

### Create Geometry Options

In order to get the wall's geometry information, you must create a Geometry.Options object which provides detailed customized options. The code is as follows:

<table summary="" id="GUID-96A0E5EC-D9AD-42F2-901D-CC902ADD0BED__TABLE_18738B75657F43469B5FC720790D5FAE"><tbody><tr><td><b>Code Region 20-1: Creating Geometry.Options</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateOptions</span><span>(</span><span>Application</span><span> application</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Options</span><span> geomOption </span><span>=</span><span> application</span><span>.</span><span>Create</span><span>.</span><span>NewGeometryOptions</span><span>();</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> geomOption</span><span>)</span><span>
        </span><span>{</span><span>
                geomOption</span><span>.</span><span>ComputeReferences</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
                geomOption</span><span>.</span><span>DetailLevel</span><span> </span><span>=</span><span> </span><span>ViewDetailLevel</span><span>.</span><span>Fine</span><span>;</span><span>

                </span><span>// Either the DetailLevel or the View can be set, but not both</span><span>
                </span><span>//geomOption.View = commandData.Application.ActiveUIDocument.Document.ActiveView;</span><span>

                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Geometry Option created successfully."</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Retrieve Faces and Edges

Wall geometry is a solid made up of faces and edges. Complete the following steps to get the faces and edges:

1.  Retrieve a Geometry.Element instance using the Wall class Geometry property. This instance contains all geometry objects in the Object property, such as a solid, a line, and so on.
2.  Iterate the Object property to get a geometry solid instance containing all geometry faces and edges in the Faces and Edges properties.
3.  Iterate the Faces property to get all geometry faces.
4.  Iterate the Edges property to get all geometry edges.

The sample code follows:

<table summary="" id="GUID-96A0E5EC-D9AD-42F2-901D-CC902ADD0BED__TABLE_21C9DC7D16314EE58CD93BAD609215AD"><tbody><tr><td><b>Code Region 20-2: Retrieving faces and edges</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetFacesAndEdges</span><span>(</span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>String</span><span> faceInfo </span><span>=</span><span> </span><span>""</span><span>;</span><span>

        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Options</span><span> opt </span><span>=</span><span> </span><span>new</span><span> </span><span>Options</span><span>();</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geomElem </span><span>=</span><span> wall</span><span>.</span><span>get_Geometry</span><span>(</span><span>opt</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geomObj </span><span>in</span><span> geomElem</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Solid</span><span> geomSolid </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> geomSolid</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>int</span><span> faces </span><span>=</span><span> </span><span>0</span><span>;</span><span>
                        </span><span>double</span><span> totalArea </span><span>=</span><span> </span><span>0</span><span>;</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> geomFace </span><span>in</span><span> geomSolid</span><span>.</span><span>Faces</span><span>)</span><span>
                        </span><span>{</span><span>
                                faces</span><span>++;</span><span>
                                faceInfo </span><span>+=</span><span> </span><span>"Face "</span><span> </span><span>+</span><span> faces </span><span>+</span><span> </span><span>" area: "</span><span> </span><span>+</span><span> geomFace</span><span>.</span><span>Area</span><span>.</span><span>ToString</span><span>()</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
                                totalArea </span><span>+=</span><span> geomFace</span><span>.</span><span>Area</span><span>;</span><span>
                        </span><span>}</span><span>
                        faceInfo </span><span>+=</span><span> </span><span>"Number of faces: "</span><span> </span><span>+</span><span> faces </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
                        faceInfo </span><span>+=</span><span> </span><span>"Total area: "</span><span> </span><span>+</span><span> totalArea</span><span>.</span><span>ToString</span><span>()</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>Edge</span><span> geomEdge </span><span>in</span><span> geomSolid</span><span>.</span><span>Edges</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>// get wall's geometry edges</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> faceInfo</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Example Retrieve Geometry Data from a Wall  Autodesk.md ===== -->

---

