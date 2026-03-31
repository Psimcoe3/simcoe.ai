---
created: 2026-01-28T21:15:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Commands_html
author: 
---

# Help | Commands | Autodesk

> ## Excerpt
> The Revit API provides access to existing Revit commands, either located on a tab, the application menu, or right-click menu. The main ways to work with Revit commands using the API is to either replace the existing command implementation or to post a command.

---
The Revit API provides access to existing Revit commands, either located on a tab, the application menu, or right-click menu. The main ways to work with Revit commands using the API is to either replace the existing command implementation or to post a command.

### Overriding a Revit command

The AddInCommandBinding class can be used to override an existing command in Revit. It has three events related to replacing the existing command implementation.

-   **BeforeExecuted**\- This read-only event occurs before the associated command executes. An application can react to this event but cannot make changes to documents, or affect the invocation of the command.
-   **CanExecute** - Occurs when the associated command initiates a check to determine whether the command can be executed on the command target.
-   **Executed** - This event occurs when the associated command executes and is where any overriding implementation should be performed.

To create the commandbinding, call either UIApplication.CreateAddInCommandBinding() or UIControlledApplication.CreateAddInCommandBinding(). Both methods require a RevitCommandId id to identify the command handler you want to replace. The RevitCommandId has two static methods for obtaining a command's id:

-   **LookupCommandId** - Retrieves the Revit command id with the given id string. To find the command id string, open a session of Revit, invoke the desired command, close Revit, then look in the journal from that session. The "Jrn.Command" entry that was recorded when it was selected will have the string needed for LookupCommandId() and will look something like "ID\_EDIT\_DESIGNOPTIONS".
-   **LookupPostableCommandId** - Retrieves the Revit command id using the PostableCommand enumeration. This only works for commands which are postable (discussed in the following section).

The following example, taken from Revit 2014 SDK's DisableCommand sample, demonstrates how to create an AddInCommandBinding and override the implementation to disable the command with a message to the user.

<table summary="" id="GUID-1C7289DE-8D10-47B5-B6DB-EA1310851C8F__TABLE_0A7CD204C02844D988173E09F5D9A3D7"><tbody><tr><td><b>Code Region: Overriding a command</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Implements the Revit add-in interface IExternalApplication</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>MyApplication</span><span> </span><span>:</span><span> </span><span>IExternalApplication</span><span>
</span><span>{</span><span>
    </span><span>#region IExternalApplication Members</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Implements the OnStartup event</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="application"&gt;&lt;/param&gt;</span><span>
    </span><span>/// &lt;returns&gt;&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Lookup the desired command by name</span><span>
        s_commandId </span><span>=</span><span> </span><span>RevitCommandId</span><span>.</span><span>LookupCommandId</span><span>(</span><span>s_commandToDisable</span><span>);</span><span>

        </span><span>// Confirm that the command can be overridden</span><span>
        </span><span>if</span><span> </span><span>(!</span><span>s_commandId</span><span>.</span><span>CanHaveBinding</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ShowDialog</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"The target command "</span><span> </span><span>+</span><span> s_commandToDisable </span><span>+</span><span>
                        </span><span>" selected for disabling cannot be overridden"</span><span>);</span><span>
   </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>// Create a binding to override the command.</span><span>
        </span><span>// Note that you could also implement .CanExecute to override the accessibiliy of the command.</span><span>
        </span><span>// Doing so would allow the command to be grayed out permanently or selectively, however,</span><span>
        </span><span>// no feedback would be available to the user about why the command is grayed out.</span><span>
        </span><span>try</span><span>
        </span><span>{</span><span>
            </span><span>AddInCommandBinding</span><span> commandBinding </span><span>=</span><span> application</span><span>.</span><span>CreateAddInCommandBinding</span><span>(</span><span>s_commandId</span><span>);</span><span>
            commandBinding</span><span>.</span><span>Executed</span><span> </span><span>+=</span><span> </span><span>DisableEvent</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>// Most likely, this is because someone else has bound this command already.</span><span>
        </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ShowDialog</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"This add-in is unable to disable the target command "</span><span> </span><span>+</span><span> s_commandToDisable </span><span>+</span><span>
                        </span><span>"; most likely another add-in has overridden this command."</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Implements the OnShutdown event</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="application"&gt;&lt;/param&gt;</span><span>
    </span><span>/// &lt;returns&gt;&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Remove the command binding on shutdown</span><span>
        </span><span>if</span><span> </span><span>(</span><span>s_commandId</span><span>.</span><span>HasBinding</span><span>)</span><span>
            application</span><span>.</span><span>RemoveAddInCommandBinding</span><span>(</span><span>s_commandId</span><span>);</span><span>
        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>#endregion</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// A command execution method which disables any command it is applied to (with a user-visible message).</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="sender"&gt;Event sender.&lt;/param&gt;</span><span>
    </span><span>/// &lt;param name="args"&gt;Arguments.&lt;/param&gt;</span><span>
    </span><span>private</span><span> </span><span>void</span><span> </span><span>DisableEvent</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>ExecutedEventArgs</span><span> args</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>ShowDialog</span><span>(</span><span>"Disabled"</span><span>,</span><span> </span><span>"Use of this command has been disabled."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Show a task dialog with a message and title.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="title"&gt;The title.&lt;/param&gt;</span><span>
    </span><span>/// &lt;param name="message"&gt;The message.&lt;/param&gt;</span><span>
    </span><span>private</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>ShowDialog</span><span>(</span><span>string</span><span> title</span><span>,</span><span> </span><span>string</span><span> message</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Show the user a message.</span><span>
        </span><span>TaskDialog</span><span> td </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>title</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>MainInstruction</span><span> </span><span>=</span><span> message</span><span>,</span><span>
            </span><span>TitleAutoPrefix</span><span> </span><span>=</span><span> </span><span>false</span><span>
        </span><span>};</span><span>
        td</span><span>.</span><span>Show</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// The string name of the command to disable.  To lookup a command id string, open a session of Revit,</span><span>
    </span><span>/// invoke the desired command, close Revit, then look to the journal from that session.  The command</span><span>
    </span><span>/// id string will be toward the end of the journal, look for the "Jrn.Command" entry that was recorded</span><span>
    </span><span>/// when it was selected.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>static</span><span> </span><span>String</span><span> s_commandToDisable </span><span>=</span><span> </span><span>"ID_EDIT_DESIGNOPTIONS"</span><span>;</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// The command id, stored statically to allow for removal of the command binding.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>static</span><span> </span><span>RevitCommandId</span><span> s_commandId</span><span>;</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>

### Posting a command

The method UIApplication.PostCommand() will post a command to the Revit message queue to be invoked when control returns from the current API application. Only certain commands can be posted this way. They include all of the commands in the Autodesk.Revit.UI.PostableCommand enumerated type as well as external commands created by any add-in.

Note: Even a postable command may not execute when using PostCommand(). One reason this may happen is if another command has already been posted. Only one command may be posted to Revit at a given time, so if a second command is posted, PostCommand() will throw an exception. Another reason a posted command may not execute is if the command to be executed is not accessible at the time. Whether it is accessible is determined only at the point where Revit returns from the API context, so a failure to execute for this reason will not be reported directly back to the application that posted the command. UIApplication. CanPostCommand() can be used to identify if the given command can be posted, meaning whether it is a member of PostableCommand or an external command. It does not identify if the command is currently accessible.

Both PostCommand() and CanPostCommand() require a RevitCommandId which can be obtained as described in the "Overriding a Revit command" section above.
