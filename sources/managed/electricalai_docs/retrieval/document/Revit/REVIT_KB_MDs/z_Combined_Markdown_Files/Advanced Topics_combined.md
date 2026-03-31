


<!-- ===== BEGIN: Help  Advanced Topics  Autodesk.md ===== -->

---
created: 2026-01-28T21:14:02 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Advanced Topics | Autodesk

> ## Excerpt
> 

---
### Was this information helpful?

-   Yes
-   No


<!-- ===== END: Help  Advanced Topics  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Energy Data  Autodesk.md ===== -->

---
created: 2026-01-28T21:15:07 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Energy_Data_html
author: 
---

# Help | Energy Data | Autodesk

> ## Excerpt
> The EnergyDataSettings object contains settings for gbXML Export and Heating and Cooling Load Calculations and project level settings for Conceptual Energy Analysis.

---
The EnergyDataSettings object contains settings for gbXML Export and Heating and Cooling Load Calculations and project level settings for Conceptual Energy Analysis.

The EnergyDataSettings object is derived from the Element base object. It is unique in each project, similar to ProjectInformation. Though EnergyDataSettings is a subclass of the Element class, most of the members inherited from the Element return null or an empty set except for Name, Id, UniqueId, and Parameters.

The following code sample uses the EnergyDataSettings class. The result appears in a TaskDialog after invoking the command.

