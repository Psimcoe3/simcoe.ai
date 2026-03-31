---
created: 2026-01-28T21:18:20 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_External_Events_html
author: 
---

# Help | External Events | Autodesk

> ## Excerpt
> The Revit API provides an External Events framework to accommodate the use of modeless dialogs. It is tailored for asynchronous processing and operates similarly to the Idling event with default frequency.

---
The Revit API provides an External Events framework to accommodate the use of modeless dialogs. It is tailored for asynchronous processing and operates similarly to the Idling event with default frequency.

To implement a modeless dialog using the External Events framework, follow these steps:

1.  Implement an external event handler by deriving from the IExternalEventHandler interface
2.  Create an ExternalEvent using the static ExternalEvent.Create() method
3.  When an event occurs in the modeless dialog where a Revit action needs to be taken, call ExternalEvent.Raise()
4.  Revit will call the implementation of the IExternalEventHandler.Execute() method when there is an available Idling time cycle.
    
    ### IExternalEventHandler
    

This is the interface to be implemented for an external event. An instance of a class implementing this interface is registered with Revit, and every time the corresponding external event is raised, the Execute method of this interface is invoked.

The IExternalEventHandler has only two methods to implement, the Execute() method and GetName() which should return the name of the event. Below is a basic implementation which will display a TaskDialog when the event is raised.

