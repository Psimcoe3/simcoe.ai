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
