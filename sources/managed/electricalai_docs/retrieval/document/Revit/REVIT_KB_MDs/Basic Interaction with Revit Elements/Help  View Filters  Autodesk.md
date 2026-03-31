---
created: 2026-01-28T20:52:53 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Filters_html
author: 
---

# Help | View Filters | Autodesk

> ## Excerpt
> Filters are elements independent of views. They can be applied to Views using the ParameterFilterElement class or a SelectionFilterElement class.

---
Filters are elements independent of views. They can be applied to Views using the ParameterFilterElement class or a SelectionFilterElement class.

### ParameterFilterElement

A ParameterFilterElement filters elements based on the elements’ categories and an ElementFilter. The ElementFilter must be either an ElementParameterFilter or an ElementLogicalFilter containing only ElementParameterFilters and other ElementLogicalFilters. This allows the view filter to be constructed from a combination of AND and OR filters that are then gathered by an AND filter, an OR filter, or an ElementParameterFilter as an input to ParameterFilterElement.Create().

Once a filter has been defined (with one or more categories and zero or more filter rules), it can be applied to a View using one of several methods. The View.AddFilter() method will apply the filter to the view, but with default overrides, meaning the view's display will not change. View.SetFilterOverrides() sets graphical overrides associated with a filter. Setting elements that pass a filter to not be visibile in a view is done with View.SetFilterVisibility(ElementId filterElementId, bool visibility). AddFilter() and SetFilterVisibility() will both apply the filter to the view if it is not already applied, making it unnecessary to call AddFilter() separately.

#### Validation

Validation restrictions for the ElementFilter stored by a ParameterFilterElement (the class that represents a View Filter) support flexible creation of OR filters where criteria can reference parameters only associated to specific categories. The ElementFilter must be either an ElementParameterFilter or an ElementLogicalFilter representing a Boolean combination of ElementParameterFilters.

In addition, Revit checks that each ElementParameterFilter satisfies the following conditions:

-   Its array of FilterRules is not empty and contains:
    -   Any number of FilterRules of type FilterValueRule, FilterInverseRule, and SharedParameterApplicableRule or
    -   Exactly one FilterCategoryRule containing only one category from categories stored by this ParameterFilterElement or
    -   Exactly two rules: the first one is a FilterCategoryRule containing only one category from categories stored by this ParameterFilterElement and the second one is a FilterRule of type FilterValueRule, FilterInverseRule, or SharedParameterApplicableRule.

Cases in the second and third bullet are currently allowed only if the parent node of ElementParameterFilter is LogicalOrFilter.

The method `ParameterFilterElement.GetElementFilterParametersForCategory()` retrieves a list of the parameters associated with all rules in the filter that are combined (using logical AND) with a FilterCategoryRule corresponding to single categoryId.

These methods identify or set if the filter is enabled in this view:

-   View.GetIsFilterEnabled()
-   View.SetIsFilterEnabled()

`View.GetOrderedFilters()` gets the filters applied to the view in the order they are applied.

The following example creates a new view filter matching multiple criteria and then hides those elements in the view.

