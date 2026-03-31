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
