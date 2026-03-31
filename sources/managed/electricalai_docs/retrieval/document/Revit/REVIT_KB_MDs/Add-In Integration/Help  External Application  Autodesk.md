---
created: 2026-01-28T20:36:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | External Application | Autodesk

> ## Excerpt
> Developers can add functionality through External Applications as well as External Commands. Ribbon tabs and ribbon panels are customized using the External Application. Ribbon panel buttons are bound to an External command.

---
Developers can add functionality through External Applications as well as External Commands. Ribbon tabs and ribbon panels are customized using the External Application. Ribbon panel buttons are bound to an External command.

### IExternalApplication

To add an External Application to Revit, you create an object that implements the IExternalApplication interface.

The IExternalApplication interface has two abstract methods, OnStartup() and OnShutdown(), which you override in your external application. Revit calls OnStartup() when it starts, and OnShutdown() when it closes.

This is the OnStartup() and OnShutdown() abstract definition:

<table summary="" id="GUID-CEF0F9C9-046E-46E2-9535-3B9620D8A170__TABLE_9667A8DFCE104846B4843149E689BB5C"><tbody><tr><td><b>Code Region 3-6: OnShutdown() and OnStartup()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>interface</span><span> </span><span>IExternalApplication</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>);</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The UIControlledApplication parameter provides access to certain Revit events and allows customization of ribbon panels and controls and the addition of ribbon tabs. For example, the public event DialogBoxShowing of UIControlledApplication can be used to capture the event of a dialog being displayed.

The following code snippet registers the handling function that is called right before a dialog is shown and illustrates how to use the UIControlledApplication type to register an event handler and process the event when it occurs.

<table summary="" id="GUID-CEF0F9C9-046E-46E2-9535-3B9620D8A170__TABLE_17D3914BD26940858D0816F598985571"><tbody><tr><td><b>Code Region 3-8: Using ControlledApplication</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>Application_DialogBoxShowing</span><span> </span><span>:</span><span> </span><span>IExternalApplication</span><span>
</span><span>{</span><span>
        </span><span>// Implement the OnStartup method to register events when Revit starts.</span><span>
        </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Register related events</span><span>
                application</span><span>.</span><span>DialogBoxShowing</span><span> </span><span>+=</span><span> 
        </span><span>new</span><span> </span><span>EventHandler</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Events</span><span>.</span><span>DialogBoxShowingEventArgs</span><span>&gt;(</span><span>AppDialogShowing</span><span>);</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>// Implement this method to unregister the subscribed events when Revit exits.</span><span>
        </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
        </span><span>{</span><span>

                </span><span>// unregister events</span><span>
                application</span><span>.</span><span>DialogBoxShowing</span><span> </span><span>-=</span><span> 
        </span><span>new</span><span> </span><span>EventHandler</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Events</span><span>.</span><span>DialogBoxShowingEventArgs</span><span>&gt;(</span><span>AppDialogShowing</span><span>);</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>// The DialogBoxShowing event handler, which allow you to </span><span>
        </span><span>// do some work before the dialog shows</span><span>
        </span><span>void</span><span> </span><span>AppDialogShowing</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>DialogBoxShowingEventArgs</span><span> args</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// Get the help id of the showing dialog</span><span>
            </span><span>string</span><span> dialogId </span><span>=</span><span> args</span><span>.</span><span>DialogId</span><span>;</span><span>

            </span><span>// return if the dialog has no DialogId (such as with a Task Dialog)</span><span>
            </span><span>if</span><span> </span><span>(</span><span>dialogId </span><span>==</span><span> </span><span>""</span><span>)</span><span>
                </span><span>return</span><span>;</span><span>

            </span><span>// Show the prompt message and allow the user to close the dialog directly.</span><span>
            </span><span>TaskDialog</span><span> taskDialog </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Revit"</span><span>);</span><span>
            taskDialog</span><span>.</span><span>MainContent</span><span> </span><span>=</span><span> </span><span>"A Revit dialog is about to be opened.\n"</span><span> </span><span>+</span><span>
                </span><span>"The DialogId of this dialog is "</span><span> </span><span>+</span><span> dialogId </span><span>+</span><span> </span><span>"\n"</span><span> </span><span>+</span><span>
                </span><span>"Press 'Cancel' to immediately dismiss the dialog"</span><span>;</span><span>
            taskDialog</span><span>.</span><span>CommonButtons</span><span> </span><span>=</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Ok</span><span> </span><span>|</span><span>
                                         </span><span>TaskDialogCommonButtons</span><span>.</span><span>Cancel</span><span>;</span><span>
            </span><span>TaskDialogResult</span><span> result </span><span>=</span><span> taskDialog</span><span>.</span><span>Show</span><span>();</span><span>
            </span><span>if</span><span> </span><span>(</span><span>TaskDialogResult</span><span>.</span><span>Cancel</span><span> </span><span>==</span><span> result</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// dismiss the Revit dialog </span><span>
                args</span><span>.</span><span>OverrideResult</span><span>(</span><span>1</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
