---
created: 2026-01-28T20:49:58 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_GlobalParameter_Basics_html
author: 
---

# Help | GlobalParameter Basics | Autodesk

> ## Excerpt
> The GlobalParameter class represents a global parameter in a project document and can be used to create and modify global parameters.

---
The GlobalParameter class represents a global parameter in a project document and can be used to create and modify global parameters.

## Creating global parameters

Global parameters may be created only in project documents, not in families. Global parameters are created via the static Create() method in a given document, with a given name and SpecTypeId. Each new parameter must have a name that is unique within the document, which can be determined using the static GlobalParametersManager.IsUniqueName() method. Global parameters can be created with almost any type of data, but there are a few types that are not currently supported, such as the ElementId type. Test whether a particular data type is appropriate for a global parameter by using the static SpecUtils.IsSpec() method.

Parameters are created as non-reporting initially, but can be changed after creation using the IsReporting property if the global parameter is of an eligible type. See the [Reporting vs. Non-Reporting Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Reporting_vs_Non_Reporting_parameters_html "The most significant difference in types of global parameters is whether they are reporting or non-reporting.") page for more information.

<table summary="" id="GUID-24FE1FF0-A13C-4053-802A-72E4C77FD752__TABLE_E2A463303AAA4F09B5BAB775B1171CEF"><tbody><tr><td><b>Code Region: Create a new global parameter</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Creates a new Global Parameter of type Length, assigns it an initial value,</span><span>
</span><span>/// and uses it to label a set of input dimension elements.</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>/// &lt;param name="document"&gt;Revit project document in which to create the parameter.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="name"&gt;Name of the global parameter to create.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="value"&gt;A value the new global parameter is to have.&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="dimensionsToLabel"&gt;A set of dimension to labe by the new global parameter.&lt;/param&gt;</span><span>
</span><span>/// &lt;returns&gt;ElementId of the new GlobalParameter&lt;/returns&gt;</span><span>
</span><span>public</span><span> </span><span>ElementId</span><span> </span><span>CreateNewGlobalParameter</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>String</span><span> name</span><span>,</span><span> </span><span>double</span><span> value</span><span>,</span><span> </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> dimensionsToLabel</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>GlobalParametersManager</span><span>.</span><span>AreGlobalParametersAllowed</span><span>(</span><span>document</span><span>))</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>InvalidOperationException</span><span>(</span><span>"Global parameters are not permitted in the given document"</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(!</span><span>GlobalParametersManager</span><span>.</span><span>IsUniqueName</span><span>(</span><span>document</span><span>,</span><span> name</span><span>))</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>ArgumentException</span><span>(</span><span>"Global parameter with such name already exists in the document"</span><span>,</span><span> </span><span>"name"</span><span>);</span><span>

    </span><span>ElementId</span><span> gpid </span><span>=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>;</span><span>

    </span><span>// creation of any element must be in a transaction</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Create Global Parameter"</span><span>))</span><span>
    </span><span>{</span><span>
        trans</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// create a GP with the given name and type Length</span><span>
        </span><span>GlobalParameter</span><span> gp </span><span>=</span><span> </span><span>GlobalParameter</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> name</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>Length</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>gp </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// if created successfully, assign it a value</span><span>
            </span><span>// note: parameters of type Length accept Double values</span><span>
            gp</span><span>.</span><span>SetValue</span><span>(</span><span>new</span><span> </span><span>DoubleParameterValue</span><span>(</span><span>value</span><span>));</span><span>

            </span><span>// if a collection of dimensions was given, label them with this new parameter</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> elemid </span><span>in</span><span> dimensionsToLabel</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// not just any dimension is allowed to be labeled</span><span>
                </span><span>// check first to avoid exceptions</span><span>
                </span><span>if</span><span> </span><span>(</span><span>gp</span><span>.</span><span>CanLabelDimension</span><span>(</span><span>elemid</span><span>))</span><span>
                </span><span>{</span><span>
                    gp</span><span>.</span><span>LabelDimension</span><span>(</span><span>elemid</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>

            gpid </span><span>=</span><span> gp</span><span>.</span><span>Id</span><span>;</span><span>
        </span><span>}</span><span>
        trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> gpid</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Getting and setting the value of a global parameter

All global parameters, formula-driven, dimension-driven, or independent, have values. A value can be obtained by calling the GetValue() method. The object returned by that method is an instance of one of the classes derived from the ParameterValue class:

-   IntegerParameterValue
-   DoubleParameterValue
-   StringParameterValue

All the derived classes have only one property, Value, which gets or sets the value as the corresponding type.

The concrete instance is determined by the type of the global parameter which was specified upon creation. Parameters that are neither formula-driven nor dimension-driven (reporting) can have a value assigned. The method to use is SetValue() and it accepts the same type of ParameterValue that is returned by GetValue(). However, the type can also be deduced easily: **Text** parameters accept only StringParameterValue. **Integer** and **YesNo** parameters accept only IntegerParameterValue. All other parameters accept only DoubleParameterValue.

## Elements affected by a global parameter

Global parameters can be associated with other global parameters as well as regular family instance parameters (which may report global parameters as their values via the assignment formula.) There are two methods available to find relations among parameters: GlobalParameter.GetAffectedGlobalParameters() and GlobalParameter.GetAffectedElements(). The former returns all other global parameters that refer to a particular global parameter in their respective formulas. The latter method returns a set of all elements of which some parameters are controlled by the global parameter. These two methods together with the GlobalParameter.GetLabeledDimensions() can help determine out how model elements relate to each other via global parameters.

Methods for maintaining associations between element properties and global parameters can be found in the [Parameter](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Parameter_html "The Parameter class contains the value for the given parameter.") class.
