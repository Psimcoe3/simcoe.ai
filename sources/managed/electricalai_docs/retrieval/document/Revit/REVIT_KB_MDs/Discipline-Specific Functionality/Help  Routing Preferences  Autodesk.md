---
created: 2026-01-28T21:09:00 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Routing_Preferences_html
author: 
---

# Help | Routing Preferences | Autodesk

> ## Excerpt
> Routing prefences are accessible through the RoutingPreferenceManager class. An instance of this class is available from a property of the MEPCurveType class. Currently, only PipeType and DuctType support routing preferences.

---
Routing prefences are accessible through the RoutingPreferenceManager class. An instance of this class is available from a property of the MEPCurveType class. Currently, only PipeType and DuctType support routing preferences.

The RoutingPreferenceManager manages all rules for selecting segment types and sizes as well as fitting types based on user selection criteria. The RoutingPreferenceRule class manages one segment or fitting preference and instances of this class can be added to the RoutingPreferenceManager. Each routing preference rule is grouped according to what type of routing item in manages. The type is represented by the RoutingPreferenceRuleGroupType and includes these options:

<table summary="" id="GUID-A3B0E633-3EE8-455C-A97D-E5FB4BD4219F__TABLE_8CCB5A531EBD4B9EBB54FF5E33FB6D59"><tbody><tr><td><b>Member name</b></td><td><b>Description</b></td></tr><tr><td>Undefined</td><td>Undefined group type (default initial value)</td></tr><tr><td>Segments</td><td>Segment types (e.g. pipe stocks)</td></tr><tr><td>Elbows</td><td>Elbow types</td></tr><tr><td>Junctions</td><td>Junction types (e.g. takeoff, tee, wye, tap)</td></tr><tr><td>Crosses</td><td>Cross types</td></tr><tr><td>Transitions</td><td>Transition types (Note that the multi-shape transitions may have their own groups)</td></tr><tr><td>Unions</td><td>Union types that connect two segments together</td></tr><tr><td>MechanicalJoints</td><td>Mechanical joint types that connect fitting to fitting, segment to fitting, or segment to segment</td></tr><tr><td>TransitionsRectangularToRound</td><td>Multi-shape transition from the rectangular profile to the round profile</td></tr><tr><td>TransitionsRectangularToOval</td><td>Multi-shape transition from the rectangular profile to the oval profile</td></tr><tr><td>TransitionsOvalToRound</td><td>Multi-shape transition from the oval profile to the round profile</td></tr></tbody></table>

Each routing preference rule can have one or more selection criteria, represented by the RoutingCriterionBase class, and the derived type PrimarySizeCriterion. PrimarySizeCriterion selects fittings and segments based on minimum and maximum size constraints.

The RoutingConditions class holds a collection of RoutingCondition instances. The RoutingCondition class represents routing information that is used as input when determining if a routing criterion, such as minimum or maximum diameter, is met. The RoutingPreferencesManager.GetMEPPartId() method gets a fitting or segment id based on a RoutingPreferenceRuleGroupType and RoutingConditions.

The following example gets all the pipe types in the document, gets the routing preference manager for each one, then gets the sizes for each segment based on the rules in the routing preference manager.

<table summary="" id="GUID-A3B0E633-3EE8-455C-A97D-E5FB4BD4219F__TABLE_D7312BF9EF464B64995AE941B2BC71EC"><tbody><tr><td><b>Code Region: Using Routing Preferences</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>List</span><span>&lt;double&gt;</span><span> </span><span>GetAvailablePipeSegmentSizesFromDocument</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>System</span><span>.</span><span>Collections</span><span>.</span><span>Generic</span><span>.</span><span>HashSet</span><span>&lt;double&gt;</span><span> sizes </span><span>=</span><span> </span><span>new</span><span> </span><span>HashSet</span><span>&lt;double&gt;</span><span>();</span><span>

    </span><span>FilteredElementCollector</span><span> collectorPipeType </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collectorPipeType</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>PipeType</span><span>));</span><span>

    </span><span>IEnumerable</span><span>&lt;</span><span>PipeType</span><span>&gt;</span><span> pipeTypes </span><span>=</span><span> collectorPipeType</span><span>.</span><span>ToElements</span><span>().</span><span>Cast</span><span>&lt;</span><span>PipeType</span><span>&gt;();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>PipeType</span><span> pipeType </span><span>in</span><span> pipeTypes</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>RoutingPreferenceManager</span><span> rpm </span><span>=</span><span> pipeType</span><span>.</span><span>RoutingPreferenceManager</span><span>;</span><span>

        </span><span>int</span><span> segmentCount </span><span>=</span><span> rpm</span><span>.</span><span>GetNumberOfRules</span><span>(</span><span>RoutingPreferenceRuleGroupType</span><span>.</span><span>Segments</span><span>);</span><span>
        </span><span>for</span><span> </span><span>(</span><span>int</span><span> index </span><span>=</span><span> </span><span>0</span><span>;</span><span> index </span><span>!=</span><span> segmentCount</span><span>;</span><span> </span><span>++</span><span>index</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>RoutingPreferenceRule</span><span> segmentRule </span><span>=</span><span> rpm</span><span>.</span><span>GetRule</span><span>(</span><span>RoutingPreferenceRuleGroupType</span><span>.</span><span>Segments</span><span>,</span><span> index</span><span>);</span><span>
            </span><span>Segment</span><span> segment </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>segmentRule</span><span>.</span><span>MEPPartId</span><span>)</span><span> </span><span>as</span><span> </span><span>Segment</span><span>;</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>MEPSize</span><span> size </span><span>in</span><span> segment</span><span>.</span><span>GetSizes</span><span>())</span><span>
            </span><span>{</span><span>
                sizes</span><span>.</span><span>Add</span><span>(</span><span>size</span><span>.</span><span>NominalDiameter</span><span>);</span><span>  </span><span>//Use a hash-set to remove duplicate sizes among Segments and PipeTypes.</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>List</span><span>&lt;double&gt;</span><span> sizesSorted </span><span>=</span><span> sizes</span><span>.</span><span>ToList</span><span>();</span><span>
    sizesSorted</span><span>.</span><span>Sort</span><span>();</span><span>
    </span><span>return</span><span> sizesSorted</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
