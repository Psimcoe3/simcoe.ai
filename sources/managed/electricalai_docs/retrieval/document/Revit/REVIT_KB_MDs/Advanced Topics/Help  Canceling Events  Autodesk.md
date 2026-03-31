---
created: 2026-01-28T21:17:54 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Canceling_Events_html
author: 
---

# Help | Canceling Events | Autodesk

> ## Excerpt
> Events that are triggered before an action has taken place (i.e. DocumentSaving) are often cancellable. (Use the Cancellable property to determine if the event can be cancelled.) For example, you may want to check some criteria are met in a model before it is saved. By registering for the DocumentSaving or DocumentSavingAs event, for example, you can check for certain criteria in the document and cancel the Save or Save As action. Once cancelled, an event cannot be un-cancelled.

---
Events that are triggered before an action has taken place (i.e. DocumentSaving) are often cancellable. (Use the Cancellable property to determine if the event can be cancelled.) For example, you may want to check some criteria are met in a model before it is saved. By registering for the DocumentSaving or DocumentSavingAs event, for example, you can check for certain criteria in the document and cancel the Save or Save As action. Once cancelled, an event cannot be un-cancelled.

Note: If a pre-event is cancelled, other event handlers that have subscribed to the event will not be notified. However, handlers that have subscribed to a post-event related to the pre-event will be notified. The following event handler for the DocumentSavingAs event checks if the ProjectInformation Status parameter is empty, and if it is, cancels the SaveAs event. Note that if your application cancels an event, it should offer an explanation to the user.

<table summary="" id="GUID-318E460B-FBA3-4C6F-95F4-96352515F6A2__TABLE_FED5415922934CDFAE484C031669D51B"><tbody><tr><td><b>Code Region 24-2: Canceling an Event</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CheckProjectStatusInitial</span><span>(</span><span>Object</span><span> sender</span><span>,</span><span> </span><span>DocumentSavingAsEventArgs</span><span> args</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Document</span><span> doc </span><span>=</span><span> args</span><span>.</span><span>Document</span><span>;</span><span>
        </span><span>ProjectInfo</span><span> proInfo </span><span>=</span><span> doc</span><span>.</span><span>ProjectInformation</span><span>;</span><span>

        </span><span>// Project information is only available for project document.</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> proInfo</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>string</span><span>.</span><span>IsNullOrEmpty</span><span>(</span><span>proInfo</span><span>.</span><span>Status</span><span>))</span><span>
                </span><span>{</span><span>

                        </span><span>// cancel the save as process.</span><span>
                        args</span><span>.</span><span>Cancel</span><span>();</span><span>
                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Status project parameter is not set.  Save is aborted."</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: Although most event arguments have the Cancel and Cancellable properties, the DocumentChanged and FailuresProcessing events have corresponding Cancel() and IsCancellable() methods.
