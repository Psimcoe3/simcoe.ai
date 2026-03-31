---
created: 2026-01-28T20:49:43 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_SharedParameterElement_html
author: 
---

# Help | SharedParameterElement | Autodesk

> ## Excerpt
> SharedParameterElements store information about a particular user-defined shared parameter in the document

---
SharedParameterElements store information about a particular user-defined shared parameter in the document

User-defined parameters are stored in the document and represented by the ParameterElement class. The subclass SharedParameterElement represents a shared parameter loaded into the document. ParemeterElement is also the base class for GlobalParameter.

Once a shared parameter has been loaded into a document, information about it can be retrieved from the SharedParameterElement class. SharedParameterElement inherits the GetDefinition() method from the parent ParameterElement class. GetDefinition() returns the InternalDefinition that represents the definition for the parameter in the document, as opposed to the ExternalDefinition for a shared parameter that is stored in the shared parameter file. SharedParameterElement also provides access to the Guid that identifies the shared parameter via the GuidValue property.

The static Create() method on this class can create a new SharedParameterElement in the document from an ExternalDefinition.

The static Lookup() method can retrieve a SharedParameterElement from a given Guid.

In the following example, a schedule contains a field representing the value of a shared parameter. The definition for the shared parameter is retrieved from the SharedParameterElement.

<table summary="" id="GUID-B8342E8A-CFF1-4670-B85F-6F952DE993B8__TABLE_0D36FD6D39C342238FAF2997C6DF7514"><tbody><tr><td><b>Code Region: Getting the definition of a shared parameter</b></td></tr><tr><td><pre><code><span>// Check if a given shared parameter in a schedule can vary across groups</span><span>
</span><span>public</span><span> </span><span>bool</span><span> </span><span>CanParamVaryAcrossGroups</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>string</span><span> sharedParamName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> variesAcrossGroups </span><span>=</span><span> </span><span>false</span><span>;</span><span>

    </span><span>int</span><span> numFields </span><span>=</span><span>  schedule</span><span>.</span><span>Definition</span><span>.</span><span>GetFieldCount</span><span>();</span><span>
    </span><span>// Find the field with the given name</span><span>
    </span><span>for</span><span> </span><span>(</span><span>int</span><span> i </span><span>=</span><span> </span><span>0</span><span>;</span><span> i </span><span>&lt;</span><span> numFields</span><span>;</span><span> i</span><span>++)</span><span>
       </span><span>{</span><span>
              </span><span>ScheduleField</span><span> field </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>.</span><span>GetField</span><span>(</span><span>i</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>field</span><span>.</span><span>GetName</span><span>().</span><span>Contains</span><span>(</span><span>sharedParamName</span><span>))</span><span>
        </span><span>{</span><span>
            </span><span>// Get the SharedParameterElement from the field's parameter id</span><span>
            </span><span>SharedParameterElement</span><span> spe </span><span>=</span><span> schedule</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>field</span><span>.</span><span>ParameterId</span><span>)</span><span> </span><span>as</span><span> </span><span>SharedParameterElement</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>spe </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>InternalDefinition</span><span> definition </span><span>=</span><span> spe</span><span>.</span><span>GetDefinition</span><span>();</span><span>
                variesAcrossGroups </span><span>=</span><span> definition</span><span>.</span><span>VariesAcrossGroups</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
       </span><span>}</span><span>

    </span><span>return</span><span> variesAcrossGroups</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

SharedParameterElements are especially useful when working with [RebarContainers](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Rebar_Containers_html "Rebar Containers are elements which represent an aggregation of rebars in one host. This element can only be created via the API."). A shared parameter can be added as an override to the parameters manager for a RebarContainer. The shared parameter does not need to be bound to any categories to be added as an override. The following example adds a given shared parameter as an override to a RebarContainer.

<table summary="" id="GUID-B8342E8A-CFF1-4670-B85F-6F952DE993B8__TABLE_7439F7FF5ED14855B13B4FB4831915E0"><tbody><tr><td><b>Code Region: Using a SharedParameterElement as an override for a RebarContainer</b></td></tr><tr><td><pre><code><span>// Find the named shared parameter and add it as an override to the parameter manger for the given RebarContainer</span><span>
</span><span>void</span><span> </span><span>AddSharedParameterOverride</span><span>(</span><span>RebarContainer</span><span> container</span><span>,</span><span> </span><span>string</span><span> sharedParamName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// find the shared parameter guid</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>container</span><span>.</span><span>Document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>SharedParameterElement</span><span>));</span><span>
    </span><span>IEnumerable</span><span>&lt;</span><span>SharedParameterElement</span><span>&gt;</span><span> paramCollector </span><span>=</span><span> collector</span><span>.</span><span>Cast</span><span>&lt;</span><span>SharedParameterElement</span><span>&gt;();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>SharedParameterElement</span><span> spe </span><span>in</span><span> paramCollector</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>spe</span><span>.</span><span>Name</span><span>.</span><span>CompareTo</span><span>(</span><span>sharedParamName</span><span>)</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>RebarContainerParameterManager</span><span> paramManager </span><span>=</span><span> container</span><span>.</span><span>GetParametersManager</span><span>();</span><span>
            paramManager</span><span>.</span><span>AddSharedParameterAsOverride</span><span>(</span><span>spe</span><span>.</span><span>Id</span><span>);</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
