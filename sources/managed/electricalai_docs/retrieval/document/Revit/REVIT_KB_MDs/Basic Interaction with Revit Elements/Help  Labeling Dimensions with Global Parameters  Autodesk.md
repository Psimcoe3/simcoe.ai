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
