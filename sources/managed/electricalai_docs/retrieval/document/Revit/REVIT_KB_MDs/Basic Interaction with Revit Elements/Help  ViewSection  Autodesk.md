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