<table summary="" id="GUID-C42BBD66-25E9-48C6-ABF6-001303791615__TABLE_885CE8BC60714083A07723EAA8EED263"><tbody><tr><td><b>Code Region 28-7: Using the EnergyDataSettings class</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetInfo_EnergyData</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>EnergyDataSettings</span><span> energyData </span><span>=</span><span> </span><span>EnergyDataSettings</span><span>.</span><span>GetFromDocument</span><span>(</span><span>document</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> energyData</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>string</span><span> message </span><span>=</span><span> </span><span>"energyData : "</span><span>;</span><span>
                message </span><span>+=</span><span> </span><span>"\nBuildingType : "</span><span> </span><span>+</span><span> energyData</span><span>.</span><span>BuildingType</span><span>;</span><span>
                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> message</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Energy Data  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Analysis Visualization  Autodesk.md ===== -->

---
created: 2026-01-28T21:15:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Analysis_Visualization_html
author: 
---

# Help | Analysis Visualization | Autodesk

> ## Excerpt
> The Revit API provides a mechanism for external analysis applications to easily display the results of their computation in the Revit model. The SpatialFieldManager class is the main class for communicating analysis results back to Revit. It is used to create, delete, and modify the "containers" in which the analysis results are stored. The AnalysisResultSchema class contains all information about one analysis result, such as a description and the names and multipliers of all units for result visualization. Multiple AnalysisResultSchemas can be registered with the SpatialFieldManager.

---
The Revit API provides a mechanism for external analysis applications to easily display the results of their computation in the Revit model. The SpatialFieldManager class is the main class for communicating analysis results back to Revit. It is used to create, delete, and modify the "containers" in which the analysis results are stored. The AnalysisResultSchema class contains all information about one analysis result, such as a description and the names and multipliers of all units for result visualization. Multiple AnalysisResultSchemas can be registered with the SpatialFieldManager.

The AnalysisDisplayStyle class can then be used to control the appearance of the results. Creation and modification of AnalysisDisplayStyle from a plug-in is optional; end users can have the same control over the presentation of the analysis results with the Revit UI.

The data model supported by Revit API requires that analysis results are specified at a certain set of points, and that at each point one or more distinct numbers ("measurements") are computed. The number of measurements must be the same at all model points. The results data is transient; it is stored only in the model until the document is closed. If the model is saved, closed, and reopened the analysis results will not be present.


<!-- ===== END: Help  Analysis Visualization  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Manager for Analysis Results  Autodesk.md ===== -->

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


<!-- ===== END: Help  Manager for Analysis Results  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Creating analysis results data  Autodesk.md ===== -->

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


<!-- ===== END: Help  Creating analysis results data  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Analysis Results Display  Autodesk.md ===== -->

---
created: 2026-01-28T21:15:32 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Analysis_Visualization_Analysis_Results_Display_html
author: 
---

# Help | Analysis Results Display | Autodesk

> ## Excerpt
> The AnalysisDisplayStyle class can be used to control how the analysis results are displayed in the view. The static CreateAnalysisDisplayStyle() method can create either a colored surface display style, a markers with text style, a deformed shape style, diagram style or vector style. For any style, the color and legend settings can also be set.

---
The AnalysisDisplayStyle class can be used to control how the analysis results are displayed in the view. The static CreateAnalysisDisplayStyle() method can create either a colored surface display style, a markers with text style, a deformed shape style, diagram style or vector style. For any style, the color and legend settings can also be set.

Once a new AnalysisDisplayStyle is created, use the View.AnalysisDisplayStyleId to assign the style to a view. Although the analysis results are not saved with the document, analysis display styles and their assignment to a view are saved with the model.

The following example creates a new colored surface analysis display style (if not already found in the document) and then assigns it to the current view.

<table summary="" id="GUID-A164161C-2C12-4A31-901C-1E7FEB576137__TABLE_B46BCA2224AE4666B09E2760048FC6E5"><tbody><tr><td><b>Code Region 27-2: Setting analysis display style for view</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SetDisplayStyle</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>        
        </span><span>AnalysisDisplayStyle</span><span> analysisDisplayStyle </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>// Look for an existing analysis display style with a specific name</span><span>
        </span><span>FilteredElementCollector</span><span> collector1 </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span>  
                collector1</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>AnalysisDisplayStyle</span><span>)).</span><span>ToElements</span><span>();</span><span>
        </span><span>var</span><span> displayStyle </span><span>=</span><span> </span><span>from</span><span> element </span><span>in</span><span> collection 
                </span><span>where</span><span> element</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Display Style 1"</span><span> 
                </span><span>select</span><span> element</span><span>;</span><span>

                                                </span><span>// If display style does not already exist in the document, create it</span><span>
        </span><span>if</span><span> </span><span>(</span><span>displayStyle</span><span>.</span><span>Count</span><span>()</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>AnalysisDisplayColoredSurfaceSettings</span><span> coloredSurfaceSettings </span><span>=</span><span> </span><span>new</span><span> </span><span>AnalysisDisplayColoredSurfaceSettings</span><span>();</span><span>
                coloredSurfaceSettings</span><span>.</span><span>ShowGridLines</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>

                </span><span>AnalysisDisplayColorSettings</span><span> colorSettings </span><span>=</span><span> </span><span>new</span><span> </span><span>AnalysisDisplayColorSettings</span><span>();</span><span>
                </span><span>Color</span><span> orange </span><span>=</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>255</span><span>,</span><span> </span><span>205</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                </span><span>Color</span><span> purple </span><span>=</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>200</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>200</span><span>);</span><span>
                colorSettings</span><span>.</span><span>MaxColor</span><span> </span><span>=</span><span> orange</span><span>;</span><span>
                colorSettings</span><span>.</span><span>MinColor</span><span> </span><span>=</span><span> purple</span><span>;</span><span>

                </span><span>AnalysisDisplayLegendSettings</span><span> legendSettings </span><span>=</span><span> </span><span>new</span><span> </span><span>AnalysisDisplayLegendSettings</span><span>();</span><span>
                legendSettings</span><span>.</span><span>NumberOfSteps</span><span> </span><span>=</span><span> </span><span>10</span><span>;</span><span>
                legendSettings</span><span>.</span><span>Rounding</span><span> </span><span>=</span><span> </span><span>0.05</span><span>;</span><span>
                legendSettings</span><span>.</span><span>ShowDataDescription</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
                legendSettings</span><span>.</span><span>ShowLegend</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>

                </span><span>FilteredElementCollector</span><span> collector2 </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
                </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> elementCollection </span><span>=</span><span> collector2</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>TextNoteType</span><span>)).</span><span>ToElements</span><span>();</span><span>
                </span><span>var</span><span> textElements </span><span>=</span><span> </span><span>from</span><span> element </span><span>in</span><span> collector2 
                                                        </span><span>where</span><span> element</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"LegendText"</span><span> 
                                                        </span><span>select</span><span> element</span><span>;</span><span>
                </span><span>// if LegendText exists, use it for this Display Style</span><span>
                </span><span>if</span><span> </span><span>(</span><span>textElements</span><span>.</span><span>Count</span><span>()</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span> 
                </span><span>{</span><span>
                        </span><span>TextNoteType</span><span> textType </span><span>=</span><span> 
                                textElements</span><span>.</span><span>Cast</span><span>&lt;</span><span>TextNoteType</span><span>&gt;().</span><span>ElementAt</span><span>&lt;</span><span>TextNoteType</span><span>&gt;(</span><span>0</span><span>);</span><span>
                        legendSettings</span><span>.</span><span>TextTypeId</span><span> </span><span>=</span><span> textType</span><span>.</span><span>Id</span><span>;</span><span>
                </span><span>}</span><span>
                analysisDisplayStyle </span><span>=</span><span> </span><span>AnalysisDisplayStyle</span><span>.</span><span>CreateAnalysisDisplayStyle</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Display Style 1"</span><span>,</span><span> coloredSurfaceSettings</span><span>,</span><span> colorSettings</span><span>,</span><span> legendSettings</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
                analysisDisplayStyle </span><span>=</span><span> 
                        displayStyle</span><span>.</span><span>Cast</span><span>&lt;</span><span>AnalysisDisplayStyle</span><span>&gt;().</span><span>ElementAt</span><span>&lt;</span><span>AnalysisDisplayStyle</span><span>&gt;(</span><span>0</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>// now assign the display style to the view</span><span>
        doc</span><span>.</span><span>ActiveView</span><span>.</span><span>AnalysisDisplayStyleId</span><span> </span><span>=</span><span> analysisDisplayStyle</span><span>.</span><span>Id</span><span>;</span><span>
        </span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Analysis Results Display  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Updating Analysis Results  Autodesk.md ===== -->

---
created: 2026-01-28T21:15:37 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Analysis_Visualization_Updating_Analysis_Results_html
author: 
---

# Help | Updating Analysis Results | Autodesk

> ## Excerpt
> The Revit analysis framework does not update results automatically, and potentially any change to Revit model can invalidate results.

---
The Revit analysis framework does not update results automatically, and potentially any change to Revit model can invalidate results.

In order to keep results up to date, API developers should use [Dynamic Model Update](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_html) triggers or subscribe to the [DocumentChanged event](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Database_Events_DocumentChanged_event_html) to be notified when the Revit model has changed and previously calculated results may be invalid and in need of recalculation. For an example showing Dynamic Model Update together with Analysis Visualization, see the DistanceToSurfaces sample in the Revit SDK.


<!-- ===== END: Help  Updating Analysis Results  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Detailed Energy Analysis Model  Autodesk.md ===== -->

---
created: 2026-01-28T21:15:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Detailed_Energy_Analysis_Model_html
author: 
---

# Help | Detailed Energy Analysis Model | Autodesk

> ## Excerpt
> The Autodesk.Revit.DB.Analysis namespace includes several classes to obtain and analyze the contents of a project's detailed energy analysis model.

---
The Autodesk.Revit.DB.Analysis namespace includes several classes to obtain and analyze the contents of a project's detailed energy analysis model.

The Export to gbXML and the Heating and Cooling Loads features produce an analytical thermal model from the physical model of a building. The analytical thermal model is composed of spaces, zones and planar surfaces that represent the actual volumetric elements of the building.

The classes related to the detailed energy analysis model are:

-   EnergyAnalysisDetailModel
-   EnergyAnalysisDetailModelOptions
-   EnergyAnalysisOpening
-   EnergyAnalysisSpace
-   EnergyAnalysisSurface
-   Polyloop
    
    ### Energy analysis model creation
    

Use the static method EnergyAnalysisDetailModel.Create() to create and populate the energy analysis model. The EnergyAnaysisDetailModel is stored as an element in the Revit model, and thus the EnergyAnalysisDetailModel.Create() method requires there to be an open transaction. The generated model is always returned in world coordinates, but the method TransformModel() transforms all surfaces in the model according to ground plane, shared coordinates and true north.

If an energy analysis model is already created, the static method EnergyAnalysisDetailModel.GetMainEnergyAnalysisDetailModel() returns the main EnergyAnalysisDetailModel contained in the given document (or null if none has been created). The energy analysis detail model can be displayed in associated views.

Set the appropriate options using the EnergyAnalysisDetailModelOptions class.

The options available when creating the energy analysis detail model include:

-   The level of computation for energy analysis model - NotComputed, FirstLevelBoundaries, meaning analytical spaces and zones, SecondLevelBoundaries, meaning analytical surfaces, or Final, meaning constructions, schedules, and non-graphical data
-   Whether the energy model is based on rooms/spaces or building elements
-   Whether mullions should be exported as shading surfaces
-   Whether shading surfaces will be included
-   Whether to simplify curtain systems - When true, a single large window/opening will be exported for a curtain wall/system regardless of the number of panels in the system

The EnergyAnalysisDetailModelOptions.EnergyModelType property can be set to SpatialElement (where the energy model is based on rooms or spaces) or BuildingElement (where the energy model is based on analysis of building element volumes). However, note that the generated energy model is also affected by settings in EnergyDataSettings, including the EnergyDataSettings.AnalysisType property. If this property is set to AnalysisMode.ConceptualMassesAndBuildingElements, the EnergyAnalysisDetailModel will use the combination of conceptual masses and building elements.

The following example creates a new energy analysis detailed model from the physical model then displays the originating element for each surface of each space in the model.

<table summary="" id="GUID-471B3969-42E7-436C-8DD3-C5ED18DD9209__TABLE_1A78873357B14703BD52913F64102E94"><tbody><tr><td><b>Code Region: Energy Analysis Detail Model</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetThermalModelData</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Collect space and surface data from the building's analytical thermal model</span><span>
    </span><span>EnergyAnalysisDetailModelOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>EnergyAnalysisDetailModelOptions</span><span>();</span><span>
    options</span><span>.</span><span>Tier</span><span> </span><span>=</span><span> </span><span>EnergyAnalysisDetailModelTier</span><span>.</span><span>Final</span><span>;</span><span> </span><span>// include constructions, schedules, and non-graphical data in the computation of the energy analysis model</span><span>
    options</span><span>.</span><span>EnergyModelType</span><span> </span><span>=</span><span> </span><span>EnergyModelType</span><span>.</span><span>SpatialElement</span><span>;</span><span>   </span><span>// Energy model based on rooms or spaces</span><span>

    </span><span>EnergyAnalysisDetailModel</span><span> eadm </span><span>=</span><span> </span><span>EnergyAnalysisDetailModel</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> options</span><span>);</span><span> </span><span>// Create a new energy analysis detailed model from the physical model</span><span>
    </span><span>IList</span><span>&lt;</span><span>EnergyAnalysisSpace</span><span>&gt;</span><span> spaces </span><span>=</span><span> eadm</span><span>.</span><span>GetAnalyticalSpaces</span><span>();</span><span>
    </span><span>StringBuilder</span><span> builder </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>();</span><span>
    builder</span><span>.</span><span>AppendLine</span><span>(</span><span>"Spaces: "</span><span> </span><span>+</span><span> spaces</span><span>.</span><span>Count</span><span>);</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>EnergyAnalysisSpace</span><span> space </span><span>in</span><span> spaces</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>SpatialElement</span><span> spatialElement </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>space</span><span>.</span><span>CADObjectUniqueId</span><span>)</span><span> </span><span>as</span><span> </span><span>SpatialElement</span><span>;</span><span>
        </span><span>ElementId</span><span> spatialElementId </span><span>=</span><span> spatialElement </span><span>==</span><span> </span><span>null</span><span> </span><span>?</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span> </span><span>:</span><span> spatialElement</span><span>.</span><span>Id</span><span>;</span><span>
        builder</span><span>.</span><span>AppendLine</span><span>(</span><span>"   &gt;&gt;&gt; "</span><span> </span><span>+</span><span> space</span><span>.</span><span>SpaceName</span><span> </span><span>+</span><span> </span><span>" related to "</span><span> </span><span>+</span><span> spatialElementId</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>EnergyAnalysisSurface</span><span>&gt;</span><span> surfaces </span><span>=</span><span> space</span><span>.</span><span>GetAnalyticalSurfaces</span><span>();</span><span>
        builder</span><span>.</span><span>AppendLine</span><span>(</span><span>"       has "</span><span> </span><span>+</span><span> surfaces</span><span>.</span><span>Count</span><span> </span><span>+</span><span> </span><span>" surfaces."</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>EnergyAnalysisSurface</span><span> surface </span><span>in</span><span> surfaces</span><span>)</span><span>
        </span><span>{</span><span>
            builder</span><span>.</span><span>AppendLine</span><span>(</span><span>"            +++ Surface from "</span><span> </span><span>+</span><span> surface</span><span>.</span><span>OriginatingElementDescription</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"EAM"</span><span>,</span><span> builder</span><span>.</span><span>ToString</span><span>());</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

After creating the EnergyAnalysisDetailModel, the spaces, openings and surfaces associated with it can be retrieved with the GetAnalyticalOpenings(), GetAnalyticalSpaces(), GetAnalyticalShadingSurfaces() and GetAnalyticalSurfaces() methods.

It is recommended that applications call Document.Delete() on the EnergyAnalysisDetailModel elements that they create when finished accessing the data, but any energy models created after the main energy model will be deleted automatically before document saving or synchronization.

### EnergyAnalysisSpace

From an EnergyAnalysisSpace you can retrieve the collection of EnergyAnalysisSurfaces which define an enclosed volume bounded by the center plane of walls and the top plane of roofs and floors. Alternatively, GetClosedShell() retrieves a collection of Polyloops, which are planar polygons, that define an enclosed volume measured by interior bounding surfaces. For two-dimensions, use GetBoundary() which returns a collection of Polyloops representing the 2D boundary of the space that defines an enclosed area measured by interior bounding surfaces.

The EnergyAnalysisSpace class also has a number of properties for accessing information about the analysis space, such as AnalyticalVolume, SpaceName and Area.

### EnergyAnalysisSurface

From an EnergyAnalysisSpace you can retrieve the primary analysis space associated with the surface as well as the secondary adjacent analytical space. The GetAnalyticalOpenings() method will retrieve a collection of all analytical openings in the surface. The GetPolyloop() method obtains the planar polygon describing the surface geometry as described in gbXML.

The EnergyAnalysisSurface class has numerous properties to provide more information about the analytical surface, such as Height, Width, Corner (lower-left coordinate for the analytical rectangular geometry viewed from outside), and an originating element description.

The surface type is available either as an EnergyAnalysisSurfaceType or as a gbXMLSurfaceType. The gbXML surface type attribute is determined by the source element and the number of space adjacencies. Possible types are:

<table summary="" id="GUID-471B3969-42E7-436C-8DD3-C5ED18DD9209__TABLE_2C53060F15BF4F5394A1D2BBACD0BC71"><tbody><tr><td><b>Type</b></td><td><b>Source element and space adjacencies</b></td></tr><tr><td>_Shade_</td><td>No associated source element and no space adjacencies</td></tr><tr><td>_Air_</td><td>No associated source element and at least one space adjacency</td></tr><tr><td>_ExteriorWall_</td><td>Source element is a Wall or a Curtain Wall there is one space adjacency</td></tr><tr><td>_InteriorWall_</td><td>Source element is a Wall or a Curtain Wall and: there are two space adjacencies or the type Function parameter is set to "Interior" or "CoreShaft"</td></tr><tr><td>_UndergroundWall_</td><td>Source element is a Wall or a Curtain Wall and there is one space adjacency and if it is below grade</td></tr><tr><td>_SlabOnGrade_</td><td>Source element is a Floor and there is one space adjacency</td></tr><tr><td>_RaisedFloor_</td><td>Source element is a Floor and there is one space adjacency and it is above grade</td></tr><tr><td>_UndergroundSlab_</td><td>Source element is a Floor and there is one space adjacency and it is below grade</td></tr><tr><td>_InteriorFloor_</td><td>Source element is a Floor and: there are two space adjacencies or the type Function parameter is set to "Interior</td></tr><tr><td>_Roof_</td><td>Source element is a Roof or a Ceiling and there is one space adjacency</td></tr><tr><td>_UndergroundCeiling_</td><td>Source element is a Roof or a Ceiling and there is one space adjacency and it is below grade</td></tr><tr><td>_Ceiling_</td><td>Source element is a Roof or a Ceiling and there are two space adjacencies</td></tr></tbody></table>

### EnergyAnalysisOpening

From an EnergyAnalysisOpening you can retrieve the associated parent analytical surface element. The GetPolyloop() method returns the opening geometry as a planar polygon.

A number of properties are available to obtain information about the analytical opening, such as Height, Width, Corner and OpeningName. Similar as for analytical surfaces, the analytical opening type can be obtained as a simple EnergyAnalysisOpeningType enumeration or as a gbXMLOpeningType attribute. The type of the opening is based on the family category for the opening and in what element it is contained, as shown in the following table:

<table summary="" id="GUID-471B3969-42E7-436C-8DD3-C5ED18DD9209__TABLE_BE73E7D705664FEB8F56C30CE131CB3E"><tbody><tr><td><b>Type</b></td><td><b>Family Category or containing element</b></td></tr><tr><td><i>OperableWindow</i></td><td>Window</td></tr><tr><td><i>NonSlidingDoor</i></td><td>Door</td></tr><tr><td><i>FixedSkylight</i></td><td>Opening contained in a Roof</td></tr><tr><td><i>FixedWindow</i></td><td>Opening contained in a Curtain Wall Panel</td></tr><tr><td><i>Air</i></td><td>Opening of the category Openings</td></tr></tbody></table>


<!-- ===== END: Help  Detailed Energy Analysis Model  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Path Of Travel  Autodesk.md ===== -->

---
created: 2026-01-28T21:15:47 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Path_Of_Travel_html
author: 
---

# Help | Path Of Travel | Autodesk

> ## Excerpt
> The path of travel element allows you to analyze travel distances and times between 2 selected points in your model. The path of travel is generated based on the model elements acting as obstacles along the path of travel. It avoids contact with model elements in the analysis zone and calculates the shortest distance between the start and end points.

---
The path of travel element allows you to analyze travel distances and times between 2 selected points in your model. The path of travel is generated based on the model elements acting as obstacles along the path of travel. It avoids contact with model elements in the analysis zone and calculates the shortest distance between the start and end points. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/PathOfTravel.png)

The class `Autodesk.Revit.DB.Analysis.PathOfTravel` represents this path element.

Members of this class include:

-   PathOfTravel.Create() - creates a single PathOfTravel element given a start and end point.
-   PathOfTravel.CreateMultiple() - creates multiple PathOfTravel elements given arrays of start and end points.
-   PathOfTravel.CreateMapped() - creates multiple PathOfTravel elements by mapping each of a set of start points to each of a set of end points.
-   PathOfTravel.GetCurves()
-   PathOfTravel.LineStyle
-   PathOfTravel.PathStart
-   PathOfTravel.PathMidpoint
-   PathOfTravel.PathEnd
-   PathOfTravel.Update()
-   PathOfTravel.UpdateMultiple()

The class `Autodesk.Revit.DB.Analysis.RouteAnalysisSettings` represents a settings element which contains project-wide settings for route calculations in plan views. Currently, these settings are only used by the Autodesk.Revit.DB.Analysis.PathOfTravel element, but in the future they can be used by any other functionalities which do route calculations.

Members of this class include:

-   RouteAnalysisSettings.EnableIgnoredCategoryIds() - enable ignoring specified categories of elements during calculations
-   RouteAnalysisSettings.SetIgnoredCategoryIds() - sets the categories to be ignored during calculations
-   RouteAnalysisSettings.AnalysisZoneTopOffset - the analysis zone top (an offset above the level of the plan view)
-   RouteAnalysisSettings.AnalysisZoneBottomOffset - the analysis zone bottom (an offset above the level of the plan view)
-   RouteAnalysisSettings.IgnoreImports - If true, import instances are ignored by route calculation

## Reveal Obstacles mode for Path of Travel

The Reveal Obstacles view mode highlights elements in the plan view when those elements will act as obstacles for the current Path of Travel calculation settings. These methods provide access to read or set if a view is displaying this mode:

-   PathOfTravel.IsInRevealObstaclesMode()
-   PathOfTravel.SetRevealObstaclesMode()

## Path finding analysis for Path of Travel

`List<XYZ> PathOfTravel.FindStartsOfLongestPathsFromRooms(View view, List<XYZ> destinationPoints)` For a floor plan view, calculates paths from points inside rooms to the closests of the destinations. Returns the start points of the longest path(s). If multiple paths have the same longest length, returns multiple start points. The entire plan is divided in small tiles, and the distance to the closest destination point is calculated for each tile center point. Only tile center points that are located in rooms in the view are taken into account.

`List<XYZ> PathOfTravel.FindEndsOfShortestPaths(View view, List<XYZ> destinationPoints, List<XYZ> startPoints)` For a floor plan view, calculates the paths from each start point to its closest destination and return the path end points. The calculation is done in a floor plan with one or more destinationPoints and one or more startPoints. The shortest path is calculated from each start point to its corresponding closest destination.

`List<List<XYZ>> PathOfTravel.FindShortestPaths(View view, List<XYZ> destinationPoints, List<XYZ> startPoints)` For a floor plan view, calculates paths from each start point to its closest destinations. Returns the path, represented by an array of XYZ points. The calculation is done in a floor plan with one or more destinationPoints and one or more startPoints. The shortest path is calculated from each start point to its closest destination point.

## Waypoints

These methods provide access to read and modify the waypoints associated to a particular PathOfTravel element. Waypoints force the path of travel calculation to ensure that the path includes each of the specified points, in the order specified, between the start and end points.

-   PathOfTravel.GetWaypoints()
-   PathOfTravel.InsertWaypoint()
-   PathOfTravel.SetWaypoint()
-   PathOfTravel.RemoveWaypoint()


<!-- ===== END: Help  Path Of Travel  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Browser Organization  Autodesk.md ===== -->

---
created: 2026-01-28T21:15:51 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_BrowserOrganization_html
author: 
---

# Help | Browser Organization | Autodesk

> ## Excerpt
> The BrowserOrganization class provides read-access to the settings for grouping, sorting, and filtering of items in the project browser.

---
The BrowserOrganization class provides read-access to the settings for grouping, sorting, and filtering of items in the project browser.

BrowserOrganization.AreFiltersSatisfied() determines if the given element satisfies the filters defined by the browser organization.

## Getting the current organization

-   GetCurrentBrowserOrganizationForViews() gets the BrowserOrganization that applies to the Views section of the project browser.
-   GetCurrentBrowserOrganizationForSheets() gets the BrowserOrganization that applies to the Sheets section of the project browser.
-   BrowserOrganization.GetCurrentBrowserOrganizationForSchedules() gets the BrowserOrganization that applies to the Schedules section of the project browser

## Sorting

-   SortingOrder – The sorting order if sorting of items is applicable in the browser.
-   SortingParameterId – The id of the parameter used to determine the sorting order of items in the browser.

## FolderItemInfo

BrowserOrganization.GetFolderItems(ElementId) returns a collection of leaf FolderItemInfo objects each containing the given element Id.

FolderItemInfo contains the ElementId and Name info for each item in the organization settings of the project browser.


<!-- ===== END: Help  Browser Organization  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Commands  Autodesk.md ===== -->

---
created: 2026-01-28T21:15:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Commands_html
author: 
---

# Help | Commands | Autodesk

> ## Excerpt
> The Revit API provides access to existing Revit commands, either located on a tab, the application menu, or right-click menu. The main ways to work with Revit commands using the API is to either replace the existing command implementation or to post a command.

---
The Revit API provides access to existing Revit commands, either located on a tab, the application menu, or right-click menu. The main ways to work with Revit commands using the API is to either replace the existing command implementation or to post a command.

### Overriding a Revit command

The AddInCommandBinding class can be used to override an existing command in Revit. It has three events related to replacing the existing command implementation.

-   **BeforeExecuted**\- This read-only event occurs before the associated command executes. An application can react to this event but cannot make changes to documents, or affect the invocation of the command.
-   **CanExecute** - Occurs when the associated command initiates a check to determine whether the command can be executed on the command target.
-   **Executed** - This event occurs when the associated command executes and is where any overriding implementation should be performed.

To create the commandbinding, call either UIApplication.CreateAddInCommandBinding() or UIControlledApplication.CreateAddInCommandBinding(). Both methods require a RevitCommandId id to identify the command handler you want to replace. The RevitCommandId has two static methods for obtaining a command's id:

-   **LookupCommandId** - Retrieves the Revit command id with the given id string. To find the command id string, open a session of Revit, invoke the desired command, close Revit, then look in the journal from that session. The "Jrn.Command" entry that was recorded when it was selected will have the string needed for LookupCommandId() and will look something like "ID\_EDIT\_DESIGNOPTIONS".
-   **LookupPostableCommandId** - Retrieves the Revit command id using the PostableCommand enumeration. This only works for commands which are postable (discussed in the following section).

The following example, taken from Revit 2014 SDK's DisableCommand sample, demonstrates how to create an AddInCommandBinding and override the implementation to disable the command with a message to the user.

<table summary="" id="GUID-1C7289DE-8D10-47B5-B6DB-EA1310851C8F__TABLE_0A7CD204C02844D988173E09F5D9A3D7"><tbody><tr><td><b>Code Region: Overriding a command</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Implements the Revit add-in interface IExternalApplication</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>MyApplication</span><span> </span><span>:</span><span> </span><span>IExternalApplication</span><span>
</span><span>{</span><span>
    </span><span>#region IExternalApplication Members</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Implements the OnStartup event</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="application"&gt;&lt;/param&gt;</span><span>
    </span><span>/// &lt;returns&gt;&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Lookup the desired command by name</span><span>
        s_commandId </span><span>=</span><span> </span><span>RevitCommandId</span><span>.</span><span>LookupCommandId</span><span>(</span><span>s_commandToDisable</span><span>);</span><span>

        </span><span>// Confirm that the command can be overridden</span><span>
        </span><span>if</span><span> </span><span>(!</span><span>s_commandId</span><span>.</span><span>CanHaveBinding</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ShowDialog</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"The target command "</span><span> </span><span>+</span><span> s_commandToDisable </span><span>+</span><span>
                        </span><span>" selected for disabling cannot be overridden"</span><span>);</span><span>
   </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>// Create a binding to override the command.</span><span>
        </span><span>// Note that you could also implement .CanExecute to override the accessibiliy of the command.</span><span>
        </span><span>// Doing so would allow the command to be grayed out permanently or selectively, however,</span><span>
        </span><span>// no feedback would be available to the user about why the command is grayed out.</span><span>
        </span><span>try</span><span>
        </span><span>{</span><span>
            </span><span>AddInCommandBinding</span><span> commandBinding </span><span>=</span><span> application</span><span>.</span><span>CreateAddInCommandBinding</span><span>(</span><span>s_commandId</span><span>);</span><span>
            commandBinding</span><span>.</span><span>Executed</span><span> </span><span>+=</span><span> </span><span>DisableEvent</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>// Most likely, this is because someone else has bound this command already.</span><span>
        </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ShowDialog</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"This add-in is unable to disable the target command "</span><span> </span><span>+</span><span> s_commandToDisable </span><span>+</span><span>
                        </span><span>"; most likely another add-in has overridden this command."</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Implements the OnShutdown event</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="application"&gt;&lt;/param&gt;</span><span>
    </span><span>/// &lt;returns&gt;&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Remove the command binding on shutdown</span><span>
        </span><span>if</span><span> </span><span>(</span><span>s_commandId</span><span>.</span><span>HasBinding</span><span>)</span><span>
            application</span><span>.</span><span>RemoveAddInCommandBinding</span><span>(</span><span>s_commandId</span><span>);</span><span>
        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>#endregion</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// A command execution method which disables any command it is applied to (with a user-visible message).</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="sender"&gt;Event sender.&lt;/param&gt;</span><span>
    </span><span>/// &lt;param name="args"&gt;Arguments.&lt;/param&gt;</span><span>
    </span><span>private</span><span> </span><span>void</span><span> </span><span>DisableEvent</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>ExecutedEventArgs</span><span> args</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>ShowDialog</span><span>(</span><span>"Disabled"</span><span>,</span><span> </span><span>"Use of this command has been disabled."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Show a task dialog with a message and title.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="title"&gt;The title.&lt;/param&gt;</span><span>
    </span><span>/// &lt;param name="message"&gt;The message.&lt;/param&gt;</span><span>
    </span><span>private</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>ShowDialog</span><span>(</span><span>string</span><span> title</span><span>,</span><span> </span><span>string</span><span> message</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Show the user a message.</span><span>
        </span><span>TaskDialog</span><span> td </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>title</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>MainInstruction</span><span> </span><span>=</span><span> message</span><span>,</span><span>
            </span><span>TitleAutoPrefix</span><span> </span><span>=</span><span> </span><span>false</span><span>
        </span><span>};</span><span>
        td</span><span>.</span><span>Show</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// The string name of the command to disable.  To lookup a command id string, open a session of Revit,</span><span>
    </span><span>/// invoke the desired command, close Revit, then look to the journal from that session.  The command</span><span>
    </span><span>/// id string will be toward the end of the journal, look for the "Jrn.Command" entry that was recorded</span><span>
    </span><span>/// when it was selected.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>static</span><span> </span><span>String</span><span> s_commandToDisable </span><span>=</span><span> </span><span>"ID_EDIT_DESIGNOPTIONS"</span><span>;</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// The command id, stored statically to allow for removal of the command binding.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>static</span><span> </span><span>RevitCommandId</span><span> s_commandId</span><span>;</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>

### Posting a command

The method UIApplication.PostCommand() will post a command to the Revit message queue to be invoked when control returns from the current API application. Only certain commands can be posted this way. They include all of the commands in the Autodesk.Revit.UI.PostableCommand enumerated type as well as external commands created by any add-in.

Note: Even a postable command may not execute when using PostCommand(). One reason this may happen is if another command has already been posted. Only one command may be posted to Revit at a given time, so if a second command is posted, PostCommand() will throw an exception. Another reason a posted command may not execute is if the command to be executed is not accessible at the time. Whether it is accessible is determined only at the point where Revit returns from the API context, so a failure to execute for this reason will not be reported directly back to the application that posted the command. UIApplication. CanPostCommand() can be used to identify if the given command can be posted, meaning whether it is a member of PostableCommand or an external command. It does not identify if the command is currently accessible.

Both PostCommand() and CanPostCommand() require a RevitCommandId which can be obtained as described in the "Overriding a Revit command" section above.


<!-- ===== END: Help  Commands  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Construction Modeling  Autodesk.md ===== -->

---
created: 2026-01-28T21:16:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Construction_Modeling_html
author: 
---

# Help | Construction Modeling | Autodesk

> ## Excerpt
> The Revit API allows elements to be divided into sub-parts or collected into assemblies to support construction modeling workflows, much the same way as can be done with the Revit user interface. Both parts and assemblies can be independently scheduled, tagged, filtered, and exported. You can also divide a part into smaller parts. After creating an assembly type, you can place additional instances in the project and generate isolated assembly views.

---
The Revit API allows elements to be divided into sub-parts or collected into assemblies to support construction modeling workflows, much the same way as can be done with the Revit user interface. Both parts and assemblies can be independently scheduled, tagged, filtered, and exported. You can also divide a part into smaller parts. After creating an assembly type, you can place additional instances in the project and generate isolated assembly views.

The main classes related to Construction Modeling are:

-   **AssemblyInstance** - This class combines multiple elements for tagging, filtering, scheduling and creating isolated assembly views.
-   **AssemblyType** - Represents a type for construction assembly elements. Each new unique assembly created in the project automatically creats a corresponding AssemblyType. A new AssemblyInstance can be placed in the document from an existing AssemblyType.
-   **PartUtils** - This utility class contains general part utility methods, including the ability to create parts, divide parts, and to get information about parts.
-   **AssemblyViewUtils** - A utility class to create various types of assembly views.


<!-- ===== END: Help  Construction Modeling  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Assemblies and Views  Autodesk.md ===== -->

---
created: 2026-01-28T21:16:06 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Construction_Modeling_Assemblies_and_Views_html
author: 
---

# Help | Assemblies and Views | Autodesk

> ## Excerpt
> You can combine any number of model elements to create an assembly, which can then be edited, tagged, scheduled, and filtered.

---
You can combine any number of model elements to create an assembly, which can then be edited, tagged, scheduled, and filtered.

## Creating assemblies

The static Create() method of the AssemblyInstance class is used to create a new assembly instance in the project. The Create() method must be created inside a transaction and the transaction must be committed before performing any action on the newly created assembly instance. The assembly type is assigned after the transaction is complete. Each unique assembly has its own AssemblyType.

The following example creates a new assembly instance, changes the name of its AssemblyType and then creates some views for the assembly instance.

<table summary="" id="GUID-12C5A454-680F-4CA1-8AA9-D34E54C7F75D__TABLE_4E486EC837A64C28B41C63B2B6EA2F42"><tbody><tr><td><b>Code Region: Create Assembly and Views</b></td></tr><tr><td><pre><code><span>AssemblyInstance</span><span> </span><span>CreateAssemblyAndViews</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> elementIds</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>AssemblyInstance</span><span> assemblyInstance </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>ElementId</span><span> categoryId </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>elementIds</span><span>.</span><span>First</span><span>()).</span><span>Category</span><span>.</span><span>Id</span><span>;</span><span> </span><span>// use category of one of the assembly elements</span><span>
        </span><span>if</span><span> </span><span>(</span><span>AssemblyInstance</span><span>.</span><span>IsValidNamingCategory</span><span>(</span><span>doc</span><span>,</span><span> categoryId</span><span>,</span><span> elementIds</span><span>))</span><span>
        </span><span>{</span><span>
            transaction</span><span>.</span><span>Start</span><span>(</span><span>"Create Assembly Instance"</span><span>);</span><span>
            assemblyInstance </span><span>=</span><span> </span><span>AssemblyInstance</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> elementIds</span><span>,</span><span> categoryId</span><span>);</span><span>
            transaction</span><span>.</span><span>Commit</span><span>();</span><span> </span><span>// commit the transaction that creates the assembly instance before modifying the instance's name</span><span>

            </span><span>if</span><span> </span><span>(</span><span>transaction</span><span>.</span><span>GetStatus</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Committed</span><span>)</span><span>
            </span><span>{</span><span>
                transaction</span><span>.</span><span>Start</span><span>(</span><span>"Set Assembly Name"</span><span>);</span><span>
                assemblyInstance</span><span>.</span><span>AssemblyTypeName</span><span> </span><span>=</span><span> </span><span>"My Assembly Name"</span><span>;</span><span>
                transaction</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>

            </span><span>if</span><span> </span><span>(</span><span>assemblyInstance</span><span>.</span><span>AllowsAssemblyViewCreation</span><span>())</span><span> </span><span>// create assembly views for this assembly instance</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>transaction</span><span>.</span><span>GetStatus</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Committed</span><span>)</span><span>
                </span><span>{</span><span>
                    transaction</span><span>.</span><span>Start</span><span>(</span><span>"View Creation"</span><span>);</span><span>
                    </span><span>View3D</span><span> view3d </span><span>=</span><span> </span><span>AssemblyViewUtils</span><span>.</span><span>Create3DOrthographic</span><span>(</span><span>doc</span><span>,</span><span> assemblyInstance</span><span>.</span><span>Id</span><span>);</span><span>
                    </span><span>ViewSchedule</span><span> partList </span><span>=</span><span> </span><span>AssemblyViewUtils</span><span>.</span><span>CreatePartList</span><span>(</span><span>doc</span><span>,</span><span> assemblyInstance</span><span>.</span><span>Id</span><span>);</span><span>
                    transaction</span><span>.</span><span>Commit</span><span>();</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> assemblyInstance</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Another way to create an AssemblyInstance is to use an existing AssemblyType. To create an AssemblyInstance using an AssemblyType, use the static method AssemblyInstance.PlaceInstance() and specify the ElementId of the AssemblyType to use and a location at which to place the assembly.

## Assembly Views

Various assembly views can be created for an assembly instance using static methods of the AssemblyViewUtils class, including an orthographic 3D assembly view, a detail section assembly view, a material takeoff multicategory schedule assembly view, a part list multicategory schedule assembly view, a single-category schedule and a sheet assembly view. All of these except sheet views have overloaded creation methods which create the schedule or view from a template. In addition to a template Id, these overloads have a parameter to indicate if the template will be assigned or applied.

Note that assembly views must all be assigned to the same assembly instance of the assembly type. AssemblyInstance.AllowsAssemblyViewCreation() returns true if that assembly instance can accept new assembly views (either because it already has views or because no assembly instance has views).

The following example creates a new single-category schedule for an assembly from a given template.

<table summary="" id="GUID-12C5A454-680F-4CA1-8AA9-D34E54C7F75D__TABLE_2FAEE6CE71C745219673394C9ECC42B9"><tbody><tr><td><b>Code Region: Create assembly view from template</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>ViewSchedule</span><span> </span><span>CreateScheduleForAssembly</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>AssemblyInstance</span><span> assemblyInstance</span><span>,</span><span> </span><span>ElementId</span><span> viewTemplateId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ViewSchedule</span><span> schedule </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>assemblyInstance</span><span>.</span><span>AllowsAssemblyViewCreation</span><span>())</span><span> </span><span>// create assembly views for this assembly instance</span><span>
    </span><span>{</span><span>
        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>))</span><span>
        </span><span>{</span><span>
            transaction</span><span>.</span><span>Start</span><span>(</span><span>"Create Schedule"</span><span>);</span><span>

            </span><span>// use naming category for the schedule</span><span>
            </span><span>if</span><span> </span><span>(</span><span>ViewSchedule</span><span>.</span><span>IsValidCategoryForSchedule</span><span>(</span><span>assemblyInstance</span><span>.</span><span>NamingCategoryId</span><span>))</span><span>
            </span><span>{</span><span>
                schedule </span><span>=</span><span> </span><span>AssemblyViewUtils</span><span>.</span><span>CreateSingleCategorySchedule</span><span>(</span><span>doc</span><span>,</span><span> assemblyInstance</span><span>.</span><span>Id</span><span>,</span><span> assemblyInstance</span><span>.</span><span>NamingCategoryId</span><span>,</span><span> viewTemplateId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
            </span><span>}</span><span>
            transaction</span><span>.</span><span>Commit</span><span>();</span><span>

            </span><span>if</span><span> </span><span>(</span><span>schedule </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> transaction</span><span>.</span><span>GetStatus</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Committed</span><span>)</span><span>
            </span><span>{</span><span>
                transaction</span><span>.</span><span>Start</span><span>(</span><span>"Edit Schedule"</span><span>);</span><span>
                schedule</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"AssemblyViewSchedule"</span><span>;</span><span>
                transaction</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> schedule</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The document must be regenerated before using any of these newly created assembly views. You'll note in the example above that a transaction is committed after creating a new assembly view. The Commit() method automatically regenerates the document.


<!-- ===== END: Help  Assemblies and Views  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Parts  Autodesk.md ===== -->

---
created: 2026-01-28T21:16:40 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Construction_Modeling_Parts_html
author: 
---

# Help | Parts | Autodesk

> ## Excerpt
> Parts can be generated from elements with layered structures, such as:

---
Parts can be generated from elements with layered structures, such as:

-   Walls (excluding stacked walls and curtain walls)
-   Floors (excluding shape-edited floors)
-   Roofs (excluding those with ridge lines)
-   Ceilings
-   Structural slab foundations

In the Revit API, elements can be divided into parts using the PartUtils class. The static method PartUtils.CreateParts() is used to create parts from one or more elements. Note that this method instantiates a PartMaker and creates Parts that will be split in smaller parts if you chose to use DivideParts. The PartMaker uses its embedded rules to drive creation of the needed parts during regeneration.

The API also offers an interface to subdivide parts. PartUtils.DivideParts() accepts as input a collection of part ids, a collection of “intersecting element” ids (which can be layers and grids), and a collection of curves. The routine uses the intersecting elements and curves as boundaries from which to divide and generate new parts.

The GetAssociatedParts() method can be called to find some or all of the parts associated with an element, or use HasAssociatedParts() to determine if an element has parts.

You can delete parts through the API either by deleting the individual part elements, or by deleting the PartMaker associated to the parts (which will delete all parts generated by this PartMaker after the next regeneration).

Parts can be manipulated in the Revit API much the same as they can in the Revit user interface. For example, the outer boundaries of parts may be offset with PartUtils.SetFaceOffset().

___

The following example offsets all the faces of a part that can be offset.

<table summary="" id="GUID-FF4B3E7D-0804-4EE4-9384-C78255B5480C__TABLE_6A58E12349864DB5872559F3E7E14271"><tbody><tr><td><b>Code Region: Offset Faces of a Part</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>OffsetPartFaces</span><span>(</span><span>Part</span><span> part</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> part</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geomElem </span><span>=</span><span> part</span><span>.</span><span>get_Geometry</span><span>(</span><span>new</span><span> </span><span>Options</span><span>());</span><span>

    </span><span>foreach</span><span>(</span><span>GeometryObject</span><span> geomObject </span><span>in</span><span> geomElem</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>geomObject </span><span>is</span><span> </span><span>Solid</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Solid</span><span> solid </span><span>=</span><span> geomObject </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
            </span><span>FaceArray</span><span> faceArray </span><span>=</span><span> solid</span><span>.</span><span>Faces</span><span>;</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> face </span><span>in</span><span> faceArray</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>part</span><span>.</span><span>CanOffsetFace</span><span>(</span><span>face</span><span>))</span><span>
                </span><span>{</span><span>
                    part</span><span>.</span><span>SetFaceOffset</span><span>(</span><span>face</span><span>,</span><span> </span><span>1</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span><span> </span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/OffsetParts.jpg)

**Before and After Offseting faces of a selected Part**

## Returning the entities that create a divided Part

These methods identify and return the curves that were sketched to create the part division and, optionally, also outputs also the sketch plane for those curves.

-   PartUtils.GetSplittingCurves(Document, ElementId)
-   PartUtils.GetSplittingCurves(Document, ElementId, out SketchPlane)

`PartUtils.GetSplittingElements(Document, ElementId)`identifies and returns the elements ( ReferencePlane, Level or Grid ) that were used to create the division.

## Parts and Direct Shapes

Parts can be created from DirectShape instances, either in the same host document or in a link. These methods indicate whether it is possible to create parts from an instance of one of those classes.

-   DirectShape.CanCreateParts()
-   DirectShapeType.CanCreateParts()


<!-- ===== END: Help  Parts  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Dockable Dialog Panes  Autodesk.md ===== -->

---
created: 2026-01-28T21:16:44 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dockable_Dialog_Panes_html
author: 
---

# Help | Dockable Dialog Panes | Autodesk

> ## Excerpt
> Since Revit 2013, applications have been able to use modeless dialogs by taking advantage of the Idling Event and the External Events class in the Revit API. Add-ins requiring modeless dialogs also have the option to use dockable modeless dialogs. Similar to standard modeless dialogs, dockable dialogs are registered Windows Presentation Foundation (WPF) dialog panes that participate in Revit's window docking system. A registered dockable pane can dock into the top, left, right, and bottom of the main Revit window, as well as be added as a tab to an existing system pane, such as the project browser. Additionally, dockable panes can float, behaving much like a standard modeless dialog.

---
Since Revit 2013, applications have been able to use modeless dialogs by taking advantage of the [Idling Event](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_User_Inteface_Events_html) and the [External Events](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_External_Events_html) class in the Revit API. Add-ins requiring modeless dialogs also have the option to use dockable modeless dialogs. Similar to standard modeless dialogs, dockable dialogs are registered Windows Presentation Foundation (WPF) dialog panes that participate in Revit's window docking system. A registered dockable pane can dock into the top, left, right, and bottom of the main Revit window, as well as be added as a tab to an existing system pane, such as the project browser. Additionally, dockable panes can float, behaving much like a standard modeless dialog.

### IDockablePaneProvider

Registering a dockable pane requires an instance of the IDockablePaneProvider interface. The SetupDockablePane() method of this interface is called during initialization of the Revit user interface to gather information about add-in dockable pane windows. SetupDockablePane() has one parameter of type DockablePaneProviderData, which is a container for information about the new dockable pane.

Implementations of the IDockablePaneProvider interface should set the FrameworkElement and InitialState properties of DockablePaneProviderData. The FrameworkElement property is the Windows Presentation Framework object containing the pane's user interface.

Note: It is recommended that the dockable dialog in the add-in be the class that implements IDockablePaneProvider and that it be subclassed from System.Windows.Controls.Page.

The InitialState property is the initial position and settings of the docking pane, indicated by the DockablePaneState class. The pane's DockPosition can be Top, Bottom, Left, Right, Floating or Tabbed. If the position is Tabbed, the DockablePaneState.TabBehind property can be used to specify which pane the new pane will appear behind. If the position is Floating, the DockablePaneState.FloatingRectangle property contains the rectangle that determines the size and position of the pane.

### DockablePane

To access a dockable pane during runtime, it needs to be registered by calling the UIApplication.RegisterDockablePane() method. This method requires a unique identifier for the new pane (DockablePaneId), a string specifying the caption for the pane, and an implementation of the IDockablePaneProvider interface.

Dockable panes can be accessed by calling UIApplication.GetDockablePane() and passing in the unique DockablePaneId.This method returns a DockablePane. DockablePane.Show() will display the pane in the Revit user interface at its last docked location, if not currently visible. DockablePane.Hide() will hide a visible dockable pane. However, it has no effect on built-in Revit dockable panes.


<!-- ===== END: Help  Dockable Dialog Panes  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Dynamic Model Update  Autodesk.md ===== -->

---
created: 2026-01-28T21:16:49 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_html
author: 
---

# Help | Dynamic Model Update | Autodesk

> ## Excerpt
> Dynamic model update offers the ability for a Revit API application to modify the Revit model as a reaction to changes happening in the model when those changes are about to be committed at the end of a transaction. Revit API applications can create updaters by implementing the IUpdater interface and registering it with the UpdaterRegistry class. Registering includes specifying what changes in the model should trigger the updater.

---
Dynamic model update offers the ability for a Revit API application to modify the Revit model as a reaction to changes happening in the model when those changes are about to be committed at the end of a transaction. Revit API applications can create updaters by implementing the IUpdater interface and registering it with the UpdaterRegistry class. Registering includes specifying what changes in the model should trigger the updater.

**Pages in this section**

-   [Implementing IUpdater](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Implementing_IUpdater_html)
-   [The Execute method](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_The_Execute_method_html)
-   [Registering Updaters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Registering_Updaters_html)
-   [Exposure to End-User](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Exposure_to_End_User_html)

**Parent page:** [Advanced Topics](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_html)


<!-- ===== END: Help  Dynamic Model Update  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Implementing IUpdater  Autodesk.md ===== -->

---
created: 2026-01-28T21:16:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Implementing_IUpdater_html
author: 
---

# Help | Implementing IUpdater | Autodesk

> ## Excerpt
> The IUpdater interface requires that the following 5 methods to be implemented:

---
The IUpdater interface requires that the following 5 methods to be implemented:

-   GetUpdaterId() - This method should return a globally unique Id for the Updater consisting of the application Id plus a GUID for this Updater. This method is called once during registration of the Updater.
    
-   GetUpdaterName() - This returns a name by which the Updater can be identified to the user, if there is a problem with the Updater at runtime.
    
-   GetAdditionalInformation() - This method should return auxiliary text that Revit will use to inform the end user when the Updater is not loaded.
    
-   GetChangePriority() - This method identifies the nature of the changes the Updater will be performing. It is used to identify the order of execution of updaters. This method is called once during registration of the Updater.
    
-   Execute() - This is the method that Revit will invoke to perform an update. See the next section for more information on the Execute() method.
    

If a document is modified by an Updater, the document will store the unique Id of the updater. If the user later opens the document and the Updater is not present, Revit will warn the user that the 3<sup id="GUID-6D434229-0A2E-41FE-B29D-1BB2E6471F50__GUID-6E5D2283-83A6-4CEF-8A32-F90313B5F84E">rd</sup> party updater which previously edited the document is not available unless the Updater is flagged as optional. By default, updaters are non-optional and optional updaters should be used only when necessary.

The following code is a simple example of implementing the IUpdater interface (to change the WallType for newly added walls) and registering the updater in the OnStartup() method. It demonstrates all the key aspects of creating and using an updater.

<table summary="" id="GUID-6D434229-0A2E-41FE-B29D-1BB2E6471F50__TABLE_CA2261094F954FA8BC31C87B4CA0A70C"><tbody><tr><td><b>Code Region 25-1: Example of implementing IUpdater</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>WallUpdaterApplication</span><span> </span><span>:</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>IExternalApplication</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Register wall updater with Revit</span><span>
                </span><span>WallUpdater</span><span> updater </span><span>=</span><span> </span><span>new</span><span> </span><span>WallUpdater</span><span>(</span><span>application</span><span>.</span><span>ActiveAddInId</span><span>);</span><span>
                </span><span>UpdaterRegistry</span><span>.</span><span>RegisterUpdater</span><span>(</span><span>updater</span><span>);</span><span>

                </span><span>// Change Scope = any Wall element</span><span>
                </span><span>ElementClassFilter</span><span> wallFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>Wall</span><span>));</span><span>

                </span><span>// Change type = element addition</span><span>
                </span><span>UpdaterRegistry</span><span>.</span><span>AddTrigger</span><span>(</span><span>updater</span><span>.</span><span>GetUpdaterId</span><span>(),</span><span> wallFilter</span><span>,</span><span> </span><span>Element</span><span>.</span><span>GetChangeTypeElementAddition</span><span>());</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>WallUpdater</span><span> updater </span><span>=</span><span> </span><span>new</span><span> </span><span>WallUpdater</span><span>(</span><span>application</span><span>.</span><span>ActiveAddInId</span><span>);</span><span>
                </span><span>UpdaterRegistry</span><span>.</span><span>UnregisterUpdater</span><span>(</span><span>updater</span><span>.</span><span>GetUpdaterId</span><span>());</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>class</span><span> </span><span>WallUpdater</span><span> </span><span>:</span><span> </span><span>IUpdater</span><span>
</span><span>{</span><span>
        </span><span>static</span><span> </span><span>AddInId</span><span> m_appId</span><span>;</span><span>
        </span><span>static</span><span> </span><span>UpdaterId</span><span> m_updaterId</span><span>;</span><span>
        </span><span>WallType</span><span> m_wallType </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>// constructor takes the AddInId for the add-in associated with this updater</span><span>
        </span><span>public</span><span> </span><span>WallUpdater</span><span>(</span><span>AddInId</span><span> id</span><span>)</span><span>
        </span><span>{</span><span>
                m_appId </span><span>=</span><span> id</span><span>;</span><span>
                m_updaterId </span><span>=</span><span> </span><span>new</span><span> </span><span>UpdaterId</span><span>(</span><span>m_appId</span><span>,</span><span> </span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"FBFBF6B2-4C06-42d4-97C1-D1B4EB593EFF"</span><span>));</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>void</span><span> </span><span>Execute</span><span>(</span><span>UpdaterData</span><span> data</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Document</span><span> doc </span><span>=</span><span> data</span><span>.</span><span>GetDocument</span><span>();</span><span>

                </span><span>// Cache the wall type</span><span>
                </span><span>if</span><span> </span><span>(</span><span>m_wallType </span><span>==</span><span> </span><span>null</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
                        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>WallType</span><span>));</span><span>
                        </span><span>var</span><span> wallTypes </span><span>=</span><span> </span><span>from</span><span> element </span><span>in</span><span> collector
                                                        </span><span>where</span><span>
                                                                element</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Exterior - Brick on CMU"</span><span>
                                                        </span><span>select</span><span> element</span><span>;</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>wallTypes</span><span>.</span><span>Count</span><span>&lt;</span><span>Element</span><span>&gt;()</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
                        </span><span>{</span><span>
                                m_wallType </span><span>=</span><span> wallTypes</span><span>.</span><span>Cast</span><span>&lt;</span><span>WallType</span><span>&gt;().</span><span>ElementAt</span><span>&lt;</span><span>WallType</span><span>&gt;(</span><span>0</span><span>);</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>

                </span><span>if</span><span> </span><span>(</span><span>m_wallType </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>// Change the wall to the cached wall type.</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> addedElemId </span><span>in</span><span> data</span><span>.</span><span>GetAddedElementIds</span><span>())</span><span>
                        </span><span>{</span><span>
                                </span><span>Wall</span><span> wall </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>addedElemId</span><span>)</span><span> </span><span>as</span><span> </span><span>Wall</span><span>;</span><span>
                                </span><span>if</span><span> </span><span>(</span><span>wall </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
                                </span><span>{</span><span>
                                        wall</span><span>.</span><span>WallType</span><span> </span><span>=</span><span> m_wallType</span><span>;</span><span>
                                </span><span>}</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>string</span><span> </span><span>GetAdditionalInformation</span><span>()</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>"Wall type updater example: updates all newly created walls to a special wall"</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>ChangePriority</span><span> </span><span>GetChangePriority</span><span>()</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>ChangePriority</span><span>.</span><span>FloorsRoofsStructuralWalls</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>UpdaterId</span><span> </span><span>GetUpdaterId</span><span>()</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> m_updaterId</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>string</span><span> </span><span>GetUpdaterName</span><span>()</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>"Wall Type Updater"</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Implementing IUpdater  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  The Execute method  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_The_Execute_method_html
author: 
---

# Help | The Execute method | Autodesk

> ## Excerpt
> The purpose of the Execute() method is to allow your Updater to react to changes that have been made to the document, and make appropriate related. This method is invoked by Revit at the end of a document transaction in which elements that matched the UpdateTrigger for this Updater were added, changed or deleted. The method may be invoked more than once for the same transaction due to changes made by other Updaters. Updaters are invoked before the DocumentChanged event, so this event will contain changes made by all updaters.

---
The purpose of the Execute() method is to allow your Updater to react to changes that have been made to the document, and make appropriate related. This method is invoked by Revit at the end of a document transaction in which elements that matched the UpdateTrigger for this Updater were added, changed or deleted. The method may be invoked more than once for the same transaction due to changes made by other Updaters. Updaters are invoked before the DocumentChanged event, so this event will contain changes made by all updaters.

All changes to the document made during the invocation of this method will become a part of the invoking transaction, and maintained for undo and redo operations. When implementing this method you may not open any new transactions (an exception will be thrown), but you may use sub-transactions as required.

Although it can be used to also update data outside of the document, such changes will not become part of the original transaction and will not be subject to undo or redo when the original transaction is undone or redone. If you do use this method to modify data outside of the document, you should also subscribe to the DocumentChanged event to update your data when the original transaction is undone or redone.

### Scope of Changes

The Execute() method has an UpdaterData parameter that provides all necessary data needed to perform the update, including the document and information about the changes that triggered the update. Three basic methods (GetAddedElementIds(),GetDeletedElementIds(), and GetModifiedElementIds()) identify the elements that triggered the update. The Updater can also check specifically if a particular change triggered the update by using the IsChangeTriggered() method.

### Forbidden and Cautionary Changes

The following methods may not be called while executing an Updater, because they introduce cross references between elements. (This can result in document corruption when these changes are combined with workset operations). A ForbiddenForDynamicUpdateException will be thrown when an updater attempts to call any of these methods:

-   Autodesk.Revit.DB.ViewSheet.AddView()
-   Autodesk.Revit.DB.Document.LoadFamily(Autodesk.Revit.DB.Document, Autodesk.Revit.DB.IFamilyLoadOptions)
-   AreaReinforcement.Create()
-   PathReinforcement.Create()

In addition to the forbidden methods listed above, other API methods that require documents to be in transaction-free state may not be called either. Such methods include but are not limited to Save(), SaveAs(), Close(), LoadFamily(), etc. Please refer to the documentation of the respective methods for more information.

Calls to the UpdaterRegistry class, such as RegistryUpdater() or AddTrigger(), from within the Execute() method of an updater are also forbidden. Calling any of the UpdaterRegistry methods will throw an exception. The one exception to this rule is the UpdaterRegistry.UnregisterUpdater() method, which may be called during execution of an updater as long as the updater to be unregistered is not the one currently being executed.

Although the following methods are allowed during execution of an Updater, they can also throw ForbiddenForDynamicUpdateException when cross-references between elements are established as a result of the call. One such example could be creating a face wall that intersects with an existing face wall, so those two would have to be joined together. Apply caution when calling these methods from an Updater:

-   Autodesk.Revit.Creation.ItemFactoryBase.NewFamilyInstances2()
-   Autodesk.Revit.Creation.ItemFactoryBase.NewFamilyInstance(Autodesk.Revit.DB.XYZ, Autodesk.Revit.DB.FamilySymbol, Autodesk.Revit.DB.Element,Autodesk.Revit.DB.Structure.StructuralType)
-   Autodesk.Revit.Creation.Document.NewFamilyInstance(Autodesk.Revit.DB.XYZ, Autodesk.Revit.DB.FamilySymbol, Autodesk.Revit.DB.Element, Autodesk.Revit.DB.Level, Autodesk.Revit.DB.Structure.StructuralType)
-   Autodesk.Revit.DB.FaceWall.Create()

It should also be noted that deleting and recreating existing elements should be avoided if modifying them would suffice. While deleting elements may be a simpler solution, it will not only affect Revit's performance, but it will also destroy any references to "recreated" objects from other elements. This could cause the user to lose work they have done to constrain and annotate the elements in question.

### Managing Changes

Updaters need to be able to handle complex issues that may arise from their use, possibly reconciling subsequent changes to an element. Elements modified by an updater may change by the time the updater is next invoked, and those changes may impact information modified by the updater. For example, the element may be explicitly edited by the user, or implicitly edited due to propagated changes triggered by a regeneration.

It is also possible that the same element may be modified by another updater, possibly even within the same transaction. Although explicit changes of exactly the same data is tracked and prohibited, indirect or propagated changes are still possible. Perhaps the most complex case is that an element could be changed by the user and/or the same updater in different versions of the file. After the user reloads the latest or saves to central, the modified target element will be brought from the other file and the updater will need to reconcile changes.

It is also important to realize that when a document synchs with the central file, the ElementId of elements may be affected. If new elements have been added to two versions of the same file and the same ElementId is used in both places, this will be reconciled when the files are synched to the central database. For this reason, when using updaters to cross-reference one element in another element, they should use Element.UniqueId which is guaranteed to be unique.

Another issue to consider is if an updater attaches some data (i.e. as a parameter) to an element, it not only must be sure to maintain that information in the element to which it was added, but also to reconcile data in cases when that element is duplicated via copy/paste or group propagation. For example, if an updater adds a parameter "Total weight of rebar" to a rebar host, that parameter and its value will be copied to the duplicated rebar host even though the rebar itself may be not copied with the host. In this case the updater needs to ensure the parameter value is reset in the newly copied rebar host.


<!-- ===== END: Help  The Execute method  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Registering Updaters  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Registering_Updaters_html
author: 
---

# Help | Registering Updaters | Autodesk

> ## Excerpt
> Updaters must be registered in order to be notified of changes to the model. The application level UpdaterRegistry class provides the ability to register/unregister and manipulate the options set for Updaters. Updaters may be registered from any API callback and can be registered as application-wide or document-specific, meaning they will only be triggered by changes made to the specified document. In order to use the UpdaterRegistry functionality, the Revit add-in must be registered in a manifest file and the Id returned by UpdaterId.GetAddInId() for any Updater (obtained from GetUpdaterId()) must match the AddInId field in the add-in's manifest file. An add-in cannot add, remove, or modify Updaters that do not belong to it.

---
Updaters must be registered in order to be notified of changes to the model. The application level UpdaterRegistry class provides the ability to register/unregister and manipulate the options set for Updaters. Updaters may be registered from any API callback and can be registered as application-wide or document-specific, meaning they will only be triggered by changes made to the specified document. In order to use the UpdaterRegistry functionality, the Revit add-in must be registered in a manifest file and the Id returned by UpdaterId.GetAddInId() for any Updater (obtained from GetUpdaterId()) must match the AddInId field in the add-in's manifest file. An add-in cannot add, remove, or modify Updaters that do not belong to it.

### Triggers

In addition to calling the UpdaterRegistry.RegisterUpdater() method, Updaters should add one or more update triggers via the AddTrigger() methods. These triggers indicate to the UpdaterRegistry what events should trigger the Updaters Execute() method to run. They can be set application-wide, or can apply to changes made in a specific document. Update triggers are specified by pairing a change scope and a change type.

The change scope is one of two things:

-   An explicit list of element Ids in a document - only changes happening to those elements will trigger the Updater
-   An implicit list of elements communicated via an ElementFilter - every changed element will be run against the filter, and if any pass, the Updater is triggered

There are several options available for change type. ChangeTypes are obtained from static methods on the Element class.

-   Element addition - via Element.GetChangeTypeElementAddition()
-   Element deletion - via Element.GetChangeTypeElementDeletion()
-   Change of element geometry (shape or position) - via Element.GetChangeTypeGeometry()
-   Changing value of a specific parameter - via Element.GetChangeTypeParameter()
-   Any change of element - via Element.GetChangeTypeAny().

Note that geometry changes are triggered due to potentially many causes, like a change of element type, modification of properties and parameters, move and rotate, or changes imposed on the element from other modified elements during regeneration.

Also note that the last option, any change of element, only triggers the Updater for modifications of pre-existing elements, and does not trigger the Updater for newly added or deleted elements. Additionally, when using this trigger for an instance, only certain modifications to its type will trigger the Updater. Changes that affect the instance itself, such as modification of the instance's geometry, will trigger the Updater. However, changes that do not modify the instance directly and do not result in any discernable change to the instance, such as changes to text parameters, will not trigger the Updater for the instance. To trigger based on these changes, the Type must also be included in the trigger's change scope.

### Order of Execution

The primary way that Revit sorts multiple Updaters to execute in the correct order is by looking at the ChangePriority returned by a given Updater. An Updater reporting a priority for a more fundamental set of elements (e.g. GridsLevelsReferencePlanes) will execute prior to Updaters reporting a priority for elements driven by these fundamental elements (e.g. Annotations). Reporting a proper change priority for the elements which your Updater modifies benefits users of your application: Revit is less likely to have to execute the Updater a second time due to changes made by another Updater.

For Updaters which report the same change priority, execution is ordered based on a sorting of UpdaterId. The method UpdaterRegistry.SetExecutionOrder() allows you set the execution order between any two registered Updaters (even updaters registered by other API add-ins) so long as your code knows the ids of the two Updaters.


<!-- ===== END: Help  Registering Updaters  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Exposure to End-User  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Exposure_to_End_User_html
author: 
---

# Help | Exposure to End-User | Autodesk

> ## Excerpt
> When updaters work as they should, they are transparent to the user. In some special cases though, Revit will display a warning to the user concerning a 3rd party updater. Such messages will use the value of the GetUpdaterName() method to refer to the updater.

---
When updaters work as they should, they are transparent to the user. In some special cases though, Revit will display a warning to the user concerning a 3<sub id="GUID-EEE24659-C2D4-4925-B756-D15A3696D0F8__GUID-CE4AFA9D-ECF1-42D3-B2DE-4CA9C12B9372">rd</sub> party updater. Such messages will use the value of the GetUpdaterName() method to refer to the updater.

### Updater not installed

If a document is modified by a non-optional updater and later loaded when that updater is not installed, a task dialog similar to the following is displayed:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-301A03BC-C348-483D-980C-30B05831F84B-low.png)**Figure 135: Missing Third Party Updater Warning**

### Updater performs invalid operation

If an updater has an error, such as an unhandled exception, a message similar to the following is displayed giving the user the option to disable the updater:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-D68E0684-0F8A-47D5-9803-61523979E454-low.png)**Figure 136: Updater performed an invalid operation**

If the user selects Cancel, the entire transaction is rolled back. In the Wall Updater example from earlier in this chapter, the newly added wall is removed. If the user selects Disable Updater, the updater is no longer called, but the transaction is not rolled back.

### Infinite loop

In the event that an updater falls into an infinite loop, Revit will notify the user and disable the updater for the duration of the Revit session.

### Two updaters attempt to edit same element

If an updater attempts to edit the same parameter of an element that was updated by another updater in the same transaction, or if an updater attempts to edit the geometry of an element in a way that conflicts with a change made by another updater, the updater is canceled, an error message is displayed and the user is given the option to disable the updater.

### Central document modified by updater not present locally

If the user reloads latest or saves to central with a central file that was modified by an updater that is not installed locally, a task dialog is presented giving them the option to continue or cancel the synchronization. The warning indicates that proceeding may cause problems with the central model when it is used with the third party updater at a later time.


<!-- ===== END: Help  Exposure to End-User  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Storing Data in the Revit model  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:20 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Storing_Data_in_the_Revit_model_html
author: 
---

# Help | Storing Data in the Revit model | Autodesk

> ## Excerpt
> Use shared parameters or extensible storage to store data in the Revit model.

---
Use shared parameters or extensible storage to store data in the Revit model.

The Revit API provides two methods for storing data in the Revit model. The first is using shared parameters. The Revit API gives programmatic access to the same shared parameters feature that is available through the Revit UI. Shared parameters, if defined as visible, will be viewable to the user in an element's property window. Shared parameters can be assigned to many, but not all, categories of elements. For more information, see [Shared Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_html "Shared Parameters are parameter definitions stored in an external text file").

The other option is extensible storage, which allows you to create custom data structures and then assign instances of that data to elements in the model. This data is never visible to the user in the Revit UI, but may be accessible to other third party applications via the Revit API depending on the read/write access assigned to the schema when it is defined. Unlike Shared Parameters, extensible storage is not limited to certain categories of elements. Extensible storage data can be assigned to any object that derives from the base class Element in the Revit model.


<!-- ===== END: Help  Storing Data in the Revit model  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Extensible Storage  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:25 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Storing_Data_in_the_Revit_model_Extensible_Storage_html
author: 
---

# Help | Extensible Storage | Autodesk

> ## Excerpt
> Create your own class-like Schema data structures and attach instances of them to any Element in a Revit model.

---
Create your own class-like Schema data structures and attach instances of them to any Element in a Revit model.

Schema-based data is saved with the Revit model and allows for higher-level, metadata-enhanced, object-oriented data structures. Schema data can be configured to be readable and/or writable to all users, just a specific application vendor, or just a specific application from a vendor.

The following steps are necessary to store data with Elements in Revit:

1.  Create and name a new schema
2.  Set the read/write access for the schema
3.  Define one or more fields of data for the schema
4.  Create an entity based on the schema
5.  Assign values to the fields for the entity
6.  Associate the entity with a Revit element
    
    ### Schemas and SchemaBuilder
    

The first step to creating extensible storage is to define the schema. A schema is similar to a class in an object-oriented programming language. Use the SchemaBuilder class constructor to create a new schema. SchemaBuilder is a helper class used to create schemas. Once a schema is finalized using SchemaBuilder, the Schema class is used to access properties of the schema. At that stage, the schema is no longer editable.

Although the SchemaBuilder constructor takes a GUID which is used to identify the schema, a schema name is also required. After creating the schema, call SchemaBuilder.SetSchemaName() to assign a user-friendly identifier for the schema. The schema name is useful to identify a schema in an error message.

The read and write access levels of entities associated with the schema can be set independently. The options are Public, Vendor, or Application. If either the read or write access level is set to Vendor, the VendorId of the third-party vendor that may access entities of the schema must be specified. If either access level is set to Application, the GUID of the application or add-in that may access entities of the schema must be supplied.

Note: Schemas are stored with the document and any Revit API add-in may read the available schemas in the document, as well as some data of the schema. However, access to the fields of a schema is restricted based on the read access defined in the schema and the actual data in the entities stored with specific elements is restricted based on the read and write access levels set in the schema when it is defined.

### Fields and FieldBuilder

Once the schema has been created, fields may be defined. A field is similar to a property of a class. It contains a name, documentation, value type and unit type. Fields can be a simple type, an array, or a map. The following simple data types are allowed:

<table summary="" id="GUID-113B09CA-DBBB-41A7-8021-005663B267AE__TABLE_0E949AA5AB7F45FA9C786263C927A687"><tbody><tr><td><b>Type</b></td><td><b>Default Value</b></td></tr><tr><td>int</td><td>0</td></tr><tr><td>short</td><td>0</td></tr><tr><td>byte</td><td>0</td></tr><tr><td>double</td><td>0.0</td></tr><tr><td>float</td><td>0.0</td></tr><tr><td>bool</td><td>false</td></tr><tr><td>string</td><td>Empty string ("")</td></tr><tr><td>GUID</td><td>Guid.Empty {00000000-0000-0000-0000-000000000000}</td></tr><tr><td>ElementId</td><td>ElementId.InvalidElementId</td></tr><tr><td>Autodesk.Revit.DB.XYZ</td><td>(0.0,0.0,0.0)</td></tr><tr><td>Autodesk.Revit.DB.UV</td><td>(0.0,0.0)</td></tr></tbody></table>

Additionally, a field may be of type Autodesk.Revit.DB.ExtensibleStorage.Entity. In other words, an instance of another Schema, also known as a SubSchema or SubEntity. The default value for a field of this type is Entity with null schema, and guid of Guid.Empty.

When using string fields, note that Revit has a 16mb limit on string objects.

A simple field can be created using the SchemaBuilder.AddSimpleField() method to specify a name and type for the field. AddSimpleField() returns a FieldBuilder, which is a helper class for defining Fields. If the type of the field was specified as Entity, use FieldBuilder.SetSubSchemaGUID() to specify the GUID of the schema of the Entities that are to be stored in this field.

Use the SchemaBuilder.AddArrayField() method to create a field containing an array of values in the Schema, with a given name and type of contained values. Array fields can have all the same types as simple fields.

Use the SchemaBuilder.AddMapField() method to create a field containing an ordered key-value map in the Schema, with given name, type of key and type of contained values. Supported types for values are the same as for simple fields. Supported types for keys are limited to int, short, byte, string, bool, ElementId and GUID.

Once the schema is finalized using SchemaBuilder, fields can no longer be edited using FieldBuilder. At that stage, the Schema class provides methods to get a Field by name, or a list of all Fields defined in the Schema.

### Entities

After all fields have been defined for the schema, SchemaBuilder.Finish() will return the finished Schema. A new Entity can be created using that schema. For each Field in the Schema, the value can be stored using Entity.Set(), which takes a Field and a value (whose type is dependent on the field type). Once all applicable fields have been set for the entity, it can be assigned to an element using the Element.SetEntity() method.

To retrieve the data later, call Element.GetEntity() passing in the corresponding Schema. If no entity based on that schema was saved with the Element, an invalid Entity will be returned. To check that a valid Entity was returned, call the Entity.IsValid() method. Field values from the entity can be obtained using the Entity.Get() method.

To remove an extensible storage entity from an Element, call Element.DeleteEntity() passing in the Schema that was used to create it.

To determine Entities stored with an element, use the Element.GetEntitySchemaGuids() method, which returns the Schema guids of any Entities for the Element. The Schema guids can be used with the static method Schema.Lookup() to retrieve the corresponding Schemas.

The following is an example of defining an extensible storage Schema, creating an Entity, setting its values, assigning it to an Element, and retrieving the data.

<table summary="" id="GUID-113B09CA-DBBB-41A7-8021-005663B267AE__TABLE_5ADE5BC497BC47A5B2203B87CA13070D"><tbody><tr><td><b>Code Region 22-9: Extensible Storage</b></td></tr><tr><td><pre><code><span>// Create a data structure, attach it to a wall, populate it with data, and retrieve the data back from the wall</span><span>
</span><span>void</span><span> </span><span>StoreDataInWall</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> XYZ dataToStore</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Transaction</span><span> createSchemaAndStoreData </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>wall</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"tCreateAndStore"</span><span>);</span><span>
        createSchemaAndStoreData</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>SchemaBuilder</span><span> schemaBuilder </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>SchemaBuilder</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"720080CB-DA99-40DC-9415-E53F280AA1F0"</span><span>));</span><span>
        schemaBuilder</span><span>.</span><span>SetReadAccessLevel</span><span>(</span><span>AccessLevel</span><span>.</span><span>Public</span><span>);</span><span> </span><span>// allow anyone to read the object</span><span>
        schemaBuilder</span><span>.</span><span>SetWriteAccessLevel</span><span>(</span><span>AccessLevel</span><span>.</span><span>Vendor</span><span>);</span><span> </span><span>// restrict writing to this vendor only</span><span>
        schemaBuilder</span><span>.</span><span>SetVendorId</span><span>(</span><span>"ADSK"</span><span>);</span><span> </span><span>// required because of restricted write-access</span><span>
        schemaBuilder</span><span>.</span><span>SetSchemaName</span><span>(</span><span>"WireSpliceLocation"</span><span>);</span><span>
        </span><span>// create a field to store an XYZ</span><span>
        </span><span>FieldBuilder</span><span> fieldBuilder </span><span>=</span><span> 
                schemaBuilder</span><span>.</span><span>AddSimpleField</span><span>(</span><span>"WireSpliceLocation"</span><span>,</span><span> </span><span>typeof</span><span>(</span><span>XYZ</span><span>));</span><span> 
        fieldBuilder</span><span>.</span><span>SetSpec</span><span>(</span><span>SpecTypeId</span><span>.</span><span>Length</span><span>);</span><span>
        fieldBuilder</span><span>.</span><span>SetDocumentation</span><span>(</span><span>"A stored location value representing a wiring splice in a wall."</span><span>);</span><span>

        </span><span>Schema</span><span> schema </span><span>=</span><span> schemaBuilder</span><span>.</span><span>Finish</span><span>();</span><span> </span><span>// register the Schema object</span><span>
        </span><span>Entity</span><span> entity </span><span>=</span><span> </span><span>new</span><span> </span><span>Entity</span><span>(</span><span>schema</span><span>);</span><span> </span><span>// create an entity (object) for this schema (class)</span><span>
        </span><span>// get the field from the schema</span><span>
        </span><span>Field</span><span> fieldSpliceLocation </span><span>=</span><span> schema</span><span>.</span><span>GetField</span><span>(</span><span>"WireSpliceLocation"</span><span>);</span><span> 
        </span><span>// set the value for this entity</span><span>
        entity</span><span>.</span><span>Set</span><span>&lt;</span><span>XYZ</span><span>&gt;(</span><span>fieldSpliceLocation</span><span>,</span><span> dataToStore</span><span>,</span><span> </span><span>UnitTypeId</span><span>.</span><span>Meters</span><span>);</span><span>
        wall</span><span>.</span><span>SetEntity</span><span>(</span><span>entity</span><span>);</span><span> </span><span>// store the entity in the element</span><span>

        </span><span>// get the data back from the wall</span><span>
        </span><span>Entity</span><span> retrievedEntity </span><span>=</span><span> wall</span><span>.</span><span>GetEntity</span><span>(</span><span>schema</span><span>);</span><span>
        XYZ retrievedData </span><span>=</span><span> 
                retrievedEntity</span><span>.</span><span>Get</span><span>&lt;</span><span>XYZ</span><span>&gt;(</span><span>schema</span><span>.</span><span>GetField</span><span>(</span><span>"WireSpliceLocation"</span><span>),</span><span>
                </span><span>UnitTypeId</span><span>.</span><span>Meters</span><span>);</span><span>
        createSchemaAndStoreData</span><span>.</span><span>Commit</span><span>();</span><span>  
</span><span>}</span></code></pre></td></tr></tbody></table>

## Advantages

#### Self Documenting and Self-Defining

Creating a schema by adding fields, units, sub-entities, and description strings is not only a means for storing data. It is also implicit documentation for other users and a way for others to create entities of the same schema later with an easy adoption path.

#### Takes Advantage of Locality

Because schema entities are stored on a per-element basis, there is no need to necessarily read all extensible storage data in a document (e.g. all data from all beam family instances) when an application might only need data for the currently selected beam. This allows the potential for more specifically targeted data access code and better data access performance overall.


<!-- ===== END: Help  Extensible Storage  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Events  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_html
author: 
---

# Help | Events | Autodesk

> ## Excerpt
> Events are notifications that are triggered on specific actions in the Revit user interface or API workflows. By subscribing to events, an add-in application can be notified when an action is about to happen or has just happened and take some action related to that event. Some events come in pairs around actions, one occurring before the action takes place ("pre" event) and the other happening after the action takes place ("post" event). Events that do not occur in these pre/post pairs are called "single" events.

---
Events are notifications that are triggered on specific actions in the Revit user interface or API workflows. By subscribing to events, an add-in application can be notified when an action is about to happen or has just happened and take some action related to that event. Some events come in pairs around actions, one occurring before the action takes place ("pre" event) and the other happening after the action takes place ("post" event). Events that do not occur in these pre/post pairs are called "single" events.

Revit provides access to events at both the Application level (such as ApplicationClosing or DocumentOpened) and the Document level (such as DocumentClosing and DocumentPrinting). The same application level events available from the Application class are also available from the ControlledApplication class, which represents the Revit application with no access to documents. It is ControlledApplication that is available to add-ins from the OnStartup() and OnShutdown() methods. In terms of subscribing and unsubscribing to events, these classes are interchangeable; subscribing to an event from the ControlledApplication class is the same as subscribing from the Application class.

Events can also be categorized as database (DB) events or user interface (UI) events. DB events are available from the Application and Document classes, while UI events are available from the UIApplication class. (Currently all UI events are at the application level only).

Some events are considered read-only, which means that during their execution the model may not be modified. The fact that an event is read-only is documented in the API help file. It is important to know that even during regular events (i.e. not read-only events), the model may be in a state in which it cannot be modified. The programmer should check the properties Document.IsModifiable and Document.IsReadOnly to determine whether the model may be modified.


<!-- ===== END: Help  Events  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Database Events  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:34 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Database_Events_html
author: 
---

# Help | Database Events | Autodesk

> ## Excerpt
> The following table lists database events, their type and whether they are available at the application and/or document level:

---
The following table lists database events, their type and whether they are available at the application and/or document level:

**Table 53: DB Event Types**

<table summary="" id="GUID-BB901E53-61FD-4D4A-8571-3CC6582DA85A__TABLE_DF9946D275D04F2785B0ED6712065C42"><tbody><tr><td><b>Event</b></td><td><b>Type</b></td><td><b>Application</b></td><td><b>Document</b></td></tr><tr><td><a href="https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Database_Events_DocumentChanged_event_html" data-url="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/files/Revit_API_Developers_Guide/Advanced_Topics/Events/Database_Events/Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Database_Events_DocumentChanged_event_html.html">DocumentChanged event</a></td><td>single</td><td>X</td><td></td></tr><tr><td>DocumentClosing</td><td>pre</td><td>X</td><td>X</td></tr><tr><td>DocumentClosed</td><td>post</td><td>X</td><td></td></tr><tr><td>DocumentCreating</td><td>pre</td><td>X</td><td></td></tr><tr><td>DocumentCreated</td><td>post</td><td>X</td><td></td></tr><tr><td>DocumentOpening</td><td>pre</td><td>X</td><td></td></tr><tr><td>DocumentOpened</td><td>post</td><td>X</td><td></td></tr><tr><td>DocumentPrinting</td><td>pre</td><td>X</td><td>X</td></tr><tr><td>DocumentPrinted</td><td>post</td><td>X</td><td>X</td></tr><tr><td>DocumentSaving</td><td>pre</td><td>X</td><td>X</td></tr><tr><td>DocumentSaved</td><td>post</td><td>X</td><td>X</td></tr><tr><td>DocumentSavingAs</td><td>pre</td><td>X</td><td>X</td></tr><tr><td>DocumentSavedAs</td><td>post</td><td>X</td><td>X</td></tr><tr><td>DocumentSynchronizingWithCentral</td><td>pre</td><td>X</td><td></td></tr><tr><td>DocumentSynchronizedWithCentral</td><td>post</td><td>X</td><td></td></tr><tr><td>FailuresProcessing</td><td>single</td><td>X</td><td></td></tr><tr><td>FileExporting</td><td>pre</td><td>X</td><td></td></tr><tr><td>FileExported</td><td>post</td><td>X</td><td></td></tr><tr><td>FileImporting</td><td>pre</td><td>X</td><td></td></tr><tr><td>FileImported</td><td>post</td><td>X</td><td></td></tr><tr><td>ProgressChanged</td><td>single</td><td>X</td><td>&nbsp;</td></tr><tr><td>ViewPrinting</td><td>pre</td><td>X</td><td>X</td></tr><tr><td>ViewPrinted</td><td>post</td><td>X</td><td>X</td></tr></tbody></table>

-   DocumentChanged - notification when a transaction is committed, undone or redone
-   DocumentClosing - notification when Revit is about to close a document
-   DocumentClosed - notification just after Revit has closed a document
-   DocumentCreating - notification when Revit is about to create a new document
-   DocumentCreated - notification when Revit has finished creating a new document
-   DocumentOpening - notification when Revit is about to open a document
-   DocumentOpened - notification after Revit has opened a document
-   DocumentPrinting - notification when Revit is about to print a view or ViewSet of the document
-   DocumentPrinted - notification just after Revit has printed a view or ViewSet of the document
-   DocumentSaving - notification when Revit is about to save the document
-   DocumentSaved - notification just after Revit has saved the document
-   DocumentSavingAs - notification when Revit is about to save the document with a new name
-   DocumentSavedAs - notification when Revit has just saved the document with a new name
-   DocumentSynchronizingWithCentral - notification when Revit is about to synchronize a document with the central file
-   DocumentSynchronizedWithCentral - notification just after Revit has synchronized a document with the central file
-   FailuresProcessing - notification when Revit is processing failures at the end of a transaction
-   FileExporting - notification when Revit is about to export to a file format supported by the API
-   FileExported - notification after Revit has exported to a file format supported by the API
-   FileImporting - notification when Revit is about to import a file format supported by the API
-   FileImported - notification after Revit has imported a file format supported by the API
-   ProgressChanged - notification when an operation in Revit has progress bar data
-   ViewPrinting - notification when Revit is about to print a view of the document
-   ViewPrinted - notification just after Revit has printed a view of the document


<!-- ===== END: Help  Database Events  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  DocumentChanged event  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Database_Events_DocumentChanged_event_html
author: 
---

# Help | DocumentChanged event | Autodesk

> ## Excerpt
> The DocumentChanged event is triggered when the Revit document has changed. This event is raised whenever a Revit transaction is either committed, undone or redone. This is a read-only event, designed to allow external data to be kept in synch with the state of the Revit database. To update the Revit database in response to changes in elements, use the IUpdater framework.

---
The DocumentChanged event is triggered when the Revit document has changed. This event is raised whenever a Revit transaction is either committed, undone or redone. This is a read-only event, designed to allow external data to be kept in synch with the state of the Revit database. To update the Revit database in response to changes in elements, use the IUpdater framework.

The DocumentChangedEventArgs class is used by the DocumentChanged event. This class has several methods to get the element Ids of any newly added elements (GetAddElementIds()), deleted elements (GetDeletedElementIds()) or elements that have been modified (GetModifiedElementIds()). The GetAddElementIds() and GetModifiedElementIds() methods have overloads that take an ElementFilter, which makes it easy to detect only changes of interest.


<!-- ===== END: Help  DocumentChanged event  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  User Inteface Events  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:44 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_User_Inteface_Events_html
author: 
---

# Help | User Inteface Events | Autodesk

> ## Excerpt
> The following table lists user interface events, their type and whether they are available at the application and/or document level:

---
The following table lists user interface events, their type and whether they are available at the application and/or document level:

**Table 54: UI Event Types**

<table summary="" id="GUID-062C0D65-EF26-4341-B1E5-C532AF0767D6__TABLE_4CEFEB89263846C6851A67D24CF2DD5E"><tbody><tr><td><b>Event</b></td><td><b>Type</b></td><td><b>UIApplication</b></td><td><b>ControlledApplication</b></td><td><b>UIDocument</b></td></tr><tr><td>ApplicationClosing</td><td>pre</td><td>X</td><td>&nbsp;</td><td></td></tr><tr><td>ApplicationInitialized</td><td>single</td><td>&nbsp;</td><td>X</td><td>&nbsp;</td></tr><tr><td>DialogBoxShowing</td><td>single</td><td>X</td><td>&nbsp;</td><td></td></tr><tr><td>DisplayingOptionsDialog</td><td>single</td><td>X</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>Idling</td><td>single</td><td>X</td><td>&nbsp;</td><td></td></tr><tr><td>ViewActivating</td><td>pre</td><td>X</td><td>&nbsp;</td><td></td></tr><tr><td>ViewActivated</td><td>post</td><td>X</td><td>&nbsp;</td><td></td></tr></tbody></table>

-   ApplicationClosing - notification when the Revit application is about to be closed
-   ApplicationInitialized - notification after the Revit application has been initialized, after all external applications have been started and the application is ready to work with documents
-   DialogBoxShowing - notification when Revit is showing a dialog or message box
-   DisplayingOptionsDialog - notification when Revit options dialog is displaying
-   Idling - notification when Revit is not in an active tool or transaction
-   ViewActivating - notification when Revit is about to activate a view of the document
-   ViewActivated - notification just after Revit has activated a view of the document


<!-- ===== END: Help  User Inteface Events  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Registering Events  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:49 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Registering_Events_html
author: 
---

# Help | Registering Events | Autodesk

> ## Excerpt
> Where and how to register events.

---
Where and how to register events.

Using events is a two step process. First, you must have a function that will handle the event notification. This function must take two parameters, the first is an Object that denotes the "sender" of the event notification, the second is an event-specific object that contains event arguments specific to that event. For example, to register the DocumentSavingAs event, your event handler must take a second parameter that is a DocumentSavingAsEventArgs object.

The second part of using an event is registering the event with Revit. This can be done as early as in the OnStartup() function through the ControlledApplication parameter, or at any time after Revit starts up. Although events can be registered for External Commands as well as External Applications, it is not recommended unless the External Command registers and unregisters the event in the same external command. Also note that registering to and unregistering from events must happen while executing on the main thread. An exception will be thrown if an external application attempts to register to (or unregister from) events from outside of a valid API context.

The following example registers the DocumentOpened event, and when that event is triggered, this application will set the address of the project.

<table summary="" id="GUID-8DF6F94A-1460-42AD-AC00-CF92B9A135BA__TABLE_1777953E7120479DB3E78278CB9B7CA5"><tbody><tr><td><b>Code Region 24-1: Registering ControlledApplication.DocumentOpened</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>Application_DocumentOpened</span><span> </span><span>:</span><span> </span><span>IExternalApplication</span><span>
</span><span>{</span><span>
    </span><span>/// &lt;ExampleMethod&gt;</span><span>
    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Implement this method to subscribe to event.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>try</span><span>
        </span><span>{</span><span>
            </span><span>// Register event. </span><span>
            application</span><span>.</span><span>ControlledApplication</span><span>.</span><span>DocumentOpened</span><span> </span><span>+=</span><span> </span><span>new</span><span> </span><span>EventHandler</span><span>
                </span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Events</span><span>.</span><span>DocumentOpenedEventArgs</span><span>&gt;(</span><span>application_DocumentOpened</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// remove the event.</span><span>
        application</span><span>.</span><span>ControlledApplication</span><span>.</span><span>DocumentOpened</span><span> </span><span>-=</span><span> application_DocumentOpened</span><span>;</span><span>
        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>void</span><span> application_DocumentOpened</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>DocumentOpenedEventArgs</span><span> args</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// get document from event args.</span><span>
        </span><span>Document</span><span> doc </span><span>=</span><span> args</span><span>.</span><span>Document</span><span>;</span><span>

        </span><span>// Following code snippet demonstrates support of DocumentOpened event to modify the model.</span><span>
        </span><span>// Because DocumentOpened supports model changes, it allows user to update document data.</span><span>
        </span><span>// Here, this sample assigns a specified value to ProjectInformation.Address property. </span><span>
        </span><span>// User can change other properties of document or create(delete) something as he likes.</span><span>
        </span><span>//</span><span>
        </span><span>// Please note that ProjectInformation property is empty for family document.</span><span>
        </span><span>// So please don't run this sample on family document.</span><span>
        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Edit Address"</span><span>))</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>transaction</span><span>.</span><span>Start</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
            </span><span>{</span><span>
                doc</span><span>.</span><span>ProjectInformation</span><span>.</span><span>Address</span><span> </span><span>=</span><span>
                    </span><span>"United States - Massachusetts - Waltham - 1560 Trapelo Road"</span><span>;</span><span>
                transaction</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Registering Events  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Canceling Events  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:54 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Canceling_Events_html
author: 
---

# Help | Canceling Events | Autodesk

> ## Excerpt
> Events that are triggered before an action has taken place (i.e. DocumentSaving) are often cancellable. (Use the Cancellable property to determine if the event can be cancelled.) For example, you may want to check some criteria are met in a model before it is saved. By registering for the DocumentSaving or DocumentSavingAs event, for example, you can check for certain criteria in the document and cancel the Save or Save As action. Once cancelled, an event cannot be un-cancelled.

---
Events that are triggered before an action has taken place (i.e. DocumentSaving) are often cancellable. (Use the Cancellable property to determine if the event can be cancelled.) For example, you may want to check some criteria are met in a model before it is saved. By registering for the DocumentSaving or DocumentSavingAs event, for example, you can check for certain criteria in the document and cancel the Save or Save As action. Once cancelled, an event cannot be un-cancelled.

Note: If a pre-event is cancelled, other event handlers that have subscribed to the event will not be notified. However, handlers that have subscribed to a post-event related to the pre-event will be notified. The following event handler for the DocumentSavingAs event checks if the ProjectInformation Status parameter is empty, and if it is, cancels the SaveAs event. Note that if your application cancels an event, it should offer an explanation to the user.

<table summary="" id="GUID-318E460B-FBA3-4C6F-95F4-96352515F6A2__TABLE_FED5415922934CDFAE484C031669D51B"><tbody><tr><td><b>Code Region 24-2: Canceling an Event</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CheckProjectStatusInitial</span><span>(</span><span>Object</span><span> sender</span><span>,</span><span> </span><span>DocumentSavingAsEventArgs</span><span> args</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Document</span><span> doc </span><span>=</span><span> args</span><span>.</span><span>Document</span><span>;</span><span>
        </span><span>ProjectInfo</span><span> proInfo </span><span>=</span><span> doc</span><span>.</span><span>ProjectInformation</span><span>;</span><span>

        </span><span>// Project information is only available for project document.</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> proInfo</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>string</span><span>.</span><span>IsNullOrEmpty</span><span>(</span><span>proInfo</span><span>.</span><span>Status</span><span>))</span><span>
                </span><span>{</span><span>

                        </span><span>// cancel the save as process.</span><span>
                        args</span><span>.</span><span>Cancel</span><span>();</span><span>
                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Status project parameter is not set.  Save is aborted."</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: Although most event arguments have the Cancel and Cancellable properties, the DocumentChanged and FailuresProcessing events have corresponding Cancel() and IsCancellable() methods.


<!-- ===== END: Help  Canceling Events  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Export  Autodesk.md ===== -->

---
created: 2026-01-28T21:17:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_html
author: 
---

# Help | Export | Autodesk

> ## Excerpt
> The Revit API allows for a Revit document, or a portion thereof, to be exported to various formats for use with other software. The Document class has an overloaded Export() method that will initiate an export of a document using the built-in exporter in Revit (when available). For more advanced needs, some types of exports can be customized with a Revit add-in, such as export to IFC and export to Navisworks. (Note, Navisworks export is only available as an add-in exporter).

---
The Revit API allows for a Revit document, or a portion thereof, to be exported to various formats for use with other software. The Document class has an overloaded Export() method that will initiate an export of a document using the built-in exporter in Revit (when available). For more advanced needs, some types of exports can be customized with a Revit add-in, such as export to IFC and export to Navisworks. (Note, Navisworks export is only available as an add-in exporter).

The Document.Export() method overloads are outlined in the table below.

**Table: Document.Export() Methods**

<table summary="" id="GUID-A1BE34A2-DA7C-4C2C-9CCB-958A56F1150D__TABLE_EDA7D7AB3C5944EA8D4A0E634918E5E0"><tbody><tr><td><b>Format</b></td><td><b>Export() parameters</b></td><td><b>Comments</b></td></tr><tr><td>gbXML</td><td>String, String, GBXMLExportOptions</td><td>Exports a gbXML file from a mass model document</td></tr><tr><td>gbXML</td><td>String, String, GBXMLExportOptions</td><td>Exports the document in Green-Building XML format. If EnergyDataSettings is set to use conceptual models, this function cannot be used: instead use the method above.</td></tr><tr><td>IFC</td><td>String, String, IFCExportOptions</td><td>Exports the document to the Industry Standard Classes (IFC) format.</td></tr><tr><td>NWC</td><td>String, String, NavisworksExportOptions</td><td>Exports a Revit project to the Navisworks .nwc format. Note that in order to use this function,you must have a compatible Navisworks exporter add-in registered with your session of Revit.</td></tr><tr><td>DWF</td><td>String, String, ViewSet, DWFExportOptions</td><td>Exports the current view or a selection of views in DWF format.</td></tr><tr><td>DWFX</td><td>String, String, ViewSet, DWFXExportOptions</td><td>Exports the current view or a selection of views in DWFX format.</td></tr><tr><td>FBX</td><td>String, String, ViewSet, FBXExportOptions</td><td>Exports the document in 3D-Studio Max (FBX) format.</td></tr><tr><td>DGN</td><td>String, String, ICollection(ElementId), DGNExportOptions</td><td>Exports a selection of views in DGN format.</td></tr><tr><td>DWG</td><td>String, String, ICollection(ElementId), DWGExportOptions</td><td>Exports a selection of views in DWG format.</td></tr><tr><td>DXF</td><td>String, String, ICollection(ElementId), DXFExportOptions</td><td>Exports a selection of views in DXF format.</td></tr><tr><td>SAT</td><td>String, String, ICollection(ElementId), SATExportOptions</td><td>Exports the current view or a selection of views in SAT format.</td></tr><tr><td>PDF</td><td>String, IList(ElementId), PDFExportOptions</td><td>Exports a selection of views in PDF format.</td></tr></tbody></table>

#### Exporting to gbXML

There are two methods for exporting to the Green Building XML format. The one whose last parameter is GBXMLExportOptions is only available for projects containing one or more instances of Conceptual Mass families. The GBXMLExportOptions object to pass into this method can be constructed with just the ids of the mass zones to analyze in the exported gbXML, or with the mass zone ids and the ids of the masses to use as shading surfaces in the exported gbXML. Whe using masses, they must not have mass floors or mass zones so as not to end up with duplicate surface information in the gbXML output.

The GBXMLExportOptions object used for the other gbXML export option has no settings to specify. It uses all default settings. Note that this method does not generate the energy model. The main energy model must already be stored in the document before this export is invoked.

#### Exporting to IFC

Calling Document.Export() using the IFC option will either use the default Revit IFC export implementation or a custom [IFC Export](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_IFC_Export_html), if one has been registered with the current session of Revit. In either case, the IFCExportOptions class is used to set export options such as whether to export IFC standard quantities currently supported by Revit or to allow division of multi-level walls and columns by levels.

#### Exporting to Navisworks

The Export method for Navisworks requires a compatible Navisworks exporter add-in registered with the current Revit session. If there is no compatible exporter registered, the method will throw an exception. Use the OptionalFunctionalityUtils.IsNavisworksExporterAvailable() method to determine if a Navisworks exporter is registered.

The NavisworksExportOptions object can be used to set numerous export settings for exporting to Navisworks, such as whether to divide the file into levels and whether or not to export room geometry. Additionally, the NavisworksExportOptions.ExportScope property specifieds the export scope. The default is Model. Other options include View and SelectedElements. When set to View, the NavisworksExportOptions . ViewId property should be set accordingly. This property is only used when the export scope is set to View. When set to SelectedElements, the NavisworksExportOptions . SetSelectedElementIds() method should be called with the ids of the elements to be exported.

#### Exporting to DWF and DWFX

Both DWF and DWFX files can be exported using the corresponding Document.Export() overloads. Both methods have a ViewSet parameter that represents the views to be exported. All the views in the ViewSet must be printable in order for the export to succeed. This can be checked using the View.CanBePrinted property of each view. The last parameter is either DWFExportOptions or DWFXExportOptions. DWFXExportOptions is derived from DWFExportOptions and has all the same export settings. Options include whether or not to export the crop box, the image quality whether or not to export textures to 3D DWF files, and the paper format.

<table summary="" id="GUID-A1BE34A2-DA7C-4C2C-9CCB-958A56F1150D__TABLE_1BB826B11FB04198B5250D174FFC45D8"><tbody><tr><td><b>Code Region: Export DWF</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>ExportViewToDWF</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>View</span><span> view</span><span>,</span><span> </span><span>string</span><span> pathname</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>DWFExportOptions</span><span> dwfOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>DWFExportOptions</span><span>();</span><span>
    </span><span>// export with crop box and area and room geometry</span><span>
    dwfOptions</span><span>.</span><span>CropBoxVisible</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    dwfOptions</span><span>.</span><span>ExportingAreas</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    dwfOptions</span><span>.</span><span>ExportTexture</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>ViewSet</span><span> views </span><span>=</span><span> </span><span>new</span><span> </span><span>ViewSet</span><span>();</span><span>
    views</span><span>.</span><span>Insert</span><span>(</span><span>view</span><span>);</span><span>
    </span><span>return</span><span> </span><span>(</span><span>document</span><span>.</span><span>Export</span><span>(</span><span>Path</span><span>.</span><span>GetDirectoryName</span><span>(</span><span>pathname</span><span>),</span><span>
        </span><span>Path</span><span>.</span><span>GetFileNameWithoutExtension</span><span>(</span><span>pathname</span><span>),</span><span> views</span><span>,</span><span> dwfOptions</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

#### Exporting to 3D-Studio Max

FBX Export requires the presence of certain modules that are optional and may not be part of the installed Revit, so the OptionalFunctionalityUtils . IsFBXExportAvailable() method reports whether the FBX Export functionality is available. The Export() method for exporting to 3D-Studio Max has a ViewSet parameter representing the set of views to export. Only 3D views are allowed. The FBXExportOptions parameter can be used to specify whether to export without boundary edges, wther to use levels of detail, and whether the export process should stop when a view fails to export.

#### Exporting to CAD Formats

Exporting to DGN , DWG and DXF format files have similar export methods and options.

DGN , DWG and DXF Export all require the presence of certain modules that are optional and may not be part of the installed version of Revit, so the OptionalFunctionalityUtils class as corresponding methods to reports whether the each of these types of export functionality are available.

The Export() methods for exporting to DGN, DWG and DXF formats all have a parameter representing the views to be exported (as an ICollection of the ElementIds of the views). At least one valid view must be present and it must be printable for the export to succeed. This can be checked using the View.CanBePrinted property of each view.

The export options for each of these formats derives from BaseExportOptions, so there are many export settings in common, such as the color mode or whether or not to hide the scope box. BaseExportOptions also has a static method called GetPredefinedSetupNames() which will return any predefined setups for a document. The name of a predefined setup can then be passed into the static method GetPredefinedOptions() available from the corresponding options class: DWGExportOptions, DGNExportOptions or DXFExportOptions. The export options for DWG and DXF files have even more options in common as they share the base class ACADExportOptions.

The following example exports the active view (if it can be printed) to a DGN file using the first predefined setup name and the predefined options, without making any changes.

<table summary="" id="GUID-A1BE34A2-DA7C-4C2C-9CCB-958A56F1150D__TABLE_828E9F5353004D06ACED2092FD80BF66"><tbody><tr><td><b>Code Region: Export DGN</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>ExportDGN</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> exported </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>// Get predefined setups and export the first one</span><span>
    </span><span>IList</span><span>&lt;string&gt;</span><span> setupNames </span><span>=</span><span> </span><span>BaseExportOptions</span><span>.</span><span>GetPredefinedSetupNames</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>setupNames</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Get predefined options for first predefined setup</span><span>
        </span><span>DGNExportOptions</span><span> dgnOptions </span><span>=</span><span> </span><span>DGNExportOptions</span><span>.</span><span>GetPredefinedOptions</span><span>(</span><span>document</span><span>,</span><span> setupNames</span><span>[</span><span>0</span><span>]);</span><span>

        </span><span>// export the active view if it is printable</span><span>
        </span><span>if</span><span> </span><span>(</span><span>document</span><span>.</span><span>ActiveView</span><span>.</span><span>CanBePrinted</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> views </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
            views</span><span>.</span><span>Add</span><span>(</span><span>view</span><span>.</span><span>Id</span><span>);</span><span>
            exported </span><span>=</span><span> document</span><span>.</span><span>Export</span><span>(</span><span>Path</span><span>.</span><span>GetDirectoryName</span><span>(</span><span>document</span><span>.</span><span>PathName</span><span>),</span><span>
                </span><span>Path</span><span>.</span><span>GetFileNameWithoutExtension</span><span>(</span><span>document</span><span>.</span><span>PathName</span><span>),</span><span> views</span><span>,</span><span> dgnOptions</span><span>);</span><span>
        </span><span>}</span><span>
 </span><span>}</span><span>

    </span><span>return</span><span> exported</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

For these file types it is possible to specify or modify various mapping settings, such as layer mapping or text font mapping by creating the corresponding table and passing it into the appropriate method of the BaseExportOptions class. For layer mapping, you may alternatively pass in a string value to BaseExportOptions.LayerMapping of a predefined layer mapping style or the filename of a layer mapping file. For more information on creating or modifying export tables, see the [Export Tables](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_Export_Tables_html) topic.

#### Exporting to SAT

The Export method for SAT has a parameter representing the views to be exported (as an ICollection of the ElementIds of the views). At least one valid view must be present and it must be printable for the export to succeed. This can be checked using the View.CanBePrinted property of each view. The SATExportOptions object has no settings to specify. It uses all default settings.

#### Exporting to Civil Engineering Design Applications

The last Export() method exports a 3D view of the document in the format of Civil Engineering design applications. One parameter of the method is a Viewplan that specifies the gross area plan. All the areas on the view plan will be exported and it must be 'Gross Building' area plan. To check whether its area scheme is Gross Building, use the AreaScheme.GrossBuildingArea property. The BuildingSiteExportOptions object allows custom values for settings such as gross area or total occupancy.

#### Exporting to PDF

**Code Region: Print all sheets to PDF**

```
private void PDFExport(Document doc)
{
    PDFExportOptions opt = new PDFExportOptions();
    opt.Combine = true;
    opt.FileName = "My House";
    opt.PaperFormat = ExportPaperFormat.ARCH_E;
    doc.Export(
        Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
        new FilteredElementCollector(doc)
            .OfClass(typeof(ViewSheet))
            .ToElementIds().ToList(),
        opt);
}
```


<!-- ===== END: Help  Export  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Export Tables  Autodesk.md ===== -->

---
created: 2026-01-28T21:18:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_Export_Tables_html
author: 
---

# Help | Export Tables | Autodesk

> ## Excerpt
> The classes listed in the table below expose read and write access to the tables used for mapping on export to various formats such as DWG and DGN. Each class contains (key, info) pairs of mapping data.

---
The classes listed in the table below expose read and write access to the tables used for mapping on export to various formats such as DWG and DGN. Each class contains (key, info) pairs of mapping data.

<table summary="" id="GUID-0A59F08C-2627-4DA3-AC25-C2BCBDE09ED8__TABLE_E048117C2F884E9F9EB547A4634FE5BD"><tbody><tr><td><b>Class</b></td><td><b>Description</b></td></tr><tr><td>ExportLayerTable</td><td>Represents a table supporting a mapping of various layer properties (Category, name, color name) to layer name in the target export format.</td></tr><tr><td>ExportLinetypeTable</td><td>Represents a table supporting a mapping of linetype names in the target export format.</td></tr><tr><td>ExportPatternTable</td><td>Represents a table supporting a mapping of FillPattern names and ids to FillPattern names in the target export format.</td></tr><tr><td>ExportFontTable</td><td>Represents a table s upporting a mapping of font names in the target export format.</td></tr><tr><td>ExportLineweightTable</td><td>Represents a table s upporting a mapping of lineweight names in the target export format.</td></tr></tbody></table>

Most of these tables are available through the BaseExportOptions class (the base class for options for DGN, DXF and DWG formats). The ExportLineweightTable is available from the DGNExportOptions class. Each table has a corresponding Get and Set method. To modify the mappings, get the corresponding table, make changes and then set it back to the options class.

The following example modifies the ExportLayerTable prior to exporting a DWG file.

<table summary="" id="GUID-0A59F08C-2627-4DA3-AC25-C2BCBDE09ED8__TABLE_FE3D2F55A2C248E4B26C9BB4B63938B4"><tbody><tr><td><b>Code Region: Export DWG with modified ExportLayerTable</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>ExportDWGModifyLayerTable</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> exported </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>IList</span><span>&lt;string&gt;</span><span> setupNames </span><span>=</span><span> </span><span>BaseExportOptions</span><span>.</span><span>GetPredefinedSetupNames</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>setupNames</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Get the export options for the first predefined setup</span><span>
        </span><span>DWGExportOptions</span><span> dwgOptions </span><span>=</span><span> </span><span>DWGExportOptions</span><span>.</span><span>GetPredefinedOptions</span><span>(</span><span>document</span><span>,</span><span> setupNames</span><span>[</span><span>0</span><span>]);</span><span>

        </span><span>// Get the export layer table</span><span>
        </span><span>ExportLayerTable</span><span> layerTable </span><span>=</span><span> dwgOptions</span><span>.</span><span>GetExportLayerTable</span><span>();</span><span>

        </span><span>// Find the first mapping for the Ceilings category</span><span>
        </span><span>string</span><span> category </span><span>=</span><span> </span><span>"Ceilings"</span><span>;</span><span>
        </span><span>ExportLayerKey</span><span> targetKey </span><span>=</span><span> layerTable</span><span>.</span><span>GetKeys</span><span>().</span><span>First</span><span>&lt;</span><span>ExportLayerKey</span><span>&gt;(</span><span>layerKey </span><span>=&gt;</span><span> layerKey</span><span>.</span><span>CategoryName</span><span> </span><span>==</span><span> category</span><span>);</span><span>
        </span><span>ExportLayerInfo</span><span> targetInfo </span><span>=</span><span> layerTable</span><span>[</span><span>targetKey</span><span>];</span><span>

        </span><span>// change the color name and cut color number for this mapping</span><span>
        targetInfo</span><span>.</span><span>ColorName</span><span> </span><span>=</span><span> </span><span>"31"</span><span>;</span><span>
        targetInfo</span><span>.</span><span>CutColorNumber</span><span> </span><span>=</span><span> </span><span>31</span><span>;</span><span>

        </span><span>// Set the change back to the map</span><span>
        layerTable</span><span>[</span><span>targetKey</span><span>]</span><span> </span><span>=</span><span> targetInfo</span><span>;</span><span>

        </span><span>// Set the modified table back to the options</span><span>
        dwgOptions</span><span>.</span><span>SetExportLayerTable</span><span>(</span><span>layerTable</span><span>);</span><span>

        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> views </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
        views</span><span>.</span><span>Add</span><span>(</span><span>view</span><span>.</span><span>Id</span><span>);</span><span>

        exported </span><span>=</span><span> document</span><span>.</span><span>Export</span><span>(</span><span>Path</span><span>.</span><span>GetDirectoryName</span><span>(</span><span>document</span><span>.</span><span>PathName</span><span>),</span><span>
            </span><span>Path</span><span>.</span><span>GetFileNameWithoutExtension</span><span>(</span><span>document</span><span>.</span><span>PathName</span><span>),</span><span> views</span><span>,</span><span> dwgOptions</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> exported</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Export Tables  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  IFC Export  Autodesk.md ===== -->

---
created: 2026-01-28T21:18:08 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_IFC_Export_html
author: 
---

# Help | IFC Export | Autodesk

> ## Excerpt
> Custom IFC Export

---
Custom IFC Export

The Revit API allows custom applications to override the default implementation for the IFC export process.

When an IExporterIFC object is registered with Revit, it will be used both when the user invokes an export to IFC from the UI as well as from the API method Document.Export(String, String, IFCExportOptions). In both cases, if no custom IFC exporter if registered, the default Revit implementation for IFC export is used.

When invoking an IFC export from the API, IFCExportOptions can be used to set the same export options as are available to the user from the Export IFC dialog box.

The functions:

-   IFCImportOptions.GetExtraOptions()
-   IFCImportOptions.SetExtraOptions()

allow for passing in arbitrary options for custom IFC importers. Users can pass in a string to string map specifying extra data they wish to pass for IFC import.

### IExporterIFC

The interface IExporterIFC has only one method to implement, ExportIFC(). This method is invoked by Revit to perform an export to IFC. An ExporterIFC object is passed to this method as one of its parameters. ExporterIFC is the main class provided by Revit to allow implementation of an IFC export. It contains information on the options selected by the user for the export operation, as well as members used to access specific types of data needed to implement the export properly.

The Autodesk.Revit.DB.IFC namespace contains numerous IFC related API classes that can be utilized by a custom implementation of the IFC export process. For a complete sample of a custom IFC export application, see the Open Source example at [http://sourceforge.net/projects/ifcexporter/](http://sourceforge.net/projects/ifcexporter/).


<!-- ===== END: Help  IFC Export  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Custom export  Autodesk.md ===== -->

---
created: 2026-01-28T21:18:13 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_Custom_export_html
author: 
---

# Help | Custom export | Autodesk

> ## Excerpt
> Use a custom export process to export views from a Revit document.

---
Use a custom export process to export views from a Revit document.

The Revit API provides a set of classes that make it possible to export views via a custom export context. These classes provide access to the rendering output pipeline through which Revit sends the graphical representation of a model to an output device. In the case of a custom export, the "device" is represented by a context object that could be any kind of a device. A file would be the most common case.

An implementation of a custom exporter provides a context and invokes rendering of a model, upon which Revit starts processing the model and sends graphic data out via methods of the context. The data describes the model exactly as it would have appeared in Revit when the model is rendered. The data includes all geometry and material properties.

## CustomExporter class

The CustomExporter class allows exporting views via a custom export context. The Export() method of this class triggers the standard rendering process in Revit, but instead of displaying the result on screen or printer, the output is channeled through the given custom context that handles processing the geometric as well as non-geometric information.

### CustomExporter support for 2D views

CustomExporter can export 2D plan, section and elevation views.

The method `CustomExporter.Export(IList<ElementId>)` can accept either 3D or 2D views, with the limitation that views in the collection must be either all 3D or all 2D.

For both Export() calls, the exporter context must correspond to the views' type; use IModelExportContext or IPhotoRenderContext for 3D views and IExportContext2D for 2D views.

Several properties for the CustomExporter exist to support 2D objects:

-   CustomExporter.Export2DGeometricObjectsIncludingPatternLines - Indicates whether pattern lines of geometric objects should be exported in a 2D context. Defaults to false.
-   CustomExporter.Export2DIncludingAnnotationObjects - Indicates whether annotation objects should be exported in a 2D context. Defaults to false.
-   CustomExporter.Export2DForceDisplayStyle - Forces a display style for the export. If the style is DisplayStyle.Undefined, then export uses DisplayStyle.Wireframe for wireframe views and DisplayStyle.HLR for other views. Defaults to DisplayStyle.Undefined.

Use the interface `IExportContext2D` for exporting 2D views. It has the following methods in addition to the method inherited from IExportContext:

-   IExportContext2D.OnElementBegin2D()
-   IExportContext2D.OnElementEnd2D()
-   IExportContext2D.OnFaceEdge2D()
-   IExportContext2D.OnFaceSilhouette2D()

To access data for various 2D exported objects, use the classes:

-   ElementNode
-   FaceEdgeNode
-   FaceSilhouetteNode

Some notes on 2D export in DisplayStyle.Wireframe:

1.  Geometric object methods (OnCurve, OnFaceEdge2D, OnFaceSilhouette2D) are called regardless of the object being eventually output, i.e. even if it is occluded by another element.

And in DisplayStyle.HLR:

1.  Tessellated geometry methods (OnLineSegment and OnPolylineSegments) are called regardless of the return value of the respective geometric object methods (OnCurve, OnFaceEdge2D, OnFaceSilhouette2D).
2.  None of these methods are called between the respective pairs of calls OnInstanceBegin/OnInstanceEnd or OnLinkBegin/OnLinkEnd. They are called between OnElementBegin2D/OnElementEnd2D and OnViewBegin/OnViewEnd.

For an example of the use of the API for custom export of 2D views, see the SDK sample CustomExporter/Custom2DExporter.

### CustomExporter events

Subscribe to these events to be notified when Revit is just about to export, or has just exported, one or more views of the document via an export context by CustomExporter:

-   `Autodesk.Revit.ApplicationServices.Application.ViewsExportingByContext`
-   `Autodesk.Revit.ApplicationServices.Application.ViewsExportedByContext`

`Autodesk.Revit.DB.Events.ViewsExportingByContextEventArg` provides information when Revit is just about to export one or more views of the document via an export context by CustomExporter. It has the method `ViewsExportingByContextEventArgs.GetViewIds()` to get the ids of views about to be exported by CustomExporter.

`Autodesk.Revit.DB.Events.ViewsExportedByContextEventArgs` provides information when Revit has just exported one or more views of the document via an export context by CustomExporter. It has the method `ViewsExportedByContextEventArgs.GetViewIds()` - Gets the ids of views that have been exported by CustomExporter.

## IExportContext

An instance of the IExportContext class is passed in as a parameter of the CustomExporter constructor. The methods of this interface are then called as the entities of the model are exported.

Although it is possible to create classes derived from the IExportContext class, it is preferred to use one of its derived classes: IPhotoRenderContext or IModelExportContext. When using an IPhotoRenderContext to perform a custom export, Revit will traverse the model and output the model's geometry as if processing the Render command invoked via the UI. Only elements that have actual geometry and are suitable to appear in a rendered view will be processed and output.

The IModelExportContext should be used for processing elements in the view in the same manner that Revit processes them in 3D views. This context supports additional elements including model curves and text as shown in the 3D views.

## RenderNode classes

RenderNode is the base class for all output nodes in a model-exporting process. A node can be either geometric (such as an element or light) or non-geometric (such as material). Some types of nodes are container nodes, which include other render nodes.

## CameraInfo

The CameraInfo class describes information about projection mapping of a 3D view to a rendered image. An instance of this class can be obtained via a property of ViewNode. If it is null, an orthographic view should be assumed.


<!-- ===== END: Help  Custom export  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  External Events  Autodesk.md ===== -->

---
created: 2026-01-28T21:18:20 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_External_Events_html
author: 
---

# Help | External Events | Autodesk

> ## Excerpt
> The Revit API provides an External Events framework to accommodate the use of modeless dialogs. It is tailored for asynchronous processing and operates similarly to the Idling event with default frequency.

---
The Revit API provides an External Events framework to accommodate the use of modeless dialogs. It is tailored for asynchronous processing and operates similarly to the Idling event with default frequency.

To implement a modeless dialog using the External Events framework, follow these steps:

1.  Implement an external event handler by deriving from the IExternalEventHandler interface
2.  Create an ExternalEvent using the static ExternalEvent.Create() method
3.  When an event occurs in the modeless dialog where a Revit action needs to be taken, call ExternalEvent.Raise()
4.  Revit will call the implementation of the IExternalEventHandler.Execute() method when there is an available Idling time cycle.
    
    ### IExternalEventHandler
    

This is the interface to be implemented for an external event. An instance of a class implementing this interface is registered with Revit, and every time the corresponding external event is raised, the Execute method of this interface is invoked.

The IExternalEventHandler has only two methods to implement, the Execute() method and GetName() which should return the name of the event. Below is a basic implementation which will display a TaskDialog when the event is raised.

<table summary="" id="GUID-0A0D656E-5C44-49E8-A891-6C29F88E35C0__TABLE_34FBDABFEC644B8EA286FE00A91E78CC"><tbody><tr><td><b>Code Region: Implementing IExternalEventHandler</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>ExternalEventExample</span><span> </span><span>:</span><span> </span><span>IExternalEventHandler</span><span>
</span><span>{</span><span>
    </span><span>public</span><span> </span><span>void</span><span> </span><span>Execute</span><span>(</span><span>UIApplication</span><span> app</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"External Event"</span><span>,</span><span> </span><span>"Click Close to close."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>string</span><span> </span><span>GetName</span><span>()</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> </span><span>"External Event Example"</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### ExternalEvent

The ExternalEvent class is used to create an ExternalEvent. An instance of this class will be returned to an external event's owner upon the event's creation. The event's owner will use this instance to signal that the event should be called by Revit. Revit will periodically check if any of the events have been signaled (raised), and will execute all events that were raised by calling the Execute method on the events' respective handlers.

The following example shows the implementation of an IExternalApplication that has a method ShowForm() that is called from an ExternalCommand (shown at the end of the code region). The ShowForm() method creates a new instance of the external events handler from the example above, creates a new ExternalEvent and then displays the modeless dialog box which will later use the passed in ExternalEvent object to raise events.

<table summary="" id="GUID-0A0D656E-5C44-49E8-A891-6C29F88E35C0__TABLE_9BCB14BA4854427899766E379E9CEA63"><tbody><tr><td><b>Code Region: Create the ExternalEvent</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>ExternalEventExampleApp</span><span> </span><span>:</span><span> </span><span>IExternalApplication</span><span>
</span><span>{</span><span>
    </span><span>// class instance</span><span>
    </span><span>public</span><span> </span><span>static</span><span> </span><span>ExternalEventExampleApp</span><span> thisApp </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>// ModelessForm instance</span><span>
    </span><span>private</span><span> </span><span>ExternalEventExampleDialog</span><span> m_MyForm</span><span>;</span><span>

    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>m_MyForm </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> m_MyForm</span><span>.</span><span>Visible</span><span>)</span><span>
        </span><span>{</span><span>
            m_MyForm</span><span>.</span><span>Close</span><span>();</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        m_MyForm </span><span>=</span><span> </span><span>null</span><span>;</span><span>   </span><span>// no dialog needed yet; the command will bring it</span><span>
        thisApp </span><span>=</span><span> </span><span>this</span><span>;</span><span>  </span><span>// static access to this application instance</span><span>

        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>//   The external command invokes this on the end-user's request</span><span>
    </span><span>public</span><span> </span><span>void</span><span> </span><span>ShowForm</span><span>(</span><span>UIApplication</span><span> uiapp</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// If we do not have a dialog yet, create and show it</span><span>
        </span><span>if</span><span> </span><span>(</span><span>m_MyForm </span><span>==</span><span> </span><span>null</span><span> </span><span>||</span><span> m_MyForm</span><span>.</span><span>IsDisposed</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// A new handler to handle request posting by the dialog</span><span>
            </span><span>ExternalEventExample</span><span> handler </span><span>=</span><span> </span><span>new</span><span> </span><span>ExternalEventExample</span><span>();</span><span>

            </span><span>// External Event for the dialog to use (to post requests)</span><span>
            </span><span>ExternalEvent</span><span> exEvent </span><span>=</span><span> </span><span>ExternalEvent</span><span>.</span><span>Create</span><span>(</span><span>handler</span><span>);</span><span>

            </span><span>// We give the objects to the new dialog;</span><span>
            </span><span>// The dialog becomes the owner responsible for disposing them, eventually.</span><span>
            m_MyForm </span><span>=</span><span> </span><span>new</span><span> </span><span>ExternalEventExampleDialog</span><span>(</span><span>exEvent</span><span>,</span><span> handler</span><span>);</span><span>
            m_MyForm</span><span>.</span><span>Show</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>[</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>Transaction</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>Manual</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>Command</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
    </span><span>public</span><span> </span><span>virtual</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>try</span><span>
        </span><span>{</span><span>
            </span><span>ExternalEventExampleApp</span><span>.</span><span>thisApp</span><span>.</span><span>ShowForm</span><span>(</span><span>commandData</span><span>.</span><span>Application</span><span>);</span><span>
            </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span> ex</span><span>)</span><span>
        </span><span>{</span><span>
            message </span><span>=</span><span> ex</span><span>.</span><span>Message</span><span>;</span><span>
            </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Raise Event

Once the modeless dialog is displayed, the user may interact with it. Actions in the dialog may need to trigger some action in Revit. When this happens, the ExternalEvent.Raise() method is called. The following example is the code for a simple modeless dialog with two buttons: one to raise our event and one to close the dialog.

<table summary="" id="GUID-0A0D656E-5C44-49E8-A891-6C29F88E35C0__TABLE_F02CB5FDB6DF4F9EB41A1DE944176998"><tbody><tr><td><b>Code Region: Raise the Event</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>partial</span><span> </span><span>class</span><span> </span><span>ExternalEventExampleDialog</span><span> </span><span>:</span><span> </span><span>Form</span><span>
</span><span>{</span><span>
    </span><span>private</span><span> </span><span>ExternalEvent</span><span> m_ExEvent</span><span>;</span><span>
    </span><span>private</span><span> </span><span>ExternalEventExample</span><span> m_Handler</span><span>;</span><span>

    </span><span>public</span><span> </span><span>ExternalEventExampleDialog</span><span>(</span><span>ExternalEvent</span><span> exEvent</span><span>,</span><span> </span><span>ExternalEventExample</span><span> handler</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>InitializeComponent</span><span>();</span><span>
        m_ExEvent </span><span>=</span><span> exEvent</span><span>;</span><span>
        m_Handler </span><span>=</span><span> handler</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>protected</span><span> </span><span>override</span><span> </span><span>void</span><span> </span><span>OnFormClosed</span><span>(</span><span>FormClosedEventArgs</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// we own both the event and the handler</span><span>
        </span><span>// we should dispose it before we are closed</span><span>
        m_ExEvent</span><span>.</span><span>Dispose</span><span>();</span><span>
        m_ExEvent </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        m_Handler </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>// do not forget to call the base class</span><span>
        </span><span>base</span><span>.</span><span>OnFormClosed</span><span>(</span><span>e</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>private</span><span> </span><span>void</span><span> closeButton_Click</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>EventArgs</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Close</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>private</span><span> </span><span>void</span><span> showMessageButton_Click</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>EventArgs</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        m_ExEvent</span><span>.</span><span>Raise</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

When the ExternalEvent.Raise() method is called, Revit will wait for an available Idling timecycle and then call the IExternalEventHandler.Execute() method. In this simple example, it will display a TaskDialog with the text "Click Close to close." as shown in the first code region above.

For a more complex example of using the External Events framework, see the sample code in the SDK under the ModelessDialog\\ModelessForm\_ExternalEvent folder. It uses a modeless dialog with numerous buttons and the IExternalEventHandler implementation has a public property to track which button was pressed so it can switch on that value in the Execute() method.


<!-- ===== END: Help  External Events  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Failure Posting and Handling  Autodesk.md ===== -->

---
created: 2026-01-28T21:18:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Failure_Posting_and_Handling_html
author: 
---

# Help | Failure Posting and Handling | Autodesk

> ## Excerpt
> Share

---
Share

The Revit API provides the ability to post failures when a user-visible problem has occurred and to respond to failures posted by Revit or Revit add-ins.

**Pages in this section**

-   [Posting Failures](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Failure_Posting_and_Handling_Posting_Failures_html)
-   [Handling Failures](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Failure_Posting_and_Handling_Handling_Failures_html)

**Parent page:** [Advanced Topics](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_html)

### Was this information helpful?

-   Yes
-   No


<!-- ===== END: Help  Failure Posting and Handling  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Posting Failures  Autodesk.md ===== -->

---
created: 2026-01-28T21:18:28 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Failure_Posting_and_Handling_Posting_Failures_html
author: 
---

# Help | Posting Failures | Autodesk

> ## Excerpt
> To use the failure posting mechanism to report problems, the following steps are required:

---
To use the failure posting mechanism to report problems, the following steps are required:

1.  New failures not already defined in Revit must be defined and registered in the FailureDefinitionRegistry during the OnStartup() call of the ExternalApplication.
2.  Find the failure definition id, either from the BuiltInFailures classes or from the pre-registered custom failures using the class related to FailureDefinition.
3.  Post the failure to the document that has a problem using the classes related to FailureMessage to set options and details related to the failure.
    
    ### Defining and registering a failure
    

Each possible failure in Revit must be defined and registered during Revit application startup by creating a FailureDefinition object that contains some persistent information about the failure such as identity, severity, basic description, types of resolution and default resolution.

The following example creates two new failures, a warning and an error, that can be used for walls that are too tall. In this example, they are used in conjunction with an Updater that will do the failure posting (in a subsequent code sample in this chapter). The FailureDefinitionIds are saved in the Updater class since they will be required when posting failures. The sections following explain the FailureDefinition.CreateFailureDefinition() method parameters in more detail.

<table summary="" id="GUID-8AE4ADAF-82AB-4AC1-81A2-7A8DD9346055__TABLE_A909459E77B3435CBD87D86E1D7F66BD"><tbody><tr><td><b>Code Region 26-1: Defining and registering a failure</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>PostWallFailure</span><span>()</span><span>
</span><span>{</span><span>
    </span><span>WallWarnUpdater</span><span> wallUpdater </span><span>=</span><span> </span><span>new</span><span> </span><span>WallWarnUpdater</span><span>(</span><span>new</span><span> </span><span>AddInId</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"F0F045A5-06E8-4C89-837D-8A8F85484953"</span><span>)));</span><span>
    </span><span>UpdaterRegistry</span><span>.</span><span>RegisterUpdater</span><span>(</span><span>wallUpdater</span><span>);</span><span>
    </span><span>ElementClassFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>Wall</span><span>));</span><span>
    </span><span>UpdaterRegistry</span><span>.</span><span>AddTrigger</span><span>(</span><span>wallUpdater</span><span>.</span><span>GetUpdaterId</span><span>(),</span><span> filter</span><span>,</span><span> </span><span>Element</span><span>.</span><span>GetChangeTypeGeometry</span><span>());</span><span>

    </span><span>// define a new failure id for a warning about walls</span><span>
    </span><span>FailureDefinitionId</span><span> warnId </span><span>=</span><span> </span><span>new</span><span> </span><span>FailureDefinitionId</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"FB4F5AF3-42BB-4371-B559-FB1648D5B4D1"</span><span>));</span><span>

    </span><span>// register the new warning using FailureDefinition</span><span>
    </span><span>FailureDefinition</span><span> failDef </span><span>=</span><span> </span><span>FailureDefinition</span><span>.</span><span>CreateFailureDefinition</span><span>(</span><span>warnId</span><span>,</span><span> </span><span>FailureSeverity</span><span>.</span><span>Warning</span><span>,</span><span> </span><span>"Wall is too big (&gt;100'). Performance problems may result."</span><span>);</span><span>

    </span><span>FailureDefinitionId</span><span> failId </span><span>=</span><span> </span><span>new</span><span> </span><span>FailureDefinitionId</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"691E5825-93DC-4f5c-9290-8072A4B631BC"</span><span>));</span><span>

    </span><span>FailureDefinition</span><span> failDefError </span><span>=</span><span> </span><span>FailureDefinition</span><span>.</span><span>CreateFailureDefinition</span><span>(</span><span>failId</span><span>,</span><span> </span><span>FailureSeverity</span><span>.</span><span>Error</span><span>,</span><span> </span><span>"Wall is WAY too big (&gt;200'). Performance problems may result."</span><span>);</span><span>
    </span><span>// save ids for later reference</span><span>
    wallUpdater</span><span>.</span><span>WarnId</span><span> </span><span>=</span><span> warnId</span><span>;</span><span>
    wallUpdater</span><span>.</span><span>FailureId</span><span> </span><span>=</span><span> failId</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

#### FailureDefinitionId

A unique FailureDefinitionId must be used as a key to register the FailureDefinition. Each unique FailureDefinitionId should be created using a GUID generation tool. Later, the FailureDefinitionId can be used to look up a FailureDefinition in FailureDefinitionRegistry, and to create and post FailureMessages.

#### Severity

When registering a new failure, a severity is specified, along with the FailureDefinitionId and a text description of the failure that can be displayed to the user. The severity determines what actions are allowed in a document and whether the transaction can be committed at all. The severity options are:

-   _**Warning**_ - Failure that can be ignored by end-user. Failures of this severity do not prevent transactions from being committed. This severity should be used when Revit needs to communicate a problem to the user, but the problem does not prevent the user from continuing to work on the document
-   _**Error**_ - Failure that cannot be ignored. If FailureMeassage of this severity is posted, the current transaction cannot be committed unless the failure is resolved via an appropriate FailureResolution. This severity should be used when work on the document cannot be continued unless the problem is resolved. If the failure has no predefined resolutions available or these resolutions fail to resolve the problem, the transaction must be aborted in order to continue working with the document. It is strongly encouraged to have at least one resolution in each failure of this severity.
-   _**DocumentCorruption**_ - Failure that forces the Transaction to be rolled back as soon as possible due to known corruption to a document. When failure of this severity is posted, reading of information from a document is not allowed. The current transaction must be rolled back first in order to work with the document. This severity is used only if there is known data corruption in the document. This type of failure should generally be avoided unless there is no way to prevent corruption or to recover from it locally.

A fourth severity, None, cannot be specified when defining a new FailureDefinition.

#### Failure Resolutions

When a failure can be resolved, all possible resolutions should be predefined in the FailureDefinition class. This informs Revit what failure resolutions can possibly be used with a given failure. The FailureDefinition contains a full list of resolution types applicable to the failure, including a user-visible caption of the resolution.

The number of resolutions is not limited, however as of the 2011 Revit API, the only exposed failure resolution is DeleteElements. When more than one resolution is specified, unless explicitly changed using the SetDefaultResolutionType() method, the first resolution added becomes the default resolution. The default resolution is used by the Revit failure processing mechanism to resolve failures automatically when applicable. The Revit UI only uses the default resolution, but Revit add-ins, via the Revit API, can use any applicable resolution, and can provide an alternative UI for doing that (as described in the Handling Failures section later in this chapter).

In the case of a failure with a severity of DocumentCorruption, by the time failure resolution could occur, the transaction is already aborted, so there is nothing to resolve. Therefore, FailureResolutions should not be added to API-defined Failures of severity DocumentCorruption.

### Posting a failure

The Document.PostFailure() method is used to notify the document of a problem. Failures will be validated and possibly resolved at the end of the transaction. Warnings posted via this method will not be stored in the document after they are resolved. Failure posting is used to address a state of the document which may change before the end of the transaction or when it makes sense to defer resolution until the end of the transaction. Not all failures encountered by an external command should post a failure. If the failure is unrelated to the document, a task dialog should be used. For example, if the Revit UI is in an invalid state to perform the external command.

To post a failure, create a new FailureMessage using the FailureDefinitionId from when the custom failure was defined, or use a BuiltInFailure provided by the Revit API. Set any additional information in the FailureMessage object, such as failing elements, and then call Document.PostFailure() passing in the new FailureMessage. Note that the document must be modifiable in order to post a failure.

A unique FailureMessageKey returned by PostFailure() can be stored for the lifetime of transaction and used to remove a failure message if it is no longer relevant. If the same FailureMessage is posted two or more times, the same FailureMessageKey is returned. If a posted failure has a severity of DocumentCorruption, an invalid FailureMessageKey is returned. This is because a DocumentCorruption failure cannot be unposted.

The following example shows an IUpdate class (referenced in the "Defining and registering a failure" code region above) that posts a new failure based on information received in the Execute() method.

<table summary="" id="GUID-8AE4ADAF-82AB-4AC1-81A2-7A8DD9346055__TABLE_86A7525484AB46A4BAD38F3382665A9C"><tbody><tr><td><b>Code Region 26-2: Posting a failure</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>WallWarnUpdater</span><span> </span><span>:</span><span> </span><span>IUpdater</span><span>
</span><span>{</span><span>
    </span><span>static</span><span> </span><span>AddInId</span><span> m_appId</span><span>;</span><span>
    </span><span>UpdaterId</span><span> m_updaterId</span><span>;</span><span>
    </span><span>FailureDefinitionId</span><span> m_failureId </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>FailureDefinitionId</span><span> m_warnId </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// constructor takes the AddInId for the add-in associated with this updater</span><span>
    </span><span>public</span><span> </span><span>WallWarnUpdater</span><span>(</span><span>AddInId</span><span> id</span><span>)</span><span>
    </span><span>{</span><span>
        m_appId </span><span>=</span><span> id</span><span>;</span><span>
        m_updaterId </span><span>=</span><span> </span><span>new</span><span> </span><span>UpdaterId</span><span>(</span><span>m_appId</span><span>,</span><span> 
            </span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"69797663-7BCB-44f9-B756-E4189FE0DED8"</span><span>));</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>void</span><span> </span><span>Execute</span><span>(</span><span>UpdaterData</span><span> data</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Document</span><span> doc </span><span>=</span><span> data</span><span>.</span><span>GetDocument</span><span>();</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span> doc</span><span>.</span><span>Application</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> data</span><span>.</span><span>GetModifiedElementIds</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>Wall</span><span> wall </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>Wall</span><span>;</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Parameter</span><span> p </span><span>=</span><span> wall</span><span>.</span><span>LookupParameter</span><span>(</span><span>"Unconnected Height"</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>p </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>p</span><span>.</span><span>AsDouble</span><span>()</span><span> </span><span>&gt;</span><span> </span><span>200</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>FailureMessage</span><span> failMessage </span><span>=</span><span> </span><span>new</span><span> </span><span>FailureMessage</span><span>(</span><span>FailureId</span><span>);</span><span>
                    failMessage</span><span>.</span><span>SetFailingElement</span><span>(</span><span>id</span><span>);</span><span>
                    doc</span><span>.</span><span>PostFailure</span><span>(</span><span>failMessage</span><span>);</span><span>
                </span><span>}</span><span>
                </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>p</span><span>.</span><span>AsDouble</span><span>()</span><span> </span><span>&gt;</span><span> </span><span>100</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>FailureMessage</span><span> failMessage </span><span>=</span><span> </span><span>new</span><span> </span><span>FailureMessage</span><span>(</span><span>WarnId</span><span>);</span><span>
                    failMessage</span><span>.</span><span>SetFailingElement</span><span>(</span><span>id</span><span>);</span><span>
                    doc</span><span>.</span><span>PostFailure</span><span>(</span><span>failMessage</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>FailureDefinitionId</span><span> </span><span>FailureId</span><span>
    </span><span>{</span><span>
        </span><span>get</span><span> </span><span>{</span><span> </span><span>return</span><span> m_failureId</span><span>;</span><span> </span><span>}</span><span>
        </span><span>set</span><span> </span><span>{</span><span> m_failureId </span><span>=</span><span> value</span><span>;</span><span> </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>FailureDefinitionId</span><span> </span><span>WarnId</span><span>
    </span><span>{</span><span>
        </span><span>get</span><span> </span><span>{</span><span> </span><span>return</span><span> m_warnId</span><span>;</span><span> </span><span>}</span><span>
        </span><span>set</span><span> </span><span>{</span><span> m_warnId </span><span>=</span><span> value</span><span>;</span><span> </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>string</span><span> </span><span>GetAdditionalInformation</span><span>()</span><span> 
    </span><span>{</span><span> 
        </span><span>return</span><span> </span><span>"Give warning and error if wall is too tall"</span><span>;</span><span> 
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>ChangePriority</span><span> </span><span>GetChangePriority</span><span>()</span><span> 
    </span><span>{</span><span> 
        </span><span>return</span><span> </span><span>ChangePriority</span><span>.</span><span>FloorsRoofsStructuralWalls</span><span>;</span><span> 
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>UpdaterId</span><span> </span><span>GetUpdaterId</span><span>()</span><span> 
    </span><span>{</span><span> 
        </span><span>return</span><span> m_updaterId</span><span>;</span><span> 
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>string</span><span> </span><span>GetUpdaterName</span><span>()</span><span> 
    </span><span>{</span><span> 
        </span><span>return</span><span> </span><span>"Wall Height Check"</span><span>;</span><span> 
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Removal of posted failures

Because there may be multiple changes to a document and multiple regenerations in the same transaction, it is possible that some failures are no longer relevant and they may need to be removed to prevent "false alarms". Specific messages can be un-posted by calling the Document.UnpostFailure() method and passing in the FailureMessageKey obtained when PostFailure() was called. UnpostFailure() will throw an exception if the severity of the failure is DocumentCorruption.

It is also possible to automatically remove all posted failures when a transaction is about to be rolled back (so that the user is not bothered to hit Cancel) by using the Transaction.SetFailureHandlingOptions() method.


<!-- ===== END: Help  Posting Failures  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Handling Failures  Autodesk.md ===== -->

---
created: 2026-01-28T21:18:32 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Failure_Posting_and_Handling_Handling_Failures_html
author: 
---

# Help | Handling Failures | Autodesk

> ## Excerpt
> Normally posted failures are processed by Revit's standard failure resolution UI at the end of a transaction (specifically when Transaction.Commit() or Transaction.Rollback() are invoked). The user is presented information and options to deal with the failures.

---
Normally posted failures are processed by Revit's standard failure resolution UI at the end of a transaction (specifically when Transaction.Commit() or Transaction.Rollback() are invoked). The user is presented information and options to deal with the failures.

If an operation (or set of operations) on the document requires some special treatment from a Revit add-in for certain errors, failure handling can be customized to carry out this resolution. Custom failure handling can be supplied:

-   For a given transaction using the interface IFailuresPreprocessor.
-   For all possible errors using the FailuresProcessing event.

Finally, the API offers the ability to completely replace the standard failure processing user interface using the interface IFailuresProcessor. Although the first two methods for handling failures should be sufficient in most cases, this last option can be used in special cases, such as to provide a better failure processing UI or when an application is used as a front-end on top of Revit.

### Overview of Failure Processing

It is important to remember there are many things happening between the call to Transaction.Commit() and the actual processing of failures. Auto-join, overlap checks, group checks and workset editability checks are just to name a few. These checks and changes may make some failures disappear or, more likely, can post new failures. Therefore, conclusions cannot be drawn about the state of failures to be processed when Transaction.Commit() is called. To process failures correctly, it is necessary to hook up to the actual failures processing mechanism.

When failures processing begins, all changes to a document that are supposed to be made in the transaction are made, and all failures are posted. Therefore, no uncontrolled changes to a document are allowed during failures processing. There is a limited ability to resolve failures via the restricted interface provided by FailuresAccessor. If this has happened, all end of transaction checks and failures processing have to be repeated. So there may be a few failure resolution cycles at the end of one transaction.

Each cycle of failures processing includes 3 steps:

1.  Preprocessing of failures (FailuresPreprocessor)
2.  Broadcasting of failures processing event (FailuresProcessing event)
3.  Final processing (FailuresProcessor)

Each of these 3 steps can control what happens next by returning different FailureProcessingResults. The options are:

-   _**Continue**_ - has no impact on execution flow. If FailuresProcessor returns "Continue" with unresolved failures, Revit will instead act as if "ProceedWithRollBack" was returned.
-   _**ProceedWithCommit**_ - interrupts failures processing and immediately triggers another loop of end-of-transaction checks followed by another failures processing. Should be returned after an attempt to resolve failures. Can easily lead to an infinite loop if returned without any successful failure resolution. Cannot be returned if transaction is already being rolled back and will be treated as "ProceedWithRollBack" in this case.
-   _**ProceedWithRollback**_ - continues execution of failure processing, but forces transaction to be rolled back, even if it was originally requested to commit. If before ProceedWithRollBack is returned FailureHandlingOptions are set to clear errors after rollback, no further error processing will take place, all failures will be deleted and transaction is rolled back silently. Otherwise default failure processing will continue, failures may be delivered to the user, but transaction is guaranteed to be rolled back.
-   _**WaitForUserInput**_ - Can be returned only by FailuresProcessor if it is waiting for an external event (typically user input) to complete failures processing.

Depending on the severity of failures posted in the transaction and whether the transaction is being committed or rolled back, each of these 3 steps may have certain options to resolve errors. All information about failures posted in a document, information about ability to perform certain operations to resolve failures and API to perform such operations are provided via the FailuresAccessor class. The Document can be used to obtain additional information, but it cannot be changed other than via FailuresAccessor.

### FailuresAccessor

A FailuresAccessor object is passed to each of failure processing steps as an argument and is the only available interface to fetch information about failures in a document. While reading from a document during failure processing is allowed, the only way to modify a document during failure resolution is via methods provided by this class. After returning from failure processing, the instance of the class is deactivated and cannot be used any longer.

#### Information Available from FailuresAccessor

The FailuresAccessor object offers some generic information such as:

-   Document for which failures are being processed or preprocessed
-   Highest severity of failures posted in the document
-   Transaction name and failure handling options for transaction being finished
-   Whether transaction was requested to be committed or rolled back.

The FailuresAccessor object also offers information about specific failures via the GetFailuresMessages() method.

#### Options to resolve failures

The FailuresAccessor object provides a few ways to resolve failures:

-   Failure messages with a severity of Warning can be deleted with the DeleteWarning() or DeleteAllWarnings() methods.
-   ResolveFailure() or ResolveFailures() methods can be used to resolve one or more failures using the last failure resolution type set for each failure.
-   DeleteElements() can resolve failures by deleting elements related to the failure.
-   Or delete all failure messages and replace them with one "generic" failure using the ReplaceFailures() method.
    
    ### IFailuresPreprocessor
    

The IFailuresPreprocessor interface can be used to provide custom failure handling for a specific transaction only. IFailuresPreprocessor is an interface that may be used to perform a preprocessing step to either filter out anticipated transaction failures or to post new failures. Failures can be "filtered out" by:

-   silently removing warnings that are known to be posted for the transaction and are deemed as irrelevant for the user in the context of a particular transaction
-   silently resolving certain failures that are known to be posted for the transaction and that should always be resolved in a context of a given transaction
-   silently aborting the transaction in cases where "imperfect" transactions should not be committed or aborting the transaction is preferable over user interaction for a given workflow.

The IFailuresPreprocessor interface gets control first during the failure resolution process. It is nearly equivalent to checking and resolving failures before finishing a transaction, except that IFailuresPreprocessor gets control at the right time, after all failures guaranteed to be posted and/or after all irrelevant ones are deleted.

There may be only one IFailuresPreprocessor per transaction and there is no default failure preprocessor. If one is not attached to the transaction (via the failure handling options), this first step of failure resolution is simply omitted.

<table summary="" id="GUID-52A45CC1-3BB4-48B4-BFC7-F6F8666C2AA4__TABLE_02F7FD0C66BF48ADAC64D7C8D87D43A4"><tbody><tr><td><b>Code Region 26-3: Handling failures from IFailuresPreprocessor</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>SwallowTransactionWarning</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span>
                        commandData</span><span>.</span><span>Application</span><span>.</span><span>Application</span><span>;</span><span>
                </span><span>Document</span><span> doc </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>
                </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>;</span><span>

                </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
                </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> elementCollection </span><span>=</span><span>
                        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Level</span><span>)).</span><span>ToElements</span><span>();</span><span>
                </span><span>Level</span><span> level </span><span>=</span><span> elementCollection</span><span>.</span><span>Cast</span><span>&lt;</span><span>Level</span><span>&gt;().</span><span>ElementAt</span><span>&lt;</span><span>Level</span><span>&gt;(</span><span>0</span><span>);</span><span>

                </span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>);</span><span>
                t</span><span>.</span><span>Start</span><span>(</span><span>"room"</span><span>);</span><span>
                </span><span>FailureHandlingOptions</span><span> failOpt </span><span>=</span><span> t</span><span>.</span><span>GetFailureHandlingOptions</span><span>();</span><span>
                failOpt</span><span>.</span><span>SetFailuresPreprocessor</span><span>(</span><span>new</span><span> </span><span>RoomWarningSwallower</span><span>());</span><span>
                t</span><span>.</span><span>SetFailureHandlingOptions</span><span>(</span><span>failOpt</span><span>);</span><span>

                doc</span><span>.</span><span>Create</span><span>.</span><span>NewRoom</span><span>(</span><span>level</span><span>,</span><span> </span><span>new</span><span> UV</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>
                t</span><span>.</span><span>Commit</span><span>();</span><span>

                </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>RoomWarningSwallower</span><span> </span><span>:</span><span> </span><span>IFailuresPreprocessor</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>FailureProcessingResult</span><span> </span><span>PreprocessFailures</span><span>(</span><span>FailuresAccessor</span><span> failuresAccessor</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>IList</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;</span><span> failList </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;();</span><span>
                </span><span>// Inside event handler, get all warnings</span><span>
                failList </span><span>=</span><span> failuresAccessor</span><span>.</span><span>GetFailureMessages</span><span>();</span><span>        
                </span><span>foreach</span><span> </span><span>(</span><span>FailureMessageAccessor</span><span> failure </span><span>in</span><span> failList</span><span>)</span><span>
                </span><span>{</span><span> 
                        </span><span>// check FailureDefinitionIds against ones that you want to dismiss,</span><span>
                        </span><span>FailureDefinitionId</span><span> failID </span><span>=</span><span> failure</span><span>.</span><span>GetFailureDefinitionId</span><span>();</span><span>
                        </span><span>// prevent Revit from showing Unenclosed room warnings</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>failID </span><span>==</span><span> </span><span>BuiltInFailures</span><span>.</span><span>RoomFailures</span><span>.</span><span>RoomNotEnclosed</span><span>)</span><span>
                        </span><span>{</span><span>
                                failuresAccessor</span><span>.</span><span>DeleteWarning</span><span>(</span><span>failure</span><span>);</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>

                </span><span>return</span><span> </span><span>FailureProcessingResult</span><span>.</span><span>Continue</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### FailuresProcessing Event

The FailuresProcessing event is most suitable for applications that want to provide custom failure handling without a user interface, either for the entire session or for many unrelated transactions. Some use cases for handling failures via this event are:

-   automatic removal of certain warnings and/or automatic resolving of certain errors based on office standards (or other criteria)
-   custom logging of failures

The FailuresProcessing event is raised after IFailuresPreprocessor (if any) has finished. It can have any number of handlers, and all of them will be invoked. Since event handlers have no way to return a value, the SetProcessingResult() on the event argument should be used to communicate status. Only Continue, ProceedWithRollback or ProceedWithCommit can be set.

The following example shows an event handler for the FailuresProcessing event.

<table summary="" id="GUID-52A45CC1-3BB4-48B4-BFC7-F6F8666C2AA4__TABLE_B81CB6C364F64D78936118530C4EF8F2"><tbody><tr><td><b>Code Region 26-4: Handling the FailuresProcessing Event</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CheckWarnings</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>FailuresProcessingEventArgs</span><span> e</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>FailuresAccessor</span><span> fa </span><span>=</span><span> e</span><span>.</span><span>GetFailuresAccessor</span><span>();</span><span>
        </span><span>IList</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;</span><span> failList </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;();</span><span>
        failList </span><span>=</span><span> fa</span><span>.</span><span>GetFailureMessages</span><span>();</span><span> </span><span>// Inside event handler, get all warnings</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>FailureMessageAccessor</span><span> failure </span><span>in</span><span> failList</span><span>)</span><span>
        </span><span>{</span><span> 
                </span><span>// check FailureDefinitionIds against ones that you want to dismiss,</span><span>
                </span><span>FailureDefinitionId</span><span> failID </span><span>=</span><span> failure</span><span>.</span><span>GetFailureDefinitionId</span><span>();</span><span>
                </span><span>// prevent Revit from showing Unenclosed room warnings</span><span>
                </span><span>if</span><span> </span><span>(</span><span>failID </span><span>==</span><span> </span><span>BuiltInFailures</span><span>.</span><span>RoomFailures</span><span>.</span><span>RoomNotEnclosed</span><span>)</span><span>
                </span><span>{</span><span>
                        fa</span><span>.</span><span>DeleteWarning</span><span>(</span><span>failure</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### FailuresProcessor

The IFailuresProcessor interface gets control last, after the FailuresProcessing event is processed. There is only one active IFailuresProcessor in a Revit session. To register a failures processor, derive a class from IFailuresProcessor and register it using the Application.RegisterFailuresProcessor() method. If there is previously registered failures processor, it is discarded. If a Revit add-in opts to register a failures processor for Revit that processor will become the default error handler for all Revit errors for the session and the standard Revit error dialog will not appear. If no failures processors are set, there is a default one in the Revit UI that invokes all regular Revit error dialogs. FailuresProcessor should only be overridden to replace the existing Revit failure UI with a custom failure resolution handler, which can be interactive or have no user interface.

If the RegisterFailuresProcessor() method is passed NULL, any transaction that has any failures is silently aborted (unless failures are resolved by first two steps of failures processing).

The IFailuresProcessor.ProcessFailures() method is allowed to return WaitForUserInput, which leaves the transaction pending. It is expected that in this case, FailuresProcessor leaves some UI on the screen that will eventually commit or rollback a pending transaction - otherwise the pending state will last indefinitely, essentially freezing the document.

The following example of implementing the IFailuresProcessor checks for a failure, deletes the failing elements and sets an appropriate message for the user.

<table summary="" id="GUID-52A45CC1-3BB4-48B4-BFC7-F6F8666C2AA4__TABLE_0C94C835C36D4E2C9FE8AA01C8DED3B3"><tbody><tr><td><b>Code Region 26-5: IFailuresProcessor</b></td></tr><tr><td><pre><code><span>[</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>Transaction</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>Manual</span><span>)]</span><span>   
</span><span>public</span><span> </span><span>class</span><span> </span><span>MyFailuresUI</span><span> </span><span>:</span><span> </span><span>IExternalApplication</span><span>
</span><span>{</span><span>
        </span><span>static</span><span> </span><span>AddInId</span><span> m_appId </span><span>=</span><span> </span><span>new</span><span> </span><span>AddInId</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"9F179363-B349-4541-823F-A2DDB2B86AF3"</span><span>));</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>UIControlledApplication</span><span> uiControlledApplication</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>IFailuresProcessor</span><span> myFailUI </span><span>=</span><span> </span><span>new</span><span> </span><span>FailUI</span><span>();</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span>.</span><span>RegisterFailuresProcessor</span><span>(</span><span>myFailUI</span><span>);</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>class</span><span> </span><span>FailUI</span><span> </span><span>:</span><span> </span><span>IFailuresProcessor</span><span>
        </span><span>{</span><span>
                </span><span>public</span><span> </span><span>void</span><span> </span><span>Dismiss</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>// This method is being called in case of exception or document destruction to </span><span>
                        </span><span>// dismiss any possible pending failure UI that may have left on the screen</span><span>
                </span><span>}</span><span>

                </span><span>public</span><span> </span><span>FailureProcessingResult</span><span> </span><span>ProcessFailures</span><span>(</span><span>FailuresAccessor</span><span> failuresAccessor</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>IList</span><span>&lt;</span><span>FailureResolutionType</span><span>&gt;</span><span> resolutionTypeList </span><span>=</span><span>
                                </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FailureResolutionType</span><span>&gt;();</span><span> 
                        </span><span>IList</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;</span><span> failList </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;();</span><span>
                        </span><span>// Inside event handler, get all warnings</span><span>
                        failList </span><span>=</span><span> failuresAccessor</span><span>.</span><span>GetFailureMessages</span><span>();</span><span> 
                        </span><span>string</span><span> errorString </span><span>=</span><span> </span><span>""</span><span>;</span><span>
                        </span><span>bool</span><span> hasFailures </span><span>=</span><span> </span><span>false</span><span>;</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>FailureMessageAccessor</span><span> failure </span><span>in</span><span> failList</span><span>)</span><span>
                        </span><span>{</span><span>

                                </span><span>// check how many resolutions types were attempted to try to prevent</span><span>
                                </span><span>// entering infinite loop</span><span>
                                resolutionTypeList </span><span>=</span><span> 
                                        failuresAccessor</span><span>.</span><span>GetAttemptedResolutionTypes</span><span>(</span><span>failure</span><span>);</span><span>
                                </span><span>if</span><span> </span><span>(</span><span>resolutionTypeList</span><span>.</span><span>Count</span><span> </span><span>&gt;=</span><span> </span><span>3</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Cannot resolve failures - transaction will be rolled back."</span><span>);</span><span>
                                        </span><span>return</span><span> </span><span>FailureProcessingResult</span><span>.</span><span>ProceedWithRollBack</span><span>;</span><span>
                                </span><span>}</span><span>

                                errorString </span><span>+=</span><span> </span><span>"IDs "</span><span>;</span><span>
                                </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> failure</span><span>.</span><span>GetFailingElementIds</span><span>())</span><span>
                                </span><span>{</span><span>
                                        errorString </span><span>+=</span><span> id </span><span>+</span><span> </span><span>", "</span><span>;</span><span>
                                        hasFailures </span><span>=</span><span> </span><span>true</span><span>;</span><span>
                                </span><span>}</span><span>
                                errorString </span><span>+=</span><span> </span><span>"\nWill be deleted because: "</span><span> </span><span>+</span><span> failure</span><span>.</span><span>GetDescriptionText</span><span>()</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
                                failuresAccessor</span><span>.</span><span>DeleteElements</span><span>(</span><span>
                                                        failure</span><span>.</span><span>GetFailingElementIds</span><span>()</span><span> </span><span>as</span><span> </span><span>IList</span><span>&lt;</span><span>ElementId</span><span>&gt;);</span><span>
                        </span><span>}</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>hasFailures</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> errorString</span><span>);</span><span>
                                </span><span>return</span><span> </span><span>FailureProcessingResult</span><span>.</span><span>ProceedWithCommit</span><span>;</span><span>
                        </span><span>}</span><span>

                        </span><span>return</span><span> </span><span>FailureProcessingResult</span><span>.</span><span>Continue</span><span>;</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Handling Failures  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Linked Files  Autodesk.md ===== -->

---
created: 2026-01-28T21:18:37 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Linked_Files_html
author: 
---

# Help | Linked Files | Autodesk

> ## Excerpt
> The Revit API can determine which elements in Revit are references to external files ("linked files") and can make some modifications to how Revit loads external files.

---
The Revit API can determine which elements in Revit are references to external files ("linked files") and can make some modifications to how Revit loads external files.

An Element which contains an ExternalFileReference is an element which refers to some file outside of the base .rvt file. Examples include Revit links, CAD links, the element which stores the location of the keynote file, and rendering decals. Element.IsExternalFileReference() returns whether or not an element represents an external file. And Element.GetExternalFileReference() returns the ExternalFileReference for a given Element which contains information pertaining to the external file referenced by the element.

The following classes are associated with linked files in the Revit API:

-   **ExternalFileReference** - A non-Element class which contains path and type information for a single external file which a Revit project references.
-   **ExternalFileUtils** - A utility class which allows the user to find all external file references, get the external file reference from an element, or tell whether an element is an external file reference.
-   **RevitLinkType** - An element representing a Revit file linked into a Revit project.
-   **ModelPath** - A non-Element class which contains path information for a file (not necessarily a .rvt file.) Paths can be to a location on a local or network drive, or to a Revit Server location.
-   **ModelPathUtils** - A utility class which provides methods for converting between strings and ModelPaths.
-   **TransmissionData** - A class which stores information about all of the external file references in a document. The TransmissionData for a Revit project can be read without opening the document.
    
    ### ModelPath
    

ModelPaths are paths to another file. They can refer to Revit models, or to any of Revit's external file references such as DWG links. Paths can be relative or absolute, but they must include an extension indicating the file type. Relative paths are generally relative to the currently opened document. If the current document is workshared, paths will be treated as relative to the central model. To create a ModelPath, use one of the derived classes FilePath or ServerPath.

The class ModelPathUtils contains utility functions for converting ModelPaths to and from user-visible path strings, as well as to determine if a string is a valid server path.

Shared Coordinates let the position of one linked file be known to other linked models.

-   Document.AcquireCoordinates acquires the project coordinates from a specified link instance. This works for both Revit links (RevitLinkInstance) and DWG links (ImportInstance).
-   Document.PublishCoordinates - Publishes shared coordinates to a specified ProjectLocation. This method works only on Revit links. These read-only properties provide information on the geographic coordinate system of a SiteLocation. The geographic coordinate system is imported from a DWG file from AutoCAD or Civil 3D. If the SiteLocation has geographic coordinate system information, the latitude and longitude of the SiteLocation will be updated automatically when the model's Survey Point is moved.

-   SiteLocation.GeoCoordinateSystemId - Gets a string corresponding to geographic coordinate system ID, such as "AMG-50" or "Beijing1954/a.GK3d-40" for the SiteLocation. The value will be the empty string if there is no coordinate system specified for the SiteLocation.
-   SiteLocation.GeoCoordinateSystemDefinition - Gets an XML string describing the geographic coordinate system. The value will be the empty string if there is no coordinate system specified for the SiteLocation.


<!-- ===== END: Help  Linked Files  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Revit Links  Autodesk.md ===== -->

---
created: 2026-01-28T21:18:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Linked_Files_Revit_Links_html
author: 
---

# Help | Revit Links | Autodesk

> ## Excerpt
> Revit documents can have links to various external files, including other Revit documents. These types of links in the Revit API are represented by the RevitLinkType and RevitLinkInstance classes. The RevitLinkType class represents another Revit Document ("link") brought into the current one ("host"), while the RevitLinkInstance class represents an instance of a RevitLinkType.

---
Revit documents can have links to various external files, including other Revit documents. These types of links in the Revit API are represented by the RevitLinkType and RevitLinkInstance classes. The RevitLinkType class represents another Revit Document ("link") brought into the current one ("host"), while the RevitLinkInstance class represents an instance of a RevitLinkType.

### Creating New Links

To create a new Revit link, use the static RevitLinkType.Create() method which will create a new Revit link type and load the linked document and the static RevitLinkInstance.Create() method to place an instance of the link in the model. The RevitLinkType.Create() method requires a document (which will be the host), a ModelPath to the file to be linked, and a RevitLinkOptions object. The RevitLinkOptions class represents options for creating and loading a Revit link. Options include whether or not Revit will store a relative or absolute path to the linked file and the workset configuration. The WorksetConfiguration class is used to specify which, if any, worksets will be opened when creating the link. Note that the relative or absolute path determines how Revit will store the path, but the ModelPath passed into the Create() method needs a complete path to find the linked document initially.

The following example demonstrates the use of RevitLinkType.Create(). The variable pathName is the full path to the file on disk to be linked.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_A0816A8F90D8495CBCDFCAFF1A47C994"><tbody><tr><td><b>Code Region: Create new Revit Link</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>ElementId</span><span> </span><span>CreateRevitLink</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>string</span><span> pathName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilePath</span><span> path </span><span>=</span><span> </span><span>new</span><span> </span><span>FilePath</span><span>(</span><span>pathName</span><span>);</span><span>
    </span><span>RevitLinkOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitLinkOptions</span><span>(</span><span>false</span><span>);</span><span>
    </span><span>// Create new revit link storing absolute path to file</span><span>
    </span><span>LinkLoadResult</span><span> result </span><span>=</span><span> </span><span>RevitLinkType</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> path</span><span>,</span><span> options</span><span>);</span><span>
    </span><span>return</span><span> </span><span>(</span><span>result</span><span>.</span><span>ElementId</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Once the RevitLinkType is created, instances can be added to the document. In the following example, two instances of a RevitLinkType are added, offset by 100'. Until a RevitLinkInstance is created, the Revit link will show up in the Manage Links window, but the elements of the linked file will not be visible in any views.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_A314A2C068AE49879C31807FC70D37D5"><tbody><tr><td><b>Code Region: Create new Revit Link Instance</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateLinkInstances</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>ElementId</span><span> linkTypeId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create revit link instance at origin</span><span>
    </span><span>RevitLinkInstance</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> linkTypeId</span><span>);</span><span>
    </span><span>RevitLinkInstance</span><span> instance2 </span><span>=</span><span> </span><span>RevitLinkInstance</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> linkTypeId</span><span>);</span><span>
    </span><span>// Offset second instance by 100 feet</span><span>
    </span><span>Location</span><span> location </span><span>=</span><span> instance2</span><span>.</span><span>Location</span><span>;</span><span>
    location</span><span>.</span><span>Move</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The examples above work with files on the local disk. Below is a more complex example involving a link to a model on Revit server.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_049D8737A2184D7381C13CE834018D5F"><tbody><tr><td><b>Code Region: Create new Revit Link to a model located on Revit server</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateLinkToServerModel</span><span>(</span><span>UIApplication</span><span> uiApp</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>UIDocument</span><span> uiDoc </span><span>=</span><span> uiApp</span><span>.</span><span>ActiveUIDocument</span><span>;</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> uiDoc</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>// Try to get the server path for the particular model on the server</span><span>
    </span><span>Application</span><span> application </span><span>=</span><span> uiApp</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>String</span><span> hostId </span><span>=</span><span> application</span><span>.</span><span>GetRevitServerNetworkHosts</span><span>().</span><span>First</span><span>();</span><span>
    </span><span>String</span><span> rootFolder </span><span>=</span><span> </span><span>"|"</span><span>;</span><span>
    </span><span>ModelPath</span><span> serverPath </span><span>=</span><span> </span><span>FindModelPathOnServer</span><span>(</span><span>application</span><span>,</span><span> hostId</span><span>,</span><span> rootFolder</span><span>,</span><span> </span><span>"Wall pin model for updaters.rvt"</span><span>);</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create link"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>RevitLinkOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitLinkOptions</span><span>(</span><span>false</span><span>);</span><span>

        </span><span>LinkLoadResult</span><span> result </span><span>=</span><span> </span><span>RevitLinkType</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> serverPath</span><span>,</span><span> options</span><span>);</span><span>

        </span><span>RevitLinkInstance</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> result</span><span>.</span><span>ElementId</span><span>);</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>static</span><span> </span><span>ModelPath</span><span> </span><span>FindModelPathOnServer</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>string</span><span> hostId</span><span>,</span><span> </span><span>string</span><span> folderName</span><span>,</span><span> </span><span>string</span><span> fileName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Connect to host to find list of available models (the "/contents" flag)</span><span>
    </span><span>XmlDictionaryReader</span><span> reader </span><span>=</span><span> </span><span>GetServerResponse</span><span>(</span><span>app</span><span>,</span><span> hostId</span><span>,</span><span> folderName </span><span>+</span><span> </span><span>"/contents"</span><span>);</span><span>
    </span><span>bool</span><span> found </span><span>=</span><span> </span><span>false</span><span>;</span><span>

    </span><span>// Look for the target model name in top level folder</span><span>
    </span><span>List</span><span>&lt;</span><span>String</span><span>&gt;</span><span> folders </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>String</span><span>&gt;();</span><span>
    </span><span>while</span><span> </span><span>(</span><span>reader</span><span>.</span><span>Read</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>// Save a list of subfolders, if found</span><span>
        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Folders"</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>while</span><span> </span><span>(</span><span>reader</span><span>.</span><span>Read</span><span>())</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>EndElement</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Folders"</span><span>)</span><span>
                    </span><span>break</span><span>;</span><span>

                </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Name"</span><span>)</span><span>
                </span><span>{</span><span>
                    reader</span><span>.</span><span>Read</span><span>();</span><span>
                    folders</span><span>.</span><span>Add</span><span>(</span><span>reader</span><span>.</span><span>Value</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>// Check for a matching model at this folder level</span><span>
        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Models"</span><span>)</span><span>
        </span><span>{</span><span>
            found </span><span>=</span><span> </span><span>FindModelInServerResponse</span><span>(</span><span>reader</span><span>,</span><span> fileName</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>found</span><span>)</span><span>
                </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    reader</span><span>.</span><span>Close</span><span>();</span><span>

    </span><span>// Build the model path to match the found model on the server</span><span>
    </span><span>if</span><span> </span><span>(</span><span>found</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Server URLs use "|" for folder separation, Revit API uses "/"</span><span>
        </span><span>String</span><span> folderNameFragment </span><span>=</span><span> folderName</span><span>.</span><span>Replace</span><span>(</span><span>'|'</span><span>,</span><span> </span><span>'/'</span><span>);</span><span>

        </span><span>// Add trailing "/" if not present</span><span>
        </span><span>if</span><span> </span><span>(!</span><span>folderNameFragment</span><span>.</span><span>EndsWith</span><span>(</span><span>"/"</span><span>))</span><span>
            folderNameFragment </span><span>+=</span><span> </span><span>"/"</span><span>;</span><span>

        </span><span>// Build server path</span><span>
        </span><span>ModelPath</span><span> modelPath </span><span>=</span><span> </span><span>new</span><span> </span><span>ServerPath</span><span>(</span><span>hostId</span><span>,</span><span> folderNameFragment </span><span>+</span><span> fileName</span><span>);</span><span>
        </span><span>return</span><span> modelPath</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>// Try subfolders</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>String</span><span> folder </span><span>in</span><span> folders</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ModelPath</span><span> modelPath </span><span>=</span><span> </span><span>FindModelPathOnServer</span><span>(</span><span>app</span><span>,</span><span> hostId</span><span>,</span><span> folder</span><span>,</span><span> fileName</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>modelPath </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
                </span><span>return</span><span> modelPath</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>null</span><span>;</span><span>
</span><span>}</span><span>

</span><span>// This string is different for each RevitServer version</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>string</span><span> revitServerVersion </span><span>=</span><span> </span><span>"/RevitServerAdminRESTService2014/AdminRESTService.svc/"</span><span>;</span><span>

</span><span>private</span><span> </span><span>static</span><span> </span><span>XmlDictionaryReader</span><span> </span><span>GetServerResponse</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>string</span><span> hostId</span><span>,</span><span> </span><span>string</span><span> info</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create request    </span><span>
    </span><span>WebRequest</span><span> request </span><span>=</span><span> </span><span>WebRequest</span><span>.</span><span>Create</span><span>(</span><span>"http://"</span><span> </span><span>+</span><span> hostId </span><span>+</span><span> revitServerVersion </span><span>+</span><span> info</span><span>);</span><span>
    request</span><span>.</span><span>Method</span><span> </span><span>=</span><span> </span><span>"GET"</span><span>;</span><span>

    </span><span>// Add the information the request needs</span><span>

    request</span><span>.</span><span>Headers</span><span>.</span><span>Add</span><span>(</span><span>"User-Name"</span><span>,</span><span> app</span><span>.</span><span>Username</span><span>);</span><span>
    request</span><span>.</span><span>Headers</span><span>.</span><span>Add</span><span>(</span><span>"User-Machine-Name"</span><span>,</span><span> app</span><span>.</span><span>Username</span><span>);</span><span>
    request</span><span>.</span><span>Headers</span><span>.</span><span>Add</span><span>(</span><span>"Operation-GUID"</span><span>,</span><span> </span><span>Guid</span><span>.</span><span>NewGuid</span><span>().</span><span>ToString</span><span>());</span><span>

    </span><span>// Read the response</span><span>
    </span><span>XmlDictionaryReaderQuotas</span><span> quotas </span><span>=</span><span>
        </span><span>new</span><span> </span><span>XmlDictionaryReaderQuotas</span><span>();</span><span>
    </span><span>XmlDictionaryReader</span><span> jsonReader </span><span>=</span><span>
        </span><span>JsonReaderWriterFactory</span><span>.</span><span>CreateJsonReader</span><span>(</span><span>request</span><span>.</span><span>GetResponse</span><span>().</span><span>GetResponseStream</span><span>(),</span><span> quotas</span><span>);</span><span>

    </span><span>return</span><span> jsonReader</span><span>;</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>static</span><span> </span><span>bool</span><span> </span><span>FindModelInServerResponse</span><span>(</span><span>XmlDictionaryReader</span><span> reader</span><span>,</span><span> </span><span>string</span><span> fileName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Read through entries in this section</span><span>
    </span><span>while</span><span> </span><span>(</span><span>reader</span><span>.</span><span>Read</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>EndElement</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Models"</span><span>)</span><span>
            </span><span>break</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Name"</span><span>)</span><span>
        </span><span>{</span><span>
            reader</span><span>.</span><span>Read</span><span>();</span><span>
            </span><span>String</span><span> modelName </span><span>=</span><span> reader</span><span>.</span><span>Value</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>modelName</span><span>.</span><span>Equals</span><span>(</span><span>fileName</span><span>))</span><span>
            </span><span>{</span><span>
                </span><span>// Match found, stop looping and return</span><span>
                </span><span>return</span><span> </span><span>true</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>false</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

In the example below, the WorksetConfiguration is obtained, modified so that only one specified workset is opened and set back to the RevitLinkOptions prior to creating the new link.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_3BF18721D9E147C99E51A9D47AEB5044"><tbody><tr><td><b>Code Region: Create link with one workset open</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>CreateRevitLinkWithOneWorksetOpen</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>string</span><span> pathName</span><span>,</span><span> </span><span>string</span><span> worksetName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilePath</span><span> path </span><span>=</span><span> </span><span>new</span><span> </span><span>FilePath</span><span>(</span><span>pathName</span><span>);</span><span>
    </span><span>RevitLinkOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitLinkOptions</span><span>(</span><span>true</span><span>);</span><span>

    </span><span>// Get info on all the user worksets in the project prior to opening</span><span>
    </span><span>IList</span><span>&lt;</span><span>WorksetPreview</span><span>&gt;</span><span> worksets </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>GetUserWorksetInfo</span><span>(</span><span>path</span><span>);</span><span>
    </span><span>IList</span><span>&lt;</span><span>WorksetId</span><span>&gt;</span><span> worksetIds </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>WorksetId</span><span>&gt;();</span><span>
    </span><span>// Find worksetName</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>WorksetPreview</span><span> worksetPrev </span><span>in</span><span> worksets</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>worksetPrev</span><span>.</span><span>Name</span><span>.</span><span>CompareTo</span><span>(</span><span>worksetName</span><span>)</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
            worksetIds</span><span>.</span><span>Add</span><span>(</span><span>worksetPrev</span><span>.</span><span>Id</span><span>);</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// close all worksets but the one specified</span><span>
    </span><span>WorksetConfiguration</span><span> worksetConfig </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksetConfiguration</span><span>(</span><span>WorksetConfigurationOption</span><span>.</span><span>CloseAllWorksets</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>worksetIds</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        worksetConfig</span><span>.</span><span>Open</span><span>(</span><span>worksetIds</span><span>);</span><span>
    </span><span>}</span><span>
    options</span><span>.</span><span>SetWorksetConfiguration</span><span>(</span><span>worksetConfig</span><span>);</span><span>

    </span><span>LinkLoadResult</span><span> result </span><span>=</span><span> </span><span>RevitLinkType</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> path</span><span>,</span><span> options</span><span>);</span><span>
    </span><span>RevitLinkType</span><span> type </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>result</span><span>.</span><span>ElementId</span><span>)</span><span> </span><span>as</span><span> </span><span>RevitLinkType</span><span>;</span><span>
    </span><span>return</span><span> </span><span>(</span><span>result</span><span>.</span><span>LoadResult</span><span> </span><span>==</span><span> </span><span>LinkLoadResultType</span><span>.</span><span>LinkLoaded</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Whether creating or loading a link, a LinkLoadResult is returned. This class has a property to determine if the link was loaded. It also has an ElementId property that is the id of the created or loaded linked model.

RevitLinkInstance.Create(ImportPlacement placement)creates a new instance of a linked Revit project (RevitLinkType). Instances will be placed origin-to-origin or by shared coordinates according to the input placement type.

### Loading and Unloading Links

RevitLinkType has several methods related to loading links. Load(), LoadFrom() and Unload() allow a link to be loaded or unloaded, or to be loaded from a new location. These methods regenerate the document. The document's Undo history will be cleared by these methods. All transaction phases (e.g. transactions, transaction groups and sub-transactions) that were explicitly started must be finished prior to calling one of these methods.

The static method RevitLinkType.IsLoaded() will return whether or not the link is loaded.

### Getting Link Information

Each RevitLinkType in a document can have one or more associated RevitLinkInstances. The RevitLinkInstance.GetLinkDocument() method returns a Document associated with the Revit link. This document cannot be modified, meaning that operations that require a transaction or modify the document's status in memory (such as Save and Close) cannot be performed.

The associated RevitLinkType for a RevitLinkInstance can be retrieved from the document using the ElementId obtained from the RevitLinkInstance.GetTypeId() method. The RevitLinkType for a linked file has several methods and properties related to nested links. A document that is linked in to another document may itself have links. The IsNested property returns true if the RevitLinkType is a nested link (i.e. it has some other link as a parent), or false if it is a top-level link. The method GetParentId() will get the id of the immediate parent of this link, while GetRootId() will return the id of the top-level link which this link is ultimately linked under. Both methods will return invalidElementId if this link is a top-level link. The method GetChildIds() will return the element ids of all links which are linked directly into this one.

For example, if C is linked into document B and B in turn is linked into document A, calling GetParentId() for the C link will return the id of document B and calling GetRootId() for the C link will return the id of document A. Calling GetChildIds() for document A will only return the id of B's link since C is not a direct link under A.

RevitLinkType also has a PathType property which indicates if the path to the external file reference is relative to the host file's location (or to the central model's location if the host is workshared), an absolute path to a location on disk or the network, or if the path is to a Revit Server location.

The AttachmentType property of RevitLinkType indicates if the link is an attachment or an overlay. "Attachment" links are considered to be part of their parent link and will be brought along if their parent is linked into another document. "Overlay" links are only visible when their parent is opened directly.

The following example gets all RevitLinkInstances in the document and displays some information on them.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_37FBA1DF81EC4336931323A6ACB298F4"><tbody><tr><td><b>Code Region: Getting Link information</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetAllRevitLinkInstances</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>RevitLinkInstance</span><span>));</span><span>
    </span><span>StringBuilder</span><span> linkedDocs </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> elem </span><span>in</span><span> collector</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>RevitLinkInstance</span><span> instance </span><span>=</span><span> elem </span><span>as</span><span> </span><span>RevitLinkInstance</span><span>;</span><span>
        </span><span>Document</span><span> linkDoc </span><span>=</span><span> instance</span><span>.</span><span>GetLinkDocument</span><span>();</span><span>
        linkedDocs</span><span>.</span><span>AppendLine</span><span>(</span><span>"FileName: "</span><span> </span><span>+</span><span> </span><span>Path</span><span>.</span><span>GetFileName</span><span>(</span><span>linkDoc</span><span>.</span><span>PathName</span><span>));</span><span>
        </span><span>RevitLinkType</span><span> type </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>instance</span><span>.</span><span>GetTypeId</span><span>())</span><span> </span><span>as</span><span> </span><span>RevitLinkType</span><span>;</span><span>
        linkedDocs</span><span>.</span><span>AppendLine</span><span>(</span><span>"Is Nested: "</span><span> </span><span>+</span><span> type</span><span>.</span><span>IsNestedLink</span><span>.</span><span>ToString</span><span>());</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit Links in Document"</span><span>,</span><span> linkedDocs</span><span>.</span><span>ToString</span><span>());</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Link Geometry

#### Shared coordinates

The RevitLinkType methods SavePositions() and HasSaveablePositions() support saving shared coordinates changes back to the linked document. Use HasSaveablePositions() to determine if the link has shared positioning changes which can be saved. Call SavePositions() to save shared coordinates changes back to the linked document. SavePositions() requires an instance of the ISaveSharedCoordinatesCallback interface to resolve situations when Revit encounters modified links. The interface's GetSaveModifiedLinksOption() method determines whether Revit should save the link, not save the link, or discard shared positioning entirely.

While SavePositions() does not clear the document's undo history, it cannot be undone since it saves the link's shared coordinates changes to disk.

`ResetSharedCoordinates()` resets the shared coordinates for the host model. It provides the same functionality as the UI Command "Reset Shared Coordinates". After resetting coordinates, the following changes will take place:

-   GIS coordinate system will be erased
-   Shared coordinates?relationships with other linked models will be eliminated.
-   The Survey Point will be moved back to the startup location, where it coincides with the Internal Origin.
-   The angle between Project North and True North will be reset to 0.

Note: There will be no changes to linked models.

#### Conversion of geometric references

The Reference class has members related to linked files that allow conversion between Reference objects which reference only the contents of the link and Reference objects which reference the host. This allows an application, for example, to look at the geometry in the link, find the needed face, and convert the reference to that face into a reference in the host suitable for use to place a face-based instance. Also, these Reference members make it possible to obtain a reference in the host (e.g. from a dimension or family) and convert it to a reference in the link suitable for use in Element.GetGeometryObjectFromReference().

The Reference. LinkedElementId property represents the id of the top-level element in the linked document that is referred to by this reference, or InvalidElementId for references that do not refer to an element in a linked RVT file. The Reference . CreateLinkReference() method uses a RevitLinkInstance to create a Reference from a Reference in a Revit link. And the Reference. CreateReferenceInLink() method creates a Reference in a Revit Link from a Reference in the host file

#### Picking elements in links

The Selection methods PickObject() and PickObjects() allow the selection of objects in Revit links. To allow the user to select elements in linked files, use the ObjectType.LinkedElement enumeration value for the first parameter of the PickObject() or PickObjects(). Note that this option allows for selection of elements in links only, not in the host document.

In the example below, an ISelectionFilter is used to allow only walls to be selected in linked files.

<table summary="" id="GUID-0DFBA9EA-0E7B-49D4-9576-6D0528FC0D3C__TABLE_44433DC9BBAA43E589F3191FE6F3C44B"><tbody><tr><td><b>Code Region: Selecting Elements in Linked File</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SelectElementsInLinkedDoc</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>Selection</span><span> choices </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>;</span><span>
    </span><span>// Pick one wall from Revit link</span><span>
    </span><span>WallInLinkSelectionFilter</span><span> wallFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>WallInLinkSelectionFilter</span><span>();</span><span>
    </span><span>Reference</span><span> elementRef </span><span>=</span><span> choices</span><span>.</span><span>PickObject</span><span>(</span><span>ObjectType</span><span>.</span><span>LinkedElement</span><span>,</span><span> wallFilter</span><span>,</span><span> </span><span>"Select a wall in a linked document"</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>elementRef </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Element from link document selected."</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>// This filter allows selection of only a certain element type in a link instance.</span><span>
</span><span>class</span><span> </span><span>WallInLinkSelectionFilter</span><span> </span><span>:</span><span> </span><span>ISelectionFilter</span><span>
</span><span>{</span><span>
    </span><span>private</span><span> </span><span>RevitLinkInstance</span><span> m_currentInstance </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowElement</span><span>(</span><span>Element</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Accept any link instance, and save the handle for use in AllowReference()</span><span>
        m_currentInstance </span><span>=</span><span> e </span><span>as</span><span> </span><span>RevitLinkInstance</span><span>;</span><span>
        </span><span>return</span><span> </span><span>(</span><span>m_currentInstance </span><span>!=</span><span> </span><span>null</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>bool</span><span> </span><span>AllowReference</span><span>(</span><span>Reference</span><span> refer</span><span>,</span><span> XYZ point</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>m_currentInstance </span><span>==</span><span> </span><span>null</span><span>)</span><span>
            </span><span>return</span><span> </span><span>false</span><span>;</span><span>

        </span><span>// Get the handle to the element in the link</span><span>
        </span><span>Document</span><span> linkedDoc </span><span>=</span><span> m_currentInstance</span><span>.</span><span>GetLinkDocument</span><span>();</span><span>
        </span><span>Element</span><span> elem </span><span>=</span><span> linkedDoc</span><span>.</span><span>GetElement</span><span>(</span><span>refer</span><span>.</span><span>LinkedElementId</span><span>);</span><span>

        </span><span>// Accept the selection if the element exists and is of the correct type</span><span>
        </span><span>return</span><span> elem </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> elem </span><span>is</span><span> </span><span>Wall</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Revit Links  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Managing External Files  Autodesk.md ===== -->

---
created: 2026-01-28T21:18:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Linked_Files_Managing_External_Files_html
author: 
---

# Help | Managing External Files | Autodesk

> ## Excerpt
> As its name implies, this utility class provides information about external file references. TheExternalFileUtils.GetAllExternalFileReferences() method returns a collection of ElementIds of all elements that are external file references in the document. (Note that it will not return the ids of nested Revit links; it only returns top-level references.) This utility class has two other methods, IsExternalFileReference() and GetExternalFileReference() which perform the same function as the similarly named methods of the Element class, but can be used when you have an ElementId rather than first obtaining the Element.

---
### ExternalFileUtils

As its name implies, this utility class provides information about external file references. TheExternalFileUtils.GetAllExternalFileReferences() method returns a collection of ElementIds of all elements that are external file references in the document. (Note that it will not return the ids of nested Revit links; it only returns top-level references.) This utility class has two other methods, IsExternalFileReference() and GetExternalFileReference() which perform the same function as the similarly named methods of the Element class, but can be used when you have an ElementId rather than first obtaining the Element.

TransmissionDataTransmissionData stores information on both the previous state and requested state of an external file reference. This means that it stores the load state and path of the reference from the most recent time this TransmissionData's document was opened. It also stores load state and path information for what Revit should do the next time the document is opened.

As such, TransmissionData can be used to perform operations on external file references without having to open the entire associated Revit document. The methods ReadTransmissionData and WriteTransmissionData can be used to obtain information about external references, or to change that information. For example, calling WriteTransmissionData with a TransmissionData object which has had all references set to LinkedFileStatus.Unloaded would cause no references to be loaded upon next opening the document.

TransmissionData cannot add or remove references to external files. If AddExternalFileReference is called using an ElementId which does not correspond to an element which is an external file reference, the information will be ignored on file load.

The following example reads the TransmissionData for a file at the given location and sets all Revit links to be unloaded the next time the document is opened.

<table summary="" id="GUID-2C8C4EC0-6EEB-4D0A-A3AB-6F3434A70461__TABLE_15BEED9592504EFEAF1F8928ED3B1A98"><tbody><tr><td><b>Code Region: Unload Revit Links</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>UnloadRevitLinks</span><span>(</span><span>ModelPath</span><span> location</span><span>)</span><span>
</span><span>/// This method will set all Revit links to be unloaded the next time the document at the given location is opened. </span><span>
</span><span>/// The TransmissionData for a given document only contains top-level Revit links, not nested links.</span><span>
</span><span>/// However, nested links will be unloaded if their parent links are unloaded, so this function only needs to look at the document's immediate links. </span><span>
</span><span>{</span><span>
    </span><span>// access transmission data in the given Revit file</span><span>
    </span><span>TransmissionData</span><span> transData </span><span>=</span><span> </span><span>TransmissionData</span><span>.</span><span>ReadTransmissionData</span><span>(</span><span>location</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>transData </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// collect all (immediate) external references in the model</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> externalReferences </span><span>=</span><span> transData</span><span>.</span><span>GetAllExternalFileReferenceIds</span><span>();</span><span>
        </span><span>// find every reference that is a link</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> refId </span><span>in</span><span> externalReferences</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ExternalFileReference</span><span> extRef </span><span>=</span><span> transData</span><span>.</span><span>GetLastSavedReferenceData</span><span>(</span><span>refId</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>extRef</span><span>.</span><span>ExternalFileReferenceType</span><span> </span><span>==</span><span> </span><span>ExternalFileReferenceType</span><span>.</span><span>RevitLink</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// we do not want to change neither the path nor the path-type</span><span>
                </span><span>// we only want the links to be unloaded (shouldLoad = false)</span><span>
                transData</span><span>.</span><span>SetDesiredReferenceData</span><span>(</span><span>refId</span><span>,</span><span> extRef</span><span>.</span><span>GetPath</span><span>(),</span><span> extRef</span><span>.</span><span>PathType</span><span>,</span><span> </span><span>false</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>// make sure the IsTransmitted property is set </span><span>
        transData</span><span>.</span><span>IsTransmitted</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>// modified transmission data must be saved back to the model</span><span>
        </span><span>TransmissionData</span><span>.</span><span>WriteTransmissionData</span><span>(</span><span>location</span><span>,</span><span> transData</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Unload Links"</span><span>,</span><span> </span><span>"The document does not have any transmission data"</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

#### Construct ModelPath for location on Revit Server

To read the TransmissionData object, you need to call the static method TransmissionData.ReadTransmissionData. It requires a ModelPath object.

There are two ways to construct a ModelPath object that refers to a central file. The first way involves using ModelPathUtils and the base ModelPath class. The steps are as follows:

1.  Compose the user-visible path string of the central file: `RSN://` + “relative path”.
    
    Note: The folder separator used in the "relative path" is a forward slash(/). The correct separator is a forward slash.
    
2.  Create a ModelPath object via the ModelPathUtils.ConvertUserVisiblePathToModelPath() method. Pass in the string composed in the previous step.
    
3.  Read the transmission data via the TransmissionData::ReadTransmissionData() method. Pass in the ModelPath obtained in the previous step.
    

The following example demonstrates this method assuming a central file testmodel.rvt is stored in the root folder of Revit Server, SHACNG035WQRP.

<table summary="" id="GUID-2C8C4EC0-6EEB-4D0A-A3AB-6F3434A70461__TABLE_8D9A6DA3E5804C46AE4F37D20C2611A4"><tbody><tr><td><b>Code Region: Constructing path to central file using ModelPath</b></td></tr><tr><td><pre><code><span>[</span><span>TransactionAttribute</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>Manual</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>RevitCommandLink</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
  </span><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span>        
         </span><span>ref</span><span> </span><span>string</span><span> messages</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>UIApplication</span><span> app </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> app</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"ExComm"</span><span>);</span><span>
    trans</span><span>.</span><span>Start</span><span>();</span><span>
    </span><span>string</span><span> visiblePath </span><span>=</span><span> </span><span>"RSN://testmodel.rvt"</span><span>;</span><span>
    </span><span>ModelPath</span><span> serverPath </span><span>=</span><span> </span><span>ModelPathUtils</span><span>.</span><span>ConvertUserVisiblePathToModelPath</span><span>(</span><span>visiblePath</span><span>);</span><span>
    </span><span>TransmissionData</span><span> transData </span><span>=</span><span> </span><span>TransmissionData</span><span>.</span><span>ReadTransmissionData</span><span>(</span><span>serverPath</span><span>);</span><span>
    </span><span>string</span><span> mymessage </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>transData </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
         </span><span>//access the data in the transData here.</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
      </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Unload Links"</span><span>,</span><span>
      </span><span>"The document does not have any transmission data"</span><span>);</span><span>
    </span><span>}</span><span>
    trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
  </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The second way to construct the ModelPath object that that refers to a central file is to use the child class ServerPath. This way can be used if the program knows the local server name, however, it is not recommended as the server name may be changed by the Revit user from the Revit UI. The steps are as follows:

1.  Create a ServerPath object using ServerPath constructor.
    
    ```
    public ServerPath GetServerPath()
    {
    return new ServerPath("ServerNameOrServerIp", "relative path without the initial forward slash");
    }
    ```
    

Note: The first parameter is the server name, not the "RSN://" string. The second parameter does not include the initial forward slash. See the following sample code. The folder separator is a forward slash(/) too.

1\. Read the TransmissionData object via the TransmissionData.ReadTransmissionData() method.Pass in the ServerPath obtained in the previous step

The following code demonstrates this method.

<table summary="" id="GUID-2C8C4EC0-6EEB-4D0A-A3AB-6F3434A70461__TABLE_25FF84A4048F4110BCE03C0A93D8DA65"><tbody><tr><td><b>Code Region: Constructing path to central file using ServerPath</b></td></tr><tr><td><pre><code><span>[</span><span>TransactionAttribute</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>Manual</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>RevitCommand</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
  </span><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span>
         </span><span>ref</span><span> </span><span>string</span><span> messages</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
  </span><span>{</span><span>
    </span><span>UIApplication</span><span> app </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> app</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"ExComm"</span><span>);</span><span>
    trans</span><span>.</span><span>Start</span><span>();</span><span>
    </span><span>ServerPath</span><span> serverPath </span><span>=</span><span> </span><span>new</span><span> </span><span>ServerPath</span><span>(</span><span>"SHACNG035WQRP"</span><span>,</span><span> </span><span>"testmodel.rvt"</span><span>);</span><span>
    </span><span>TransmissionData</span><span> transData </span><span>=</span><span> </span><span>TransmissionData</span><span>.</span><span>ReadTransmissionData</span><span>(</span><span>serverPath</span><span>);</span><span>
    </span><span>string</span><span> mymessage </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>transData </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
       </span><span>//access the data in the transData here.</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
      </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Unload Links"</span><span>,</span><span>
         </span><span>"The document does not have any transmission data"</span><span>);</span><span>
    </span><span>}</span><span>
    trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
  </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Managing External Files  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Performance Adviser  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Performance_Adviser_html
author: 
---

# Help | Performance Adviser | Autodesk

> ## Excerpt
> The performance adviser feature of the Revit API is designed to analyze a document and flag for the user any elements and/or settings that may cause performance degradation. The Performance Adviser command executes a set of rules and displays their result in a standard review warnings dialog.

---
The performance adviser feature of the Revit API is designed to analyze a document and flag for the user any elements and/or settings that may cause performance degradation. The Performance Adviser command executes a set of rules and displays their result in a standard review warnings dialog.

The API for performance adviser consists of 2 classes:

-   **PerformanceAdviser** - an application-wide object that has a dual role as a registry of rules to run in order to detect potential performance problems and an engine to execute them
-   **IPerformanceAdviserRule** - an interface that allows you to define new rules for the Performance Adviser
    
    ### Performance Adviser
    

PerformanceAdviser is used to add or delete rules to be checked, enable and disable rules, get information about rules in the list, and to execute some or all rules in the list. Applications that create new rules are expected to use AddRule() to register the new rule during application startup and DeleteRule() to deregister it during application shutdown. ExecuteAllRules() will execute all rules in the list on a given document, while ExecuteRules() can be used to execute selected rules in a document. Both methods will return a list of failure messages explaining performance problems detected in the document.

The following example demonstrates looping through all performance adviser rules and executing all the rules for a document.

<table summary="" id="GUID-471E470E-FD4D-497B-98C7-AC0A97F57D4C__TABLE_D9E9C4F79A25460C9C4ED8B0F49AF588"><tbody><tr><td><b>Code Region: Performance Adviser</b></td></tr><tr><td><pre><code><span>//Get the name of each registered PerformanceRule and then execute all of them.</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>RunAllRules</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>PerformanceAdviserRuleId</span><span> id </span><span>in</span><span> </span><span>PerformanceAdviser</span><span>.</span><span>GetPerformanceAdviser</span><span>().</span><span>GetAllRuleIds</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>string</span><span> ruleName </span><span>=</span><span> </span><span>PerformanceAdviser</span><span>.</span><span>GetPerformanceAdviser</span><span>().</span><span>GetRuleName</span><span>(</span><span>id</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>PerformanceAdviser</span><span>.</span><span>GetPerformanceAdviser</span><span>().</span><span>ExecuteAllRules</span><span>(</span><span>document</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### IPerformanceAdviserRule

Create an instance of the IPerformanceAdviserRule interface to create new rules for the Performance Adviser. Rules can be specific to elements or can be document-wide rules. The following methods need to be implemented:

-   GetName() - a short string naming the rule
-   GetDescription() - a one to two sentence description of the rule
-   InitCheck() -method invoked by performance advisor once in the beginning of the check. If rule checks the document as a whole rather than specific elements, the check should be performed in this method.
-   FinalizeCheck() - method invoked by performance advisor once in the end of the check. Any problematic results found during rule execution can be reported during this message using FailureMessage(s)
-   WillCheckElements() - indicates if rule needs to be executed on idividual elements
-   GetElementFilter() - retrieves a filter to restrict elements to be checked
-   ExecuteElementCheck() - method invoked by performance advisor for each element to be checked

The following excerpt from the PerformanceAdviserControl sample in the Revit API SDK Samples folder demonstrates the implementation of a custom rule used to identify any doors in the document that are face-flipped. (See the sample project for the complete class implementation.)

<table summary="" id="GUID-471E470E-FD4D-497B-98C7-AC0A97F57D4C__TABLE_767B135077F244C49D87F8778175D55E"><tbody><tr><td><b>Code Region: Implementing IPerformanceAdviserRule</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>FlippedDoorCheck</span><span> </span><span>:</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>IPerformanceAdviserRule</span><span>
</span><span>{</span><span>
    </span><span>private</span><span> </span><span>string</span><span> m_name</span><span>;</span><span>
    </span><span>private</span><span> </span><span>string</span><span> m_description</span><span>;</span><span>
    </span><span>private</span><span> </span><span>FailureDefinitionId</span><span> m_doorWarningId</span><span>;</span><span>
    </span><span>private</span><span> </span><span>FailureDefinition</span><span> m_doorWarning</span><span>;</span><span>
    </span><span>private</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> m_FlippedDoors</span><span>;</span><span>
    </span><span>#region Constructor</span><span>
    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Set up rule name, description, and error handling</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>public</span><span> </span><span>FlippedDoorCheck</span><span>()</span><span>
    </span><span>{</span><span>
        m_name </span><span>=</span><span> </span><span>"Flipped Door Check"</span><span>;</span><span>
        m_description </span><span>=</span><span> </span><span>"An API-based rule to search for and return any doors that are face-flipped"</span><span>;</span><span>
        m_doorWarningId </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FailureDefinitionId</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"25570B8FD4AD42baBD78469ED60FB9A3"</span><span>));</span><span>
        m_doorWarning </span><span>=</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FailureDefinition</span><span>.</span><span>CreateFailureDefinition</span><span>(</span><span>m_doorWarningId</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FailureSeverity</span><span>.</span><span>Warning</span><span>,</span><span> </span><span>"Some doors in this project are face-flipped."</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>#endregion</span><span>

    </span><span>#region IPerformanceAdviserRule implementation</span><span>
    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Does some preliminary work before executing tests on elements.  In this case,</span><span>
    </span><span>/// we instantiate a list of FamilyInstances representing all doors that are flipped.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="document"&gt;The document being checked&lt;/param&gt;</span><span>
    </span><span>public</span><span> </span><span>void</span><span> </span><span>InitCheck</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
    </span><span>{</span><span>
       </span><span>if</span><span> </span><span>(</span><span>m_FlippedDoors </span><span>==</span><span> </span><span>null</span><span>)</span><span>
          m_FlippedDoors </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>&gt;();</span><span>
       </span><span>else</span><span>
          m_FlippedDoors</span><span>.</span><span>Clear</span><span>();</span><span>
       </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// This method does most of the work of the IPerformanceAdviserRule implementation.</span><span>
    </span><span>/// It is called by PerformanceAdviser.</span><span>
    </span><span>/// It examines the element passed to it (which was previously filtered by the filter</span><span>
    </span><span>/// returned by GetElementFilter() (see below)).  After checking to make sure that the</span><span>
    </span><span>/// element is an instance, it checks the FacingFlipped property of the element.</span><span>
    </span><span>///</span><span>
    </span><span>/// If it is flipped, it adds the instance to a list to be used later.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="document"&gt;The active document&lt;/param&gt;</span><span>
    </span><span>/// &lt;param name="element"&gt;The current element being checked&lt;/param&gt;</span><span>
    </span><span>public</span><span> </span><span>void</span><span> </span><span>ExecuteElementCheck</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> element</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>((</span><span>element </span><span>is</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FamilyInstance</span><span>))</span><span>
        </span><span>{</span><span>
             </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FamilyInstance</span><span> doorCurrent </span><span>=</span><span> element </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FamilyInstance</span><span>;</span><span>
             </span><span>if</span><span> </span><span>(</span><span>doorCurrent</span><span>.</span><span>FacingFlipped</span><span>)</span><span>
                 m_FlippedDoors</span><span>.</span><span>Add</span><span>(</span><span>doorCurrent</span><span>.</span><span>Id</span><span>);</span><span>
        </span><span>}</span><span>

    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// This method is called by PerformanceAdviser after all elements in document</span><span>
    </span><span>/// matching the ElementFilter from GetElementFilter() are checked by ExecuteElementCheck().</span><span>
    </span><span>///</span><span>
    </span><span>/// This method checks to see if there are any elements (door instances, in this case) in the</span><span>
    </span><span>/// m_FlippedDoor instance member.  If there are, it iterates through that list and displays</span><span>
    </span><span>/// the instance name and door tag of each item.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="document"&gt;The active document&lt;/param&gt;</span><span>
    </span><span>public</span><span> </span><span>void</span><span> </span><span>FinalizeCheck</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>m_FlippedDoors</span><span>.</span><span>Count</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
            </span><span>System</span><span>.</span><span>Diagnostics</span><span>.</span><span>Debug</span><span>.</span><span>WriteLine</span><span>(</span><span>"No doors were flipped.  Test passed."</span><span>);</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            </span><span>//Pass the element IDs of the flipped doors to the revit failure reporting APIs.</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FailureMessage</span><span> fm </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FailureMessage</span><span>(</span><span>m_doorWarningId</span><span>);</span><span>
            fm</span><span>.</span><span>SetFailingElements</span><span>(</span><span>m_FlippedDoors</span><span>);</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Transaction</span><span> failureReportingTransaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Failure reporting transaction"</span><span>);</span><span>
            failureReportingTransaction</span><span>.</span><span>Start</span><span>();</span><span>
            document</span><span>.</span><span>PostFailure</span><span>(</span><span>fm</span><span>);</span><span>
            failureReportingTransaction</span><span>.</span><span>Commit</span><span>();</span><span>
            m_FlippedDoors</span><span>.</span><span>Clear</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Gets the description of the rule</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;returns&gt;The rule description&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>string</span><span> </span><span>GetDescription</span><span>()</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> m_description</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// This method supplies an element filter to reduce the number of elements that PerformanceAdviser</span><span>
    </span><span>/// will pass to GetElementCheck().  In this case, we are filtering for door elements.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="document"&gt;The document being checked&lt;/param&gt;</span><span>
    </span><span>/// &lt;returns&gt;A door element filter&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementFilter</span><span> </span><span>GetElementFilter</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementCategoryFilter</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>BuiltInCategory</span><span>.</span><span>OST_Doors</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Gets the name of the rule</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;returns&gt;The rule name&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>string</span><span> </span><span>GetName</span><span>()</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> m_name</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Returns true if this rule will iterate through elements and check them, false otherwise</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;returns&gt;True&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>bool</span><span> </span><span>WillCheckElements</span><span>()</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> </span><span>true</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>#endregion</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Performance Adviser  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Place and Locations  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_html
author: 
---

# Help | Place and Locations | Autodesk

> ## Excerpt
> Every building has a unique place in the world because the Latitude and Longitude are unique. In addition, a building can have many locations in relation to other buildings. The Revit Platform API Site namespace uses certain classes to save the geographical location information for Revit projects.

---
Every building has a unique place in the world because the Latitude and Longitude are unique. In addition, a building can have many locations in relation to other buildings. The Revit Platform API Site namespace uses certain classes to save the geographical location information for Revit projects.

Note: The Revit Platform API does not expose the Site menu functions. Only Site namespace provides functions corresponding to the Location options found on the Project Location panel on the Manage tab.

### Topics in this section


<!-- ===== END: Help  Place and Locations  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Place  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_Place_html
author: 
---

# Help | Place | Autodesk

> ## Excerpt
> In the Revit Platform API, the SiteLocation class contains place information including Latitude, Longitude, and Time Zone. This information identifies where the project is located in the world. When setting either the Latitude or Longitude, note that:

---
## SiteLocation

In the Revit Platform API, the SiteLocation class contains place information including Latitude, Longitude, and Time Zone. This information identifies where the project is located in the world. When setting either the Latitude or Longitude, note that:

1.  Revit will attempt to match the coordinates to a city it knows about, and if a match is found, will set the name accordingly.
2.  Revit will attempt to automatically adjust the time zone value to match the new Longitude or Latitude value set using SunAndShadowSettings.CalculateTimeZone(). For some boundary cases, the time zone calculated may not be correct and the TimeZone property can be set directly if necessary.

Properties include information about the longitude, latitude, place name, and time zone. Its methods are:

-   ConvertFromProjectTime - Converts project time to UTC time
-   ConvertToProjectTime - Converts local time or UTC time to project time
-   IsCompatibleWith - Checks whether the geographic coordinate system of this site is compatible with the given site
-   SiteLocation.SetGeoCoordinateSystem(string coordSystem) - sets the Geo coordinate system for the current document

## InternalOrigin

The InternalOrigin class represents the origin of Revit's internal coordinate system. Each Revit project contains one InternalOrigin. It has the following members:

-   InternalOrigin.Get(Document doc) - Returns the internal origin of the project
-   InternalOrigin.Position - Read-only property which returns the XYZ value of the internal coordinates. The position will always be (0,0,0)
-   InternalOrigin.SharedPosition - Read-only property which returns the shared position of the internal origin based on the active ProjectLocation of its project

## BasePoint

The BasePoint class represents the Project Base Point and Survey Point. Each Revit project contains one project base point and one survey point. The project base point represents the origin of the project coordinate system. The survey point represents the origin of the shared coordinate system.

-   BasePoint.Position - Gets the XYZ value corresponding to the base point's position in Revit's internal coordinates
-   BasePoint.SharedPosition - Gets the XYZ value corresponding to the base point's position in the transformed (shared) coordinates
-   BasePoint.GetProjectBasePoint() - Gets the project base point
-   BasePoint.GetSurveyPoint() - Gets the survey point
-   BasePoint.Clipped gets and sets the clipped state of the survey point BasePoint based on the active ProjectLocation of its Document. For the project base point, it will always return false and attempting to set it will throw an exception.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F3A532FC-E537-4CD5-A351-48AC48C21092-low.png)**Figure 123: Project Place**


<!-- ===== END: Help  Place  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  City  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:20 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_City_html
author: 
---

# Help | City | Autodesk

> ## Excerpt
> City is an object that contains geographical location information for a known city in the world. It contains longitude, latitude, and time zone information. The city list is retrieved by the Cities property in the Application object. New cities cannot be added to the existing list in Revit. The city where the current project is located is not exposed by the Revit Platform API.

---
City is an object that contains geographical location information for a known city in the world. It contains longitude, latitude, and time zone information. The city list is retrieved by the Cities property in the Application object. New cities cannot be added to the existing list in Revit. The city where the current project is located is not exposed by the Revit Platform API.

**Parent page:** [Place and Locations](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_html)


<!-- ===== END: Help  City  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  ProjectLocation  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:25 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_ProjectLocation_html
author: 
---

# Help | ProjectLocation | Autodesk

> ## Excerpt
> A project only has one site which is the absolute location on the earth. However, it can have different locations relative to the projects around it. Depending on the coordinates and origins in use, there can be many ProjectLocation objects in one project.

---
A project only has one site which is the absolute location on the earth. However, it can have different locations relative to the projects around it. Depending on the coordinates and origins in use, there can be many ProjectLocation objects in one project.

By default each Revit project contains at least one named location, Internal. It is the active project location. You can retrieve it using the Document.ActiveProjectLocation property. All existing ProjectLocation objects are retrieved using the Document.ProjectLocations property.


<!-- ===== END: Help  ProjectLocation  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Project Position  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:30 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_Project_Position_html
author: 
---

# Help | Project Position | Autodesk

> ## Excerpt
> Project position is an object that represents a geographical offset and rotation. It is usually used by the ProjectLocation object to get and set geographical information. The following figure shows the results after changing the ProjectLocation geographical rotation and the coordinates for the same point. However, you cannot see the result of changing the ProjectLocation geographical offset directly.

---
Project position is an object that represents a geographical offset and rotation. It is usually used by the ProjectLocation object to get and set geographical information. The following figure shows the results after changing the ProjectLocation geographical rotation and the coordinates for the same point. However, you cannot see the result of changing the ProjectLocation geographical offset directly.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-7242FF42-B873-48EC-8D6C-208675848D2D-low.png)**Figure 125: Point coordinates**

Note: East indicates that the Location is rotated counterclockwise; West indicates that the location is rotated clockwise. If the Angle value is between 180 and 360 degrees, Revit transforms it automatically. For example, if you select East and type 200 degrees for Angle, Revit transforms it to West 160 degrees.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-C784E377-BFF8-4CCE-B5A8-77310071FCD3-low.png)**Figure 126: Geographical offset and rotation sketch map**

The following sample code illustrates how to retrieve the ProjectLocation object.

<table summary="" id="GUID-A1B6B145-132D-47EF-8B2E-DB1659CB6A0A__TABLE_73FFF89973034B8AA41420D93CAE0CDF"><tbody><tr><td><b>Code Region 21-1: Retrieving the ProjectLocation object</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ShowActiveProjectLocationUsage</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the project location handle </span><span>
    </span><span>ProjectLocation</span><span> projectLocation </span><span>=</span><span> document</span><span>.</span><span>ActiveProjectLocation</span><span>;</span><span>

    </span><span>// Show the information of current project location</span><span>
    XYZ origin </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>ProjectPosition</span><span> position </span><span>=</span><span> projectLocation</span><span>.</span><span>GetProjectPosition</span><span>(</span><span>origin</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> position</span><span>)</span><span>
    </span><span>{</span><span>
            </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"No project position in origin point."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Format the prompt string to show the message.</span><span>
    </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"Current project location information:\n"</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t"</span><span> </span><span>+</span><span> </span><span>"Origin point position:"</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"Angle: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>Angle</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"East to West offset: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>EastWest</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"Elevation: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>Elevation</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"North to South offset: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>NorthSouth</span><span>;</span><span>

    </span><span>// Angles are in radians when coming from Revit API, so we </span><span>
    </span><span>// convert to degrees for display</span><span>
    </span><span>const</span><span> </span><span>double</span><span> angleRatio </span><span>=</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>180</span><span>;</span><span>        </span><span>// angle conversion factor</span><span>

    </span><span>SiteLocation</span><span> site </span><span>=</span><span> projectLocation</span><span>.</span><span>GetSiteLocation</span><span>();</span><span>
    </span><span>string</span><span> degreeSymbol </span><span>=</span><span> </span><span>((</span><span>char</span><span>)</span><span>176</span><span>).</span><span>ToString</span><span>();</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t"</span><span> </span><span>+</span><span> </span><span>"Site location:"</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"Latitude: "</span><span> </span><span>+</span><span> site</span><span>.</span><span>Latitude</span><span> </span><span>/</span><span> angleRatio </span><span>+</span><span> degreeSymbol</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"Longitude: "</span><span> </span><span>+</span><span> site</span><span>.</span><span>Longitude</span><span> </span><span>/</span><span> angleRatio </span><span>+</span><span> degreeSymbol</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"TimeZone: "</span><span> </span><span>+</span><span> site</span><span>.</span><span>TimeZone</span><span>;</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: There is only one active project location at a time. To see the result after changing the ProjectLocation geographical offset and rotation, change the Orientation property from Project North to True North in the plan view Properties pane.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-57E4EC63-4A77-4C7C-91B3-770F3ADDBE6D-low.png)**Figure 128: Project is rotated 30 degrees from Project North to True North**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-57C77B88-C8F7-4207-9A4F-3728182159F3-low.png)**Figure 129: Project location information**

### Creating and Deleting Project Locations

Create new project locations by duplicating an existing project location using the Duplicate() method. The following code sample illustrates how to create a new project location using the Duplicate() method.

<table summary="" id="GUID-A1B6B145-132D-47EF-8B2E-DB1659CB6A0A__TABLE_27AF2AE0989C472BB31F2D5233A7BE03"><tbody><tr><td><b>Code Region 21-2: Creating a project location</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>ProjectLocation</span><span> </span><span>DuplicateLocation</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>string</span><span> newName</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>ProjectLocation</span><span> currentLocation </span><span>=</span><span> document</span><span>.</span><span>ActiveProjectLocation</span><span>;</span><span>
        </span><span>ProjectLocationSet</span><span> locations </span><span>=</span><span> document</span><span>.</span><span>ProjectLocations</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ProjectLocation</span><span> projectLocation </span><span>in</span><span> locations</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>projectLocation</span><span>.</span><span>Name</span><span> </span><span>==</span><span> newName</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"The name is same as a project location's name, please change one."</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>return</span><span> currentLocation</span><span>.</span><span>Duplicate</span><span>(</span><span>newName</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following code sample illustrates how to delete an existing project location from the current project.

<table summary="" id="GUID-A1B6B145-132D-47EF-8B2E-DB1659CB6A0A__TABLE_3FE6D1C068D6463280D075BA85C12B80"><tbody><tr><td><b>Code Region 21-3: Deleting a project location</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>DeleteLocation</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ProjectLocation</span><span> currentLocation </span><span>=</span><span> document</span><span>.</span><span>ActiveProjectLocation</span><span>;</span><span>
    </span><span>//There must be at least one project location in the project.</span><span>
    </span><span>ProjectLocationSet</span><span> locations </span><span>=</span><span> document</span><span>.</span><span>ProjectLocations</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>1</span><span> </span><span>==</span><span> locations</span><span>.</span><span>Size</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>string</span><span> name </span><span>=</span><span> </span><span>"location"</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>name </span><span>!=</span><span> currentLocation</span><span>.</span><span>Name</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ProjectLocation</span><span> projectLocation </span><span>in</span><span> locations</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>projectLocation</span><span>.</span><span>Name</span><span> </span><span>==</span><span> name</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>ICollection</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>&gt;</span><span> elemSet </span><span>=</span><span> document</span><span>.</span><span>Delete</span><span>(</span><span>projectLocation</span><span>.</span><span>Id</span><span>);</span><span>
                </span><span>if</span><span> </span><span>(</span><span>elemSet</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Project Location Deleted!"</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: The following rules apply to deleting a project location:

-   The active project location cannot be deleted because there must be at least one project location in the project.
-   You cannot delete the project location if the ProjectLocationSet class instance is read-only.


<!-- ===== END: Help  Project Position  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Point Clouds  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:35 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Point_Clouds_html
author: 
---

# Help | Point Clouds | Autodesk

> ## Excerpt
> The Revit API provides 2 ways to work with point clouds. The first way allows you to create new point cloud instances, read and filter points, select sub-sets of the overall points, and select points to be highlighted or isolated. The second way allows you to use your own point cloud engine and process unsupported file formats (i.e. other than .pcg, .rcp or .rcs), providing points to Revit for the user to see.

---
The Revit API provides 2 ways to work with point clouds. The first way allows you to create new point cloud instances, read and filter points, select sub-sets of the overall points, and select points to be highlighted or isolated. The second way allows you to use your own point cloud engine and process unsupported file formats (i.e. other than .pcg, .rcp or .rcs), providing points to Revit for the user to see.

-   Client API
    
    -   Create new Point Cloud instances
    -   Read & Filter Points
    -   Point Set Selection
    -   Control Point Cloud highlighting
-   Engine API
    
    -   Register Point Cloud file extension
    -   Provide points to Revit for rendering


<!-- ===== END: Help  Point Clouds  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Point Cloud Client  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Point_Clouds_Point_Cloud_Client_html
author: 
---

# Help | Point Cloud Client | Autodesk

> ## Excerpt
> The point cloud client API supports read and modification of point cloud instances within Revit.

---
The point cloud client API supports read and modification of point cloud instances within Revit.

The points supplied by the point cloud instances come from the point cloud engine, which is either a built-in engine within Revit, or [a third party engine loaded as an application](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Point_Clouds_Point_Cloud_Engine_html). A client point cloud API application doesn’t need to be concerned with the details of how the engine stores and serves points to Revit. Instead, the client API can be used to create point clouds, manipulate their properties, and read the points found matching a given filter.

The main classes related to point clouds are:

-   **PointCloudType** - type of point cloud loaded into a Revit document. Each PointCloudType maps to a single file or identifier (depending upon the type of Point Cloud Engine which governs it).
-   **PointCloudInstance** - an instance of a point cloud in a location in the Revit project.
-   **PointCloudFilter** - a filter determining the volume of interest when extracting points.
-   **PointCollection** - a collection of points obtained from an instance and a filter.
-   **PointIterator** - an iterator for the points in a PointCollection.
-   **CloudPoint** - an individual point cloud point, representing an X, Y, Z location in the coordinates of the cloud, and a color.
-   **PointCloudOverrides** - and its related settings classes specify graphic overrides that are stored by a view to be applied to a PointCloudInstance element, or a scan within the element.

### Point cloud file paths

Two important path locations dealing with point clouds are available as read-only data:

1.  PointCloudType.GetPath() - The path of the link source from which the points are loaded
2.  Application.PointCloudsRootPath - The root path for point cloud files which is used by Revit to calculate relative paths to point cloud files

### Creating a Point Cloud

To create a new point cloud in a Revit document, create a PointCloudType and then use it to create a PointCloudInstance. The static PointCloudType.Create() method requires the engine identifier, as it was registered with Revit by a third party, or the file extension of the point cloud file, if it is a supported file type. It also requires a file name or the identification string for a non-file based engine. In the following sample, a pcg file is used to create a point cloud in a Revit document.

<table summary="" id="GUID-B80DBCF1-56A8-4864-A0CD-181466E0EDE8__TABLE_DB4694291F3E4A2C870574D205436A48"><tbody><tr><td><b>Code Region: Create a point cloud from an rcs file</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>PointCloudInstance</span><span> </span><span>CreatePointCloud</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>PointCloudType</span><span> type </span><span>=</span><span> </span><span>PointCloudType</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"rcs"</span><span>,</span><span> </span><span>"c:\\32_cafeteria.rcs"</span><span>);</span><span>
    </span><span>return</span><span> </span><span>(</span><span>PointCloudInstance</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> type</span><span>.</span><span>Id</span><span>,</span><span> </span><span>Transform</span><span>.</span><span>Identity</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/PointCloudInstance.png)

**Figure: Point Cloud from 32\_cafeteria.rcs**

### Accessing Points in a Point Cloud

There are two ways to access the points in a point cloud:

1.  Iterate the resulting points directly from the PointCollection return using the `IEnumerable<CloudPoint>` interface
2.  Get a pointer to the point storage of the collection and access the points directly in memory in an unsafe interface

Either way, the first step to access a collection of points from the PointCloudInstance is to use the method

-   PointCloudInstance.GetPoints(PointCloudFilter filter, double averageDistance, int numPoints)

Note that as a result of search algorithms used by Revit and the point cloud engine, the exact requested number of points may not be returned.

Although the second option involves dealing with pointers directly, there may be performance improvements when traversing large buffers of points. However, this option is only possible from C# and C++/CLI.

The following two examples show how to iterate part of a point cloud using on one of these two methods.

<table summary="" id="GUID-B80DBCF1-56A8-4864-A0CD-181466E0EDE8__TABLE_386801A0786842078EFB34D4B4DCAA7F"><tbody><tr><td><b>Code Region: Reading point cloud points by iteration</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetPointCloudDataByIteration</span><span>(</span><span>PointCloudInstance</span><span> pcInstance</span><span>,</span><span> </span><span>PointCloudFilter</span><span> pointCloudFilter</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// read points by iteration</span><span>
    </span><span>double</span><span> averageDistance </span><span>=</span><span> </span><span>0.001</span><span>;</span><span>
    </span><span>PointCollection</span><span> points </span><span>=</span><span> pcInstance</span><span>.</span><span>GetPoints</span><span>(</span><span>pointCloudFilter</span><span>,</span><span> averageDistance</span><span>,</span><span> </span><span>10000</span><span>);</span><span> </span><span>// Get points.  Number of points is determined by the needs of the client</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>CloudPoint</span><span> point </span><span>in</span><span> points</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Process each point</span><span>
        </span><span>System</span><span>.</span><span>Drawing</span><span>.</span><span>Color</span><span> color </span><span>=</span><span> </span><span>System</span><span>.</span><span>Drawing</span><span>.</span><span>ColorTranslator</span><span>.</span><span>FromWin32</span><span>(</span><span>point</span><span>.</span><span>Color</span><span>);</span><span>
        </span><span>String</span><span> pointDescription </span><span>=</span><span> </span><span>String</span><span>.</span><span>Format</span><span>(</span><span>"({0}, {1}, {2}, {3}"</span><span>,</span><span> point</span><span>.</span><span>X</span><span>,</span><span> point</span><span>.</span><span>Y</span><span>,</span><span> point</span><span>.</span><span>Z</span><span>,</span><span> color</span><span>.</span><span>ToString</span><span>());</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

<table summary="" id="GUID-B80DBCF1-56A8-4864-A0CD-181466E0EDE8__TABLE_72DCC06A0A54449CBFBFCD95C5F54FC0"><tbody><tr><td><b>Code Region: Reading point cloud points by pointer</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>unsafe</span><span> </span><span>void</span><span> </span><span>GetPointCloudDataByPointer</span><span>(</span><span>PointCloudInstance</span><span> pcInstance</span><span>,</span><span> </span><span>PointCloudFilter</span><span> pointCloudFilter</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>double</span><span> averageDistance </span><span>=</span><span> </span><span>0.001</span><span>;</span><span>
    </span><span>PointCollection</span><span> points </span><span>=</span><span> pcInstance</span><span>.</span><span>GetPoints</span><span>(</span><span>pointCloudFilter</span><span>,</span><span> averageDistance</span><span>,</span><span> </span><span>10000</span><span>);</span><span>
    </span><span>CloudPoint</span><span>*</span><span> pointBuffer </span><span>=</span><span> </span><span>(</span><span>CloudPoint</span><span>*)</span><span>points</span><span>.</span><span>GetPointBufferPointer</span><span>().</span><span>ToPointer</span><span>();</span><span>
    </span><span>int</span><span> totalCount </span><span>=</span><span> points</span><span>.</span><span>Count</span><span>;</span><span>
    </span><span>for</span><span> </span><span>(</span><span>int</span><span> numberOfPoints </span><span>=</span><span> </span><span>0</span><span>;</span><span> numberOfPoints </span><span>&lt;</span><span> totalCount</span><span>;</span><span> numberOfPoints</span><span>++)</span><span>
    </span><span>{</span><span>
        </span><span>CloudPoint</span><span> point </span><span>=</span><span> </span><span>*(</span><span>pointBuffer </span><span>+</span><span> numberOfPoints</span><span>);</span><span>
        </span><span>// Process each point</span><span>
        </span><span>System</span><span>.</span><span>Drawing</span><span>.</span><span>Color</span><span> color </span><span>=</span><span> </span><span>System</span><span>.</span><span>Drawing</span><span>.</span><span>ColorTranslator</span><span>.</span><span>FromWin32</span><span>(</span><span>point</span><span>.</span><span>Color</span><span>);</span><span>
        </span><span>String</span><span> pointDescription </span><span>=</span><span> </span><span>String</span><span>.</span><span>Format</span><span>(</span><span>"({0}, {1}, {2}, {3}"</span><span>,</span><span> point</span><span>.</span><span>X</span><span>,</span><span> point</span><span>.</span><span>Y</span><span>,</span><span> point</span><span>.</span><span>Z</span><span>,</span><span> color</span><span>.</span><span>ToString</span><span>());</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Filters

Filters are used both to limit the volume which is searched when reading points, and also to govern the display of point clouds. A PointCloudFilter can be created based upon a collection of planar boundaries. The filter will check whether a point is located on the “positive” side of each input plane, as indicated by the positive direction of the plane normal. Therefore, such filter implicitly defines a volume, which is the intersection of the positive half-spaces corresponding to all the planes. This volume does not have to be closed, but it will always be convex.

The display of point clouds can be controlled by assigning a filter to:

-   PointCloudInstance.SetSelectionFilter()

Display of the filtered points will be based on the value of the property:

-   PointCloudInstance.FilterAction

If it is set to None, the selection filter is ignored. If it is set to Highlight, points that pass the filter are highlighted. If it is set to Isolate, only points that pass the filter will be visible.

The following example will highlight a subset of the points in a point cloud based on its bounding box.

<table summary="" id="GUID-B80DBCF1-56A8-4864-A0CD-181466E0EDE8__TABLE_E6BC7B0EA75A43AC9E567DD0EF1C5F08"><tbody><tr><td><b>Code Region: Reading point cloud points by pointer</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>PointCloudFilter</span><span> </span><span>ReadPointCloud</span><span>(</span><span>PointCloudInstance</span><span> pointCloudInstance</span><span>)</span><span>
</span><span>{</span><span>
 </span><span>// Filter will match 1/8 of the overall point cloud</span><span>
 </span><span>// Use the bounding box (filter coordinates are in the coordinates of the model)</span><span>
 </span><span>BoundingBoxXYZ</span><span> boundingBox </span><span>=</span><span> pointCloudInstance</span><span>.</span><span>get_BoundingBox</span><span>(</span><span>null</span><span>);</span><span>
 </span><span>List</span><span>&lt;</span><span>Plane</span><span>&gt;</span><span> planes </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Plane</span><span>&gt;();</span><span>
 XYZ midpoint </span><span>=</span><span> </span><span>(</span><span>boundingBox</span><span>.</span><span>Min</span><span> </span><span>+</span><span> boundingBox</span><span>.</span><span>Max</span><span>)</span><span> </span><span>/</span><span> </span><span>2.0</span><span>;</span><span>

 </span><span>// X boundaries</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> boundingBox</span><span>.</span><span>Min</span><span>));</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(-</span><span>XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> midpoint</span><span>));</span><span>

 </span><span>// Y boundaries</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>XYZ</span><span>.</span><span>BasisY</span><span>,</span><span> boundingBox</span><span>.</span><span>Min</span><span>));</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(-</span><span>XYZ</span><span>.</span><span>BasisY</span><span>,</span><span> midpoint</span><span>));</span><span>

 </span><span>// Z boundaries</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>XYZ</span><span>.</span><span>BasisZ</span><span>,</span><span> boundingBox</span><span>.</span><span>Min</span><span>));</span><span>
 planes</span><span>.</span><span>Add</span><span>(</span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(-</span><span>XYZ</span><span>.</span><span>BasisZ</span><span>,</span><span> midpoint</span><span>));</span><span>

 </span><span>// Create filter</span><span>
 </span><span>PointCloudFilter</span><span> filter </span><span>=</span><span> </span><span>PointCloudFilterFactory</span><span>.</span><span>CreateMultiPlaneFilter</span><span>(</span><span>planes</span><span>);</span><span>
 pointCloudInstance</span><span>.</span><span>FilterAction</span><span> </span><span>=</span><span> </span><span>SelectionFilterAction</span><span>.</span><span>Highlight</span><span>;</span><span>

 </span><span>return</span><span> filter</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

This is the result when the sample above is run on a small pipe point cloud:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/PointCloudHighlight.jpg)**Figure: Point cloud with selection filter**

The Selection.PickBox() method which invokes a general purpose two-click editor that lets the user to specify a rectangular area on the screen can be used in conjunction with a PointCloudFilter by using the resulting PickedBox to generate the planar boundaries of the filter.

### Scans

An .rcp file can contain multiple scans. The method PointCloudInstance.GetScans() returns a list of scan names which can be used to set visibility and fixed color overrides independently for each scan in the PointCloudInstance. PointCloudInstance.ContainsScan() indicates whether the given scan name is contained in the point cloud instance while PointCloudInstance.GetScanOrigin() will return the origin of the given scan in model coordinates.

### Regions

Scan regions are specific to Autodesk ReCap™. If a point cloud was created in ReCap, it may have regions. PointCloudInstance.GetRegions() returns a list of region names which can be used to set visibility and fixed color overrides independently for each region in the PointCloudInstance.

`PointCloudType.GetReCapProject()` provides a direct entry point to get access to an object from the ReCap SDK (`ReCapWrapper.RCProject`) from Revit. This object represents the point cloud from the RC file path stored in `PointCloudType`. The ReCap assembly ReCapWrapper.dll will need to be included into code using this method. The coordinate system in RCProject is defined by the Point Cloud. Please refer to ReCap SDK documentation for `RCProject.getCoordinateSystem()`. If you need points converted to the modeling coordinate system in Revit, you can obtain the transformation matrix from `PointCloudInstance.GetTransform()`.

### Overrides

Point cloud override settings assigned to a given view can be modified using the Revit API. These settings correspond to the settings on the Point Clouds tab of the Visibility/Graphics Overrides task pane in the Revit UI. Overrides can be applied to an entire point cloud instance, or to specific scans within that instance. Options for the overrides include setting visibility for scans in the point cloud instance, setting it to a fixed color, or to color gradients based on elevation, normals, or intensity. The property PointCloudInstance.SupportsOverrides identifies point clouds which support override settings (clouds which are based on .rcp or .rcs files).

The following classes are involved in setting the overrides for point clouds:

-   **PointCloudOverrides** - Used to get or set the PointCloudOverrideSettings for a PointCloudInstance, one of its scans, or for a particular region within the PointCloudInstance.
-   **PointCloudOverrideSettings** - Used to get or set the visibility, color mode, and PointCloudColorSettings.
-   **PointCloudColorSettings** - Used to assign specific colors for certain color modes to a PointCloudInstance element, or one of its scans. Does not apply if the PointCloudColorMode is NoOverride or Normals.


<!-- ===== END: Help  Point Cloud Client  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Point Cloud Engine  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:43 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Point_Clouds_Point_Cloud_Engine_html
author: 
---

# Help | Point Cloud Engine | Autodesk

> ## Excerpt
> A custom point cloud engine can be implemented to supply cloud points to Revit.

---
A custom point cloud engine can be implemented to supply cloud points to Revit.

A point cloud engine can be file-based or non-file-based. A file-based implementation requires that each point cloud be mapped to a single file on disk. Revit will allow users to create new point cloud instances in a document directly by selecting point cloud files whose extension matches the engine identifier. These files are treated as external links in Revit and may be reloaded and remapped when necessary from the Manage Links dialog.

A non-file-based engine implementation may obtain point clouds from anywhere (e.g. from a database, from a server, or from one part of a larger aggregate file). Because there is no file that the user may select, Revit's user interface will not allow a user to create a point cloud of this type. Instead, the engine provider supplies a custom command using PointCloudType.Create() and PointCloudInstance.Create() to create and place point clouds of this type. The Manage Links dialog will show the point clouds of this type, but since there is no file associated with the point cloud, the user cannot manage, reload or remap point clouds of this type.

Regardless of the type of implementation, a custom engine implementation consists of the following:

-   An implementation of IPointCloudEngine registered with Revit via the PointCloudEngineRegistry.
-   An implementation of IPointCloudAccess which will respond to inquiries from Revit regarding the properties of a single point cloud.
-   An implementation of IPointSetIterator which will return sets of points to Revit when requested.

In order to supply the points of the point cloud to Revit, there are two ReadPoints() methods which must be implemented:

-   IPointCloudAccess.ReadPoints() - this provides a single set of points in a one-time call, either from Revit or the API. Revit uses this during some display activities including selection pre-highlighting. It is also possible for API clients to call this method directly via PointCloudInstance.GetPoints().
-   IPointSetIterator.ReadPoints() - this provides a subset of points as a part of a larger iteration of points in the cloud. Revit uses this method during normal display of the point cloud; quantities of points will be requested repeatedly until it obtains enough points or until something in the display changes. The engine implementation must keep track of which points have been returned to Revit during any given point set iteration.

See the PointCloudEngine folder under the Samples directory included with the Revit API SDK for a complete example of registering and implementing both file-based and non-file-based point cloud engines.


<!-- ===== END: Help  Point Cloud Engine  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Transport Layer Security  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:47 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_TransportLayerSecurity_html
author: 
---

# Help | Transport Layer Security | Autodesk

> ## Excerpt
> When your add-on requires Internet communications and a specific security protocol is involved, if the protocol is TLS 1.0, 1.1 or 1.2 do not write any setting in the add-on. Instead take advantage of the native TLS support in Revit and its target .NET Framework. The complexities due to variety of Windows versions as well as .NET Framework versions have been handled in Revit.

---
When your add-on requires Internet communications and a specific security protocol is involved, if the protocol is TLS 1.0, 1.1 or 1.2 do not write any setting in the add-on. Instead take advantage of the native TLS support in Revit and its target .NET Framework. The complexities due to variety of Windows versions as well as .NET Framework versions have been handled in Revit.

If the add-on needs to specify a security protocol or its version, do not hard-code it exclusively, e.g. by directly assigning the protocol/version to the application-wide property `ServicePointManager.SecurityProtocol`. This will override Revit's native TLS configuration, which is critical for Revit to communicate with various Autodesk cloud services.

A **problematic** usage is `System.Net.ServicePointManager.SecurityProtocol = System.Net.SecurityProtocolType.Tls12;`

Instead, specify the protocol/version inclusively, e.g. by using bitwise OR (logical OR) on the application-wide property ServicePointManager.SecurityProtocol.

A **correct** usage is `System.Net.ServicePointManager.SecurityProtocol |= System.Net.SecurityProtocolType.Tls12;`


<!-- ===== END: Help  Transport Layer Security  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Window Handle  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:51 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Window_Handle_html
author: 
---

# Help | Window Handle | Autodesk

> ## Excerpt
> Two properties allow access to the handle of the Revit main window:

---
Two properties allow access to the handle of the Revit main window:

-   Autodesk.Revit.UI.UIApplication.MainWindowHandle
-   Autodesk.Revit.UI.UIControlledApplication.MainWindowHandle

This handle should be used when displaying modal dialogs and message windows to insure that they are properly parented. Use these properties instead of System.Diagnostics.Process.GetCurrentProcess().MainWindowHandle, which is not a reliable method for retrieving the main window handle.

**Parent page:** [Advanced Topics](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_html)


<!-- ===== END: Help  Window Handle  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Worksharing  Autodesk.md ===== -->

---
created: 2026-01-28T21:19:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_html
author: 
---

# Help | Worksharing | Autodesk

> ## Excerpt
> Worksharing is a design method that allows multiple team members to work on the same project model at the same time. When worksharing is enabled, a Revit document can be subdivided into worksets, which are collections of elements in the project.

---
Worksharing is a design method that allows multiple team members to work on the same project model at the same time. When worksharing is enabled, a Revit document can be subdivided into worksets, which are collections of elements in the project.

**Pages in this section**

-   [Worksharing Overview](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Worksharing_Overview_html)
-   [Worksets](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Worksets_html)
-   [Elements in Worksets](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Elements_in_Worksets_html)
-   [Editing Elements in Worksets](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Editing_Elements_in_Worksets_html)
-   [Opening a Workshared Document](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Opening_a_Workshared_Document_html)
-   [Visibility and Display](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Visibility_and_Display_html)
-   [Workshared File Management](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Workshared_File_Management_html)

**Parent page:** [Advanced Topics](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_html)


<!-- ===== END: Help  Worksharing  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Worksharing Overview  Autodesk.md ===== -->

---
created: 2026-01-28T21:20:00 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Worksharing_Overview_html
author: 
---

# Help | Worksharing Overview | Autodesk

> ## Excerpt
> When creating add-ins for Revit, it is important to understand how documents function in a workshared environment. Whether the file is local, central or managed by Revit server affects how changes to the model will impact other users, or whether a model is potentially out of date or has worksets locked by another user.

---
When creating add-ins for Revit, it is important to understand how documents function in a workshared environment. Whether the file is local, central or managed by Revit server affects how changes to the model will impact other users, or whether a model is potentially out of date or has worksets locked by another user.

## Workflow

This is the worksharing workflow from a high level perspective. When the user opens a central model, they get a local copy of the model. When they edit elements, the elements are checked out from the central model so that no one else can edit them. Local changes are only committed to the central model when a Synchronize with Central is performed. Once committed, other users can get the changes by performing a Reload Latest.

## Worksets

Elements are placed in worksets. An entire workset can be checked out so that the user has exclusive editing rights to all the elements in the workset. If new elements are added, they are placed in the active workset in the local model.

Specific worksets can be opened with the model. Only opened worksets are visible, but all elements are available in the model. A workshared model may also be open "detached", in which there is no possibility of updating the central model. In this case, no workset management is required.

## Worksharing types

There are three types of worksharing:

-   **File-based** - The central model is accessible on disk over the network
-   **Server-based** - Revit server manages the central model and possibly locally available accelerators
-   **Cloud-based** - Uses the Revit Cloud Worksharing service to author Revit models in the cloud concurrently with other team members


<!-- ===== END: Help  Worksharing Overview  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Worksets  Autodesk.md ===== -->

---
created: 2026-01-28T21:20:05 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Worksets_html
author: 
---

# Help | Worksets | Autodesk

> ## Excerpt
> Worksets are a way to divide a set of elements in the Revit document into subsets for worksharing. There may be one or many worksets in a document.

---
Worksets are a way to divide a set of elements in the Revit document into subsets for worksharing. There may be one or many worksets in a document.

## Accessing worksets in the document

The document contains a WorksetTable which is a table containing references to all the worksets contained in that document. There is one WorksetTable for each document. There will be at least one default workset in the table, even if worksharing has not been enabled in the document. The Document.IsWorkshared property can be used to determine if worksharing has been enabled in the document. The WorksetTable class can be used to get the active workset (as shown in the example below) and to set the active workset, by calling SetActiveWorksetId()

<table summary="" id="GUID-4BC148EC-6288-495A-A6DD-1524F326B32C__TABLE_CF10A43D2F08444BA805431BFDFBA24F"><tbody><tr><td><b>Code Region: Get Active Workset</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Workset</span><span> </span><span>GetActiveWorkset</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
     </span><span>// Get the workset table from the document</span><span>
     </span><span>WorksetTable</span><span> worksetTable </span><span>=</span><span> doc</span><span>.</span><span>GetWorksetTable</span><span>();</span><span>
     </span><span>// Get the Id of the active workset</span><span>
     </span><span>WorksetId</span><span> activeId </span><span>=</span><span> worksetTable</span><span>.</span><span>GetActiveWorksetId</span><span>();</span><span>
     </span><span>// Find the workset with that Id</span><span>
     </span><span>Workset</span><span> workset </span><span>=</span><span> worksetTable</span><span>.</span><span>GetWorkset</span><span>(</span><span>activeId</span><span>);</span><span>
     </span><span>return</span><span> workset</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Filtering worksets

Since the Workset class is not derived from Element, use FilteredWorksetCollector to search, filter and iterate through a set of worksets. Conditions can be assigned to filter the worksets that are returned. If no condition is applied, this filter will access all of the worksets in the document. The WorksetKind enumerator is useful for filtering worksets as shown in the next example. The WorksetKind identifies the subdivision of worksets:

-   **User** - user managed worksets for 3D instance elements
-   **Family** - where family symbols & families are kept
-   **Standard** - where project standards live including system family types
-   **Other** - internally used worksets which should not typically be considered by applications
-   **View** - contain views and view-specific elements

<table summary="" id="GUID-4BC148EC-6288-495A-A6DD-1524F326B32C__TABLE_90B564C0C5184D3B9D796E987FC5E2F8"><tbody><tr><td><b>Code Region: Filtering Worksets</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetWorksetsInfo</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>String</span><span> message </span><span>=</span><span> </span><span>String</span><span>.</span><span>Empty</span><span>;</span><span>
    </span><span>// Enumerating worksets in a document and getting basic information for each</span><span>
    </span><span>FilteredWorksetCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredWorksetCollector</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// find all user worksets</span><span>
    collector</span><span>.</span><span>OfKind</span><span>(</span><span>WorksetKind</span><span>.</span><span>UserWorkset</span><span>);</span><span>
    </span><span>IList</span><span>&lt;</span><span>Workset</span><span>&gt;</span><span> worksets </span><span>=</span><span> collector</span><span>.</span><span>ToWorksets</span><span>();</span><span>

    </span><span>// get information for each workset</span><span>
    </span><span>int</span><span> count </span><span>=</span><span> </span><span>3</span><span>;</span><span> </span><span>// show info for 3 worksets only</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Workset</span><span> workset </span><span>in</span><span> worksets</span><span>)</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"Workset : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>Name</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nUnique Id : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>UniqueId</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nOwner : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>Owner</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nKind : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>Kind</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nIs default : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>IsDefaultWorkset</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nIs editable : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>IsEditable</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nIs open : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>IsOpen</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nIs visible by default : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>IsVisibleByDefault</span><span>;</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"GetWorksetsInfo"</span><span>,</span><span> message</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>==</span><span> </span><span>--</span><span>count</span><span>)</span><span>
            </span><span>break</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Workset properties

The Workset class represents a workset in a Revit document. As is shown in the filtering worksets example above, the Workset class provides many properties to get information about a given workset, such as the owner and whether or not the workset is editable. These properties are read-only. To change the name of an existing workset, use the static method WorksetTable.RenameWorkset().

## Creating worksets

The static Workset.Create() method can be used to create a new workset in a given document with a specified name. Worksets can only be created in a document that has worksharing enabled and the name must be unique. The static method WorksetTable.IsWorksetNameUnique() will confirm if a given name is unique in the document. The following example demonstrates how to create a new workset.

<table summary="" id="GUID-4BC148EC-6288-495A-A6DD-1524F326B32C__TABLE_8BCDCF63042C4D0199A4E6312122F8A7"><tbody><tr><td><b>Code Region: Create a new workset</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Workset</span><span> </span><span>CreateWorkset</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Workset</span><span> newWorkset </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>// Worksets can only be created in a document with worksharing enabled</span><span>
    </span><span>if</span><span> </span><span>(</span><span>document</span><span>.</span><span>IsWorkshared</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>string</span><span> worksetName </span><span>=</span><span> </span><span>"New Workset"</span><span>;</span><span>
        </span><span>// Workset name must not be in use by another workset</span><span>
        </span><span>if</span><span> </span><span>(</span><span>WorksetTable</span><span>.</span><span>IsWorksetNameUnique</span><span>(</span><span>document</span><span>,</span><span> worksetName</span><span>))</span><span>
        </span><span>{</span><span>
            </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> worksetTransaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Set preview view id"</span><span>))</span><span>
            </span><span>{</span><span>
                worksetTransaction</span><span>.</span><span>Start</span><span>();</span><span>
                newWorkset </span><span>=</span><span> </span><span>Workset</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> worksetName</span><span>);</span><span>
                worksetTransaction</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> newWorkset</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Worksets  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Elements in Worksets  Autodesk.md ===== -->

---
created: 2026-01-28T21:20:10 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Elements_in_Worksets_html
author: 
---

# Help | Elements in Worksets | Autodesk

> ## Excerpt
> Each element in the document must belong to one and only one workset. Each element has a WorksetId which identifies the unique workset to which it belongs. Additionally, given a WorksetId, it is possible to get all of the elements in the document belonging to that Workset using the ElementWorksetFilter as shown below.

---
Each element in the document must belong to one and only one workset. Each element has a WorksetId which identifies the unique workset to which it belongs. Additionally, given a WorksetId, it is possible to get all of the elements in the document belonging to that Workset using the ElementWorksetFilter as shown below.

<table summary="" id="GUID-FD80EF04-2BCD-4E43-8079-2AE408A5B294__TABLE_3521C75C989842588436FAD539F80993"><tbody><tr><td><b>Code Region: ElementWorksetFilter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>WorksetElements</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>Workset</span><span> workset</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// filter all elements that belong to the given workset</span><span>
    </span><span>FilteredElementCollector</span><span> elementCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    </span><span>ElementWorksetFilter</span><span> elementWorksetFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementWorksetFilter</span><span>(</span><span>workset</span><span>.</span><span>Id</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> worksetElemsfounds </span><span>=</span><span> elementCollector</span><span>.</span><span>WherePasses</span><span>(</span><span>elementWorksetFilter</span><span>).</span><span>ToElements</span><span>();</span><span>

    </span><span>// how many elements were found?</span><span>
    </span><span>int</span><span> elementsCount </span><span>=</span><span> worksetElemsfounds</span><span>.</span><span>Count</span><span>;</span><span>
    </span><span>String</span><span> message </span><span>=</span><span> </span><span>"Element count : "</span><span> </span><span>+</span><span> elementsCount</span><span>;</span><span>

    </span><span>// Get name and/or Id of the elements that pass the given filter and show a few of them</span><span>
    </span><span>int</span><span> count </span><span>=</span><span> </span><span>5</span><span>;</span><span>  </span><span>// show info for 5 elements only</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> ele </span><span>in</span><span> worksetElemsfounds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> ele</span><span>)</span><span>
        </span><span>{</span><span>
             message </span><span>+=</span><span> </span><span>"\nElementId : "</span><span> </span><span>+</span><span> ele</span><span>.</span><span>Id</span><span>;</span><span>
             message </span><span>+=</span><span> </span><span>", Element Name : "</span><span> </span><span>+</span><span> ele</span><span>.</span><span>Name</span><span>;</span><span>

             </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>==</span><span> </span><span>--</span><span>count</span><span>)</span><span>
                  </span><span>break</span><span>;</span><span>
         </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"ElementsOfWorkset"</span><span>,</span><span> message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

New elements are automatically placed in the active workset in the user's local copy of the model. Since the WorksetId for an element is a read only property, use the parameter ELEM\_PARTITION\_PARAM. The following example demonstrates the creation of an element that is changed to belong to a different workset.

<table summary="" id="GUID-FD80EF04-2BCD-4E43-8079-2AE408A5B294__TABLE_C0E859D67C9A4F1C9813F44952D97642"><tbody><tr><td><b>Code Region: Changing a new element's workset</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ChangeWorkset</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>String</span><span> targetWorksetName </span><span>=</span><span> </span><span>"Target workset"</span><span>;</span><span>

    </span><span>//Find target workset</span><span>
    </span><span>FilteredWorksetCollector</span><span> worksetCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredWorksetCollector</span><span>(</span><span>doc</span><span>);</span><span>
    worksetCollector</span><span>.</span><span>OfKind</span><span>(</span><span>WorksetKind</span><span>.</span><span>UserWorkset</span><span>);</span><span>
    </span><span>Workset</span><span> workset </span><span>=</span><span> worksetCollector</span><span>.</span><span>FirstOrDefault</span><span>&lt;</span><span>Workset</span><span>&gt;(</span><span>ws </span><span>=&gt;</span><span> ws</span><span>.</span><span>Name</span><span> </span><span>==</span><span> targetWorksetName</span><span>);</span><span>

    </span><span>// Workset not found, abort</span><span>
    </span><span>if</span><span> </span><span>(</span><span>workset </span><span>==</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span> dialog </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Error"</span><span>);</span><span>
        dialog</span><span>.</span><span>MainInstruction</span><span> </span><span>=</span><span> </span><span>String</span><span>.</span><span>Format</span><span>(</span><span>"There is no workset named {0} in the document. Aborting this operation."</span><span>,</span><span> targetWorksetName</span><span>);</span><span>
        dialog</span><span>.</span><span>MainIcon</span><span> </span><span>=</span><span> </span><span>TaskDialogIcon</span><span>.</span><span>TaskDialogIconWarning</span><span>;</span><span>
        dialog</span><span>.</span><span>Show</span><span>();</span><span>
        </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>// Find "Level 1" for the new wall</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Level</span><span>));</span><span>
    </span><span>Level</span><span> level </span><span>=</span><span> collector</span><span>.</span><span>Cast</span><span>&lt;</span><span>Level</span><span>&gt;().</span><span>First</span><span>&lt;</span><span>Level</span><span>&gt;(</span><span>lvl </span><span>=&gt;</span><span> lvl</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Level 1"</span><span>);</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Add elements by API"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// Create the wall</span><span>
        </span><span>Wall</span><span> wall </span><span>=</span><span> </span><span>Wall</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>25</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>25</span><span>,</span><span> </span><span>15</span><span>,</span><span> </span><span>0</span><span>)),</span><span> level</span><span>.</span><span>Id</span><span>,</span><span> </span><span>false</span><span>);</span><span>

        </span><span>// Get the parameter that stores the workset id</span><span>
        </span><span>Parameter</span><span> p </span><span>=</span><span> wall</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>ElemPartitionParam</span><span>);</span><span>

        </span><span>// This parameter storage type is Integer</span><span>
        p</span><span>.</span><span>Set</span><span>(</span><span>workset</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>);</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Worksharing information such as the current owner and checkout status of an element can be obtained using the WorksharingUtils class. It is a static class that contains utility functions related to worksharing.

<table summary="" id="GUID-FD80EF04-2BCD-4E43-8079-2AE408A5B294__TABLE_128D32D1D0FB4CFBB7DCCFCC8635C3E0"><tbody><tr><td><b>Code Region: WorksharingUtils</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetElementWorksharingInfo</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>ElementId</span><span> elemId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>String</span><span> message </span><span>=</span><span> </span><span>String</span><span>.</span><span>Empty</span><span>;</span><span>
    message </span><span>+=</span><span> </span><span>"Element Id: "</span><span> </span><span>+</span><span> elemId</span><span>;</span><span>

    </span><span>Element</span><span> elem </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>elemId</span><span>);</span><span>
    </span><span>if</span><span>(</span><span>null</span><span> </span><span>==</span><span> elem</span><span>)</span><span>
    </span><span>{</span><span>
       message </span><span>+=</span><span> </span><span>"Element does not exist"</span><span>;</span><span>
       </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>// The workset the element belongs to</span><span>
    </span><span>WorksetId</span><span> worksetId </span><span>=</span><span> elem</span><span>.</span><span>WorksetId</span><span>;</span><span>
    message </span><span>+=</span><span> </span><span>(</span><span>"\nWorkset Id : "</span><span> </span><span>+</span><span> worksetId</span><span>.</span><span>ToString</span><span>());</span><span>

    </span><span>// Model Updates Status of the element</span><span>
    </span><span>ModelUpdatesStatus</span><span> updateStatus </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>GetModelUpdatesStatus</span><span>(</span><span>doc</span><span>,</span><span> elemId</span><span>);</span><span>
    message </span><span>+=</span><span> </span><span>(</span><span>"\nUpdate status : "</span><span> </span><span>+</span><span> updateStatus</span><span>.</span><span>ToString</span><span>());</span><span>

    </span><span>// Checkout Status of the element</span><span>
    </span><span>CheckoutStatus</span><span> checkoutStatus </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>GetCheckoutStatus</span><span>(</span><span>doc</span><span>,</span><span> elemId</span><span>);</span><span>
    message </span><span>+=</span><span> </span><span>(</span><span>"\nCheckout status : "</span><span> </span><span>+</span><span> checkoutStatus</span><span>.</span><span>ToString</span><span>());</span><span>

    </span><span>// Getting WorksharingTooltipInfo of a given element Id</span><span>
    </span><span>WorksharingTooltipInfo</span><span> tooltipInfo </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>GetWorksharingTooltipInfo</span><span>(</span><span>doc</span><span>,</span><span> elemId</span><span>);</span><span>
    message </span><span>+=</span><span> </span><span>(</span><span>"\nCreator : "</span><span> </span><span>+</span><span> tooltipInfo</span><span>.</span><span>Creator</span><span>);</span><span>
    message </span><span>+=</span><span> </span><span>(</span><span>"\nCurrent Owner : "</span><span> </span><span>+</span><span> tooltipInfo</span><span>.</span><span>Owner</span><span>);</span><span>
    message </span><span>+=</span><span> </span><span>(</span><span>"\nLast Changed by : "</span><span> </span><span>+</span><span> tooltipInfo</span><span>.</span><span>LastChangedBy</span><span>);</span><span>

    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"GetElementWorksharingInfo"</span><span>,</span><span> message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Elements in Worksets  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Editing Elements in Worksets  Autodesk.md ===== -->

---
created: 2026-01-28T21:20:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Editing_Elements_in_Worksets_html
author: 
---

# Help | Editing Elements in Worksets | Autodesk

> ## Excerpt
> Users working in teams can encounter usability issues with Revit API add-ins beyond what a single user might experience. In particular, how an add-in is designed can prevent or create editing conflicts. For example, if an add-in attempts to edit thousands of elements, all of those elements will need to be checked out to the local user and will be unavailable to other users until a synchronize with central is performed. Or some of the elements may be checked out to other users and unavailable to be edited. This is important to keep in mind when making changes to a workshared model from the API.

---
## Overview

Users working in teams can encounter usability issues with Revit API add-ins beyond what a single user might experience. In particular, how an add-in is designed can prevent or create editing conflicts. For example, if an add-in attempts to edit thousands of elements, all of those elements will need to be checked out to the local user and will be unavailable to other users until a synchronize with central is performed. Or some of the elements may be checked out to other users and unavailable to be edited. This is important to keep in mind when making changes to a workshared model from the API.

The basic model editing workflow goes like this:

| Action | Example | Why this is important |
| --- | --- | --- |
| The user changes some elements in the model | User drags a wall | These changes are "user changes". The user must borrow these elements to make the change. |
| Revit regenerates additional data in the model as needed | Joined walls move, floor updates, roof updates, room updates, room tags check if they're still in their rooms | These changes are "system changes". Even though they are changed, they are still available to other users. |

Most API changes are "user changes" and are treated the same as if the local user made the changes manually. This is the case whether called from an External Command, a macro, or an event. The one exception is that changes made from updaters are treated as system changes. .

## Element Ownership

One way to address worksharing issues that may arise from attempting to edit an element in a workshared document is to set up FailureHandlingOptions for the transaction used to edit the element. This allows for catching and suppressing editing errors automatically and rollback the changes as shown below:

<table summary="" id="GUID-60C319EC-6CC7-4FC3-B004-10266B8879AD__TABLE_53F78D156D72490EA87C59131F3476AA"><tbody><tr><td><b>Code Region: Suppressing worksharing errors</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>TryToEditGeometricElement</span><span>(</span><span>Element</span><span> elem</span><span>,</span><span> </span><span>bool</span><span> useFailureHandlingOpts</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> elem</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>MakeTransaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Move element"</span><span>,</span><span> useFailureHandlingOpts</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>ElementTransformUtils</span><span>.</span><span>MoveElement</span><span>(</span><span>doc</span><span>,</span><span> elem</span><span>.</span><span>Id</span><span>,</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>));</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>static</span><span> </span><span>Transaction</span><span> </span><span>MakeTransaction</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>string</span><span> name</span><span>,</span><span> </span><span>bool</span><span> useFailureHandlingOpts</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> name</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>useFailureHandlingOpts</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>FailureHandlingOptions</span><span> opts </span><span>=</span><span> t</span><span>.</span><span>GetFailureHandlingOptions</span><span>();</span><span>
        opts</span><span>.</span><span>SetClearAfterRollback</span><span>(</span><span>true</span><span>);</span><span>
        opts</span><span>.</span><span>SetFailuresPreprocessor</span><span>(</span><span>new</span><span> </span><span>WorksharingErrorsPreprocessor</span><span>());</span><span>
        t</span><span>.</span><span>SetFailureHandlingOptions</span><span>(</span><span>opts</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> t</span><span>;</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>class</span><span> </span><span>WorksharingErrorsPreprocessor</span><span> </span><span>:</span><span> </span><span>IFailuresPreprocessor</span><span>
</span><span>{</span><span>
    </span><span>FailureProcessingResult</span><span> </span><span>IFailuresPreprocessor</span><span>.</span><span>PreprocessFailures</span><span>(</span><span>FailuresAccessor</span><span> failuresAccessor</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> </span><span>FailureProcessingResult</span><span>.</span><span>Continue</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The WorksharingUtils class can be used to modify element and workset ownership. The CheckoutElements() method obtains ownership for the current user of as many specified elements as possible, while the CheckoutWorksets() method does the same for worksets. These methods are useful for attempting to checkout elements prior to performing edits. Editing is limited to elements and worksets the user owns until Reload Latest or Synchronize with Central is conducted after the model is opened. The RelinquishOwnership() method relinquishes elements and worksets owned by the current user based on the specified RelinquishOptions.

For best performance, checkout all elements or worksets and relinquish items in one big call, rather than many small calls. However, when working on a cloud model and checking out a large number of elements in one request `CheckoutElementsRequestTooLargeException` may be thrown. Checking out corresponding worksets is recommended in this case.

Note: When checking out an element, Revit may check out additional elements that are needed to make the requested element editable. For example, if an element is in a group, Revit will checkout the entire group. The following example tries to checkout the given element prior to editing and issues a message to the user if there is an issue.

<table summary="" id="GUID-60C319EC-6CC7-4FC3-B004-10266B8879AD__TABLE_6A4F60A8DF3A41EB994DB9AE027BE3BB"><tbody><tr><td><b>Code Region: Checkout elements</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>bool</span><span> </span><span>AttemptToCheckoutInAdvance</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> element</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>String</span><span> categoryName </span><span>=</span><span> element</span><span>.</span><span>Category</span><span>.</span><span>Name</span><span>;</span><span>

    </span><span>// Checkout attempt</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> checkedOutIds </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>CheckoutElements</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>[]</span><span> </span><span>{</span><span> element</span><span>.</span><span>Id</span><span> </span><span>});</span><span>

    </span><span>// Confirm checkout</span><span>
    </span><span>bool</span><span> checkedOutSuccessfully </span><span>=</span><span> checkedOutIds</span><span>.</span><span>Contains</span><span>(</span><span>element</span><span>.</span><span>Id</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(!</span><span>checkedOutSuccessfully</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Element is not checked out"</span><span>,</span><span> </span><span>"Cannot edit the "</span><span> </span><span>+</span><span> categoryName </span><span>+</span><span> </span><span>" element - "</span><span> </span><span>+</span><span>
                        </span><span>"it was not checked out successfully and may be checked out to another."</span><span>);</span><span>
        </span><span>return</span><span> </span><span>false</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>// If element is updated in central or deleted in central, it is not editable</span><span>
    </span><span>ModelUpdatesStatus</span><span> updatesStatus </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>GetModelUpdatesStatus</span><span>(</span><span>doc</span><span>,</span><span> element</span><span>.</span><span>Id</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>updatesStatus </span><span>==</span><span> </span><span>ModelUpdatesStatus</span><span>.</span><span>DeletedInCentral</span><span> </span><span>||</span><span> updatesStatus </span><span>==</span><span> </span><span>ModelUpdatesStatus</span><span>.</span><span>UpdatedInCentral</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Element is not up to date"</span><span>,</span><span> </span><span>"Cannot edit the "</span><span> </span><span>+</span><span> categoryName </span><span>+</span><span> </span><span>" element - "</span><span> </span><span>+</span><span>
                        </span><span>"it is not up to date with central, but it is checked out."</span><span>);</span><span>
        </span><span>return</span><span> </span><span>false</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>true</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The next example demonstrates checking out all the view worksets.

<table summary="" id="GUID-60C319EC-6CC7-4FC3-B004-10266B8879AD__TABLE_8E8E8E20F5564599ABEA39F50C145D21"><tbody><tr><td><b>Code Region: Checkout worksets</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>CheckoutAllViewWorksets</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredWorksetCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredWorksetCollector</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// find all view worksets</span><span>
    collector</span><span>.</span><span>OfKind</span><span>(</span><span>WorksetKind</span><span>.</span><span>ViewWorkset</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>WorksetId</span><span>&gt;</span><span> viewworksets </span><span>=</span><span> collector</span><span>.</span><span>ToWorksetIds</span><span>();</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>WorksetId</span><span>&gt;</span><span> checkoutworksets </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>CheckoutWorksets</span><span>(</span><span>doc</span><span>,</span><span> viewworksets</span><span>);</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Checked out worksets"</span><span>,</span><span> </span><span>"Number of worksets checked out: "</span><span> </span><span>+</span><span> checkoutworksets</span><span>.</span><span>Count</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Editing Elements in Worksets  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Opening a Workshared Document  Autodesk.md ===== -->

---
created: 2026-01-28T21:20:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Opening_a_Workshared_Document_html
author: 
---

# Help | Opening a Workshared Document | Autodesk

> ## Excerpt
> The Application.OpenDocumentFile(ModelPath, OpenOptions) method can be used to set options related to opening a workshared document. In addition to options to detach from the central document or to allow a local file to be opened ReadOnly by a user other than its owner, options may also be set related to worksets. When a workshared document is opened, all system worksets are automatically opened, however user-created worksets can be specified to be opened or closed. Elements in an open workset can be expanded and displayed. However, elements in a closed workset are not displayed to avoid expanding them. By only opening worksets necessary in the current session, Revit's memory footprint is reduced, which can help with performance.

---
The Application.OpenDocumentFile(ModelPath, OpenOptions) method can be used to set options related to opening a workshared document. In addition to options to detach from the central document or to allow a local file to be opened ReadOnly by a user other than its owner, options may also be set related to worksets. When a workshared document is opened, all system worksets are automatically opened, however user-created worksets can be specified to be opened or closed. Elements in an open workset can be expanded and displayed. However, elements in a closed workset are not displayed to avoid expanding them. By only opening worksets necessary in the current session, Revit's memory footprint is reduced, which can help with performance.

In the example below, a document is opened with two worksets specified to be opened. Note that the WorksharingUtils.GetUserWorksetInfo() method can be used to access workset information from a closed Revit document.

<table summary="" id="GUID-F99FBBCC-AE58-46F5-85AF-0A7C3C5C0576__TABLE_FC2899FD121E4503873B3A95C92E0A26"><tbody><tr><td><b>Code Region: Open Workshared Document</b></td></tr><tr><td><pre><code><span>Document</span><span> </span><span>OpenDocumentWithWorksets</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>ModelPath</span><span> projectPath</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>try</span><span>
    </span><span>{</span><span>
        </span><span>// Get info on all the user worksets in the project prior to opening</span><span>
        </span><span>IList</span><span>&lt;</span><span>WorksetPreview</span><span>&gt;</span><span> worksets </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>GetUserWorksetInfo</span><span>(</span><span>projectPath</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>WorksetId</span><span>&gt;</span><span> worksetIds </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>WorksetId</span><span>&gt;();</span><span>
        </span><span>// Find two predetermined worksets</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>WorksetPreview</span><span> worksetPrev </span><span>in</span><span> worksets</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>worksetPrev</span><span>.</span><span>Name</span><span>.</span><span>CompareTo</span><span>(</span><span>"Workset1"</span><span>)</span><span> </span><span>==</span><span> </span><span>0</span><span> </span><span>||</span><span>
                worksetPrev</span><span>.</span><span>Name</span><span>.</span><span>CompareTo</span><span>(</span><span>"Workset2"</span><span>)</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
            </span><span>{</span><span>
                worksetIds</span><span>.</span><span>Add</span><span>(</span><span>worksetPrev</span><span>.</span><span>Id</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>OpenOptions</span><span> openOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>OpenOptions</span><span>();</span><span>
        </span><span>// Setup config to close all worksets by default</span><span>
        </span><span>WorksetConfiguration</span><span> openConfig </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksetConfiguration</span><span>(</span><span>WorksetConfigurationOption</span><span>.</span><span>CloseAllWorksets</span><span>);</span><span>
        </span><span>// Set list of worksets for opening </span><span>
        openConfig</span><span>.</span><span>Open</span><span>(</span><span>worksetIds</span><span>);</span><span>
        openOptions</span><span>.</span><span>SetOpenWorksetsConfiguration</span><span>(</span><span>openConfig</span><span>);</span><span>
        doc </span><span>=</span><span> app</span><span>.</span><span>OpenDocumentFile</span><span>(</span><span>projectPath</span><span>,</span><span> openOptions</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Open File Failed"</span><span>,</span><span> e</span><span>.</span><span>Message</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> doc</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Another option is to open the document while just opening the last viewed worksets.

<table summary="" id="GUID-F99FBBCC-AE58-46F5-85AF-0A7C3C5C0576__TABLE_1DA72F15EB5D4284A4E357B4FC779B2B"><tbody><tr><td><b>Code Region: Open last viewed worksets</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>Document</span><span> </span><span>OpenLastViewed</span><span>(</span><span>UIApplication</span><span> uiApplication</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Application</span><span> application </span><span>=</span><span> uiApplication</span><span>.</span><span>Application</span><span>;</span><span>

    </span><span>// Setup options</span><span>
    </span><span>OpenOptions</span><span> options1 </span><span>=</span><span> </span><span>new</span><span> </span><span>OpenOptions</span><span>();</span><span>

    </span><span>// Default config opens all.  Close all first, then open last viewed to get the correct settings.</span><span>
    </span><span>WorksetConfiguration</span><span> worksetConfig </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksetConfiguration</span><span>(</span><span>WorksetConfigurationOption</span><span>.</span><span>OpenLastViewed</span><span>);</span><span>
    options1</span><span>.</span><span>SetOpenWorksetsConfiguration</span><span>(</span><span>worksetConfig</span><span>);</span><span>

    </span><span>// Open the document</span><span>
    </span><span>Document</span><span> openedDoc </span><span>=</span><span> application</span><span>.</span><span>OpenDocumentFile</span><span>(</span><span>GetWSAPIModelPath</span><span>(</span><span>"WorkaredFileSample.rvt"</span><span>),</span><span> options1</span><span>);</span><span>

    </span><span>return</span><span> openedDoc</span><span>;</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>static</span><span> </span><span>ModelPath</span><span> </span><span>GetWSAPIModelPath</span><span>(</span><span>string</span><span> fileName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Utility to get a local path for a target model file</span><span>
    </span><span>FileInfo</span><span> filePath </span><span>=</span><span> </span><span>new</span><span> </span><span>FileInfo</span><span>(</span><span>Path</span><span>.</span><span>Combine</span><span>(@</span><span>"C:\Documents\Revit Projects"</span><span>,</span><span> fileName</span><span>));</span><span>
    </span><span>ModelPath</span><span> mp </span><span>=</span><span> </span><span>ModelPathUtils</span><span>.</span><span>ConvertUserVisiblePathToModelPath</span><span>(</span><span>filePath</span><span>.</span><span>FullName</span><span>);</span><span>

    </span><span>return</span><span> mp</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following two examples demonstrate how to create a new local first from disk or from a Revit server, and then open it. Note that the sample below uses the GetWSAPIModelPath() method used in the previous example.

<table summary="" id="GUID-F99FBBCC-AE58-46F5-85AF-0A7C3C5C0576__TABLE_162B83853A7241DCAFE8A4D788A3CD74"><tbody><tr><td><b>Code Region: Open new local from disk</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>Document</span><span> </span><span>OpenNewLocalFromDisk</span><span>(</span><span>UIApplication</span><span> uiApplication</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create new local from a disk location</span><span>
    </span><span>ModelPath</span><span> newLocalPath </span><span>=</span><span> </span><span>GetWSAPIModelPath</span><span>(</span><span>"LocalWorksharing.rvt"</span><span>);</span><span>
    </span><span>return</span><span> </span><span>(</span><span>OpenNewLocalFromModelPath</span><span>(</span><span>uiApplication</span><span>.</span><span>Application</span><span>,</span><span> </span><span>GetWSAPIModelPath</span><span>(</span><span>"NewLocalWorksharing.rvt"</span><span>),</span><span> newLocalPath</span><span>));</span><span>
</span><span>}</span><span>

</span><span>private</span><span> </span><span>static</span><span> </span><span>Document</span><span> </span><span>OpenNewLocalFromModelPath</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>ModelPath</span><span> centralPath</span><span>,</span><span> </span><span>ModelPath</span><span> localPath</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create the new local at the given path</span><span>
    </span><span>WorksharingUtils</span><span>.</span><span>CreateNewLocal</span><span>(</span><span>centralPath</span><span>,</span><span> localPath</span><span>);</span><span>

    </span><span>// Select specific worksets to open</span><span>
    </span><span>// First get a list of worksets from the unopened document</span><span>
    </span><span>IList</span><span>&lt;</span><span>WorksetPreview</span><span>&gt;</span><span> worksets </span><span>=</span><span> </span><span>WorksharingUtils</span><span>.</span><span>GetUserWorksetInfo</span><span>(</span><span>localPath</span><span>);</span><span>
    </span><span>List</span><span>&lt;</span><span>WorksetId</span><span>&gt;</span><span> worksetsToOpen </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>WorksetId</span><span>&gt;();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>WorksetPreview</span><span> preview </span><span>in</span><span> worksets</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Match worksets to open with criteria</span><span>
        </span><span>if</span><span> </span><span>(</span><span>preview</span><span>.</span><span>Name</span><span>.</span><span>StartsWith</span><span>(</span><span>"O"</span><span>))</span><span>
            worksetsToOpen</span><span>.</span><span>Add</span><span>(</span><span>preview</span><span>.</span><span>Id</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Setup option to open the target worksets</span><span>
    </span><span>// First close all, then set specific ones to open</span><span>
    </span><span>WorksetConfiguration</span><span> worksetConfig </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksetConfiguration</span><span>(</span><span>WorksetConfigurationOption</span><span>.</span><span>CloseAllWorksets</span><span>);</span><span>
    worksetConfig</span><span>.</span><span>Open</span><span>(</span><span>worksetsToOpen</span><span>);</span><span>

    </span><span>// Open the new local</span><span>
    </span><span>OpenOptions</span><span> options1 </span><span>=</span><span> </span><span>new</span><span> </span><span>OpenOptions</span><span>();</span><span>
    options1</span><span>.</span><span>SetOpenWorksetsConfiguration</span><span>(</span><span>worksetConfig</span><span>);</span><span>
    </span><span>Document</span><span> openedDoc </span><span>=</span><span> app</span><span>.</span><span>OpenDocumentFile</span><span>(</span><span>localPath</span><span>,</span><span> options1</span><span>);</span><span>

    </span><span>return</span><span> openedDoc</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following example uses the OpenNewLocalFromModelPath() method demonstrated as part of the previous example.

<table summary="" id="GUID-F99FBBCC-AE58-46F5-85AF-0A7C3C5C0576__TABLE_E6C6F43A63E34845AEBB3BFF72135458"><tbody><tr><td><b>Code Region: Open new local from Revit Server</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Get the server path for a particular model and open a new local copy</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>public</span><span> </span><span>static</span><span> </span><span>Document</span><span> </span><span>OpenNewLocalFromServer</span><span>(</span><span>UIApplication</span><span> uiApp</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create new local from a server location</span><span>
    </span><span>Application</span><span> app </span><span>=</span><span> uiApp</span><span>.</span><span>Application</span><span>;</span><span>

    </span><span>// Get the host id/IP of the server</span><span>
    </span><span>String</span><span> hostId </span><span>=</span><span> app</span><span>.</span><span>GetRevitServerNetworkHosts</span><span>().</span><span>First</span><span>();</span><span>

    </span><span>// try to get the server path for the particular model on the server</span><span>
    </span><span>String</span><span> rootFolder </span><span>=</span><span> </span><span>"|"</span><span>;</span><span>
    </span><span>ModelPath</span><span> serverPath </span><span>=</span><span> </span><span>FindWSAPIModelPathOnServer</span><span>(</span><span>app</span><span>,</span><span> hostId</span><span>,</span><span> rootFolder</span><span>,</span><span> </span><span>"WorksharingOnServer.rvt"</span><span>);</span><span>

    </span><span>ModelPath</span><span> newLocalPath </span><span>=</span><span> </span><span>GetWSAPIModelPath</span><span>(</span><span>"WorksharingLocalFromServer.rvt"</span><span>);</span><span>
    </span><span>return</span><span> </span><span>(</span><span>OpenNewLocalFromModelPath</span><span>(</span><span>uiApp</span><span>.</span><span>Application</span><span>,</span><span> serverPath</span><span>,</span><span> newLocalPath</span><span>));</span><span>
</span><span>}</span><span>

</span><span>/// &lt;summary&gt;</span><span>
</span><span>/// Uses the Revit Server REST API to recursively search the folders of the Revit Server for a particular model.</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>ModelPath</span><span> </span><span>FindWSAPIModelPathOnServer</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>string</span><span> hostId</span><span>,</span><span> </span><span>string</span><span> folderName</span><span>,</span><span> </span><span>string</span><span> fileName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Connect to host to find list of available models (the "/contents" flag)</span><span>
    </span><span>XmlDictionaryReader</span><span> reader </span><span>=</span><span> </span><span>GetResponse</span><span>(</span><span>app</span><span>,</span><span> hostId</span><span>,</span><span> folderName </span><span>+</span><span> </span><span>"/contents"</span><span>);</span><span>
    </span><span>bool</span><span> found </span><span>=</span><span> </span><span>false</span><span>;</span><span>

    </span><span>// Look for the target model name in top level folder</span><span>
    </span><span>List</span><span>&lt;</span><span>String</span><span>&gt;</span><span> folders </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>String</span><span>&gt;();</span><span>
    </span><span>while</span><span> </span><span>(</span><span>reader</span><span>.</span><span>Read</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>// Save a list of subfolders, if found</span><span>
        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Folders"</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>while</span><span> </span><span>(</span><span>reader</span><span>.</span><span>Read</span><span>())</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>EndElement</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Folders"</span><span>)</span><span>
                    </span><span>break</span><span>;</span><span>

                </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Name"</span><span>)</span><span>
                </span><span>{</span><span>
                    reader</span><span>.</span><span>Read</span><span>();</span><span>
                    folders</span><span>.</span><span>Add</span><span>(</span><span>reader</span><span>.</span><span>Value</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>// Check for a matching model at this folder level</span><span>
        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Models"</span><span>)</span><span>
        </span><span>{</span><span>
            found </span><span>=</span><span> </span><span>FindModelInServerResponseJson</span><span>(</span><span>reader</span><span>,</span><span> fileName</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>found</span><span>)</span><span>
                </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    reader</span><span>.</span><span>Close</span><span>();</span><span>

    </span><span>// Build the model path to match the found model on the server</span><span>
    </span><span>if</span><span> </span><span>(</span><span>found</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Server URLs use "|" for folder separation, Revit API uses "/"</span><span>
        </span><span>String</span><span> folderNameFragment </span><span>=</span><span> folderName</span><span>.</span><span>Replace</span><span>(</span><span>'|'</span><span>,</span><span> </span><span>'/'</span><span>);</span><span>

        </span><span>// Add trailing "/" if not present</span><span>
        </span><span>if</span><span> </span><span>(!</span><span>folderNameFragment</span><span>.</span><span>EndsWith</span><span>(</span><span>"/"</span><span>))</span><span>
            folderNameFragment </span><span>+=</span><span> </span><span>"/"</span><span>;</span><span>

        </span><span>// Build server path</span><span>
        </span><span>ModelPath</span><span> modelPath </span><span>=</span><span> </span><span>new</span><span> </span><span>ServerPath</span><span>(</span><span>hostId</span><span>,</span><span> folderNameFragment </span><span>+</span><span> fileName</span><span>);</span><span>
        </span><span>return</span><span> modelPath</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>// Try subfolders</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>String</span><span> folder </span><span>in</span><span> folders</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ModelPath</span><span> modelPath </span><span>=</span><span> </span><span>FindWSAPIModelPathOnServer</span><span>(</span><span>app</span><span>,</span><span> hostId</span><span>,</span><span> folder</span><span>,</span><span> fileName</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>modelPath </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
                </span><span>return</span><span> modelPath</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>null</span><span>;</span><span>
</span><span>}</span><span>

</span><span>// This string is different for each RevitServer version</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>string</span><span> s_revitServerVersion </span><span>=</span><span> </span><span>"/RevitServerAdminRESTService2014/AdminRESTService.svc/"</span><span>;</span><span>

</span><span>/// &lt;summary&gt;</span><span>
</span><span>/// Connect to server to get list of available models and return server response</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>XmlDictionaryReader</span><span> </span><span>GetResponse</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>string</span><span> hostId</span><span>,</span><span> </span><span>string</span><span> info</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create request    </span><span>
    </span><span>WebRequest</span><span> request </span><span>=</span><span> </span><span>WebRequest</span><span>.</span><span>Create</span><span>(</span><span>"http://"</span><span> </span><span>+</span><span> hostId </span><span>+</span><span> s_revitServerVersion </span><span>+</span><span> info</span><span>);</span><span>
    request</span><span>.</span><span>Method</span><span> </span><span>=</span><span> </span><span>"GET"</span><span>;</span><span>

    </span><span>// Add the information the request needs</span><span>

    request</span><span>.</span><span>Headers</span><span>.</span><span>Add</span><span>(</span><span>"User-Name"</span><span>,</span><span> app</span><span>.</span><span>Username</span><span>);</span><span>
    request</span><span>.</span><span>Headers</span><span>.</span><span>Add</span><span>(</span><span>"User-Machine-Name"</span><span>,</span><span> app</span><span>.</span><span>Username</span><span>);</span><span>
    request</span><span>.</span><span>Headers</span><span>.</span><span>Add</span><span>(</span><span>"Operation-GUID"</span><span>,</span><span> </span><span>Guid</span><span>.</span><span>NewGuid</span><span>().</span><span>ToString</span><span>());</span><span>

    </span><span>// Read the response</span><span>
    </span><span>XmlDictionaryReaderQuotas</span><span> quotas </span><span>=</span><span>
        </span><span>new</span><span> </span><span>XmlDictionaryReaderQuotas</span><span>();</span><span>
    </span><span>XmlDictionaryReader</span><span> jsonReader </span><span>=</span><span>
        </span><span>JsonReaderWriterFactory</span><span>.</span><span>CreateJsonReader</span><span>(</span><span>request</span><span>.</span><span>GetResponse</span><span>().</span><span>GetResponseStream</span><span>(),</span><span> quotas</span><span>);</span><span>

    </span><span>return</span><span> jsonReader</span><span>;</span><span>
</span><span>}</span><span>

</span><span>/// &lt;summary&gt;</span><span>
</span><span>/// Read through server response to find particular model</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>private</span><span> </span><span>static</span><span> </span><span>bool</span><span> </span><span>FindModelInServerResponseJson</span><span>(</span><span>XmlDictionaryReader</span><span> reader</span><span>,</span><span> </span><span>string</span><span> fileName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Read through entries in this section</span><span>
    </span><span>while</span><span> </span><span>(</span><span>reader</span><span>.</span><span>Read</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>EndElement</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Models"</span><span>)</span><span>
            </span><span>break</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>reader</span><span>.</span><span>NodeType</span><span> </span><span>==</span><span> </span><span>XmlNodeType</span><span>.</span><span>Element</span><span> </span><span>&amp;&amp;</span><span> reader</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Name"</span><span>)</span><span>
        </span><span>{</span><span>
            reader</span><span>.</span><span>Read</span><span>();</span><span>
            </span><span>String</span><span> modelName </span><span>=</span><span> reader</span><span>.</span><span>Value</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>modelName</span><span>.</span><span>Equals</span><span>(</span><span>fileName</span><span>))</span><span>
            </span><span>{</span><span>
                </span><span>// Match found, stop looping and return</span><span>
                </span><span>return</span><span> </span><span>true</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>false</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Open detached from central

If an add-in will be working on a workshared file but does not need to make permanet changes, it can open the model detached from the central file.

**Code Region: Open detached**

```
private static Document OpenDetached(Application application, ModelPath modelPath)
{
    OpenOptions options1 = new OpenOptions();

    options1.DetachFromCentralOption = DetachFromCentralOption.DetachAndDiscardWorksets;
    Document openedDoc = application.OpenDocumentFile(modelPath, options1);

    return openedDoc;
}
```

If an application only needs read-only access to a server file, the example below demonstrates how to copy the server model locally and open it detached. Note this code sample re-uses methods demonstrated in previous examples.

<table summary="" id="GUID-F99FBBCC-AE58-46F5-85AF-0A7C3C5C0576__TABLE_3A8EC07A41C44592B6E75E852965C3A4"><tbody><tr><td><b>Code Region: Copy and open detached</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>Document</span><span> </span><span>CopyAndOpenDetached</span><span>(</span><span>UIApplication</span><span> uiApp</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Copy a server model locally and open detached</span><span>
    </span><span>Application</span><span> application </span><span>=</span><span> uiApp</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>String</span><span> hostId </span><span>=</span><span> application</span><span>.</span><span>GetRevitServerNetworkHosts</span><span>().</span><span>First</span><span>();</span><span>

    </span><span>// Try to get the server path for the particular model on the server</span><span>
    </span><span>String</span><span> rootFolder </span><span>=</span><span> </span><span>"|"</span><span>;</span><span>
    </span><span>ModelPath</span><span> serverPath </span><span>=</span><span> </span><span>FindWSAPIModelPathOnServer</span><span>(</span><span>application</span><span>,</span><span> hostId</span><span>,</span><span> rootFolder</span><span>,</span><span> </span><span>"ServerModel.rvt"</span><span>);</span><span>

    </span><span>// For debugging</span><span>
    </span><span>String</span><span> sourcePath </span><span>=</span><span> </span><span>ModelPathUtils</span><span>.</span><span>ConvertModelPathToUserVisiblePath</span><span>(</span><span>serverPath</span><span>);</span><span>

    </span><span>// Setup the target location for the copy</span><span>
    </span><span>ModelPath</span><span> localPath </span><span>=</span><span> </span><span>GetWSAPIModelPath</span><span>(</span><span>"CopiedModel.rvt"</span><span>);</span><span>

    </span><span>// Copy, allowing overwrite</span><span>
    application</span><span>.</span><span>CopyModel</span><span>(</span><span>serverPath</span><span>,</span><span> </span><span>ModelPathUtils</span><span>.</span><span>ConvertModelPathToUserVisiblePath</span><span>(</span><span>localPath</span><span>),</span><span> </span><span>true</span><span>);</span><span>

    </span><span>// Open the copy as detached</span><span>
    </span><span>Document</span><span> openedDoc </span><span>=</span><span> </span><span>OpenDetached</span><span>(</span><span>application</span><span>,</span><span> localPath</span><span>);</span><span>

    </span><span>return</span><span> openedDoc</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Opening a Workshared Document  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Visibility and Display  Autodesk.md ===== -->

---
created: 2026-01-28T21:20:21 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Visibility_and_Display_html
author: 
---

# Help | Visibility and Display | Autodesk

> ## Excerpt
> A workset’s visibility can be set for a particular view using View.SetWorksetVisibility(). The WorksetVisibility options are Visible (it will be visible if the workset is open), Hidden, and UseGlobalSetting (indicating not to override the setting for the view). The corresponding View.GetWorksetVisibility() method retrieves the current visibility settings for a workset in that view. However, this method does not consider whether the workset is currently open. To determine if a workset is visible in a View, including taking into account whether the workset is open or closed, use View.IsWorksetVisible().

---
## Visibility

A workset’s visibility can be set for a particular view using View.SetWorksetVisibility(). The WorksetVisibility options are Visible (it will be visible if the workset is open), Hidden, and UseGlobalSetting (indicating not to override the setting for the view). The corresponding View.GetWorksetVisibility() method retrieves the current visibility settings for a workset in that view. However, this method does not consider whether the workset is currently open. To determine if a workset is visible in a View, including taking into account whether the workset is open or closed, use View.IsWorksetVisible().

The class WorksetDefaultVisibilitySettings manages default visibility of worksets in a document. It is not available for family documents. If worksharing is disabled in a document, all elements are moved into a single workset; that workset, and any worksets (re)created if worksharing is re-enabled, is visible by default regardless of any current settings.

The following example hides a workset in a given view and hides it by default in other views.

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_AE77CC75BFB1470DB482D427DF80149F"><tbody><tr><td><b>Code Region: Hide a Workset</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>HideWorkset</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>View</span><span> view</span><span>,</span><span> </span><span>WorksetId</span><span> worksetId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// get the current visibility</span><span>
    </span><span>WorksetVisibility</span><span> visibility </span><span>=</span><span> view</span><span>.</span><span>GetWorksetVisibility</span><span>(</span><span>worksetId</span><span>);</span><span>

    </span><span>// and set it to 'Hidden' if it is not hidden yet</span><span>
    </span><span>if</span><span> </span><span>(</span><span>visibility </span><span>!=</span><span> </span><span>WorksetVisibility</span><span>.</span><span>Hidden</span><span>)</span><span>
    </span><span>{</span><span>
        view</span><span>.</span><span>SetWorksetVisibility</span><span>(</span><span>worksetId</span><span>,</span><span> </span><span>WorksetVisibility</span><span>.</span><span>Hidden</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Get the workset’s default visibility      </span><span>
    </span><span>WorksetDefaultVisibilitySettings</span><span> defaultVisibility </span><span>=</span><span> </span><span>WorksetDefaultVisibilitySettings</span><span>.</span><span>GetWorksetDefaultVisibilitySettings</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// and making sure it is set to 'false'</span><span>
    </span><span>if</span><span> </span><span>(</span><span>true</span><span> </span><span>==</span><span> defaultVisibility</span><span>.</span><span>IsWorksetVisible</span><span>(</span><span>worksetId</span><span>))</span><span>
    </span><span>{</span><span>
        defaultVisibility</span><span>.</span><span>SetWorksetVisibility</span><span>(</span><span>worksetId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Display Modes

In addition to getting and setting information about the workset visibility, the View class also provides methods to access information on the worksharing display mode and settings. The WorksharingDisplayMode enumeration indicates which mode a view is in, if any:

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_626E2FBB86D24496A52442096DE4266D"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td><b>Off</b></td><td>No active worksharing display mode.</td></tr><tr><td><b>CheckoutStatus</b></td><td>The view is displaying the checkout status of elements.</td></tr><tr><td><b>Owners</b></td><td>The view is displaying the specific owners of elements.</td></tr><tr><td><b>ModelUpdates</b></td><td>The view is displaying model updates.</td></tr><tr><td><b>Worksets</b></td><td>The view is displaying which workset each element is assigned to.</td></tr></tbody></table>

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_C842939754CF4799BCFD7C76042B5F46"><tbody><tr><td><b>Code Region: Activate different worksharing display modes</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>View</span><span> activeView </span><span>=</span><span> commandData</span><span>.</span><span>View</span><span>;</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> activeView</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>// Prepare settings</span><span>
    </span><span>Color</span><span> red </span><span>=</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>0xFF</span><span>,</span><span> </span><span>0x00</span><span>,</span><span> </span><span>0x00</span><span>);</span><span>
    </span><span>WorksharingDisplayGraphicSettings</span><span> settingsToApply </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span>(</span><span>true</span><span>,</span><span> red</span><span>);</span><span>

    </span><span>// Toggle mode based on the current mode</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Toggle display mode"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>WorksharingDisplaySettings</span><span> settings </span><span>=</span><span> </span><span>WorksharingDisplaySettings</span><span>.</span><span>GetOrCreateWorksharingDisplaySettings</span><span>(</span><span>doc</span><span>);</span><span>

        </span><span>switch</span><span> </span><span>(</span><span>activeView</span><span>.</span><span>GetWorksharingDisplayMode</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>case</span><span> </span><span>WorksharingDisplayMode</span><span>.</span><span>Off</span><span>:</span><span>
                activeView</span><span>.</span><span>SetWorksharingDisplayMode</span><span>(</span><span>WorksharingDisplayMode</span><span>.</span><span>CheckoutStatus</span><span>);</span><span>
                settings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>CheckoutStatus</span><span>.</span><span>OwnedByOtherUser</span><span>,</span><span> settingsToApply</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>WorksharingDisplayMode</span><span>.</span><span>CheckoutStatus</span><span>:</span><span>
                activeView</span><span>.</span><span>SetWorksharingDisplayMode</span><span>(</span><span>WorksharingDisplayMode</span><span>.</span><span>ModelUpdates</span><span>);</span><span>
                settings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>ModelUpdatesStatus</span><span>.</span><span>UpdatedInCentral</span><span>,</span><span> settingsToApply</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>WorksharingDisplayMode</span><span>.</span><span>ModelUpdates</span><span>:</span><span>
                activeView</span><span>.</span><span>SetWorksharingDisplayMode</span><span>(</span><span>WorksharingDisplayMode</span><span>.</span><span>Owners</span><span>);</span><span>
                settings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>"Target user"</span><span>,</span><span> settingsToApply</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>WorksharingDisplayMode</span><span>.</span><span>Owners</span><span>:</span><span>
                activeView</span><span>.</span><span>SetWorksharingDisplayMode</span><span>(</span><span>WorksharingDisplayMode</span><span>.</span><span>Worksets</span><span>);</span><span>
                settings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>doc</span><span>.</span><span>GetWorksetTable</span><span>().</span><span>GetActiveWorksetId</span><span>(),</span><span> settingsToApply</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>WorksharingDisplayMode</span><span>.</span><span>Worksets</span><span>:</span><span>
                activeView</span><span>.</span><span>SetWorksharingDisplayMode</span><span>(</span><span>WorksharingDisplayMode</span><span>.</span><span>Off</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Graphics Settings

The WorksharingDisplaySettings class controls how elements will appear when they are displayed in any of the worksharing display modes. The colors stored in these settings are a common setting and are shared by all users in the model. Whether a given color is applied is specific to the current user and will not be shared by other users. Note that these settings are available even in models that are not workshared. This is to allow pre-configuring the display settings before enabling worksets so that they can be stored in template files.

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_78E2B7D8D21C45C0ABE8E889FC02021A"><tbody><tr><td><b>Code Region: Worksharing Display Graphic Settings</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span> </span><span>GetWorksharingDisplaySettings</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>String</span><span> userName</span><span>,</span><span> </span><span>WorksetId</span><span> worksetId</span><span>,</span><span> </span><span>bool</span><span> ownedbyCurrentUser</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>WorksharingDisplayGraphicSettings</span><span> graphicSettings</span><span>;</span><span>

    </span><span>// get or create a WorksharingDisplaySettings current active document</span><span>
    </span><span>WorksharingDisplaySettings</span><span> displaySettings </span><span>=</span><span> </span><span>WorksharingDisplaySettings</span><span>.</span><span>GetOrCreateWorksharingDisplaySettings</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// get graphic settings for a user, if specified</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>String</span><span>.</span><span>IsNullOrEmpty</span><span>(</span><span>userName</span><span>))</span><span>
        graphicSettings </span><span>=</span><span> displaySettings</span><span>.</span><span>GetGraphicOverrides</span><span>(</span><span>userName</span><span>);</span><span>

     </span><span>// get graphicSettings for a workset, if specified</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>worksetId </span><span>!=</span><span> </span><span>WorksetId</span><span>.</span><span>InvalidWorksetId</span><span>)</span><span>
        graphicSettings </span><span>=</span><span> displaySettings</span><span>.</span><span>GetGraphicOverrides</span><span>(</span><span>worksetId</span><span>);</span><span>

    </span><span>// get graphic settings for the OwnedByCurrentUser status</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>ownedbyCurrentUser</span><span>)</span><span>
        graphicSettings </span><span>=</span><span> displaySettings</span><span>.</span><span>GetGraphicOverrides</span><span>(</span><span>CheckoutStatus</span><span>.</span><span>OwnedByCurrentUser</span><span>);</span><span>

    </span><span>// otherwise get graphic settings for the CurrentWithCentral status</span><span>
     </span><span>else</span><span>
          graphicSettings </span><span>=</span><span> displaySettings</span><span>.</span><span>GetGraphicOverrides</span><span>(</span><span>ModelUpdatesStatus</span><span>.</span><span>CurrentWithCentral</span><span>);</span><span>

     </span><span>return</span><span> graphicSettings</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The overloaded method WorksharingDisplaySettings.SetGraphicOverrides() sets the graphic overrides assigned to elements based on the given criteria.

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_91FCA3F081244BB7A8B8530AE5D14092"><tbody><tr><td><b>Code Region: Graphic Overrides</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SetWorksharingDisplaySettings</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>WorksetId</span><span> worksetId</span><span>,</span><span> </span><span>String</span><span> userName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>String</span><span> message </span><span>=</span><span> </span><span>String</span><span>.</span><span>Empty</span><span>;</span><span>

    </span><span>// get or create a WorksharingDisplaySettings current active document</span><span>
    </span><span>WorksharingDisplaySettings</span><span> displaySettings </span><span>=</span><span> </span><span>WorksharingDisplaySettings</span><span>.</span><span>GetOrCreateWorksharingDisplaySettings</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// set a new graphicSettings for CheckoutStatus - NotOwned</span><span>
    </span><span>WorksharingDisplayGraphicSettings</span><span> graphicSettings </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span>(</span><span>true</span><span>,</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>255</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    displaySettings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>CheckoutStatus</span><span>.</span><span>NotOwned</span><span>,</span><span> graphicSettings</span><span>);</span><span>

    </span><span>// set a new graphicSettings for ModelUpdatesStatus - CurrentWithCentral</span><span>
    graphicSettings </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span>(</span><span>true</span><span>,</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>128</span><span>,</span><span> </span><span>128</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    displaySettings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>ModelUpdatesStatus</span><span>.</span><span>CurrentWithCentral</span><span>,</span><span> graphicSettings</span><span>);</span><span>

    </span><span>// set a new graphicSettings by a given userName</span><span>
    graphicSettings </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span>(</span><span>true</span><span>,</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>0</span><span>,</span><span> </span><span>255</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    displaySettings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>userName</span><span>,</span><span> graphicSettings</span><span>);</span><span>

    </span><span>// set a new graphicSettings by a given workset Id</span><span>
    graphicSettings </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span>(</span><span>true</span><span>,</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>255</span><span>));</span><span>
    displaySettings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>worksetId</span><span>,</span><span> graphicSettings</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The WorksharingDisplaySettings class can also be used to control which users are listed in the displayed users for the document. The RemoveUsers() method removes users from the list of displayed users and permanently discards any customization of the graphics. Only users who do not own any elements in the document can be removed. The RestoreUsers() method adds removed users back to the list of displayed users and permits customization of the graphics for those users. Note that any restored users will be shown with default graphic overrides and any customizations that existed prior to removing the user will not be restored.

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_2C78F82752EC4B40BC74159A3679941A"><tbody><tr><td><b>Code Region: Removing Users</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>RemoveAndRestoreUsers</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// get or create a WorksharingDisplaySettings current active document</span><span>
    </span><span>WorksharingDisplaySettings</span><span> displaySettings </span><span>=</span><span> </span><span>WorksharingDisplaySettings</span><span>.</span><span>GetOrCreateWorksharingDisplaySettings</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// get all users with GraphicOverrides</span><span>
    </span><span>ICollection</span><span>&lt;string&gt;</span><span> users </span><span>=</span><span> displaySettings</span><span>.</span><span>GetAllUsersWithGraphicOverrides</span><span>();</span><span>

    </span><span>// remove the users from the display settings (they will not have graphic overrides anymore)</span><span>
    </span><span>ICollection</span><span>&lt;string&gt;</span><span> outUserList</span><span>;</span><span>
    displaySettings</span><span>.</span><span>RemoveUsers</span><span>(</span><span>doc</span><span>,</span><span> users</span><span>,</span><span> </span><span>out</span><span> outUserList</span><span>);</span><span>

    </span><span>// show the current list of removed users</span><span>
    </span><span>ICollection</span><span>&lt;string&gt;</span><span> removedUsers </span><span>=</span><span> displaySettings</span><span>.</span><span>GetRemovedUsers</span><span>();</span><span>

    </span><span>String</span><span> message </span><span>=</span><span> </span><span>"Current list of removed users: "</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>removedUsers</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span> </span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>String</span><span> user </span><span>in</span><span> removedUsers</span><span>)</span><span>
        </span><span>{</span><span>
           message </span><span>+=</span><span> </span><span>"\n"</span><span> </span><span>+</span><span> user</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        message </span><span>=</span><span> </span><span>"[Empty]"</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Users Removed"</span><span>,</span><span> message</span><span>);</span><span>

    </span><span>// restore the previously removed users</span><span>
    </span><span>int</span><span> number </span><span>=</span><span> displaySettings</span><span>.</span><span>RestoreUsers</span><span>(</span><span>outUserList</span><span>);</span><span>

    </span><span>// again, show the current list of removed users</span><span>
    </span><span>// it should not contain the users that were restored</span><span>
    removedUsers </span><span>=</span><span> displaySettings</span><span>.</span><span>GetRemovedUsers</span><span>();</span><span>

    message </span><span>=</span><span> </span><span>"Current list of removed users: "</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>removedUsers</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span> </span><span>)</span><span>
    </span><span>{</span><span>
       </span><span>foreach</span><span> </span><span>(</span><span>String</span><span> user </span><span>in</span><span> removedUsers</span><span>)</span><span>
        </span><span>{</span><span>
           message </span><span>+=</span><span> </span><span>"\n"</span><span> </span><span>+</span><span> user</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        message </span><span>=</span><span> </span><span>"[Empty]"</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Removed Users Restored"</span><span>,</span><span> message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Visibility and Display  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Workshared File Management  Autodesk.md ===== -->

---
created: 2026-01-28T21:20:25 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Workshared_File_Management_html
author: 
---

# Help | Workshared File Management | Autodesk

> ## Excerpt
> There are several Document methods for use with a workshared project file.

---
There are several Document methods for use with a workshared project file.

### Enable Worksharing

If a document is not already workshared, which can be determined from the Document.IsWorkshared property, worksharing can be enabled via the Revit API using the Document.EnableWorksharing() method. The document's Undo history will be cleared by this command, therefore this command and others executed before it cannot be undone. Additionally, all transaction phases (e.g. transactions, transaction groups and sub-transactions) that were explicitly started must be finished prior to calling EnableWorksharing().

#### Worksharing in the Cloud

-   Document.EnableCloudWorksharing() converts a cloud model into a workshared cloud model.
-   Document.CanEnableCloudWorksharing() can be used to check whether this operation is valid on a given model.

### Reload Latest

The method Document.ReloadLatest() retrieves changes from the central model (due to one or more synchronizations with central) and merges them into the current session.

The following examples uses ReloadLatest() to update the current session after confirming with the user that it is OK to do so.

<table summary="" id="GUID-95A89253-7B8C-43A6-BE90-0C7B90FA237F__TABLE_AF79DB8A57A949DFB2D9C364E4503AD1"><tbody><tr><td><b>Code Region: Reload from Central</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>ReloadLatestWithMessage</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Tell user what we're doing</span><span>
    </span><span>TaskDialog</span><span> td </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Alert"</span><span>);</span><span>
    td</span><span>.</span><span>MainInstruction</span><span> </span><span>=</span><span> </span><span>"Application 'Automatic element creator' needs to reload changes from central in order to proceed."</span><span>;</span><span>
    td</span><span>.</span><span>MainContent</span><span> </span><span>=</span><span> </span><span>"This will update your local with all changes currently in the central model.  This operation "</span><span> </span><span>+</span><span>
                        </span><span>"may take some time depending on the number of changes available on the central."</span><span>;</span><span>
    td</span><span>.</span><span>CommonButtons</span><span> </span><span>=</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Ok</span><span> </span><span>|</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Cancel</span><span>;</span><span>

    </span><span>TaskDialogResult</span><span> result </span><span>=</span><span> td</span><span>.</span><span>Show</span><span>();</span><span>

    </span><span>if</span><span> </span><span>(</span><span>result </span><span>==</span><span> </span><span>TaskDialogResult</span><span>.</span><span>Ok</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// There are no currently customizable user options for ReloadLatest.</span><span>
        doc</span><span>.</span><span>ReloadLatest</span><span>(</span><span>new</span><span> </span><span>ReloadLatestOptions</span><span>());</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Proceeding..."</span><span>,</span><span> </span><span>"Reload operation completed, proceeding with updates."</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Canceled."</span><span>,</span><span> </span><span>"Reload operation canceled, so changes will not be made.  Return to this command later when ready to reload."</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Synchronizing with Central Model

The method Document.SynchronizeWithCentral() reloads any changes from the central model so that the current session is up to date and then saves local changes back to central. A save to central is performed even if no changes were made.

When using SynchronizeWithCentral(), options can be specified for accessing the central model as well as synchronizing with it. The main option for accessing the central is to determine how the call should behave if the central model is locked. Since the synchronization requires a temporary lock on the central model, it cannot be performed if the model is already locked. The default behavior is to wait and repeatedly try to lock the central model in order to proceed with the synchronization. This behavior can be overridden using the TransactWithCentralOptions parameter of the SynchronizeWithCentral() method.

The SynchronizeWithCentralOptions parameter of the method is used to set options for the actual synchronization, such as whether elements or worksets owned by the current user should be relinquished during synchronization.

In the following example, an attempt is made to synchronize with a central model. If the central model is locked, it will immediately give up.

<table summary="" id="GUID-95A89253-7B8C-43A6-BE90-0C7B90FA237F__TABLE_79B7EEDC12AB4851ACA186D695869D4F"><tbody><tr><td><b>Code Region: Synchronize with Central</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SyncWithoutRelinquishing</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Set options for accessing central model</span><span>
    </span><span>TransactWithCentralOptions</span><span> transOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>TransactWithCentralOptions</span><span>();</span><span>
    </span><span>SynchLockCallback</span><span> transCallBack </span><span>=</span><span> </span><span>new</span><span> </span><span>SynchLockCallback</span><span>();</span><span>
    </span><span>// Override default behavior of waiting to try again if the central model is locked</span><span>
    transOpts</span><span>.</span><span>SetLockCallback</span><span>(</span><span>transCallBack</span><span>);</span><span>

    </span><span>// Set options for synchronizing with central</span><span>
    </span><span>SynchronizeWithCentralOptions</span><span> syncOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>SynchronizeWithCentralOptions</span><span>();</span><span>
    </span><span>// Sync without relinquishing any checked out elements or worksets</span><span>
    </span><span>RelinquishOptions</span><span> relinquishOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>RelinquishOptions</span><span>(</span><span>false</span><span>);</span><span>
    syncOpts</span><span>.</span><span>SetRelinquishOptions</span><span>(</span><span>relinquishOpts</span><span>);</span><span>
    </span><span>// Do not automatically save local model after sync</span><span>
    syncOpts</span><span>.</span><span>SaveLocalAfter</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    syncOpts</span><span>.</span><span>Comment</span><span> </span><span>=</span><span> </span><span>"Changes to Workset1"</span><span>;</span><span>

    </span><span>try</span><span>
    </span><span>{</span><span>
        doc</span><span>.</span><span>SynchronizeWithCentral</span><span>(</span><span>transOpts</span><span>,</span><span> syncOpts</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Synchronize Failed"</span><span>,</span><span> e</span><span>.</span><span>Message</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>class</span><span> </span><span>SynchLockCallback</span><span> </span><span>:</span><span> </span><span>ICentralLockedCallback</span><span>
</span><span>{</span><span>
    </span><span>// If unable to lock central, give up rather than waiting</span><span>
    </span><span>public</span><span> </span><span>bool</span><span> </span><span>ShouldWaitForLockAvailability</span><span>()</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> </span><span>false</span><span>;</span><span>
    </span><span>}</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>

In the next example, the user is given a message prior to synching, and is given options on whether to relinquish all elements when synchronizing, or keep worksets checked out.

<table summary="" id="GUID-95A89253-7B8C-43A6-BE90-0C7B90FA237F__TABLE_BD4FEF23BDD9450B8518FEEE643E8305"><tbody><tr><td><b>Code Region: Synchronize with Central With Message</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>SynchWithCentralWithMessage</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Checkout workset (for use with "keep checked out worksets" option later)</span><span>
    </span><span>FilteredWorksetCollector</span><span> fwc </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredWorksetCollector</span><span>(</span><span>doc</span><span>);</span><span>
    fwc</span><span>.</span><span>OfKind</span><span>(</span><span>WorksetKind</span><span>.</span><span>UserWorkset</span><span>);</span><span>
    </span><span>Workset</span><span> workset1 </span><span>=</span><span> fwc</span><span>.</span><span>First</span><span>&lt;</span><span>Workset</span><span>&gt;(</span><span>ws </span><span>=&gt;</span><span> ws</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Workset1"</span><span>);</span><span>

    </span><span>WorksharingUtils</span><span>.</span><span>CheckoutWorksets</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>WorksetId</span><span>[]</span><span> </span><span>{</span><span> workset1</span><span>.</span><span>Id</span><span> </span><span>});</span><span>

    </span><span>// Make a change</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Add Level"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>Level</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>100</span><span>);</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>// Tell user what we're doing</span><span>
    </span><span>TaskDialog</span><span> td </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Alert"</span><span>);</span><span>
    td</span><span>.</span><span>MainInstruction</span><span> </span><span>=</span><span> </span><span>"Application 'Automatic element creator' has made changes and is prepared to synchronize with central."</span><span>;</span><span>
    td</span><span>.</span><span>MainContent</span><span> </span><span>=</span><span> </span><span>"This will update central with all changes currently made in the project by the application or by the user.  This operation "</span><span> </span><span>+</span><span>
                        </span><span>"may take some time depending on the number of changes made by the app and by the user."</span><span>;</span><span>

    td</span><span>.</span><span>AddCommandLink</span><span>(</span><span>TaskDialogCommandLinkId</span><span>.</span><span>CommandLink1</span><span>,</span><span> </span><span>"Do not synchronize at this time."</span><span>);</span><span>
    td</span><span>.</span><span>AddCommandLink</span><span>(</span><span>TaskDialogCommandLinkId</span><span>.</span><span>CommandLink2</span><span>,</span><span> </span><span>"Synchronize and relinquish all elements."</span><span>);</span><span>
    td</span><span>.</span><span>AddCommandLink</span><span>(</span><span>TaskDialogCommandLinkId</span><span>.</span><span>CommandLink3</span><span>,</span><span> </span><span>"Synchronize but keep checked out worksets."</span><span>);</span><span>
    td</span><span>.</span><span>DefaultButton</span><span> </span><span>=</span><span> </span><span>TaskDialogResult</span><span>.</span><span>CommandLink1</span><span>;</span><span>

    </span><span>TaskDialogResult</span><span> result </span><span>=</span><span> td</span><span>.</span><span>Show</span><span>();</span><span>

    </span><span>switch</span><span> </span><span>(</span><span>result</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>case</span><span> </span><span>TaskDialogResult</span><span>.</span><span>CommandLink1</span><span>:</span><span>
        </span><span>default</span><span>:</span><span>
            </span><span>{</span><span>
                </span><span>// Do not synch.  Nothing to do.</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>case</span><span> </span><span>TaskDialogResult</span><span>.</span><span>CommandLink2</span><span>:</span><span>
        </span><span>case</span><span> </span><span>TaskDialogResult</span><span>.</span><span>CommandLink3</span><span>:</span><span>
            </span><span>{</span><span>
                </span><span>// Prepare to synch</span><span>
                </span><span>// TransactWithCentralOptions has to do with the behavior related to locked or busy central models.</span><span>
                </span><span>// We'll use the default behavior.</span><span>
                </span><span>TransactWithCentralOptions</span><span> twcOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>TransactWithCentralOptions</span><span>();</span><span>

                </span><span>// Setup synch-with-central options (add a comment about our change)</span><span>
                </span><span>SynchronizeWithCentralOptions</span><span> swcOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>SynchronizeWithCentralOptions</span><span>();</span><span>
                swcOpts</span><span>.</span><span>Comment</span><span> </span><span>=</span><span> </span><span>"Synchronized by 'Automatic element creator' with user acceptance."</span><span>;</span><span>

                </span><span>if</span><span> </span><span>(</span><span>result </span><span>==</span><span> </span><span>TaskDialogResult</span><span>.</span><span>CommandLink3</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>// Setup relinquish options to keep user worksets checked out</span><span>
                    </span><span>RelinquishOptions</span><span> rOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>RelinquishOptions</span><span>(</span><span>true</span><span>);</span><span>
                    rOptions</span><span>.</span><span>UserWorksets</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
                    swcOpts</span><span>.</span><span>SetRelinquishOptions</span><span>(</span><span>rOptions</span><span>);</span><span>
                </span><span>}</span><span>

                doc</span><span>.</span><span>SynchronizeWithCentral</span><span>(</span><span>twcOpts</span><span>,</span><span> swcOpts</span><span>);</span><span>

                </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Create New Local Model

The WorksharingUtils.CreateNewLocal() method copies a central model to a new local file. This method does not open the new file. For an example of creating a new local model and opening it, see [Opening a Workshared Document](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Opening_a_Workshared_Document_html)


<!-- ===== END: Help  Workshared File Management  Autodesk.md ===== -->

---

