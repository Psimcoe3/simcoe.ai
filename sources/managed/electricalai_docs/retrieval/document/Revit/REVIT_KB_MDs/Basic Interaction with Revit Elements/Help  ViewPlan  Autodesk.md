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