<table summary="" id="GUID-B6FB80F2-7A17-4242-9E95-D6056090E85B__TABLE_D20AF6F893E34769897200046D711DE2"><tbody><tr><td><b>Code Region: Applying a parameter filter to a view</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateViewFilter</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> categories </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
    categories</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Walls</span><span>));</span><span>
    </span><span>List</span><span>&lt;</span><span>ElementFilter</span><span>&gt;</span><span> elementFilterList </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementFilter</span><span>&gt;();</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Add view filter"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// Criterion 1 - wall type Function is "Exterior"</span><span>
        </span><span>ElementId</span><span> exteriorParamId </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>FUNCTION_PARAM</span><span>);</span><span>
        elementFilterList</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>ParameterFilterRuleFactory</span><span>.</span><span>CreateEqualsRule</span><span>(</span><span>exteriorParamId</span><span>,</span><span> </span><span>(</span><span>int</span><span>)</span><span>WallFunction</span><span>.</span><span>Exterior</span><span>)));</span><span>

        </span><span>// Criterion 2 - wall length &gt; = 28 or &lt; = 14</span><span>
        </span><span>ElementId</span><span> lengthId </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>CURVE_ELEM_LENGTH</span><span>);</span><span>
        </span><span>LogicalOrFilter</span><span> wallHeightFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>LogicalOrFilter</span><span>(</span><span>
            </span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>ParameterFilterRuleFactory</span><span>.</span><span>CreateGreaterOrEqualRule</span><span>(</span><span>lengthId</span><span>,</span><span> </span><span>28.0</span><span>,</span><span> </span><span>0.00001</span><span>)),</span><span>
            </span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>ParameterFilterRuleFactory</span><span>.</span><span>CreateLessOrEqualRule</span><span>(</span><span>lengthId</span><span>,</span><span> </span><span>14.0</span><span>,</span><span> </span><span>0.00001</span><span>)));</span><span>
        elementFilterList</span><span>.</span><span>Add</span><span>(</span><span>wallHeightFilter</span><span>);</span><span>

        </span><span>// Criterion 3 - custom shared parameter value matches string pattern</span><span>
        </span><span>// Get the id for the shared parameter - the ElementId is not hardcoded, so we need to get an instance of this type to find it</span><span>
        </span><span>Guid</span><span> spGuid </span><span>=</span><span> </span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"96b00b61-7f5a-4f36-a828-5cd07890a02a"</span><span>);</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Wall</span><span>));</span><span>
        </span><span>Wall</span><span> wall </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>Wall</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>wall </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Parameter</span><span> sharedParam </span><span>=</span><span> wall</span><span>.</span><span>get_Parameter</span><span>(</span><span>spGuid</span><span>);</span><span>
            </span><span>ElementId</span><span> sharedParamId </span><span>=</span><span> sharedParam</span><span>.</span><span>Id</span><span>;</span><span>

            elementFilterList</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>ParameterFilterRuleFactory</span><span>.</span><span>CreateBeginsWithRule</span><span>(</span><span>sharedParamId</span><span>,</span><span> </span><span>"15."</span><span>,</span><span> </span><span>true</span><span>)));</span><span>
        </span><span>}</span><span>

        </span><span>// Create filter element associated to the input categories</span><span>
        </span><span>LogicalAndFilter</span><span> andFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>LogicalAndFilter</span><span>(</span><span>elementFilterList</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>ParameterFilterElement</span><span>.</span><span>ElementFilterIsAcceptableForParameterFilterElement</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>HashSet</span><span>&lt;</span><span>ElementId</span><span>&gt;(</span><span>categories</span><span>),</span><span> andFilter</span><span>))</span><span>
        </span><span>{</span><span>
            </span><span>ParameterFilterElement</span><span> parameterFilterElement </span><span>=</span><span> </span><span>ParameterFilterElement</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Example view filter"</span><span>,</span><span> categories</span><span>,</span><span> andFilter</span><span>);</span><span>

            </span><span>// Apply filter to view</span><span>
            view</span><span>.</span><span>AddFilter</span><span>(</span><span>parameterFilterElement</span><span>.</span><span>Id</span><span>);</span><span>
            view</span><span>.</span><span>SetFilterVisibility</span><span>(</span><span>parameterFilterElement</span><span>.</span><span>Id</span><span>,</span><span> </span><span>false</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Filter cannot be used"</span><span>);</span><span>
        </span><span>}</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### SelectionFilterElement

A SelectionFilterElement is a special view filter not based on rules, but on a group of possibly unrelated elements. Specific elements can be added to the filter as required and the resulting selection can be overridden just like ParameterFilterElement.

The following example creates a new selection filter and applies an override to it.

<table summary="" id="GUID-B6FB80F2-7A17-4242-9E95-D6056090E85B__TABLE_16DDCED9E9654683A8E7B7A81657AF7F"><tbody><tr><td><b>Code Region: Applying a selection filter to a view</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateSelectionFilter</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// find room tags in this view</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>,</span><span> view</span><span>.</span><span>Id</span><span>);</span><span>
    collector</span><span>.</span><span>WherePasses</span><span>(</span><span>new</span><span> </span><span>RoomTagFilter</span><span>());</span><span>

    </span><span>// collect tags whose room number matches criteria</span><span>
    </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> tagIds </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>RoomTag</span><span> tag </span><span>in</span><span> collector</span><span>.</span><span>Cast</span><span>&lt;</span><span>RoomTag</span><span>&gt;())</span><span>
    </span><span>{</span><span>
        </span><span>int</span><span> number </span><span>=</span><span> </span><span>Int32</span><span>.</span><span>Parse</span><span>(</span><span>tag</span><span>.</span><span>Room</span><span>.</span><span>Number</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>number </span><span>%</span><span> </span><span>3</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
            tagIds</span><span>.</span><span>Add</span><span>(</span><span>tag</span><span>.</span><span>Id</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create SelectionFilterElement"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// Create selection filter and assign ids</span><span>
        </span><span>SelectionFilterElement</span><span> filterElement </span><span>=</span><span> </span><span>SelectionFilterElement</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Room tags filter"</span><span>);</span><span>
        filterElement</span><span>.</span><span>SetElementIds</span><span>(</span><span>tagIds</span><span>);</span><span>

        </span><span>ElementId</span><span> filterId </span><span>=</span><span> filterElement</span><span>.</span><span>Id</span><span>;</span><span>

        </span><span>// Add the filter to the view</span><span>
        view</span><span>.</span><span>AddFilter</span><span>(</span><span>filterId</span><span>);</span><span>

        doc</span><span>.</span><span>Regenerate</span><span>();</span><span>

        </span><span>// Use the existing graphics settings, and change the color to Blue</span><span>
        </span><span>OverrideGraphicSettings</span><span> overrideSettings </span><span>=</span><span> view</span><span>.</span><span>GetFilterOverrides</span><span>(</span><span>filterId</span><span>);</span><span>

        overrideSettings</span><span>.</span><span>SetProjectionLineColor</span><span>(</span><span>new</span><span> </span><span>Color</span><span>(</span><span>0x00</span><span>,</span><span> </span><span>0x00</span><span>,</span><span> </span><span>0xFF</span><span>));</span><span>

        view</span><span>.</span><span>SetFilterOverrides</span><span>(</span><span>filterId</span><span>,</span><span> overrideSettings</span><span>);</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Modifying filters

All filters applied to a view can be retrieved using the View.GetFilters() method which will return a list of filter ids. Filter visibility and graphic overrides can be checked for a specific filter using the View.GetFilterVisibility() and View.GetFilterOverrides() methods respectively. View.RemoveFilter will remove a filter from the view.

The following example demonstrates how to get the filters in a view and then modifies the overrides associated with any filter currently setting the cut color to red.

<table summary="" id="GUID-B6FB80F2-7A17-4242-9E95-D6056090E85B__TABLE_B19DC40567284A65938B03E299351172"><tbody><tr><td><b>Code Region: Modify existing filter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>ModifyExistingFilter</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find any filter with overrides setting cut color to Red</span><span>
    </span><span>Dictionary</span><span>&lt;</span><span>ElementId</span><span>,</span><span> </span><span>OverrideGraphicSettings</span><span>&gt;</span><span> filterIdsToChange </span><span>=</span><span> </span><span>new</span><span> </span><span>Dictionary</span><span>&lt;</span><span>ElementId</span><span>,</span><span> </span><span>OverrideGraphicSettings</span><span>&gt;();</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> filterId </span><span>in</span><span> view</span><span>.</span><span>GetFilters</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>OverrideGraphicSettings</span><span> overrideSettings </span><span>=</span><span> view</span><span>.</span><span>GetFilterOverrides</span><span>(</span><span>filterId</span><span>);</span><span>

        </span><span>Color</span><span> lineColor </span><span>=</span><span> overrideSettings</span><span>.</span><span>CutLineColor</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>lineColor </span><span>==</span><span> </span><span>Color</span><span>.</span><span>InvalidColorValue</span><span>)</span><span>
            </span><span>continue</span><span>;</span><span>

        </span><span>// Save overrides setting the cut color to green</span><span>
        </span><span>if</span><span> </span><span>(</span><span>lineColor</span><span>.</span><span>Red</span><span> </span><span>==</span><span> </span><span>0xFF</span><span> </span><span>&amp;&amp;</span><span> lineColor</span><span>.</span><span>Green</span><span> </span><span>==</span><span> </span><span>0x00</span><span> </span><span>&amp;&amp;</span><span> lineColor</span><span>.</span><span>Blue</span><span> </span><span>==</span><span> </span><span>0x00</span><span>)</span><span>
        </span><span>{</span><span>
            overrideSettings</span><span>.</span><span>SetCutLineColor</span><span>(</span><span>new</span><span> </span><span>Color</span><span>(</span><span>0x00</span><span>,</span><span> </span><span>0xFF</span><span>,</span><span> </span><span>0x00</span><span>));</span><span>
            filterIdsToChange</span><span>[</span><span>filterId</span><span>]</span><span> </span><span>=</span><span> overrideSettings</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// Make the change to all found filters</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Change override filters"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> filterId </span><span>in</span><span> filterIdsToChange</span><span>.</span><span>Keys</span><span>)</span><span>
        </span><span>{</span><span>
            view</span><span>.</span><span>SetFilterOverrides</span><span>(</span><span>filterId</span><span>,</span><span> filterIdsToChange</span><span>[</span><span>filterId</span><span>]);</span><span>
        </span><span>}</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
