---
created: 2026-01-28T21:17:49 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Registering_Events_html
author: 
---

# Help | Registering Events | Autodesk

> ## Excerpt
> Where and how to register events.

---
Where and how to register events.

Using events is a two step process. First, you must have a function that will handle the event notification. This function must take two parameters, the first is an Object that denotes the "sender" of the event notification, the second is an event-specific object that contains event arguments specific to that event. For example, to register the DocumentSavingAs event, your event handler must take a second parameter that is a DocumentSavingAsEventArgs object.

The second part of using an event is registering the event with Revit. This can be done as early as in the OnStartup() function through the ControlledApplication parameter, or at any time after Revit starts up. Although events can be registered for External Commands as well as External Applications, it is not recommended unless the External Command registers and unregisters the event in the same external command. Also note that registering to and unregistering from events must happen while executing on the main thread. An exception will be thrown if an external application attempts to register to (or unregister from) events from outside of a valid API context.

The following example registers the DocumentOpened event, and when that event is triggered, this application will set the address of the project.

<table summary="" id="GUID-8DF6F94A-1460-42AD-AC00-CF92B9A135BA__TABLE_1777953E7120479DB3E78278CB9B7CA5"><tbody><tr><td><b>Code Region 24-1: Registering ControlledApplication.DocumentOpened</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>Application_DocumentOpened</span><span> </span><span>:</span><span> </span><span>IExternalApplication</span><span>
</span><span>{</span><span>
    </span><span>/// &lt;ExampleMethod&gt;</span><span>
    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Implement this method to subscribe to event.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>try</span><span>
        </span><span>{</span><span>
            </span><span>// Register event. </span><span>
            application</span><span>.</span><span>ControlledApplication</span><span>.</span><span>DocumentOpened</span><span> </span><span>+=</span><span> </span><span>new</span><span> </span><span>EventHandler</span><span>
                </span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Events</span><span>.</span><span>DocumentOpenedEventArgs</span><span>&gt;(</span><span>application_DocumentOpened</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// remove the event.</span><span>
        application</span><span>.</span><span>ControlledApplication</span><span>.</span><span>DocumentOpened</span><span> </span><span>-=</span><span> application_DocumentOpened</span><span>;</span><span>
        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>void</span><span> application_DocumentOpened</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>DocumentOpenedEventArgs</span><span> args</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// get document from event args.</span><span>
        </span><span>Document</span><span> doc </span><span>=</span><span> args</span><span>.</span><span>Document</span><span>;</span><span>

        </span><span>// Following code snippet demonstrates support of DocumentOpened event to modify the model.</span><span>
        </span><span>// Because DocumentOpened supports model changes, it allows user to update document data.</span><span>
        </span><span>// Here, this sample assigns a specified value to ProjectInformation.Address property. </span><span>
        </span><span>// User can change other properties of document or create(delete) something as he likes.</span><span>
        </span><span>//</span><span>
        </span><span>// Please note that ProjectInformation property is empty for family document.</span><span>
        </span><span>// So please don't run this sample on family document.</span><span>
        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Edit Address"</span><span>))</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>transaction</span><span>.</span><span>Start</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
            </span><span>{</span><span>
                doc</span><span>.</span><span>ProjectInformation</span><span>.</span><span>Address</span><span> </span><span>=</span><span>
                    </span><span>"United States - Massachusetts - Waltham - 1560 Trapelo Road"</span><span>;</span><span>
                transaction</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
