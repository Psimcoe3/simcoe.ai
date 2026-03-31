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
