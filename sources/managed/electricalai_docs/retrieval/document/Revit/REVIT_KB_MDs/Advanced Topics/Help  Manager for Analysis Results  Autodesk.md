---
created: 2026-01-28T21:15:21 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Analysis_Visualization_Manager_for_analysis_results_html
author: 
---

# Help | Manager for Analysis Results | Autodesk

> ## Excerpt
> A new SpatialFieldManager can be added to a view using the static SpatialFieldManager.CreateSpatialFieldManager() method. Only one manager can be associated with a view. If a view already has a SpatialFieldManager, it can be retrieved with the static method GetSpatialFieldManager().

---
A new SpatialFieldManager can be added to a view using the static SpatialFieldManager.CreateSpatialFieldManager() method. Only one manager can be associated with a view. If a view already has a SpatialFieldManager, it can be retrieved with the static method GetSpatialFieldManager().

CreateSpatialFieldManager() takes a parameter for the number of measurements that will be calculated for each point. This number defines how many results values will be associated with each point at which results are calculated. For example, if average solar radiation is computed for every month of the year, each point would have 12 corresponding values.

To add analysis results to the view, call AddSpatialFieldPrimitive() to create a new analysis results container. Four overloads of this method exist to create primitives associated with:

-   A Reference (to a curve or a face)
-   A curve and a transform
-   A face and a transform
-   No Revit geometry - To improve performance when creating many data points that are not related to Revit geometry, it is recommended to create multiple primitives with no more than 500 points each instead of one large primitive containing all points.

A typical use of the transform overloads will be to locate the results data offset from geometry in the Revit model, for example, 3 feet above a floor.

The AddSpatialFieldPrimitive() method returns a unique integer identifier of the primitive within the SpatialFieldManager, which can later be used to identify the primitive to remove it (RemoveSpatialFieldPrimitive()) or to modify the primitive (UpdateSpatialFieldPrimitive()).

Note that the AddSpatialFieldPrimitive() method creates an empty analysis results primitive. UpdateSpatialFieldPrimitive() must be called in order populate the analysis results data with points and values as shown in the [Creating analysis results data](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Analysis_Visualization_Creating_analysis_results_data_html) section.

The UpdateSpatialFieldPrimitive() method requires the unique index of an AnalysisResultSchema that has been registered with the SpatialFieldManager. An AnalysisResultSchema holds information about an analysis results, such as a name, description and the names and multipliers of all units for result visualization. The following example demonstrates how to create a new AnalysisResultSchema and set its units.

<table summary="" id="GUID-CE3064D8-2323-4C4A-B5AA-53B4AD831706__TABLE_C5D2706F622A430D9133B8936A0A6F77"><tbody><tr><td><b>Code Region: AnalysisResultsSchema</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateSchema</span><span>()</span><span>
</span><span>{</span><span>
    </span><span>IList</span><span>&lt;string&gt;</span><span> unitNames </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;string&gt;</span><span>();</span><span>
    unitNames</span><span>.</span><span>Add</span><span>(</span><span>"Feet"</span><span>);</span><span>
    unitNames</span><span>.</span><span>Add</span><span>(</span><span>"Inches"</span><span>);</span><span>
    </span><span>IList</span><span>&lt;double&gt;</span><span> multipliers </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;double&gt;</span><span>();</span><span>
    multipliers</span><span>.</span><span>Add</span><span>(</span><span>1</span><span>);</span><span>
    multipliers</span><span>.</span><span>Add</span><span>(</span><span>12</span><span>);</span><span>

    </span><span>AnalysisResultSchema</span><span> resultSchema </span><span>=</span><span> </span><span>new</span><span> </span><span>AnalysisResultSchema</span><span>(</span><span>"Schema Name"</span><span>,</span><span> </span><span>"Description"</span><span>);</span><span>

    resultSchema</span><span>.</span><span>SetUnits</span><span>(</span><span>unitNames</span><span>,</span><span> multipliers</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Once the AnalysisResultschema is configured, it needs to be registered using the SpatialFieldManager.RegisterResult() method, which will return a unique index for the result. Use GetResultSchema() and SetResultSchema() using this unique index to get and change the result after it has been registered.
