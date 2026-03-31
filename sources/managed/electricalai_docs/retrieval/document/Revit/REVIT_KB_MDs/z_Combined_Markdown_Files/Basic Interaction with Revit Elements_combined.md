


<!-- ===== BEGIN: Help  Overview  Autodesk.md ===== -->

---
created: 2026-01-28T20:51:44 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_Overview_html
author: 
---

# Help | Overview | Autodesk

> ## Excerpt
> A project model can have several view types. In the API, there are three ways to classify views. The first way is by using the view element View.ViewType property. It returns an enumerated value indicating the view type. The following table lists all available view types.

---
A project model can have several view types. In the API, there are three ways to classify views. The first way is by using the view element View.ViewType property. It returns an enumerated value indicating the view type. The following table lists all available view types.

**Table 44: Autodesk.Revit.DB.ViewType**

<table summary="" id="GUID-BEB5734B-DCD8-49DF-82AB-52FE0B6D2A1B__TABLE_1FBD459E9EF84661A72B1619CEAD5D57"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td>AreaPlan</td><td>Area view.</td></tr><tr><td>CeilingPlan</td><td>Reflected ceiling plan view.</td></tr><tr><td>ColumnSchedule</td><td>Coulmn schedule view.</td></tr><tr><td>CostReport</td><td>Cost report view.</td></tr><tr><td>Detail</td><td>Detail view.</td></tr><tr><td>DraftingView</td><td>Drafting view.</td></tr><tr><td>DrawingSheet</td><td>Drawing sheet view.</td></tr><tr><td>Elevation</td><td>Elevation view.</td></tr><tr><td>EngineeringPlan</td><td>Engineering view.</td></tr><tr><td>FloorPlan</td><td>Floor plan view.</td></tr><tr><td>Internal</td><td>Revit's internal view.</td></tr><tr><td>Legend</td><td>Legend view.</td></tr><tr><td>LoadsReport</td><td>Loads report view.</td></tr><tr><td>PanelSchedule</td><td>Panel schedule view.</td></tr><tr><td>PressureLossReport</td><td>Pressure Loss Report view.</td></tr><tr><td>Rendering</td><td>Rendering view.</td></tr><tr><td>Report</td><td>Report view.</td></tr><tr><td>Schedule</td><td>Schedule view.</td></tr><tr><td>Section</td><td>Cross section view.</td></tr><tr><td>ThreeD</td><td>3-D view.</td></tr><tr><td>Undefined</td><td>Undefined/unspecified view.</td></tr><tr><td>Walkthrough</td><td>Walkthrough view.</td></tr></tbody></table>

The second way to classify views is by the class type.

The following table lists the view types and the corresponding views in the Project browser.

**Table 45: Project Browser Views**

<table summary="" id="GUID-BEB5734B-DCD8-49DF-82AB-52FE0B6D2A1B__TABLE_3AAE197041EB47DC8E535B652D3994A0"><tbody><tr><td><b>Project Browser Views</b></td><td><b>View Type</b></td><td><b>Class Type</b></td></tr><tr><td>Area Plans</td><td>ViewType.AreaPlan</td><td>Elements.ViewPlan</td></tr><tr><td>Ceiling Plans</td><td>ViewType.CeilingPlan</td><td>Elements.ViewPlan</td></tr><tr><td>Graphic Column Schedule</td><td>ViewType.ColumnSchedule</td><td>Elements.View</td></tr><tr><td>Detail Views</td><td>ViewType.Detail</td><td>Elements.ViewSection</td></tr><tr><td>Drafting Views</td><td>ViewType.DraftingView</td><td>Elements.ViewDrafting</td></tr><tr><td>Sheets</td><td>ViewType.DrawingSheet</td><td>Elements.ViewSheet</td></tr><tr><td>Elevations</td><td>ViewType.Elevation</td><td>Elements.ViewSection</td></tr><tr><td>Structural Plans</td><td>ViewType.EngineeringPlan</td><td>Elements.ViewPlan</td></tr><tr><td>Floor Plans</td><td>ViewType.FloorPlan</td><td>Elements.ViewPlan</td></tr><tr><td>Legends</td><td>ViewType.Legend</td><td>Elements.View</td></tr><tr><td>Reports (MEP engineering)</td><td>ViewType.LoadsReport</td><td>Elements.View</td></tr><tr><td>Reports (MEP engineering)</td><td>ViewType.PanelSchedule</td><td>Elements.PanelScheduleView</td></tr><tr><td>Reports (MEP engineering)</td><td>ViewType.PresureLossReport</td><td>Elements.View</td></tr><tr><td>Renderings</td><td>ViewType.Rendering</td><td>Elements.ViewDrafting</td></tr><tr><td>Reports</td><td>ViewType.Report</td><td>Elements.View</td></tr><tr><td>Schedules/Quantities</td><td>ViewType.Schedule</td><td>Elements.ViewSchedule</td></tr><tr><td>Sections</td><td>ViewType.Section</td><td>Elements.ViewSection</td></tr><tr><td>3D Views</td><td>ViewType.ThreeD</td><td>Elements.View3D</td></tr><tr><td>Walkthroughs</td><td>ViewType.Walkthrough</td><td>Elements.View3D</td></tr></tbody></table>

This example shows how to use the ViewType property of a view to determine the view's type.

<table summary="" id="GUID-BEB5734B-DCD8-49DF-82AB-52FE0B6D2A1B__TABLE_58190796F5074FEF9F19F6EBBA0338CB"><tbody><tr><td><b>Code Region: Determining the View type</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetViewType</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Get the view type of the given view, and format the prompt string</span><span>
        </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"The view is "</span><span>;</span><span>

        </span><span>switch</span><span> </span><span>(</span><span>view</span><span>.</span><span>ViewType</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>case</span><span> </span><span>ViewType</span><span>.</span><span>AreaPlan</span><span>:</span><span>
                        prompt </span><span>+=</span><span> </span><span>"an area view."</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>ViewType</span><span>.</span><span>CeilingPlan</span><span>:</span><span>
                        prompt </span><span>+=</span><span> </span><span>"a reflected ceiling plan view."</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>ViewType</span><span>.</span><span>ColumnSchedule</span><span>:</span><span>
                        prompt </span><span>+=</span><span> </span><span>"a column schedule view."</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>ViewType</span><span>.</span><span>CostReport</span><span>:</span><span>
                        prompt </span><span>+=</span><span> </span><span>"a cost report view."</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>ViewType</span><span>.</span><span>Detail</span><span>:</span><span>
                        prompt </span><span>+=</span><span> </span><span>"a detail view."</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>ViewType</span><span>.</span><span>DraftingView</span><span>:</span><span>
                        prompt </span><span>+=</span><span> </span><span>"a drafting view."</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>ViewType</span><span>.</span><span>DrawingSheet</span><span>:</span><span>
                        prompt </span><span>+=</span><span> </span><span>"a drawing sheet view."</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>ViewType</span><span>.</span><span>Elevation</span><span>:</span><span>
                        prompt </span><span>+=</span><span> </span><span>"an elevation view."</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>ViewType</span><span>.</span><span>EngineeringPlan</span><span>:</span><span>
                        prompt </span><span>+=</span><span> </span><span>"an engineering view."</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>case</span><span> </span><span>ViewType</span><span>.</span><span>FloorPlan</span><span>:</span><span>
                        prompt </span><span>+=</span><span> </span><span>"a floor plan view."</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>// ...</span><span>
                </span><span>default</span><span>:</span><span>
                        </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>// Give the user some information</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The third way to classify views is using the ViewFamilyType class. Most view creation methods required the Id of a ViewFamilyType for the new view. The Id of the ViewFamilyType can be retrieved from the View.GetTypeId() method. The ViewFamilyType.ViewFamily property returns a ViewFamily enumeration which specifies the family of the ViewFamilyType and similar to the ViewType enum documented above. The following example shows how to get the ViewFamily from a View.

<table summary="" id="GUID-BEB5734B-DCD8-49DF-82AB-52FE0B6D2A1B__TABLE_F86D32A5612542B3B4B0CA25EC9FBFCD"><tbody><tr><td><b>Code Region: Determining view type from ViewFamilyType</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>ViewFamily</span><span> </span><span>GetViewFamily</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ViewFamily</span><span> viewFamily </span><span>=</span><span> </span><span>ViewFamily</span><span>.</span><span>Invalid</span><span>;</span><span>

    </span><span>ElementId</span><span> viewTypeId </span><span>=</span><span> view</span><span>.</span><span>GetTypeId</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>viewTypeId</span><span>.</span><span>IntegerValue</span><span> </span><span>&gt;</span><span> </span><span>1</span><span>)</span><span> </span><span>// some views may not have a ViewFamilyType</span><span>
    </span><span>{</span><span>
        </span><span>ViewFamilyType</span><span> viewFamilyType </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>viewTypeId</span><span>)</span><span> </span><span>as</span><span> </span><span>ViewFamilyType</span><span>;</span><span>
        viewFamily </span><span>=</span><span> viewFamilyType</span><span>.</span><span>ViewFamily</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> viewFamily</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Overview  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Filtering  Autodesk.md ===== -->

---
created: 2026-01-28T20:47:57 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_html
author: 
---

# Help | Filtering | Autodesk

> ## Excerpt
> The Revit API provides a mechanism for filtering and iterating elements in a Revit document. This is the best way to get a set of related elements, such as all walls or doors in the document. Filters can also be used to find a very specific set of elements, such as all beams of a specific size.

---
The Revit API provides a mechanism for filtering and iterating elements in a Revit document. This is the best way to get a set of related elements, such as all walls or doors in the document. Filters can also be used to find a very specific set of elements, such as all beams of a specific size.

The basic steps to get elements passing a specified filter are as follows:

1.  Create a new FilteredElementCollector
2.  Apply one or more filters to it
3.  Get filtered elements or element ids (using one of several methods)

The following sample covers the basic steps to filtering and iterating elements in the document.

<table summary="" id="GUID-85E4A43E-88B5-43C6-908C-2D138C9F611D__TABLE_9B881B8A742C4C1885A86B5BE0CEFA42"><tbody><tr><td><b>Code Region 6-1: Use element filtering to get all wall instances in document</b></td></tr><tr><td><pre><code><span>// Find all Wall instances in the document by using category filter</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>GetAllWalls</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ElementCategoryFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementCategoryFilter</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Walls</span><span>);</span><span>

    </span><span>// Apply the filter to the elements in the active document</span><span>
    </span><span>// Use shortcut WhereElementIsNotElementType() to find wall instances only</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> walls </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>WhereElementIsNotElementType</span><span>().</span><span>ToElements</span><span>();</span><span>
    </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"The walls in the current document are:\n"</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> walls</span><span>)</span><span>
    </span><span>{</span><span>
            prompt </span><span>+=</span><span> e</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Filtering  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Create a FilteredElementCollector  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Create_a_FilteredElementCollector_html
author: 
---

# Help | Create a FilteredElementCollector | Autodesk

> ## Excerpt
> The main class used for element iteration and filtering is called FilteredElementCollector. It is constructed in one of three ways:

---
The main class used for element iteration and filtering is called FilteredElementCollector. It is constructed in one of three ways:

1.  From a document - will search and filter the set of elements in a document
2.  From a document and set of ElementIds - will search and filter a specified set of elements
3.  From a document and a view - will search and filter the visible elements in a view

Note: Always check that a view is valid for element iteration when filtering elements in a specified view by using the static FilteredElementCollector.IsViewValidForElementIteration().

When the object is first created, there are no filters applied. This class requires that at least one condition be set before making at attempt to access the elements, otherwise an exception will be thrown.


<!-- ===== END: Help  Create a FilteredElementCollector  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Applying Filters  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Applying_Filters_html
author: 
---

# Help | Applying Filters | Autodesk

> ## Excerpt
> Filters can be applied to a FilteredElementCollector using ElementFilters. An ElementFilter is a class that examines an element to see if it meets a certain criteria. The ElementFilter base class has three derived classes that divide element filters into three categories.

---
Filters can be applied to a FilteredElementCollector using ElementFilters. An ElementFilter is a class that examines an element to see if it meets a certain criteria. The ElementFilter base class has three derived classes that divide element filters into three categories.

-   _**ElementQuickFilter**_ - Quick filters operate only on the ElementRecord, a low-memory class which has a limited interface to read element properties. Elements which are rejected by a quick filter will not be expanded in memory.
-   _**ElementSlowFilter**_ - Slow filters require that the Element be obtained and expanded in memory first. Thus it is preferable to couple slow filters with at least one ElementQuickFilter, which should minimize the number of Elements that are expanded in order to evaluate against the criteria set by this filter.
-   _**ElementLogicalFilter**_ - Logical filters combine two or more filters logically. The component filters may be reordered by Revit to cause the quickest acting filters to be evaluated first.

Most filters may be inverted using an overload constructor that takes a Boolean argument indicating to invert the filter so that elements that would normally be accepted by the filter will be rejected, and elements that would normally be rejected will be accepted. Filters that cannot be inverted are noted in their corresponding sections below.

There is a set of predefined filters available for common uses. Many of these built-in filters provide the basis for the FilteredElementCollector shortcut methods mentioned in the FilteredElementCollector section above. The next three sections provide more information on the built-in filters.

Once a filter is created, it needs to be applied to the FilteredElementCollector. The generic method WherePasses() is used to apply a single ElementFilter to the FilteredElementCollector.

Filters can also be applied using a number of shortcut methods provided by FilteredElementCollector. Some apply a specific filter without further input, such as WhereElementIsCurveDriven(), while others apply a specific filter with a simple piece of input, such as the OfCategory() method which takes a BuiltInCategory as a parameter. And lastly there are methods such as UnionWith() that join filters together. All of these methods return the same collector allowing filters to be easily chained together.

### Quick filters

Quick filters operate only on the ElementRecord, a low-memory class which has a limited interface to read element properties. Elements which are rejected by a quick filter will not be expanded in memory. The following table summarizes the built-in quick filters, and some examples follow for a few of the filters.

**Table 13: Built-in Quick Filters**

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_699DFD12B41C4EB9A0136ABFC83E1321"><tbody><tr><td><b>Built-in Filter</b></td><td><b>What it passes</b></td><td><b>Shortcut Method(s)</b></td></tr><tr><td>BoundingBoxContainsPointFilter</td><td>Elements which have a bounding box that contains a given point</td><td>None</td></tr><tr><td>BoundingBoxIntersectsFilter</td><td>Elements which have a bounding box which intersects a given outline</td><td>None</td></tr><tr><td>BoundingBoxIsInsideFilter</td><td>Elements which have a bounding box inside a given outline</td><td>None</td></tr><tr><td>ElementCategoryFilter</td><td>Elements matching the input category id</td><td>OfCategoryId()</td></tr><tr><td>ElementClassFilter</td><td>Elements matching the input runtime class (or derived classes)</td><td>OfClass()</td></tr><tr><td>ElementDesignOptionFilter</td><td>Elements in a particular design option</td><td>ContainedInDesignOption()</td></tr><tr><td>ElementIdSetFilter</td><td>Elements whose ElementIds are included in a collection</td></tr><tr><td>ElementIsCurveDrivenFilter</td><td>Elements which are curve driven</td><td>WhereElementIsCurveDriven()</td></tr><tr><td>ElementIsElementTypeFilter</td><td>Elements which are "Element types"</td><td>WhereElementIsElementType() WhereElementIsNotElementType()</td></tr><tr><td>ElementMulticategoryFilter</td><td>Elements matching any of a given set of categories</td><td>None</td></tr><tr><td>ElementMulticlassFilter</td><td>Elements matching a given set of classes (or derived classes)</td><td>None</td></tr><tr><td>ElementOwnerViewFilter</td><td>Elements which are view-specific</td><td>OwnedByView() WhereElementIsViewIndependent()</td></tr><tr><td>ElementStructuralTypeFilter</td><td>Elements matching a given structural type</td><td>None</td></tr><tr><td>ExclusionFilter</td><td>All elements except the element ids input to the filter</td><td>Excluding()</td></tr><tr><td>FamilySymbolFilter</td><td>Symbols of a particular family</td><td></td></tr><tr><td>VisibleInViewFilter</td><td>Elements that are most likely visible in the given view</td><td></td></tr></tbody></table>

Note: The FamilySymbolFilter cannot be inverted.

Note: The bounding box filters exclude all objects derived from View and objects derived from ElementType.

The following example creates an outline in the document and then uses a BoundingBoxIntersectsFilter to find the elements in the document with a bounding box that intersects that outline. It then shows how to use an inverted filter to find all walls whose bounding box do not intersect the given outline. Note that the use of the OfClass() method applies an ElementClassFilter to the collection as well.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_186443DF4DA745609A975C68D0E5FD0B"><tbody><tr><td><b>Code Region 6-2: BoundingBoxIntersectsFilter example</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>IntersectsFilterSample</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use BoundingBoxIntersects filter to find elements with a bounding box that intersects the given Outline in the document.</span><span>

        </span><span>// Create a Outline, uses a minimum and maximum XYZ point to initialize the outline. </span><span>
        </span><span>Outline</span><span> myOutLn </span><span>=</span><span> </span><span>new</span><span> </span><span>Outline</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>100</span><span>));</span><span>

        </span><span>// Create a BoundingBoxIntersects filter with this Outline</span><span>
        </span><span>BoundingBoxIntersectsFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>BoundingBoxIntersectsFilter</span><span>(</span><span>myOutLn</span><span>);</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>// This filter excludes all objects derived from View and objects derived from ElementType</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> elements </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>ToElements</span><span>();</span><span>

        </span><span>// Find all walls which don't intersect with BoundingBox: use an inverted filter to match elements</span><span>
        </span><span>// Use shortcut command OfClass() to find walls only</span><span>
        </span><span>BoundingBoxIntersectsFilter</span><span> invertFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>BoundingBoxIntersectsFilter</span><span>(</span><span>myOutLn</span><span>,</span><span> </span><span>true</span><span>);</span><span>
        collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> notIntersectWalls </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Wall</span><span>)).</span><span>WherePasses</span><span>(</span><span>invertFilter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The next example uses an exclusion filter to find all walls that are not currently selected in the document.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_02814077FD664BF89F63FFB6803DF358"><tbody><tr><td><b>Code Region 6-3: Creating an exclusion filter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FindNotSelectedWalls</span><span>(</span><span>UIDocument</span><span> uiDocument</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Find all walls that are not currently selected, </span><span>
        </span><span>// Get all element ids which are current selected by users, exclude these ids when filtering</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uiDocument</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

        </span><span>// Use the selection to instantiate an exclusion filter</span><span>
        </span><span>ExclusionFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ExclusionFilter</span><span>(</span><span>selectedIds</span><span>);</span><span>
        </span><span>// For the sake of simplicity we do not test here whether the selection is empty or not,</span><span>
        </span><span>// but in production code a proper validation would have to be done to avoid an argument</span><span>
        </span><span>// exception from the filter's consructor.</span><span>

        </span><span>// Apply the filter to the elements in the active document,</span><span>
        </span><span>// Use shortcut method OfClass() to find Walls only</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>uiDocument</span><span>.</span><span>Document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> walls </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Wall</span><span>)).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: The ElementClassFilter will match elements whose class is an exact match to the input class, or elements whose class is derived from the input class. The following example uses an ElementClassFilter to get all loads in the document.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_EACB2C1A610A4E4CB771DD4758CC68ED"><tbody><tr><td><b>Code Region 6-4: Using an ElementClassFilter to get loads</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MakeLoadFilter</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use ElementClassFilter to find all loads in the document</span><span>
        </span><span>// Using typeof(LoadBase) will yield all AreaLoad, LineLoad and PointLoad</span><span>
        </span><span>ElementClassFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>LoadBase</span><span>));</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> allLoads </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

There is a small subset of Element subclasses in the API which are not supported by the element class filter. These types exist in the API, but not in Revit's native object model, which means that this filter doesn't support them. In order to use a class filter to find elements of these types, it is necessary to use a higher level class and then process the results further to find elements matching only the subtype.

Note: Dedicated filters exist for some of these types.

The following types are affected by this restriction:

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_B749B356451E43F892FA804E108867EB"><tbody><tr><td><b>Type</b></td><td><b>Dedicated Filter</b></td></tr><tr><td>Subclasses of Autodesk.Revit.DB.Material</td><td>None</td></tr><tr><td>Subclasses of Autodesk.Revit.DB.CurveElement</td><td>CurveElementFilter</td></tr><tr><td>Subclasses of Autodesk.Revit.DB.ConnectorElement</td><td>None</td></tr><tr><td>Subclasses of Autodesk.Revit.DB.HostedSweep</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Architecture.Room</td><td>RoomFilter</td></tr><tr><td>Autodesk.Revit.DB.Mechanical.Space</td><td>SpaceFilter</td></tr><tr><td>Autodesk.Revit.DB.Area</td><td>AreaFilter</td></tr><tr><td>Autodesk.Revit.DB.Architecture.RoomTag</td><td>RoomTagFilter</td></tr><tr><td>Autodesk.Revit.DB.Mechanical.SpaceTag</td><td>SpaceTagFilter</td></tr><tr><td>Autodesk.Revit.DB.AreaTag</td><td>AreaTagFilter</td></tr><tr><td>Autodesk.Revit.DB.CombinableElement</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Mullion</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Panel</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.AnnotationSymbol</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Structure.AreaReinforcementType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Structure.PathReinforcementType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.AnnotationSymbolType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Architecture.RoomTagType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Mechanical.SpaceTagType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.AreaTagType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Structure.TrussType</td><td>None</td></tr></tbody></table>

### Slow Filters

Slow filters require that the Element be obtained and expanded in memory first. Thus it is preferable to couple slow filters with at least one ElementQuickFilter, which should minimize the number of Elements that are expanded in order to evaluate against the criteria set by this filter. The following table summarizes the built-in slow filters, while a few examples follow to provide an in-depth look at some of the filters.

**Table 14: Built-in Slow Filters**

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_89C43C4C3BBF4001A3430D2B3088713F"><tbody><tr><td><b>Built-in Filter</b></td><td><b>What it passes</b></td><td><b>Shortcut Method(s)</b></td></tr><tr><td>AreaFilter</td><td>Areas</td><td>None</td></tr><tr><td>AreaTagFilter</td><td>Area tags</td><td>None</td></tr><tr><td>CurveElementFilter</td><td>CurveElements</td><td>None</td></tr><tr><td>ElementLevelFilter</td><td>Elements associated with a given level id</td><td>None</td></tr><tr><td>ElementParameterFilter</td><td>Elements passing one or more parameter filter rules</td><td>None</td></tr><tr><td>ElementPhaseStatusFilter</td><td>Elements with a given phase status on a given phase</td><td>None</td></tr><tr><td>FamilyInstanceFilter</td><td>Instances of a particular family instance</td><td>None</td></tr><tr><td>FamilyStructuralMaterialTypeFilter</td><td>Family elements of given structural material type</td><td>None</td></tr><tr><td>PrimaryDesignOptionMemberFilter</td><td>Elements owned by any primary design option</td><td>None</td></tr><tr><td>RoomFilter</td><td>Rooms</td><td>None</td></tr><tr><td>RoomTagFilter</td><td>Room tags</td><td>None</td></tr><tr><td>SpaceFilter</td><td>Spaces</td><td>None</td></tr><tr><td>SpaceTagFilter</td><td>Space tags</td><td>None</td></tr><tr><td>StructuralInstanceUsageFilter</td><td>FamilyInstances of given structural usage</td><td>None</td></tr><tr><td>StructuralMaterialTypeFilter</td><td>FamilyInstances of given structural material type</td><td>None</td></tr><tr><td>StructuralWallUsageFilter</td><td>Walls of given structural wall usage</td><td>None</td></tr><tr><td><a href="https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Element_Intersection_Filters_html" data-url="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/files/Revit_API_Developers_Guide/Basic_Interaction_with_Revit_Elements/Filtering/Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Element_Intersection_Filters_html.html">Element Intersection Filters</a></td><td>Elements that intersect the solid geometry of a given element</td><td>None</td></tr><tr><td><a href="https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Element_Intersection_Filters_html" data-url="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/files/Revit_API_Developers_Guide/Basic_Interaction_with_Revit_Elements/Filtering/Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Element_Intersection_Filters_html.html">Element Intersection Filters&gt;</a></td><td>Elements that intersect the given solid geometry</td><td>None</td></tr></tbody></table>

The following slow filters cannot be inverted:

-   RoomFilter
-   RoomTagFilter
-   AreaFilter
-   AreaTagFilter
-   SpaceFilter
-   SpaceTagFilter
-   FamilyInstanceFilter

As mentioned in the quick filters section, some classes do not work with the ElementClassFilter. Some of those classes, such as Room and RoomTag have their own dedicated filters.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_4AB07B2CE0294AE3ACFEAD5378B7CBAF"><tbody><tr><td><b>Code Region 6-5: Using the Room filter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MakeRoomFilter</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use a RoomFilter to find all room elements in the document. It is necessary to use the RoomFilter and not an ElementClassFilter or the shortcut method OfClass() because the Room class is not supported by those methods.</span><span>
        </span><span>RoomFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>RoomFilter</span><span>();</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> rooms </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The ElementParameterFilter is a powerful filter that can find elements based on values of parameters they may have. It can find elements whose parameter values match a specific value or are greater or less than some value. ElementParameterFilter can also be used to find elements that support a specific shared parameter.

The example below uses an ElementParameterFilter to find rooms whose size is more than 100 square feet and rooms with less than 100 square feet.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_3905C77CB625485CAD0429E99FCE13CA"><tbody><tr><td><b>Code Region 6-6: Using a parameter filter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FindRooms</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Creates an ElementParameter filter to find rooms whose area is greater than specified value</span><span>
        </span><span>// Create filter by provider and evaluator </span><span>
        </span><span>BuiltInParameter</span><span> areaParam </span><span>=</span><span> </span><span>BuiltInParameter</span><span>.</span><span>ROOM_AREA</span><span>;</span><span>
        </span><span>// provider</span><span>
        </span><span>ParameterValueProvider</span><span> pvp </span><span>=</span><span> </span><span>new</span><span> </span><span>ParameterValueProvider</span><span>(</span><span>new</span><span> </span><span>ElementId</span><span>((</span><span>int</span><span>)</span><span>areaParam</span><span>));</span><span>
        </span><span>// evaluator</span><span>
        </span><span>FilterNumericRuleEvaluator</span><span> fnrv </span><span>=</span><span> </span><span>new</span><span> </span><span>FilterNumericGreater</span><span>();</span><span>
        </span><span>// rule value </span><span>
        </span><span>double</span><span> ruleValue </span><span>=</span><span> </span><span>100.0f</span><span>;</span><span>      </span><span>// filter room whose area is greater than 100 SF</span><span>
        </span><span>// rule</span><span>
        </span><span>FilterRule</span><span> fRule </span><span>=</span><span> </span><span>new</span><span> </span><span>FilterDoubleRule</span><span>(</span><span>pvp</span><span>,</span><span> fnrv</span><span>,</span><span> ruleValue</span><span>,</span><span> </span><span>1E-6</span><span>);</span><span>

        </span><span>// Create an ElementParameter filter</span><span>
        </span><span>ElementParameterFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>fRule</span><span>);</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> rooms </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>ToElements</span><span>();</span><span>

        </span><span>// Find rooms whose area is less than or equal to 100: </span><span>
        </span><span>// Use inverted filter to match elements</span><span>
        </span><span>ElementParameterFilter</span><span> lessOrEqualFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>fRule</span><span>,</span><span> </span><span>true</span><span>);</span><span> 
        collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> lessOrEqualFounds </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>lessOrEqualFilter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following example shows how to use the FamilyStructuralMaterialTypeFilter to find all families whose material type is wood. It also shows how to use an inverted filter to find all families whose material type is not wood.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_3DD5DAFCBBD842A6BF7F33B4BB528F98"><tbody><tr><td><b>Code Region 6-7: Find all families with wood material</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FindWoodFamilies</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use FamilyStructuralMaterialType filter to find families whose material type is Wood</span><span>
        </span><span>FamilyStructuralMaterialTypeFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>FamilyStructuralMaterialTypeFilter</span><span>(</span><span>StructuralMaterialType</span><span>.</span><span>Wood</span><span>);</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> woodFamiles </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>ToElements</span><span>();</span><span>

        </span><span>// Find families are not Wood: Use inverted filter to match families</span><span>
        </span><span>FamilyStructuralMaterialTypeFilter</span><span> notWoodFilter </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>FamilyStructuralMaterialTypeFilter</span><span>(</span><span>StructuralMaterialType</span><span>.</span><span>Wood</span><span>,</span><span> </span><span>true</span><span>);</span><span>
        collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> notWoodFamilies </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>notWoodFilter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The last two slow filters derive from ElementIntersectsFilter which is a base class for filters used to match elements which intersect with geometry. See Code Region: Find Nearby Walls in the section [Geometry Utility Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Utility_Classes_html)for an example of the use of this type of filter.

### Logical filters

Logical filters combine two or more filters logically. The following table summarizes the built-in logical filters.

**Table 15: Built-in Logical Filters**

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_C27A6B50681A4003AD2212073993E958"><tbody><tr><td><b>Built-in Filter</b></td><td><b>What it passes</b></td><td><b>Shortcut Method(s)</b></td></tr><tr><td>LogicalAndFilter</td><td>Elements that pass 2 or more filters</td><td>WherePasses()- adds one additional filter<p>IntersectWith() - joins two sets of independent filters</p></td></tr><tr><td>LogicalOrFilter</td><td>Elements that pass at least one of 2 or more filters</td><td>UnionWith() - joins two sets of independent filters</td></tr></tbody></table>

In the example below, two quick filters are combined using a logical filter to get all door FamilyInstance elements in the document.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_D3B3A22C953B4E5DA02D0B7956E0C715"><tbody><tr><td><b>Code Region 6-8: Using LogicalAndFilter to find all door instances</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FindDoors</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Find all door instances in the project by finding all elements that both belong to the door category and are family instances.</span><span>
</span><span>ElementClassFilter</span><span> familyInstanceFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>FamilyInstance</span><span>));</span><span>

</span><span>// Create a category filter for Doors</span><span>
</span><span>ElementCategoryFilter</span><span> doorsCategoryfilter </span><span>=</span><span> 
        </span><span>new</span><span> </span><span>ElementCategoryFilter</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Doors</span><span>);</span><span>

</span><span>// Create a logic And filter for all Door FamilyInstances</span><span>
</span><span>LogicalAndFilter</span><span> doorInstancesFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>LogicalAndFilter</span><span>(</span><span>familyInstanceFilter</span><span>,</span><span> 
        doorsCategoryfilter</span><span>);</span><span>

</span><span>// Apply the filter to the elements in the active document</span><span>
</span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
</span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> doors </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>doorInstancesFilter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Applying Filters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Getting filtered elements or element ids  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Getting_filtered_elements_or_element_ids_html
author: 
---

# Help | Getting filtered elements or element ids | Autodesk

> ## Excerpt
> Once one or more filters have been applied to the FilteredElementCollector, the filtered set of elements can be retrieved in one of three ways:

---
Once one or more filters have been applied to the FilteredElementCollector, the filtered set of elements can be retrieved in one of three ways:

1.  Obtain a collection of Elements or ElementIds.
    -   ToElements() - returns all elements that pass all applied filters
    -   ToElementIds() - returns ElementIds of all elements which pass all applied filters
2.  Obtain the first Element or ElementId that matches the filter.
    -   FirstElement() - returns first element to pass all applied filters
    -   FirstElementId() - returns id of first element to pass all applied filters
3.  Obtain an ElementId or Element iterator.
    -   GetElementIdIterator() - returns FilteredElementIdIterator to the element ids passing the filters
    -   GetElementIterator() - returns FilteredElementIterator to the elements passing the filters
    -   GetEnumerator() - returns an `IEnumerator<Element>` that iterates through collection of passing elements

You should only use one of the methods from these groups at a time; the collector will reset if you call another method to extract elements. Thus, if you have previously obtained an iterator, it will be stopped and traverse no more elements if you call another method to extract elements.

Which method is best depends on the application. If just one matching element is required, FirstElement() or FirstElementId() is the best choice. If all the matching elements are required, use ToElements(). If a variable number are needed, use an iterator.

If the application will be deleting elements or making significant changes to elements in the filtered list, ToElementIds() or an element id iterator are the best options. This is because deleting elements or making significant changes to an element can invalidate an element handle. With element ids, the call to Document.GetElement() with the ElementId will always return a valid Element (or a null reference if the element has been deleted).

Using the ToElements() method to get the filter results as a collection of elements allows for the use of foreach to examine each element in the set, as is shown below:

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_207AA8B68C604D5FAD2D32200DBC38AF"><tbody><tr><td><b>Code Region 6-9: Using ToElements() to get filter results</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ToElementsSample</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use ElementClassFilter to find all loads in the document</span><span>
        </span><span>// Using typeof(LoadBase) will yield all AreaLoad, LineLoad and PointLoad</span><span>
        </span><span>ElementClassFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>LoadBase</span><span>));</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> allLoads </span><span>=</span><span> collector</span><span>.</span><span>ToElements</span><span>();</span><span>

        </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"The loads in the current document are:\n"</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> loadElem </span><span>in</span><span> allLoads</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>LoadBase</span><span> load </span><span>=</span><span> loadElem </span><span>as</span><span> </span><span>LoadBase</span><span>;</span><span>
                prompt </span><span>+=</span><span> load</span><span>.</span><span>GetType</span><span>().</span><span>Name</span><span> </span><span>+</span><span>  </span><span>": "</span><span> </span><span>+</span><span> 
                                load</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

When just one passing element is needed, use FirstElement():

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_E6B708B8CDF14FEA9D8CFF9164C1E3D9"><tbody><tr><td><b>Code Region 6-10: Get the first passing element</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetFirstElement</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Create a filter to find all columns</span><span>
        </span><span>StructuralInstanceUsageFilter</span><span> columnFilter </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>StructuralInstanceUsageFilter</span><span>(</span><span>StructuralInstanceUsage</span><span>.</span><span>Column</span><span>);</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        collector</span><span>.</span><span>WherePasses</span><span>(</span><span>columnFilter</span><span>);</span><span>

        </span><span>// Get the first column from the filtered results</span><span>
        </span><span>// Element will be a FamilyInstance</span><span>
        </span><span>FamilyInstance</span><span> column </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

In some cases, FirstElement() is not sufficient. This next example shows how to use extension methods to get the first non-template 3D view (which is useful for input to the ReferenceIntersector constructors).

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_BAB9F3774BDD45609D959578662FA8B9"><tbody><tr><td><b>Code Region 6-11: Get first passing element using extension methods</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>UseExtensionMethods</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use filter to find a non-template 3D view</span><span>
        </span><span>// This example does not use FirstElement() since first filterd view3D might be a template</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>Func</span><span>&lt;</span><span>View3D</span><span>,</span><span> </span><span>bool</span><span>&gt;</span><span> isNotTemplate </span><span>=</span><span> v3 </span><span>=&gt;</span><span> </span><span>!(</span><span>v3</span><span>.</span><span>IsTemplate</span><span>);</span><span>

        </span><span>// apply ElementClassFilter</span><span>
        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>View3D</span><span>));</span><span>

        </span><span>// use extension methods to get first non-template View3D</span><span>
        </span><span>View3D</span><span> view3D </span><span>=</span><span> collector</span><span>.</span><span>Cast</span><span>&lt;</span><span>View3D</span><span>&gt;().</span><span>First</span><span>&lt;</span><span>View3D</span><span>&gt;(</span><span>isNotTemplate</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following example demonstrates the use of the FirstElementId() method to get one passing element (a 3d view in this case) and the use of ToElementIds() to get the filter results as a collection of element ids (in order to delete a set of elements in this case).

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_2D746E4434264430A42E85A14C20ECC7"><tbody><tr><td><b>Code Region 6-12: Using Getting filter results as element ids</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetElementIds</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>

        </span><span>// Use shortcut OfClass to get View elements</span><span>
        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>View3D</span><span>));</span><span>

        </span><span>// Get the Id of the first view</span><span>
        </span><span>ElementId</span><span> viewId </span><span>=</span><span> collector</span><span>.</span><span>FirstElementId</span><span>();</span><span>

        </span><span>// Test if the view is valid for element filtering</span><span>
        </span><span>if</span><span> </span><span>(</span><span>FilteredElementCollector</span><span>.</span><span>IsViewValidForElementIteration</span><span>(</span><span>document</span><span>,</span><span> viewId</span><span>))</span><span>
        </span><span>{</span><span>
                </span><span>FilteredElementCollector</span><span> viewCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>,</span><span> viewId</span><span>);</span><span>

                </span><span>// Get all FamilyInstance items in the view</span><span>
                viewCollector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilyInstance</span><span>));</span><span>
                </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> familyInstanceIds </span><span>=</span><span> viewCollector</span><span>.</span><span>ToElementIds</span><span>();</span><span>

                document</span><span>.</span><span>Delete</span><span>(</span><span>familyInstanceIds</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The GetElementIterator() method is used in the following example that iterates through the filtered elements to check the flow state of some pipes.

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_F8DE91F5939B480C9B3B12273F7F3E55"><tbody><tr><td><b>Code Region 6-13: Getting the results as an element iterator</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetIterator</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>

        </span><span>// Apply a filter to get all pipes in the document</span><span>
        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Plumbing</span><span>.</span><span>Pipe</span><span>));</span><span>

        </span><span>// Get results as an element iterator and look for a pipe with</span><span>
        </span><span>// a specific flow state</span><span>
        </span><span>FilteredElementIterator</span><span> elemItr </span><span>=</span><span> collector</span><span>.</span><span>GetElementIterator</span><span>();</span><span>
        elemItr</span><span>.</span><span>Reset</span><span>();</span><span>
        </span><span>while</span><span> </span><span>(</span><span>elemItr</span><span>.</span><span>MoveNext</span><span>())</span><span>
        </span><span>{</span><span>
                </span><span>Pipe</span><span> pipe </span><span>=</span><span> elemItr</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Pipe</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>pipe</span><span>.</span><span>FlowState</span><span> </span><span>==</span><span> </span><span>PipeFlowState</span><span>.</span><span>LaminarState</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Model has at least one pipe with Laminar flow state."</span><span>);</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Alternatively, the filter results can be returned as an element id iterator:

<table summary="" id="GUID-F1C6A68A-AD69-4153-A17B-A63F2B1C4E00__TABLE_E6A4097E7F4F4B639C7BA1B84E99138B"><tbody><tr><td><b>Code Region 6-14: Getting the results as an element id iterator</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetIdIterator</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use a RoomFilter to find all room elements in the document. </span><span>
        </span><span>RoomFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>RoomFilter</span><span>();</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>);</span><span>

        </span><span>// Get results as ElementId iterator</span><span>
        </span><span>FilteredElementIdIterator</span><span> roomIdItr </span><span>=</span><span> collector</span><span>.</span><span>GetElementIdIterator</span><span>();</span><span>
        roomIdItr</span><span>.</span><span>Reset</span><span>();</span><span>
        </span><span>while</span><span> </span><span>(</span><span>roomIdItr</span><span>.</span><span>MoveNext</span><span>())</span><span>
        </span><span>{</span><span>
                </span><span>ElementId</span><span> roomId </span><span>=</span><span> roomIdItr</span><span>.</span><span>Current</span><span>;</span><span>
                </span><span>// Warn rooms smaller than 50 SF</span><span>
                </span><span>Room</span><span> room </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>roomId</span><span>)</span><span> </span><span>as</span><span> </span><span>Room</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>room</span><span>.</span><span>Area</span><span> </span><span>&lt;</span><span> </span><span>50.0</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"Room is too small: id = "</span><span> </span><span>+</span><span> roomId</span><span>.</span><span>ToString</span><span>();</span><span>
                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

In some cases, it may be useful to test a single element against a given filter, rather than getting all elements that pass the filter. There are two overloads for ElementFilter.PassesFilter() that test a given Element, or ElementId, against the filter, returning true if the element passes the filter.


<!-- ===== END: Help  Getting filtered elements or element ids  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  LINQ Queries  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_LINQ_Queries_html
author: 
---

# Help | LINQ Queries | Autodesk

> ## Excerpt
> In .NET, the FilteredElementCollector class supports the IEnumerable interface for Elements. You can use this class with LINQ queries and operations to process lists of elements. Note that because the ElementFilters and the shortcut methods offered by this class process elements in native code before their managed wrappers are generated, better performance will be obtained by using as many native filters as possible on the collector before attempting to process the results using LINQ queries.

---
In .NET, the FilteredElementCollector class supports the IEnumerable interface for Elements. You can use this class with LINQ queries and operations to process lists of elements. Note that because the ElementFilters and the shortcut methods offered by this class process elements in native code before their managed wrappers are generated, better performance will be obtained by using as many native filters as possible on the collector before attempting to process the results using LINQ queries.

The following example uses an ElementClassFilter to get all FamilyInstance elements in the document, and then uses a LINQ query to narrow down the results to those FamilyInstances with a specific name.

<table summary="" id="GUID-2D0664C5-840E-49F5-B0B9-72F72C2A01A3__TABLE_696F17085098416F9F1EF7F109F66CD6"><tbody><tr><td><b>Code Region 6-15: Using LINQ query</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>LinqSample</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Use ElementClassFilter to find family instances whose name is 60" x 30" Student </span><span>
    </span><span>ElementClassFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>FamilyInstance</span><span>));</span><span>

    </span><span>// Apply the filter to the elements in the active document</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>);</span><span>

    </span><span>// Use Linq query to find family instances whose name is 60" x 30" Student</span><span>
    </span><span>var</span><span> query </span><span>=</span><span> </span><span>from</span><span> element </span><span>in</span><span> collector
                            </span><span>where</span><span> element</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"60\" x 30\" Student"</span><span>
                            </span><span>select</span><span> element</span><span>;</span><span>

    </span><span>// Cast found elements to family instances, </span><span>
    </span><span>// this cast to FamilyInstance is safe because ElementClassFilter for FamilyInstance was used</span><span>
    </span><span>List</span><span>&lt;</span><span>FamilyInstance</span><span>&gt;</span><span> familyInstances </span><span>=</span><span> query</span><span>.</span><span>Cast</span><span>&lt;</span><span>FamilyInstance</span><span>&gt;().</span><span>ToList</span><span>&lt;</span><span>FamilyInstance</span><span>&gt;();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  LINQ Queries  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Bounding Box filters  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Bounding_Box_filters_html
author: 
---

# Help | Bounding Box filters | Autodesk

> ## Excerpt
> The BoundingBox filters:

---
The BoundingBox filters:

-   BoundingBoxIsInsideFilter
-   BoundingBoxIntersectsFilter
-   BoundingBoxContainsPointFilter

help you find elements whose bounding boxes meet a certain criteria. You can check if each element’s bounding box is inside a given volume, intersects a given volume, or contains a given point. You can also reverse this check to find elements which do not intersect a volume or contain a given point.

BoundingBox filters use Outline as their inputs. Outline is a class representing a right rectangular prism whose axes are aligned to the Revit world coordinate system.

These filters work best for shapes whose actual geometry matches closely the geometry of its bounding box. Examples might include linear walls whose curve aligns with the X or Y direction, rectangular rooms formed by such walls, floors or roofs aligned to such walls, or reasonably rectangular families. Otherwise, there is the potential for false positives as the bounding box of the element may be much bigger than the actual geometry. (In these cases, you can use the actual element’s geometry to determine if the element really meets the criteria).


<!-- ===== END: Help  Bounding Box filters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Element Intersection Filters  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:28 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Element_Intersection_Filters_html
author: 
---

# Help | Element Intersection Filters | Autodesk

> ## Excerpt
> The element filters:

---
The element filters:

-   ElementIntersectsElementFilter
-   ElementIntersectsSolidFilter

pass elements whose actual 3D geometry intersects the 3D geometry of the target object.

With ElementIntersectsElementFilter, the target object is another element. The intersection is determined with the same logic used by Revit to determine if an interference exists during generation of an Interference Report. (This means that some combinations of elements will never pass this filter, such as concrete members which are automatically joined at their intersections, or site elements which are also excluded from interference checks). Also, elements which have no solid geometry, such as Rebar, will not pass this filter.

With ElementIntersectsSolidFilter, the target object is any solid. This solid could have been obtained from an existing element, created from scratch using the routines in GeometryCreationUtilities, or the result of a secondary operation such as a Boolean operation. Similar to the ElementIntersectsElementFilter, this filter will not pass elements which lack solid geometry.

Both filters can be inverted to match elements outside the target object volume.

Both filters are slow filters, and thus are best combined with one or more quick filters such as class or category filters.

<table summary="" id="GUID-2DE34D37-912E-475F-B3E0-BE40D88C8875__TABLE_074B6F03965549DE90BF60FFB33347F3"><tbody><tr><td><b>Code region: using ElementIntersectsSolidFilter to match elements which block disabled egress to doors</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Finds any Revit physical elements which interfere with the target </span><span>
</span><span>/// solid region surrounding a door.&lt;/summary&gt;</span><span>
</span><span>/// &lt;remarks&gt;This routine is useful for detecting interferences which are </span><span>
</span><span>/// violations of the Americans with Disabilities Act or other local disabled </span><span>
</span><span>/// access codes.&lt;/remarks&gt;</span><span>
</span><span>/// &lt;param name="doorInstance"&gt;The door instance.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="doorAccessibilityRegion"&gt;The accessibility region calculated</span><span>
</span><span>/// to surround the approach of the door.</span><span>
</span><span>/// Because the geometric parameters of this region are code- and </span><span>
</span><span>/// door-specific, calculation of the geometry of the region is not </span><span>
</span><span>/// demonstrated in this example.&lt;/param&gt;</span><span>
</span><span>/// &lt;returns&gt;A collection of interfering element ids.&lt;/returns&gt;</span><span>
</span><span>private</span><span> </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> </span><span>FindElementsInterferingWithDoor</span><span>(</span><span>FamilyInstance</span><span> doorInstance</span><span>,</span><span> </span><span>Solid</span><span> doorAccessibilityRegion</span><span>)</span><span>
</span><span>{</span><span>
   </span><span>// Setup the filtered element collector for all document elements.</span><span>
   </span><span>FilteredElementCollector</span><span> interferingCollector </span><span>=</span><span> 
      </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doorInstance</span><span>.</span><span>Document</span><span>);</span><span>

   </span><span>// Only accept element instances</span><span>
   interferingCollector</span><span>.</span><span>WhereElementIsNotElementType</span><span>();</span><span>

   </span><span>// Exclude intersections with the door itself or the host wall for the door.</span><span>
   </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> excludedElements </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
   excludedElements</span><span>.</span><span>Add</span><span>(</span><span>doorInstance</span><span>.</span><span>Id</span><span>);</span><span>
   excludedElements</span><span>.</span><span>Add</span><span>(</span><span>doorInstance</span><span>.</span><span>Host</span><span>.</span><span>Id</span><span>);</span><span>
   </span><span>ExclusionFilter</span><span> exclusionFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ExclusionFilter</span><span>(</span><span>excludedElements</span><span>);</span><span>
   interferingCollector</span><span>.</span><span>WherePasses</span><span>(</span><span>exclusionFilter</span><span>);</span><span>

   </span><span>// Set up a filter which matches elements whose solid geometry intersects </span><span>
   </span><span>// with the accessibility region</span><span>
   </span><span>ElementIntersectsSolidFilter</span><span> intersectionFilter </span><span>=</span><span> 
      </span><span>new</span><span> </span><span>ElementIntersectsSolidFilter</span><span>(</span><span>doorAccessibilityRegion</span><span>);</span><span>
   interferingCollector</span><span>.</span><span>WherePasses</span><span>(</span><span>intersectionFilter</span><span>);</span><span>

   </span><span>// Return all elements passing the collector</span><span>
   </span><span>return</span><span> interferingCollector</span><span>.</span><span>ToElementIds</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Element Intersection Filters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Selection  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:32 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_html
author: 
---

# Help | Selection | Autodesk

> ## Excerpt
> You can get the selected objects from the current active document using the UIDocument.Selection.GetElementIds() method which returns a collection fo ElementIds of the selected elements. The collection returned by this method can be used directly with FilteredElementCollector to filter the selected elements.

---
You can get the selected objects from the current active document using the UIDocument.Selection.GetElementIds() method which returns a collection fo ElementIds of the selected elements. The collection returned by this method can be used directly with FilteredElementCollector to filter the selected elements.

The Selection object can also be used to change the current selection programmatically using the SetElementIds() method.

**Pages in this section**

-   [Changing the Selection](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_Changing_the_Selection_html)
-   [User Selection](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_User_Selection_html)
-   [Filtered User Selection](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_Filtered_User_Selection_html)

**Parent page:** [Basic Interaction with Revit Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_html)


<!-- ===== END: Help  Selection  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Changing the Selection  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:40 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_Changing_the_Selection_html
author: 
---

# Help | Changing the Selection | Autodesk

> ## Excerpt
> To modify the selected elements:

---
To modify the selected elements:

1.  Create a new List of ElementIds.
2.  Put ElementIds in it.
3.  Call SetElementIds() with the new list.

The following example illustrates how to change the selected Elements by getting the current selection and filtering out just walls to set as the new selection.

It is also possible to select references by using `SetReferences()`. The references can be an element or a sub element in the host or a linked document. `GetReferences()` returns the references that are currently selected.

<table summary="" id="GUID-541141C8-F390-424E-88BD-54F667C823F8__TABLE_41B2C4147FA34DF794CABDD1932F8C2B"><tbody><tr><td><b>Code Region 7-1: Changing selected elements</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ChangeSelection</span><span>(</span><span>UIDocument</span><span> uidoc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get selected elements from current document.</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

    </span><span>// Display current number of selected elements</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Number of selected elements: "</span><span> </span><span>+</span><span> selectedIds</span><span>.</span><span>Count</span><span>.</span><span>ToString</span><span>());</span><span>

    </span><span>// Go through the selected items and filter out walls only.</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedWallIds </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> elements </span><span>=</span><span> uidoc</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>elements </span><span>is</span><span> </span><span>Wall</span><span>)</span><span>
        </span><span>{</span><span>
            selectedWallIds</span><span>.</span><span>Add</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// Set the created element set as current select element set.</span><span>
    uidoc</span><span>.</span><span>Selection</span><span>.</span><span>SetElementIds</span><span>(</span><span>selectedWallIds</span><span>);</span><span>

    </span><span>// Give the user some information.</span><span>
    </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>!=</span><span> selectedWallIds</span><span>.</span><span>Count</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> selectedWallIds</span><span>.</span><span>Count</span><span>.</span><span>ToString</span><span>()</span><span> </span><span>+</span><span> </span><span>" Walls are selected!"</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"No Walls have been selected!"</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Changing the Selection  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  User Selection  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_User_Selection_html
author: 
---

# Help | User Selection | Autodesk

> ## Excerpt
> The Selection class also has methods for allowing the user to select new objects, or even a point on screen. This allows the user to select one or more Elements (or other objects, such as an edge or a face) using the cursor and then returns control to your application. These functions do not automatically add the new selection to the active selection collection.

---
The Selection class also has methods for allowing the user to select new objects, or even a point on screen. This allows the user to select one or more Elements (or other objects, such as an edge or a face) using the cursor and then returns control to your application. These functions do not automatically add the new selection to the active selection collection.

-   The PickObject() method prompts the user to select an object in the Revit model.
-   The PickObjects() method prompts the user to select multiple objects in the Revit model.
-   The PickElementsByRectangle() method prompts the user to select multiple elements using a rectangle.
-   The PickPoint() method prompts the user to pick a point in the active sketch plane.
-   The PickBox() method invokes a general purpose two-click editor that lets the user to specify a rectangular area on the screen.

The type of object to be selected is specified when calling PickObject() or PickObjects. Types of objects that can be specified are: Element, PointOnElement, Edge or Face.

The StatusbarTip property shows a message in the status bar when your application prompts the user to pick objects or elements. Each of the Pick functions has an overload that has a String parameter in which a custom status message can be provided.

<table summary="" id="GUID-97372731-5ACA-4EB7-ABDF-7E6B56640DA2__TABLE_F2441DC827DC4D3481B67DC8C3B6EF26"><tbody><tr><td><b>Code Region 7-2: Adding selected elements with PickObject() and PickElementsByRectangle()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SelectElements</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>Selection</span><span> choices </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>;</span><span>
    </span><span>// Pick one object from Revit.</span><span>
    </span><span>Reference</span><span> hasPickOne </span><span>=</span><span> choices</span><span>.</span><span>PickObject</span><span>(</span><span>ObjectType</span><span>.</span><span>Element</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>hasPickOne </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"One element selected."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Use the rectangle picking tool to identify model elements to select.</span><span>
    </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> pickedElements </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>PickElementsByRectangle</span><span>(</span><span>"Select by rectangle"</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>pickedElements</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span> 
        </span><span>// Collect Ids of all picked elements</span><span>
        </span><span>IList</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> idsToSelect </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;(</span><span>pickedElements</span><span>.</span><span>Count</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> element </span><span>in</span><span> pickedElements</span><span>)</span><span>
        </span><span>{</span><span>
            idsToSelect</span><span>.</span><span>Add</span><span>(</span><span>element</span><span>.</span><span>Id</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>// Update the current selection</span><span>
        uidoc</span><span>.</span><span>Selection</span><span>.</span><span>SetElementIds</span><span>(</span><span>idsToSelect</span><span>);</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>string</span><span>.</span><span>Format</span><span>(</span><span>"{0} elements added to Selection."</span><span>,</span><span> idsToSelect</span><span>.</span><span>Count</span><span>));</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The PickPoint() method has 2 overloads with an ObjectSnapTypes parameter which is used to specify the type of snap types used for the selection. More than one can be specified, as shown in the next example.

<table summary="" id="GUID-97372731-5ACA-4EB7-ABDF-7E6B56640DA2__TABLE_772F9E8F0AC743EF8613D7CF268C9035"><tbody><tr><td><b>Code Region 7-3: Snap points</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>PickPoint</span><span>(</span><span>UIDocument</span><span> uidoc</span><span>)</span><span>
</span><span>{</span><span>

        </span><span>ObjectSnapTypes</span><span> snapTypes </span><span>=</span><span> </span><span>ObjectSnapTypes</span><span>.</span><span>Endpoints</span><span> </span><span>|</span><span> </span><span>ObjectSnapTypes</span><span>.</span><span>Intersections</span><span>;</span><span>
        XYZ point </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>PickPoint</span><span>(</span><span>snapTypes</span><span>,</span><span> </span><span>"Select an end point or intersection"</span><span>);</span><span>

        </span><span>string</span><span> strCoords </span><span>=</span><span> </span><span>"Selected point is "</span><span> </span><span>+</span><span> point</span><span>.</span><span>ToString</span><span>();</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> strCoords</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The PickBox() method takes a PickBoxStyle enumerator. The options are Crossing, the style used when selecting objects completely or partially inside the box, Enclosing, the style used selecting objects that are completely enclosed by the box, and Directional, in which the style of the box depends on the direction in which the box is being drawn. It uses the Crossing style if it is being drawn from right to left, or the Enclosing style when drawn in the opposite direction.

PickBox() returns a PickedBox which contains the Min and Max points selected. The following example demonstrates the use of PickBox() in Point Cloud selection.

<table summary="" id="GUID-97372731-5ACA-4EB7-ABDF-7E6B56640DA2__TABLE_F4E420FBF48D45BFA285281678FB7B98"><tbody><tr><td><b>Code Region: PickBox</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>PromptForPointCloudSelection</span><span>(</span><span>UIDocument</span><span> uiDoc</span><span>,</span><span> </span><span>PointCloudInstance</span><span> pcInstance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span> uiDoc</span><span>.</span><span>Application</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>Selection</span><span> currentSel </span><span>=</span><span> uiDoc</span><span>.</span><span>Selection</span><span>;</span><span>

    </span><span>PickedBox</span><span> pickedBox </span><span>=</span><span> currentSel</span><span>.</span><span>PickBox</span><span>(</span><span>PickBoxStyle</span><span>.</span><span>Enclosing</span><span>,</span><span> </span><span>"Select region of cloud for highlighting"</span><span>);</span><span>

    XYZ min </span><span>=</span><span> pickedBox</span><span>.</span><span>Min</span><span>;</span><span>
    XYZ max </span><span>=</span><span> pickedBox</span><span>.</span><span>Max</span><span>;</span><span>

    </span><span>//Transform points into filter</span><span>
    </span><span>View</span><span> view </span><span>=</span><span> uiDoc</span><span>.</span><span>ActiveView</span><span>;</span><span>
    XYZ right </span><span>=</span><span> view</span><span>.</span><span>RightDirection</span><span>;</span><span>
    XYZ up </span><span>=</span><span> view</span><span>.</span><span>UpDirection</span><span>;</span><span>

    </span><span>List</span><span>&lt;</span><span>Plane</span><span>&gt;</span><span> planes </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Plane</span><span>&gt;();</span><span>

    </span><span>// X boundaries</span><span>
    </span><span>bool</span><span> directionCorrect </span><span>=</span><span> </span><span>IsPointAbovePlane</span><span>(</span><span>right</span><span>,</span><span> min</span><span>,</span><span> max</span><span>);</span><span>
    planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>right</span><span>,</span><span> directionCorrect </span><span>?</span><span> min </span><span>:</span><span> max</span><span>));</span><span>
    planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(-</span><span>right</span><span>,</span><span> directionCorrect </span><span>?</span><span> max </span><span>:</span><span> min</span><span>));</span><span>

    </span><span>// Y boundaries</span><span>
    directionCorrect </span><span>=</span><span> </span><span>IsPointAbovePlane</span><span>(</span><span>up</span><span>,</span><span> min</span><span>,</span><span> max</span><span>);</span><span>
    planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>up</span><span>,</span><span> directionCorrect </span><span>?</span><span> min </span><span>:</span><span> max</span><span>));</span><span>
    planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(-</span><span>up</span><span>,</span><span> directionCorrect </span><span>?</span><span> max </span><span>:</span><span> min</span><span>));</span><span>

    </span><span>// Create filter</span><span>
    </span><span>PointCloudFilter</span><span> filter </span><span>=</span><span> </span><span>PointCloudFilterFactory</span><span>.</span><span>CreateMultiPlaneFilter</span><span>(</span><span>planes</span><span>);</span><span>
    </span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>uiDoc</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Highlight"</span><span>);</span><span>
    t</span><span>.</span><span>Start</span><span>();</span><span>
    pcInstance</span><span>.</span><span>SetSelectionFilter</span><span>(</span><span>filter</span><span>);</span><span>
    pcInstance</span><span>.</span><span>FilterAction</span><span> </span><span>=</span><span> </span><span>SelectionFilterAction</span><span>.</span><span>Highlight</span><span>;</span><span>
    t</span><span>.</span><span>Commit</span><span>();</span><span>
    uiDoc</span><span>.</span><span>RefreshActiveView</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Selection Events

The `SelectionChanged` event notifies your code after the selection changes. `SelectionChangedEventArgs` provides access to the references and element ids that are selected.


<!-- ===== END: Help  User Selection  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Filtered User Selection  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:49 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_Filtered_User_Selection_html
author: 
---

# Help | Filtered User Selection | Autodesk

> ## Excerpt
> PickObject(), PickObjects() and PickElementsByRectangle() all have overloads that take an ISelectionFilter as a parameter. ISelectionFilter is an interface that can be implemented to filter objects during a selection operation. It has two methods that can be overridden: AllowElement() which is used to specify if an element is allowed to be selected, and AllowReference() which is used to specify if a reference to a piece of geometry is allowed to be selected.

---
PickObject(), PickObjects() and PickElementsByRectangle() all have overloads that take an ISelectionFilter as a parameter. ISelectionFilter is an interface that can be implemented to filter objects during a selection operation. It has two methods that can be overridden: AllowElement() which is used to specify if an element is allowed to be selected, and AllowReference() which is used to specify if a reference to a piece of geometry is allowed to be selected.

The following example illustrates how to use an ISelectionFilter interface to limit the user's selection to elements in the Mass category. It does not allow any references to geometry to be selected.

<table summary="" id="GUID-ECB1EE82-EA91-451C-995C-7683C1F676CB__TABLE_441BBE03B59F4A7398ED1A104D1C6250"><tbody><tr><td><b>Code Region 7-4: Using ISelectionFilter to limit element selection</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> </span><span>GetManyRefByRectangle</span><span>(</span><span>UIDocument</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>ReferenceArray</span><span> ra </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>
        </span><span>ISelectionFilter</span><span> selFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>MassSelectionFilter</span><span>();</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> eList </span><span>=</span><span> doc</span><span>.</span><span>Selection</span><span>.</span><span>PickElementsByRectangle</span><span>(</span><span>selFilter</span><span>,</span><span> 
                </span><span>"Select multiple faces"</span><span>)</span><span> </span><span>as</span><span> </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;;</span><span>
        </span><span>return</span><span> eList</span><span>;</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>class</span><span> </span><span>MassSelectionFilter</span><span> </span><span>:</span><span> </span><span>ISelectionFilter</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowElement</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
        </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>element</span><span>.</span><span>Category</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Mass"</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>true</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>return</span><span> </span><span>false</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowReference</span><span>(</span><span>Reference</span><span> refer</span><span>,</span><span> XYZ point</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>false</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The next example demonstrates the use of ISelectionFilter to allow only planar faces to be selected.

<table summary="" id="GUID-ECB1EE82-EA91-451C-995C-7683C1F676CB__TABLE_CBF97B8571924E25937696B04827FB08"><tbody><tr><td><b>Code Region 7-5: Using ISelectionFilter to limit geometry selection</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SelectPlanarFaces</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ISelectionFilter</span><span> selFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>PlanarFacesSelectionFilter</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Reference</span><span>&gt;</span><span> faces </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>PickObjects</span><span>(</span><span>ObjectType</span><span>.</span><span>Face</span><span>,</span><span> 
                selFilter</span><span>,</span><span> </span><span>"Select multiple planar faces"</span><span>);</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>class</span><span> </span><span>PlanarFacesSelectionFilter</span><span> </span><span>:</span><span> </span><span>ISelectionFilter</span><span>
</span><span>{</span><span>
        </span><span>Document</span><span> doc </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>public</span><span> </span><span>PlanarFacesSelectionFilter</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
        </span><span>{</span><span>
                doc </span><span>=</span><span> document</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowElement</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>true</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowReference</span><span>(</span><span>Reference</span><span> refer</span><span>,</span><span> XYZ point</span><span>)</span><span>
        </span><span>{</span><span>   
                </span><span>if</span><span> </span><span>(</span><span>doc</span><span>.</span><span>GetElement</span><span>(</span><span>refer</span><span>).</span><span>GetGeometryObjectFromReference</span><span>(</span><span>refer</span><span>)</span><span> </span><span>is</span><span> </span><span>PlanarFace</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>// Only return true for planar faces. Non-planar faces will not be selectable </span><span>
                        </span><span>return</span><span> </span><span>true</span><span>;</span><span> 
                </span><span>}</span><span>
                </span><span>return</span><span> </span><span>false</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

For more information about retrieving Elements from selected Elements, see [Walkthrough: Retrieve Selected Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Walkthrough_Retrieve_Selected_Elements_html) in the [Getting Started](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_html) section.


<!-- ===== END: Help  Filtered User Selection  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Parameters  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:54 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_html
author: 
---

# Help | Parameters | Autodesk

> ## Excerpt
> Revit provides a general mechanism for giving each element a set of parameters that you can edit.

---
Revit provides a general mechanism for giving each element a set of parameters that you can edit.

In the Revit UI, some element parameters are visible in the Element Properties Palette. The following sections describe how to get and use built-in parameters, shared parameters and global parameters.

In the Revit Platform API, Parameters are managed in the Element class. You can access Parameters in these ways:

Common ways to get the value of a parameter are shown below. In this sample, all three lines of code get the same parameter. Because this parameter is stored as a string, the `AsString()` method is used to get its value.

```
private void GetStringParameterValue(Wall wall)
{
    string s1 = wall.LookupParameter("Comments").AsString();
    string s2 = wall.GetParameter(ParameterTypeId.AllModelInstanceComments).AsString();
    string s3 = wall.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS).AsString();
}
```

Other ways to get a parameter are:

-   By iterating through the Element.Parameters collection of all parameters for an Element (for an example, see the sample code in [Walkthrough Get Selected Element Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Walkthrough_Get_Selected_Element_Parameters_html)).
-   By iterating through the collection returned by Element.GetOrderedParameters(), which returns only parameters visible in the Properties Palette.
-   By accessing a parameter by name via the Element.ParametersMap collection or Element.GetParameters()

You can retrieve the Parameter object from an Element using the overloaded Parameter property if you know the built-in ID, definition, or GUID. The Parameter\[GUID\] property overload gets a shared parameter based on its Global Unique ID (GUID), which is assigned to the shared parameter when it's created.

The Element.LookupParameter() method gets a parameter based on its localized name, so your code should handle different languages if it's going to look up parameters by name and needs to run in more than one locale. Also, keep in mind that multiple matches of parameters with the same name can occur because shared parameters or project parameters can be bound to an element category even if there is already a built-in parameter with the same name. For this reason, it is better to use Element.GetParameters() which will return all parameters matching the given name. Element.LookupParameter() will return the first match found.


<!-- ===== END: Help  Parameters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Parameter  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:03 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Parameter_html
author: 
---

# Help | Parameter | Autodesk

> ## Excerpt
> The Parameter class contains the value for the given parameter.

---
The Parameter class contains the value for the given parameter.

All Elements within Autodesk Revit contain Parameters, which can be retrieved as a set or individually. An individual parameter object can be obtained from any Element using either a BuiltInParameter enumeration, a Definition object or a Shared Parameter GUID.

The data contained within the parameter can be either a Double, Integer, String or ElementId, as indicated by its StorageType property. For value types, the DisplayUnitType property will indicate the display unit used for the parameter value. The Parameter object also contains a [Definition](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Definition_html "The Definition object describes the data type, name, and other Parameter details.") object that describes the data type, name and other details of the parameter.

## StorageType

StorageType describes the type of parameter values stored internally.

Based on the property value, use the corresponding get and set methods to retrieve and set the parameter data value.

The StorageType is an enumerated type that lists all internal parameter data storage types supported by Revit:

<table summary="" id="GUID-FEA13CF3-85D2-4D19-978B-0A5BCD0D710A__TABLE_CC5D594BCB2B441FA238B6B3BB9061B8"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td>_String_</td><td>Internal data is stored as a string of characters.</td></tr><tr><td>_ElementId_</td><td>Data type represents an element and is stored as an Element ID.</td></tr><tr><td>_Double_</td><td>Data is stored internally as an 8-byte floating point number.</td></tr><tr><td>_Integer_</td><td>Internal data is stored as a signed 32-bit integer.</td></tr><tr><td>_None_</td><td>None represents an invalid storage type. For internal use only.</td></tr></tbody></table>

In most cases, the ElementId value is a positive number. However, it can be a negative number. When the ElementId value is negative, it does not represent an Element but has another meaning. For example, the storage type parameter for a beam's Vertical Projection is ElementId. When the parameter value is Level 1 or Level 2, the ElementId value is positive and corresponds to the ElementId of that level. However, when the parameter value is set to Auto-detect, Center of Beam or Top of Beam, the ElementId value is negative.

The following code sample shows how to check whether a parameter's value can be set to a double value, based on its StorageType:

<table summary="" id="GUID-FEA13CF3-85D2-4D19-978B-0A5BCD0D710A__TABLE_E19B02276D564884B2EB427762713A30"><tbody><tr><td><b>Code Region: Checking a parameter's StorageType</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>SetParameter</span><span>(</span><span>Parameter</span><span> parameter</span><span>,</span><span> </span><span>double</span><span> value</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> result </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>//if the parameter is readonly, you can't change the value of it</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> parameter </span><span>&amp;&amp;</span><span> </span><span>!</span><span>parameter</span><span>.</span><span>IsReadOnly</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>StorageType</span><span> storageType </span><span>=</span><span> parameter</span><span>.</span><span>StorageType</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>StorageType</span><span>.</span><span>Double</span><span> </span><span>!=</span><span> storageType</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"The storagetypes of value and parameter are different!"</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>//If successful, the result is true</span><span>
        result </span><span>=</span><span> parameter</span><span>.</span><span>Set</span><span>(</span><span>value</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> result</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The Set() method return value indicates that the Parameter value was changed. The Set() method returns true if the Parameter value was changed, otherwise it returns false.

Not all Parameters are writable. An Exception is thrown if the Parameter is read-only.

## AsValueString() and SetValueString()

These two Parameter class methods only apply to value type parameters, which are double or integer parameters representing a measured quantity.

Use the AsValueString() method to get the parameter value as a string with the unit of measure. For example, the Base Offset value, a wall parameter, is a Double value. Usually the value is shown as a string like -20'0" in the Element Properties. Using the AsValueString() method, you get the -20'0" string value directly. Using the AsDouble() method, you get a double value like -20 without the units of measure.

Use the SetValueString() method to change the value of a value type parameter instead of using the Set() method. The following code sample illustrates how to change the parameter value using the SetValueString() method:

<table summary="" id="GUID-FEA13CF3-85D2-4D19-978B-0A5BCD0D710A__TABLE_0AC674B655AF45A885ABE785167F4713"><tbody><tr><td><b>Code Region: Using Parameter.SetValueString()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>SetWithValueString</span><span>(</span><span>Parameter</span><span> foundParameter</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> result </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>foundParameter</span><span>.</span><span>IsReadOnly</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>//If successful, the result is true</span><span>
        result </span><span>=</span><span> foundParameter</span><span>.</span><span>SetValueString</span><span>(</span><span>"-22\'3\""</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>return</span><span> result</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Global parameter associations

The Parameter class has several methods for maintaining associations between element parameters and global parameters. The method GetAssociatedGlobalParameter() returns the ElementId of a global parameter, if any, currently associated with a parameter. InvalidElementId is returned in case this parameter is not associated with any global parameter. InvalidElementId is also returned if called for a parameter that cannot even be associated with a global parameters (i.e. a non-parameterizable parameter or a parameter with a formula).

There are two methods to determine if a parameter can be associated with global parameters. Parameter.CanBeAssociatedWithGlobalParameters() tests wether a parameter can be associated with any global parameter. Only properties defined as parametrizable can be associated with global parameters. That excludes any read-only and formula-driven parameters, as well as those that have other explicit or implicit restrictions imposed by Revit. To test whether a specific global parameter can be associated with this parameter, use Parameter.CanBeAssociatedWithGlobalParameter(). Keep in mind that the parameter's value type must match the type of the global parameter to create an association.

For parameters that can be associated with a global parameter, use AssociateWithGlobalParameter() to create the association. Once associated, the parameter can be later dissociated by calling the DissociateFromGlobalParameter() method

## ParameterUtils

ParameterUtils is a class with static utility functions related to ForgeTypeId parameter identifiers:

-   ParameterUtils.GetAllBuiltInGroups()
-   ParameterUtils.GetAllBuiltInParameters()
-   ParameterUtils.IsBuiltInGroup(ForgeTypeId)
-   ParameterUtils.IsBuiltInParameter(ForgeTypeId)

The ParameterUtils class contains several methods new in Revit 2022 but also deprecated. They are offered only to assist in migrating code from the BuiltInParameter and BuiltInParameterGroup enumerations to the ForgeTypeId class.

-   ParameterUtils.GetBuiltInParameter(ForgeTypeId)
-   ParameterUtils.GetBuiltInParameterGroup(ForgeTypeId)
-   ParameterUtils.GetParameterGroupTypeId(BuiltInParameterGroup)
-   ParameterUtils.GetParameterTypeId(BuiltInParameter)

## Multiple Values

The `MultipleValuesIndicationSettings` class allows access to the custom value used in instances of the Properties dialog, Tags, and Schedules when multiple elements are referenced and the value of the parameter is differs among those elements


<!-- ===== END: Help  Parameter  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Definition  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:08 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Definition_html
author: 
---

# Help | Definition | Autodesk

> ## Excerpt
> The Definition object describes the data type, name, and other Parameter details.

---
The Definition object describes the data type, name, and other Parameter details.

There are two kinds of definition objects derived from this object.

-   InternalDefinition represents all kinds of definitions existing entirely in the Revit database.
-   ExternalDefinition represents definitions stored on disk in a shared parameter file.

You should write the code to use the Definition base class so that the code is applicable to both internal and external parameter Definitions. The following code sample shows how to find a specific parameter using the definition type.

<table summary="" id="GUID-13EE268E-DEAC-4245-A192-E14BFA63E382__TABLE_E2A463303AAA4F09B5BAB775B1171CEF"><tbody><tr><td><b>Code Region 8-2: Finding a parameter based on definition type</b></td></tr><tr><td><pre><code><span>//Find parameter using the Parameter's definition type.</span><span>
</span><span>public</span><span> </span><span>Parameter</span><span> </span><span>FindParameter</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Parameter</span><span> foundParameter </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>// This will find the first parameter that measures length</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Parameter</span><span> parameter </span><span>in</span><span> element</span><span>.</span><span>Parameters</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>parameter</span><span>.</span><span>Definition</span><span>.</span><span>GetDataType</span><span>()</span><span> </span><span>==</span><span> </span><span>SpecTypeId</span><span>.</span><span>Length</span><span>)</span><span>
                </span><span>{</span><span>
                        foundParameter </span><span>=</span><span> parameter</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>return</span><span> foundParameter</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Parameter Data Type

For parameters associated with units of measurement, `GetDataType()` returns a measurable spec identifier. Use `UnitUtils.IsMeasurableSpec(ForgeTypeId)` to detect a measurable spec identifier.

For Family Type parameters, `GetDataType()` returns a category identifier. Use `Category.IsBuiltInCategory(ForgeTypeId)` to detect a category identifier.

For all other parameters, `GetDataType()` returns a spec identifier. Use `Parameter.IsSpec(ForgeTypeId)` to detect a spec identifier, including measurable specs.

### GetGroupTypeId()

The Definition class GetGroupTypeId() method returns a ForgeTypeId. The members of the GroupTypeId class list all value supported by Revit. The GroupTypeId is used to sort parameters in the Element Properties dialog box.

## InternalDefinition

Every Parameter object has an InternalDefinition, which can be obtained from the Definition property. The InternalDefinition represents the parameter definition in the Revit document. In addition to the properties it inherits from Definition, it also has some other key properties.

### BuiltInParameter

This property tests whether this definition identifies a built-in parameter or not. For a built-in parameter, this property returns one of the BuiltInParameter enumerated values. For custom-defined parameters, such as shared, global, or family parameters the value will be BuiltInParameter.INVALID.

### Id

This property returns the id for the associated ParameterElement if the parameter is not built-in.

### VariesAcrossGroups

This property, and the corresponding SetAllowVaryBetweenGroups() method, determine whether the values of this parameter can vary across the related members of group instances. If False, the values will be consistent across the related members in group instances. This can only be set for non-built-in parameters.

### Visible

The visible property indicates whether a shared parameter is hidden from the user. This is useful if you wish to add data to an element that is only meaningful to your application and not to the user. This value can only be set when the shared parameter definition is created.


<!-- ===== END: Help  Definition  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Built-In Parameters  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:13 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Built_In_Parameters_html
author: 
---

# Help | Built-In Parameters | Autodesk

> ## Excerpt
> The Revit Platform API has a large number of built-in parameters.

---
The Revit Platform API has a large number of built-in parameters.

Built-in parameters are defined in the Autodesk.Revit.Parameters.BuiltInParameter enumeration (see the RevitAPI Help.chm file for the definition of this enumeration). This enumeration has generated documentation visible from Visual Studio intellisense as shown below. The documentation for each id includes the parameter name, as found in the Element Properties dialog in the English version of Autodesk Revit. Note that multiple distinct parameter ids may map to the same English name; in those cases you must examine the parameters associated with a specific element to determine which parameter id to use.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/BuiltInParameter-76164.jpg)

The parameter ID is used to retrieve the specific parameter from an element, if it exists, using the Element.Parameter property. However, not all parameters can be retrieved using the ID. For example, family parameters are not exposed in the Revit Platform API, therefore, you cannot get them using the built-in parameter ID.

The following code sample shows how to get the specific parameter using the BuiltInParameter Id:

<table summary="" id="GUID-C0D9C62F-1BEB-412E-B5B4-E70E2EF4F378__TABLE_7B05D97002E64C939B306A59D69E43DE"><tbody><tr><td><b>Code Region 8-3: Getting a parameter based on BuiltInParameter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Parameter</span><span> </span><span>FindWithBuiltinParameterID</span><span>(</span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use the WALL_BASE_OFFSET paramametId</span><span>
        </span><span>// to get the base offset parameter of the wall.</span><span>
        </span><span>BuiltInParameter</span><span> paraIndex </span><span>=</span><span> </span><span>BuiltInParameter</span><span>.</span><span>WALL_BASE_OFFSET</span><span>;</span><span>
        </span><span>Parameter</span><span> parameter </span><span>=</span><span> wall</span><span>.</span><span>get_Parameter</span><span>(</span><span>paraIndex</span><span>);</span><span>

        </span><span>return</span><span> parameter</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Getting localized parameter names

The method `LabelUtils.GetLabelFor Method (BuiltInParameter, LanguageType)` returns the localized string name for the built-in parameter. If the corresponding resource DLL cannot be found, the US-English name will be returned.


<!-- ===== END: Help  Built-In Parameters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Parameter Relationships  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Parameter_Relationships_html
author: 
---

# Help | Parameter Relationships | Autodesk

> ## Excerpt
> Parameters can be affected by each other.

---
Parameters can be affected by each other.

There are relationships between Parameters where the value of one Parameter can affect:

-   whether another Parameter can be set, or is read-only
-   what parameters are valid for the element
-   the computed value of another parameter

Additionally, some parameters are always read-only.

Some parameters are computed in Revit, such as wall Length and Area parameter. These parameters are always read-only because they depend on the element's internal state.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-B11C1A73-B5DE-4429-B728-C739D963AE1A-low.png)**Figure 29: Wall computed parameters**

In this code sample, the Sill Height parameter for an opening is adjusted, which results in the Head Height parameter being re-computed:

<table summary="" id="GUID-5FCE711C-A73C-434C-AD3E-5B07BEA27CB4__TABLE_A0B3C4D039D749799C1D8E68567358A4"><tbody><tr><td><b>Code Region: Parameter relationship example</b></td></tr><tr><td><pre><code><span>// opening should be an opening such as a window or a door</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>ShowParameterRelationship</span><span>(</span><span>FamilyInstance</span><span> opening</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// get the original Sill Height and Head Height parameters for the opening</span><span>
        </span><span>Parameter</span><span> sillPara </span><span>=</span><span> opening</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>InstanceSillHeightParam</span><span>);</span><span>
        </span><span>Parameter</span><span> headPara </span><span>=</span><span> opening</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>InstanceHeadHeightParam</span><span>);</span><span>
        </span><span>double</span><span> sillHeight </span><span>=</span><span> sillPara</span><span>.</span><span>AsDouble</span><span>();</span><span>
        </span><span>double</span><span> origHeadHeight </span><span>=</span><span> headPara</span><span>.</span><span>AsDouble</span><span>();</span><span>

        </span><span>// Change the Sill Height only and notice that Head Height is recalculated</span><span>
        sillPara</span><span>.</span><span>Set</span><span>(</span><span>sillHeight </span><span>+</span><span> </span><span>2.0</span><span>);</span><span>
        </span><span>double</span><span> newHeadHeight </span><span>=</span><span> headPara</span><span>.</span><span>AsDouble</span><span>();</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Info"</span><span>,</span><span> </span><span>"Old head height: "</span><span> </span><span>+</span><span> origHeadHeight </span><span>+</span><span> </span><span>"; new head height: "</span><span> 
                </span><span>+</span><span> newHeadHeight</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Global parameters also have relationships with other parameters. See the [GlobalParameter Basics](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_GlobalParameter_Basics_html "The GlobalParameter class represents a global parameter in a project document and can be used to create and modify global parameters.") topic for more information.


<!-- ===== END: Help  Parameter Relationships  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Shared Parameters  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_html
author: 
---

# Help | Shared Parameters | Autodesk

> ## Excerpt
> Shared Parameters are parameter definitions stored in an external text file.

---
Shared Parameters are parameter definitions stored in an external text file.

The definitions are identified by a unique identifier generated when the definition is created and can be used in multiple projects.

The main objects associated with shared parameters are:

-   DefinitionFile - represents a shared parameters file on disk
-   DefinitionGroup - group of shared parameters which are organized into meaningful sets
-   ExternalDefinition - represents a shared parameter definition, belongs to a DefinitionGroup
-   ExternalDefinitions - supports the creation of new shared parameters definitions
-   Binding - binds a parameter definition to one or more categories
-   BindingMap - contains all the parameter bindings that exist in the Autodesk Revit project
-   ParameterElement - stores information about a particular user-defined parameter in the document
-   SharedParameterElement - derived from ParameterElement, stores the definition of a shared parameter The following sections describe how to gain access to shared parameter definitions through the Revit Platform API, including how to get a shared parameter definition and bind it to Elements in certain Categories.

To access Shared Parameters after they are defined and bound to categories, see [Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Built_In_Parameters_html "Revit provides a general mechanism for giving each element a set of parameters that you can edit.").

## Clearing the value of a parameter

`Parameter.ClearValue()` resets the value of a shared parameter with the HideWhenNoValue flag to a cleared state. This method is not applicable to clear the value of any other parameter type.

### Hiding empty parameters

The property `ExternalDefinition.HideWhenNoValue` indicates if the shared parameter should be hidden from the property palette and `Element.GetOrderedParameters()` when it has no value.

This can be set when creating a shared parameter by setting `ExternalDefinitionCreationOptions.HideWhenNoValue` There is also `SharedParameterElement.ShouldHideWhenNoValue()`

### Filtering by presence or absence of parameter value

These filter classes define filter rules evaluating whether or not a parameter has a value for a specific element:

-   ParameterValuePresenceRule
-   HasValueFilterRule
-   HasNoValueFilterRule

These static methods create an instance of these rules for use in a parameter filter.:

-   FilterRule.CreateHasValueParameterRule()
-   FilterRule.CreateHasNoValueParameterRule()

In schedules, use these new enumerated values with the method `ScheduleDefinition.CanFilterByValuePresence()` to filter based on the presence or absence of a value assigned to that parameter:

-   ScheduleFilterType.HasValue
-   ScheduleFilterType.HasNoValue


<!-- ===== END: Help  Shared Parameters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Definition File  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:30 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_Definition_File_html
author: 
---

# Help | Definition File | Autodesk

> ## Excerpt
> The DefinitionFile object represents a shared parameter file which is a common text file.

---
The DefinitionFile object represents a shared parameter file which is a common text file.

## Format

The shared parameter definition file is a text file (.txt) with three blocks: META, GROUP and PARAM. The GROUP and PARAM blocks are relevant to the shared parameter functionality in the Revit API. Do not edit the definition file directly; instead, edit it using the UI or the API.

Although the Revit API takes care of reading and writing this file, the following section provides information the format of the file, which closely corresponds to the API objects and methods used to access shared parameters. The file uses tabs to separate fields and can be difficult to read in a text editor. The code region below shows the contents of a sample shared parameter text file.

<table summary="" id="GUID-9C7F6E02-05C2-4F72-8108-60F2175FB9E3__TABLE_4C1829695A954DB2A85684E526336D06"><tbody><tr><td><b>Code Region 22-1: Parameter definition file example</b></td></tr><tr><td><pre><code><span># This is a Revit shared parameter file.</span><span>
</span><span># Do not edit manually.</span><span>
</span><span>*</span><span>META    VERSION    MINVERSION
META    </span><span>2</span><span>    </span><span>1</span><span>
</span><span>*</span><span>GROUP    ID    NAME
GROUP    </span><span>1</span><span>    </span><span>MyGroup</span><span>
GROUP    </span><span>2</span><span>    </span><span>AnotherGroup</span><span>
</span><span>*</span><span>PARAM    GUID    NAME    DATATYPE    DATACATEGORY    GROUP    VISIBLE    DESCRIPTION    USERMODIFIABLE
PARAM    bb7f0005</span><span>-</span><span>9692</span><span>-</span><span>4b76</span><span>-</span><span>8fa3</span><span>-</span><span>30cec8aecf74</span><span>    </span><span>Price</span><span>    INTEGER        </span><span>2</span><span>    </span><span>1</span><span>    </span><span>Enter</span><span> price </span><span>in</span><span> USD    </span><span>1</span><span>
PARAM    b7ea2654</span><span>-</span><span>b206</span><span>-</span><span>4694</span><span>-</span><span>a087</span><span>-</span><span>756359b52e7f</span><span>    areaTags    FAMILYTYPE    </span><span>-</span><span>2005020</span><span>    </span><span>1</span><span>    </span><span>1</span><span>        </span><span>1</span><span>
PARAM    d1a5439d</span><span>-</span><span>dc8d</span><span>-</span><span>4053</span><span>-</span><span>99fa</span><span>-</span><span>2f33804bae0e</span><span>    </span><span>MyParam</span><span>    TEXT        </span><span>1</span><span>    </span><span>1</span><span>        </span><span>1</span></code></pre></td></tr></tbody></table>

-   The GROUP block contains group entries that associate every parameter definition with a group. The following fields appear in the GROUP block:
    
    -   ID - Uniquely identifies the group and associates the parameter definition with a group.
    -   Name - The group name displayed in the UI.
-   The PARAM block contains parameter definitions. The following fields appear in the PARAM block:
    
    -   GUID - Identifies the parameter definition.
        
    -   NAME - Parameter definition name.
        
    -   DATATYPE - Parameter type. This field can be a common type (TEXT, INTEGER, etc.), structural type (FORCE, MOMENT, etc.) or common family type (Area Tags, etc). Common type and structural type parameters are specified in the text file directly (e.g.: TEXT, FORCE). If the value of the DATATYPE field is FAMILYTYPE, an extra number is added. For example, FAMILYTYPE followed by -2005020 represents Family type: Area Tags.
        
    -   DATACATEGORY - An optional field for parameters whose DATATYPE is FAMILYTYPE.
        
    -   GROUP - A group ID used to identify the group that includes the current parameter definition.
        
    -   VISIBLE - Identifies whether the parameter is visible. The value of this field is 0 or 1.0 = invisible
        
        1 = visible
        
    -   DESCRIPTION - An optional field for a tooltip for this parameter.
        
    -   USERMODIFIABLE - Identifies whether the parameter is editable by the user.0 = user cannot edit the parameter and it is greyed out in the UI
        
        1 = user can edit the parameter value in the UI
        

In the sample definition file, there are two groups:

-   MyGroup - ID 1 - Contains the parameter definition for MyParam which is a Text type parameter, and the definition for areaTags which is a FamilyType parameter.
-   AnotherGroup - ID 2 - Contains the parameter definition for Price which is an Integer type parameter.

Of the 3 parameters in the sample file, only Price has a description. All of the parameters are visible and user modifiable.


<!-- ===== END: Help  Definition File  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Working with the Definition File  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:34 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_Working_with_the_Definition_File_html
author: 
---

# Help | Working with the Definition File | Autodesk

> ## Excerpt
> The definition file provides access to shared parameters.

---
The definition file provides access to shared parameters.

## Accessing parameters in the definition file

Use the following steps to gain access to the definition file and its parameters:

1.  Specify the Application.SharedParametersFilename property with an existing text file or a new one.
2.  Open the shared parameters file, using the Application.OpenSharedParameterFile() method.
3.  Open an existing group or create a new group using the DefinitionFile.Groups property.
4.  Open an existing external parameter definition or create a new definition using the DefinitionGroup.Definitions property.

The following classes and methods in the Autodesk.Revit.DB namespace provide access to shared parameters using the Revit API.

-   DefinitionFile Class
    -   Retrieved using the Application.OpenSharedParameterFile() method. Revit uses one shared parameter file at a time.
    -   Represents one shared parameter file.
    -   Contains a number of Group objects.
    -   Shared parameters are grouped for easy management and contain shared parameter definitions.
    -   New definitions can be added as needed.
-   ExternalDefinition Class
    -   The ExternalDefinition object is created by a DefinitionGroup object from a shared parameter file.
    -   External parameter definitions must belong to a Group which is a collection of shared parameter definitions.
-   Application.SharedParametersFilename Property
    -   Get and set the shared parameter file path using this property.
    -   By default, Revit does not have a shared parameter file.
    -   Initialize this property before using. If it is not initialized, an exception is thrown.
        
        ### Create a Shared Parameter File
        

Because the definition file is a text file, it can be created manually or using code.

<table summary="" id="GUID-C6FAC918-DC11-41B6-94FD-F745C3C00D98__TABLE_0D36FD6D39C342238FAF2997C6DF7514"><tbody><tr><td><b>Code Region 22-3: Creating a shared parameter file</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateExternalSharedParamFile</span><span>(</span><span>string</span><span> sharedParameterFile</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>System</span><span>.</span><span>IO</span><span>.</span><span>FileStream</span><span> fileStream </span><span>=</span><span> </span><span>System</span><span>.</span><span>IO</span><span>.</span><span>File</span><span>.</span><span>Create</span><span>(</span><span>sharedParameterFile</span><span>);</span><span>
        fileStream</span><span>.</span><span>Close</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Access an Existing Shared Parameter File

Since Revit can have many shared parameter files, it is necessary to specifically identify the file and external parameters you want to access. The following two procedures illustrate how to access an existing shared parameter file.

#### Get DefinitionFile from an External Parameter File

Set the shared parameter file path as the following code illustrates, then invoke the Application.OpenSharedParameterFile() method.

<table summary="" id="GUID-C6FAC918-DC11-41B6-94FD-F745C3C00D98__TABLE_B6089AE38BBA40969BC78F2E23CD9C45"><tbody><tr><td><b>Code Region 22-4: Getting the definition file from an external parameter file</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>DefinitionFile</span><span> </span><span>SetAndOpenExternalSharedParamFile</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>string</span><span> sharedParameterFile</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// set the path of shared parameter file to current Revit</span><span>
    application</span><span>.</span><span>SharedParametersFilename</span><span> </span><span>=</span><span> sharedParameterFile</span><span>;</span><span>
    </span><span>// open the file</span><span>
    </span><span>return</span><span> application</span><span>.</span><span>OpenSharedParameterFile</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: Consider the following points when you set the shared parameter path:

-   During each installation, Revit cannot detect whether the shared parameter file was set in other versions. You must bind the shared parameter file for the new Revit installation again.
-   If Application.SharedParametersFilename is set to an invalid path, an exception is thrown only when OpenSharedParameterFile() is called.
-   Revit can work with multiple shared parameter files. Even though only one parameter file is used when loading a parameter, the current file can be changed freely.
    
    #### Traverse All Parameter Entries
    

The following sample illustrates how to traverse the parameter entries and display the results in a message box.

<table summary="" id="GUID-C6FAC918-DC11-41B6-94FD-F745C3C00D98__TABLE_674A9F985BA149489A6F2961C045BDA2"><tbody><tr><td><b>Code Region 22-5: Traversing parameter entries</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ShowDefinitionFileInfo</span><span>(</span><span>DefinitionFile</span><span> myDefinitionFile</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>StringBuilder</span><span> fileInformation </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>(</span><span>500</span><span>);</span><span>

    </span><span>// get the file name </span><span>
    fileInformation</span><span>.</span><span>AppendLine</span><span>(</span><span>"File Name: "</span><span> </span><span>+</span><span> myDefinitionFile</span><span>.</span><span>Filename</span><span>);</span><span>

    </span><span>// iterate the Definition groups of this file</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>DefinitionGroup</span><span> myGroup </span><span>in</span><span> myDefinitionFile</span><span>.</span><span>Groups</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// get the group name</span><span>
        fileInformation</span><span>.</span><span>AppendLine</span><span>(</span><span>"Group Name: "</span><span> </span><span>+</span><span> myGroup</span><span>.</span><span>Name</span><span>);</span><span>

        </span><span>// iterate the difinitions</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Definition</span><span> definition </span><span>in</span><span> myGroup</span><span>.</span><span>Definitions</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// get definition name</span><span>
            fileInformation</span><span>.</span><span>AppendLine</span><span>(</span><span>"Definition Name: "</span><span> </span><span>+</span><span> definition</span><span>.</span><span>Name</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>fileInformation</span><span>.</span><span>ToString</span><span>());</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Change the Parameter Definition Owner Group

The following sample shows how to change the parameter definition group owner.

<table summary="" id="GUID-C6FAC918-DC11-41B6-94FD-F745C3C00D98__TABLE_74AFDA7C512E4465857DFBEC26F63D3D"><tbody><tr><td><b>Code Region 22-6: Changing parameter definition group owner</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ReadEditExternalParam</span><span>(</span><span>DefinitionFile</span><span> file</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// get ExternalDefinition from shared parameter file</span><span>
    </span><span>DefinitionGroups</span><span> myGroups </span><span>=</span><span> file</span><span>.</span><span>Groups</span><span>;</span><span>
    </span><span>DefinitionGroup</span><span> myGroup </span><span>=</span><span> myGroups</span><span>.</span><span>get_Item</span><span>(</span><span>"MyGroup"</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>myGroup </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>ExternalDefinition</span><span> myExtDef </span><span>=</span><span> myGroup</span><span>.</span><span>Definitions</span><span>.</span><span>get_Item</span><span>(</span><span>"MyParam"</span><span>)</span><span> </span><span>as</span><span> </span><span>ExternalDefinition</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>myExtDef </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>DefinitionGroup</span><span> newGroup </span><span>=</span><span> myGroups</span><span>.</span><span>get_Item</span><span>(</span><span>"AnotherGroup"</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>newGroup </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// change the OwnerGroup of the ExternalDefinition</span><span>
                myExtDef</span><span>.</span><span>OwnerGroup</span><span> </span><span>=</span><span> newGroup</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Working with the Definition File  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Binding  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_Binding_html
author: 
---

# Help | Binding | Autodesk

> ## Excerpt
> Binding is what ties shared parameters to elements in certain categories in the model.

---
Binding is what ties shared parameters to elements in certain categories in the model.

There are two types of binding available, Instance binding and Type binding. The key difference between the two is that the instance bound parameters appear on all instances of the elements in those categories. Changing the parameter on one does not affect the other instances of the parameter. The Type bound parameters appear only on the type object and is shared by all the instances that use that type. Changing the type bound parameter affects all instances of the elements that use that type. Note, a definition can only be bound to an instance or a type and not both.

To bind a parameter:

1.  Use an InstanceBinding or a TypeBinding object to create a new Binding object that includes the categories to which the parameter is bound.
2.  Add the binding and definition to the document using the BindingMap object available from the Document.ParameterBindings property.

The following class and method in the Autodesk.Revit.DB namespace provide more information on binding parameters to elements.

-   BindingMap Class
    -   Retrieved from the Document.ParameterBindings property.
    -   Parameter binding connects a parameter definition to elements within one or more categories.
    -   The map is used to interrogate existing bindings as well as generate new parameter bindings using the Insert method.
-   BindingMap.Insert() Method
    -   The binding object type dictates whether the parameter is bound to all instances or just types.
    -   A parameter definition cannot be bound to both instances and types.
    -   If the parameter binding exists, the method returns false.

### Type Binding

The TypeBinding objects are used to bind a property to a Revit type, such as a wall type. It differs from Instance bindings in that the property is shared by all instances identified in type binding. Changing the parameter for one type affects all instances of the same type.

The following code sample demonstrates how to add parameter definitions using a shared parameter file. The following code performs the same actions as using the dialog box in the Revit UI. Parameter definitions are created in the following order:

1.  A shared parameter file is created.
2.  A definition group and a parameter definition are created for the Walls type.
3.  The definition is bound to the wall type parameter in the current document based on the wall category.

#### Code Region 22-7: Adding type parameter definitions using a shared parameter file

```
public bool SetNewParameterToTypeWall(UIApplication app, DefinitionFile myDefinitionFile)
{
    // Create a new group in the shared parameters file
    DefinitionGroups myGroups = myDefinitionFile.Groups;
    DefinitionGroup myGroup = myGroups.Create("MyParameters");

    // Create a type definition
    ExternalDefinitionCreationOptions option = new ExternalDefinitionCreationOptions("CompanyName", SpecTypeId.String.Text);
    Definition myDefinition_CompanyName = myGroup.Definitions.Create(option);

    // Create a category set and insert category of wall to it
    CategorySet myCategories = app.Application.Create.NewCategorySet();
    // Use BuiltInCategory to get category of wall
    Category myCategory = Category.GetCategory(app.ActiveUIDocument.Document, BuiltInCategory.OST_Walls);

    myCategories.Insert(myCategory);

    //Create an object of TypeBinding according to the Categories
    TypeBinding typeBinding = app.Application.Create.NewTypeBinding(myCategories);

    // Get the BingdingMap of current document.
    BindingMap bindingMap = app.ActiveUIDocument.Document.ParameterBindings;

    // Bind the definitions to the document
    bool typeBindOK = bindingMap.Insert(myDefinition_CompanyName, typeBinding,
        BuiltInParameterGroup.PG_TEXT);
    return typeBindOK;
}  
```

### Instance Binding

The InstanceBinding object indicates binding between a parameter definition and a parameter in certain category instances.

Once bound, the parameter appears in all property dialog boxes for the instance (if the visible property is set to true). Changing the parameter in any one instance does not change the value in any other instance.

The following code sample demonstrates how to add parameter definitions using a shared parameter file. Parameter definitions are added in the following order:

1.  A shared parameter file is created
2.  A definition group and a definition for all Walls instances is created
3.  Definitions are bound to each wall instance parameter in the current document based on the wall category.

#### Code Region 22-8: Adding instance parameter definitions using a shared parameter file

```
public bool SetNewParameterToInstanceWall(UIApplication app, DefinitionFile myDefinitionFile)
    {
        // create a new group in the shared parameters file
        DefinitionGroups myGroups = myDefinitionFile.Groups;
        DefinitionGroup myGroup = myGroups.Create("MyParameters1");

        // create an instance definition in definition group MyParameters
        ExternalDefinitionCreationOptions option = new ExternalDefinitionCreationOptions("Instance_ProductDate", SpecTypeId.String.Text);
        // Don't let the user modify the value, only the API
        option.UserModifiable = false;
        // Set tooltip
        option.Description = "Wall product date";
        Definition myDefinition_ProductDate = myGroup.Definitions.Create(option);

        // create a category set and insert category of wall to it
        CategorySet myCategories = app.Application.Create.NewCategorySet();
        // use BuiltInCategory to get category of wall
        Category myCategory = Category.GetCategory(app.ActiveUIDocument.Document, BuiltInCategory.OST_Walls);

        myCategories.Insert(myCategory);

        //Create an instance of InstanceBinding
        InstanceBinding instanceBinding = app.Application.Create.NewInstanceBinding(myCategories);

        // Get the BingdingMap of current document.
        BindingMap bindingMap = app.ActiveUIDocument.Document.ParameterBindings;

        // Bind the definitions to the document
        bool instanceBindOK = bindingMap.Insert(myDefinition_ProductDate,
                                        instanceBinding, BuiltInParameterGroup.PG_TEXT);
        return instanceBindOK;
    }
```


<!-- ===== END: Help  Binding  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  SharedParameterElement  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:43 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_SharedParameterElement_html
author: 
---

# Help | SharedParameterElement | Autodesk

> ## Excerpt
> SharedParameterElements store information about a particular user-defined shared parameter in the document

---
SharedParameterElements store information about a particular user-defined shared parameter in the document

User-defined parameters are stored in the document and represented by the ParameterElement class. The subclass SharedParameterElement represents a shared parameter loaded into the document. ParemeterElement is also the base class for GlobalParameter.

Once a shared parameter has been loaded into a document, information about it can be retrieved from the SharedParameterElement class. SharedParameterElement inherits the GetDefinition() method from the parent ParameterElement class. GetDefinition() returns the InternalDefinition that represents the definition for the parameter in the document, as opposed to the ExternalDefinition for a shared parameter that is stored in the shared parameter file. SharedParameterElement also provides access to the Guid that identifies the shared parameter via the GuidValue property.

The static Create() method on this class can create a new SharedParameterElement in the document from an ExternalDefinition.

The static Lookup() method can retrieve a SharedParameterElement from a given Guid.

In the following example, a schedule contains a field representing the value of a shared parameter. The definition for the shared parameter is retrieved from the SharedParameterElement.

<table summary="" id="GUID-B8342E8A-CFF1-4670-B85F-6F952DE993B8__TABLE_0D36FD6D39C342238FAF2997C6DF7514"><tbody><tr><td><b>Code Region: Getting the definition of a shared parameter</b></td></tr><tr><td><pre><code><span>// Check if a given shared parameter in a schedule can vary across groups</span><span>
</span><span>public</span><span> </span><span>bool</span><span> </span><span>CanParamVaryAcrossGroups</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>string</span><span> sharedParamName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> variesAcrossGroups </span><span>=</span><span> </span><span>false</span><span>;</span><span>

    </span><span>int</span><span> numFields </span><span>=</span><span>  schedule</span><span>.</span><span>Definition</span><span>.</span><span>GetFieldCount</span><span>();</span><span>
    </span><span>// Find the field with the given name</span><span>
    </span><span>for</span><span> </span><span>(</span><span>int</span><span> i </span><span>=</span><span> </span><span>0</span><span>;</span><span> i </span><span>&lt;</span><span> numFields</span><span>;</span><span> i</span><span>++)</span><span>
       </span><span>{</span><span>
              </span><span>ScheduleField</span><span> field </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>.</span><span>GetField</span><span>(</span><span>i</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>field</span><span>.</span><span>GetName</span><span>().</span><span>Contains</span><span>(</span><span>sharedParamName</span><span>))</span><span>
        </span><span>{</span><span>
            </span><span>// Get the SharedParameterElement from the field's parameter id</span><span>
            </span><span>SharedParameterElement</span><span> spe </span><span>=</span><span> schedule</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>field</span><span>.</span><span>ParameterId</span><span>)</span><span> </span><span>as</span><span> </span><span>SharedParameterElement</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>spe </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>InternalDefinition</span><span> definition </span><span>=</span><span> spe</span><span>.</span><span>GetDefinition</span><span>();</span><span>
                variesAcrossGroups </span><span>=</span><span> definition</span><span>.</span><span>VariesAcrossGroups</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
       </span><span>}</span><span>

    </span><span>return</span><span> variesAcrossGroups</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

SharedParameterElements are especially useful when working with [RebarContainers](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Rebar_Containers_html "Rebar Containers are elements which represent an aggregation of rebars in one host. This element can only be created via the API."). A shared parameter can be added as an override to the parameters manager for a RebarContainer. The shared parameter does not need to be bound to any categories to be added as an override. The following example adds a given shared parameter as an override to a RebarContainer.

<table summary="" id="GUID-B8342E8A-CFF1-4670-B85F-6F952DE993B8__TABLE_7439F7FF5ED14855B13B4FB4831915E0"><tbody><tr><td><b>Code Region: Using a SharedParameterElement as an override for a RebarContainer</b></td></tr><tr><td><pre><code><span>// Find the named shared parameter and add it as an override to the parameter manger for the given RebarContainer</span><span>
</span><span>void</span><span> </span><span>AddSharedParameterOverride</span><span>(</span><span>RebarContainer</span><span> container</span><span>,</span><span> </span><span>string</span><span> sharedParamName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// find the shared parameter guid</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>container</span><span>.</span><span>Document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>SharedParameterElement</span><span>));</span><span>
    </span><span>IEnumerable</span><span>&lt;</span><span>SharedParameterElement</span><span>&gt;</span><span> paramCollector </span><span>=</span><span> collector</span><span>.</span><span>Cast</span><span>&lt;</span><span>SharedParameterElement</span><span>&gt;();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>SharedParameterElement</span><span> spe </span><span>in</span><span> paramCollector</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>spe</span><span>.</span><span>Name</span><span>.</span><span>CompareTo</span><span>(</span><span>sharedParamName</span><span>)</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>RebarContainerParameterManager</span><span> paramManager </span><span>=</span><span> container</span><span>.</span><span>GetParametersManager</span><span>();</span><span>
            paramManager</span><span>.</span><span>AddSharedParameterAsOverride</span><span>(</span><span>spe</span><span>.</span><span>Id</span><span>);</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  SharedParameterElement  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Global Parameters  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:49 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_html
author: 
---

# Help | Global Parameters | Autodesk

> ## Excerpt
> Global parameters support controlling geometry constraints through special parameters defined in a project document.

---
Global parameters support controlling geometry constraints through special parameters defined in a project document.

Global Parameters can be used for both labeling and reporting to/from dimensions, as well as setting values of instance parameters. They can be used to drive values of dimensions or other elements' parameters and they can be driven by a selected dimension, the value of which then determines the value of the global parameter.

**Pages in this section**

-   [Managing Global Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Managing_Global_Parameters_html)
-   [GlobalParameter Basics](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_GlobalParameter_Basics_html)
-   [Reporting vs. Non-Reporting parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Reporting_vs_Non_Reporting_parameters_html)
-   [Formulas and Global Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Formulas_and_Global_Parameters_html)
-   [Labeling Dimensions with Global Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Labeling_Dimensions_with_Global_Parameters_html)

**Parent page:** [Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_html)


<!-- ===== END: Help  Global Parameters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Managing Global Parameters  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:53 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Managing_Global_Parameters_html
author: 
---

# Help | Managing Global Parameters | Autodesk

> ## Excerpt
> The GlobalParametersManager class provides access to general information and data of Global Parameter elements in a particular model.

---
The GlobalParametersManager class provides access to general information and data of Global Parameter elements in a particular model.

GlobalParametersManager provides the main access point to managing global parameters in a project document. It provides static methods to access and reorder global parameters and to test for name uniqueness and Id validity.

## Accessing global parameters

Global parameters are only supported in project documents, not family documents. Even with a project document, however, global parameters may be disallowed under certain circumstances, either temporarily or permanently. The AreGlobalParametersAllowed() method will indicate whether global parameters are allowed within a specified document.

If global parameters are allowed in a project document, use the methods GetAllGlobalParameters() to get all global parameters in a specified document, or GetGlobalParametersOrdered() to get an ordered list of the global parameters. When retrieving an ordered list, the order of the items corresponds to the order in which global parameters appear in the standard Global Parameters dialog in the Revit user interface.

To get a global parameter by name, call FindByName(), which will return the ElementId of the named global parameter, or ElementId.InvalidElementId if no global parameter is found with the given name. Since global parameter names must be unique, the IsUniqueName() method should be called to check a name prior to creating a new GlobalParameter.

Given an ElementId for a GlobalParameter, the IsValidGlobalParameter() will confirm that the given ElementId is a valid global parameter id.

The following example demonstrates how to get all global parameters, if global parameters are allowed in the document.

<table summary="" id="GUID-9FDC35A5-C054-46CA-B2DC-E20958FD197F__TABLE_0D36FD6D39C342238FAF2997C6DF7514"><tbody><tr><td><b>Code Region: Getting global parameters</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Returns all global parameter elements defined in the given document. </span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>/// &lt;param name="document"&gt;Revit project document.&lt;/param&gt;</span><span>
</span><span>/// &lt;returns&gt;A set of ElementIds of global parameter elements&lt;/returns&gt;</span><span>
</span><span>public</span><span> </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> </span><span>GetAllGlobalParameters</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Global parameters are not available in all documents.</span><span>
    </span><span>// They are available in projects, but not in families.</span><span>
    </span><span>if</span><span> </span><span>(</span><span>GlobalParametersManager</span><span>.</span><span>AreGlobalParametersAllowed</span><span>(</span><span>document</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> </span><span>GlobalParametersManager</span><span>.</span><span>GetAllGlobalParameters</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// return an empty set if global parameters are not available in the document</span><span>
    </span><span>return</span><span> </span><span>new</span><span> </span><span>HashSet</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Reordering global parameters

GlobalParametersManager provides methods to change the given order of the global parameters in the project document. These operations have no effect on the global parameters themselves. The rearranged order is only visible in the standard Global Parameters dialog in Revit and reflected in the GetGlobalParametersOrdered() method.

-   SortParameters() - sorts the global parameters in either ascending or descending alphabetical order, but only within the range of their respective parameter group.
-   MoveParameterDownOrder() - moves a given parameter down in the current order.
-   MoveParameterUpOrder() - moves the given parameter up in the current order. A parameter can only be moved within its parameter group, so if a parameter can no longer move because it is at the boundary of its group, the MoveParameter methods will return False.


<!-- ===== END: Help  Managing Global Parameters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  GlobalParameter Basics  Autodesk.md ===== -->

---
created: 2026-01-28T20:49:58 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_GlobalParameter_Basics_html
author: 
---

# Help | GlobalParameter Basics | Autodesk

> ## Excerpt
> The GlobalParameter class represents a global parameter in a project document and can be used to create and modify global parameters.

---
The GlobalParameter class represents a global parameter in a project document and can be used to create and modify global parameters.

## Creating global parameters

Global parameters may be created only in project documents, not in families. Global parameters are created via the static Create() method in a given document, with a given name and SpecTypeId. Each new parameter must have a name that is unique within the document, which can be determined using the static GlobalParametersManager.IsUniqueName() method. Global parameters can be created with almost any type of data, but there are a few types that are not currently supported, such as the ElementId type. Test whether a particular data type is appropriate for a global parameter by using the static SpecUtils.IsSpec() method.

Parameters are created as non-reporting initially, but can be changed after creation using the IsReporting property if the global parameter is of an eligible type. See the [Reporting vs. Non-Reporting Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Reporting_vs_Non_Reporting_parameters_html "The most significant difference in types of global parameters is whether they are reporting or non-reporting.") page for more information.

<table summary="" id="GUID-24FE1FF0-A13C-4053-802A-72E4C77FD752__TABLE_E2A463303AAA4F09B5BAB775B1171CEF"><tbody><tr><td><b>Code Region: Create a new global parameter</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Creates a new Global Parameter of type Length, assigns it an initial value,</span><span>
</span><span>/// and uses it to label a set of input dimension elements.</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>/// &lt;param name="document"&gt;Revit project document in which to create the parameter.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="name"&gt;Name of the global parameter to create.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="value"&gt;A value the new global parameter is to have.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="dimensionsToLabel"&gt;A set of dimension to labe by the new global parameter.&lt;/param&gt;</span><span>
</span><span>/// &lt;returns&gt;ElementId of the new GlobalParameter&lt;/returns&gt;</span><span>
</span><span>public</span><span> </span><span>ElementId</span><span> </span><span>CreateNewGlobalParameter</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>String</span><span> name</span><span>,</span><span> </span><span>double</span><span> value</span><span>,</span><span> </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> dimensionsToLabel</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>GlobalParametersManager</span><span>.</span><span>AreGlobalParametersAllowed</span><span>(</span><span>document</span><span>))</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>InvalidOperationException</span><span>(</span><span>"Global parameters are not permitted in the given document"</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(!</span><span>GlobalParametersManager</span><span>.</span><span>IsUniqueName</span><span>(</span><span>document</span><span>,</span><span> name</span><span>))</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>ArgumentException</span><span>(</span><span>"Global parameter with such name already exists in the document"</span><span>,</span><span> </span><span>"name"</span><span>);</span><span>

    </span><span>ElementId</span><span> gpid </span><span>=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>;</span><span>

    </span><span>// creation of any element must be in a transaction</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Create Global Parameter"</span><span>))</span><span>
    </span><span>{</span><span>
        trans</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// create a GP with the given name and type Length</span><span>
        </span><span>GlobalParameter</span><span> gp </span><span>=</span><span> </span><span>GlobalParameter</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> name</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>Length</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>gp </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// if created successfully, assign it a value</span><span>
            </span><span>// note: parameters of type Length accept Double values</span><span>
            gp</span><span>.</span><span>SetValue</span><span>(</span><span>new</span><span> </span><span>DoubleParameterValue</span><span>(</span><span>value</span><span>));</span><span>

            </span><span>// if a collection of dimensions was given, label them with this new parameter</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> elemid </span><span>in</span><span> dimensionsToLabel</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// not just any dimension is allowed to be labeled</span><span>
                </span><span>// check first to avoid exceptions</span><span>
                </span><span>if</span><span> </span><span>(</span><span>gp</span><span>.</span><span>CanLabelDimension</span><span>(</span><span>elemid</span><span>))</span><span>
                </span><span>{</span><span>
                    gp</span><span>.</span><span>LabelDimension</span><span>(</span><span>elemid</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>

            gpid </span><span>=</span><span> gp</span><span>.</span><span>Id</span><span>;</span><span>
        </span><span>}</span><span>
        trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> gpid</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Getting and setting the value of a global parameter

All global parameters, formula-driven, dimension-driven, or independent, have values. A value can be obtained by calling the GetValue() method. The object returned by that method is an instance of one of the classes derived from the ParameterValue class:

-   IntegerParameterValue
-   DoubleParameterValue
-   StringParameterValue

All the derived classes have only one property, Value, which gets or sets the value as the corresponding type.

The concrete instance is determined by the type of the global parameter which was specified upon creation. Parameters that are neither formula-driven nor dimension-driven (reporting) can have a value assigned. The method to use is SetValue() and it accepts the same type of ParameterValue that is returned by GetValue(). However, the type can also be deduced easily: **Text** parameters accept only StringParameterValue. **Integer** and **YesNo** parameters accept only IntegerParameterValue. All other parameters accept only DoubleParameterValue.

## Elements affected by a global parameter

Global parameters can be associated with other global parameters as well as regular family instance parameters (which may report global parameters as their values via the assignment formula.) There are two methods available to find relations among parameters: GlobalParameter.GetAffectedGlobalParameters() and GlobalParameter.GetAffectedElements(). The former returns all other global parameters that refer to a particular global parameter in their respective formulas. The latter method returns a set of all elements of which some parameters are controlled by the global parameter. These two methods together with the GlobalParameter.GetLabeledDimensions() can help determine out how model elements relate to each other via global parameters.

Methods for maintaining associations between element properties and global parameters can be found in the [Parameter](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Parameter_html "The Parameter class contains the value for the given parameter.") class.


<!-- ===== END: Help  GlobalParameter Basics  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Reporting vs. Non-Reporting parameters  Autodesk.md ===== -->

---
created: 2026-01-28T20:50:03 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Reporting_vs_Non_Reporting_parameters_html
author: 
---

# Help | Reporting vs. Non-Reporting parameters | Autodesk

> ## Excerpt
> The most significant difference in types of global parameters is whether they are reporting or non-reporting.

---
The most significant difference in types of global parameters is whether they are reporting or non-reporting.

## What are reporting and non-reporting parameters?

There are several ways global parameters can be categorized, but probably the most significant categorization stems from the GlobalParameter.IsReporting property which divides global parameters into two groups - Reporting and Non-Reporting. The significance of reporting parameters lays in the fact that their values are driven by the dimension that has been labeled by a reporting parameter. It means that the value of a reporting parameter reflects the value of a dimension (length or angle) and gets updated anytime the dimension changes. Non-Reporting parameters behave in the opposite manner - they drive value of dimensions that have been labeled by them, which results in controlling the model's geometry through global parameters' values.

Reporting parameters are limited in several ways. They can be only of **Length** or **Angle** type, a requirement due to the fact that a dimension must be able to drive the value. For the same reason reporting parameters may not have formulas.

Non-Reporting parameters, on the other way, can be of almost any type (**Length**, **Integer**, **Area**, etc.) with the exception of ElementId type. Also, Non-Reporting parameters may have assigned formulas in which other global parameters may be used as arguments. This way one global parameter's value can be derived from other parameter (or parameters), and the other parameter can be either reporting or non-reporting.

Other important properties of global parameters are IsDrivenByDimension and IsDrivenByFormula, which are mutually exclusive - a parameter that has a formula assigned cannot be driven by a dimension (nor can be reporting) and vice versa.

## Making a global parameter reporting or non-reporting

Global parameters are initially non-reporting upon creation, but can be set to reporting use the GlobalParameter.IsReporting property once a global parameter is created and is of an eligible type. Use GlobalParameter.HasValidTypeForReporting() to ensure that a certain data type can be made reporting. Note, that a parameter may not be made reporting after more than one dimension has been labeled by it. It is because reporting parameters can label (and be driven) by one dimension only.

An alternative way of making a parameter reporting is via the GlobalParameter.SetDrivingDimension() method which labels one dimension by a global parameter and also makes the parameter reporting if it is not reporting yet.

Although parameters driven by a dimension are automatically made reporting, parameters driven by a formula are not. In order to set a formula, the global parameter must be non-reporting. Therefore a reporting parameter must be changed to non-reporting first before assigning a formula.


<!-- ===== END: Help  Reporting vs. Non-Reporting parameters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Formulas and Global Parameters  Autodesk.md ===== -->

---
created: 2026-01-28T20:50:07 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Formulas_and_Global_Parameters_html
author: 
---

# Help | Formulas and Global Parameters | Autodesk

> ## Excerpt
> Formulas may be assigned to non-reporting parameters.

---
Formulas may be assigned to non-reporting parameters.

As with family parameters, formulas may be assigned to global parameters using the GlobalParameter.SetFormula() method. Since a global parameter must be non-reporting to set a formula, a reporting parameter must be changed to non-reporting prior to assigning a formula.

Value of the evaluated formula must be compatible with the value-type of the parameter. For example, it is permitted to use **Integer** parameters in a formula assigned to a Double ( **Number**) parameter, or vice versa. It is not allowed, however, to use **Length** or **Angle** arguments in a formula in a parameter whose type is ether **Integer** or **Number**.

Formulas may include all standard arithmetic operations and logical operations (as functions **and**, **or**, **not**.) Input to logical operations must be Boolean values (parameters of YesNo type). Consequently, arithmetic operations can be applied to numeric values only. While there are no operations supported for string (text) arguments, strings can be used as results of a logical **If** operation. Depending on their type (and units), parameters of different value types can be combined. However, unit-less values such as **Integer** and **Number** (double) may only be combined with each other.

Since formulas can get quite complicated, and since some formulas cannot be assigned to certain parameters, the method IsValidFormula() can be used to test whether a formula is valid for a global parameter. If SetFormula() is called with an invalid formula for the global parameter, an Exception will be thrown.

GetFormula() will return the current formula in the form of a string.

The following code sample creates four global parameters and then sets a formula to one so that it has a value of either of two other parameters depending on the boolean value of the fourth one.

<table summary="" id="GUID-2B4E911F-30B2-49D4-830B-880814F3753A__TABLE_A9CB38B47E414A8E8C0BF70AA9BB2F44"><tbody><tr><td><b>Code Region: Setting a formula</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SetCombinationParameters</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>GlobalParameter</span><span> gpB </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>GlobalParameter</span><span> gpT </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>GlobalParameter</span><span> gpF </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>GlobalParameter</span><span> gpX </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>int</span><span> TRUE </span><span>=</span><span> </span><span>1</span><span>;</span><span>
    </span><span>int</span><span> FALSE </span><span>=</span><span> </span><span>0</span><span>;</span><span>

    </span><span>// transaction to create global parameters and set their values</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Creating global parameters"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>// create 4 new global parameters</span><span>

        trans</span><span>.</span><span>Start</span><span>();</span><span>

        gpB </span><span>=</span><span> </span><span>GlobalParameter</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"GPB"</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>Boolean</span><span>.</span><span>YesNo</span><span>);</span><span>
        gpT </span><span>=</span><span> </span><span>GlobalParameter</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"GPT"</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>String</span><span>.</span><span>Text</span><span>);</span><span>
        gpF </span><span>=</span><span> </span><span>GlobalParameter</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"GPF"</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>String</span><span>.</span><span>Text</span><span>);</span><span>
        gpX </span><span>=</span><span> </span><span>GlobalParameter</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"GPX"</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>String</span><span>.</span><span>Text</span><span>);</span><span>

        </span><span>// assign initial values and a formula to the global parameters</span><span>

        gpB</span><span>.</span><span>SetValue</span><span>(</span><span>new</span><span> </span><span>IntegerParameterValue</span><span>(</span><span>TRUE</span><span>));</span><span>
        gpT</span><span>.</span><span>SetValue</span><span>(</span><span>new</span><span> </span><span>StringParameterValue</span><span>(</span><span>"TypeA"</span><span>));</span><span>
        gpF</span><span>.</span><span>SetValue</span><span>(</span><span>new</span><span> </span><span>StringParameterValue</span><span>(</span><span>"TypeB"</span><span>));</span><span>

        </span><span>// Set the formula to GPX so that its final value is either the value of GPT (TypeA)</span><span>
        </span><span>// or GPF (TypeB) depending on whether the value of GPB is True or False.</span><span>
        </span><span>// Note: in this particular case we are certain the formula is valid, but if weren't </span><span>
        </span><span>// certain, we could use a validation method as we are now going to illustrate here:</span><span>
        </span><span>string</span><span> expression </span><span>=</span><span> </span><span>"if(GPB,GPT,GPF)"</span><span>;</span><span> </span><span>// XPX &lt;== if (GPB == TRUE) then GPT else GPF</span><span>
        </span><span>if</span><span> </span><span>(</span><span>gpX</span><span>.</span><span>IsValidFormula</span><span>(</span><span>expression</span><span>))</span><span>
        </span><span>{</span><span>
            gpX</span><span>.</span><span>SetFormula</span><span>(</span><span>expression</span><span>);</span><span>  
        </span><span>}</span><span>

        trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>// we can test that the formula works</span><span>
    </span><span>// since the boolean value is TRUE, the value of the GPX parameter</span><span>
    </span><span>// should be the same as the value of the GPT parameters</span><span>

    </span><span>StringParameterValue</span><span> sTrue </span><span>=</span><span> gpT</span><span>.</span><span>GetValue</span><span>()</span><span> </span><span>as</span><span> </span><span>StringParameterValue</span><span>;</span><span>
    </span><span>StringParameterValue</span><span> sFalse </span><span>=</span><span> gpF</span><span>.</span><span>GetValue</span><span>()</span><span> </span><span>as</span><span> </span><span>StringParameterValue</span><span>;</span><span>
    </span><span>StringParameterValue</span><span> sValue </span><span>=</span><span> gpX</span><span>.</span><span>GetValue</span><span>()</span><span> </span><span>as</span><span> </span><span>StringParameterValue</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>sValue</span><span>.</span><span>Value</span><span> </span><span>!=</span><span> sTrue</span><span>.</span><span>Value</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Unexpected value of a global parameter"</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// we can also test that evaluation of the formula is affected by changes</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Change value of a YesNo parameter"</span><span>))</span><span>
    </span><span>{</span><span>
        trans</span><span>.</span><span>Start</span><span>();</span><span>
        gpB</span><span>.</span><span>SetValue</span><span>(</span><span>new</span><span> </span><span>IntegerParameterValue</span><span>(</span><span>FALSE</span><span>));</span><span>
        trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    sValue </span><span>=</span><span> gpX</span><span>.</span><span>GetValue</span><span>()</span><span> </span><span>as</span><span> </span><span>StringParameterValue</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>sValue</span><span>.</span><span>Value</span><span> </span><span>!=</span><span> sFalse</span><span>.</span><span>Value</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Unexpected value of a global parameter"</span><span>);</span><span>
    </span><span>}</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Formulas and Global Parameters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Labeling Dimensions with Global Parameters  Autodesk.md ===== -->

---
created: 2026-01-28T20:50:13 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Labeling_Dimensions_with_Global_Parameters_html
author: 
---

# Help | Labeling Dimensions with Global Parameters | Autodesk

> ## Excerpt
> A key feature of global parameters is their ability to "label" dimensions.

---
A key feature of global parameters is their ability to "label" dimensions.

When a dimension is labeled by a global parameter, then its value is either controlled by the parameter (non-reporting), or drives the value of the parameter (reporting). It is important to note that a reporting parameter can label at most one dimension object - meaning, a parameter can be driven by one dimension only. If the dimension has several segments and is labeled by a non-reporting parameter, the value of each segment will be driven by this parameter. Multi-segmented dimensions cannot be labeled by reporting parameters.

If the dimension is already labeled by another global parameter, labeling it again will automatically detach it from that parameter.

Presently, only single **Linear** and **Angular** dimensions can be labeled, but there are other restrictions in effect too. Use the CanLabelDimension() method to find out whether a particular dimension element may be labeled or not. Also, since the value of the parameter and the dimension labeled by it depend on each other, the data type of the global parameter must be either **Length** or **Angle**, since those are the only units a dimension can represent.

The following example creates a global parameter and uses it to label the set of given dimension elements.

<table summary="" id="GUID-98925277-4F65-4963-9ECD-C1CAA831E86D__TABLE_71F3FCEC973049DEA00CC8DAABDA8028"><tbody><tr><td><b>Code Region: Labeling dimensions</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>int</span><span> </span><span>DriveSelectedDimensions</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>string</span><span> name</span><span>,</span><span> </span><span>double</span><span> value</span><span>,</span><span> </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> dimset</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>GlobalParametersManager</span><span>.</span><span>AreGlobalParametersAllowed</span><span>(</span><span>document</span><span>))</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>InvalidOperationException</span><span>(</span><span>"Global parameters are not permitted in the given document"</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(!</span><span>GlobalParametersManager</span><span>.</span><span>IsUniqueName</span><span>(</span><span>document</span><span>,</span><span> name</span><span>))</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>ArgumentException</span><span>(</span><span>"Global parameter with such name already exists in the document"</span><span>,</span><span> </span><span>"name"</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>value </span><span>&lt;=</span><span> </span><span>0.0</span><span>)</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>ArgumentException</span><span>(</span><span>"Value of a global parameter that drives dimension must be a positive number"</span><span>,</span><span> </span><span>"value"</span><span>);</span><span>

    </span><span>int</span><span> nLabeledDims </span><span>=</span><span> </span><span>0</span><span>;</span><span>   </span><span>// number of labeled dimensions (for testing)</span><span>

    </span><span>// creation of any element must be in a transaction</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Create Global Parameter"</span><span>))</span><span>
    </span><span>{</span><span>
        trans</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// create a GP with the given name and type Length</span><span>
        </span><span>// Note: Length (or Angle) is required type of global parameters that are to label a dimension</span><span>
        </span><span>GlobalParameter</span><span> newgp </span><span>=</span><span> </span><span>GlobalParameter</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> name</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>Length</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>newgp </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            newgp</span><span>.</span><span>SetValue</span><span>(</span><span>new</span><span> </span><span>DoubleParameterValue</span><span>(</span><span>value</span><span>));</span><span>

            </span><span>// use the parameter to label the given dimensions</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> elemid </span><span>in</span><span> dimset</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// not just any dimension is allowed to be labeled</span><span>
                </span><span>// check first to avoid exceptions</span><span>
                </span><span>if</span><span> </span><span>(</span><span>newgp</span><span>.</span><span>CanLabelDimension</span><span>(</span><span>elemid</span><span>))</span><span>
                </span><span>{</span><span>
                    newgp</span><span>.</span><span>LabelDimension</span><span>(</span><span>elemid</span><span>);</span><span>
                    nLabeledDims </span><span>+=</span><span> </span><span>1</span><span>;</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>

            trans</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// for illustration purposes only, we'll test the results of our modifications </span><span>

    </span><span>// 1.) Check the new parameter can be found</span><span>

    </span><span>ElementId</span><span> gpid </span><span>=</span><span> </span><span>GlobalParametersManager</span><span>.</span><span>FindByName</span><span>(</span><span>document</span><span>,</span><span>name</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>gpid </span><span>==</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Failed to find a newly created global parameter"</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>GlobalParameter</span><span> gp </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>gpid</span><span>)</span><span> </span><span>as</span><span> </span><span>GlobalParameter</span><span>;</span><span>

    </span><span>// 2\. Check the number of labeled dimension is as expected</span><span>

    </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> labeledSet </span><span>=</span><span> gp</span><span>.</span><span>GetLabeledDimensions</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>labeledSet</span><span>.</span><span>Count</span><span> </span><span>!=</span><span> nLabeledDims</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Have not found all the dimension that were labeled."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> labeledSet</span><span>.</span><span>Count</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The SetDrivingDimension() method combines two actions: a) Making the parameter reporting if it is not yet, and b) Labeling the given dimension with it. Therefore, the global parameter must be eligible for reporting, and must not be used to label more than one dimensions yet. See the [Reporting vs. Non-Reporting Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Reporting_vs_Non_Reporting_parameters_html "The most significant difference in types of global parameters is whether they are reporting or non-reporting.") page for more information on reporting parameters

In case this parameter is already driven by another dimension, the other dimension will be unlabeled first before the given one is labeled. This is because a reporting parameter can only label one dimension at a time (i.e. it can be driven by one dimension only.)

The next example creates a global parameter to be driven by the value of a dimension.

<table summary="" id="GUID-98925277-4F65-4963-9ECD-C1CAA831E86D__TABLE_804DBC2F3E634F4689EE199AA86313DC"><tbody><tr><td><b>Code Region: Assign driving dimension</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>AssignDrivingDimension</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>ElementId</span><span> gpid</span><span>,</span><span> </span><span>ElementId</span><span> dimid</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// we expect to find the global parameter in the document</span><span>
    </span><span>GlobalParameter</span><span> gp </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>gpid</span><span>)</span><span> </span><span>as</span><span> </span><span>GlobalParameter</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>gp </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>return</span><span> </span><span>false</span><span>;</span><span>

    </span><span>// we expect to find the given dimension in the document</span><span>
    </span><span>Dimension</span><span> dim </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>dimid</span><span>)</span><span> </span><span>as</span><span> </span><span>Dimension</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>dim </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>return</span><span> </span><span>false</span><span>;</span><span>

    </span><span>// not every global parameter can label</span><span>
    </span><span>// and not every dimension can be labeled</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>gp</span><span>.</span><span>CanLabelDimension</span><span>(</span><span>dimid</span><span>))</span><span>
        </span><span>return</span><span> </span><span>false</span><span>;</span><span>

    </span><span>// we need a transaction to modify the model</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span>"Assign a driving dimension"</span><span>))</span><span>
    </span><span>{</span><span>
        trans</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// we cannot assign a driving dimension to a global</span><span>
        </span><span>// parameter that is already used to label other dimensions</span><span>
        </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> dimset </span><span>=</span><span> gp</span><span>.</span><span>GetLabeledDimensions</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> elemid </span><span>in</span><span> dimset</span><span>)</span><span>
        </span><span>{</span><span>
            gp</span><span>.</span><span>UnlabelDimension</span><span>(</span><span>elemid</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>// with the GP free of all previously labels (if there were any)</span><span>
        gp</span><span>.</span><span>SetDrivingDimension</span><span>(</span><span>dimid</span><span>);</span><span>

        </span><span>// we should be able to commit, but we test the result anyway</span><span>
        </span><span>if</span><span> </span><span>(</span><span>trans</span><span>.</span><span>Commit</span><span>()</span><span> </span><span>!=</span><span> </span><span>TransactionStatus</span><span>.</span><span>Committed</span><span>)</span><span>
            </span><span>return</span><span> </span><span>false</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>true</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Labeling Dimensions with Global Parameters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Collections  Autodesk.md ===== -->

---
created: 2026-01-28T20:50:17 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Collections_html
author: 
---

# Help | Collections | Autodesk

> ## Excerpt
> Most Revit Platform API properties and methods use .NET Framework collection classes when providing access to a group of related items.

---
Most Revit Platform API properties and methods use .NET Framework collection classes when providing access to a group of related items.

The IEnumerable and IEnumerator interfaces implemented in Revit collection types are defined in the System.Collection namespace.

**Pages in this section**

-   [Interface](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Collections_Interface_html)
-   [Collections and Iterators](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Collections_Collections_and_Iterators_html)

**Parent page:** [Basic Interaction with Revit Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_html)


<!-- ===== END: Help  Collections  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Interface  Autodesk.md ===== -->

---
created: 2026-01-28T20:50:22 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Collections_Interface_html
author: 
---

# Help | Interface | Autodesk

> ## Excerpt
> The following sections discuss interface-related collection types.

---
The following sections discuss interface-related collection types.

### IEnumerable

The IEnumerable interface is in the System.Collections namespace. It exposes the enumerator, which supports a simple iteration over a non-generic collection. The GetEnumerator() method gets an enumerator that implements this interface. The returned [IEnumerator](http://msdn2.microsoft.com/en-us/library/system.collections.ienumerator.aspx) object is iterated throughout the collection. The GetEnumerator() method is used implicitly by foreach loops in C#.

### IEnumerator

The IEnumerator interface is in the System.Collections namespace. It supports a simple iteration over a non-generic collection. IEnumerator is the base interface for all non-generic enumerators. The foreach statement in C# hides the enumerator's complexity.

Note: Using foreach is recommended instead of directly manipulating the enumerator.

Enumerators are used to read the collection data, but they cannot be used to modify the underlying collection. Use IEnumerator as follows:

-   Initially, the enumerator is positioned in front of the first element in the collection. However, it is a good idea to always call Reset() when you first obtain the enumerator.
    -   The Reset() method moves the enumerator back to the original position. At this position, calling the Current property throws an exception.
    -   Call the MoveNext() method to advance the enumerator to the collection's first element before reading the current iterator value.
-   The Current property returns the same object until either the MoveNext() method or Reset() method is called. The MoveNext() method sets the current iterator to the next element.
-   If MoveNext passes the end of the collection, the enumerator is positioned after the last element in the collection and MoveNext returns false.
    -   When the enumerator is in this position, subsequent calls to the MoveNext also return false.
    -   If the last call to the MoveNext returns false, calling the Current property throws an exception.
    -   To set the current iterator to the first element in the collection again, call the Reset() method followed by MoveNext().
-   An enumerator remains valid as long as the collection remains unchanged.
    -   If changes are made to the collection, such as adding, modifying, or deleting elements, the enumerator is invalidated and the next call to the MoveNext() or the Reset() method throws an InvalidOperationException.
    -   If the collection is modified between the MoveNext and the current iterator, the Current property returns to the specified element, even if the enumerator is already invalidated.

Note: All calls to the Reset() method must result in the same state for the enumerator. The preferred implementation is to move the enumerator to the collection beginning, before the first element. This invalidates the enumerator if the collection is modified after the enumerator was created, which is consistent with the MoveNext() and the Current properties.


<!-- ===== END: Help  Interface  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Collections and Iterators  Autodesk.md ===== -->

---
created: 2026-01-28T20:50:27 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Collections_Collections_and_Iterators_html
author: 
---

# Help | Collections and Iterators | Autodesk

> ## Excerpt
> In the Revit Platform API, Collections and Iterators are generic and type safe.

---
In the Revit Platform API, Collections and Iterators are generic and type safe.

All collections implement the IEnumerable interface and all relevant iterators implement the IEnumerator interface. As a result, all methods and properties are implemented in the Revit Platform API and can play a role in the relevant collections.

Implementing all of the collections is similar. The following example uses ModelCurveArray to demonstrate how to use the main collection properties:

<table summary="" id="GUID-D6F6C00C-B0FF-42E5-9A45-16B4E2D3DC63__TABLE_C8AF48AF0E86477182C069DAE70F94FD"><tbody><tr><td><b>Code Region 9-2: Using collections</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>UsingCollections</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span> 
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

    </span><span>// Store the ModelLine references</span><span>
    </span><span>ModelCurveArray</span><span> lineArray </span><span>=</span><span> </span><span>new</span><span> </span><span>ModelCurveArray</span><span>();</span><span>

    </span><span>// … Store operation</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> id </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>(</span><span>131943</span><span>);</span><span> </span><span>//assume 131943 is a model line element id</span><span>
    lineArray</span><span>.</span><span>Append</span><span>(</span><span>document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>);</span><span>

    </span><span>// use Size property of Array</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Before Insert: "</span><span> </span><span>+</span><span> lineArray</span><span>.</span><span>Size</span><span> </span><span>+</span><span> </span><span>" in lineArray."</span><span>);</span><span>

    </span><span>// use IsEmpty property of Array</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>lineArray</span><span>.</span><span>IsEmpty</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// use Item(int) property of Array</span><span>
        </span><span>ModelCurve</span><span> modelCurve </span><span>=</span><span> lineArray</span><span>.</span><span>get_Item</span><span>(</span><span>0</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelCurve</span><span>;</span><span>

        </span><span>// erase the specific element from the set of elements</span><span>
        selectedIds</span><span>.</span><span>Remove</span><span>(</span><span>modelCurve</span><span>.</span><span>Id</span><span>);</span><span>

        </span><span>// create a new model line and insert to array of model line</span><span>
        </span><span>SketchPlane</span><span> sketchPlane </span><span>=</span><span> modelCurve</span><span>.</span><span>SketchPlane</span><span>;</span><span>

        XYZ startPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>  </span><span>// the start point of the line</span><span>
        XYZ endPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>  </span><span>// the end point of the line</span><span>
        </span><span>// create geometry line</span><span>
        </span><span>Line</span><span> geometryLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>startPoint</span><span>,</span><span> endPoint</span><span>);</span><span>

        </span><span>// create the ModelLine</span><span>
        </span><span>ModelLine</span><span> line </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geometryLine</span><span>,</span><span> sketchPlane</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>;</span><span>

        lineArray</span><span>.</span><span>Insert</span><span>(</span><span>line</span><span>,</span><span> lineArray</span><span>.</span><span>Size</span><span> </span><span>-</span><span> </span><span>1</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"After Insert: "</span><span> </span><span>+</span><span> lineArray</span><span>.</span><span>Size</span><span> </span><span>+</span><span> </span><span>" in lineArray."</span><span>);</span><span>

    </span><span>// use the Clear() method to remove all elements in lineArray</span><span>
    lineArray</span><span>.</span><span>Clear</span><span>();</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"After Clear: "</span><span> </span><span>+</span><span> lineArray</span><span>.</span><span>Size</span><span> </span><span>+</span><span> </span><span>" in lineArray."</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Collections and Iterators  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Editing Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:50:31 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html
author: 
---

# Help | Editing Elements | Autodesk

> ## Excerpt
> In Revit, you can move, copy, rotate, align, delete, mirror, group, and array one element or a set of elements with the Revit Platform API. Using the editing functionality in the API is similar to the commands in the Revit UI.

---
In Revit, you can move, copy, rotate, align, delete, mirror, group, and array one element or a set of elements with the Revit Platform API. Using the editing functionality in the API is similar to the commands in the Revit UI.

**Pages in this section**

-   [Moving Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Moving_Elements_html)
-   [Copying Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Copying_Elements_html)
-   [Rotating elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Rotating_elements_html)
-   [Aligning Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Aligning_Elements_html)
-   [Mirroring Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Mirroring_Elements_html)
-   [Grouping Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Grouping_Elements_html)
-   [Creating Arrays of Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Creating_Arrays_of_Elements_html)
-   [Deleting Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Deleting_Elements_html)
-   [Pinned Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Pinned_Elements_html)

**Parent page:** [Basic Interaction with Revit Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_html)


<!-- ===== END: Help  Editing Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Moving Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:50:35 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Moving_Elements_html
author: 
---

# Help | Moving Elements | Autodesk

> ## Excerpt
> The ElementTransformUtils class provides two static methods to move one or more elements from one place to another.

---
The ElementTransformUtils class provides two static methods to move one or more elements from one place to another.

**Table 19: Move Methods**

|  |  |
| --- | --- |
| Member | Description |
| `MoveElement( Document, ElementId, XYZ)` | Move an element in the document by a specified vector. |
| `MoveElements(Document, ICollection<ElementId>, XYZ)` | Move several elements by a set of IDs in the document by a specified vector. |

Note: When you use the MoveElement() or MoveElements() methods, the following rules apply.

-   The methods cannot move a level-based element up or down from the level. When the element is level-based, you cannot change the Z coordinate value. However, you can place the element at any location in the same level. As well, some level based elements have an offset instance parameter you can use to move them in the Z direction.For example, if you create a new column at the original location (0, 0, 0) in Level1, and then move it to the new location (10, 20, 30), the column is placed at the location (10, 20, 0) instead of (10, 20, 30).
    
    <table summary="" id="GUID-CD3B9A83-8DBC-418E-8099-D655AB3DA010__TABLE_AE46ADAF23A64DEB8AB387ACFCCD32D5"><tbody><tr><td><b>Code Region 10-1: Using MoveElement()</b></td></tr><tr><td></td></tr></tbody></table>
    

```
public void MoveColumn(Autodesk.Revit.DB.Document document, FamilyInstance column)
{
        // get the column current location
        LocationPoint columnLocation = column.Location as LocationPoint;

        XYZ oldPlace = columnLocation.Point;

        // Move the column to new location.
        XYZ newPlace = new XYZ(10, 20, 30);
        ElementTransformUtils.MoveElement(document, column.Id, newPlace);

        // now get the column's new location
        columnLocation = column.Location as LocationPoint;
        XYZ newActual = columnLocation.Point;

        string info = "Original Z location: " + oldPlace.Z + 
                        "\nNew Z location: " + newActual.Z;

        TaskDialog.Show("Revit",info);
}
```

```
</td>

</tr>

</tbody>

</table>
```

-   When you move one or more elements, associated elements are moved. For example, if a wall with windows is moved, the windows are also moved.
-   [Pinned Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Pinned_Elements_html) cannot be moved.

Another way to move an element in Revit is to use Location and its derivative objects. In the Revit Platform API, the Location object provides the ability to translate and rotate elements. More location information and control is available using the Location object derivatives such as LocationPoint or LocationCurve. If the Location element is downcast to a LocationCurve object or a LocationPoint object, move the curve or the point to a new place directly.

<table summary="" id="GUID-CD3B9A83-8DBC-418E-8099-D655AB3DA010__TABLE_AF33E1AB2AEC436096E2BD1C6B962793"><tbody><tr><td><b>Code Region 10-2: Moving using Location</b></td></tr><tr><td><pre><code><span>bool</span><span> </span><span>MoveUsingLocationCurve</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>LocationCurve</span><span> wallLine </span><span>=</span><span> wall</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
        XYZ translationVec </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>20</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        </span><span>return</span><span> </span><span>(</span><span>wallLine</span><span>.</span><span>Move</span><span>(</span><span>translationVec</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

When you move the element, note that the vector (10, 20, 0) is not the destination but the offset. The following picture illustrates the wall position before and after moving.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-CA323378-0ABA-4B2B-B242-2D98C01F0A78-low.png)**Figure 30: Move a wall using the LocationCurve**

In addition, you can use the LocationCurve Curve property or the LocationPoint Point property to move one element in Revit.

Use the Curve property to move a curve-driven element to any specified position. Many elements are curve-driven, such as walls, beams, and braces. Also use the property to resize the length of the element.

<table summary="" id="GUID-CD3B9A83-8DBC-418E-8099-D655AB3DA010__TABLE_1D166EBA33324A2398067CD862BE6F1C"><tbody><tr><td><b>Code Region 10-3: Moving using Curve</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>MoveUsingCurveParam</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>LocationCurve</span><span> wallLine </span><span>=</span><span> wall</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
    XYZ p1 </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
    XYZ p2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>20</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Line</span><span> newWallLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p1</span><span>,</span><span> p2</span><span>);</span><span>

    </span><span>// Change the wall line to a new line.</span><span>
    wallLine</span><span>.</span><span>Curve</span><span> </span><span>=</span><span> newWallLine</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

You can also get or set a curve-based element's join properties with the LocationCurve.JoinType property.

Use the LocationPoint Point property to set the element's physical location.

<table summary="" id="GUID-CD3B9A83-8DBC-418E-8099-D655AB3DA010__TABLE_76091AAAC4C04143BB5F5B2EACBE99E5"><tbody><tr><td><b>Code Region 10-4: Moving using Point</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>LocationMove</span><span>(</span><span>FamilyInstance</span><span> column</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>LocationPoint</span><span> columnPoint </span><span>=</span><span> column</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationPoint</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> columnPoint</span><span>)</span><span>
        </span><span>{</span><span>
                XYZ newLocation </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>20</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                </span><span>// Move the column to the new location</span><span>
                columnPoint</span><span>.</span><span>Point</span><span> </span><span>=</span><span> newLocation</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Moving Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Copying Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:50:41 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Copying_Elements_html
author: 
---

# Help | Copying Elements | Autodesk

> ## Excerpt
> The ElementTransformUtils class provides several static methods to copy one or more elements from one place to another, either within the same document or view, or to a different document or view.

---
The ElementTransformUtils class provides several static methods to copy one or more elements from one place to another, either within the same document or view, or to a different document or view.

**Table: Copy Methods**

|  |  |
| --- | --- |
| Member | Description |
| `CopyElement( Document, ElementId, XYZ)` | Copies an element and places the copy at a location indicated by a given transformation.. |
| `CopyElements(Document, ICollection<ElementId>, XYZ)` | Copies a set of elements and places the copies at a location indicated by a given translation. |
| `CopyElements(Document, ICollection<ElementId>, Document, Transform, CopyPasteOptions)` | Copies a set of elements from source document to destination document. |
| `CopyElements(View, ICollection<ElementId>, View, Transform, CopyPasteOptions)` | Copies a set of elements from source view to destination view. |

All of the methods return a collection of ElementIds of the newly created elements, including CopyElement(). The collection includes any elements created due to dependencies.

The method for copying from one document to another can be used for copying non-view specific elements only. Copies are placed at their respective original location or locations specified by the optional transformation.

View-specific elements should be copied using the method that copies from one view to another. That method can be used for both view-specific and model elements however, drafting views cannot be used as a destination for model elements. The pasted elements are repositioned to ensure proper placement in the destination view. For example, the elevation is changed when copying from one level to another. An additional transformation within the destination view can be performed by providing the optional Transform argument. This additional transformation must be within the plane of the destination view.

When copying from one view to another, both the source and destination views must be 2D graphics views capable of drawing details and view-specific elements, such as floor and ceiling plans, elevations, sections, or drafting views. The ElementTransformUtils.GetTransformFromViewToView() method will return the transformation that is applied to elements when copying from a source view to a destination view.

When copying between views or between documents, an optional CopyPasteOptions parameter may be set to override default copy/paste settings. By default, in the event of duplicate type names during a paste operation, Revit displays a modal dialog with options to either copy types with unique names only, or to cancel the operation. CopyPasteOptions can be used to specify a custom handler, using the IDuplicateTypeNamesHandler interface, to handle duplicate type names.

See the Duplicate Views sample in the Revit SDK for a detailed example of copying between documents and between views.


<!-- ===== END: Help  Copying Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Rotating elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:50:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Rotating_elements_html
author: 
---

# Help | Rotating elements | Autodesk

> ## Excerpt
> The ElementTransformUtils class provides two static methods to rotate one or several elements in the project.

---
The ElementTransformUtils class provides two static methods to rotate one or several elements in the project.

**Table 20: Rotate Methods**

|  |  |
| --- | --- |
| Member | Description |
| `RotateElement(Document, ElementId, Line, double)` | Rotate an element in the document by a specified number of radians around a given axis. |
| `RotateElements(Document, ICollection<ElementId>, Line, double)` | Rotate several elements by IDs in the project by a specified number of radians around a given axis. |

In these methods, the angle of rotation is in radians. The positive radian means rotating counterclockwise around the specified axis, while the negative radian means clockwise, as the following pictures illustrates.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-2CDF32C7-BA19-499B-81BE-02A982E310D7-low.png)**Figure 31: Counterclockwise rotation**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-11A64EB3-0D9F-4A33-8DB7-CBA34CFBD04C-low.png)**Figure 32: Clockwise rotation**

Note that pinned elements cannot be rotated.

<table summary="" id="GUID-B1C87D72-CAA5-4311-929C-CFC9B5480D24__TABLE_D006222F789C45FAAA18D7CBAEEB9DEF"><tbody><tr><td><b>Code Region 10-5: Using RotateElement()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>RotateColumn</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    XYZ point1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>20</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ point2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>20</span><span>,</span><span> </span><span>30</span><span>);</span><span>
    </span><span>// The axis should be a bound line.</span><span>
    </span><span>Line</span><span> axis </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>point1</span><span>,</span><span> point2</span><span>);</span><span>
    </span><span>ElementTransformUtils</span><span>.</span><span>RotateElement</span><span>(</span><span>document</span><span>,</span><span> element</span><span>.</span><span>Id</span><span>,</span><span> axis</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>3.0</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

If the element Location can be downcast to a LocationCurve or a LocationPoint, you can rotate the curve or the point directly.

<table summary="" id="GUID-B1C87D72-CAA5-4311-929C-CFC9B5480D24__TABLE_DB1024D1257A48B3B4BFD58C5246E884"><tbody><tr><td><b>Code Region 10-6: Rotating based on location curve</b></td></tr><tr><td><pre><code><span>bool</span><span> </span><span>LocationRotate</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> rotated </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>// Rotate the element via its location curve.</span><span>
    </span><span>LocationCurve</span><span> curve </span><span>=</span><span> element</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> curve</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Curve</span><span> line </span><span>=</span><span> curve</span><span>.</span><span>Curve</span><span>;</span><span>
        XYZ aa </span><span>=</span><span> line</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>
        XYZ cc </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>aa</span><span>.</span><span>X</span><span>,</span><span> aa</span><span>.</span><span>Y</span><span>,</span><span> aa</span><span>.</span><span>Z </span><span>+</span><span> </span><span>10</span><span>);</span><span>
        </span><span>Line</span><span> axis </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>aa</span><span>,</span><span> cc</span><span>);</span><span>
        rotated </span><span>=</span><span> curve</span><span>.</span><span>Rotate</span><span>(</span><span>axis</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>2.0</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> rotated</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

<table summary="" id="GUID-B1C87D72-CAA5-4311-929C-CFC9B5480D24__TABLE_8F36FBC62F844D8FA44A062AA2308CF2"><tbody><tr><td><b>Code Region 10-7: Rotating based on location point</b></td></tr><tr><td><pre><code><span>bool</span><span> </span><span>LocationPointRotate</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>bool</span><span> rotated </span><span>=</span><span> </span><span>false</span><span>;</span><span>
        </span><span>LocationPoint</span><span> location </span><span>=</span><span> element</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationPoint</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> location</span><span>)</span><span>
        </span><span>{</span><span>
                XYZ aa </span><span>=</span><span> location</span><span>.</span><span>Point</span><span>;</span><span>
                XYZ cc </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>aa</span><span>.</span><span>X</span><span>,</span><span> aa</span><span>.</span><span>Y</span><span>,</span><span> aa</span><span>.</span><span>Z </span><span>+</span><span> </span><span>10</span><span>);</span><span>
                </span><span>Line</span><span> axis </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>aa</span><span>,</span><span> cc</span><span>);</span><span>           
                rotated </span><span>=</span><span> location</span><span>.</span><span>Rotate</span><span>(</span><span>axis</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>2.0</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> rotated</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Rotating elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Aligning Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:50:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Aligning_Elements_html
author: 
---

# Help | Aligning Elements | Autodesk

> ## Excerpt
> The ItemFactoryBase.NewAlignment() method can create a new locked alignment between two references. These two references must be one of the following combinations:

---
The ItemFactoryBase.NewAlignment() method can create a new locked alignment between two references. These two references must be one of the following combinations:

-   2 planar faces
-   2 lines
-   line and point
-   line and reference plane
-   2 arcs
-   2 cylindrical faces

These references must be already geometrically aligned as this function will not force them to become aligned. If the alignment can be created a new Dimension object is returned representing the locked alignment. Otherwise an exception will be thrown.

The NewAlignment() method also requires a view which will determine the orientation of the alignment.

See the CreateTruss example in the FamilyCreation folder included with the SDK Samples. It has several examples of the use of NewAlignment(), such as locking the bottom chord of a new truss to a bottom reference plane.


<!-- ===== END: Help  Aligning Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Mirroring Elements  Autodesk.md ===== -->

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


<!-- ===== END: Help  Mirroring Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Grouping Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:51:02 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Grouping_Elements_html
author: 
---

# Help | Grouping Elements | Autodesk

> ## Excerpt
> The Revit Platform API uses the Creation.Document.NewGroup() method to select an element or multiple elements or groups and then combines them. With each instance of a group that you place, there is associatively among them. For example, you create a group with a bed, walls, and window and then place multiple instances of the group in your project. If you modify a wall in one group, it changes for all instances of that group. This makes modifying your building model much easier because you can change several instances of a group in one operation.

---
The Revit Platform API uses the Creation.Document.NewGroup() method to select an element or multiple elements or groups and then combines them. With each instance of a group that you place, there is associatively among them. For example, you create a group with a bed, walls, and window and then place multiple instances of the group in your project. If you modify a wall in one group, it changes for all instances of that group. This makes modifying your building model much easier because you can change several instances of a group in one operation.

<table summary="" id="GUID-1A0E4AB2-86B2-40C4-A11C-48636284FCE4__TABLE_7A648D1F5F024144B570518E4D82A45A"><tbody><tr><td><b>Code Region 10-9: Creating a Group</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MakeGroup</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Group</span><span> </span><span>group</span><span> </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

    </span><span>if</span><span> </span><span>(</span><span>selectedIds</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Group all selected elements</span><span>
        </span><span>group</span><span> </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewGroup</span><span>(</span><span>selectedIds</span><span>);</span><span>
        </span><span>// Initially, the group has a generic name, such as Group 1\. It can be modified by changing the name of the group type as follows:</span><span>
        </span><span>// Change the default group name to a new name "MyGroup"</span><span>
        </span><span>group</span><span>.</span><span>GroupType</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"MyGroup"</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

There are three types of groups in Revit; Model Group, Detail Group, and Attached Detail Group. All are created using the NewGroup() method. The created Group's type depends on the Elements passed.

-   If no detail Element is passed, a Model Group is created.
-   If all Elements are detail elements, then a Detail Group is created.
-   If both types of Elements are included, a Model Group that contains an Attached Detail Group is created and returned.

Note: When elements are grouped, they can be deleted from the project.

-   When a model element in a model group is deleted, it is still visible when the mouse cursor hovers over or clicks the group, even if the application returns Succeeded to the UI. In fact, the model element is deleted and you cannot select or access that element.
-   When the last member of a group instance is deleted, excluded, or removed from the project, the model group instance is deleted.

When elements are grouped, they cannot be moved or rotated. If you perform these operations on the grouped elements, nothing happens to the elements, though the Move() or Rotate() method returns true.

You cannot group dimensions and tags without grouping the elements they reference. If you do, the API call will fail.

You can group dimensions and tags that refer to model elements in a model group. The dimensions and tags are added to an attached detail group. The attached detail group cannot be moved, copied, rotated, arrayed, or mirrored without doing the same to the parent group.

## Attached Detail Groups

To determine if a group is an attached detail group, use the `Group.IsAttached` property. To find the group to which a detail group is attached, use the `Group.AttachedParentId` property.

If a Model Group has attached detail groups, the visibility of these detail groups can be controlled with:

-   Group.ShowAttachedDetailGroups()
-   Group.ShowAllAttachedDetailGroups()
-   Group.HideAttachedDetailGroups()
-   Group.HideAllAttachedDetailGroups()

The attached detail groups available for a group or group type can be found with:

-   Group.GetAvailableAttachedDetailGroupTypeIds()
-   GroupType.GetAvailableAttachedDetailGroupTypeIds()

`Group.IsCompatibleAttachedDetailGroupType()` checks if the orientation of an attached detail group matches the orientation of a view. To prevent displaying detail groups in the wrong view, verify that the OwnerViewId of a detail group matches the view in which you are trying to display it.


<!-- ===== END: Help  Grouping Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Creating Arrays of Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:51:07 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Creating_Arrays_of_Elements_html
author: 
---

# Help | Creating Arrays of Elements | Autodesk

> ## Excerpt
> The Revit Platform API provides two classes, LinearArray and RadialArray to array one or more elements in the project. These classes provide static methods to create a linear or radial array of one or more selected components. Linear arrays represent an array created along a line from one point, while radial arrays represent an array created along an arc.

---
The Revit Platform API provides two classes, LinearArray and RadialArray to array one or more elements in the project. These classes provide static methods to create a linear or radial array of one or more selected components. Linear arrays represent an array created along a line from one point, while radial arrays represent an array created along an arc.

As an example of using an array, you can select a door and windows located in the same wall and then create multiple instances of the door, wall, and window configuration.

Both LinearArray and RadialArray also provide methods to array one or several elements without being grouped and associated. Although similar to the Create() methods for arraying elements, each resulting element is independent of the others, and can be manipulated without affecting the other elements. See the tables below for more information on the methods available to create linear or radial arrays.

**Table 22: LinearArray Methods**

|  |  |
| --- | --- |
| Member | Description |
| `Create(Document, View, ElementId, int, XYZ, ArrayAnchorMember)` | Array one element in the project by a specified number. |
| `Create(Document, View, ICollection<ElementId>, int, XYZ, ArrayAnchorMember)` | Array a set of elements in the project by a specified number. |
| `ArrayElementWithoutAssociation(Document, View, ElementId, int, XYZ, ArrayAnchorMember)` | Array one element in the project by a specified number. The resulting elements are not associated with a linear array. |
| `ArrayElementsWithoutAssociation(Document, View, ICollection<ElementId>, int, XYZ, ArrayAnchorMember)` | Array a set of elements in the project by a specified number. The resulting elements are not associated with a linear array. |

**Table 23: RadialArray Methods**

|  |  |
| --- | --- |
| Member | Description |
| `Create(Document, View, ElementId, int, Line, double, ArrayAnchorMember)` | Array one element in the project based on an input rotation axis. |
| `ArrayElementWithoutAssociation(Document, View, ElementId, int, Line, double, ArrayAnchorMember)` | Array one element in the project based on an input rotation axis.. The resulting elements are not associated with a linear array. |
| `ArrayElementsWithoutAssociation(Document, View, ICollection<ElementId>, int, Line, double, ArrayAnchorMember)` | Array a set of elements in the project based on an input rotation axis.. The resulting elements are not associated with a linear array. |

The methods for arraying elements are useful if you need to create several instances of a component and manipulate them simultaneously. Every instance in an array can be a member of a group.

Note: When using the methods for arraying elements, the following rules apply:

-   When performing Linear and Radial Array operations, elements dependent on the arrayed elements are also arrayed.
-   Some elements cannot be arrayed because they cannot be grouped. See the Revit User's Guide for more information about restrictions on groups and arrays.
-   Arrays are not supported by most annotation symbols.


<!-- ===== END: Help  Creating Arrays of Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Deleting Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:51:11 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Deleting_Elements_html
author: 
---

# Help | Deleting Elements | Autodesk

> ## Excerpt
> The Revit Platform API provides Delete() methods to delete one or more elements in the project.

---
The Revit Platform API provides Delete() methods to delete one or more elements in the project.

**Table 23: Delete Members**

<table summary="" id="GUID-D8D01E04-2F08-49B2-8614-AED24F560F5C__TABLE_C698AFE08C52448B82FC7C02E23844D6"><tbody><tr><td><b>Member</b></td><td><b>Description</b></td></tr><tr><td>Delete(ElementId)</td><td>Delete an element from the project using the element ID</td></tr><tr><td>Delete(<a href="http://msdn2.microsoft.com/en-us/library/92t2ye13" target="_blank">ICollection</a>)</td><td>Delete several elements from the project by their IDs.</td></tr></tbody></table>

The first method deletes a single element based on its Id, as shown in the example below.

<table summary="" id="GUID-D8D01E04-2F08-49B2-8614-AED24F560F5C__TABLE_E9BC67116341441CA2E5B8222497A865"><tbody><tr><td><b>Code Region: Deleting an element based on ElementId</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>DeleteElement</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Delete an element via its id</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> elementId </span><span>=</span><span> element</span><span>.</span><span>Id</span><span>;</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>&gt;</span><span> deletedIdSet </span><span>=</span><span> document</span><span>.</span><span>Delete</span><span>(</span><span>elementId</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>==</span><span> deletedIdSet</span><span>.</span><span>Count</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Deleting the selected element in Revit failed."</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"The selected element has been removed and "</span><span>;</span><span>
        prompt </span><span>+=</span><span> deletedIdSet</span><span>.</span><span>Count</span><span> </span><span>-</span><span> </span><span>1</span><span>;</span><span>
        prompt </span><span>+=</span><span> </span><span>" more dependent elements have also been removed."</span><span>;</span><span>

        </span><span>// Give the user some information</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: When an element is deleted, any child elements associated with that element are also deleted, as indicated in the sample above.

The API also provides a way to delete several elements.

<table summary="" id="GUID-D8D01E04-2F08-49B2-8614-AED24F560F5C__TABLE_DCF65C320D43485F9FCFFD209929E9BA"><tbody><tr><td><b>Code Region: Deleting multiple elements based on Id</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>DeleteSelected</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Delete all the selected elements via the set of elements</span><span>
        </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span> 
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> elements </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>&gt;</span><span> deletedIdSet </span><span>=</span><span> document</span><span>.</span><span>Delete</span><span>(</span><span>elements</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>==</span><span> deletedIdSet</span><span>.</span><span>Count</span><span>)</span><span>
        </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Deleting the selected elements in Revit failed."</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"The selected element has been removed."</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: After you delete the elements, any references to the deleted elements become invalid and throw an exception if they are accessed.

## Element Dependencies

Element.GetDependentElements() returns a list of ids of elements which are "children" of this element; that is, those elements which will be deleted along with this element. The method optionally takes an ElementFilter which can be used to reduce the output list to the collection of elements matching specific criteria.


<!-- ===== END: Help  Deleting Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Pinned Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:51:15 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Pinned_Elements_html
author: 
---

# Help | Pinned Elements | Autodesk

> ## Excerpt
> Elements can be pinned to prevent them from moving. The Element.Pinned property can be used to check if an Element is pinned or to pin or unpin an element.

---
Elements can be pinned to prevent them from moving. The Element.Pinned property can be used to check if an Element is pinned or to pin or unpin an element.

When Element.Pinned is set to true, the element cannot be moved or rotated.

**Parent page:** [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html)


<!-- ===== END: Help  Pinned Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Views  Autodesk.md ===== -->

---
created: 2026-01-28T20:51:20 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_html
author: 
---

# Help | Views | Autodesk

> ## Excerpt
> Views are images produced from a Revit model with privileged access to the data stored in the documents. They can be graphics, such as plans, or text, such as schedules. Each project document has one or more different views. The last focused window is the active view.

---
Views are images produced from a Revit model with privileged access to the data stored in the documents. They can be graphics, such as plans, or text, such as schedules. Each project document has one or more different views. The last focused window is the active view.

The Autodesk.Revit.DB.View class is the base class for all view types in the Revit document. The Autodesk.Revit.UI.UIView class represents the window view in the Revit user interface.

In the following sections, you learn how views are generated, the types of views supported by Revit, the features for each view, as well as the functionality available for view windows in the user interface.


<!-- ===== END: Help  Views  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  About views  Autodesk.md ===== -->

---
created: 2026-01-28T20:51:26 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_About_views_html
author: 
---

# Help | About views | Autodesk

> ## Excerpt
> The Revit API provides access to View properties and the ability to create and delete views programmatically.

---
The Revit API provides access to View properties and the ability to create and delete views programmatically.

This section is a high-level overview that includes the following:

-   How views are generated
-   View types
-   View navigation tools
-   Creating and deleting views.
    
    ### View process
    

The following figure illustrates how a view is generated.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-EBFC1A8B-6618-4D25-BAEF-AD97A02830F5-low.png)**Figure 94: Create view process**

Each view is generated by projecting a three-dimensional object onto a two-dimensional projection plane. Projections are divided into two basic classes:

-   Perspective
-   Parallel

After the projection type is determined, you must specify the conditions under which the 3D model is needed and the scene is to be rendered. For more information about projection, refer to the [View3D](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_View3D_html) section.

World coordinates include the following:

-   The viewer's eye position
-   The viewing plane location where the projection is displayed.

Revit uses two coordinate systems:

-   The global or model space coordinates where the building exists
-   The viewing coordinate system.

The viewing coordinate system represents how the model is presented in the observer's view. Its origin is the viewer's eye position whose coordinates in the model space are retrieved by the View.Origin property. The X, Y, and Z axes are represented by the View.RightDirection, View.UpDirection, and View.ViewDirection properties respectively.

-   View.RightDirection is towards the right side of the screen.
-   View.UpDirection towards the up side of the screen.
-   View.ViewDirection from the screen to the viewer.

The viewing coordinate system is right-handed. For more information, see the [View3D](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_View3D_html) and the Parallel Projection picture in [View3D](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_View3D_html).

Some portions of a 3D model space that do not display, such as those that are behind the viewer or are too far away to display clearly, are excluded before being projected onto the projection plane. This action requires cropping the view. The following rules apply to cropping:

-   Elements outside of the crop region are no longer in the view.
    
-   The View.GetCropRegionShapeManager method returns a ViewCropRegionShapeManager which provides the boundary information for the crop region, which may or may not be rectangular.
    
-   The View.CropBoxVisible property determines whether the crop box is visible in the view.
    
-   The View.CropBoxActive property determines whether the crop box is actually being used to crop the view.
    

After cropping, the model is projected onto the projection plane. The following rules apply to the projection:

-   The projection contents are mapped to the screen view port for display.
-   During the mapping process, the projection contents are scaled so that they are shown properly on the screen.
-   The View.Scale property is the ratio of the actual model size to the view size.
-   The view boundary on paper is the crop region, which is a projection of the crop shape on the projection plane.
-   The size and position of the crop region is determined by the View.OutLine property.

You can transform between model space and a view's projection space witht the following methods:

-   TransformWithBoundary.GetModelToProjectionTransform()
-   TransformWithBoundary.GetBoundary() - Returns the boundary for the model space to view projection space transform.
-   View.GetModelToProjectionTransforms() - Gets the transforms from the model space to the view projection space. Views with split crop regions have more than one transform.
-   View.HasViewTransforms() - Returns true if the view reports model space to view projection space transforms. Schedules and legends, for example, do not report any.

Transforming between a view's projection space and sheet space can be done with `Viewport.GetProjectionToSheetTransform()`.

### View navigation tools

You may access information about the home view camera currently set in the view cube settings. There may only be one home view camera set for the document. This corresponds to the view orientation and other camera parameters saved when the user invokes the ViewCube UI command to "Set current view as home" in the ViewCube right-click context menu.

Access the ViewNavigationToolSettings by calling the static method ViewNavigationToolSettings.GetViewNavigationToolSettings() which will return the ViewNavigationToolSettings element associated with the document.

The ViewNavigationToolSettings will allow you to query whether a home view has been set with the method IsHomeCameraSet() which returns a boolean indicating the current state of the home view setting.

Access read-only information about the home camera set in the ViewCube by getting a copy of the home camera with the ViewNavigationToolSettings.GetHomeCamera() method. This function returns Null if the home camera is not yet set. The HomeCamera class provides informationabout the camera and view for the Home view orientation stored in the model such as EyePosition and UpDirection.

### Creating and deleting views

The Revit Platform API provides numerous methods to create the corresponding view elements derived from Autodesk.Revit.DB.View class. Most view types are created using static methods of the derived view classes. If a view is created successfully, these methods return a reference to the view, otherwise they return null. The methods are described in the following sections specific to each view class.

Views can also be created using the View.Duplicate() method. A new view can be created from an existing view with options for the new view to be dependent or to have detailing. The following example demonstrates how to create a new dependent view.

<table summary="" id="GUID-D8D8C7F5-3043-4459-A198-0B5984CBF41C__TABLE_819A2DD6FF4E4078A6B8A43723BBF551"><tbody><tr><td><b>Code Region: Create a dependent view</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>View</span><span> </span><span>CreateDependentCopy</span><span>(</span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>View</span><span> dependentView </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ElementId</span><span> newViewId </span><span>=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>view</span><span>.</span><span>CanViewBeDuplicated</span><span>(</span><span>ViewDuplicateOption</span><span>.</span><span>AsDependent</span><span>))</span><span>
    </span><span>{</span><span>
        newViewId </span><span>=</span><span> view</span><span>.</span><span>Duplicate</span><span>(</span><span>ViewDuplicateOption</span><span>.</span><span>AsDependent</span><span>);</span><span>
        dependentView </span><span>=</span><span> view</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>newViewId</span><span>)</span><span> </span><span>as</span><span> </span><span>View</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> dependentView</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>dependentView</span><span>.</span><span>GetPrimaryViewId</span><span>()</span><span> </span><span>==</span><span> view</span><span>.</span><span>Id</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Dependent View"</span><span>,</span><span> </span><span>"Dependent view created successfully!"</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> dependentView</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Delete a view by using the Document.Delete() method with the view Id. You can also delete elements associated with a view. For example, deleting the level element causes Revit to delete the corresponding plan view or deleting the camera element causes Revit to delete the corresponding 3D view.

### Dependent Views

As seen above, dependent views can be created using the View.Duplicate() method and passing in the AsDependent value for the ViewDuplicationOption enumerator. A dependent view will remain synchronous with the primary view and all other dependent views , so that when view-specific changes (such as view scale and annotations) are made in one view, they are reflected in all views. Not all view types can be duplicated and you cannot create a dependent view from another dependent view. Use View.CanViewBeDuplicated() to make sure a dependent view can be generated from the view. This method takes a ViewDuplicationOption enum to check whether a view can be duplicated in a specific way. You may be able to duplicate a view as an independent view, but not a dependent view.

Dependent views have a valid primary view element Id that can be obtained from the method View.GetPrimaryViewId(). Independent views have InvalidElementId as their primary view Id. A dependent view can be converted to an independent view using the View.ConvertToIndependent() method. This method will thrown an exception if the view is not dependent.

<table summary="" id="GUID-D8D8C7F5-3043-4459-A198-0B5984CBF41C__TABLE_EEA4AB267C8645BF813DE5E13C5EA6B6"><tbody><tr><td><b>Code Region: Make a dependent view independent</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MakeViewIndependent</span><span>(</span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Independent views will have an InvalidElementId for the Primary View Id</span><span>
    </span><span>if</span><span> </span><span>(</span><span>view</span><span>.</span><span>GetPrimaryViewId</span><span>()</span><span> </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        view</span><span>.</span><span>ConvertToIndependent</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  About views  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  View Graphics  Autodesk.md ===== -->

---
created: 2026-01-28T20:51:32 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Graphics_html
author: 
---

# Help | View Graphics | Autodesk

> ## Excerpt
> Many elements of the graphics and display options for views are exposed via the API.

---
Many elements of the graphics and display options for views are exposed via the API.

## Display settings

The view class has properties to get and set the display style settings and the detail level settings. The View.DisplayStyle property uses the DisplayStyle enumeration and corresponds to the display options available at the bottom of the Revit window as shown below.![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/DisplayStyles.jpg)

Note: The display style cannot be set to Raytrace from the Revit API because this display style puts Revit into a restricted mode with limited capabilities.

The View.DetailLevel property uses the ViewDetailLevel enumeration and corresponds to the detail level options available at the bottom of the Revit window as shown below.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/DetailLevel.jpg)The ViewDetailLevel enumeration includes Undefined in the case that a given View does not use detail level.

## Thin Lines

The Thin Lines option, available in the Revit UI on the Graphics panel of the View tab, controls how lines are drawn in a view. Typically, when you zoom in on a model in a small scale view, element lines appear much thicker than they actually are. When Thin Lines is enabled, all lines are drawn as a single width regardless of zoom level. This option is made available via the ThinLinesOptions utility class, which has a property called AreThinLinesEnabled. It is a static property which affects the entire Revit session.

## Temporary view modes

The TemporaryViewModes class allows for control of temporary view modes. It can be accessed from the View.TemporaryViewModes property. For views that do not support temporary view modes, this property will be null. The RevealConstraints, RevealHiddenElements and WorksharingDisplay properties can be used to get and set the current state of these modes in the corresponding view. Note that some modes are only available in certain views and/or in a certain context. Additionally an available mode is not necessarily enabled in the current context. The TemporaryViewModes methods IsModeAvailable() and IsModeEnabled() can be used to test that a particular mode is both available and enabled before use. These methods take a TemporaryViewMode enum. The possible options are shown below.

<table summary="" id="GUID-5A0D8870-EC39-43AF-95E5-3C1CFC398606__TABLE_07C91F91DCC24C10A97015F7A2A3A5EC"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td>RevealHiddenElements</td><td>The reveal hidden elements mode</td></tr><tr><td>TemporaryHideIsolate</td><td>The temporary hide/isolate mode</td></tr><tr><td>WorksharingDisplay</td><td>One of the worksharing display modes</td></tr><tr><td>TemporaryViewProperties</td><td>The temporary View Properties mode</td></tr><tr><td>ExplodedView</td><td>The mode that shows the model in exploded view and allows user changes/configurations</td></tr><tr><td>RevealConstraints</td><td>The mode that reveals constraints between elements in the model</td></tr></tbody></table>

<table summary="" id="GUID-5A0D8870-EC39-43AF-95E5-3C1CFC398606__TABLE_64A3F167A26044DE8188F11A71CFBD2A"><tbody><tr><td><b>Code Region: Reveal hidden elements in a view</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>RevealHiddenElementsInView</span><span>(</span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> hiddenRevealed </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>TemporaryViewModes</span><span> viewModes </span><span>=</span><span> view</span><span>.</span><span>TemporaryViewModes</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>viewModes </span><span>==</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Invalid View"</span><span>,</span><span> </span><span>"This view does not support temporary view modes."</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>// Mode must be available and enabled to be activated</span><span>
        </span><span>if</span><span> </span><span>(</span><span>viewModes</span><span>.</span><span>IsModeEnabled</span><span>(</span><span>TemporaryViewMode</span><span>.</span><span>RevealHiddenElements</span><span>)</span><span> </span><span>&amp;&amp;</span><span> viewModes</span><span>.</span><span>IsModeAvailable</span><span>(</span><span>TemporaryViewMode</span><span>.</span><span>RevealHiddenElements</span><span>))</span><span>
        </span><span>{</span><span>
            viewModes</span><span>.</span><span>RevealHiddenElements</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
            hiddenRevealed </span><span>=</span><span> viewModes</span><span>.</span><span>RevealHiddenElements</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> hiddenRevealed</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The TemporaryViewModes.IsModeActive() method tests whether a given mode is currently active in the view. Use the DeactivateAllModes() method to deactivate all currently active views, or use DeactiveMode() to deactivate a specific mode.

The PreviewFamilyVisibility property gets and sets the current state of the PreviewFamilyVisibility mode in the associated view. This mode is only available when the document of the view is in the environment of the family editor. This property is a PreviewFamilyVisibilityMode enumerated value rather than a bool. Possible states for this mode are:

<table summary="" id="GUID-5A0D8870-EC39-43AF-95E5-3C1CFC398606__TABLE_78AE3050B17F47ED8F39BEF0C65A7127"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td>Off</td><td>Element Visibility is not applied. All family elements visible.</td></tr><tr><td>On</td><td>Element Visibility of a view is applied to show visible elements only. Elements that are cut by a reference plane will be shown with their respective cut geometry.</td></tr><tr><td>Uncut</td><td>Element Visibility of a view is applied to show elements visible if instance is not cut. Note that this state is only available in certain views, such as floor plan and ceilings.</td></tr></tbody></table>

Even if the PreviewFamilyVisibility mode is available and enabled for a view, not all states are valid in all views. Before applying one of these states to a view, call IsValidState() to ensure it can be applied.

<table summary="" id="GUID-5A0D8870-EC39-43AF-95E5-3C1CFC398606__TABLE_139BCA553ECD47CA864F0BAED3A2340D"><tbody><tr><td><b>Code Region: Turn off preview family visibility mode</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>TurnOffFamilyVisibilityMode</span><span>(</span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>TemporaryViewModes</span><span> viewModes </span><span>=</span><span> view</span><span>.</span><span>TemporaryViewModes</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>viewModes </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>viewModes</span><span>.</span><span>IsModeAvailable</span><span>(</span><span>TemporaryViewMode</span><span>.</span><span>PreviewFamilyVisibility</span><span>)</span><span> </span><span>&amp;&amp;</span><span> viewModes</span><span>.</span><span>IsModeEnabled</span><span>(</span><span>TemporaryViewMode</span><span>.</span><span>PreviewFamilyVisibility</span><span>))</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>viewModes</span><span>.</span><span>IsValidState</span><span>(</span><span>PreviewFamilyVisibilityMode</span><span>.</span><span>Off</span><span>))</span><span>
            </span><span>{</span><span>
                viewModes</span><span>.</span><span>PreviewFamilyVisibility</span><span> </span><span>=</span><span> </span><span>PreviewFamilyVisibilityMode</span><span>.</span><span>Off</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

When a view is opened for the first time, its state of the PreviewFamilyVisibility mode is determined based on the default settings which is controlled through the static TemporaryViewModes properties PreviewFamilyVisibilityDefaultOnState and PreviewFamilyVisibilityDefaultUncutState as shown below.

<table summary="" id="GUID-5A0D8870-EC39-43AF-95E5-3C1CFC398606__TABLE_819A2DD6FF4E4078A6B8A43723BBF551"><tbody><tr><td><b>Code Region: Set default preview family visibility state</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SetDefaultPreviewFamilyVisibilityState</span><span>()</span><span>
</span><span>{</span><span>
    </span><span>TemporaryViewModes</span><span>.</span><span>PreviewFamilyVisibilityDefaultOnState</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    </span><span>TemporaryViewModes</span><span>.</span><span>PreviewFamilyVisibilityDefaultUncutState</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The PreviewFamilyVisibilityDefaultOnState value controls whether each newly opened view is to have the PreviewFamilyVisibility mode turned On by default or not. This property is applicable to all types of views. Views that support both cut and uncut previews (such as floor plans) will use the cut/uncut state indicated by the PreviewFamilyVisibilityDefaultUncutState property, but only if the PreviewFamilyVisibilityDefaultOnState property is set to true.

These settings are applicable to the whole application rather than to individual family documents; the values persists between Revit sessions. Although the value is allowed to be set at any time, any changes made after the Revit application has been initialized will not have effect until the next session of Revit.

Note that once the PreviewFamilyVisibility property is explicitly modified, the applied setting stays in effect for the respective view even after the view is closed and later reopened again.

### Custom Temporary View Modes

The Revit API allows customization to create "custom temporary view modes" applied to a view as a temporary view property. For example, the "Reveal Obstacles for Path of Travel" temporary mode is implemented this way. It uses the Analysis Visualization Framework (AVF) to display additional graphics on top of the view contents.

These properties provide access to read and modify a custom temporary view mode. `CustomTitle` should be set to cause the view to display the customized frame. The application is responsible to adjust the appearance of elements in the view related to the mode.

-   TemporaryViewModes.CustomTitle
-   TemporaryViewModes.CustomColor
-   TemporaryViewModes.RemoveCustomization()
-   TemporaryViewModes.IsCustomized()

## Element visibility in a view

Views keep track of visible elements. All elements that are graphical and visible in the view can be retrieved using a FilteredElementCollector constructed with a document and the id of the view. However, some elements in the set may be hidden or covered by other elements. You can see them by rotating the view or removing the elements that cover them. Accessing these visible elements may require Revit to rebuild the geometry of the view. The first time your code uses this constructor for a given view, or the first time your code uses this constructor for a view whose display settings have just been changed, you may experience a significant performance degradation.

Individual elements can be hidden in a particular view. The method Element.IsHidden() indicates if an element is hidden in the given view, and Element.CanBeHidden() returns whether the element can be hidden. To hide individual elements, use View.HideElements() which takes a collection of ElementIds corresponding to the elements you wish to hide.

Element visibility can also be changed by category.

-   The View.GetCategoryHidden() method queries a category id to determine if it is hidden or visible in the view.
-   The View.SetCategoryHidden() method sets all elements in a specific category to hidden or visible.
-   The View.CanCategoryBeHidden() method indicates if a specific category of elements can be hidden in the view.

A FilteredElementCollector based on a view will only contain elements visible in the current view. You cannot retrieve elements that are not graphical or elements that are invisible. A FilteredElementCollector based on a document retrieves all elements in the document including invisible elements and non-graphical elements. For example, when creating a default 3D view in an empty project, there are no elements in the view but there are many elements in the document, all of which are invisible.

The following code sample counts the number of wall category elements in the active document and active view. The number of elements in the active view differs from the number of elements in the document since the document contains non-graphical wall category elements.

<table summary="" id="GUID-5A0D8870-EC39-43AF-95E5-3C1CFC398606__TABLE_A8EA219732534FC3BDE4CE9F1B2C83E0"><tbody><tr><td><b>Code Region: Counting elements in the active view</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CountElements</span><span>(</span><span>UIDocument</span><span> uiDoc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>StringBuilder</span><span> message </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>();</span><span>
    </span><span>FilteredElementCollector</span><span> viewCollector </span><span>=</span><span> 
        </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>uiDoc</span><span>.</span><span>Document</span><span>,</span><span> uiDoc</span><span>.</span><span>ActiveView</span><span>.</span><span>Id</span><span>);</span><span>
    viewCollector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Walls</span><span>);</span><span>
    message</span><span>.</span><span>AppendLine</span><span>(</span><span>"Wall category elements within active View: "</span><span>
        </span><span>+</span><span> viewCollector</span><span>.</span><span>ToElementIds</span><span>().</span><span>Count</span><span>);</span><span>

    </span><span>FilteredElementCollector</span><span> docCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>uiDoc</span><span>.</span><span>Document</span><span>);</span><span>
    docCollector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Walls</span><span>);</span><span>
    message</span><span>.</span><span>AppendLine</span><span>(</span><span>"Wall category elements within document: "</span><span>
        </span><span>+</span><span> docCollector</span><span>.</span><span>ToElementIds</span><span>().</span><span>Count</span><span>);</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> message</span><span>.</span><span>ToString</span><span>());</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Temporary view modes can affect element visibility. The View.IsInTemporaryViewMode() method can be used to determine if a View is in a temporary view mode. The method View.IsElementVisibleInTemporaryViewMode() identifies if an element should be visible in the indicated view mode. This applies only to the TemporaryHideIsolate and AnalyticalModel view modes. Other modes will result in an exception.

## Depth Cueing

The ViewDisplayDepthCueing class provides control of the display of distant objects in section and elevation views. When depth cueing is active, objects blend into the background color (fade) with increasing distance from the viewer. The current depth cueing settings for a view can be retrieved using View.GetDepthCueing(). If changes are made to the returned ViewDisplayDepthCueing, they will not be applied to the view until calling View.SetDepthCueing().

The ViewDisplayDepthCueing class has the following properties:

<table summary="" id="GUID-5A0D8870-EC39-43AF-95E5-3C1CFC398606__TABLE_C4392AA6B71B4338BD97E00BA3682CA2"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td>EnableDepthCueing</td><td>True to enable depth cueing.</td></tr><tr><td>StartPercentage</td><td>Indicates where depth cueing begins. A value of 0 indicates that depth cueing begins at the front clip plane of the view.</td></tr><tr><td>EndPercentage</td><td>Indicates where depth cueing ends. Objects further than the end plane will fade the same amount as objects at the end plane. A value of 100 indicates the far clip plane.</td></tr><tr><td>FadeTo</td><td>Indicates the maximum amount to fade objects via depth cueing. A value of 100 indicates complete invisibility.</td></tr></tbody></table>

The SetStartEndPercentages() method can be used to set the start and end percentages in one call.

The following example demonstrates how to get the current depth cueing, change its properties and set it back to the view. Note that not all views can use depth cueing.

<table summary="" id="GUID-5A0D8870-EC39-43AF-95E5-3C1CFC398606__TABLE_4D0B487A931E4AEABCAA578ECA030C66"><tbody><tr><td><b>Code Region: Change the depth cueing for a view</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>AdjustDepthCueing</span><span>(</span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(</span><span>view</span><span>.</span><span>CanUseDepthCueing</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>view</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Change depth cueing"</span><span>))</span><span>
        </span><span>{</span><span>
            t</span><span>.</span><span>Start</span><span>();</span><span>
            </span><span>ViewDisplayDepthCueing</span><span> depthCueing </span><span>=</span><span> view</span><span>.</span><span>GetDepthCueing</span><span>();</span><span>
            depthCueing</span><span>.</span><span>EnableDepthCueing</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
            depthCueing</span><span>.</span><span>FadeTo</span><span> </span><span>=</span><span> </span><span>50</span><span>;</span><span>    </span><span>// set fade to percent</span><span>
            depthCueing</span><span>.</span><span>SetStartEndPercentages</span><span>(</span><span>0</span><span>,</span><span> </span><span>75</span><span>);</span><span>
            view</span><span>.</span><span>SetDepthCueing</span><span>(</span><span>depthCueing</span><span>);</span><span>
            t</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  View Graphics  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  View Types  Autodesk.md ===== -->

---
created: 2026-01-28T20:51:38 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_html
author: 
---

# Help | View Types | Autodesk

> ## Excerpt
> Different types of Revit views are represented by different classes in the Revit API. See the following topics for more information on each type of view.

---
Different types of Revit views are represented by different classes in the Revit API. See the following topics for more information on each type of view.


<!-- ===== END: Help  View Types  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  View3D  Autodesk.md ===== -->

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


<!-- ===== END: Help  View3D  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  ViewPlan  Autodesk.md ===== -->

---
created: 2026-01-28T20:51:55 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_ViewPlan_html
author: 
---

# Help | ViewPlan | Autodesk

> ## Excerpt
> Plan views are level-based. There are three types of plan views: floor plan view, ceiling plan view, and area plan view.

---
Plan views are level-based. There are three types of plan views: floor plan view, ceiling plan view, and area plan view.

## Creating plan view

-   Generally the floor plan view is the default view opened in a new project.
    
-   Most projects include at least one floor plan view and one ceiling plan view.
    
-   Plan views are usually created after adding new levels to the project.
    

Adding new levels using the API does not add plan views automatically. Use the static ViewPlan.Create() method to create new floor and ceiling plan views. Use the static ViewPlan.CreateAreaPlan() method to create a new area plan view.

<table summary="" id="GUID-DDD3ABF7-0C89-437C-A676-8C5AA4F5F56F__TABLE_9928295F773E487A9323BF732E1C7F7C"><tbody><tr><td><b>Code Region: Creating Plan Views</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>ViewPlan</span><span> </span><span>ViewPlan</span><span>.</span><span>Create</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>ElementId</span><span> viewFamilyTypeId</span><span>,</span><span> </span><span>ElementId</span><span> levelId</span><span>);</span><span>

</span><span>public</span><span> </span><span>static</span><span> </span><span>ViewPlan</span><span> </span><span>ViewPlan</span><span>.</span><span>CreateAreaPlan</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>ElementId</span><span> areaSchemeId</span><span>,</span><span> </span><span>ElementId</span><span> levelId</span><span>);</span></code></pre></td></tr></tbody></table>

The viewFamilyTypeId parameter in ViewPlan.Create() needs to be a FloorPlan, CeilingPlan, AreaPlan, or StructuralPlan ViewType. The levelId parameter represents the Id of the level element in the project to which the plan view is associated.

The following code creates a floor plan and a ceiling plan based on a certain level.

<table summary="" id="GUID-DDD3ABF7-0C89-437C-A676-8C5AA4F5F56F__TABLE_0D605D3DBB614668ADEA9B78CE20E6D8"><tbody><tr><td><b>Code Region: Creating a floor plan and ceiling plan</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateViewPlan</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> viewFamilyTypes </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>ViewFamilyType</span><span>)).</span><span>ToElements</span><span>();</span><span>
    </span><span>ElementId</span><span> floorPlanId </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(-</span><span>1</span><span>);</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> viewFamilyTypes</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>ViewFamilyType</span><span> v </span><span>=</span><span> e </span><span>as</span><span> </span><span>ViewFamilyType</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>v </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> v</span><span>.</span><span>ViewFamily</span><span> </span><span>==</span><span> </span><span>ViewFamily</span><span>.</span><span>FloorPlan</span><span>)</span><span>
        </span><span>{</span><span>
            floorPlanId </span><span>=</span><span> e</span><span>.</span><span>Id</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>ElementId</span><span> ceilingPlanId </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(-</span><span>1</span><span>);</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> viewFamilyTypes</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>e</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Ceiling Plan"</span><span>)</span><span>
        </span><span>{</span><span>
            ceilingPlanId </span><span>=</span><span> e</span><span>.</span><span>Id</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// Create a Level and a Floor Plan based on it</span><span>
    </span><span>double</span><span> elevation </span><span>=</span><span> </span><span>10.0</span><span>;</span><span>
    </span><span>Level</span><span> level1 </span><span>=</span><span> </span><span>Level</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> elevation</span><span>);</span><span>
    </span><span>ViewPlan</span><span> floorView </span><span>=</span><span> </span><span>ViewPlan</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> floorPlanId</span><span>,</span><span> level1</span><span>.</span><span>Id</span><span>);</span><span>

    </span><span>// Create another Level and a Ceiling Plan based on it</span><span>
    elevation </span><span>+=</span><span> </span><span>10.0</span><span>;</span><span>
    </span><span>Level</span><span> level2 </span><span>=</span><span> </span><span>Level</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> elevation</span><span>);</span><span>
    </span><span>ViewPlan</span><span> ceilingView </span><span>=</span><span> </span><span>ViewPlan</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> ceilingPlanId</span><span>,</span><span> level2</span><span>.</span><span>Id</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Plan view properties

After creating a new plan view, the Discipline for the view can be set using the Discipline parameter which is type ViewDiscipline. Options include Architectural, Structural, Mechanical, Electrical, Plumbing and Coordination.

For structural plan views, the view direction can be set to either Up or Down using the ViewFamilyType.PlanViewDirection property. Although it is a property of the ViewFamilyType class, an exception will be thrown if the property is accessed for views other than StructuralPlan views.

## View range

The view range for plan views can be retrieved via the ViewPlan.GetViewRange() method. The returned PlanViewRange object can be used to find the levels which a plane is relative to and the offset of each plane from that level. It is the same information that is available in the View Range dialog in the Revit user interface:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ViewRange-76168.jpg)The following example shows how to get the top clip plane and the associated offset for a plan view

<table summary="" id="GUID-DDD3ABF7-0C89-437C-A676-8C5AA4F5F56F__TABLE_20714FC3AA944BD9AFB8A2BCA40B5565"><tbody><tr><td><b>Code Region: Getting information on the view range</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ViewRange</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(</span><span>view </span><span>is</span><span> </span><span>ViewPlan</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>ViewPlan</span><span> viewPlan </span><span>=</span><span> view </span><span>as</span><span> </span><span>ViewPlan</span><span>;</span><span>
        </span><span>PlanViewRange</span><span> viewRange </span><span>=</span><span> viewPlan</span><span>.</span><span>GetViewRange</span><span>();</span><span>

        </span><span>ElementId</span><span> topClipPlane </span><span>=</span><span> viewRange</span><span>.</span><span>GetLevelId</span><span>(</span><span>PlanViewPlane</span><span>.</span><span>TopClipPlane</span><span>);</span><span>
        </span><span>double</span><span> dOffset </span><span>=</span><span> viewRange</span><span>.</span><span>GetOffset</span><span>(</span><span>PlanViewPlane</span><span>.</span><span>TopClipPlane</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>topClipPlane</span><span>.</span><span>IntegerValue</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Element</span><span> levelAbove </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>topClipPlane</span><span>);</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>view</span><span>.</span><span>Name</span><span>,</span><span> </span><span>"Top Clip Plane: "</span><span> </span><span>+</span><span> levelAbove</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>"\r\nTop Offset: "</span><span> </span><span>+</span><span> dOffset </span><span>+</span><span> </span><span>" ft"</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Plan view underlay

The top and base levels of the underlay range can be retrieved and set from ViewPlan. Use GetUnderlayBaseLevel() and SetUnderlayBaseLevel() to access the base level for the underlay range. If the base level id is InvalidElementId then the underlay base level is not set and no elements will be displayed as underlay. When setting the base level for the underlay range, the elevation of the next highest level will be used to determine the top of the underlay range. If the level specified for the base level is the highest level, the underlay range will be unbounded and will consist of everything above the specified level.

Use GetUnderlayTopLevel() and SetUnderlayRange() to access the top level for the underlay range. If GetUnderlayTopLevel() returns InvalidElementId and the underlay base level is a valid level, then the underlay range is unbounded, and consists of everything above the underlay base level. To set the top level, you must use SetUnderlayRange() which takes ElementIds for both the base and top levels. This method will throw an exception if the elevation of the top level is not greater than the elevation of the base level.

Use the GetUnderlayOrientation() and SetUnderlayOrientation() methods to control how elements in the underlay are viewed. The UnderlayOrientation is either LookingDown (underlay elements are viewed as if looking down from above ) or LookingUp (underlay elements are viewed as if looking up from below).

The following code sets the underlay range if the current orientation is LookingDown and the top level Id is different than the new value. Then the orientation is changed to LookingUp.

<table summary="" id="GUID-DDD3ABF7-0C89-437C-A676-8C5AA4F5F56F__TABLE_8C5D382065B74F1285134EAAFBD64EB1"><tbody><tr><td><b>Code Region: Change the view underlay range</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ViewUnderlay</span><span>(</span><span>ViewPlan</span><span> planView</span><span>,</span><span> </span><span>ElementId</span><span> topLevelId</span><span>,</span><span> </span><span>ElementId</span><span> baseLevelId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(</span><span>planView</span><span>.</span><span>GetUnderlayOrientation</span><span>()</span><span> </span><span>==</span><span> </span><span>UnderlayOrientation</span><span>.</span><span>LookingDown</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>planView</span><span>.</span><span>GetUnderlayTopLevel</span><span>()</span><span> </span><span>!=</span><span> topLevelId</span><span>)</span><span>
        </span><span>{</span><span>
            planView</span><span>.</span><span>SetUnderlayRange</span><span>(</span><span>baseLevelId</span><span>,</span><span> topLevelId</span><span>);</span><span>
        </span><span>}</span><span>

        planView</span><span>.</span><span>SetUnderlayOrientation</span><span>(</span><span>UnderlayOrientation</span><span>.</span><span>LookingUp</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  ViewPlan  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  ViewDrafting  Autodesk.md ===== -->

---
created: 2026-01-28T20:51:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_ViewDrafting_html
author: 
---

# Help | ViewDrafting | Autodesk

> ## Excerpt
> Views to create unassociated, view-specific details that are not part of the modeled design.

---
Views to create unassociated, view-specific details that are not part of the modeled design.

The drafting view is not associated with the model. It allows the user to create detail drawings that are not included in the model.

-   In the drafting view, the user can create details in different view scales (coarse, fine, or medium).
    
-   You can use 2D detailing tools, including:
    
    <table summary="" id="GUID-217A0AFB-5A0C-4EC3-A417-C7F8F78D05B5__TABLE_4FA9C3F4D7BF4A4F91790596A66C169B"><tbody><tr><td><ul><li>Detail lines</li><li>Detail regions</li><li>Detail components</li><li>Insulation</li></ul></td><td><ul><li>Reference planes</li><li>Dimensions</li><li>Symbols</li><li>Text</li></ul></td></tr></tbody></table>
    

These tools are the same tools used to create a detail view.

-   Drafting views do not display model elements.

Use the static ViewDrafting.Create() method to create a drafting view. Model elements are not displayed in the drafting view.

### ImageView

The ImageView class is derived from ViewDrafting. It can be used to create rendering views containing images imported from disk. Use the static ImageView.Create(Document, ImageTypeOptions) method to create new rendering views.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/RenderingView-76170.jpg)


<!-- ===== END: Help  ViewDrafting  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  ViewSection  Autodesk.md ===== -->

---
created: 2026-01-28T20:52:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_ViewSection_html
author: 
---

# Help | ViewSection | Autodesk

> ## Excerpt
> Represents section, detail, callout and elevation views, as well as reference callouts and reference sections.

---
Represents section, detail, callout and elevation views, as well as reference callouts and reference sections.

The ViewSection class can be used to create section views, detail views, callout views, reference callouts and reference sections. It also represents elevation views.

### Section Views and Reference Sections

Section views cut through the model to expose the interior structure. The `ViewSection.CreateSection()` method creates the section view.

The viewFamilyTypeId parameter is the Id for the ViewFamilyType which will be used by the new ViewSection. The type needs to be a Section ViewFamily. The sectionBox parameter is the section view crop box. It provides the direction and extents which are required for the section view. Usually, another view's crop box is used as the parameter. You can also build a custom BoundingBoxXYZ instance to represent the direction and extents.

The following code shows how to create a section view. A bounding box for the section view is created at the center of a wall. The resulting section view will be located in the Sections (Building Section) node in the Project Browser. Note that the far clip distance will be equal to the difference of the z-coordinates of bounding box's min and max values on creation.

<table summary="" id="GUID-776D3BC5-26A3-4D3C-A30C-9E9FD6552147__TABLE_79542D1B82AC42B58D8C80894F84FCA1"><tbody><tr><td><b>Code Region: Creating a section view</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateSection</span><span>(</span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> document </span><span>=</span><span> wall</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>// Find a section view type</span><span>
    </span><span>IEnumerable</span><span>&lt;</span><span>ViewFamilyType</span><span>&gt;</span><span> viewFamilyTypes </span><span>=</span><span> </span><span>from</span><span> elem </span><span>in</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>).</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>ViewFamilyType</span><span>))</span><span>
        </span><span>let</span><span> type </span><span>=</span><span> elem </span><span>as</span><span> </span><span>ViewFamilyType</span><span>
        </span><span>where</span><span> type</span><span>.</span><span>ViewFamily</span><span> </span><span>==</span><span> </span><span>ViewFamily</span><span>.</span><span>Section</span><span>
        </span><span>select</span><span> type</span><span>;</span><span>

    </span><span>// Create a BoundingBoxXYZ instance centered on wall</span><span>
    </span><span>LocationCurve</span><span> lc </span><span>=</span><span> wall</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
    </span><span>Transform</span><span> curveTransform </span><span>=</span><span> lc</span><span>.</span><span>Curve</span><span>.</span><span>ComputeDerivatives</span><span>(</span><span>0.5</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    </span><span>// using 0.5 and "true" (to specify that the parameter is normalized) </span><span>
    </span><span>// places the transform's origin at the center of the location curve)</span><span>

    XYZ origin </span><span>=</span><span> curveTransform</span><span>.</span><span>Origin</span><span>;</span><span> </span><span>// mid-point of location curve</span><span>
    XYZ viewDirection </span><span>=</span><span> curveTransform</span><span>.</span><span>BasisX</span><span>.</span><span>Normalize</span><span>();</span><span> </span><span>// tangent vector along the location curve</span><span>
    XYZ normal </span><span>=</span><span> viewDirection</span><span>.</span><span>CrossProduct</span><span>(</span><span>XYZ</span><span>.</span><span>BasisZ</span><span>).</span><span>Normalize</span><span>();</span><span> </span><span>// location curve normal @ mid-point</span><span>

    </span><span>Transform</span><span> transform </span><span>=</span><span> </span><span>Transform</span><span>.</span><span>Identity</span><span>;</span><span>
    transform</span><span>.</span><span>Origin</span><span> </span><span>=</span><span> origin</span><span>;</span><span>
    transform</span><span>.</span><span>BasisX</span><span> </span><span>=</span><span> normal</span><span>;</span><span>
    transform</span><span>.</span><span>BasisY</span><span> </span><span>=</span><span> XYZ</span><span>.</span><span>BasisZ</span><span>;</span><span>

    </span><span>// can use this simplification because wall's "up" is vertical.</span><span>
    </span><span>// For a non-vertical situation (such as section through a sloped floor the surface normal would be needed)</span><span>
    transform</span><span>.</span><span>BasisZ</span><span> </span><span>=</span><span> normal</span><span>.</span><span>CrossProduct</span><span>(</span><span>XYZ</span><span>.</span><span>BasisZ</span><span>);</span><span>

    </span><span>BoundingBoxXYZ</span><span> sectionBox </span><span>=</span><span> </span><span>new</span><span> </span><span>BoundingBoxXYZ</span><span>();</span><span>
    sectionBox</span><span>.</span><span>Transform</span><span> </span><span>=</span><span> transform</span><span>;</span><span>
    sectionBox</span><span>.</span><span>Min</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>10</span><span>,</span><span>0</span><span>,</span><span>0</span><span>);</span><span>
    sectionBox</span><span>.</span><span>Max</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span>12</span><span>,</span><span>5</span><span>);</span><span>
    </span><span>// Min &amp; Max X values (-10 &amp; 10) define the section line length on each side of the wall</span><span>
    </span><span>// Max Y (12) is the height of the section box// Max Z (5) is the far clip offset</span><span>

    </span><span>// Create a new view section.</span><span>
    </span><span>ViewSection</span><span> viewSection </span><span>=</span><span> </span><span>ViewSection</span><span>.</span><span>CreateSection</span><span>(</span><span>document</span><span>,</span><span> viewFamilyTypes</span><span>.</span><span>First</span><span>().</span><span>Id</span><span>,</span><span> sectionBox</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Reference sections are sections that reference an existing view. Revit does not add a new view when you create a new reference section.

<table summary="" id="GUID-776D3BC5-26A3-4D3C-A30C-9E9FD6552147__TABLE_A17BAA1C21AC469380524C5DAB48694F"><tbody><tr><td><b>Code Region: ViewSection.CreateReferenceSection()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>ViewSection</span><span> </span><span>ViewSection</span><span>.</span><span>CreateReferenceSection</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>ElementId</span><span> parentViewId</span><span>,</span><span> </span><span>ElementId</span><span> viewIdToReference</span><span>,</span><span> XYZ headPoint</span><span>,</span><span> XYZ tailPoint</span><span>);</span></code></pre></td></tr></tbody></table>

The parentViewId parameter is the Id of the view in which the new reference section marker will appear. Reference sections can be created in FloorPlan, CeilingPlan, StructuralPlan, Section, Elevation, Drafting, and Detail views. The viewIdToReference can be the Id of a Detail, Drafting or Section view. The ViewFamilyType of the referenced view will be used by the new reference section. The two XYZ points will determine the location of the section marker's head in the parent view.

#### Detail Views

A detail view is a view of the model that appears as a callout or section in other views. This type of view typically represents the model at finer scales of detail than in the parent view. It is used to add more information to specific parts of the model. The static ViewSection.CreateDetail() method is used to create a new detail ViewSection.

<table summary="" id="GUID-776D3BC5-26A3-4D3C-A30C-9E9FD6552147__TABLE_ADE817B01A9347019D9248EBCEA23F74"><tbody><tr><td><b>Code Region: ViewSection.CreateDetail()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>ViewSection</span><span> </span><span>ViewSection</span><span>.</span><span>CreateDetail</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>ElementId</span><span> viewFamilyTypeId</span><span>,</span><span> </span><span>BoundingBoxXYZ</span><span> sectionBox</span><span>);</span></code></pre></td></tr></tbody></table>

The viewFamilyTypeId parameter is the Id for the ViewFamilyType which will be used by the new ViewSection. The type needs to be a Detail ViewFamily. Just as for a standard section view, the sectionBox parameter is the section view crop box. It provides the direction and extents which are required for the section view.

When a new detail ViewSection is added, it will appear in the Detail Views (Detail) node in the Project Browser.

#### Elevation Views

An elevation view is a cross-section of the model where level lines are displayed. An elevation view is represented by the ViewSection class. However, unlike the other types of section views, you cannot create elevation views using a static method on the ViewSection class. To create an elevation view, first create an elevation marker, then use the marker to generate the elevation view. The newly created elevation view will appear in the Elevations (Building Elevation) node in the Project Browser. It will be assigned a unique name.

The following example creates an elevation view based on the location of a beam.

<table summary="" id="GUID-776D3BC5-26A3-4D3C-A30C-9E9FD6552147__TABLE_C53E0D4040E0492B86043A2AAF6E64C7"><tbody><tr><td><b>Code Region: Creating an Elevation View</b></td></tr><tr><td><pre><code><span>ViewSection</span><span> </span><span>CreateElevationView</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> beam</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find an elevation view type</span><span>
    </span><span>IEnumerable</span><span>&lt;</span><span>ViewFamilyType</span><span>&gt;</span><span> viewFamilyTypes </span><span>=</span><span> </span><span>from</span><span> elem </span><span>in</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>).</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>ViewFamilyType</span><span>))</span><span>
                                                    </span><span>let</span><span> type </span><span>=</span><span> elem </span><span>as</span><span> </span><span>ViewFamilyType</span><span>
                                                    </span><span>where</span><span> type</span><span>.</span><span>ViewFamily</span><span> </span><span>==</span><span> </span><span>ViewFamily</span><span>.</span><span>Elevation</span><span>
                                                    </span><span>select</span><span> type</span><span>;</span><span>

    </span><span>LocationCurve</span><span> lc </span><span>=</span><span> beam</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
    XYZ xyz </span><span>=</span><span> lc</span><span>.</span><span>Curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>
    </span><span>ElevationMarker</span><span> marker </span><span>=</span><span> </span><span>ElevationMarker</span><span>.</span><span>CreateElevationMarker</span><span>(</span><span>document</span><span>,</span><span> viewFamilyTypes</span><span>.</span><span>First</span><span>().</span><span>Id</span><span>,</span><span> xyz</span><span>,</span><span> </span><span>1</span><span>);</span><span>
    </span><span>ViewSection</span><span> elevationView </span><span>=</span><span> marker</span><span>.</span><span>CreateElevation</span><span>(</span><span>document</span><span>,</span><span> document</span><span>.</span><span>ActiveView</span><span>.</span><span>Id</span><span>,</span><span> </span><span>1</span><span>);</span><span>

    </span><span>return</span><span> elevationView</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The ElevationMarker.CreateElevation() method takes an id of a ViewPlan as a parameter. That is the ViewPlan in which the ElevationMarker is visible. The new elevation ViewSection will derive its extents and inherit settings from the ViewPlan. The last parameter is the index on the ElevationMarker where the new elevation view will be placed. The index on the ElevationMarker must be valid and unused. The view's direction is determined by the index.

#### Split Sections

These methods identify if a section view is split and return the offset for the specified split crop region:

-   DBViewSection.IsSplitSection()
-   ViewCropRegionShapeManager.GetSplitRegionOffset()

#### Callouts and Reference Callouts

A callout shows part of another view at a larger scale. Callout views can be created using the static method ViewSection.CreateCallout(). Callouts can be created in FloorPlan, CeilingPlan, StructuralPlan, Section, Elevation, Drafting and Detail views. The resulting view will be either a ViewSection, ViewPlan or ViewDetail depending on the ViewFamilyType used and will appear in the corresponding node in the Project Browser.

-   `View.GetCalloutParentId()` returns the ID of a view which this callout references, or InvalidElementId if there is not parent.
-   `View.IsCallout` identifies if the view is a callout view

<table summary="" id="GUID-776D3BC5-26A3-4D3C-A30C-9E9FD6552147__TABLE_509E0BD2824E425EB5E8F1B71B1A73C6"><tbody><tr><td><b>Code Region: ViewSection.CreateCallout()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>ViewSection</span><span> </span><span>ViewSection</span><span>.</span><span>CreateCallout</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> 
                                            </span><span>ElementId</span><span> parentViewId</span><span>,</span><span> 
                                            </span><span>ElementId</span><span> viewFamilyTypeId</span><span>,</span><span>
                                            XYZ point1</span><span>,</span><span>
                                            XYZ point2</span><span>);</span></code></pre></td></tr></tbody></table>

The parent view Id parameter can be the Id of any type of View on which callouts can be created. The point parameters determine the extents of the callout symbol in the parent view.A reference callout is a callout that refers to an existing view. When you add a reference callout, Revit does not create a view in the project. Instead, it creates a pointer to a specified, existing view. Multiple reference callouts can point to the same view.

<table summary="" id="GUID-776D3BC5-26A3-4D3C-A30C-9E9FD6552147__TABLE_6571A3EF8EB84E3AA770C68F56805518"><tbody><tr><td><b>Code Region: ViewSection.CreateReferenceCallout()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>ViewSection</span><span> </span><span>ViewSection</span><span>.</span><span>CreateReferenceCallout</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> 
                                                      </span><span>ElementId</span><span> parentViewId</span><span>,</span><span> 
                                                      </span><span>ElementId</span><span> viewIdToReference</span><span>,</span><span>
                                                      XYZ point1</span><span>,</span><span>
                                                      XYZ point2</span><span>);</span></code></pre></td></tr></tbody></table>

Creation of a reference callout is similar to creation of a callout. But rather than having the Id of the ViewFamilyType for the callout as a parameter, the CreateReferenceCallout() method takes the Id of the view to reference. The ViewFamilyType of the referenced view will be used by the new reference callout.

Only cropped views can be referenced, unless the referenced view is a Drafting view. Drafting views can always be referenced regardless of the parent view type. Elevation views can be referenced from Elevation and Drafting parent views. Section views can be referenced from Section and Drafting parent views. Detail views can be referenced from all parent views except for in FloorPlan, CeilingPlan and StructuralPlan parent views where only horizontally-oriented Detail views can be referenced. FloorPlan, CeilingPlan and StructuralPlan views can be referenced from FloorPlan, CeilingPlan and StructuralPlan parent views.

The following example creates a new callout using a Detail ViewFamilyType and then uses the new callout view to create a reference callout.

<table summary="" id="GUID-776D3BC5-26A3-4D3C-A30C-9E9FD6552147__TABLE_1BDDB578E66A4106B95EDF1555E97D8E"><tbody><tr><td><b>Code Region: Creating a callout and reference callout</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateCalloutView</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>View</span><span> parentView</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find a detail view type</span><span>
    </span><span>IEnumerable</span><span>&lt;</span><span>ViewFamilyType</span><span>&gt;</span><span> viewFamilyTypes </span><span>=</span><span> </span><span>from</span><span> elem </span><span>in</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>).</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>ViewFamilyType</span><span>))</span><span>
                                                    </span><span>let</span><span> type </span><span>=</span><span> elem </span><span>as</span><span> </span><span>ViewFamilyType</span><span>
                                                    </span><span>where</span><span> type</span><span>.</span><span>ViewFamily</span><span> </span><span>==</span><span> </span><span>ViewFamily</span><span>.</span><span>Detail</span><span>
                                                    </span><span>select</span><span> type</span><span>;</span><span>

    </span><span>ElementId</span><span> viewFamilyTypeId </span><span>=</span><span> viewFamilyTypes</span><span>.</span><span>First</span><span>().</span><span>Id</span><span>;</span><span>  
    XYZ point1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>2</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>2</span><span>);</span><span>
    XYZ point2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>30</span><span>,</span><span> </span><span>30</span><span>,</span><span> </span><span>30</span><span>);</span><span>
    </span><span>ElementId</span><span> parentViewId </span><span>=</span><span> parentView</span><span>.</span><span>Id</span><span>;</span><span>  </span><span>// a ViewPlan</span><span>
    </span><span>View</span><span> view </span><span>=</span><span> </span><span>ViewSection</span><span>.</span><span>CreateCallout</span><span>(</span><span>document</span><span>,</span><span> parentViewId</span><span>,</span><span> viewFamilyTypeId</span><span>,</span><span> point1</span><span>,</span><span> point2</span><span>);</span><span>

    </span><span>ViewSection</span><span>.</span><span>CreateReferenceCallout</span><span>(</span><span>document</span><span>,</span><span> parentViewId</span><span>,</span><span> view</span><span>.</span><span>Id</span><span>,</span><span> point1</span><span>,</span><span> point2</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  ViewSection  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  ViewSheet  Autodesk.md ===== -->

---
created: 2026-01-28T20:52:08 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_ViewSheet_html
author: 
---

# Help | ViewSheet | Autodesk

> ## Excerpt
> A sheet contains views and a title block. When creating a sheet view with the ViewSheet.Create() method, a title block family symbol Id is a required parameter for the method. A title block family symbol can be found using a FilteredElementCollector.

---
A sheet contains views and a title block. When creating a sheet view with the ViewSheet.Create() method, a title block family symbol Id is a required parameter for the method. A title block family symbol can be found using a FilteredElementCollector.

<table summary="" id="GUID-48DFC75D-66DC-434C-B592-D60D40E29348__TABLE_7705E6512C3D47419E87909721D60B7D"><tbody><tr><td><b>Code Region: ViewSheet.Create()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>ViewSheet</span><span> </span><span>ViewSheet</span><span>.</span><span>Create</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>ElementId</span><span> titleBlockTypeId</span><span>);</span></code></pre></td></tr></tbody></table>

The newly created sheet has no views. The Viewport.Create() method is used to add views. The Viewport class is used to add regular views to a view sheet, i.e. plan, elevation, drafting and three dimensional. To add schedules to a view, use ScheduleSheetInstance.Create() instead.

The `View.GetPlacementOnSheetStatus` method returns a `ViewPlacementOnSheetStatus` enum that describes if the view is placed on a sheet. Some views, such as schedules, can be partially placed on a sheet by divided them into segments and placing only some of those segments on a sheet.

The property `Viewport.LabelOffset` controls the two-dimensional label offset from left bottom corner of the viewport (as established with Rotation set to None) to the left end of the viewport label line. The property `Viewport.LabelLineLength` controls the length of the viewport label line in sheet space.

<table summary="" id="GUID-48DFC75D-66DC-434C-B592-D60D40E29348__TABLE_119C0C6953834413A5BC13C8917CF9AE"><tbody><tr><td><b>Code Region: Add two views aligned at left corner</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>PlaceAlignedViewsAtLeftCorner</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> fec </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    fec</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>ViewPlan</span><span>));</span><span>
    </span><span>var</span><span> viewPlans </span><span>=</span><span> fec</span><span>.</span><span>Cast</span><span>&lt;</span><span>ViewPlan</span><span>&gt;().</span><span>Where</span><span>&lt;</span><span>ViewPlan</span><span>&gt;(</span><span>vp </span><span>=&gt;</span><span> </span><span>!</span><span>vp</span><span>.</span><span>IsTemplate</span><span> </span><span>&amp;&amp;</span><span> vp</span><span>.</span><span>ViewType</span><span> </span><span>==</span><span> </span><span>ViewType</span><span>.</span><span>CeilingPlan</span><span>);</span><span>

    </span><span>ViewPlan</span><span> vp1 </span><span>=</span><span> viewPlans</span><span>.</span><span>ElementAt</span><span>(</span><span>0</span><span>);</span><span>
    </span><span>ViewPlan</span><span> vp2 </span><span>=</span><span> viewPlans</span><span>.</span><span>ElementAt</span><span>(</span><span>1</span><span>);</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Place on sheet"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// Add two viewports distinct from one another</span><span>
        </span><span>ViewSheet</span><span> vs </span><span>=</span><span> </span><span>ViewSheet</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>);</span><span>
        </span><span>Viewport</span><span> viewport1 </span><span>=</span><span> </span><span>Viewport</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> vs</span><span>.</span><span>Id</span><span>,</span><span> vp1</span><span>.</span><span>Id</span><span>,</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>
        </span><span>Viewport</span><span> viewport2 </span><span>=</span><span> </span><span>Viewport</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> vs</span><span>.</span><span>Id</span><span>,</span><span> vp2</span><span>.</span><span>Id</span><span>,</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>5</span><span>,</span><span> </span><span>0</span><span>));</span><span>

        doc</span><span>.</span><span>Regenerate</span><span>();</span><span>

        </span><span>// Calculate the necessary move vector to align the lower left corner</span><span>
        </span><span>Outline</span><span> outline1 </span><span>=</span><span> viewport1</span><span>.</span><span>GetBoxOutline</span><span>();</span><span>
        </span><span>Outline</span><span> outline2 </span><span>=</span><span> viewport2</span><span>.</span><span>GetBoxOutline</span><span>();</span><span>
        XYZ boxCenter </span><span>=</span><span> viewport2</span><span>.</span><span>GetBoxCenter</span><span>();</span><span>
        XYZ vectorToCenter </span><span>=</span><span> boxCenter </span><span>-</span><span> outline2</span><span>.</span><span>MinimumPoint</span><span>;</span><span>
        XYZ newCenter </span><span>=</span><span> outline1</span><span>.</span><span>MinimumPoint</span><span> </span><span>+</span><span> vectorToCenter</span><span>;</span><span>

        </span><span>// Move the viewport to the new location</span><span>
        viewport2</span><span>.</span><span>SetBoxCenter</span><span>(</span><span>newCenter</span><span>);</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

-   The XYZ location parameter identifies where the added views are located. It points to the added view's center coordinate (measured in inches).
-   The coordinates, \[0, 0\], are relative to the sheet's lower left corner.

Viewports placed on sheets can have the associated view swapped for another view in the model by editing the `Viewport.ViewId` property. When this swap is done, the `Viewport.ViewportPositioning` property specifies how the viewport will be positioned on the sheet when swapped to another view by maintaining either the viewport center or the view origin.

Each sheet has a unique sheet number in the complete drawing set. The number is displayed before the sheet name in the Project Browser. It is convenient to use the sheet number in a view title to cross-reference the sheets in your drawing set. You can retrieve or modify the number using the SheetNumber property. The number must be unique; otherwise an exception is thrown when you set the number to a duplicate value.

The following example illustrates how to create and print a sheet view. Begin by finding an available title block in the document (using a filter in this case) and use it to create the sheet view. Next, add a 3D view. The view is placed with its lower left-hand corner at the center of the sheet. Finally, print the sheet by calling the View.Print() method.

<table summary="" id="GUID-48DFC75D-66DC-434C-B592-D60D40E29348__TABLE_F482645A2CCD43E18C862DAF950546CF"><tbody><tr><td><b>Code Region: Creating a sheet view</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateSheetView</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>View3D</span><span> view3D</span><span>)</span><span>
</span><span>{</span><span>

    </span><span>// Get an available title block from document</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>));</span><span>
    collector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_TitleBlocks</span><span>);</span><span>

    </span><span>FamilySymbol</span><span> fs </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>fs </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Create a new ViewSheet"</span><span>))</span><span>
        </span><span>{</span><span>
            t</span><span>.</span><span>Start</span><span>();</span><span>
            </span><span>try</span><span>
            </span><span>{</span><span>
                </span><span>// Create a sheet view</span><span>
                </span><span>ViewSheet</span><span> viewSheet </span><span>=</span><span> </span><span>ViewSheet</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> fs</span><span>.</span><span>Id</span><span>);</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> viewSheet</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Failed to create new ViewSheet."</span><span>);</span><span>
                </span><span>}</span><span>

                </span><span>// Add passed in view onto the center of the sheet</span><span>
                UV location </span><span>=</span><span> </span><span>new</span><span> UV</span><span>((</span><span>viewSheet</span><span>.</span><span>Outline</span><span>.</span><span>Max</span><span>.</span><span>U </span><span>-</span><span> viewSheet</span><span>.</span><span>Outline</span><span>.</span><span>Min</span><span>.</span><span>U</span><span>)</span><span> </span><span>/</span><span> </span><span>2</span><span>,</span><span>
                                        </span><span>(</span><span>viewSheet</span><span>.</span><span>Outline</span><span>.</span><span>Max</span><span>.</span><span>V </span><span>-</span><span> viewSheet</span><span>.</span><span>Outline</span><span>.</span><span>Min</span><span>.</span><span>V</span><span>)</span><span> </span><span>/</span><span> </span><span>2</span><span>);</span><span>

                </span><span>//viewSheet.AddView(view3D, location);</span><span>
                </span><span>Viewport</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> viewSheet</span><span>.</span><span>Id</span><span>,</span><span> view3D</span><span>.</span><span>Id</span><span>,</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>location</span><span>.</span><span>U</span><span>,</span><span> location</span><span>.</span><span>V</span><span>,</span><span> </span><span>0</span><span>));</span><span>

                </span><span>// Print the sheet out</span><span>
                </span><span>if</span><span> </span><span>(</span><span>viewSheet</span><span>.</span><span>CanBePrinted</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>TaskDialog</span><span> taskDialog </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Revit"</span><span>);</span><span>
                    taskDialog</span><span>.</span><span>MainContent</span><span> </span><span>=</span><span> </span><span>"Print the sheet?"</span><span>;</span><span>
                    </span><span>TaskDialogCommonButtons</span><span> buttons </span><span>=</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Yes</span><span> </span><span>|</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>No</span><span>;</span><span>
                    taskDialog</span><span>.</span><span>CommonButtons</span><span> </span><span>=</span><span> buttons</span><span>;</span><span>
                    </span><span>TaskDialogResult</span><span> result </span><span>=</span><span> taskDialog</span><span>.</span><span>Show</span><span>();</span><span>

                    </span><span>if</span><span> </span><span>(</span><span>result </span><span>==</span><span> </span><span>TaskDialogResult</span><span>.</span><span>Yes</span><span>)</span><span>
                    </span><span>{</span><span>
                        viewSheet</span><span>.</span><span>Print</span><span>();</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>

                t</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
            </span><span>catch</span><span>
            </span><span>{</span><span>
                t</span><span>.</span><span>RollBack</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: You cannot add a sheet view to another sheet and you cannot add a view to more than one sheet; otherwise an argument exception occurs.

### Duplicating a sheet

When duplicating a sheet, the SheetDuplicateOption enum allows you to indicate what information should be copied when duplicating a sheet. Its values are:

-   DuplicateEmptySheet - Only copies the title block.
-   DuplicateSheetWithDetailing - Copies the title block and details.
-   DuplicateSheetWithViewsOnly- Copies the title block, details, viewports and contained views. The newly created sheet will reference the newly duplicated views.
-   DuplicateSheetWithViewsAndDetailing - Copies the title block, details, and viewports. Duplicates the sheet's contained views with detailing. The newly created sheet will reference the newly duplicated views.
-   DuplicateSheetWithViewsAsDependent - Copies the title block, details, and viewports. Duplicates the sheet's contained views as dependent. The newly created sheet will reference the newly duplicated dependent views.

### Revisions on Sheets

The ViewSheet class has several methods for working with revision and revision clouds on sheets.

-   **GetAllRevisionIds()**\- Gets the ordered array of Revisions which participate in the sheet's revision schedules.
-   **GetAdditionalRevisionIds()**\- Gets the Revisions that are additionally included in the sheet's revision schedules.
-   **SetAdditionalRevisionIds()**\- Sets the Revisions to additionally include in the sheet's revision schedules.
-   **GetCurrentRevision()**\- Returns the most recent numbered Revision shown on this ViewSheet.
-   **GetRevisionCloudNumberOnSheet()**\- Gets the Revision Number for a RevisionCloud on this sheet when the numbering in the project is by sheet.
-   **GetRevisionNumberOnSheet()** - Gets the Revision Number for a particular Revision as it will appear on this sheet when the numbering in the project is by sheet. The Revisions are ordered according to the revision sequence in the project. Additionally included Revisions will always participate in the sheet's revision schedules. Normally a Revision is scheduled in the revision schedule because one of its associated RevisionClouds is present on the sheet.

The following code sample demonstrates how to add additional revisions to the sheet that match a given criteria.

<table summary="" id="GUID-48DFC75D-66DC-434C-B592-D60D40E29348__TABLE_CAF21DDC99F144ED962F6C3822552118"><tbody><tr><td><b>Code Region: Add additional revisions to sheet</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddAdditionalRevisionsToSheet</span><span>(</span><span>ViewSheet</span><span> viewSheet</span><span>,</span><span> </span><span>String</span><span> toMatch</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> viewSheet</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> revisions </span><span>=</span><span> viewSheet</span><span>.</span><span>GetAdditionalRevisionIds</span><span>();</span><span>

    </span><span>// Find revisions whose description matches input string</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    collector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Revisions</span><span>);</span><span>
    collector</span><span>.</span><span>WhereElementIsNotElementType</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>revisions</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
        collector</span><span>.</span><span>Excluding</span><span>(</span><span>revisions</span><span>);</span><span>

    </span><span>// Check if revision should be added</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> revision </span><span>in</span><span> collector</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Parameter</span><span> descriptionParam </span><span>=</span><span> revision</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>ProjectRevisionRevisionDescription</span><span>);</span><span>
        </span><span>String</span><span> description </span><span>=</span><span> descriptionParam</span><span>.</span><span>AsString</span><span>();</span><span>
        </span><span>if</span><span> </span><span>(</span><span>description</span><span>.</span><span>Contains</span><span>(</span><span>toMatch</span><span>))</span><span>
            revisions</span><span>.</span><span>Add</span><span>(</span><span>revision</span><span>.</span><span>Id</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>if</span><span> </span><span>(</span><span>revisions</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Apply the new list of revisions</span><span>
        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Add revisions to sheet"</span><span>))</span><span>
        </span><span>{</span><span>
            t</span><span>.</span><span>Start</span><span>();</span><span>
            viewSheet</span><span>.</span><span>SetAdditionalRevisionIds</span><span>(</span><span>revisions</span><span>);</span><span>
            t</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Printer Setup

You may want to change the settings of the printer before printing a sheet. The API exposes the settings for the printer with the PrintManager class, and related Autodesk.Revit.DB classes:

<table summary="" id="GUID-48DFC75D-66DC-434C-B592-D60D40E29348__TABLE_6738648BCDFC439CA3B1D2A3CCF21462"><tbody><tr><td><b>Class</b></td><td><b>Functionality</b></td></tr><tr><td>Autodesk.Revit.DB.PrintManager</td><td>Represents the Print information in Print Dialog (File-&gt;Print) within the Revit UI.</td></tr><tr><td>Autodesk.Revit.DB.PrintParameters</td><td>An object that contains settings used for printing the document.</td></tr><tr><td>Autodesk.Revit.DB.PrintSetup</td><td>Represents the Print Setup (File-&gt;Print Setup...) within the Revit UI.</td></tr><tr><td>Autodesk.Revit.DB.PaperSize</td><td>An object that represents a Paper Size of Print Setup within the Autodesk Revit project.</td></tr><tr><td>Autodesk.Revit.DB.PaperSizeSet</td><td>A set that can contain any number of paper size objects.</td></tr><tr><td>Autodesk.Revit.DB.PaperSource</td><td>An object that represents a Paper Source of Print Setup within the Autodesk Revit project.</td></tr><tr><td>Autodesk.Revit.DB.PaperSourceSet</td><td>A set that can contain any number of paper source objects.</td></tr><tr><td>Autodesk.Revit.DB.ViewSheetSetting</td><td>Represents the View/Sheet Set (File-&gt;Print) within the Revit UI.</td></tr><tr><td>Autodesk.Revit.DB.PrintSetting</td><td>Represents the Print Setup (File-&gt;Print Setup...) within the Revit UI.</td></tr></tbody></table>

For an example of code that uses these objects, see the ViewPrinter sample application that is included with the Revit Platform SDK.


<!-- ===== END: Help  ViewSheet  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  TableView  Autodesk.md ===== -->

---
created: 2026-01-28T20:52:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_html
author: 
---

# Help | TableView | Autodesk

> ## Excerpt
> This class represents a view that shows a table of data.

---
This class represents a view that shows a table of data.

TableView is the base class for ViewSchedule and PanelScheduleView.


<!-- ===== END: Help  TableView  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Schedule Classes  Autodesk.md ===== -->

---
created: 2026-01-28T20:52:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_Schedule_Classes_html
author: 
---

# Help | Schedule Classes | Autodesk

> ## Excerpt
> Schedule views use several supporting classes.

---
Schedule views use several supporting classes.

TableView is a class that represents a view that shows a table and it is the base class for ViewSchedule and PanelScheduleView. It has an associated TableData class which contains one or more sections. For ViewSchedule, there is only one header and one body section.

The TableSectionData class represents a contiguous set of cells arranged in rows and columns. For a ViewSchedule the cell contents of TableSectionData are generated from the ScheduleDefinition and parameters. Also, for ViewSchedules, while the header section has read/write permissions, the body section is read-only.

### Working with data in a schedule

The actual data for a table is contained in the TableData class. Although the TableData object cannot be obtained directly from the TableView class, both child classes have a GetTableData() method. For ViewSchedule, this method returns a TableData object. For a PanelScheduleView, GetTableData() returns a PanelScheduleData object, which derives from the TableData base class. The TableData class holds most of the data that describe the style of the rows, columns, and cells in a table. PanelScheduleData provides additional methods related specifically to panel schedules.

### Working with rows, columns and cells

Data in a table is broken down into sections. To work with the rows, columns and cells of the TableData, it is necessary to get the a TableSectionData object. TableData.GetSectionData() can be called with either an integer to the requested section data, or using the SectionType (i.e. Header or Body).

The TableSectionData class can be used to insert or remove rows or columns, format cells, and to get details of the cells that make up that section of the schedule, such as the cell type (i.e. Text or Graphic) or the cell's category id.

In the following example, a new row is added to the header section of the schedule and the text is set for the newly created cell. Note that the first row of the header section defaults to the title when created with the UI.

<table summary="" id="GUID-76A3927E-6DA6-495F-A89C-00F760E3702C__TABLE_EF29114353B64BFAAB5705A9B97E50F6"><tbody><tr><td><b>Code Region: Inserting a row</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateSubtitle</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>TableData</span><span> colTableData </span><span>=</span><span> schedule</span><span>.</span><span>GetTableData</span><span>();</span><span>

    </span><span>TableSectionData</span><span> tsd </span><span>=</span><span> colTableData</span><span>.</span><span>GetSectionData</span><span>(</span><span>SectionType</span><span>.</span><span>Header</span><span>);</span><span>
    tsd</span><span>.</span><span>InsertRow</span><span>(</span><span>tsd</span><span>.</span><span>FirstRowNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>);</span><span>
    tsd</span><span>.</span><span>SetCellText</span><span>(</span><span>tsd</span><span>.</span><span>FirstRowNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>,</span><span> tsd</span><span>.</span><span>FirstColumnNumber</span><span>,</span><span> </span><span>"Schedule of column top and base levels with offsets"</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Also note, in the code example above, it uses the properties FirstRowNumber and FirstColumnNumber. In some sections the row or column numbers might start with 0, or they might start with 1. These properties should always be used in place of a hardcoded 0 or 1.

In the following example, a new single-category schedule is created with a custom header section.

<table summary="" id="GUID-76A3927E-6DA6-495F-A89C-00F760E3702C__TABLE_DF3F34074A0444F58E0D14AD9E616839"><tbody><tr><td><b>Code Region: Customizing the header section</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateSingleCategoryScheduleWithSimpleHeaderSection</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create single-category with custom headers"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>// Build schedule</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>ViewSchedule</span><span> vs </span><span>=</span><span> </span><span>ViewSchedule</span><span>.</span><span>CreateSchedule</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Windows</span><span>));</span><span>

        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_HEIGHT</span><span>));</span><span>
        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_WIDTH</span><span>));</span><span>
        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>ALL_MODEL_MARK</span><span>));</span><span>
        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>ALL_MODEL_COST</span><span>));</span><span>

        doc</span><span>.</span><span>Regenerate</span><span>();</span><span>

        </span><span>// Get header section</span><span>
        </span><span>TableSectionData</span><span> data </span><span>=</span><span> vs</span><span>.</span><span>GetTableData</span><span>().</span><span>GetSectionData</span><span>(</span><span>SectionType</span><span>.</span><span>Header</span><span>);</span><span>

        </span><span>int</span><span> rowNumber </span><span>=</span><span> data</span><span>.</span><span>LastRowNumber</span><span>;</span><span>
        </span><span>int</span><span> columnNumber </span><span>=</span><span> data</span><span>.</span><span>LastColumnNumber</span><span>;</span><span>

        </span><span>// Get the overall width of the table so that the new columns can be resized properly</span><span>
        </span><span>double</span><span> tableWidth </span><span>=</span><span> data</span><span>.</span><span>GetColumnWidth</span><span>(</span><span>columnNumber</span><span>);</span><span>

        data</span><span>.</span><span>InsertColumn</span><span>(</span><span>columnNumber</span><span>);</span><span>
        data</span><span>.</span><span>InsertColumn</span><span>(</span><span>columnNumber</span><span>);</span><span>

        </span><span>// Refresh data to be sure that schedule is ready for text insertion</span><span>
        vs</span><span>.</span><span>RefreshData</span><span>();</span><span>

        </span><span>//Set text to the first header cell</span><span>
        data</span><span>.</span><span>SetCellText</span><span>(</span><span>rowNumber</span><span>,</span><span> data</span><span>.</span><span>FirstColumnNumber</span><span>,</span><span> </span><span>"Special Window Schedule Text"</span><span>);</span><span>

        </span><span>// Set width of first column</span><span>
        data</span><span>.</span><span>SetColumnWidth</span><span>(</span><span>data</span><span>.</span><span>FirstColumnNumber</span><span>,</span><span> tableWidth </span><span>/</span><span> </span><span>3.0</span><span>);</span><span>

        </span><span>//Set a different parameter to the second cell - the project name</span><span>
        data</span><span>.</span><span>SetCellParamIdAndCategoryId</span><span>(</span><span>rowNumber</span><span>,</span><span> data</span><span>.</span><span>FirstRowNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>PROJECT_NAME</span><span>),</span><span>
                                            </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_ProjectInformation</span><span>));</span><span>
        data</span><span>.</span><span>SetColumnWidth</span><span>(</span><span>data</span><span>.</span><span>FirstColumnNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>,</span><span> tableWidth </span><span>/</span><span> </span><span>3.0</span><span>);</span><span>

        </span><span>//Set the third column as the schedule view name - use the special category for schedule parameters for this</span><span>
        data</span><span>.</span><span>SetCellParamIdAndCategoryId</span><span>(</span><span>rowNumber</span><span>,</span><span> data</span><span>.</span><span>LastColumnNumber</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>VIEW_NAME</span><span>),</span><span>
                                            </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_ScheduleViewParamGroup</span><span>));</span><span>
        data</span><span>.</span><span>SetColumnWidth</span><span>(</span><span>data</span><span>.</span><span>LastColumnNumber</span><span>,</span><span> tableWidth </span><span>/</span><span> </span><span>3.0</span><span>);</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddRegularFieldToSchedule</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>ElementId</span><span> paramId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>

    </span><span>// Find a matching SchedulableField</span><span>
    </span><span>SchedulableField</span><span> schedulableField </span><span>=</span><span>
        definition</span><span>.</span><span>GetSchedulableFields</span><span>().</span><span>FirstOrDefault</span><span>&lt;</span><span>SchedulableField</span><span>&gt;(</span><span>sf </span><span>=&gt;</span><span> sf</span><span>.</span><span>ParameterId</span><span> </span><span>==</span><span> paramId</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>schedulableField </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Add the found field</span><span>
        definition</span><span>.</span><span>AddField</span><span>(</span><span>schedulableField</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The style of rows, columns, or individual cells can be customized for schedules. This includes the ability to set the border line style for all four sides of cells, as well as cell color and text appearance (i.e. color, font, size). For regular schedules, this can only be done in the header section of the table.

In the example below, the font of the subtitle of a ViewSchedule (assumed to be the second row of the header section) is set to bold and the font size is set to 10.

<table summary="" id="GUID-76A3927E-6DA6-495F-A89C-00F760E3702C__TABLE_EA627D36449B46249B78B567B38A93B6"><tbody><tr><td><b>Code Region: Formatting cells</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FormatSubtitle</span><span>(</span><span>ViewSchedule</span><span> colSchedule</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>TableData</span><span> colTableData </span><span>=</span><span> colSchedule</span><span>.</span><span>GetTableData</span><span>();</span><span>

    </span><span>TableSectionData</span><span> tsd </span><span>=</span><span> colTableData</span><span>.</span><span>GetSectionData</span><span>(</span><span>SectionType</span><span>.</span><span>Header</span><span>);</span><span>
    </span><span>// Subtitle is second row, first column</span><span>
    </span><span>if</span><span> </span><span>(</span><span>tsd</span><span>.</span><span>AllowOverrideCellStyle</span><span>(</span><span>tsd</span><span>.</span><span>FirstRowNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>,</span><span> tsd</span><span>.</span><span>FirstColumnNumber</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>TableCellStyle</span><span> tcs </span><span>=</span><span> </span><span>new</span><span> </span><span>TableCellStyle</span><span>();</span><span>
        </span><span>TableCellStyleOverrideOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>TableCellStyleOverrideOptions</span><span>();</span><span>
        options</span><span>.</span><span>FontSize</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        options</span><span>.</span><span>Bold</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        tcs</span><span>.</span><span>SetCellStyleOverrideOptions</span><span>(</span><span>options</span><span>);</span><span>
        tcs</span><span>.</span><span>IsFontBold</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        tcs</span><span>.</span><span>TextSize</span><span> </span><span>=</span><span> </span><span>10</span><span>;</span><span>
        tsd</span><span>.</span><span>SetCellStyle</span><span>(</span><span>tsd</span><span>.</span><span>FirstRowNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>,</span><span> tsd</span><span>.</span><span>FirstColumnNumber</span><span>,</span><span> tcs</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Schedule Classes  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  ViewSchedule  Autodesk.md ===== -->

---
created: 2026-01-28T20:52:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_ViewSchedule_html
author: 
---

# Help | ViewSchedule | Autodesk

> ## Excerpt
> A schedule is a tabular representation of data. A typical schedule shows all elements of a category (doors, rooms, etc.) with each row representing an element and each column representing a parameter.

---
A schedule is a tabular representation of data. A typical schedule shows all elements of a category (doors, rooms, etc.) with each row representing an element and each column representing a parameter.

The ViewSchedule class represents schedules and other schedule-like views, including single-category and multi-category schedules, key schedules, material takeoffs, view lists, sheet lists, keynote legends, revision schedules, and note blocks.

The ViewSchedule.Export() method will export the schedule data to a text file.

TableData.ZoomLevel allows the user to set the zoom level of a schedule in a tabular view. This setting will not change the size of text, rows, or columns in a sheet view. Additionally, the setting is temporary and only applies to the current session.

## Placing Schedules on Sheets

The static ScheduleSheetInstance.Create() method creates an instance of a schedule on a sheet. It requires the ID of the sheet where the schedule will be placed, the ID of the schedule view, and the XYZ location on the sheet where the schedule will be placed. The ScheduleSheetInstance object has properties to access the ID of the "primary" schedule that generates this ScheduleSheetInstance, the rotation of the schedule on the sheet, the location on the sheet where the schedule is placed (in sheet coordinates), as well as a flag that identifies if the ScheduleSheetInstance is a revision schedule in a titleblock family.

The `GetScheduleHeightsOnSheet` method returns the height of the column headers, row heights, and schedule title.

## Striped rows

These properties provide access to read or set if a given schedule is using a striped row display, and whether that display will be used on a sheet that displays this schedule:

-   ViewSchedule.HasStripedRows
-   ViewSchedule.UseStripedRowsOnSheets

These methods get and set the color applied to the indicated part of the pattern for a schedule with striped rows:

-   ViewSchedule.GetStripedRowsColor()
-   ViewSchedule.SetStripedRowsColor()

`ViewSchedule.IsHeaderFrozen` provides access to read or set if the header is frozen on a given schedule.

## Split Schedules

Schedules can be split, and the resulting segments can be split, merged, and deleted. An overload of `ScheduleSheetInstance.Create` exists to place a schedule segment on a sheet.

## Filtering By Sheet

With the `ScheduleDefinition.IsFilteredBySheet` property, you can define if the `ScheduleSheetInstance` will list only the elements visible in the viewports on that sheet.


<!-- ===== END: Help  ViewSchedule  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Creating a Schedule  Autodesk.md ===== -->

---
created: 2026-01-28T20:52:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_ViewSchedule_Creating_a_Schedule_html
author: 
---

# Help | Creating a Schedule | Autodesk

> ## Excerpt
> The ViewSchedule class has several methods for creating new schedules depending on the type of schedule. All of the methods have a Document parameter that is the document to which the new schedule or schedule-like view will be added. The newly created schedule views will appear under the Schedules/Quantities node in the Project Browser.

---
The ViewSchedule class has several methods for creating new schedules depending on the type of schedule. All of the methods have a Document parameter that is the document to which the new schedule or schedule-like view will be added. The newly created schedule views will appear under the Schedules/Quantities node in the Project Browser.

A standard single-category or multi-category schedule can be created with the static ViewSchedule.CreateSchedule() method.

<table summary="" id="GUID-7DB8EEA6-2C4A-4BC3-A783-1C85B6776D53__TABLE_1058380D6C044FA285D73731EEB5CE50"><tbody><tr><td><b>Code Region: Create a single-category schedule with 2 fields</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateSingleCategorySchedule</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create single-category"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// Create schedule</span><span>
        </span><span>ViewSchedule</span><span> vs </span><span>=</span><span> </span><span>ViewSchedule</span><span>.</span><span>CreateSchedule</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Windows</span><span>));</span><span>

        doc</span><span>.</span><span>Regenerate</span><span>();</span><span>

        </span><span>// Add fields to the schedule</span><span>
        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_HEIGHT</span><span>));</span><span>
        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_WIDTH</span><span>));</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>/// &lt;summary&gt;</span><span>
</span><span>/// Adds a single parameter field to the schedule</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddRegularFieldToSchedule</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>ElementId</span><span> paramId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>

    </span><span>// Find a matching SchedulableField</span><span>
    </span><span>SchedulableField</span><span> schedulableField </span><span>=</span><span>
        definition</span><span>.</span><span>GetSchedulableFields</span><span>().</span><span>FirstOrDefault</span><span>&lt;</span><span>SchedulableField</span><span>&gt;(</span><span>sf </span><span>=&gt;</span><span> sf</span><span>.</span><span>ParameterId</span><span> </span><span>==</span><span> paramId</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>schedulableField </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Add the found field</span><span>
        definition</span><span>.</span><span>AddField</span><span>(</span><span>schedulableField</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The second parameters the ID of the category whose elements will be included in the schedule, or InvalidElementId for a multi-category schedule.

A second CreateSchedule() method can be used to create an area schedule and takes an additional parameter that is the ID of an area scheme for the schedule.

<table summary="" id="GUID-7DB8EEA6-2C4A-4BC3-A783-1C85B6776D53__TABLE_6F5EB09B9E8A43F1BC877E8A73C125DD"><tbody><tr><td><b>Code Region: Creating an area schedule</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateAreaSchedule</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    collector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_AreaSchemes</span><span>);</span><span>
    </span><span>//Get first ElementId of AreaScheme.</span><span>
    </span><span>ElementId</span><span> areaSchemeId </span><span>=</span><span> collector</span><span>.</span><span>FirstElementId</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>areaSchemeId </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> areaSchemeId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// If you want to create an area schedule, you must use CreateSchedule method with three arguments. </span><span>
        </span><span>// The value of the second argument must be ElementId of BuiltInCategory.OST_Areas category</span><span>
        </span><span>// and the value of third argument must be ElementId of an AreaScheme.</span><span>
        </span><span>ViewSchedule</span><span> areaSchedule </span><span>=</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ViewSchedule</span><span>.</span><span>CreateSchedule</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Areas</span><span>),</span><span> areaSchemeId</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

A key schedule displays abstract "key" elements that can be used to populate parameters of ordinary model elements and can be created with the static ViewSchedule.CreateKeySchedule() method whose second parameter is the ID of the category of elements with which the schedule's keys will be associated.A material takeoff is a schedule that displays information about the materials that make up elements in the model. Unlike regular schedules where each row (before grouping) represents a single element, each row in a material takeoff represents a single <element, material> pair. The ViewSchedule.CreateMaterialTakeoff() method has the same parameters as the ViewSchedule.CreateSchedule() method and allows for both single- and multi-category material takeoff schedules.

View lists, sheet lists, and keynote legends are associated with a designated category and therefore their creation methods do take a category ID as a parameter. A view list is a schedule of views in the project. It is a schedule of the Views category and is created using ViewSchedule.CreateViewList().

A sheet list is a schedule of sheets in the project. It is a schedule of the Sheets category and is created using the ViewSchedule.CreateSheetList() method.

A keynote legend is a schedule of the Keynote Tags category and is created using ViewSchedule.CreateKeynoteLegend().

Revision schedules are added to titleblock families and become visible as part of titleblocks on sheets. The ViewSchedule.CreateRevisionSchedule() method will throw an exception if the document passed in is not a titleblock family.

A note block is a schedule of the Generic Annotations category that shows elements of a single family rather than all elements in a category.

The second parameter is the ID of the family whose elements will be included in the schedule.

<table summary="" id="GUID-7DB8EEA6-2C4A-4BC3-A783-1C85B6776D53__TABLE_88434DF564D2433E8B5700903A47A3E2"><tbody><tr><td><b>Code Region: Creating a note block schedule</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateNoteBlock</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Creating Note Block"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>//Get first ElementId of a Note Block family.</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> noteblockFamilies </span><span>=</span><span> </span><span>ViewSchedule</span><span>.</span><span>GetValidFamiliesForNoteBlock</span><span>(</span><span>doc</span><span>);</span><span>
        </span><span>ElementId</span><span> symbolId </span><span>=</span><span> noteblockFamilies</span><span>.</span><span>First</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
        </span><span>ViewSchedule</span><span> noteBlockSchedule </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(!</span><span>symbolId</span><span>.</span><span>Equals</span><span>(</span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>))</span><span>
        </span><span>{</span><span>
            transaction</span><span>.</span><span>Start</span><span>();</span><span>

            </span><span>//Create a note-block view schedule.</span><span>
            noteBlockSchedule </span><span>=</span><span> </span><span>ViewSchedule</span><span>.</span><span>CreateNoteBlock</span><span>(</span><span>doc</span><span>,</span><span> symbolId</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> noteBlockSchedule</span><span>)</span><span>
        </span><span>{</span><span>
            transaction</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            transaction</span><span>.</span><span>RollBack</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Creating a Schedule  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Working with ViewSchedule  Autodesk.md ===== -->

---
created: 2026-01-28T20:52:36 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_ViewSchedule_Working_with_ViewSchedule_html
author: 
---

# Help | Working with ViewSchedule | Autodesk

> ## Excerpt
> The ScheduleDefinition class helps define the ViewSchedule.

---
The ScheduleDefinition class helps define the ViewSchedule.

The ScheduleDefinition class contains various settings related to the contents of a schedule view, including:

-   The schedule's category and other basic properties that determine the type of schedule.
-   A set of fields that become the columns of the schedule.
-   Sorting and grouping criteria.
-   Filters that restrict the set of elements visible in the schedule.
-   Settings to control visibility of the title, headers, and grid lines.

Most schedules contain a single ScheduleDefinition which is retrieved via the ViewSchedule.Definition property. In Revit, schedules of certain categories can contain an "embedded schedule" containing elements associated with the elements in the primary schedule, for example a room schedule showing the elements inside each room or a duct system schedule showing the elements associated with each system. An embedded schedule has its own category, fields, filters, etc. Those settings are stored in a second ScheduleDefinition object. When present, the embedded ScheduleDefinition is obtained from the ScheduleDefinition.EmbeddedDefinition property.

### Adding Fields

Once a ViewSchedule is created, fields can be added. The ScheduleDefinition.GetSchedulableFields() method will return a list of SchedulableField objects representing the non-calculated fields that may be included in the schedule. A new field can be added from a SchedulableField object or using a ScheduleFieldType. The following table describes the options available from the ScheduleFieldType enumeration.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__MEMBERLIST"><tbody><tr><td><b>Member name</b></td><td><b>Description</b></td></tr><tr><td>Instance</td><td>An instance parameter of the scheduled elements. All shared parameters also use this type, regardless of whether they are instance or type parameters.</td></tr><tr><td>ElementType</td><td>A type parameter of the scheduled elements.</td></tr><tr><td>Count</td><td>The number of elements appearing on the schedule row.</td></tr><tr><td>ViewBased</td><td>A specialized type of field used for a few parameters whose displayed values can change based on the settings of the view:<ul><li>ROOM_AREA and ROOM_PERIMETER in room and space schedules.</li><li>PROJECT_REVISION_REVISION_NUM in revision schedules.</li><li>KEYNOTE_NUMBER in keynote legends that are numbered by sheet.</li></ul></td></tr><tr><td>Formula</td><td>A formula calculated from the values of other fields in the schedule.</td></tr><tr><td>Percentage</td><td>A value indicating what percent of the total of another field each element represents.</td></tr><tr><td>Room</td><td>A parameter of the room that a scheduled element belongs to.</td></tr><tr><td>FromRoom</td><td>A parameter of the room on the "from" side of a door or window.</td></tr><tr><td>ToRoom</td><td>A parameter of the room on the "to" side of a door or window.</td></tr><tr><td>ProjectInfo</td><td>A parameter of the Project Info element in the project that the scheduled element belongs to, which may be a linked file. Only allowed in schedules that include elements from linked files.</td></tr><tr><td>Material</td><td>In a material takeoff, a parameter of one of the materials of a scheduled element.</td></tr><tr><td>MaterialQuantity</td><td>In a material takeoff, a value representing how a particular material is used within a scheduled element. The parameter ID can be MATERIAL_AREA, MATERIAL_VOLUME, or MATERIAL_ASPAINT.</td></tr><tr><td>RevitLinkInstance</td><td>A parameter of the RevitLinkInstance that an element in a linked file belongs to. Currently RVT_LINK_INSTANCE_NAME is the only supported parameter. Only allowed in schedules that include elements from linked files.</td></tr><tr><td>RevitLinkType</td><td>A parameter of the RevitLinkType that an element in a linked file belongs to. Currently RVT_LINK_FILE_NAME_WITHOUT_EXT is the only supported parameter. Only allowed in schedules that include elements from linked files.</td></tr><tr><td>StructuralMaterial</td><td>A parameter of the structural material of a scheduled element.</td></tr><tr><td>Space</td><td>A parameter of the space that a scheduled element belongs to.</td></tr></tbody></table>

Using one of the ScheduleDefinition.AddField() methods will add the field to the end of the field list. To place a new field in a specific location in the field list, use one of the ScheduleDefinition.InsertField() methods. Fields can also be ordered after the fact using ScheduleDefinition.SetFieldOrder().

The following is a simple example showing how to add fields to a view if they are not already in the view schedule.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_B01907F3DB6E4BC2BA472F839B047368"><tbody><tr><td><b>Code Region: Adding fields to a schedule</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Add fields to view schedule.</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>/// &lt;param name="schedules"&gt;List of view schedule.&lt;/param&gt;</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>AddFieldToSchedule</span><span>(</span><span>List</span><span>&lt;</span><span>ViewSchedule</span><span>&gt;</span><span> schedules</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>IList</span><span>&lt;</span><span>SchedulableField</span><span>&gt;</span><span> schedulableFields </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ViewSchedule</span><span> vs </span><span>in</span><span> schedules</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>//Get all schedulable fields from view schedule definition.</span><span>
        schedulableFields </span><span>=</span><span> vs</span><span>.</span><span>Definition</span><span>.</span><span>GetSchedulableFields</span><span>();</span><span>

        </span><span>foreach</span><span> </span><span>(</span><span>SchedulableField</span><span> sf </span><span>in</span><span> schedulableFields</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>bool</span><span> fieldAlreadyAdded </span><span>=</span><span> </span><span>false</span><span>;</span><span>
            </span><span>//Get all schedule field ids</span><span>
            </span><span>IList</span><span>&lt;</span><span>ScheduleFieldId</span><span>&gt;</span><span> ids </span><span>=</span><span> vs</span><span>.</span><span>Definition</span><span>.</span><span>GetFieldOrder</span><span>();</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>ScheduleFieldId</span><span> id </span><span>in</span><span> ids</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>//If the GetSchedulableField() method of gotten schedule field returns same schedulable field,</span><span>
                </span><span>// it means the field is already added to the view schedule.</span><span>
                </span><span>if</span><span> </span><span>(</span><span>vs</span><span>.</span><span>Definition</span><span>.</span><span>GetField</span><span>(</span><span>id</span><span>).</span><span>GetSchedulableField</span><span>()</span><span> </span><span>==</span><span> sf</span><span>)</span><span>
                </span><span>{</span><span>
                    fieldAlreadyAdded </span><span>=</span><span> </span><span>true</span><span>;</span><span>
                    </span><span>break</span><span>;</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>

            </span><span>//If schedulable field doesn't exist in view schedule, add it.</span><span>
            </span><span>if</span><span> </span><span>(</span><span>fieldAlreadyAdded </span><span>==</span><span> </span><span>false</span><span>)</span><span>
            </span><span>{</span><span>
                vs</span><span>.</span><span>Definition</span><span>.</span><span>AddField</span><span>(</span><span>sf</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The ScheduleField class represents a single field in a ScheduleDefinition's list of fields. Each (non-hidden) field becomes a column in the schedule.

Most commonly, a field represents an instance or type parameter of elements appearing in the schedule. Some fields represent parameters of other related elements, like the room to which a scheduled element belongs. Fields can also represent data calculated from other fields in the schedule, specifically Formula and Percentage fields.

The ScheduleField class has properties to control column headings, both the text as well as the orientation. Column width and horizontal alignment of text within a column can also be defined.

The ScheduleField.IsHidden property can be used to hide a field. A hidden field is not displayed in the schedule, but it can be used for filtering, sorting, grouping, and conditional formatting and can be referenced by Formula and Percentage fields.

#### DisplayType

The ScheduleField has a DisplayType property which indicates the display type for the field. Possible values are:

-   **Standard** - Nothing is displayed if the values of the elements are different, otherwise, the common value will be displayed
-   **Totals** -Calculates and displays the total value
-   **MinMax** - Calculates and displays the minimum and maximum values
-   **Min** -Calculates and displays the maximum value
-   **Max** - Calculates and displays the minimum value The ScheduleField.CanDisplayMinMax() method indicates whether this field can display minimum and maximum values. In a non-itemized schedule, values for the non-Standard display types are displayed in regular rows when multiple elements appear on the same row.
    
    ### Style and Formatting of Fields
    

ScheduleField.GetStyle() and ScheduleField.SetStyle() use the TableCellStyle class to work with the style of fields in a schedule. Using SetStyle(), various attributes of the field can be set, including the line style for the border of the cell as well as the text font, color and size.

ScheduleField.SetFormatOptions() and ScheduleField.GetFormatOptions() use the FormatOptions class to work with the formatting of a field's data. The FormatOptions class contains settings that control how to format numbers with units as strings. It contains those settings that are typically chosen by an end user in the Format dialog and stored in the document.

In the following example, all length fields in a ViewSchedule are formatted to display in feet and fractional inches.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_2905AC04527B43AD8B0170FD38F078DB"><tbody><tr><td><b>Code Region: Formatting a field</b></td></tr><tr><td><pre><code><span>// format length units to display in feet and inches format</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>FormatLengthFields</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>int</span><span> nFields </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>.</span><span>GetFieldCount</span><span>();</span><span>
    </span><span>for</span><span> </span><span>(</span><span>int</span><span> n </span><span>=</span><span> </span><span>0</span><span>;</span><span> n </span><span>&lt;</span><span> nFields</span><span>;</span><span> n</span><span>++)</span><span>
    </span><span>{</span><span>
        </span><span>ScheduleField</span><span> field </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>.</span><span>GetField</span><span>(</span><span>n</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>field</span><span>.</span><span>GetSpecTypeId</span><span>()</span><span> </span><span>==</span><span> </span><span>SpecTypeId</span><span>.</span><span>Length</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FormatOptions</span><span> formatOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>FormatOptions</span><span>();</span><span>
            formatOpts</span><span>.</span><span>UseDefault</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
            formatOpts</span><span>.</span><span>SetUnitTypeId</span><span>(</span><span>UnitTypeId</span><span>.</span><span>FeetFractionalInches</span><span>);</span><span>
            field</span><span>.</span><span>SetFormatOptions</span><span>(</span><span>formatOpts</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The example below applies both formatting and style overrides to a given field.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_4429DA0DE7734921A6F1CD04F05F30DA"><tbody><tr><td><b>Code Region: Apply formatting and style overrides to field</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>ApplyFormattingToField</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>int</span><span> fieldIndex</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the field.</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>
    </span><span>ScheduleField</span><span> field </span><span>=</span><span> definition</span><span>.</span><span>GetField</span><span>(</span><span>fieldIndex</span><span>);</span><span>

    </span><span>// Build unit formatting for the field.</span><span>
    </span><span>FormatOptions</span><span> options </span><span>=</span><span> field</span><span>.</span><span>GetFormatOptions</span><span>();</span><span>
    options</span><span>.</span><span>UseDefault</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    options</span><span>.</span><span>SetUnitTypeId</span><span>(</span><span>UnitTypeId</span><span>.</span><span>SquareInches</span><span>);</span><span>
    options</span><span>.</span><span>SetSymbolTypeId</span><span>(</span><span>SymbolTypeId</span><span>.</span><span>InCaret2</span><span>);</span><span>

    </span><span>// Build style overrides for the field</span><span>
    </span><span>// Use override options to indicate fields that are overridden and apply changes</span><span>
    </span><span>TableCellStyle</span><span> style </span><span>=</span><span> field</span><span>.</span><span>GetStyle</span><span>();</span><span>
    </span><span>TableCellStyleOverrideOptions</span><span> overrideOptions </span><span>=</span><span> style</span><span>.</span><span>GetCellStyleOverrideOptions</span><span>();</span><span>
    overrideOptions</span><span>.</span><span>BackgroundColor</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    style</span><span>.</span><span>BackgroundColor</span><span> </span><span>=</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>0x00</span><span>,</span><span> </span><span>0x00</span><span>,</span><span> </span><span>0xFF</span><span>);</span><span>
    overrideOptions</span><span>.</span><span>FontColor</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    style</span><span>.</span><span>TextColor</span><span> </span><span>=</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>0xFF</span><span>,</span><span> </span><span>0xFF</span><span>,</span><span> </span><span>0xFF</span><span>);</span><span>
    overrideOptions</span><span>.</span><span>Italics</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    style</span><span>.</span><span>IsFontItalic</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>

    style</span><span>.</span><span>SetCellStyleOverrideOptions</span><span>(</span><span>overrideOptions</span><span>);</span><span>

    </span><span>double</span><span> width </span><span>=</span><span> field</span><span>.</span><span>GridColumnWidth</span><span>;</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>schedule</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Set style etc"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        field</span><span>.</span><span>SetStyle</span><span>(</span><span>style</span><span>);</span><span>
        field</span><span>.</span><span>SetFormatOptions</span><span>(</span><span>options</span><span>);</span><span>
        </span><span>// Change column width (affects width in grid and on sheet) - units are in Revit length units - ft.</span><span>
        field</span><span>.</span><span>GridColumnWidth</span><span> </span><span>=</span><span> width </span><span>+</span><span> </span><span>0.5</span><span>;</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Title and Headers

Display of the schedule title and/or headers is optional. Whether the title or headers are shown can be controlled with the ScheduleDefinition properties ShowTitle and ShowHeaders.

### Grouping and Sorting in Schedules

A schedule may be sorted or grouped by one or more of the schedule's fields. Several methods can be used to control grouping and sorting of fields. The ScheduleSortGroupField class represents one of the fields that the schedule is sorted or grouped by. Sorting and grouping are related operations. In either case, elements appearing in the schedule are sorted based on their values for the field by which the schedule is sorted/grouped, which automatically causes elements with identical values to be grouped together. By enabling extra header, footer, or blank rows, visual separation between groups can be achieved.

If the ScheduleDefinition.IsItemized property is false, elements having the same values for all of the fields used for sorting/grouping will be combined onto the same row. Otherwise the schedule displays each element on a separate row

A schedule can be sorted or grouped by data that is not displayed in the schedule by marking the field used for sorting/grouping as hidden using the ScheduleField.IsHidden property.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_87FC42D71B464D72AD9B7CD81EA453A2"><tbody><tr><td><b>Code Region: Add grouping/sorting to schedule</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddGroupingToSchedule</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>BuiltInParameter</span><span> paramEnum</span><span>,</span><span> </span><span>bool</span><span> withTotalsAndDecoration</span><span>,</span><span> </span><span>ScheduleSortOrder</span><span> order</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find field </span><span>
    </span><span>ScheduleField</span><span> field </span><span>=</span><span> </span><span>FindScheduleField</span><span>(</span><span>schedule</span><span>,</span><span> paramEnum</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>field </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Unable to find field."</span><span>);</span><span>

    </span><span>// Build sort/group field.</span><span>
    </span><span>ScheduleSortGroupField</span><span> sortGroupField </span><span>=</span><span> </span><span>new</span><span> </span><span>ScheduleSortGroupField</span><span>(</span><span>field</span><span>.</span><span>FieldId</span><span>,</span><span> order</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>withTotalsAndDecoration</span><span>)</span><span>
    </span><span>{</span><span>
        sortGroupField</span><span>.</span><span>ShowFooter</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        sortGroupField</span><span>.</span><span>ShowFooterTitle</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        sortGroupField</span><span>.</span><span>ShowFooterCount</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        sortGroupField</span><span>.</span><span>ShowHeader</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        sortGroupField</span><span>.</span><span>ShowBlankLine</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>// Add the sort/group field</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>schedule</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Add sort/group field"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        definition</span><span>.</span><span>AddSortGroupField</span><span>(</span><span>sortGroupField</span><span>);</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>static</span><span> </span><span>ScheduleField</span><span> </span><span>FindScheduleField</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>BuiltInParameter</span><span> paramEnum</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>
    </span><span>ScheduleField</span><span> foundField </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ElementId</span><span> paramId </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>paramEnum</span><span>);</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ScheduleFieldId</span><span> fieldId </span><span>in</span><span> definition</span><span>.</span><span>GetFieldOrder</span><span>())</span><span>
    </span><span>{</span><span>
        foundField </span><span>=</span><span> definition</span><span>.</span><span>GetField</span><span>(</span><span>fieldId</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>foundField</span><span>.</span><span>ParameterId</span><span> </span><span>==</span><span> paramId</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>return</span><span> foundField</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>null</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Headers can also be grouped. ViewSchedule.GroupHeaders() method can be used to specify which rows and columns to include in a grouping of the header section. The last parameter is a string for the caption of the grouped rows and columns.

In the following example, columns are grouped for a newly created single-category schedule.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_C5591CE29409415D9EF7ED5B5AAE6C44"><tbody><tr><td><b>Code Region: Grouping headers</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateSingleCategoryScheduleWithGroupedColumnHeaders</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create single-category with grouped column headers"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>// Build the schedule</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>ViewSchedule</span><span> vs </span><span>=</span><span> </span><span>ViewSchedule</span><span>.</span><span>CreateSchedule</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Windows</span><span>));</span><span>

        </span><span>AddRegularField</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_HEIGHT</span><span>));</span><span>
        </span><span>AddRegularField</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_WIDTH</span><span>));</span><span>
        </span><span>AddRegularField</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>ALL_MODEL_MARK</span><span>));</span><span>
        </span><span>AddRegularField</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>ALL_MODEL_COST</span><span>));</span><span>

        doc</span><span>.</span><span>Regenerate</span><span>();</span><span>

        </span><span>// Group the headers in the body section using ViewSchedule methods</span><span>
        vs</span><span>.</span><span>GroupHeaders</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>"Size"</span><span>);</span><span>
        vs</span><span>.</span><span>GroupHeaders</span><span>(</span><span>0</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>3</span><span>,</span><span> </span><span>"Other"</span><span>);</span><span>
        vs</span><span>.</span><span>GroupHeaders</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>3</span><span>,</span><span> </span><span>"All"</span><span>);</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddRegularField</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>ElementId</span><span> paramId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>

    </span><span>// Find a matching SchedulableField</span><span>
    </span><span>SchedulableField</span><span> schedulableField </span><span>=</span><span>
        definition</span><span>.</span><span>GetSchedulableFields</span><span>().</span><span>FirstOrDefault</span><span>&lt;</span><span>SchedulableField</span><span>&gt;(</span><span>sf </span><span>=&gt;</span><span> sf</span><span>.</span><span>ParameterId</span><span> </span><span>==</span><span> paramId</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>schedulableField </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Add the found field</span><span>
        definition</span><span>.</span><span>AddField</span><span>(</span><span>schedulableField</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Filtering

A ScheduleFilter can be used to filter the elements that will be displayed in a schedule. A filter is a condition that must be satisfied for an element to appear in the schedule. All filters must be satisfied for an element to appear in the schedule.

A schedule can be filtered by data that is not displayed in the schedule by marking the field used for filtering as hidden using the ScheduleField.IsHidden property.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_5A0B9ECD2D2148478BA767ECC8050860"><tbody><tr><td><b>Code Region: Add filter to schedule</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddFilterToSchedule</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>ElementId</span><span> levelId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find level field</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>

    </span><span>ScheduleField</span><span> levelField </span><span>=</span><span> </span><span>FindField</span><span>(</span><span>schedule</span><span>,</span><span> </span><span>BuiltInParameter</span><span>.</span><span>ROOM_LEVEL_ID</span><span>);</span><span>

    </span><span>// Add filter</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>schedule</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Add filter"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// If field not present, add it</span><span>
        </span><span>if</span><span> </span><span>(</span><span>levelField </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            levelField </span><span>=</span><span> definition</span><span>.</span><span>AddField</span><span>(</span><span>ScheduleFieldType</span><span>.</span><span>Instance</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>ROOM_LEVEL_ID</span><span>));</span><span>
        </span><span>}</span><span>

        </span><span>// Set field to hidden</span><span>
        levelField</span><span>.</span><span>IsHidden</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>ScheduleFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ScheduleFilter</span><span>(</span><span>levelField</span><span>.</span><span>FieldId</span><span>,</span><span> </span><span>ScheduleFilterType</span><span>.</span><span>Equal</span><span>,</span><span> levelId</span><span>);</span><span>
        definition</span><span>.</span><span>AddFilter</span><span>(</span><span>filter</span><span>);</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>/// &lt;summary&gt;</span><span>
</span><span>/// Finds an existing ScheduleField matching the given parameter</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>/// &lt;param name="schedule"&gt;&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="paramEnum"&gt;&lt;/param&gt;</span><span>
</span><span>/// &lt;returns&gt;&lt;/returns&gt;</span><span>
</span><span>public</span><span> </span><span>static</span><span> </span><span>ScheduleField</span><span> </span><span>FindField</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>BuiltInParameter</span><span> paramEnum</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>
    </span><span>ScheduleField</span><span> foundField </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ElementId</span><span> paramId </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>paramEnum</span><span>);</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ScheduleFieldId</span><span> fieldId </span><span>in</span><span> definition</span><span>.</span><span>GetFieldOrder</span><span>())</span><span>
    </span><span>{</span><span>
        foundField </span><span>=</span><span> definition</span><span>.</span><span>GetField</span><span>(</span><span>fieldId</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>foundField</span><span>.</span><span>ParameterId</span><span> </span><span>==</span><span> paramId</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>return</span><span> foundField</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>null</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Multiple Value Formatting

The `ScheduleField` class has properties which allow customization of the multiple value indication per field:

-   ScheduleField.MultipleValuesDisplayType
-   ScheduleField.MultipleValuesText - The text to be used when a field has multiple values
-   ScheduleField.MultipleValuesCustomText - The text to be used when a field has multiple values and the display type is set to ScheduleFieldMultip leValuesDisplayType.Custom

The Enum `ScheduleFieldMultipleValuesDisplayType` defines how the schedule field's multiple value indication is displayed (using the project setting, a custom text, or a predefined text "<varies>").

### Working with Schedule Data

The following example shows how to determine the list of elements in a schedule.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_815A7CD21F094301BC3655148D8880F8"><tbody><tr><td><b>Code Region: Get a schedule's contents</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>GetScheduleContents</span><span>(</span><span>ViewSchedule</span><span> viewSchedule</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Collect types displayed in the schedule</span><span>
    </span><span>FilteredElementCollector</span><span> typeCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>viewSchedule</span><span>.</span><span>Document</span><span>,</span><span> viewSchedule</span><span>.</span><span>Id</span><span>);</span><span>
    typeCollector</span><span>.</span><span>WhereElementIsElementType</span><span>();</span><span>

    </span><span>int</span><span> numberOfTypes </span><span>=</span><span> typeCollector</span><span>.</span><span>Count</span><span>();</span><span>

    </span><span>// Collect instances displayed in the schedule</span><span>
    </span><span>FilteredElementCollector</span><span> instCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>viewSchedule</span><span>.</span><span>Document</span><span>,</span><span> viewSchedule</span><span>.</span><span>Id</span><span>);</span><span>
    instCollector</span><span>.</span><span>WhereElementIsNotElementType</span><span>();</span><span>

    </span><span>int</span><span> numberOfInstances </span><span>=</span><span> instCollector</span><span>.</span><span>Count</span><span>();</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Elements in schedule"</span><span>,</span><span> </span><span>String</span><span>.</span><span>Format</span><span>(</span><span>"Types {0} instances {1}"</span><span>,</span><span> numberOfTypes</span><span>,</span><span> numberOfInstances</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

To work with the actual data in the schedule, the ViewSchedule.GetTableData() returns a TableData object that holds most of the data that describe the style and contents of the rows, columns, and cells in a table. More information can be found under [TableView](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_html).


<!-- ===== END: Help  Working with ViewSchedule  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  PanelScheduleView  Autodesk.md ===== -->

---
created: 2026-01-28T20:52:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_PanelScheduleView_html
author: 
---

# Help | PanelScheduleView | Autodesk

> ## Excerpt
> PanelScheduleView represents a panel schedule which displays information about a panel, the circuits connected to the panel, and their corresponding loads.

---
PanelScheduleView represents a panel schedule which displays information about a panel, the circuits connected to the panel, and their corresponding loads.

You can create a schedule that lists the circuits connected to a panel, and displays information about each circuit such as location on the panel, circuit name and apparent loads. Panel schedules display four main information sections: a header, circuit table, a loads summary and a footer. A new Panel Schedule view for the selected panel is displayed in the drawing area, and panel schedules are added to the project browser under the Panel Schedules folder. A panel schedule shows the following data:

-   Panel Name
-   Distribution System supported by the panel
-   Number of phases available from the panel
-   Number of wires specified for the distribution system assigned to this panel
-   Rating of the mains feeding the panel
-   Type of mounting (Surface or Recessed)
-   Type of case enclosing the panel
-   Room where the panel is installed
-   Name assigned to a load circuit
-   Rated trip current for a circuit breaker
-   Number of poles on the circuit breaker
-   Circuit number
-   Phases
-   Apparent load (VA) for each of the phases
-   Total apparent load for all three phases
-   Manufacturer
-   Notation of any changes made to the panel
-   Root Means Square amperage Additional circuit and panel information to display can be specified in the panel schedule templates, represented in the Revit API by the PanelScheduleTemplate class.

PanelScheduleView is derived from the TableView class as is ViewSchedule. Some of the common functionality between schedules and panel schedules can be found in the [Schedule Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_Schedule_Classes_html "Schedule views use several supporting classes.") topic.

### Panel schedule creation

There are two static overloads for creating a PanelScheduleView. One overload of PanelScheduleView.CreateInstanceView() only requires the document in which to create the panel schedule and the id of the electrical panel element associated with the schedule. This method uses the default panel schedule template to create the new view. The other overload takes the id of a specific PanelScheduleTemplate to use.

The following example creates a new panel schedule from a user-selected electrical panel using the default template and switches the active view to the new panel schedule view.

<table summary="" id="GUID-060A778F-29B5-4F03-974F-3DABEF2CF131__TABLE_5421C731BF84459E860D8DA820244CCA"><tbody><tr><td><b>Code Region: Create a panel schedule</b></td></tr><tr><td><pre><code><span>// Create a new panel schedule and switch to that view</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>CreatePanelSchedule</span><span>(</span><span>UIDocument</span><span> uiDocument</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>Reference</span><span> selected </span><span>=</span><span> uiDocument</span><span>.</span><span>Selection</span><span>.</span><span>PickObject</span><span>(</span><span>ObjectType</span><span>.</span><span>Element</span><span>,</span><span> </span><span>"Select an electrical panel"</span><span>);</span><span>

    </span><span>Element</span><span> panel </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>selected</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> panel</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>PanelScheduleView</span><span> psv </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create a new panel schedule"</span><span>))</span><span>
        </span><span>{</span><span>
            trans</span><span>.</span><span>Start</span><span>();</span><span>
            psv </span><span>=</span><span> </span><span>PanelScheduleView</span><span>.</span><span>CreateInstanceView</span><span>(</span><span>doc</span><span>,</span><span> panel</span><span>.</span><span>Id</span><span>);</span><span>
            trans</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> psv</span><span>)</span><span>
        </span><span>{</span><span>
            uiDocument</span><span>.</span><span>ActiveView</span><span> </span><span>=</span><span> psv</span><span>;</span><span>    </span><span>// make new view the active view</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Please select one electrical panel."</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Working with panel schedules

After a schedule is created, you may want to modify it. Several methods are helpful for moving data in the schedule. To move data around, use PanelScheduleView.GetCellsBySlotNumber() to get the range of cells for a specified slot number. PanelScheduleView.MoveSlotTo() moves the circuits in the source slot to the specific slot. Prior to moving the circuits, call PanelScheduleView.CanMoveSlotTo() to ensure the move is allowable.

If the moving circuit is in a group, all circuits in the group will be moved accordingly. The IsSlotGrouped() method will check if the slot is in a group. This method returns 0 if the slot is not in a group. If it is in a group, the returned value with be the group number (a value greater than 0).


<!-- ===== END: Help  PanelScheduleView  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Revisions  Autodesk.md ===== -->

---
created: 2026-01-28T20:52:47 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_Revisions_html
author: 
---

# Help | Revisions | Autodesk

> ## Excerpt
> The Revit API provides several classes and members for accessing project Revisions, their settings and associated Revision Clouds.

---
The Revit API provides several classes and members for accessing project Revisions, their settings and associated Revision Clouds.

## Settings

The RevisionSettings class allows an application to read and modify the project-wide settings that affect Revisions and Revision Clouds. The static RevisionSettings.GetRevisionSettings() method returns the RevisionSettings object for the given project document. The following properties can be used to access project-wide Revision settings:

-   RevisionCloudSpacing - determines the size in paper space of revision clouds drawn in a project.
-   RevisionNumbering - determines whether revision numbers for the project are determined on a per sheet or a whole project basis. The AlphanumericRevisionSettings class contains settings that apply to Revisions with the Alphanumeric RevisionNumberType. The RevisionSettings methods GetAlphanumericRevisionSettings() and SetAlphanumericRevisionSettings() provide read and write access to the AlphanumericRevisionSettings. AlphanumericRevisionSettings offers the following members:

-   Prefix - a prefix to be prepended to each revision number with alphanumeric type.
-   Suffix - a suffix to be appended to each revision number with alphanumeric type.
-   GetSequence() - gets the list of strings to be used as the numbering sequence for revisions with the alphanumeric type.
-   SetSequence() - sets the list of strings for numbering revisions of this type. Similarly, the NumericRevisionSettings class contains settings that apply to Revisions with the Numeric RevisionNumberType. The RevisionSettings methods GetNumericRevisionSettings () and SetNumericRevisionSettings() provide read and write access to these settings. NumericRevisionSettings offers the following members:

-   Prefix - a prefix to be prepended to each revision number with numeric type.
    
-   Suffix - a suffix to be appended to each revision number with numeric type.
    
-   StartNumber property - the value to be used as the first number in the sequence of numeric revisions.
    
    When revision clouds appear on a sheet, the revision number of each revision can be displayed either by tagging the revision cloud or by a revision schedule within the sheet's titleblock. There are two ways the number can be determined:
    
-   **Per project**: The value of the Revision numbers will always correspond to the project-wide Revision Sequence Number assigned to the revision. For example, if revision clouds for revisions with sequence numbers 5, 7, and 8 are placed on a sheet then revision tags and schedules on that sheet would display 5, 7, and 8.
    
-   **Per sheet**: Revision numbers will be assigned consecutive numbers based on the revision clouds visible on that sheet. For example, if revision clouds for revisions assigned project-wide Revision Sequence Numbers 5, 7, and 8 are placed on a sheet then revision tags and schedules on that sheet would display 1, 2, and 3. The sequence on the sheet will still follow the relative ordering of the Revision Sequence Numbers, so in this example revision 5 would be displayed as 1 on the sheet, revision 7 would be displayed as 2, etc.
    

The Revision class allows an application to read and modify the existing revisions in a project and to create new revisions. The Revision object represents the data related to a single revision in the project. It has properties such IssuedBy, IssuedTo, RevisionNumber, SequenceNumber and RevisionDate. Revision clouds and tags can be associated with a particular Revision object to display its properties on sheets.

The revisions in the project are stored in a specific order called the revision sequence. The revision sequence represents the conceptual sequence in which revisions will be issued. The static method Revision.GetAllRevisionIds() will return the ids of all Revisions in this order. The static method Revision.ReorderRevisionSequence() can be used to change the sequence of revisions with the project. Note that the newly specified sequence must include every Revision in the project exactly once and that changing the sequence of Revisions can change the SequenceNumber and RevisionNumber of Revisions that have already been issued.

The `RevisionNumberingSequence` class defines the sequences by which numbers are assigned to Revisions. Revision numbering is either numeric or alphanumeric. Alphanumeric from the API corresponds to the UI concept of "Custom". Members of this class provide the ability to create, read and modify the settings related to Revision numbering sequences.

`Revision.GetRevisionNumberingSequenceId()` and Revision.SetRevisionNumberingSequenceId()\` provide access to the sequence which controls a revision's numbering.

The static Create() method will create a new Revision in the specified document. In the sample below, multiple revisions are added and their properties are set.

| Code Region: Creating new revisions |
| --- |
| 
```
public IList<Revision> AddRevisions(Document document)
{
    IList<Revision> newRevisions = new List<Revision>();
    using (Transaction createRevision = new Transaction(document, "createRevision"))
    {
        createRevision.Start();
        newRevisions.Add(AddNewRevision(document, "Include door tags", "manager1", "employee1", 1, DateTime.Now));
        newRevisions.Add(AddNewRevision(document, "Add a section view", "manager1", "employee1", 2, DateTime.Now));
        newRevisions.Add(AddNewRevision(document, "Make callout view larger", "manager1", "employee1", 3, DateTime.Now));
        createRevision.Commit();
    }

    return newRevisions;
}

private Revision AddNewRevision(Document document, string description, string issuedBy, string issuedTo, int sequenceNumber, DateTime date)
{
    Revision newRevision = Revision.Create(document);
    newRevision.Description = description;
    newRevision.IssuedBy = issuedBy;
    newRevision.IssuedTo = issuedTo;

    AlphanumericRevisionSettings ars = new AlphanumericRevisionSettings();
    RevisionNumberingSequence sequence = RevisionNumberingSequence.CreateAlphanumericSequence(document, "name", ars);
    newRevision.RevisionNumberingSequenceId = sequence.Id;

    newRevision.RevisionDate = date.ToShortDateString();
    return newRevision;
}
```

 |

Two methods, CombineWithNext() and CombineWithPrevious() allow an application to combine a specified Revision with the next or previous Revision in the model. Combining the Revisions means that the RevisionClouds and revision tags associated with the specified Revision will be reassociated with the next Revision and the specified Revision will be deleted from the model. This method returns the ids of the RevisionClouds that were reassociated. However, these operations can only be implemented if neither Revision has been issued.

The following example demonstrates use of the CombineWithNext() method. It also uses the GetAllRevisionIds() method to find the next revision to be sure the CombineWithNext() method will be successful.

| Code Region: Combining revisions |
| --- |
| 
```
private bool CombineRevision(Document document, Revision revision)
{
    bool combined = false;
    // Can only combine two revisions if neither have been issued
    if (revision.Issued == false)
    {
        ElementId revisionId = revision.Id;
        Revision nextRevsion = GetNextRevision(document, revisionId);
        if (nextRevsion != null && nextRevsion.Issued == false)
        {
            ISet<ElementId> revisionCloudIds = Revision.CombineWithNext(document, revisionId);
            combined = true;
            int movedClouds = revisionCloudIds.Count;
            if (movedClouds > 0)
            {
                RevisionCloud cloud = document.GetElement(revisionCloudIds.ElementAt(0)) as RevisionCloud;
                if (cloud != null)
                {
                    string msg = string.Format("Revision {0} deleted and {1} revision clouds were added to Revsion {2}",
                        revisionId.ToString(), movedClouds, cloud.RevisionId.ToString());
                    TaskDialog.Show("Revision Combined", msg);
                }
            }
        }
    }

    return combined;
}

private Revision GetNextRevision(Document document, ElementId currentRevisionId)
{
    Revision nextRevision = null;
    IList<ElementId> revisionIds = Revision.GetAllRevisionIds(document);
    int currentRevisionIndex = -1;
    for (int n = 0; n < revisionIds.Count; n++)
    {
        if (revisionIds[n] == currentRevisionId)
        {
            currentRevisionIndex = n;
            break;
        }
    }

    // if the current revision id was found and is not the last index
    if (currentRevisionIndex >= 0 && currentRevisionIndex < revisionIds.Count - 1)
    {
        ElementId nextRevisionId = revisionIds[currentRevisionIndex + 1];
        nextRevision = document.GetElement(nextRevisionId) as Revision;
    }

    return nextRevision;
}
```

 |

## Revision clouds

A RevisionCloud is a graphical "cloud" that can be displayed on a view or sheet to indicate where revisions in the model have occurred. The RevisionCloud class allows an application to access information about the revision clouds that are present within a model and to create new revision clouds.

RevisionClouds are view specific and can be created in most graphical views, except 3D.

Note also that when a RevisionCloud is created in a ViewLegend, it is treated as a legend representation of what a RevisionCloud looks like rather than as an actual indication of a change to the model. As a result, RevisionClouds in ViewLegends will not affect the contents of revision schedules.

### Creating revision clouds

The static Create() methodallows an application to create a new RevisionCloud in a specified view based on a series of lines and curves. RevisionClouds can only be created if the associated Revision has not yet been issued.

RevisionClouds can be created in most graphical Views, excepting 3D views and graphical column schedules. Unlike most other Elements, RevisionClouds can be created directly on a ViewSheet.

RevisionClouds are created based on a series of sketched curves. There is no requirement that the curves form closed loops and self-intersections are also permitted. The curves will be automatically projected onto the appropriate plane for the View. The list of curves cannot be empty and no lines can be perpendicular to the View's plane. If the View is a model View, the coordinates specified for the curves will be interpreted in model space. If the View is a non-model View (such as a ViewSheet) then the coordinates will be interpreted in the View's space.

Each curve will have a series of "cloud bumps" drawn along it to form the appearance of a cloud. The cloud graphics will be attached to the curves under the assumption that each curve is oriented in a clockwise direction. For lines, this means that the outside of the cloud is in the direction of the line's normal vector within the View's plane. Any closed loops should therefore be oriented clockwise to create the typical cloud shape.

| Code Region: Create revision cloud |
| --- |
| 
```
private void CreateRevisionCloudInActiveView(Document document, Revision revision, IList<Curve> curves)
{
    using (Transaction newRevisionCloud = new Transaction(document, "Create Revision Cloud"))
    {
        newRevisionCloud.Start();
        // Can only create revision cloud for revision that is not issued
        if (revision.Issued == false)
        {
            RevisionCloud.Create(document, document.ActiveView, revision.Id, curves);
            newRevisionCloud.Commit();
        }
        else
        {
            newRevisionCloud.RollBack();
        }
    }
}
```

 |

### Revision cloud geometry

RevisionCloud is derived from the Element class. The Element.Geometry property for revision clouds will return the actual curved lines that make up the cloud. The RevisionCloud.GetSketchCurves() method on the other hand,will return the sketched curves that define the basic outline of the cloud and not the arcs that Revit attaches to these curves to create the cloud appearance.

### Revision Associated with RevisionCloud

Each RevisionCloud is associated with one Revision. The associated revision id is specified when calling Create() and can be retrieved from the RevisionCloud.RevisionId property. The RevisionId property for a RevisionCloud can be changed if it is not associated with a Revision that has already been issued. It can only be changed to the id of another Revision that has also not been issued. RevisionCloud.IsRevisionIssued() returns whether the associated Revision has been issued.

### ViewSheets

When a RevisionCloud is visible on a ViewSheet (either because it is directly placed on that ViewSheet or because it is visible in a View placed on the ViewSheet), any revision schedules displayed on the ViewSheet will automatically include the Revision associated with the RevisionCloud.

The RevisionCloud.GetSheetIds() method returns the ids of the ViewSheets where it may appear and contribute to the sheet's revision schedule. A RevisionCloud can appear on a ViewSheet because it is drawn directly on the ViewSheet or because its owner view is placed on the ViewSheet. If the RevisionCloud is owned by a view that is a dependent view or has associated dependent views, then the RevisionCloud can also be visible on the sheets where the related dependent or primary views have been placed.

This RevisionCloud may not be visible in all ViewSheets reported by this method. Additional factors, such as the visibility settings or annotation crop of the Views or the visibility settings of the associated Revision may still cause this RevisionCloud to not appear on a particular ViewSheet.

If this RevisionCloud is owned by a ViewLegend, no sheets will be returned because the RevisionCloud will not participate in revision schedules. The ViewSheet class includes methods for working with Revisions and RevisionClouds on sheets. See the [ViewSheet](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_ViewSheet_html) topic for more information.


<!-- ===== END: Help  Revisions  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  View Filters  Autodesk.md ===== -->

---
created: 2026-01-28T20:52:53 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Filters_html
author: 
---

# Help | View Filters | Autodesk

> ## Excerpt
> Filters are elements independent of views. They can be applied to Views using the ParameterFilterElement class or a SelectionFilterElement class.

---
Filters are elements independent of views. They can be applied to Views using the ParameterFilterElement class or a SelectionFilterElement class.

### ParameterFilterElement

A ParameterFilterElement filters elements based on the elements’ categories and an ElementFilter. The ElementFilter must be either an ElementParameterFilter or an ElementLogicalFilter containing only ElementParameterFilters and other ElementLogicalFilters. This allows the view filter to be constructed from a combination of AND and OR filters that are then gathered by an AND filter, an OR filter, or an ElementParameterFilter as an input to ParameterFilterElement.Create().

Once a filter has been defined (with one or more categories and zero or more filter rules), it can be applied to a View using one of several methods. The View.AddFilter() method will apply the filter to the view, but with default overrides, meaning the view's display will not change. View.SetFilterOverrides() sets graphical overrides associated with a filter. Setting elements that pass a filter to not be visibile in a view is done with View.SetFilterVisibility(ElementId filterElementId, bool visibility). AddFilter() and SetFilterVisibility() will both apply the filter to the view if it is not already applied, making it unnecessary to call AddFilter() separately.

#### Validation

Validation restrictions for the ElementFilter stored by a ParameterFilterElement (the class that represents a View Filter) support flexible creation of OR filters where criteria can reference parameters only associated to specific categories. The ElementFilter must be either an ElementParameterFilter or an ElementLogicalFilter representing a Boolean combination of ElementParameterFilters.

In addition, Revit checks that each ElementParameterFilter satisfies the following conditions:

-   Its array of FilterRules is not empty and contains:
    -   Any number of FilterRules of type FilterValueRule, FilterInverseRule, and SharedParameterApplicableRule or
    -   Exactly one FilterCategoryRule containing only one category from categories stored by this ParameterFilterElement or
    -   Exactly two rules: the first one is a FilterCategoryRule containing only one category from categories stored by this ParameterFilterElement and the second one is a FilterRule of type FilterValueRule, FilterInverseRule, or SharedParameterApplicableRule.

Cases in the second and third bullet are currently allowed only if the parent node of ElementParameterFilter is LogicalOrFilter.

The method `ParameterFilterElement.GetElementFilterParametersForCategory()` retrieves a list of the parameters associated with all rules in the filter that are combined (using logical AND) with a FilterCategoryRule corresponding to single categoryId.

These methods identify or set if the filter is enabled in this view:

-   View.GetIsFilterEnabled()
-   View.SetIsFilterEnabled()

`View.GetOrderedFilters()` gets the filters applied to the view in the order they are applied.

The following example creates a new view filter matching multiple criteria and then hides those elements in the view.

<table summary="" id="GUID-B6FB80F2-7A17-4242-9E95-D6056090E85B__TABLE_D20AF6F893E34769897200046D711DE2"><tbody><tr><td><b>Code Region: Applying a parameter filter to a view</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateViewFilter</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> categories </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
    categories</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Walls</span><span>));</span><span>
    </span><span>List</span><span>&lt;</span><span>ElementFilter</span><span>&gt;</span><span> elementFilterList </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementFilter</span><span>&gt;();</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Add view filter"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// Criterion 1 - wall type Function is "Exterior"</span><span>
        </span><span>ElementId</span><span> exteriorParamId </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>FUNCTION_PARAM</span><span>);</span><span>
        elementFilterList</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>ParameterFilterRuleFactory</span><span>.</span><span>CreateEqualsRule</span><span>(</span><span>exteriorParamId</span><span>,</span><span> </span><span>(</span><span>int</span><span>)</span><span>WallFunction</span><span>.</span><span>Exterior</span><span>)));</span><span>

        </span><span>// Criterion 2 - wall length &gt; = 28 or &lt; = 14</span><span>
        </span><span>ElementId</span><span> lengthId </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>CURVE_ELEM_LENGTH</span><span>);</span><span>
        </span><span>LogicalOrFilter</span><span> wallHeightFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>LogicalOrFilter</span><span>(</span><span>
            </span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>ParameterFilterRuleFactory</span><span>.</span><span>CreateGreaterOrEqualRule</span><span>(</span><span>lengthId</span><span>,</span><span> </span><span>28.0</span><span>,</span><span> </span><span>0.00001</span><span>)),</span><span>
            </span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>ParameterFilterRuleFactory</span><span>.</span><span>CreateLessOrEqualRule</span><span>(</span><span>lengthId</span><span>,</span><span> </span><span>14.0</span><span>,</span><span> </span><span>0.00001</span><span>)));</span><span>
        elementFilterList</span><span>.</span><span>Add</span><span>(</span><span>wallHeightFilter</span><span>);</span><span>

        </span><span>// Criterion 3 - custom shared parameter value matches string pattern</span><span>
        </span><span>// Get the id for the shared parameter - the ElementId is not hardcoded, so we need to get an instance of this type to find it</span><span>
        </span><span>Guid</span><span> spGuid </span><span>=</span><span> </span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"96b00b61-7f5a-4f36-a828-5cd07890a02a"</span><span>);</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Wall</span><span>));</span><span>
        </span><span>Wall</span><span> wall </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>Wall</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>wall </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Parameter</span><span> sharedParam </span><span>=</span><span> wall</span><span>.</span><span>get_Parameter</span><span>(</span><span>spGuid</span><span>);</span><span>
            </span><span>ElementId</span><span> sharedParamId </span><span>=</span><span> sharedParam</span><span>.</span><span>Id</span><span>;</span><span>

            elementFilterList</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>ParameterFilterRuleFactory</span><span>.</span><span>CreateBeginsWithRule</span><span>(</span><span>sharedParamId</span><span>,</span><span> </span><span>"15."</span><span>,</span><span> </span><span>true</span><span>)));</span><span>
        </span><span>}</span><span>

        </span><span>// Create filter element associated to the input categories</span><span>
        </span><span>LogicalAndFilter</span><span> andFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>LogicalAndFilter</span><span>(</span><span>elementFilterList</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>ParameterFilterElement</span><span>.</span><span>ElementFilterIsAcceptableForParameterFilterElement</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>HashSet</span><span>&lt;</span><span>ElementId</span><span>&gt;(</span><span>categories</span><span>),</span><span> andFilter</span><span>))</span><span>
        </span><span>{</span><span>
            </span><span>ParameterFilterElement</span><span> parameterFilterElement </span><span>=</span><span> </span><span>ParameterFilterElement</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Example view filter"</span><span>,</span><span> categories</span><span>,</span><span> andFilter</span><span>);</span><span>

            </span><span>// Apply filter to view</span><span>
            view</span><span>.</span><span>AddFilter</span><span>(</span><span>parameterFilterElement</span><span>.</span><span>Id</span><span>);</span><span>
            view</span><span>.</span><span>SetFilterVisibility</span><span>(</span><span>parameterFilterElement</span><span>.</span><span>Id</span><span>,</span><span> </span><span>false</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Filter cannot be used"</span><span>);</span><span>
        </span><span>}</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### SelectionFilterElement

A SelectionFilterElement is a special view filter not based on rules, but on a group of possibly unrelated elements. Specific elements can be added to the filter as required and the resulting selection can be overridden just like ParameterFilterElement.

The following example creates a new selection filter and applies an override to it.

<table summary="" id="GUID-B6FB80F2-7A17-4242-9E95-D6056090E85B__TABLE_16DDCED9E9654683A8E7B7A81657AF7F"><tbody><tr><td><b>Code Region: Applying a selection filter to a view</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateSelectionFilter</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// find room tags in this view</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>,</span><span> view</span><span>.</span><span>Id</span><span>);</span><span>
    collector</span><span>.</span><span>WherePasses</span><span>(</span><span>new</span><span> </span><span>RoomTagFilter</span><span>());</span><span>

    </span><span>// collect tags whose room number matches criteria</span><span>
    </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> tagIds </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>RoomTag</span><span> tag </span><span>in</span><span> collector</span><span>.</span><span>Cast</span><span>&lt;</span><span>RoomTag</span><span>&gt;())</span><span>
    </span><span>{</span><span>
        </span><span>int</span><span> number </span><span>=</span><span> </span><span>Int32</span><span>.</span><span>Parse</span><span>(</span><span>tag</span><span>.</span><span>Room</span><span>.</span><span>Number</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>number </span><span>%</span><span> </span><span>3</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
            tagIds</span><span>.</span><span>Add</span><span>(</span><span>tag</span><span>.</span><span>Id</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create SelectionFilterElement"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// Create selection filter and assign ids</span><span>
        </span><span>SelectionFilterElement</span><span> filterElement </span><span>=</span><span> </span><span>SelectionFilterElement</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Room tags filter"</span><span>);</span><span>
        filterElement</span><span>.</span><span>SetElementIds</span><span>(</span><span>tagIds</span><span>);</span><span>

        </span><span>ElementId</span><span> filterId </span><span>=</span><span> filterElement</span><span>.</span><span>Id</span><span>;</span><span>

        </span><span>// Add the filter to the view</span><span>
        view</span><span>.</span><span>AddFilter</span><span>(</span><span>filterId</span><span>);</span><span>

        doc</span><span>.</span><span>Regenerate</span><span>();</span><span>

        </span><span>// Use the existing graphics settings, and change the color to Blue</span><span>
        </span><span>OverrideGraphicSettings</span><span> overrideSettings </span><span>=</span><span> view</span><span>.</span><span>GetFilterOverrides</span><span>(</span><span>filterId</span><span>);</span><span>

        overrideSettings</span><span>.</span><span>SetProjectionLineColor</span><span>(</span><span>new</span><span> </span><span>Color</span><span>(</span><span>0x00</span><span>,</span><span> </span><span>0x00</span><span>,</span><span> </span><span>0xFF</span><span>));</span><span>

        view</span><span>.</span><span>SetFilterOverrides</span><span>(</span><span>filterId</span><span>,</span><span> overrideSettings</span><span>);</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Modifying filters

All filters applied to a view can be retrieved using the View.GetFilters() method which will return a list of filter ids. Filter visibility and graphic overrides can be checked for a specific filter using the View.GetFilterVisibility() and View.GetFilterOverrides() methods respectively. View.RemoveFilter will remove a filter from the view.

The following example demonstrates how to get the filters in a view and then modifies the overrides associated with any filter currently setting the cut color to red.

<table summary="" id="GUID-B6FB80F2-7A17-4242-9E95-D6056090E85B__TABLE_B19DC40567284A65938B03E299351172"><tbody><tr><td><b>Code Region: Modify existing filter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>ModifyExistingFilter</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find any filter with overrides setting cut color to Red</span><span>
    </span><span>Dictionary</span><span>&lt;</span><span>ElementId</span><span>,</span><span> </span><span>OverrideGraphicSettings</span><span>&gt;</span><span> filterIdsToChange </span><span>=</span><span> </span><span>new</span><span> </span><span>Dictionary</span><span>&lt;</span><span>ElementId</span><span>,</span><span> </span><span>OverrideGraphicSettings</span><span>&gt;();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> filterId </span><span>in</span><span> view</span><span>.</span><span>GetFilters</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>OverrideGraphicSettings</span><span> overrideSettings </span><span>=</span><span> view</span><span>.</span><span>GetFilterOverrides</span><span>(</span><span>filterId</span><span>);</span><span>

        </span><span>Color</span><span> lineColor </span><span>=</span><span> overrideSettings</span><span>.</span><span>CutLineColor</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>lineColor </span><span>==</span><span> </span><span>Color</span><span>.</span><span>InvalidColorValue</span><span>)</span><span>
            </span><span>continue</span><span>;</span><span>

        </span><span>// Save overrides setting the cut color to green</span><span>
        </span><span>if</span><span> </span><span>(</span><span>lineColor</span><span>.</span><span>Red</span><span> </span><span>==</span><span> </span><span>0xFF</span><span> </span><span>&amp;&amp;</span><span> lineColor</span><span>.</span><span>Green</span><span> </span><span>==</span><span> </span><span>0x00</span><span> </span><span>&amp;&amp;</span><span> lineColor</span><span>.</span><span>Blue</span><span> </span><span>==</span><span> </span><span>0x00</span><span>)</span><span>
        </span><span>{</span><span>
            overrideSettings</span><span>.</span><span>SetCutLineColor</span><span>(</span><span>new</span><span> </span><span>Color</span><span>(</span><span>0x00</span><span>,</span><span> </span><span>0xFF</span><span>,</span><span> </span><span>0x00</span><span>));</span><span>
            filterIdsToChange</span><span>[</span><span>filterId</span><span>]</span><span> </span><span>=</span><span> overrideSettings</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// Make the change to all found filters</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Change override filters"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> filterId </span><span>in</span><span> filterIdsToChange</span><span>.</span><span>Keys</span><span>)</span><span>
        </span><span>{</span><span>
            view</span><span>.</span><span>SetFilterOverrides</span><span>(</span><span>filterId</span><span>,</span><span> filterIdsToChange</span><span>[</span><span>filterId</span><span>]);</span><span>
        </span><span>}</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  View Filters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  View Cropping  Autodesk.md ===== -->

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


<!-- ===== END: Help  View Cropping  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Displaced Views  Autodesk.md ===== -->

---
created: 2026-01-28T20:53:06 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_Displaced_Views_html
author: 
---

# Help | Displaced Views | Autodesk

> ## Excerpt
> Create a displaced view using the DisplacementElement class. DisplacementElement is a view-specific element that can be used to cause elements to appear displaced from their actual location. Displaced views are useful to illustrate the relationship model elements have to the model as a whole. The DisplacementElement does not actually change the location of any model elements; it merely causes them to be displayed in a different location.

---
Create a displaced view using the DisplacementElement class. DisplacementElement is a view-specific element that can be used to cause elements to appear displaced from their actual location. Displaced views are useful to illustrate the relationship model elements have to the model as a whole. The DisplacementElement does not actually change the location of any model elements; it merely causes them to be displayed in a different location.

For a detailed example of creating displaced views, see the DisplacementElementAnimation sample in the Revit SDK.

### Creating a Displaced View

The static DisplacementElement.Create() method c reates a new DisplacementElement. The new DisplacementElement may be a child of a parent DisplacementElement if the parentDisplacementElement parameter is not null. If a parent is specified, the child DisplacementElement's transform will be concatenated with that of the parent, and the displacement of its associated elements will be relative to the parent DisplacementElement.

The Create() method also requires a document, a list of elements to be displaced, the owner view, and t he translation to be applied to the graphics of the displaced elements. An element may only be displaced by a single DisplacementElement in any view. Assigning an element to more than one DisplacementElement will result in an exception.

Other static methods of DisplacementElement can be used prior to calling Create() to help prevent any exceptions. CanCategoryBeDisplaced() tests whether elements belonging to a specific category can be displaced, while the overloaded static method CanElementsBeDisplaced() indicates if specific elements may be assigned to a new DisplacementElement. IsAllowedAsDisplacedElement() tests a single element for eligibility to be displaced.

The static GetAdditionalElementsToDisplace() method will return any additional elements that should be displaced along with the specified element in a specified view. For example, when a wall is displaced, any inserts or hosted elements should also be displaced.

When creating a child DisplacementElement, the static IsValidAsParentInView() can be used to verify a specific DisplacementElement may be used as a parent in a specific View.

Other static methods of DisplacementElement can be used to find the DisplacementElement that includes a specific element, to get a list of all displaced elements in a View, or to get all the DisplacementElements owned by a specified View.

### Working with Displaced Elements

Once a new DisplacementElement has been created, methods are available to obtain any child DisplacementElements, to get the ids of all elements affected by the DisplacementElement, or to obtain the ids of all elements affected by the DisplacementElement as well as any child DisplacementElements. The ParentId property will return the element id of the parent DisplacementElement, if there is one.

After creation, the set of elements affected by the DisplacementElement can be modified using SetDisplacedElementIds() or RemoveDisplacedElement(). Additionally, the relative displacement can be changed.

The method ResetDisplacedElements() will set the translation of the DisplacementElement to (0, 0, 0). The DisplacementElement continues to exist, but its elements are displayed in their actual location.

### Creating a Displaced Path

DisplacementPath is a view-specific annotation related to a DisplacementElement. The DisplacementPath class creates an annotation that depicts the movement of the element from its actual location to its displaced location. The DisplacementPath is anchored to the DisplacementElement by a reference to a point on an edge of a displaced element of the DisplacementElement. It is represented by a single line, or a series of jogged lines, originating at the specified point on the displaced element.

The static DisplacementPath.Create() method requires a document, id of the associated DisplacementElement, a reference that refers to an edge or curve of one of the elements displaced by the DisplacementElement, and a value in the range \[0,1\] that is a parameter along the edge specified. Once created, the path style of the DisplacementPath can get set using the PathStyle property. The anchor point can also be changed using SetAnchorPoint().

The following example creates a new displacement by moving the first wall found vertically and horizontally and then adds a displacement path for it.

| **Code Region: Create displacement and path** |
| --- |
| 
```
public static void CreateDisplacementAndPath(Document doc, View view)
{
    // Find roof
    FilteredElementCollector fec = new FilteredElementCollector(doc);
    fec.OfClass(typeof(RoofBase));
    RoofBase roof = fec.FirstElement() as RoofBase;

    // Get a geometric reference for the path
    Reference edgeRef = GetHorizontalEdgeReference(roof);

    using (Transaction t = new Transaction(doc, "CreateDisplacementAndPath"))
    {
        t.Start();
        // Create a new top level DisplacementElement
        DisplacementElement dispElem = DisplacementElement.Create(doc, new ElementId[] { roof.Id }, new XYZ(10, 0, 20), view, null);

        // Create the path associated to the element
        DisplacementPath.Create(doc, dispElem, edgeRef, 0.5);
        t.Commit();
    }
}

private static Reference GetHorizontalEdgeReference(Element elem)
{
    //Find target edge from lower face of roof
    Options options = new Options();
    options.ComputeReferences = true;

    GeometryElement geomElem = elem.get_Geometry(options);

    foreach (var geomObj in geomElem)
    {
        if (geomObj is Solid)
        {
            Solid solid = geomObj as Solid;
            var faces = solid.Faces;

            foreach (Face face in faces)
            {
                BoundingBoxUV box = face.GetBoundingBox();
                UV midpoint = (box.Min + box.Max) / 2.0;
                if (face.ComputeNormal(midpoint).Normalize().Z < -0.1) // Downward facing, this is good enough
                {
                    var edgeLoops = face.EdgeLoops;
                    foreach (EdgeArray edgeArray in edgeLoops)
                    {
                        foreach (Edge edge in edgeArray)
                        {
                            // horizontal?
                            if (Math.Abs(edge.AsCurve().ComputeDerivatives(0.0, true).BasisX.DotProduct(XYZ.BasisZ)) - 1 <= 0.00001)
                            {
                                return edge.Reference;
                            }
                        }
                    }
                }
            }
        }
    }

    return null;
}
```

 |

The associated DisplacementElement may have a parent DisplacementElement and this parent may have its own parent DisplacementElement, producing a series of ancestors. The terminal point may be the point's original (un-displaced) location, or the corresponding point on any of the intermediate displaced locations corresponding to these ancestor DisplacementElements. The DisplacementPath . AncestorIdx property specifies the end point of the path.


<!-- ===== END: Help  Displaced Views  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  UIView  Autodesk.md ===== -->

---
created: 2026-01-28T20:53:11 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_UIView_html
author: 
---

# Help | UIView | Autodesk

> ## Excerpt
> While the View class is the base class for all view types in Revit and keeps tracks of elements in the view, the UIView class contains data about the view windows in the Revit user interface. A list of all open views can be retrieved from the UIDocument using the GetOpenUIViews() method. The UIView class has methods to get information about the views drawing area as well as to pan and zoom the active view.

---
While the View class is the base class for all view types in Revit and keeps tracks of elements in the view, the UIView class contains data about the view windows in the Revit user interface. A list of all open views can be retrieved from the UIDocument using the GetOpenUIViews() method. The UIView class has methods to get information about the views drawing area as well as to pan and zoom the active view.

UIView.GetWindowRectangle() returns a rectangle that describes the size and placement of the UIView window. It does not include the window border or title bar.

### Zoom Operations

UIView has several methods related to zooming the active view. UIView.GetZoomCorners() gets the corners of the view's rectangle in model coordinates and UIView.ZoomAndCenterRectangle() offers the ability to zoom and pan the active view to center on the input region of the model.

The ZoomToFit() and ZoomSheetSize() methods provide quick ways to adjust the zoom of the window, while the Zoom() method can be used to zoom in or out by a specified factor.

### Closing a View

UIView.Close() can close a visible window. However, it cannot be used to close the last active window. Attempting to close the last active window will throw an exception.


<!-- ===== END: Help  UIView  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  View Templates  Autodesk.md ===== -->

---
created: 2026-01-28T20:53:16 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Templates_html
author: 
---

# Help | View Templates | Autodesk

> ## Excerpt
> Element.Parameter.Set(integer)

---
View Scale Scale Value VIEW\_SCALE Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.Scale property To include/exclude in non-controlled parameters set, VIEW\_SCALE has to be usedtogether with with the following parameters: VIEW\_SCALE\_PULLDOWN\_IMPERIAL VIEW\_SCALE\_PULLDOWN\_METRIC Display Model VIEW\_MODEL\_DISPLAY\_MODE Valid for all plan views, Section, Elevation, Detail Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Valid values are 0 (Normal), 1 (Halftone) and 2 (Do not display) Detail Level VIEW\_DETAIL\_LEVEL Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.DetailLevel property Use also View.CanModifyDetailLevel() and View.HasDetailLevel() Parts Visibility VIEW\_PARTS\_VISIBILITY Valid for all plan views, all 3D views, Section, Elevation, Detail View.PartsVisibility property V/G Overrides Model VIS\_GRAPHICS\_MODEL Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetCategoryOverrides

View.SetCategoryOverrides

V/G Overrides Annotation VIS\_GRAPHICS\_ANNOTATION Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetCategoryOverrides

View.SetCategoryOverrides

V/G Overrides Analytical Model VIS\_GRAPHICS\_ANALYTICAL\_MODEL Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetCategoryOverrides

View.SetCategoryOverrides

V/G Overrides Import VIS\_GRAPHICS\_IMPORT Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetCategoryOverrides

View.SetCategoryOverrides

Imported categories are not built-in, so they can be found using other API operations V/G Overrides Filters VIS\_GRAPHICS\_FILTERS Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetFilters

View.GetFilterOverrides

View.SetFilterOverrides

V/G Overrides Worksets VIS\_GRAPHICS\_WORKSETS Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetWorksetVisibility

View.SetWorksetVisibility

Valid only if Document.IsWorkshared() is true

Use also View.IsWorksetVisible(�)

V/G Overrides RVT Links VIS\_GRAPHICS\_RVT\_LINKS Valid for all plan views, all 3D views, Section, Elevation, Detail No API access at the time (Revit 2020) Valid only if Revit links are present in the document V/G Overrides Point Clouds VIS\_GRAPHICS\_POINT\_CLOUDS Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetPointCloudOverrides

View.SetPointCloudOverrides

Valid only if PointCloudInstance elements are present in the document

Use also View.ArePointCloudsHidden()

V/G Overrides Coordination Model VIS\_GRAPHICS\_COORDINATION\_MODEL Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetDirectContext3DHandleOverrides Valid only if NavisWorks coordination models are linked in the document V/G Overrides Design Options VIS\_GRAPHICS\_DESIGN\_OPTIONS Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView, all schedules No API access at the time (Revit 2020) Valid only if design options other than �Main Model� are present in the document Model Display GRAPHIC\_DISPLAY\_OPTIONS\_MODEL Valid for all plan views, all 3D views, Section, Elevation, Detail View.GetViewDisplayModel

View.SetViewDisplayModel

Shadow GRAPHIC\_DISPLAY\_OPTIONS\_SHADOW Valid for all plan views, all 3D views, Section, Elevation, Detail No API access at the time (Revit 2020) Sketchy Lines GRAPHIC\_DISPLAY\_OPTIONS\_SKETCHY\_LINES Valid for all plan views, all 3D views, Section, Elevation, Detail View.GetSketchyLines

View.SetSketchyLines

Depth Cueing GRAPHIC\_DISPLAY\_OPTIONS\_FOG Valid for all plan views, all 3D views, Section, Elevation, Detail View.GetDepthCueing

View.SetDepthCueing

Use also View.CanUseDepthCueing() Lighting GRAPHIC\_DISPLAY\_OPTIONS\_LIGHTING Valid for all plan views, all 3D views, Section, Elevation, Detail Partial API access at the time (Revit 2020):

View.ShadowIntensity property

View.SunLightIntensity property

Photographic Exposure GRAPHIC\_DISPLAY\_OPTIONS\_PHOTO\_EXPOSURE Valid for all plan views, all 3D views, Section, Elevation, Detail API access provided only for 3D views:

View3D.GetRenderingSettings

View3D.SetRenderingSettings

Background GRAPHIC\_DISPLAY\_OPTIONS\_BACKGROUND Valid for all plan views, all 3D views, Section, Elevation, Detail View.GetBackground

View.SetBackGround

Far Clipping VIEWER\_BOUND\_FAR\_CLIPPING Section, Elevation, Detail Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Phase Filter VIEW\_PHASE\_FILTER Valid for all plan views, all 3D views, Section, Elevation, Detail, all schedules Element.Parameter.AsElementId()

Element.Parameter.Set(ElementId)

Discipline VIEW\_DISCIPLINE Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.Discipline property Show Hidden Lines VIEW\_SHOW\_HIDDEN\_LINES Valid for all plan views, all 3D views, Section, Elevation, Detail Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Valid values are 0 (None), 1 (By Discipline), 2 (All) Color Scheme Location COLOR\_SCHEME\_LOCATION Valid for all plan views except for ceiling, Section, Elevation, Detail Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Valid values are 0 (Foreground), 1 (Background) Color Scheme VIEW\_SCHEMA\_SETTING\_FOR\_BUILDING Valid for all plan views except for ceiling, Section, Elevation, Detail No API access at the time (Revit 2020) Underlay Orientation VIEW\_UNDERLAY\_ORIENTATION Valid for all plan views ViewPlan.GetUnderlayOrientation

ViewPlan.SetUnderlayOrientation

View Range PLAN\_VIEW\_RANGE Valid for all plan views ViewPlan.GetViewRange

ViewPlan.SetViewRange

Orientation PLAN\_VIEW\_NORTH Valid for all plan views Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Valid values are 0 (Project North), 1 (True North) System Color Schemes VIEW\_SCHEMA\_SETTING\_FOR\_SYSTEM\_TEMPLATE Valid for all plan views except for ceiling No API access at the time (Revit 2020) Depth Clipping VIEW\_BACK\_CLIPPING Valid for all plan views Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Valid values are 0 (No Clip), 1 (Clip With Line), 2 (Clip With No Line) Rendering Settings VIEWER3D\_RENDER\_SETTINGS Valid for all 3D views View3D.GetRenderingSettings

View3D.SetRenderingSettings

Visual Style MODEL\_GRAPHICS\_STYLE\_ANON\_DRAFT Valid for DraftingView View.DisplayStyle property Use also View.HasDisplayStyle() Fields SCHEDULE\_FIELDS\_PARAM Valid for all schedules ViewSchedule.Definition.GetField

ViewSchedule.Definition.AddField

ViewSchedule.Definition.RemoveField

Filter SCHEDULE\_FILTER\_PARAM Valid for all schedules ViewSchedule.Definition.GetFilter

ViewSchedule.Definition.AddFilter

ViewSchedule.Definition.RemoveFilter

Sorting/Grouping SCHEDULE\_GROUP\_PARAM Valid for all schedules ViewSchedule.Definition.GetSortGroupField

ViewSchedule.Definition.AddSortGroupField

ViewSchedule.Definition.RemoveSortGroupField

Formatting SCHEDULE\_FORMAT\_PARAM Valid for all schedules ViewSchedule.Definition.GetField().IsHidden

ViewSchedule.Definition.GetField().ColumnHeading

ViewSchedule.Definition.GetField().GetFormatOptions

ViewSchedule.Definition.GetField().SetFormatOptions

etc.

Appearance SCHEDULE\_SHEET\_APPEARANCE\_PARAM Valid for all schedules ViewSchedule.Definition.ShowTitle

ViewSchedule.Definition.ShowHeaders

etc.


<!-- ===== END: Help  View Templates  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Temporary Graphics  Autodesk.md ===== -->

---
created: 2026-01-28T20:53:21 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_Temporary_Graphics_html
author: 
---

# Help | Temporary Graphics | Autodesk

> ## Excerpt
> The TemporaryGraphicsManager class allows you to create temporary graphics in Revit views. The graphics created by this class are not subject to undo and are not saved. The Revit API developer should manage their lifetime, creation and destruction, though Revit will destroy all of them when closing the model.

---
The `TemporaryGraphicsManager` class allows you to create temporary graphics in Revit views. The graphics created by this class are not subject to undo and are not saved. The Revit API developer should manage their lifetime, creation and destruction, though Revit will destroy all of them when closing the model.

The `AddControl` method creates a control in a specified view based on an instance of the `InCanvasControlData` class which defines the image path and location in model coordinates of the control. Additional functionality exists in the methods:

-   RemoveControl
-   SetVisibility
-   UpdateControl

This code sample creates a temporary control at the center of a wall. The website [www.autodesk.com](http://www.autodesk.com/) is opened When the user clicks on the control. The `OnClick` method is implemented in a server class that derives from `ITemporaryGraphicsHandler`.

**Code Region: Creating a Temporary Control**

```
private void TemporaryGraphicsControl(Wall wall)
{
    Document doc = wall.Document;

    MultiServerService externalService = ExternalServiceRegistry.GetService(
        ExternalServices.BuiltInExternalServices.TemporaryGraphicsHandlerService) as MultiServerService;
    MyGraphicsService myGraphicsService = new MyGraphicsService();
    externalService.AddServer(myGraphicsService);
    externalService.SetActiveServers(
        new List<Guid> {myGraphicsService.GetServerId()});

    TemporaryGraphicsManager mgr = TemporaryGraphicsManager.GetTemporaryGraphicsManager(doc);
    XYZ controlPoint = ((LocationCurve)wall.Location).Curve.Evaluate(0.5, true);
    InCanvasControlData data = new InCanvasControlData(
        @"C:/Autodesk/image32.bmp",
        controlPoint);
    mgr.AddControl(data, doc.ActiveView.Id);
}

public class MyGraphicsService: ITemporaryGraphicsHandler
{
    public void OnClick(TemporaryGraphicsCommandData data)
    {
        Process.Start("https://www.autodesk.com");
    }
    public string GetName()
    { return "My Graphics Service"; }
    public string GetDescription()
    { return "This is a graphics service"; }
    public string GetVendorId()
    { return "ADSK"; }
    public ExternalServiceId GetServiceId()
    { return ExternalServices.BuiltInExternalServices.TemporaryGraphicsHandlerService; }
    public Guid GetServerId()
    { return new Guid("a8debc37-19fe-4198-1198-01a891ff1a7f"); }
}
```


<!-- ===== END: Help  Temporary Graphics  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Transactions  Autodesk.md ===== -->

---
created: 2026-01-28T20:53:26 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_html
author: 
---

# Help | Transactions | Autodesk

> ## Excerpt
> Transactions are context-like objects that encapsulate any changes to a Revit model. Any change to a document can only be made while there is an active transaction open for that document. Attempting to change the document outside of a transaction will throw an exception. Changes do not become a part of the model until the active transaction is committed. Consequently, all changes made in a transaction can be rolled back either explicitly or implicitly (by the destructor). Only one transaction per document can be open at any given time. A transaction may consist of one or more operations.

---
Transactions are context-like objects that encapsulate any changes to a Revit model. Any change to a document can only be made while there is an active transaction open for that document. Attempting to change the document outside of a transaction will throw an exception. Changes do not become a part of the model until the active transaction is committed. Consequently, all changes made in a transaction can be rolled back either explicitly or implicitly (by the destructor). Only one transaction per document can be open at any given time. A transaction may consist of one or more operations.

There are three main classes in the Revit API related to transactions:

-   Transaction
    
-   SubTransaction
    
-   TransactionGroup
    

This section will discuss each of these classes in more depth. Only the Transaction class is required to make changes to a document. The other classes can be used to better organize changes.

Note: An exception will be thrown if a transaction is started from an outside thread or outside modeless dialog. Transactions can only be started from supported API workflows, such as part of an external command, event, updater, or call-back.


<!-- ===== END: Help  Transactions  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Transaction Classes  Autodesk.md ===== -->

---
created: 2026-01-28T20:53:30 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_Transaction_Classes_html
author: 
---

# Help | Transaction Classes | Autodesk

> ## Excerpt
> All three transaction objects share some common methods:

---
All three transaction objects share some common methods:

**Table 51: Common Transaction Object Methods**

<table summary="" id="GUID-BECA30DB-23B4-4E71-BE24-DC4DD176E52D__TABLE_34C100F27C4A4D70A1FFD309A7947A69"><tbody><tr><td><b>Method</b></td><td><b>Description</b></td></tr><tr><td>Start</td><td>Will start the context</td></tr><tr><td>Commit</td><td>Ends the context and commits all changes to the document</td></tr><tr><td>Rollback</td><td>Ends the context and discards all changes to the document</td></tr><tr><td>GetStatus</td><td>Returns the current status of the transaction object</td></tr></tbody></table>

In addition to the GetStatus() method returning the current status, the Start, Commit and RollBack methods also return a TransactionStatus indicating whether or not the method was successful. Available TransactionStatus values include:

**Table 52: TransactionStatus values**

<table summary="" id="GUID-BECA30DB-23B4-4E71-BE24-DC4DD176E52D__TABLE_C9A92B297B574CD18C8F55169F018EAC"><tbody><tr><td><b>Status</b></td><td><b>Description</b></td></tr><tr><td>Uninitialized</td><td>The initial value after object is instantiated; the context has not started yet</td></tr><tr><td>Started</td><td>Transaction object has successfully started (Start was called)</td></tr><tr><td>RolledBack</td><td>Transaction object was successfully rolled back (Rollback was called)</td></tr><tr><td>Committed</td><td>Transaction object was successfully committed (Commit was called)</td></tr><tr><td>Pending</td><td>Transaction object was attempted to be either submitted or rolled back, but due to failures that process could not be finished yet and is waiting for the end-user's response (in a modeless dialog). Once the failure processing is finished, the status will be automatically updated (to either Committed or RolledBack status).</td></tr></tbody></table>

### Transaction

A transaction is a context required in order to make any changes to a Revit model. Only one transaction can be open at a time; nesting is not allowed. Each transaction must have a name, which will be listed on the Undo menu in Revit once a transaction is successfully committed.

<table summary="" id="GUID-BECA30DB-23B4-4E71-BE24-DC4DD176E52D__TABLE_9B632B9A88174C848731232B27649C6E"><tbody><tr><td><b>Code Region 23-1: Using transactions</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreatingModelLines</span><span>(</span><span>UIApplication</span><span> uiApplication</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document </span><span>=</span><span> uiApplication</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application </span><span>=</span><span> uiApplication</span><span>.</span><span>Application</span><span>;</span><span>

    </span><span>// Create a few geometry lines. These lines are not elements,</span><span>
    </span><span>// therefore they do not need to be created inside a document transaction.</span><span>
    XYZ </span><span>Point1</span><span> </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
    XYZ </span><span>Point2</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ </span><span>Point3</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ </span><span>Point4</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>

    </span><span>Line</span><span> geomLine1 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>Point1</span><span>,</span><span> </span><span>Point2</span><span>);</span><span>
    </span><span>Line</span><span> geomLine2 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>Point4</span><span>,</span><span> </span><span>Point3</span><span>);</span><span>
    </span><span>Line</span><span> geomLine3 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>Point1</span><span>,</span><span> </span><span>Point4</span><span>);</span><span>

    </span><span>// This geometry plane is also transaction and does not need a transaction</span><span>
    XYZ origin </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
    XYZ normal </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>);</span><span>
    </span><span>Plane</span><span> geomPlane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>normal</span><span>,</span><span> origin</span><span>);</span><span>

    </span><span>// In order to a sketch plane with model curves in it, we need</span><span>
    </span><span>// to start a transaction because such operations modify the model.</span><span>

    </span><span>// All and any transaction should be enclosed in a 'using'</span><span>
    </span><span>// block or guarded within a try-catch-finally blocks</span><span>
    </span><span>// to guarantee that a transaction does not out-live its scope.</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>transaction</span><span>.</span><span>Start</span><span>(</span><span>"Create model curves"</span><span>)</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// Create a sketch plane in current document</span><span>
            </span><span>SketchPlane</span><span> sketch </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span>geomPlane</span><span>);</span><span>

            </span><span>// Create a ModelLine elements using the geometry lines and sketch plane</span><span>
            </span><span>ModelLine</span><span> line1 </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geomLine1</span><span>,</span><span> sketch</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>;</span><span>
            </span><span>ModelLine</span><span> line2 </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geomLine2</span><span>,</span><span> sketch</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>;</span><span>
            </span><span>ModelLine</span><span> line3 </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geomLine3</span><span>,</span><span> sketch</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>;</span><span>

            </span><span>// Ask the end user whether the changes are to be committed or not</span><span>
            </span><span>TaskDialog</span><span> taskDialog </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Revit"</span><span>);</span><span>
            taskDialog</span><span>.</span><span>MainContent</span><span> </span><span>=</span><span> </span><span>"Click either [OK] to Commit, or [Cancel] to Roll back the transaction."</span><span>;</span><span>
            </span><span>TaskDialogCommonButtons</span><span> buttons </span><span>=</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Ok</span><span> </span><span>|</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Cancel</span><span>;</span><span>
            taskDialog</span><span>.</span><span>CommonButtons</span><span> </span><span>=</span><span> buttons</span><span>;</span><span>

            </span><span>if</span><span> </span><span>(</span><span>TaskDialogResult</span><span>.</span><span>Ok</span><span> </span><span>==</span><span> taskDialog</span><span>.</span><span>Show</span><span>())</span><span>
            </span><span>{</span><span>
                </span><span>// For many various reasons, a transaction may not be committed</span><span>
                </span><span>// if the changes made during the transaction do not result a valid model.</span><span>
                </span><span>// If committing a transaction fails or is canceled by the end user,</span><span>
                </span><span>// the resulting status would be RolledBack instead of Committed.</span><span>
                </span><span>if</span><span> </span><span>(</span><span>TransactionStatus</span><span>.</span><span>Committed</span><span> </span><span>!=</span><span> transaction</span><span>.</span><span>Commit</span><span>())</span><span>
                </span><span>{</span><span>
                    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Failure"</span><span>,</span><span> </span><span>"Transaction could not be committed"</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span>
            </span><span>{</span><span>
                transaction</span><span>.</span><span>RollBack</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### SubTransaction

A SubTransaction can be used to enclose a set of model-modifying operations. Sub-transactions are optional. They are not required in order to modify the model. They are a convenience tool to allow logical splitting of larger tasks into smaller ones. Sub-transactions can only be created within an already opened transaction and must be closed (either committed or rolled back) before the transaction is closed (committed or rolled back). Unlike transactions, sub-transaction may be nested, but any nested sub-transaction must be closed before the enclosing sub-transaction is closed. Sub-transactions do not have a name, for they do not appear on the Undo menu in Revit.

### TransactionGroup

TransactionGroup allows grouping together several independent transactions, which gives the owner of a group an opportunity to address many transactions at once. When a transaction group is to be closed, it can be rolled back, which means that all previously committed transactions belonging to the group will be rolled back. If not rolled back, a group can be either committed or assimilated. In the former case, all committed transactions (within the group) will be left as they were. In the later case, transactions within the group will be merged together into one single transaction that will bear the group's name.

A transaction group can only be started when there is no transaction open yet, and must be closed only after all enclosed transactions are closed (rolled back or committed). Transaction groups can be nested, but any nested group must be closed before the enclosing group is closed. Transaction groups are optional. They are not required in order to make modifications to a model.

The following example shows the use of a TransactionGroup to combine two separate Transactions using the Assimilate() method. The following code will result in a single Undo item added to the Undo menu with the name "Level and Grid".

<table summary="" id="GUID-BECA30DB-23B4-4E71-BE24-DC4DD176E52D__TABLE_8FDAAAA048F842039B2B6820C17EB28E"><tbody><tr><td><b>Code Region 23-2: Combining multiple transactions into a TransactionGroup</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CompoundOperation</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// All and any transaction group should be enclosed in a 'using' block or guarded within</span><span>
    </span><span>// a try-catch-finally blocks to guarantee that the group does not out-live its scope.</span><span>
    </span><span>using</span><span> </span><span>(</span><span>TransactionGroup</span><span> transGroup </span><span>=</span><span> </span><span>new</span><span> </span><span>TransactionGroup</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Level and Grid"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>transGroup</span><span>.</span><span>Start</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// We are going to call two methods, each having its own local transaction.</span><span>
            </span><span>// For our compound operation to be considered successful, both the individual</span><span>
            </span><span>// transactions must succeed. If either one fails, we will roll our group back,</span><span>
            </span><span>// regardless of what transactions might have already been committed.</span><span>

            </span><span>if</span><span> </span><span>(</span><span>CreateLevel</span><span>(</span><span>document</span><span>,</span><span> </span><span>25.0</span><span>)</span><span> </span><span>&amp;&amp;</span><span> </span><span>CreateGrid</span><span>(</span><span>document</span><span>,</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span>0</span><span>,</span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span>0</span><span>,</span><span>0</span><span>)))</span><span>
            </span><span>{</span><span>
                </span><span>// The process of assimilating will merge the two (or any number of) committed</span><span>
                </span><span>// transaction together and will assign the grid's name to the one resulting transaction,</span><span>
                </span><span>// which will become the only item from this compound operation appearing in the undo menu.</span><span>
                transGroup</span><span>.</span><span>Assimilate</span><span>();</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span>
            </span><span>{</span><span>
                </span><span>// Since we could not successfully finish at least one of the individual</span><span>
                </span><span>// operation, we are going to roll the entire group back, which will</span><span>
                </span><span>// undo any transaction already committed while this group was open.</span><span>
                transGroup</span><span>.</span><span>RollBack</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>bool</span><span> </span><span>CreateLevel</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>double</span><span> elevation</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// All and any transaction should be enclosed in a 'using'</span><span>
    </span><span>// block or guarded within a try-catch-finally blocks</span><span>
    </span><span>// to guarantee that a transaction does not out-live its scope.</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Creating Level"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>// Must start a transaction to be able to modify a document</span><span>

        </span><span>if</span><span>(</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span> </span><span>==</span><span> transaction</span><span>.</span><span>Start</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> </span><span>Level</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> elevation</span><span>))</span><span>
            </span><span>{</span><span>
                </span><span>// For many various reasons, a transaction may not be committed</span><span>
                </span><span>// if the changes made during the transaction do not result a valid model.</span><span>
                </span><span>// If committing a transaction fails or is canceled by the end user,</span><span>
                </span><span>// the resulting status would be RolledBack instead of Committed.</span><span>
                </span><span>return</span><span> </span><span>(</span><span>TransactionStatus</span><span>.</span><span>Committed</span><span> </span><span>==</span><span> transaction</span><span>.</span><span>Commit</span><span>());</span><span>
            </span><span>}</span><span>

            </span><span>// For we were unable to create the level, we will roll the transaction back</span><span>
            </span><span>// (although on this simplified case we know there weren't any other changes)</span><span>

            transaction</span><span>.</span><span>RollBack</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>return</span><span> </span><span>false</span><span>;</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>bool</span><span> </span><span>CreateGrid</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> XYZ p1</span><span>,</span><span> XYZ p2</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// All and any transaction should be enclosed in a 'using'</span><span>
    </span><span>// block or guarded within a try-catch-finally blocks</span><span>
    </span><span>// to guarantee that a transaction does not out-live its scope.</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Creating Grid"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>// Must start a transaction to be able to modify a document</span><span>
        </span><span>if</span><span> </span><span>(</span><span>TransactionStatus</span><span>.</span><span>Started</span><span> </span><span>==</span><span> transaction</span><span>.</span><span>Start</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>// We create a line and use it as an argument to create a grid</span><span>
            </span><span>Line</span><span> gridLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p1</span><span>,</span><span> p2</span><span>);</span><span>

            </span><span>if</span><span> </span><span>((</span><span>null</span><span> </span><span>!=</span><span> gridLine</span><span>)</span><span> </span><span>&amp;&amp;</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> </span><span>Grid</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> gridLine</span><span>)))</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>TransactionStatus</span><span>.</span><span>Committed</span><span> </span><span>==</span><span> transaction</span><span>.</span><span>Commit</span><span>())</span><span>
                </span><span>{</span><span>
                </span><span>return</span><span> </span><span>true</span><span>;</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>

            </span><span>// For we were unable to create the grid, we will roll the transaction back</span><span>
            </span><span>// (although on this simplified case we know there weren't any other changes)</span><span>

            transaction</span><span>.</span><span>RollBack</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>return</span><span> </span><span>false</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Transaction Classes  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Transactions in Events  Autodesk.md ===== -->

---
created: 2026-01-28T20:53:35 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_Transactions_in_Events_html
author: 
---

# Help | Transactions in Events | Autodesk

> ## Excerpt
> Events do not automatically open transactions. Therefore, the document will not be modified during an event unless one of the event's handlers modifies it by making changes inside a transaction. If an event handler opens a transaction it is required that it will also close it (commit it or roll it back), otherwise all changes will be discarded.

---
### Modifying the document during an event

Events do not automatically open transactions. Therefore, the document will not be modified during an event unless one of the event's handlers modifies it by making changes inside a transaction. If an event handler opens a transaction it is required that it will also close it (commit it or roll it back), otherwise all changes will be discarded.

Please be aware that modifying the active document is not permitted during some events (e.g. the DocumentClosing event). If an event handler attempts to make modifications during such an event, an exception will be thrown. The event documentation indicates whether or not the event is read-only.

### DocumentChanged Event

The DocumentChanged event is raised after every transaction gets committed, undone, or redone. This is a read-only event, designed to allow you to keep external data in synch with the state of the Revit database. To update the Revit database in response to changes in elements, use the [Dynamic Model Update](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_html) framework.


<!-- ===== END: Help  Transactions in Events  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Failure Handling Options  Autodesk.md ===== -->

---
created: 2026-01-28T20:53:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_Failure_Handling_Options_html
author: 
---

# Help | Failure Handling Options | Autodesk

> ## Excerpt
> Failure handling options are options for how failures, if any, should be handled at the end of a transaction. Failure handling options may be set at any time before calling either Transaction.Commit() or Transaction.RollBack() using the Transaction.SetFailureHandlingOptions() method. However, after a transaction is committed or rolled back, the options return to their respective default settings.

---
Failure handling options are options for how failures, if any, should be handled at the end of a transaction. Failure handling options may be set at any time before calling either Transaction.Commit() or Transaction.RollBack() using the Transaction.SetFailureHandlingOptions() method. However, after a transaction is committed or rolled back, the options return to their respective default settings.

The SetFailureHandlingOptions() method takes a FailureHandlingOptions object as a parameter. This object cannot be created, it must be obtained from the transaction using the GetFailureHandlingOptions() method. Options are set by calling the corresponding Set method, such as SetClearAfterRollback(). The following sections discuss the failure handling options in more detail.

### ClearAfterRollback

This option controls whether all warnings should be cleared after a transaction is rolled back. The default value is False.

### DelayedMiniWarnings

This options controls whether mini-warnings, if any, are displayed at the end of the transaction currently being ended, or if they should be postponed until the end of next transaction. This is typically used within a chain of transactions when it is not desirable to show intermediate warnings at the end of each step, but rather to wait until the completion of the entire chain.

Warnings may be delayed for more than one transaction. The first transaction that does not have this option set to True will display all of its own warnings, if any, as well as all warnings that might have accumulated from previous transactions. The default value is False.

Note: This option is ignored in modal mode (see ForcedModalHandling below). ### ForcedModalHandling

This options controls whether eventual failures will be handled modally or modelessly. The default is True. Be aware that if the modeless failure handling is set, processing the transaction may be done asynchronously, which means that upon returning from the Commit or RollBack calls, the transaction will not be finished yet (the status will be 'Pending').

### SetFailuresPreprocessor

This interface, if provided, is invoked when there are failures found at the end of a transaction. The preprocessor may examine current failures and even try to resolve them. See [Failure Posting and Handling](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Failure_Posting_and_Handling_html) for more information.

### SetTransactionFinalizer

A finalizer is an interface, which, if provided, can be used to perform a custom action at the end of a transaction. Note that it is not invoked when the Commit() or RollBack() methods are called, but only after the process of committing or rolling back is completed. Transaction finalizers must implement the _ITransactionFinalizer_ interface, which requires two functions to be defined:

-   OnCommitted - called at the end of committing a transaction
-   OnRolledBack - called at the end of rolling back a transaction

Note: Since the finalizer is called after the transaction has finished, the document is not modifiable from the finalizer unless a new transaction is started.


<!-- ===== END: Help  Failure Handling Options  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Getting Element Geometry and AnalyticalElement  Autodesk.md ===== -->

---
created: 2026-01-28T20:53:44 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_Getting_Element_Geometry_and_AnalyticalModel_html
author: 
---

# Help | Getting Element Geometry and AnalyticalElement | Autodesk

> ## Excerpt
> After new elements are created or elements are modified, regeneration and auto-joining of elements is required to propagate the changes throughout the model. Without a regeneration (and auto-join, when relevant), the Geometry property and the AnalyticalElement for Elements are either unobtainable (in the case of creating a new element) or they may be invalid. It is important to understand how and when regeneration occurs before accessing the Geometry or AnalyticalElement of an Element.

---
After new elements are created or elements are modified, regeneration and auto-joining of elements is required to propagate the changes throughout the model. Without a regeneration (and auto-join, when relevant), the Geometry property and the AnalyticalElement for Elements are either unobtainable (in the case of creating a new element) or they may be invalid. It is important to understand how and when regeneration occurs before accessing the Geometry or AnalyticalElement of an Element.

Although regeneration and auto-join are necessary to propagate changes made in the model, it can be time consuming. It is best if these events occur only as often as necessary.

Regeneration and auto-joining occur automatically when a transaction that modifies the model is committed successfully, or whenever the Document.Regenerate() or Document.AutoJoinElements() methods are called. Regenerate() and AutoJoinElements() may only be called inside an open transaction. It should be noted that the Regeneration() method can fail, in which case the RegenerationFailedException will be thrown. If this happens, the changes to the document need to be rolled back by rolling back the current transaction or subtransaction.

For more information, see [Analytical Element](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Analytical_Model_html) and [Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html).

The following sample program demonstrates how a transaction populates these properties:

<table summary="" id="GUID-37357B53-1A5F-4913-BD59-BD4171BABE5E__TABLE_6E16CB4DD4D045479B35CBC78998C92E"><tbody><tr><td><b>Code Region 23-3: Transaction populating Geometry and AnalyticalPanel properties</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>TransactionDuringElementCreation</span><span>(</span><span>UIApplication</span><span> uiApplication</span><span>,</span><span> </span><span>Level</span><span> level</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document </span><span>=</span><span> uiApplication</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>// Build a location line for the wall creation</span><span>
    XYZ start </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ </span><span>end</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Line</span><span> geomLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>start</span><span>,</span><span> </span><span>end</span><span>);</span><span>

    </span><span>// All and any transaction should be enclosed in a 'using'</span><span>
    </span><span>// block or guarded within a try-catch-finally blocks</span><span>
    </span><span>// to guarantee that a transaction does not out-live its scope.</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> wallTransaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Creating wall"</span><span>))</span><span>
    </span><span>{</span><span>
       </span><span>// To create a wall, a transaction must be first started</span><span>
       </span><span>if</span><span> </span><span>(</span><span>wallTransaction</span><span>.</span><span>Start</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
       </span><span>{</span><span>
           </span><span>// Create a wall using the location line</span><span>
           </span><span>Wall</span><span> wall </span><span>=</span><span> </span><span>Wall</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> geomLine</span><span>,</span><span> level</span><span>.</span><span>Id</span><span>,</span><span> </span><span>true</span><span>);</span><span>

           </span><span>// the transaction must be committed before you can</span><span>
           </span><span>// get the value of Geometry and AnalyticalPanel.</span><span>

           </span><span>if</span><span> </span><span>(</span><span>wallTransaction</span><span>.</span><span>Commit</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Committed</span><span>)</span><span>
           </span><span>{</span><span>
               </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Options</span><span> options </span><span>=</span><span> uiApplication</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewGeometryOptions</span><span>();</span><span>
               </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geoelem </span><span>=</span><span> wall</span><span>.</span><span>get_Geometry</span><span>(</span><span>options</span><span>);</span><span>
               </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Structure</span><span>.</span><span>AnalyticalPanel</span><span> analyticalPanel </span><span>=</span><span> </span><span>(</span><span>AnalyticalPanel</span><span>)</span><span>document</span><span>.</span><span>GetElement</span><span>(</span><span>AnalyticalToPhysicalAssociationManager</span><span>.</span><span>GetAnalyticalToPhysicalAssociationManager</span><span>(</span><span>document</span><span>).</span><span>GetAssociatedElementId</span><span>(</span><span>wall</span><span>.</span><span>Id</span><span>));</span><span>
           </span><span>}</span><span>
       </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The transaction timeline for this sample is as follows:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-A7296713-19E7-4C50-A7B6-F3F7893A8EDD-low.png)**Figure 134: Transaction timeline**


<!-- ===== END: Help  Getting Element Geometry and AnalyticalElement  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Temporary transactions  Autodesk.md ===== -->

---
created: 2026-01-28T20:53:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_Temporary_transactions_html
author: 
---

# Help | Temporary transactions | Autodesk

> ## Excerpt
> It is not always required to commit a transaction. The transaction framework also allows for Trasactions to be rolled back. This is useful when there is an error during the processing of the transaction, but can also be leverage directly as a technique to create a temporary transaction.

---
It is not always required to commit a transaction. The transaction framework also allows for Trasactions to be rolled back. This is useful when there is an error during the processing of the transaction, but can also be leverage directly as a technique to create a temporary transaction.

Using a temporary transaction can be useful for certain types of analyses. For example, an application looking to extract geometric properties from a wall or other object before it is cut by openings should use a temporary transaction in conjunction with Document.Delete(). When the application deletes the elements that cut the target elements, the cut element’s geometry is restored to its original state (after the document has been regenerated).

To use a temporary transaction:

1.  Instantiate the Transaction using the Transaction constructor, and assign it a name.
2.  Call Transaction.Start()
3.  Make the temporary change(s) to the document (element modification, deletion or creation)
4.  Regenerate the document
5.  Extract the desired geometry and properties
6.  Call Transaction.RollBack() to restore the document to the previous state.

This technique is also applicable to SubTransactions.


<!-- ===== END: Help  Temporary transactions  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Walkthrough Get Selected Element Parameters  Autodesk.md ===== -->

---
created: 2026-01-28T20:48:58 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Walkthrough_Get_Selected_Element_Parameters_html
author: 
---

# Help | Walkthrough: Get Selected Element Parameters | Autodesk

> ## Excerpt
> The Element Parameters are retrieved by iterating through the Element ParameterSet. The following code sample illustrates how to retrieve the Parameter from a selected element.

---
The Element Parameters are retrieved by iterating through the Element ParameterSet. The following code sample illustrates how to retrieve the Parameter from a selected element.

Note: This example uses some Parameter members, such as AsValueString and StorageType, which are covered in subsequent topics.

<table summary="" id="GUID-D003803E-9FA0-4B2B-AB62-7DCC3A503644__TABLE_561142B017E44F6D8AB43E6EEC12AEE7"><tbody><tr><td><b>Code Region 8-1: Getting selected element parameters</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>GetElementParameterInformation</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Format the prompt information string</span><span>
    </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"Show parameters in selected Element: \n\r"</span><span>;</span><span>

    </span><span>StringBuilder</span><span> st </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>();</span><span>
    </span><span>// iterate element's parameters</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Parameter</span><span> para </span><span>in</span><span> element</span><span>.</span><span>Parameters</span><span>)</span><span>
    </span><span>{</span><span>
        st</span><span>.</span><span>AppendLine</span><span>(</span><span>GetParameterInformation</span><span>(</span><span>para</span><span>,</span><span> document</span><span>));</span><span>
    </span><span>}</span><span>

    </span><span>// Give the user some information</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt </span><span>+</span><span> st</span><span>.</span><span>ToString</span><span>());</span><span>
</span><span>}</span><span>

</span><span>String</span><span> </span><span>GetParameterInformation</span><span>(</span><span>Parameter</span><span> para</span><span>,</span><span> </span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>string</span><span> defName </span><span>=</span><span> para</span><span>.</span><span>Definition</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>"\t : "</span><span>;</span><span>
    </span><span>string</span><span> defValue </span><span>=</span><span> </span><span>string</span><span>.</span><span>Empty</span><span>;</span><span>
    </span><span>// Use different method to get parameter data according to the storage type</span><span>
    </span><span>switch</span><span> </span><span>(</span><span>para</span><span>.</span><span>StorageType</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>case</span><span> </span><span>StorageType</span><span>.</span><span>Double</span><span>:</span><span>
            </span><span>//covert the number into Metric</span><span>
            defValue </span><span>=</span><span> para</span><span>.</span><span>AsValueString</span><span>();</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>StorageType</span><span>.</span><span>ElementId</span><span>:</span><span>
            </span><span>//find out the name of the element</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> id </span><span>=</span><span> para</span><span>.</span><span>AsElementId</span><span>();</span><span>
            </span><span>if</span><span> </span><span>(</span><span>id</span><span>.</span><span>IntegerValue</span><span> </span><span>&gt;=</span><span> </span><span>0</span><span>)</span><span>
            </span><span>{</span><span>
                defValue </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>).</span><span>Name</span><span>;</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span>
            </span><span>{</span><span>
                defValue </span><span>=</span><span> id</span><span>.</span><span>IntegerValue</span><span>.</span><span>ToString</span><span>();</span><span>
            </span><span>}</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>StorageType</span><span>.</span><span>Integer</span><span>:</span><span>
            </span><span>if</span><span> </span><span>(</span><span>SpecTypeId</span><span>.</span><span>Boolean</span><span>.</span><span>YesNo</span><span> </span><span>==</span><span> para</span><span>.</span><span>Definition</span><span>.</span><span>GetDataType</span><span>())</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>para</span><span>.</span><span>AsInteger</span><span>()</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
                </span><span>{</span><span>
                    defValue </span><span>=</span><span> </span><span>"False"</span><span>;</span><span>
                </span><span>}</span><span>
                </span><span>else</span><span>
                </span><span>{</span><span>
                    defValue </span><span>=</span><span> </span><span>"True"</span><span>;</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span>
            </span><span>{</span><span>
                defValue </span><span>=</span><span> para</span><span>.</span><span>AsInteger</span><span>().</span><span>ToString</span><span>();</span><span>
            </span><span>}</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>StorageType</span><span>.</span><span>String</span><span>:</span><span>
            defValue </span><span>=</span><span> para</span><span>.</span><span>AsString</span><span>();</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>default</span><span>:</span><span>
            defValue </span><span>=</span><span> </span><span>"Unexposed parameter."</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> defName </span><span>+</span><span> defValue</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-07A40B76-5AD7-46C8-983F-494CECF88543-low.png)**Figure 26: Get wall parameters result**

Note: In Revit, some parameters have values in the drop-down list in the Element Properties dialog box. You can get the numeric values corresponding to the enumerated type for the Parameter using the Revit Platform API, but you cannot get the string representation for the values using the Parameter.AsValueString() method.


<!-- ===== END: Help  Walkthrough Get Selected Element Parameters  Autodesk.md ===== -->

---

