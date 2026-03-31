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