<table summary="" id="GUID-0A0D656E-5C44-49E8-A891-6C29F88E35C0__TABLE_34FBDABFEC644B8EA286FE00A91E78CC"><tbody><tr><td><b>Code Region: Implementing IExternalEventHandler</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>ExternalEventExample</span><span> </span><span>:</span><span> </span><span>IExternalEventHandler</span><span>
</span><span>{</span><span>
    </span><span>public</span><span> </span><span>void</span><span> </span><span>Execute</span><span>(</span><span>UIApplication</span><span> app</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"External Event"</span><span>,</span><span> </span><span>"Click Close to close."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>string</span><span> </span><span>GetName</span><span>()</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> </span><span>"External Event Example"</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### ExternalEvent

The ExternalEvent class is used to create an ExternalEvent. An instance of this class will be returned to an external event's owner upon the event's creation. The event's owner will use this instance to signal that the event should be called by Revit. Revit will periodically check if any of the events have been signaled (raised), and will execute all events that were raised by calling the Execute method on the events' respective handlers.

The following example shows the implementation of an IExternalApplication that has a method ShowForm() that is called from an ExternalCommand (shown at the end of the code region). The ShowForm() method creates a new instance of the external events handler from the example above, creates a new ExternalEvent and then displays the modeless dialog box which will later use the passed in ExternalEvent object to raise events.

<table summary="" id="GUID-0A0D656E-5C44-49E8-A891-6C29F88E35C0__TABLE_9BCB14BA4854427899766E379E9CEA63"><tbody><tr><td><b>Code Region: Create the ExternalEvent</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>ExternalEventExampleApp</span><span> </span><span>:</span><span> </span><span>IExternalApplication</span><span>
</span><span>{</span><span>
    </span><span>// class instance</span><span>
    </span><span>public</span><span> </span><span>static</span><span> </span><span>ExternalEventExampleApp</span><span> thisApp </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>// ModelessForm instance</span><span>
    </span><span>private</span><span> </span><span>ExternalEventExampleDialog</span><span> m_MyForm</span><span>;</span><span>

    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>m_MyForm </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> m_MyForm</span><span>.</span><span>Visible</span><span>)</span><span>
        </span><span>{</span><span>
            m_MyForm</span><span>.</span><span>Close</span><span>();</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        m_MyForm </span><span>=</span><span> </span><span>null</span><span>;</span><span>   </span><span>// no dialog needed yet; the command will bring it</span><span>
        thisApp </span><span>=</span><span> </span><span>this</span><span>;</span><span>  </span><span>// static access to this application instance</span><span>

        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>//   The external command invokes this on the end-user's request</span><span>
    </span><span>public</span><span> </span><span>void</span><span> </span><span>ShowForm</span><span>(</span><span>UIApplication</span><span> uiapp</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// If we do not have a dialog yet, create and show it</span><span>
        </span><span>if</span><span> </span><span>(</span><span>m_MyForm </span><span>==</span><span> </span><span>null</span><span> </span><span>||</span><span> m_MyForm</span><span>.</span><span>IsDisposed</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// A new handler to handle request posting by the dialog</span><span>
            </span><span>ExternalEventExample</span><span> handler </span><span>=</span><span> </span><span>new</span><span> </span><span>ExternalEventExample</span><span>();</span><span>

            </span><span>// External Event for the dialog to use (to post requests)</span><span>
            </span><span>ExternalEvent</span><span> exEvent </span><span>=</span><span> </span><span>ExternalEvent</span><span>.</span><span>Create</span><span>(</span><span>handler</span><span>);</span><span>

            </span><span>// We give the objects to the new dialog;</span><span>
            </span><span>// The dialog becomes the owner responsible for disposing them, eventually.</span><span>
            m_MyForm </span><span>=</span><span> </span><span>new</span><span> </span><span>ExternalEventExampleDialog</span><span>(</span><span>exEvent</span><span>,</span><span> handler</span><span>);</span><span>
            m_MyForm</span><span>.</span><span>Show</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>[</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>Transaction</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>Manual</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>Command</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
    </span><span>public</span><span> </span><span>virtual</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>try</span><span>
        </span><span>{</span><span>
            </span><span>ExternalEventExampleApp</span><span>.</span><span>thisApp</span><span>.</span><span>ShowForm</span><span>(</span><span>commandData</span><span>.</span><span>Application</span><span>);</span><span>
            </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span> ex</span><span>)</span><span>
        </span><span>{</span><span>
            message </span><span>=</span><span> ex</span><span>.</span><span>Message</span><span>;</span><span>
            </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Raise Event

Once the modeless dialog is displayed, the user may interact with it. Actions in the dialog may need to trigger some action in Revit. When this happens, the ExternalEvent.Raise() method is called. The following example is the code for a simple modeless dialog with two buttons: one to raise our event and one to close the dialog.

<table summary="" id="GUID-0A0D656E-5C44-49E8-A891-6C29F88E35C0__TABLE_F02CB5FDB6DF4F9EB41A1DE944176998"><tbody><tr><td><b>Code Region: Raise the Event</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>partial</span><span> </span><span>class</span><span> </span><span>ExternalEventExampleDialog</span><span> </span><span>:</span><span> </span><span>Form</span><span>
</span><span>{</span><span>
    </span><span>private</span><span> </span><span>ExternalEvent</span><span> m_ExEvent</span><span>;</span><span>
    </span><span>private</span><span> </span><span>ExternalEventExample</span><span> m_Handler</span><span>;</span><span>

    </span><span>public</span><span> </span><span>ExternalEventExampleDialog</span><span>(</span><span>ExternalEvent</span><span> exEvent</span><span>,</span><span> </span><span>ExternalEventExample</span><span> handler</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>InitializeComponent</span><span>();</span><span>
        m_ExEvent </span><span>=</span><span> exEvent</span><span>;</span><span>
        m_Handler </span><span>=</span><span> handler</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>protected</span><span> </span><span>override</span><span> </span><span>void</span><span> </span><span>OnFormClosed</span><span>(</span><span>FormClosedEventArgs</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// we own both the event and the handler</span><span>
        </span><span>// we should dispose it before we are closed</span><span>
        m_ExEvent</span><span>.</span><span>Dispose</span><span>();</span><span>
        m_ExEvent </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        m_Handler </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>// do not forget to call the base class</span><span>
        </span><span>base</span><span>.</span><span>OnFormClosed</span><span>(</span><span>e</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>private</span><span> </span><span>void</span><span> closeButton_Click</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>EventArgs</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Close</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>private</span><span> </span><span>void</span><span> showMessageButton_Click</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>EventArgs</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        m_ExEvent</span><span>.</span><span>Raise</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

When the ExternalEvent.Raise() method is called, Revit will wait for an available Idling timecycle and then call the IExternalEventHandler.Execute() method. In this simple example, it will display a TaskDialog with the text "Click Close to close." as shown in the first code region above.

For a more complex example of using the External Events framework, see the sample code in the SDK under the ModelessDialog\\ModelessForm\_ExternalEvent folder. It uses a modeless dialog with numerous buttons and the IExternalEventHandler implementation has a public property to track which button was pressed so it can switch on that value in the Execute() method.
