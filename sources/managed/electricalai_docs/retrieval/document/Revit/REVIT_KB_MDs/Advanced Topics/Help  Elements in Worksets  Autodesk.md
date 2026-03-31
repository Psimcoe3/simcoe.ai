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
