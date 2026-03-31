---
created: 2026-01-28T20:40:34 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Revit-style Task Dialogs | Autodesk

> ## Excerpt
> A TaskDialog is a Revit-style alternative to a simple Windows MessageBox. It can be used to display information and receive simple input from the user. It has a common set of controls that are arranged in a standard order to assure consistent look and feel with the rest of Revit.

---
A TaskDialog is a Revit-style alternative to a simple Windows MessageBox. It can be used to display information and receive simple input from the user. It has a common set of controls that are arranged in a standard order to assure consistent look and feel with the rest of Revit.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-6D0C2A00-3CB5-4963-B108-515FA6924728-low.png)**Figure 19: Revit-style Task Dialog**

There are two ways to create and show a task dialog to the user. The first option is to construct the TaskDialog, set its properties individually, and use the instance method Show() to show it to the user. The second is to use one of the static Show() methods to construct and show the dialog in one step. When you use the static methods only a subset of the options can be specified.

The property `TaskDialog.EnableMarqueeDialogBar` allows the TaskDialog to include a progress bar that has an indeterminate start and stop. The animation continues until the TaskDialog is closed.

Please see [Dialog Guidelines](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_API_User_Interface_Guidelines_Dialog_Guidelines_html) in the [API User Interface Guidelines](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_API_User_Interface_Guidelines_html) section for information on developing a task dialog that is compliant with the standards used by Autodesk.

___

The following example shows how to create and display the task dialog shown above.

<table summary="" id="GUID-68BD5F44-972C-47CE-9D49-543B37C90561__TABLE_698EACD7E65245699E26E565C7CFE955"><tbody><tr><td><b>Code Region 3-27: Displaying Revit-style TaskDialog</b></td></tr><tr><td><pre><code><span>[</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>Transaction</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>ReadOnly</span><span>)]</span><span>
</span><span>class</span><span> </span><span>TaskDialogExample</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementSet</span><span> elements</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Get the application and document from external command data.</span><span>
                </span><span>Application</span><span> app </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>.</span><span>Application</span><span>;</span><span>
                </span><span>Document</span><span> activeDoc </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>

                </span><span>// Creates a Revit task dialog to communicate information to the user.</span><span>
                </span><span>TaskDialog</span><span> mainDialog </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Hello, Revit!"</span><span>);</span><span>
                mainDialog</span><span>.</span><span>MainInstruction</span><span> </span><span>=</span><span> </span><span>"Hello, Revit!"</span><span>;</span><span>
                mainDialog</span><span>.</span><span>MainContent</span><span> </span><span>=</span><span> 
                        </span><span>"This sample shows how to use a Revit task dialog to communicate with the user."</span><span> 
                        </span><span>+</span><span> </span><span>"The command links below open additional task dialogs with more information."</span><span>;</span><span>

                </span><span>// Add commmandLink options to task dialog</span><span>
                mainDialog</span><span>.</span><span>AddCommandLink</span><span>(</span><span>TaskDialogCommandLinkId</span><span>.</span><span>CommandLink1</span><span>,</span><span>
                         </span><span>"View information about the Revit installation"</span><span>);</span><span>
                mainDialog</span><span>.</span><span>AddCommandLink</span><span>(</span><span>TaskDialogCommandLinkId</span><span>.</span><span>CommandLink2</span><span>,</span><span> 
                                </span><span>"View information about the active document"</span><span>);</span><span>

                </span><span>// Set common buttons and default button. If no CommonButton or CommandLink is added,</span><span>
                </span><span>// task dialog will show a Close button by default</span><span>
                mainDialog</span><span>.</span><span>CommonButtons</span><span> </span><span>=</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Close</span><span>;</span><span>
                mainDialog</span><span>.</span><span>DefaultButton</span><span> </span><span>=</span><span> </span><span>TaskDialogResult</span><span>.</span><span>Close</span><span>;</span><span>

                </span><span>// Set footer text. Footer text is usually used to link to the help document.</span><span>
                mainDialog</span><span>.</span><span>FooterText</span><span> </span><span>=</span><span> 
                        </span><span>""</span><span>                          </span><span>+</span><span> </span><span>"Click here for the Revit API Developer Center"</span><span>;</span><span>

                </span><span>TaskDialogResult</span><span> tResult </span><span>=</span><span> mainDialog</span><span>.</span><span>Show</span><span>();</span><span>

                </span><span>// If the user clicks the first command link, a simple Task Dialog </span><span>
                </span><span>// with only a Close button shows information about the Revit installation. </span><span>
                </span><span>if</span><span> </span><span>(</span><span>TaskDialogResult</span><span>.</span><span>CommandLink1</span><span> </span><span>==</span><span> tResult</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>TaskDialog</span><span> dialog_CommandLink1 </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Revit Build Information"</span><span>);</span><span>
                        dialog_CommandLink1</span><span>.</span><span>MainInstruction</span><span> </span><span>=</span><span> 
                                </span><span>"Revit Version Name is: "</span><span> </span><span>+</span><span> app</span><span>.</span><span>VersionName</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>
                         </span><span>+</span><span> </span><span>"Revit Version Number is: "</span><span> </span><span>+</span><span> app</span><span>.</span><span>VersionNumber</span><span> </span><span>+</span><span> </span><span>"\n"</span><span> 
                                </span><span>+</span><span> </span><span>"Revit Version Build is: "</span><span> </span><span>+</span><span> app</span><span>.</span><span>VersionBuild</span><span>;</span><span>

                        dialog_CommandLink1</span><span>.</span><span>Show</span><span>();</span><span>

                </span><span>}</span><span>

                </span><span>// If the user clicks the second command link, a simple Task Dialog </span><span>
                </span><span>// created by static method shows information about the active document</span><span>
                </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>TaskDialogResult</span><span>.</span><span>CommandLink2</span><span> </span><span>==</span><span> tResult</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Active Document Information"</span><span>,</span><span> 
                                </span><span>"Active document: "</span><span> </span><span>+</span><span> activeDoc</span><span>.</span><span>Title</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>
                         </span><span>+</span><span> </span><span>"Active view name: "</span><span> </span><span>+</span><span> activeDoc</span><span>.</span><span>ActiveView</span><span>.</span><span>Name</span><span>);</span><span>
                </span><span>}</span><span>

                </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
