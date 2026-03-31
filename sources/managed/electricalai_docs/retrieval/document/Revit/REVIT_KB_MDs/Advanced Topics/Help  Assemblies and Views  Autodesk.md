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
