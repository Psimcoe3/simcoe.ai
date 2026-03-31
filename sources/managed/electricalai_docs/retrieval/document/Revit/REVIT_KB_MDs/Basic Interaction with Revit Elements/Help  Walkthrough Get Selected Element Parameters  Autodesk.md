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
