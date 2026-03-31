---
created: 2026-01-28T21:15:27 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Analysis_Visualization_Creating_analysis_results_data_html
author: 
---

# Help | Creating analysis results data | Autodesk

> ## Excerpt
> Once a primitive has been added to the SpatialFieldManager, analysis results can be created and added to the analysis results container using the UpdateSpatialFieldPrimitive() method. This method takes a set of domain points (FieldDomainPoints) where results are calculated and a set of values (FieldValues) for each point. The number of FieldValues must correspond to the number of domain points. However, each domain point can have an array of values, each for a separate measurement at this point.

---
Once a primitive has been added to the SpatialFieldManager, analysis results can be created and added to the analysis results container using the UpdateSpatialFieldPrimitive() method. This method takes a set of domain points (FieldDomainPoints) where results are calculated and a set of values (FieldValues) for each point. The number of FieldValues must correspond to the number of domain points. However, each domain point can have an array of values, each for a separate measurement at this point.

The following example creates a simple set of analysis results on an element face selected by the user. The SDK sample SpatialFieldGradient demonstrates a more complex use case where each point has multiple associated values.

<table summary="" id="GUID-2BE96F87-D3CA-448A-BBD9-262FD7EB1152__TABLE_73F197C8AC35434B8DB955DD95F5E677"><tbody><tr><td><b>Code Region 27-1: Creating Analysis Results</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateAnalysisResults</span><span>(</span><span>UIDocument</span><span> uidoc</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Document</span><span> doc </span><span>=</span><span> uidoc</span><span>.</span><span>Document</span><span>;</span><span>

        </span><span>SpatialFieldManager</span><span> sfm </span><span>=</span><span> </span><span>SpatialFieldManager</span><span>.</span><span>GetSpatialFieldManager</span><span>(</span><span>doc</span><span>.</span><span>ActiveView</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> sfm</span><span>)</span><span>
        </span><span>{</span><span>
                sfm </span><span>=</span><span> </span><span>SpatialFieldManager</span><span>.</span><span>CreateSpatialFieldManager</span><span>(</span><span>doc</span><span>.</span><span>ActiveView</span><span>,</span><span> </span><span>1</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>Reference</span><span> reference </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>PickObject</span><span>(</span><span>ObjectType</span><span>.</span><span>Face</span><span>,</span><span> </span><span>"Select a face"</span><span>);</span><span>
        </span><span>int</span><span> idx </span><span>=</span><span> sfm</span><span>.</span><span>AddSpatialFieldPrimitive</span><span>(</span><span>reference</span><span>);</span><span>

        </span><span>Face</span><span> face </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>reference</span><span>).</span><span>GetGeometryObjectFromReference</span><span>(</span><span>reference</span><span>)</span><span> </span><span>as</span><span> </span><span>Face</span><span>;</span><span>

        </span><span>IList</span><span>&lt;</span><span>UV</span><span>&gt;</span><span> uvPts </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>UV</span><span>&gt;();</span><span>
        </span><span>BoundingBoxUV</span><span> bb </span><span>=</span><span> face</span><span>.</span><span>GetBoundingBox</span><span>();</span><span>
        UV min </span><span>=</span><span> bb</span><span>.</span><span>Min</span><span>;</span><span>
        UV max </span><span>=</span><span> bb</span><span>.</span><span>Max</span><span>;</span><span>
        uvPts</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> UV</span><span>(</span><span>min</span><span>.</span><span>U</span><span>,</span><span>min</span><span>.</span><span>V</span><span>));</span><span>
        uvPts</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> UV</span><span>(</span><span>max</span><span>.</span><span>U</span><span>,</span><span>max</span><span>.</span><span>V</span><span>));</span><span>

        </span><span>FieldDomainPointsByUV</span><span> pnts </span><span>=</span><span> </span><span>new</span><span> </span><span>FieldDomainPointsByUV</span><span>(</span><span>uvPts</span><span>);</span><span>

        </span><span>List</span><span>&lt;double&gt;</span><span> doubleList </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;double&gt;</span><span>();</span><span>
        </span><span>IList</span><span>&lt;</span><span>ValueAtPoint</span><span>&gt;</span><span> valList </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ValueAtPoint</span><span>&gt;();</span><span>
        doubleList</span><span>.</span><span>Add</span><span>(</span><span>0</span><span>);</span><span>
        valList</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> </span><span>ValueAtPoint</span><span>(</span><span>doubleList</span><span>));</span><span>
        doubleList</span><span>.</span><span>Clear</span><span>();</span><span>
        doubleList</span><span>.</span><span>Add</span><span>(</span><span>10</span><span>);</span><span>
        valList</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> </span><span>ValueAtPoint</span><span>(</span><span>doubleList</span><span>));</span><span>

        </span><span>FieldValues</span><span> vals </span><span>=</span><span> </span><span>new</span><span> </span><span>FieldValues</span><span>(</span><span>valList</span><span>);</span><span>

        </span><span>AnalysisResultSchema</span><span> resultSchema </span><span>=</span><span> </span><span>new</span><span> </span><span>AnalysisResultSchema</span><span>(</span><span>"Schema Name"</span><span>,</span><span> </span><span>"Description"</span><span>);</span><span>
        </span><span>int</span><span> schemaIndex </span><span>=</span><span> sfm</span><span>.</span><span>RegisterResult</span><span>(</span><span>resultSchema</span><span>);</span><span>
        sfm</span><span>.</span><span>UpdateSpatialFieldPrimitive</span><span>(</span><span>idx</span><span>,</span><span> pnts</span><span>,</span><span> vals</span><span>,</span><span> schemaIndex</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
