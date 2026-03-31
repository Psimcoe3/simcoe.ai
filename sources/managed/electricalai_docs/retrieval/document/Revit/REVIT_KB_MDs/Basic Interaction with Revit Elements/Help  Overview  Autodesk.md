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
