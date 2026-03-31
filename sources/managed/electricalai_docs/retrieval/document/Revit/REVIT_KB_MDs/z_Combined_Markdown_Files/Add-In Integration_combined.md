


<!-- ===== BEGIN: Help  External Commands  Autodesk.md ===== -->

---
created: 2026-01-28T20:36:40 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | External Commands | Autodesk

> ## Excerpt
> Developers can add functionality by implementing External Commands which appear in the External Tools menu-button.

---
Developers can add functionality by implementing External Commands which appear in the External Tools menu-button.

## Loading and Running External Commands

When no other commands or edit modes are active in Revit, registered external commands are enabled. When a command is selected, a command object is created and its Execute() method is called. Once this method returns back to Revit, the command object is destroyed. As a result, data cannot persist in the object between command executions. However, there are other ways to save data between command executions; for example you can use the Revit shared parameters mechanism to store data in the Revit project.

You can add External Commands to the External Tools Panel under the External Tools menu-button, or as a custom ribbon panel on the Add-Ins tab, Analyze tab or a new custom ribbon tab. See the [Walkthrough: Hello World](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Walkthrough_Hello_World_html) and [Walkthrough: Add Hello World Ribbon Panel](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Walkthrough_Add_Hello_World_Ribbon_Panel_html) for examples of these two approaches.

External tools, ribbon tabs and ribbon panels are initialized upon start up. The initialization steps are as follows:

-   Revit reads manifest files and identifies:
    -   External Applications that can be invoked.
    -   External Tools that can be added to the Revit External Tools menu-button.
-   External Application session adds panels and content to the Add-ins tab.
    
    ## IExternalCommand
    

You create an external command by creating an object that implements the IExternalCommand interface. The IExternalCommand interface has one abstract method, Execute, which is the main method for external commands.

The Execute() method has three parameters:

-   commandData (ExternalCommandData)
-   message (String)
-   elements (ElementSet)
    
    ### commandData (ExternalCommandData)
    

The ExternalCommandData object contains references to Application and View which are required by the external command. All Revit data is retrieved directly or indirectly from this parameter in the external command.

For example, the following statement illustrates how to retrieve Autodesk.Revit.Document from the commandData parameter:

<table summary="" id="GUID-C84BA0A2-2637-46B0-8BA7-3B0A982485A1__TABLE_06B2D92AA914449F9D30B270B19929B5"><tbody><tr><td><b>Code Region 3-1: Retrieving the Active Document</b></td></tr><tr><td><pre><code><span>Document</span><span> doc </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span></code></pre></td></tr></tbody></table>

The following table illustrates the ExternalCommandData public properties

**Table 1: ExternalCommandData public properties**

<table summary="" id="GUID-C84BA0A2-2637-46B0-8BA7-3B0A982485A1__TABLE_5DFD7881F3EA41808474CBEE08B065AD"><tbody><tr><td><b>Property</b></td><td><b>Description</b></td></tr><tr><td>Application (Autodesk.Revit.UI.UIApplication)</td><td>Retrieves an object that represents the current UIApplication for external command.</td></tr><tr><td>JournalData<p>(IDictionary&lt;String, String&gt;&gt;)</p></td><td>A data map that can be used to read and write data to the Revit journal file.</td></tr><tr><td>View (Autodesk.Revit.DB.View)</td><td>Retrieves an object that represents the View external commands work on.</td></tr></tbody></table>

### message (String):

Error messages are returned by an external command using the output parameter message. The string-type parameter is set in the external command process. When Autodesk.Revit.UI.Result.Failed or Autodesk.Revit.UI.Result.Cancelled is returned, and the message parameter is set, an error dialog appears.

The following code sample illustrates how to use the message parameter.

<table summary="" id="GUID-C84BA0A2-2637-46B0-8BA7-3B0A982485A1__TABLE_F5E59D27DDD645BB99625AF0847A24B8"><tbody><tr><td><b>Code Region 3-2: Setting an error message string</b></td></tr><tr><td><pre><code><span>class</span><span> </span><span>IExternalCommand_message</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>
                </span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span>
                </span><span>ElementSet</span><span> elements</span><span>)</span><span>
        </span><span>{</span><span>
                message </span><span>=</span><span> </span><span>"Could not locate walls for analysis."</span><span>;</span><span>
                </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Implementing the previous external command causes the following dialog box to appear:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-6E76ABBE-ED74-437E-B2FC-D92C9955C035-low.png)**Figure 12: Error message dialog box**

### elements (ElementSet):

Whenever Autodesk.Revit.UI.Result.Failed or Autodesk.Revit.UI.Result.Canceled is returned and the parameter message is not empty, an error or warning dialog box appears. Additionally, if any elements are added to the elements parameter, these elements will be highlighted on screen. It is a good practice to set the message parameter whenever the command fails, whether or not elements are also returned.

The following code highlights pre-selected walls:

<table summary="" id="GUID-C84BA0A2-2637-46B0-8BA7-3B0A982485A1__TABLE_9884FB5648EB43BA9EB7BE0D42941F3A"><tbody><tr><td><b>Code Region 3-3: Highlighting walls</b></td></tr><tr><td><pre><code><span>class</span><span> </span><span>IExternalcommand_elements</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementSet</span><span> elements</span><span>)</span><span>
        </span><span>{</span><span>
                message </span><span>=</span><span> </span><span>"Please note the highlighted Walls."</span><span>;</span><span>
                </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>commandData</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>);</span><span>
                </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Wall</span><span>)).</span><span>ToElements</span><span>();</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> collection</span><span>)</span><span>
                </span><span>{</span><span>
                        elements</span><span>.</span><span>Insert</span><span>(</span><span>e</span><span>);</span><span>
                </span><span>}</span><span>

                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Return

The Return result indicates that the execution failed, succeeded, or is canceled by the user. If it does not succeed, Revit reverses changes made by the external command.

**Table 2: IExternalCommand.Result**

<table summary="" id="GUID-C84BA0A2-2637-46B0-8BA7-3B0A982485A1__TABLE_1C1749CB5DB344AEAE834E5D1044FC1D"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td>Autodesk.Revit.UI.Result.Succeeded</td><td>The external command completed successfully. Revit keeps all changes made by the external command.</td></tr><tr><td>Autodesk.Revit.UI.Result.Failed</td><td>The external command failed to complete the task. Revit reverses operations performed by the external command. If the message parameter of Execute is set, Revit displays a dialog with the text "Error - cannot be ignored".</td></tr><tr><td>Autodesk.Revit.UI.Result.Cancelled</td><td>The user cancelled the external command. Revit reverses changes made by the external command. If the message parameter of Execute is set, Revit displays a dialog with the text "Warning - can be ignored".</td></tr></tbody></table>

The following example displays a greeting message and allows the user to select the return value. Use the Execute() method as the entrance to the Revit application.

<table summary="" id="GUID-C84BA0A2-2637-46B0-8BA7-3B0A982485A1__TABLE_15D685AC852B4F1B93C8AD17EC363C23"><tbody><tr><td><b>Code Region 3-4: Prompting the user</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span>
    </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>try</span><span>
    </span><span>{</span><span>
        </span><span>Document</span><span> doc </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>
        </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>;</span><span>
        </span><span>// Delete selected elements</span><span>

        </span><span>ICollection</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>&gt;</span><span> ids </span><span>=</span><span>
            doc</span><span>.</span><span>Delete</span><span>(</span><span>uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>());</span><span>

        </span><span>TaskDialog</span><span> taskDialog </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Revit"</span><span>);</span><span> 
        taskDialog</span><span>.</span><span>MainContent</span><span> </span><span>=</span><span> 
            </span><span>(</span><span>"Click Yes to return Succeeded. Selected members will be deleted.\n"</span><span> </span><span>+</span><span>
            </span><span>"Click No to return Failed.  Selected members will not be deleted.\n"</span><span> </span><span>+</span><span>
            </span><span>"Click Cancel to return Cancelled.  Selected members will not be deleted."</span><span>);</span><span>
        </span><span>TaskDialogCommonButtons</span><span> buttons </span><span>=</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Yes</span><span> </span><span>|</span><span> 
            </span><span>TaskDialogCommonButtons</span><span>.</span><span>No</span><span> </span><span>|</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Cancel</span><span>;</span><span>
        taskDialog</span><span>.</span><span>CommonButtons</span><span> </span><span>=</span><span> buttons</span><span>;</span><span>
        </span><span>TaskDialogResult</span><span> taskDialogResult </span><span>=</span><span> taskDialog</span><span>.</span><span>Show</span><span>();</span><span>

        </span><span>if</span><span> </span><span>(</span><span>taskDialogResult </span><span>==</span><span> </span><span>TaskDialogResult</span><span>.</span><span>Yes</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>taskDialogResult </span><span>==</span><span> </span><span>TaskDialogResult</span><span>.</span><span>No</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedElementIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedElementIds</span><span>)</span><span>
            </span><span>{</span><span>
                elements</span><span>.</span><span>Insert</span><span>(</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>);</span><span>
            </span><span>}</span><span>
            message </span><span>=</span><span> </span><span>"Failed to delete selection."</span><span>;</span><span>
            </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Cancelled</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>catch</span><span>
    </span><span>{</span><span>
        message </span><span>=</span><span> </span><span>"Unexpected Exception thrown."</span><span>;</span><span>
        </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
    </span><span>}</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>

### IExternalCommandAvailability

This interface allows you control over whether or not an external command button may be pressed. The IsCommandAvailable interface method passes the application and a set of categories matching the categories of selected items in Revit to your implementation. The typical use would be to check the selected categories to see if they meet the criteria for your command to be run.

In this example the accessibility check allows a button to be clicked when there is no active selection, or when at least one wall is selected:

<table summary="" id="GUID-C84BA0A2-2637-46B0-8BA7-3B0A982485A1__TABLE_D83B02D723A945028D1C56CE69868C5D"><tbody><tr><td><b>Code Region 3-5: Setting Command Availability</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>SampleAccessibilityCheck</span><span> </span><span>:</span><span> </span><span>IExternalCommandAvailability</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>bool</span><span> </span><span>IsCommandAvailable</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>UIApplication</span><span> applicationData</span><span>,</span><span>
                </span><span>CategorySet</span><span> selectedCategories</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Allow button click if there is no active selection</span><span>
                </span><span>if</span><span> </span><span>(</span><span>selectedCategories</span><span>.</span><span>IsEmpty</span><span>)</span><span>
                        </span><span>return</span><span> </span><span>true</span><span>;</span><span>
                </span><span>// Allow button click if there is at least one wall selected</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>Category</span><span> c </span><span>in</span><span> selectedCategories</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>c</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span> </span><span>==</span><span> </span><span>(</span><span>int</span><span>)</span><span>BuiltInCategory</span><span>.</span><span>OST_Walls</span><span>)</span><span>
                        </span><span>return</span><span> </span><span>true</span><span>;</span><span>
                </span><span>}</span><span>
                </span><span>return</span><span> </span><span>false</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  External Commands  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Add-In Integration  Autodesk.md ===== -->

---
created: 2026-01-28T20:36:26 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Add-In Integration | Autodesk

> ## Excerpt
> Developers add functionality by creating and implementing External Commands and External Applications. Revit identifies the new commands and applications using .addin manifest files.

---
Developers add functionality by creating and implementing External Commands and External Applications. Revit identifies the new commands and applications using .addin manifest files.

-   External Commands appear under the External Tools menu-button on the Add-Ins tab.
-   External Applications are invoked when Revit starts up and unloaded when Revit shuts down

This chapter focuses on the following:

-   Learning how to add functionality using External Commands and External Applications.
-   How to access Revit events.
-   How to customize the Revit UI.


<!-- ===== END: Help  Add-In Integration  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Overview  Autodesk.md ===== -->

---
created: 2026-01-28T20:36:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Overview | Autodesk

> ## Excerpt
> The Revit Platform API is based on Revit application functionality. The Revit Platform API is composed of two class Libraries that only work when Revit is running.

---
The Revit Platform API is based on Revit application functionality. The Revit Platform API is composed of two class Libraries that only work when Revit is running.

The RevitAPI.dll contains methods used to access Revit's application, documents, elements, and parameters at the database level. It also contains IExternalDBApplication and related interfaces.

The RevitAPIUI.dll contains all API interfaces related to manipulation and customization of the Revit user interface, including:

-   IExternalCommand and External Command related interfaces
-   IExternalApplication and related interfaces
-   Selection
-   RibbonPanel, RibbonItem and subclasses
-   TaskDialogs

As the following picture shows, Revit Architecture, Revit Structure, and Revit MEP are specific to Architecture, Structure, and MEP respectively.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-EADE225A-E8F2-4EB8-BB94-00CA8759C1E9-low.png)**Figure 11: Revit, RevitAPI and Add-ins**

To create a RevitAPI based add-in, you must provide specific entrypoint types in your add-in DLL. These entrypoint classes implement interfaces, either IExternalCommand, IExternalApplication, or IExternalDBApplication. In this way, the add-in is run automatically on certain events or, in the case of IExternalCommand and IExternalApplication, manually from the External Tools menu-button.

IExternalCommand, IExternalApplication, IExternalDBApplication, and other available Revit events for add-in integration are introduced in this chapter.


<!-- ===== END: Help  Overview  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  External Application  Autodesk.md ===== -->

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


<!-- ===== END: Help  External Application  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Add-in Registration  Autodesk.md ===== -->

---
created: 2026-01-28T20:36:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Add-in Registration | Autodesk

> ## Excerpt
> External commands and external applications need to be registered in order to appear inside Revit. They can be registered by adding them to a .addin manifest file.

---
External commands and external applications need to be registered in order to appear inside Revit. They can be registered by adding them to a .addin manifest file.

The order that external commands and applications are listed in Revit is determined by the order in which they are read in when Revit starts up.

## Manifest Files

Revit API applications are registered with Revit via a .addin manifest file. Manifest files are read automatically by Revit when they are placed in one of two locations on a user's system:

In a non-user-specific location in "application data":

-   C:\\ProgramData\\Autodesk\\Revit\\Addins\\Revit 2018\\

In a user-specific location in "application data":

-   C:\\Users<user>\\AppData\\Roaming\\Autodesk\\Revit\\Addins\\Revit 2018\\

All files named .addin in these locations will be read and processed by Revit during startup. All of the files in both the user-specific location and the all users location are considered together and loaded in alphabetical order. If an all users manifest file shares the same name with a user-specific manifest file, the all users manifest file is ignored. Within each manifest file, the external commands and external applications are loaded in the order in which they are listed.

A basic file adding one ExternalCommand looks like this:

**Code Region 3-9: Manifest .addin ExternalCommand**

```
<?xml version="1.0" encoding="utf-8" standalone="no"?>
<RevitAddIns>
        <AddIn Type="Command">
                <Assembly>c:\MyProgram\MyProgram.dll</Assembly>
                <AddInId>76eb700a-2c85-4888-a78d-31429ecae9ed</AddInId>
                <FullClassName>Revit.Samples.SampleCommand</FullClassName>
                <Text>Sample command</Text>
                <VendorId>ADSK</VendorId>
                <VendorDescription>Autodesk, www.autodesk.com</VendorDescription> 
                <VisibilityMode>NotVisibleInFamily</VisibilityMode>
                <Discipline>Structure</Discipline>
                <Discipline>Architecture</Discipline>
                <AvailabilityClassName>Revit.Samples.SampleAccessibilityCheck</AvailabilityClassName>
                <LongDescription>
                        This is the long description for my command.
                        This is another descriptive paragraph, with notes about how to use the command properly.
                </LongDescription>
                <TooltipImage>c:\MyProgram\Autodesk.png</TooltipImage>
                <LargeImage>c:\MyProgram\MyProgramIcon.png</LargeImage>
        </AddIn>
</RevitAddIns>
```

A basic file adding one ExternalApplication looks like this:

**Code Region 3-10: Manifest .addin ExternalApplication**

```
<?xml version="1.0" encoding="utf-8" standalone="no"?>
<RevitAddIns>
<AddIn Type="Application">
                <Name>SampleApplication</Name>
                <Assembly>c:\MyProgram\MyProgram.dll</Assembly>
                <AddInId>604B1052-F742-4951-8576-C261D1993107</AddInId>
                <FullClassName>Revit.Samples.SampleApplication</FullClassName>
                <VendorId>ADSK</VendorId>
                <VendorDescription>Autodesk, www.autodesk.com</VendorDescription>
</AddIn>
</RevitAddIns>
```

A basic file adding one DB-level External Application looks like this:

**Code Region: Manifest .addin ExternalDBApplication**

```
<?xml version="1.0" encoding="utf-8" standalone="no"?>
<RevitAddIns>
<AddIn Type="DBApplication">
                <Assembly>c:\MyDBLevelApplication\MyDBLevelApplication.dll</Assembly>
                <AddInId>DA3D570A-1AB3-4a4b-B09F-8C15DFEC6BF0</AddInId>

                <FullClassName>MyCompany.MyDBLevelAddIn</FullClassName>

                <Name>My DB-Level AddIn</Name>                    
                <VendorId>ADSK</VendorId>
                <VendorDescription>Autodesk, www.autodesk.com</VendorDescription>
</AddIn>
</RevitAddIns>
```

Multiple AddIn elements may be provided in a single manifest file.

The following table describes the available XML tags:

<table summary="" id="GUID-4FFDB03E-6936-417C-9772-8FC258A261F7__TABLE_8E7A8ACAD3C5487CA4A1E985DF05CA47"><tbody><tr><td><b>Tag</b></td><td><b>Description</b></td></tr><tr><td>Assembly</td><td>The full path to the add-in assembly file. Required for all ExternalCommands and ExternalApplications.</td></tr><tr><td>FullClassName</td><td>The full name of the class in the assembly file which implements IExternalCommand or IExternalApplication. Required for all ExternalCommands and ExternalApplications.</td></tr><tr><td>AddInId</td><td>A GUID which represents the id of this particular application. AddInIds must be unique for a given session of Revit.<p>Autodesk recommends you generate a unique GUID for each registered application or command. Required for all ExternalCommands and ExternalApplications.</p></td></tr><tr><td>Name</td><td>The name of application. Required; for ExternalApplications only.</td></tr><tr><td>Text</td><td>The name of the button. Optional; use this tag for ExternalCommands only. The default is "External Tool".</td></tr><tr><td>VendorId</td><td>A unique vendor identifier that may be used by some operations in Revit (such as identification of extensible storage). This must be unique, and thus we recommend to use reversed version of your domain name, for example, com.autodesk or uk.co.autodesk.</td></tr><tr><td>VendorDescription</td><td>Description containing vendor's legal name and/or other pertinent information. Optional.</td></tr><tr><td>Description</td><td>Short description of the command, will be used as the button tooltip. Optional; use this tag for ExternalCommands only.<p>The default is a tooltip with just the command text.</p></td></tr><tr><td>VisibilityMode</td><td>The modes in which the external command will be visible. Multiple values may be set for this option. Optional; use this tag for ExternalCommands only.<p>The default is to display the command in all modes, including when there is no active document. Previously written external commands which need to run against the active document should either be modified to ensure that the code deals with invocation of the command when there is no active document, or apply the NotVisibleWhenNoActiveDocument mode. See table below for more information.</p></td></tr><tr><td>Discipline</td><td>The disciplines in which the external command will be visible. Multiple values may be set for this option. Optional; use this tag for ExternalCommands only.<p>The default is to display the command in all disciplines. If any specific disciplines are listed, the command will only be visible in those disciplines. See table below for more information.</p></td></tr><tr><td>AvailabilityClassName</td><td>The full name of the class in the assembly file which implemented IExternalCommandAvailability. This class allows the command button to be selectively grayed out depending on context. Optional; use this tag for ExternalCommands only.<p>The default is a command that is available whenever it is visible.</p></td></tr><tr><td>LargeImage</td><td>The icon to use for the button in the External Tools pulldown menu. Optional; use this tag for ExternalCommands only.<p>The default is to show a button without an icon.</p></td></tr><tr><td>SmallImage</td><td>The icon to use if the button is promoted to the Quick Access Toolbar. Optional; use this tag for ExternalCommands only.<p>The default is to show a Quick Access Toolbar button without an icon, which can be confusing to users.</p></td></tr><tr><td>LongDescription</td><td>Long description of the command, will be used as part of the button extended tooltip, shown when the mouse hovers over the command for a longer amount of time. Optional; use this tag for ExternalCommands only. If this property and TooltipImage are not supplied, the button will not have an extended tooltip.</td></tr><tr><td>TooltipImage</td><td>An image file to show as a part of the button extended tooltip, shown when the mouse hovers over the command for a longer amount of time. Optional; use this tag for ExternalCommands only. If this property and TooltipImage are not supplied, the button will not have an extended tooltip.</td></tr><tr><td>LanguageType</td><td>Localization setting for Text, Description, LargeImage, LongDescription, and TooltipImage of external tools buttons. Revit will load the resource values from the specified language resource dll. The value can be one of the eleven languages supported by Revit. If no LanguageType is specified, the language resource which the current session of Revit is using will be automatically loaded. For more details see the section on Localization.</td></tr><tr><td>AllowLoadIntoExistingSession</td><td>The flag for loading permission. Set to false to prevent Revit from automatically loading addins in a newly added .addin manifest file without restarting. Optional. By default. Revit will automatically load addins from newly added .addin manifest files without restarting Revit.</td></tr></tbody></table>

\*\*Table 3: VisibilityMode Members\*\*

<table summary="" id="GUID-4FFDB03E-6936-417C-9772-8FC258A261F7__TABLE_531B8743F3B5484A9E1F35FEA9630769"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td>AlwaysVisible</td><td>The command is available in all possible modes supported by the Revit API.</td></tr><tr><td>NotVisibleInProject</td><td>The command is invisible when there is a project document active.</td></tr><tr><td>NotVisibleInFamily</td><td>The command is invisible when there is a family document active.</td></tr><tr><td>NotVisibleWhenNoActiveDocument</td><td>The command is invisible when there is no active document.</td></tr></tbody></table>

\*\*Table 4: Discipline Members\*\*

<table summary="" id="GUID-4FFDB03E-6936-417C-9772-8FC258A261F7__TABLE_D0B11ECA4EE848D58871A442BD3B4A5C"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td>Any</td><td>The command is available in all possible disciplines supported by the Revit API.</td></tr><tr><td>Architecture</td><td>The command is visible in Autodesk Revit Architecture.</td></tr><tr><td>Structure</td><td>The command is visible in Autodesk Revit Structure.</td></tr><tr><td>StructuralAnalysis</td><td>The command is visible when the Structural Analysis discipline editing tools are available.</td></tr><tr><td>MassingAndSite</td><td>The command is visible when the Massing and Site discipline editing tools are available.</td></tr><tr><td>EnergyAnalysis</td><td>The command is visible when Energy Analysis discipline editing tools are available.</td></tr><tr><td>Mechanical</td><td>The command is visible when the Mechanical discipline editing tools are available, e.g. in Autodesk Revit MEP.</td></tr><tr><td>Electrical</td><td>The command is visible when the Electrical discipline editing tools are available, e.g. in Autodesk Revit MEP.</td></tr><tr><td>Piping</td><td>The command is visible when the Piping discipline editing tools are available, e.g. in Autodesk Revit MEP.</td></tr><tr><td>MechanicalAnalysis</td><td>The command is visible when the Mechanical Analysis discipline editing tools are available.</td></tr><tr><td>PipingAnalysis</td><td>The command is visible when the Piping Analysis discipline editing tools are available.</td></tr><tr><td>ElectricalAnalysis</td><td>The command is visible when the Electrical Analysis discipline editing tools are available.</td></tr></tbody></table>

## .NET Add-in Utility for manifest files

The .NET utility DLL RevitAddInUtility.dll offers a dedicated API capable of reading, writing and modifying Revit Add-In manifest files. It is intended for use from product installers and scripts. Consult the API documentation in the RevitAddInUtility.chm help file in the SDK installation folder.

<table summary="" id="GUID-4FFDB03E-6936-417C-9772-8FC258A261F7__TABLE_796DAC6A9FB94CC8958CB909E81D9355"><tbody><tr><td><b>Code Region 3-11: Creating and editing a manifest file</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ManifestFile</span><span>()</span><span>
</span><span>{</span><span>
        </span><span>//create a new addin manifest</span><span>
        </span><span>RevitAddInManifest</span><span> </span><span>Manifest</span><span> </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitAddInManifest</span><span>();</span><span>

        </span><span>//create an external command</span><span>
        </span><span>RevitAddInCommand</span><span> command1 </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitAddInCommand</span><span>(</span><span>"full path\\assemblyName.dll"</span><span>,</span><span> 
        </span><span>Guid</span><span>.</span><span>NewGuid</span><span>(),</span><span> </span><span>"namespace.className"</span><span>,</span><span> </span><span>"ADSK"</span><span>);</span><span>
        command1</span><span>.</span><span>Description</span><span> </span><span>=</span><span> </span><span>"description"</span><span>;</span><span>
        command1</span><span>.</span><span>Text</span><span> </span><span>=</span><span> </span><span>"display text"</span><span>;</span><span>

        </span><span>// this command only visible in Revit MEP, Structure, and only visible </span><span>
        </span><span>// in Project document or when no document at all</span><span>
        command1</span><span>.</span><span>Discipline</span><span> </span><span>=</span><span> </span><span>Discipline</span><span>.</span><span>Mechanical</span><span> </span><span>|</span><span> </span><span>Discipline</span><span>.</span><span>Electrical</span><span> </span><span>|</span><span>
                                </span><span>Discipline</span><span>.</span><span>Piping</span><span> </span><span>|</span><span> </span><span>Discipline</span><span>.</span><span>Structure</span><span>;</span><span>
        command1</span><span>.</span><span>VisibilityMode</span><span> </span><span>=</span><span> </span><span>VisibilityMode</span><span>.</span><span>NotVisibleInFamily</span><span>;</span><span>

        </span><span>//create an external application</span><span>
        </span><span>RevitAddInApplication</span><span> application1 </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitAddInApplication</span><span>(</span><span>"appName"</span><span>,</span><span>
        </span><span>"full path\\assemblyName.dll"</span><span>,</span><span> </span><span>Guid</span><span>.</span><span>NewGuid</span><span>(),</span><span> </span><span>"namespace.className"</span><span>,</span><span> </span><span>"ADSK"</span><span>);</span><span>

        </span><span>//add both command(s) and application(s) into manifest</span><span>
        </span><span>Manifest</span><span>.</span><span>AddInCommands</span><span>.</span><span>Add</span><span>(</span><span>command1</span><span>);</span><span>
        </span><span>Manifest</span><span>.</span><span>AddInApplications</span><span>.</span><span>Add</span><span>(</span><span>application1</span><span>);</span><span>

        </span><span>//save manifest to a file</span><span>
        </span><span>RevitProduct</span><span> revitProduct1 </span><span>=</span><span> </span><span>RevitProductUtility</span><span>.</span><span>GetAllInstalledRevitProducts</span><span>()[</span><span>0</span><span>];</span><span>
        </span><span>Manifest</span><span>.</span><span>SaveAs</span><span>(</span><span>revitProduct1</span><span>.</span><span>AllUsersAddInFolder</span><span> </span><span>+</span><span> </span><span>"\\RevitAddInUtilitySample.addin"</span><span>);</span><span>
        </span><span>}</span></code></pre></td></tr></tbody></table>

<table summary="" id="GUID-4FFDB03E-6936-417C-9772-8FC258A261F7__TABLE_A7DA7C3527FB43B8AF8CCF19FAAAB290"><tbody><tr><td><b>Code Region 3-12: Reading an existing manifest file</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ReadManifest</span><span>()</span><span>
</span><span>{</span><span>
        </span><span>RevitProduct</span><span> revitProduct1 </span><span>=</span><span> </span><span>RevitProductUtility</span><span>.</span><span>GetAllInstalledRevitProducts</span><span>()[</span><span>0</span><span>];</span><span>

        </span><span>RevitAddInManifest</span><span> revitAddInManifest </span><span>=</span><span> 
     </span><span>Autodesk</span><span>.</span><span>RevitAddIns</span><span>.</span><span>AddInManifestUtility</span><span>.</span><span>GetRevitAddInManifest</span><span>(</span><span>
          revitProduct1</span><span>.</span><span>AllUsersAddInFolder</span><span> </span><span>+</span><span> </span><span>"\\RevitAddInUtilitySample.addin"</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Access to add-in data paths

Autodesk.Revit.ApplicationServices.Application.CurrentUsersAddinsDataFolderPath provides access to add-in data folder for the current Revit version and current user (such as %appdata%\\Autodesk\\Revit\\Autodesk Revit 2019\\AddinsData)


<!-- ===== END: Help  Add-in Registration  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Digitally Signing Your Revit Add-in  Autodesk.md ===== -->

---
created: 2026-01-28T20:37:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Digitally Signing Your Revit Add-in | Autodesk

> ## Excerpt
> Revit checks security credentials of add-ins.

---
Revit checks security credentials of add-ins.

If an add-in is not digitally signed with a certificate issued by a trusted certificate authority, Revit pops up a dialog when opening asking the user to confirm if he/she wants to load the application. The figure below shows an example of the security warning dialog when an unsigned add-in is detected. The user is presented with choices of: 1) allowing the same add-in to always load from now on, 2) load only this time and ask again next time, and 3) do not allow to load the add-in.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/UnsignedAddIn.png)

If you are professional developer and your application is already digitally signed by a trusted certificate authority, your add-in is already compatible with the digital signature checking in Revit. The following sections are intended for developers who author add-ins, but who are not familiar with digital signing in Revit.


<!-- ===== END: Help  Digitally Signing Your Revit Add-in  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Digitally Signing Your App  Autodesk.md ===== -->

---
created: 2026-01-28T20:37:43 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Digitally Signing Your App | Autodesk

> ## Excerpt
> If you are publisher of a Revit add-in, you will have to sign your add-in with your own certificate.

---
If you are publisher of a Revit add-in, you will have to sign your add-in with your own certificate.

To sign your add-in with your own certificate, you first need to purchase a digital signature from a digital certificate vendor. Once you obtain a certificate (cer) or Personal Information Exchange (pfx) file, you can sign your DLL(s) using **signtool**.

Alternatively, you can also use an online Authenticode signing service, such as Symantec's Secure App Service - [https://www.symantec.com/code-signing/secure-app-service/](https://www.symantec.com/CODE-SIGNING/SECURE-APP-SERVICE/).

## Digital Certificate Venders

The following is a non-exhaustive list of vendors that provide digital certificates:

-   Symantec - [www.symantec.com](https://www.symantec.com/)
-   DigiCert - [www.digicert.com](https://www.digicert.com/)
-   VERISIGN - [www.verisign.com](https://www.verisign.com/)
-   Thawte - [www.thawte.com](https://www.thawte.com/)

You can use [signtool.exe](https://msdn.microsoft.com/EN-US/LIBRARY/8S9B9YAZ(V=VS.110).ASPX) tool to sign your .NET dll. The tool is automatically installed with Visual Studio. To run the tool, use the Developer Command Prompt. The following is the format of the command line parameters:

### Command Region: Using signtool

```
signtool.exe sign /fd SHA256 /f <.pfx-file-name> /p  <password> <file-to-sign>.dll
```

Where /fd is a flag for the file digest algorithm to use. Here we use SHA256. (SHA stands for Secure Hash Algorithm. The signtool default is SHA1. We recommend SHA256, which is a newer, more secure version.) <.pfx-file-name> is the name of .pfx (Personal Information Exchange) file you obtain from the vendor. `<password>` is the password that you specify when obtaining the pfx file. `<file-to-sign>.dll` is the name of the DLL that you want to sign.

For example, if you run the command in an arbitrary folder, the above command may look like this:

#### Command Region: signtool example

```
"C:\Program Files (x86)\Windows Kits\8.1\bin\x64\signtool" sign /fd SHA256 /f "C:/Dev/MyCert.pfx" /p "password123" “C:/Dev/HelloRevit.dll”
```

Note: The exact location of signtool may differ in your environment.

Once the DLL is signed with an authorized certification, Revit will no longer pop up a security warning dialog upon loading your add-in.

You can also include the command in the Post-Built Event section of Visual Studio for your application project properties.

#### Command Region: Post-Build Event signing

```
"C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\signtool.exe" /fd SHA256 sign /f
"C:\Autodesk\MyCert.pfx" /p MyPassword "$(TargetDir)$(TargetFileName)"
```

It is also worth adding a time stamp while signing (/td and /tr switches in signtool.exe); otherwise the app becomes untrusted when the certificate expires. Adding the time stamp ensures the app is trusted forever as long as it was signed prior to expiration (unless the certificate gets revoked):

#### Command Region: Adding a time stamp

```
signtool.exe timestamp /td sha256 /tr <URL-of-time-stamp-server> <file-to-sign>.dll
```

For example, the following uses the verisign timestamp server:

#### Command Region: Time stamp example

```
signtool.exe timestamp /td sha256 /tr "http://sha256timestamp.ws.symantec.com/sha256/" HelloRevit.dll
```

Note: The /td sha256 and /tr switches used in the example above are used to sign with sha256 timestamp. Beginning January 1, 2017 Microsoft will treat SHA1 timestamps as unsigned. Please refer to [this article](http://support.ksoftware.net/support/solutions/articles/215805-the-truth-about-sha1-sha-256-and-code-signing-certificates-) for more details.


<!-- ===== END: Help  Digitally Signing Your App  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Making Your Own Certificate for Testing and Internal Use  Autodesk.md ===== -->

---
created: 2026-01-28T20:37:52 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Making Your Own Certificate for Testing and Internal Use | Autodesk

> ## Excerpt
> You can make your own digital certificate for testing or using within your company.

---
You can make your own digital certificate for testing or using within your company.

To create your own digital certificate

1.  Create a digital certificate using the [MakeCert.exe](https://msdn.microsoft.com/EN-US/LIBRARY/WINDOWS/DESKTOP/AA386968(V=VS.85).ASPX) tool.
2.  Create a Personal Information Exchange (pfx) file using the Pvk2Pfx.exe tool.
3.  [Digitally Signing Your App](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_Digitally_Signing_Your_Revit_Add_in_Digitally_Signing_Your_App_html).
4.  Import a Digital Certificate to Windows Certificate Store. ([CertMgr.msc or CertUtil.exe](https://msdn.microsoft.com/en-us/library/E78BYTA0(V=VS.110).aspx))

## Create a Digital Certificate

You can use [MakeCert.exe](https://msdn.microsoft.com/EN-US/LIBRARY/WINDOWS/DESKTOP/AA386968(V=VS.85).ASPX) tool to make your own digital certificate for testing and internal use. The following is the command format:

<table summary="" id="GUID-B9A067F4-234F-47F8-A5EE-0D84A93FA98E__TABLE_CB2735141C884AA185BF09B93CDCA5F4"><tbody><tr><td>Command Region: Make a certificate command format</td></tr><tr><td><pre><code><span>MakeCert</span><span>.</span><span>exe </span><span>-</span><span>r </span><span>-</span><span>sv </span><span>&lt;</span><span>name</span><span>-</span><span>of</span><span>-</span><span>private</span><span>-</span><span>key</span><span>-</span><span>file</span><span>&gt;.</span><span>pvk </span><span>-</span><span>n </span><span>"CN=&lt;developer-name&gt;"</span><span> </span><span>&lt;</span><span>name</span><span>-</span><span>of</span><span>-</span><span>certificate</span><span>-</span><span>file</span><span>&gt;.</span><span>cer </span><span>-</span><span>b </span><span>&lt;</span><span>start</span><span>-</span><span>data</span><span>&gt;</span><span> </span><span>-</span><span>e </span><span>&lt;</span><span>end</span><span>-</span><span>date</span><span>&gt;</span></code></pre></td></tr></tbody></table>

Where `<name-of-private-key-file>` is the name of the file where the private key is stored, `<developer- name>` is the name of the developer, `<name-of-certificate-file>` is the name of the certificate file, `<start-date>` is the date when the certificate became valid (format is mm/dd/yyyy), and `<end-date>` is the date when the validity of the certificate ends.

For example:

<table summary="" id="GUID-B9A067F4-234F-47F8-A5EE-0D84A93FA98E__TABLE_5282B69274E4442A800F24DECE780E25"><tbody><tr><td>Command Region: MakeCert.exe example</td></tr><tr><td><pre><code><span>"C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\MakeCert.exe"</span><span> </span><span>-</span><span>r </span><span>-</span><span>sv </span><span>MyCert</span><span>.</span><span>pvk </span><span>-</span><span>n </span><span>"CN=DevABC"</span><span> </span><span>MyCert</span><span>.</span><span>cer </span><span>-</span><span>b </span><span>01</span><span>/</span><span>01</span><span>/</span><span>2016</span><span> </span><span>-</span><span>e </span><span>12</span><span>/</span><span>31</span><span>/</span><span>2016</span></code></pre></td></tr></tbody></table>

Or:

<table summary="" id="GUID-B9A067F4-234F-47F8-A5EE-0D84A93FA98E__TABLE_B60C5B26166F4ED39ABE4C01B9DBEA6C"><tbody><tr><td>Command Region: MakeCert.exe example</td></tr><tr><td><pre><code><span>"C:\Program Files (x86)\Windows Kits\8.1\bin\x64\makecert.exe"</span><span> </span><span>-</span><span>r </span><span>-</span><span>sv </span><span>MyCert</span><span>.</span><span>pvk </span><span>-</span><span>n </span><span>"CN=DevABC"</span><span> </span><span>MyCert</span><span>.</span><span>cer </span><span>-</span><span>b </span><span>01</span><span>/</span><span>01</span><span>/</span><span>2016</span><span> </span><span>-</span><span>e </span><span>12</span><span>/</span><span>31</span><span>/</span><span>2016</span></code></pre></td></tr></tbody></table>

This command will bring up "Create Private Key Password" dialog. Enter the private key password in the dialog. If it asks for password, enter again. When everything is done, you will see a message "Succeeded" in the command window and .cer and .pvk files are created.

## Convert to PFX

The next step is to convert a digital certificate to a Personal Information Exchange (pfx) file using the pvk2pfx.exe tool. In this step, you need the .pvk file, .cer file, and password you created in the above step. The command format looks like this:

<table summary="" id="GUID-B9A067F4-234F-47F8-A5EE-0D84A93FA98E__TABLE_D142C4EBFF7C4DB280ABEF022A5D8986"><tbody><tr><td>Command Region: Convert to PFX command format</td></tr><tr><td><pre><code><span>pvk2pfx</span><span>.</span><span>exe</span><span>" -pvk &lt;name-of-private-key-file&gt;.pvk -pi &lt;password-for-pvk&gt; -spc &lt;name-of-certification-file-name&gt;.cer 
-pfx &lt;name-of-pfx-file&gt; -po &lt;password-for-pfx&gt;</span></code></pre></td></tr></tbody></table>

Where `<name-of-private-key-file>` is the name of pvk file you created, `<password-for-pvk>` is the password you assigned to the pvk file. `<name-of-certification-file-name>` is the name of the certification file or .cer file. `<name-of-pfx-file>` is the name of the .pfx. `<password-for-pfx>` is a password to be assigned to the .pfx file.

For example:

<table summary="" id="GUID-B9A067F4-234F-47F8-A5EE-0D84A93FA98E__TABLE_27049496D3F04BC2A51BB0056D3E7727"><tbody><tr><td>Command Region: Convert to PFX example</td></tr><tr><td><pre><code><span>"C:\Program Files (x86)\Windows Kits\8.1\bin\x64\pvk2pfx.exe"</span><span> </span><span>-</span><span>pvk </span><span>MyCert</span><span>.</span><span>pvk </span><span>-</span><span>pi password123 </span><span>-</span><span>spc </span><span>MyCert</span><span>.</span><span>cer </span><span>-</span><span>pfx </span><span>MyCert</span><span>.</span><span>pfx </span><span>-</span><span>po password234</span></code></pre></td></tr></tbody></table>

When the operation succeeds, the command ends without error message and a .pfx file will be created.

Once you have a pfx file, you can [Digitally Signing Your App](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_Digitally_Signing_Your_Revit_Add_in_Digitally_Signing_Your_App_html).

## Import the Digital Certificate to Windows Certificate Store

One more step you need when you are making your own digital certificate is to import it to your computer. You can do this in Certificate Manager ([CertMgr.msc](https://msdn.microsoft.com/EN-US/LIBRARY/E78BYTA0(V=VS.110).ASPX)) or CertUtils.exe tool. Here we use the UI tool. Please refer [here for alternatives](http://help.autodesk.com/view/ACD/2018/ENU/?guid=GUID-19D6716A-0AD1-4A7A-82BA-A067E6D65F66).

1.  From Start >> Run >> CertMgr.msc. (Or on Windows 8.1/10, right click on Start >> Run >> CertMgr.msc) CertMgr opens.
2.  On CertMgr dialog, right click on **Trusted Publishers** >> All Tasks >> Import …
3.  Follow the instructions on Certificate Import Wizard. Click Next.
4.  On a dialog which asks "Files to Import", choose the pfx file you want to import.
5.  On the "Password" dialog, enter the password. Keep "Include all extended properties" checked.
6.  Choose "Place all certificates in the following store" then Click Next.
7.  Confirm and Finish.
8.  If you see "Import a new Private signature key" dialog, click OK. (This part may differ depending on your environment.) ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/certmgr.png)
9.  Repeat the same step with **Trusted Root Certification Authorities**. This step is to validate digitally signed binary files.


<!-- ===== END: Help  Making Your Own Certificate for Testing and Internal Use  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Digital Signature References  Autodesk.md ===== -->

---
created: 2026-01-28T20:37:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Digital Signature References | Autodesk

> ## Excerpt
> 

---
### Was this information helpful?

-   Yes
-   No


<!-- ===== END: Help  Digital Signature References  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Localization  Autodesk.md ===== -->

---
created: 2026-01-28T20:38:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Localization | Autodesk

> ## Excerpt
> You can let Revit localize the user-visible resources of an external command button (including Text, large icon image, long and short descriptions and tooltip image). You will need to create a .NET Satellite DLL which contains the strings, images, and icons for the button. Then change the values of the tags in the .addin file to correspond to the names of resources in the Satellite dll, but prepended with the @character. So the tag:

---
You can let Revit localize the user-visible resources of an external command button (including Text, large icon image, long and short descriptions and tooltip image). You will need to create a .NET Satellite DLL which contains the strings, images, and icons for the button. Then change the values of the tags in the .addin file to correspond to the names of resources in the Satellite dll, but prepended with the @character. So the tag:

<table summary="" id="GUID-74C35C7C-22E8-4F7F-844F-E602EF45CFA2__TABLE_A672A867F2EC487D938423194AB939BC"><tbody><tr><td><b>Code Region 3-13: Non-localized Text Entry</b></td></tr><tr><td><p><code>&lt;Text&gt;Extension Manager&lt;/Text&gt;</code></p></td></tr></tbody></table>

Becomes:

<table summary="" id="GUID-74C35C7C-22E8-4F7F-844F-E602EF45CFA2__TABLE_5A9C1C832A7145C580EA9EF5E4801E3F"><tbody><tr><td><b>Code Region 3-14: Localized Text Entry</b></td></tr><tr><td><p><code>&lt;Text&gt;@ExtensionText&lt;/Text&gt;</code></p></td></tr></tbody></table>

where ExtensionText is the name of the resource found in the Satellite DLL.

The Satellite DLLs are expected to be in a directory with the name of the language of the language-culture, such as en or en-US. The directory should be located in the directory that contains the add-in assembly. See [http://msdn.microsoft.com/en-us/library/e9zazcx5.aspx](http://msdn.microsoft.com/en-us/library/e9zazcx5.aspx) to create managed Satellite DLLs.

You can force Revit to use a particular language resource DLL, regardless of the language of the Revit session, by specifying the language and culture explicitly with a LanguageType tag.

<table summary="" id="GUID-74C35C7C-22E8-4F7F-844F-E602EF45CFA2__TABLE_23FF102C3FC84D028B44DAB25A7453EF"><tbody><tr><td><b>Code Region 3-15: Using LanguageType Tag</b></td></tr><tr><td><p><code>&lt;LanguageType&gt;English_USA&lt;/LanguageType&gt;</code></p></td></tr></tbody></table>

For example, the entry above would force Revit to always load the values from the en-US Satellite DLL and to ignore the current Revit language and culture settings when considering the localizable members of the external command manifest file.

Revit supports the 11 languages defined in the Autodesk.Revit.ApplicationServices.LanguageType enumerated type: English\_USA, German, Spanish, French, Italian, Dutch, Chinese\_Simplified, Chinese\_Traditional, Japanese, Korean, and Russian.


<!-- ===== END: Help  Localization  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Attributes  Autodesk.md ===== -->

---
created: 2026-01-28T20:40:16 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Attributes | Autodesk

> ## Excerpt
> The Revit API provides several attributes for configuring ExternalCommand and ExternalApplication behavior.

---
The Revit API provides several attributes for configuring ExternalCommand and ExternalApplication behavior.

### TransactionAttribute

The custom attribute Autodesk.Revit.Attributes.TransactionMode must be applied to your implementation class of the IExternalCommand interface to control transaction behavior for the external command. There is no default for this option. This mode controls how the API framework expects transactions to be used when the command is invoked. The supported values are:

-   _TransactionMode.Manual_ - Revit will not create a transaction (but it will create an outer transaction group to roll back all changes if the external command returns a failure). Instead, you may use combinations of Transactions, SubTransactions, and TransactionGroups as you please. You will have to follow all rules regarding use of transactions and related classes. You will have to give your transactions names which will then appear in the Undo menu. Revit will check that all transactions (also groups and sub-transactions) are properly closed upon return from an external command. If not, Revit will discard all changes made to the model.
-   _TransactionMode.ReadOnly_ - No transaction (nor group) will be created, and no transaction may be created for the lifetime of the command. The External Command may only use methods that read from the model. Exceptions will be thrown if the command either tries to start a transaction (or group) or attempts to write to the model.

In either mode, the TransactionMode applies only to the active document. You may open other documents during the course of the command, and you may have complete control over the creation and use of Transactions, SubTransactions, and TransactionGroups on those other documents (even in ReadOnly mode).

For example, to set an external command to use manual transaction mode:

<table summary="" id="GUID-D1F0F04D-B4EA-49FA-806E-84153C507D7F__TABLE_65884741F68E479C9B980EB3AAE52155"><tbody><tr><td><b>Code Region 3-18: TransactionAttribute</b></td></tr><tr><td><pre><code><span>[</span><span>Transaction</span><span>(</span><span>TransactionMode</span><span>.</span><span>Manual</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>CommandTransaction</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>
                </span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span>
                </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementSet</span><span> elements</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Command implementation, which modifies the active document directly </span><span>
                </span><span>// after starting a new transaction</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

See [Transactions](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_html).

### JournalingAttribute

The custom attribute Autodesk.Revit.Attributes.JournalingAttribute can optionally be applied to your implementation class of the IExternalCommand interface to control the journaling behavior during the external command execution. There are two options for journaling:

-   _JournalMode.NoCommandData_ - Contents of the ExternalCommandData.JournalData map are not written to the Revit journal. This option allows Revit API calls to write to the journal as needed. This option allows commands which invoke the Revit UI for selection or responses to task dialogs to replay correctly.
-   _JournalMode.UsingCommandData_ - Uses the IDictionary<String, String> supplied in the command data. This will hide all Revit journal entries between the external command invocation and the IDictionary<String, String< entry. Commands which invoke the Revit UI for selection or responses to task dialogs may not replay correctly. This is the default if the JournalingAttribute is not specified.

<table summary="" id="GUID-D1F0F04D-B4EA-49FA-806E-84153C507D7F__TABLE_3E4CD54AC560492CB105A4375171A8A6"><tbody><tr><td><b>Code Region 3-19: JournalingAttribute</b></td></tr><tr><td><pre><code><span>[</span><span>Journaling</span><span>(</span><span>JournalingMode</span><span>.</span><span>UsingCommandData</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>CommandJournal</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>
                </span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> 
                </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementSet</span><span> elements</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Attributes  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Revit Exceptions  Autodesk.md ===== -->

---
created: 2026-01-28T20:40:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Revit Exceptions | Autodesk

> ## Excerpt
> When API methods encounter a non-fatal error, they throw an exception. Exceptions should be caught by Revit add-ins. The Revit API help file specifies exceptions that are typically encountered for specific methods. All Revit API methods throw a subclass of Autodesk.Revit.Exceptions.ApplicationException. These exceptions closely mirror standard .NET exceptions such as:

---
When API methods encounter a non-fatal error, they throw an exception. Exceptions should be caught by Revit add-ins. The Revit API help file specifies exceptions that are typically encountered for specific methods. All Revit API methods throw a subclass of Autodesk.Revit.Exceptions.ApplicationException. These exceptions closely mirror standard .NET exceptions such as:

-   ArgumentException
-   InvalidOperationException
-   FileNotFoundException

However, some of these subclasses are unique to Revit:

-   AutoJoinFailedException
-   RegenerationFailedException
-   ModificationOutsideTransactionException

In addition, there is a special exception type called InternalException, which represents a failure path which was not anticipated. Exceptions of this type carry extra diagnostic information which can be passed back to Autodesk for diagnosis.


<!-- ===== END: Help  Revit Exceptions  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Ribbon Panels and Controls  Autodesk.md ===== -->

---
created: 2026-01-28T20:40:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Ribbon Panels and Controls | Autodesk

> ## Excerpt
> Revit provides API solutions to integrate custom ribbon panels and controls.

---
Revit provides API solutions to integrate custom ribbon panels and controls.

These APIs are used with IExternalApplication. Custom ribbon panels can be added to the Add-Ins tab, the Analyze tab or to a new custom ribbon tab.

Panels can include buttons, both large and small, which can be either simple push buttons, pulldown buttons containing multiple commands, or split buttons which are pulldown buttons with a default push button attached. In addition to buttons, panels can include radio groups, combo boxes and text boxes. Panels can also include vertical separators to help separate commands into logical groups. Finally, panels can include a slide out control accessed by clicking on the bottom of the panel.

Please see [Ribbon Guidelines](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_API_User_Interface_Guidelines_Ribbon_Guidelines_html) in the [API User Interface Guidelines](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_API_User_Interface_Guidelines_html) section for information on developing a user interface that is compliant with the standards used by Autodesk.

### Create a New Ribbon Tab

Although ribbon panels can be added to the Add-Ins or Analyze tab, they can also be added to a new custom ribbon tab. This option should only be used if necessary. To ensure that the standard Revit ribbon tabs remain visible, a limit of 20 custom ribbon tabs is imposed. The following image shows a new ribbon tab with one ribbon panel and a few simple controls.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/NewRibbonTab.jpg)Below is the code that generated the above ribbon tab.

<table summary="" id="GUID-1547E521-59BD-4819-A989-F5A238B9F2B3__TABLE_2A93F1DD1B5E4ECBA7F101677061B9BD"><tbody><tr><td><b>Code Region: New Ribbon tab</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create a custom ribbon tab</span><span>
    </span><span>String</span><span> tabName </span><span>=</span><span> </span><span>"This Tab Name"</span><span>;</span><span>
    application</span><span>.</span><span>CreateRibbonTab</span><span>(</span><span>tabName</span><span>);</span><span>

    </span><span>// Create two push buttons</span><span>
    </span><span>PushButtonData</span><span> button1 </span><span>=</span><span> </span><span>new</span><span> </span><span>PushButtonData</span><span>(</span><span>"Button1"</span><span>,</span><span> </span><span>"My Button #1"</span><span>,</span><span>
        </span><span>@</span><span>"C:\ExternalCommands.dll"</span><span>,</span><span> </span><span>"Revit.Test.Command1"</span><span>);</span><span>
    </span><span>PushButtonData</span><span> button2 </span><span>=</span><span> </span><span>new</span><span> </span><span>PushButtonData</span><span>(</span><span>"Button2"</span><span>,</span><span> </span><span>"My Button #2"</span><span>,</span><span>
        </span><span>@</span><span>"C:\ExternalCommands.dll"</span><span>,</span><span> </span><span>"Revit.Test.Command2"</span><span>);</span><span>

    </span><span>// Create a ribbon panel</span><span>
    </span><span>RibbonPanel</span><span> m_projectPanel </span><span>=</span><span> application</span><span>.</span><span>CreateRibbonPanel</span><span>(</span><span>tabName</span><span>,</span><span> </span><span>"This Panel Name"</span><span>);</span><span> 

    </span><span>// Add the buttons to the panel</span><span>
    </span><span>List</span><span>&lt;</span><span>RibbonItem</span><span>&gt;</span><span> projectButtons </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>RibbonItem</span><span>&gt;();</span><span>
    projectButtons</span><span>.</span><span>AddRange</span><span>(</span><span>m_projectPanel</span><span>.</span><span>AddStackedItems</span><span>(</span><span>button1</span><span>,</span><span> button2</span><span>));</span><span>

    </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Create a New Ribbon Panel and Controls

The following image shows a ribbon panel on the Add-Ins tab using various ribbon panel controls. The following sections describe these controls in more detail and provide code samples for creating each portion of the ribbon.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-EC547A32-2941-4731-A9C9-135CEDAB4DF0-low.png)**Figure 14: New ribbon panel and controls**

The following code outlines the steps taken to create the ribbon panel pictured above. Each of the functions called in this sample is provided in subsequent samples later in this section. Those samples assume that there is an assembly located at D:\\ Sample\\HelloWorld\\bin\\Debug\\Hello.dll which contains the External Command Types:

-   Hello.HelloButton
-   Hello.HelloOne
-   Hello.HelloTwo
-   Hello.HelloThree
-   Hello.HelloA
-   Hello.HelloB
-   Hello.HelloC
-   Hello.HelloRed
-   Hello.HelloBlue
-   Hello.HelloGreen

<table summary="" id="GUID-1547E521-59BD-4819-A989-F5A238B9F2B3__TABLE_AD3E04D7261849E1A8D50CCFDFB1DFA3"><tbody><tr><td><b>Code Region: Ribbon panel and controls</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>UIControlledApplication</span><span> app</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>RibbonPanel</span><span> panel </span><span>=</span><span> app</span><span>.</span><span>CreateRibbonPanel</span><span>(</span><span>"New Ribbon Panel"</span><span>);</span><span>

        </span><span>AddRadioGroup</span><span>(</span><span>panel</span><span>);</span><span>
        panel</span><span>.</span><span>AddSeparator</span><span>();</span><span>
        </span><span>AddPushButtonWithContextualHelp</span><span>(</span><span>panel</span><span>);</span><span>
        </span><span>AddSplitButton</span><span>(</span><span>panel</span><span>);</span><span>
        </span><span>AddStackedButtons</span><span>(</span><span>panel</span><span>);</span><span>
        </span><span>AddSlideOut</span><span>(</span><span>panel</span><span>);</span><span>

        </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Ribbon Panel

Custom ribbon panels can be added to the Add-Ins tab (the default) or the Analyze tab, or they can be added to a new custom ribbon tab. There are various types of ribbon controls that can be added to ribbon panels which are discussed in more detail in the next section. All ribbon controls have some common properties and functionality.

#### Ribbon Control Classes

Each ribbon control has two classes associated with it - one derived from RibbonItemData that is used to create the control (i.e. SplitButtonData) and add it to a ribbon panel and one derived from RibbonItem (i.e. SplitButton) which represents the item after it is added to a panel. The properties available from RibbonItemData (and the derived classes) are also available from RibbonItem (and the corresponding derived classes). These properties can be set prior to adding the control to the panel or can be set using the RibbonItem class after it has been added to the panel.

#### Tooltips

Most controls can have a tooltip set (using the ToolTip property) which is displayed when the user moves the mouse over the control. When the user hovers the mouse over a control for an extended period of time, an extended tooltip will be displayed using the LongDescription and the ToolTipImage properties. If neither LongDescription nor ToolTipImage are set, the extended tooltip is not displayed. If no ToolTip is provided, then the text of the control (RibbonItem.ItemText) is displayed when the mouse moves over the control.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-261A8653-F926-4D87-8352-E86BF03EC3D0-low.png)**Figure 15: Extended Tooltip**

#### Contextual Help

Controls can have contextual help associated with them. When the user hovers the mouse over the control and hits F1, the contextual help is triggered. Contextual help options include linking to an external URL, launching a locally installed help (chm) file, or linking to a topic on the Autodesk help wiki. The ContextualHelp class is used to create a type of contextual help, and then RibbonItem.SetContextualHelp() (or RibbonItemData.SetContextualHelp()) associates it with a control. When a ContextualHelp instance is associated with a control, the text "Press F1 for more help" will appear below the tooltip when the mouse hovers over the control, as shown below.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ContextualHelp.jpg)The following example associates a new ContextualHelp with a push button control. Pressing F1 when hovered over the push button will open the Autodesk homepage in a new browser window.

<table summary="" id="GUID-1547E521-59BD-4819-A989-F5A238B9F2B3__TABLE_D667AA7C317542478AAE227FFD5B2BB3"><tbody><tr><td><b>Code Region: Contextual Help</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>AddPushButtonWithContextualHelp</span><span>(</span><span>RibbonPanel</span><span> panel</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>PushButton</span><span> pushButton </span><span>=</span><span> panel</span><span>.</span><span>AddItem</span><span>(</span><span>new</span><span> </span><span>PushButtonData</span><span>(</span><span>"HelloWorld"</span><span>,</span><span>
        </span><span>"HelloWorld"</span><span>,</span><span> </span><span>@</span><span>"D:\Sample\HelloWorld\bin\Debug\HelloWorld.dll"</span><span>,</span><span> </span><span>"HelloWorld.CsHelloWorld"</span><span>))</span><span> </span><span>as</span><span> </span><span>PushButton</span><span>;</span><span>

    </span><span>// Set ToolTip and contextual help</span><span>
    pushButton</span><span>.</span><span>ToolTip</span><span> </span><span>=</span><span> </span><span>"Say Hello World"</span><span>;</span><span>
    </span><span>ContextualHelp</span><span> contextHelp </span><span>=</span><span> </span><span>new</span><span> </span><span>ContextualHelp</span><span>(</span><span>ContextualHelpType</span><span>.</span><span>Url</span><span>,</span><span>
        </span><span>"http://www.autodesk.com"</span><span>);</span><span>
    pushButton</span><span>.</span><span>SetContextualHelp</span><span>(</span><span>contextHelp</span><span>);</span><span>

    </span><span>// Set the large image shown on button</span><span>
    pushButton</span><span>.</span><span>LargeImage</span><span> </span><span>=</span><span>
        </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\39-Globe_32x32.png"</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The ContextualHelp class has a Launch() method that can be called to display the help topic specified by the contents of this ContextualHelp object at any time, the same as when the F1 key is pressed when the control is active. This allows the association of help topics with user interface components inside dialogs created by an add-in application.

#### Associating images with controls

All of these controls can have an image associated with them using the LargeImage property. The best size for images associated with large controls, such as non-stacked ribbon and drop-down buttons, is 32×32 pixels, but larger images will be adjusted to fit the button. Stacked buttons and small controls such as text boxes and combo boxes should have a 16×16 pixel image set. Large buttons should also have a 16×16 pixel image set for the Image property. This image is used if the command is moved to the Quick Access Toolbar. If the Image property is not set, no image will be displayed if the command is moved to the Quick Access Toolbar. Note that if an image larger than 16×16 pixels is used, it will NOT be adjusted to fit the toolbar.

The ToolTipImage will be displayed below the LongDescription in the extended tooltip, if provided. There is no recommended size for this image.

#### Ribbon control availability

Ribbon controls can be enabled or disabled with the RibbonItem.Enabled property or made visible or invisible with the RibbonItem.Visible property.

### Ribbon Controls

In addition to the following controls, vertical separators can be added to ribbon panels to group related sets of controls.

#### Push Buttons

There are three types of buttons you can add to a panel: simple push buttons, drop-down buttons, and split buttons. The HelloWorld button in Figure 14 is a push button. When the button is pressed, the corresponding command is triggered.

In addition to the Enabled property, PushButton has the AvailabilityClassName property which can be used to set the name of an IExternalCommandAvailability interface that controls when the command is available.

<table summary="" id="GUID-1547E521-59BD-4819-A989-F5A238B9F2B3__TABLE_77A796C017894BCCA51114F955121CEE"><tbody><tr><td><b>Code Region: Adding a push button</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>AddSimplePushButton</span><span>(</span><span>RibbonPanel</span><span> panel</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>PushButton</span><span> pushButton </span><span>=</span><span> panel</span><span>.</span><span>AddItem</span><span>(</span><span>new</span><span> </span><span>PushButtonData</span><span>(</span><span>"HelloWorld"</span><span>,</span><span>
                </span><span>"HelloWorld"</span><span>,</span><span> </span><span>@</span><span>"D:\HelloWorld.dll"</span><span>,</span><span> </span><span>"HelloWorld.CsHelloWorld"</span><span>))</span><span> </span><span>as</span><span> </span><span>PushButton</span><span>;</span><span>

        pushButton</span><span>.</span><span>ToolTip</span><span> </span><span>=</span><span> </span><span>"Say Hello World"</span><span>;</span><span>
        </span><span>// Set the large image shown on button</span><span>
        pushButton</span><span>.</span><span>LargeImage</span><span> </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\39-Globe_32x32.png"</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

#### Drop-down buttons

Drop-down buttons expand to display two or more commands in a drop-down menu. In the Revit API, drop-down buttons are referred to as PulldownButtons. Horizontal separators can be added between items in the drop-down menu.

Each command in a drop-down menu can also have an associated LargeImage as shown in the example above.

#### Split buttons

Split buttons are drop-down buttons with a default push button attached. The top half of the button works like a push button while the bottom half functions as a drop-down button. The Option One button in Figure 14 is a split button.

Initially, the push button will be the top item in the drop-down list. However, by using the IsSynchronizedWithCurrentItem property, the default command (which is displayed as the push button top half of the split button) can be synchronized with the last used command. By default it will be synched. Selecting Option Two in the split button from Figure 14 above yields:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-FCBB9C72-5786-4B34-BF1F-E41A99F446C3-low.png)**Figure 16: Split button synchronized with current item**

Note that the ToolTip, ToolTipImage and LongDescription properties for SplitButton are ignored. The tooltip for the current push button is shown instead.

<table summary="" id="GUID-1547E521-59BD-4819-A989-F5A238B9F2B3__TABLE_3C289F93407945FFB4B4AD459E9ACF99"><tbody><tr><td><b>Code Region: Adding a split button</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>AddSplitButton</span><span>(</span><span>RibbonPanel</span><span> panel</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>string</span><span> assembly </span><span>=</span><span> </span><span>@</span><span>"D:\Sample\HelloWorld\bin\Debug\Hello.dll"</span><span>;</span><span>

        </span><span>// create push buttons for split button drop down</span><span>
        </span><span>PushButtonData</span><span> bOne </span><span>=</span><span> </span><span>new</span><span> </span><span>PushButtonData</span><span>(</span><span>"ButtonNameA"</span><span>,</span><span> </span><span>"Option One"</span><span>,</span><span>
         assembly</span><span>,</span><span> </span><span>"Hello.HelloOne"</span><span>);</span><span>
        bOne</span><span>.</span><span>LargeImage</span><span> </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\One.bmp"</span><span>));</span><span>

        </span><span>PushButtonData</span><span> bTwo </span><span>=</span><span> </span><span>new</span><span> </span><span>PushButtonData</span><span>(</span><span>"ButtonNameB"</span><span>,</span><span> </span><span>"Option Two"</span><span>,</span><span> 
                assembly</span><span>,</span><span> </span><span>"Hello.HelloTwo"</span><span>);</span><span>
        bTwo</span><span>.</span><span>LargeImage</span><span> </span><span>=</span><span>
         </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\Two.bmp"</span><span>));</span><span>

        </span><span>PushButtonData</span><span> bThree </span><span>=</span><span> </span><span>new</span><span> </span><span>PushButtonData</span><span>(</span><span>"ButtonNameC"</span><span>,</span><span> </span><span>"Option Three"</span><span>,</span><span>
         assembly</span><span>,</span><span> </span><span>"Hello.HelloThree"</span><span>);</span><span>
        bThree</span><span>.</span><span>LargeImage</span><span> </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\Three.bmp"</span><span>));</span><span>

        </span><span>SplitButtonData</span><span> sb1 </span><span>=</span><span> </span><span>new</span><span> </span><span>SplitButtonData</span><span>(</span><span>"splitButton1"</span><span>,</span><span> </span><span>"Split"</span><span>);</span><span>
        </span><span>SplitButton</span><span> sb </span><span>=</span><span> panel</span><span>.</span><span>AddItem</span><span>(</span><span>sb1</span><span>)</span><span> </span><span>as</span><span> </span><span>SplitButton</span><span>;</span><span>
        sb</span><span>.</span><span>AddPushButton</span><span>(</span><span>bOne</span><span>);</span><span>
        sb</span><span>.</span><span>AddPushButton</span><span>(</span><span>bTwo</span><span>);</span><span>
        sb</span><span>.</span><span>AddPushButton</span><span>(</span><span>bThree</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

#### Radio buttons

A radio button group is a set of mutually exclusive toggle buttons; only one can be selected at a time. After adding a RadioButtonGroup to a panel, use the AddItem() or AddItems() methods to add toggle buttons to the group. Toggle buttons are derived from PushButton. The RadioButtonGroup.Current property can be used to access the currently selected button.

Note that tooltips do not apply to radio button groups. Instead, the tooltip for each toggle button is displayed as the mouse moves over the individual buttons.

<table summary="" id="GUID-1547E521-59BD-4819-A989-F5A238B9F2B3__TABLE_147473E853D148298B9D5C05DF1F3C1F"><tbody><tr><td><b>Code Region: Adding radio button group</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>AddRadioGroup</span><span>(</span><span>RibbonPanel</span><span> panel</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// add radio button group</span><span>
        </span><span>RadioButtonGroupData</span><span> radioData </span><span>=</span><span> </span><span>new</span><span> </span><span>RadioButtonGroupData</span><span>(</span><span>"radioGroup"</span><span>);</span><span>
        </span><span>RadioButtonGroup</span><span> radioButtonGroup </span><span>=</span><span> panel</span><span>.</span><span>AddItem</span><span>(</span><span>radioData</span><span>)</span><span> </span><span>as</span><span> </span><span>RadioButtonGroup</span><span>;</span><span>

        </span><span>// create toggle buttons and add to radio button group</span><span>
        </span><span>ToggleButtonData</span><span> tb1 </span><span>=</span><span> </span><span>new</span><span> </span><span>ToggleButtonData</span><span>(</span><span>"toggleButton1"</span><span>,</span><span> </span><span>"Red"</span><span>);</span><span>
        tb1</span><span>.</span><span>ToolTip</span><span> </span><span>=</span><span> </span><span>"Red Option"</span><span>;</span><span>
        tb1</span><span>.</span><span>LargeImage</span><span> </span><span>=</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\Red.bmp"</span><span>));</span><span>
        </span><span>ToggleButtonData</span><span> tb2 </span><span>=</span><span> </span><span>new</span><span> </span><span>ToggleButtonData</span><span>(</span><span>"toggleButton2"</span><span>,</span><span> </span><span>"Green"</span><span>);</span><span>
        tb2</span><span>.</span><span>ToolTip</span><span> </span><span>=</span><span> </span><span>"Green Option"</span><span>;</span><span>
        tb2</span><span>.</span><span>LargeImage</span><span> </span><span>=</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\Green.bmp"</span><span>));</span><span>
        </span><span>ToggleButtonData</span><span> tb3 </span><span>=</span><span> </span><span>new</span><span> </span><span>ToggleButtonData</span><span>(</span><span>"toggleButton3"</span><span>,</span><span> </span><span>"Blue"</span><span>);</span><span>
        tb3</span><span>.</span><span>ToolTip</span><span> </span><span>=</span><span> </span><span>"Blue Option"</span><span>;</span><span>
        tb3</span><span>.</span><span>LargeImage</span><span> </span><span>=</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\Blue.bmp"</span><span>));</span><span>
        radioButtonGroup</span><span>.</span><span>AddItem</span><span>(</span><span>tb1</span><span>);</span><span>
        radioButtonGroup</span><span>.</span><span>AddItem</span><span>(</span><span>tb2</span><span>);</span><span>
        radioButtonGroup</span><span>.</span><span>AddItem</span><span>(</span><span>tb3</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

#### Text box

A text box is an input control for users to enter text. The image for a text box can be used as a clickable button by setting the ShowImageAsButton property to true. The default is false. The image is displayed to the left of the text box when ShowImageAsButton is false, and displayed at the right end of the text box when it acts as a button, as in Figure 14.

The text entered in the text box is only accepted if the user hits the Enter key or if they click the associated image when the image is shown as a button. Otherwise, the text will revert to its previous value.

In addition to providing a tooltip for a text box, the PromptText property can be used to indicate to the user what type of information to enter in the text box. Prompt text is displayed when the text box is empty and does not have keyboard focus. This text is displayed in italics. The text box in Figure 14 has the prompt text "Enter a comment".

The width of the text box can be set using the Width property. The default is 200 device-independent units.

The TextBox.EnterPressed event is triggered when the user presses enter, or when they click on the associated image for the text box when ShowImageAsButton is set to true. When implementing an EnterPressed event handler, cast the sender object to TextBox to get the value the user has entered as shown in the following example.

<table summary="" id="GUID-1547E521-59BD-4819-A989-F5A238B9F2B3__TABLE_4FF63092AB194569B48D83650CDBF814"><tbody><tr><td><b>Code Region: TextBox.EnterPressed event handler</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>ProcessText</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Events</span><span>.</span><span>TextBoxEnterPressedEventArgs</span><span> args</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// cast sender as TextBox to retrieve text value</span><span>
        </span><span>TextBox</span><span> textBox </span><span>=</span><span> sender </span><span>as</span><span> </span><span>TextBox</span><span>;</span><span>
        </span><span>string</span><span> strText </span><span>=</span><span> textBox</span><span>.</span><span>Value</span><span> </span><span>as</span><span> </span><span>string</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The inherited ItemText property has no effect for TextBox. The user-entered text can be obtained from the Value property, which must be converted to a string.

See the section on stacked ribbon items for an example of adding a TextBox to a ribbon panel, including how to register the event above.

#### Combo box

A combo box is a pulldown with a set of selectable items. After adding a ComboBox to a panel, use the AddItem() or AddItems() methods to add ComboBoxMembers to the list.

Separators can also be added to separate items in the list or members can be optionally grouped using the ComboBoxMember.GroupName property. All members with the same GroupName will be grouped together with a header that shows the group name. Any items not assigned a GroupName will be placed at the top of the list. Note that when grouping items, separators should not be used as they will be placed at the end of the group rather than in the order they are added.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-62DBB2D2-0D7B-4EDC-945B-DC86BAE6BF6F-low.png)**Figure 17: Combo box with grouping**

ComboBox has three events:

-   CurrentChanged - triggered when the current item of the ComboBox is changed
-   DropDownClosed - triggered when the drop-down of the ComboBox is closed
-   DropDownClosed - triggered when the drop-down of the ComboBox is opened

See the code region in the following section on stacked ribbon items for a sample of adding a ComboBox to a ribbon panel.

#### Stacked Panel Items

To conserve panel space, you can add small panel items in stacks of two or three. Each item in the stack can be a push button, a drop-down button, a combo box or a text box. Radio button groups and split buttons cannot be stacked. Stacked buttons should have an image associated through their Image property, rather than LargeImage. A 16×16 image is ideal for small stacked buttons.

The following example produces the stacked text box and combo box in Figure 14.

<table summary="" id="GUID-1547E521-59BD-4819-A989-F5A238B9F2B3__TABLE_B2EFA8F6E8784C5999DD63818BC3092D"><tbody><tr><td><b>Code Region: Adding a text box and combo box as stacked items</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>AddStackedButtons</span><span>(</span><span>RibbonPanel</span><span> panel</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>ComboBoxData</span><span> cbData </span><span>=</span><span> </span><span>new</span><span> </span><span>ComboBoxData</span><span>(</span><span>"comboBox"</span><span>);</span><span>

        </span><span>TextBoxData</span><span> textData </span><span>=</span><span> </span><span>new</span><span> </span><span>TextBoxData</span><span>(</span><span>"Text Box"</span><span>);</span><span>
        textData</span><span>.</span><span>Image</span><span> </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\39-Globe_16x16.png"</span><span>));</span><span>
        textData</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"Text Box"</span><span>;</span><span>
        textData</span><span>.</span><span>ToolTip</span><span> </span><span>=</span><span> </span><span>"Enter some text here"</span><span>;</span><span>
        textData</span><span>.</span><span>LongDescription</span><span> </span><span>=</span><span> </span><span>"This is text that will appear next to the image"</span><span> 
                </span><span>+</span><span> </span><span>"when the user hovers the mouse over the control"</span><span>;</span><span>
        textData</span><span>.</span><span>ToolTipImage</span><span> </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\39-Globe_32x32.png"</span><span>));</span><span>

        </span><span>IList</span><span>&lt;</span><span>RibbonItem</span><span>&gt;</span><span> stackedItems </span><span>=</span><span> panel</span><span>.</span><span>AddStackedItems</span><span>(</span><span>textData</span><span>,</span><span> cbData</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>stackedItems</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>1</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>TextBox</span><span> tBox </span><span>=</span><span> stackedItems</span><span>[</span><span>0</span><span>]</span><span> </span><span>as</span><span> </span><span>TextBox</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>tBox </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
                </span><span>{</span><span>
                        tBox</span><span>.</span><span>PromptText</span><span> </span><span>=</span><span> </span><span>"Enter a comment"</span><span>;</span><span>
                        tBox</span><span>.</span><span>ShowImageAsButton</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
                        tBox</span><span>.</span><span>ToolTip</span><span> </span><span>=</span><span> </span><span>"Enter some text"</span><span>;</span><span>
                        </span><span>// Register event handler ProcessText</span><span>
                        tBox</span><span>.</span><span>EnterPressed</span><span> </span><span>+=</span><span> 
                </span><span>new</span><span> </span><span>EventHandler</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Events</span><span>.</span><span>TextBoxEnterPressedEventArgs</span><span>&gt;(</span><span>ProcessText</span><span>);</span><span>
                </span><span>}</span><span>

                </span><span>ComboBox</span><span> cBox </span><span>=</span><span> stackedItems</span><span>[</span><span>1</span><span>]</span><span> </span><span>as</span><span> </span><span>ComboBox</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>cBox </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
                </span><span>{</span><span>
                        cBox</span><span>.</span><span>ItemText</span><span> </span><span>=</span><span> </span><span>"ComboBox"</span><span>;</span><span>
                        cBox</span><span>.</span><span>ToolTip</span><span> </span><span>=</span><span> </span><span>"Select an Option"</span><span>;</span><span>
                        cBox</span><span>.</span><span>LongDescription</span><span> </span><span>=</span><span> </span><span>"Select a number or letter"</span><span>;</span><span>

                        </span><span>ComboBoxMemberData</span><span> cboxMemDataA </span><span>=</span><span> </span><span>new</span><span> </span><span>ComboBoxMemberData</span><span>(</span><span>"A"</span><span>,</span><span> </span><span>"Option A"</span><span>);</span><span>
                        cboxMemDataA</span><span>.</span><span>Image</span><span> </span><span>=</span><span> 
                                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\A.bmp"</span><span>));</span><span>
                        cboxMemDataA</span><span>.</span><span>GroupName</span><span> </span><span>=</span><span> </span><span>"Letters"</span><span>;</span><span>
                        cBox</span><span>.</span><span>AddItem</span><span>(</span><span>cboxMemDataA</span><span>);</span><span>

                        </span><span>ComboBoxMemberData</span><span> cboxMemDataB </span><span>=</span><span> </span><span>new</span><span> </span><span>ComboBoxMemberData</span><span>(</span><span>"B"</span><span>,</span><span> </span><span>"Option B"</span><span>);</span><span>
                        cboxMemDataB</span><span>.</span><span>Image</span><span> </span><span>=</span><span> 
                                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\B.bmp"</span><span>));</span><span>
                        cboxMemDataB</span><span>.</span><span>GroupName</span><span> </span><span>=</span><span> </span><span>"Letters"</span><span>;</span><span>
                        cBox</span><span>.</span><span>AddItem</span><span>(</span><span>cboxMemDataB</span><span>);</span><span>

                        </span><span>ComboBoxMemberData</span><span> cboxMemData </span><span>=</span><span> </span><span>new</span><span> </span><span>ComboBoxMemberData</span><span>(</span><span>"One"</span><span>,</span><span> </span><span>"Option 1"</span><span>);</span><span>
                        cboxMemData</span><span>.</span><span>Image</span><span> </span><span>=</span><span> 
                                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\One.bmp"</span><span>));</span><span>
                        cboxMemData</span><span>.</span><span>GroupName</span><span> </span><span>=</span><span> </span><span>"Numbers"</span><span>;</span><span>
                        cBox</span><span>.</span><span>AddItem</span><span>(</span><span>cboxMemData</span><span>);</span><span>
                        </span><span>ComboBoxMemberData</span><span> cboxMemData2 </span><span>=</span><span> </span><span>new</span><span> </span><span>ComboBoxMemberData</span><span>(</span><span>"Two"</span><span>,</span><span> </span><span>"Option 2"</span><span>);</span><span>
                        cboxMemData2</span><span>.</span><span>Image</span><span> </span><span>=</span><span> 
                                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\Two.bmp"</span><span>));</span><span>
                        cboxMemData2</span><span>.</span><span>GroupName</span><span> </span><span>=</span><span> </span><span>"Numbers"</span><span>;</span><span>
                        cBox</span><span>.</span><span>AddItem</span><span>(</span><span>cboxMemData2</span><span>);</span><span>
                        </span><span>ComboBoxMemberData</span><span> cboxMemData3 </span><span>=</span><span> </span><span>new</span><span> </span><span>ComboBoxMemberData</span><span>(</span><span>"Three"</span><span>,</span><span> </span><span>"Option 3"</span><span>);</span><span>
                        cboxMemData3</span><span>.</span><span>Image</span><span> </span><span>=</span><span> 
                                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\Three.bmp"</span><span>));</span><span>
                        cboxMemData3</span><span>.</span><span>GroupName</span><span> </span><span>=</span><span> </span><span>"Numbers"</span><span>;</span><span>
                        cBox</span><span>.</span><span>AddItem</span><span>(</span><span>cboxMemData3</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

#### Slide-out panel

Use the RibbonPanel.AddSlideOut() method to add a slide out to the bottom of the ribbon panel. When a slide-out is added, an arrow is shown on the bottom of the panel, which when clicked will display the slide-out. After calling AddSlideOut(), subsequent calls to add new items to the panel will be added to the slide-out, so the slide-out must be added after all other controls have been added to the ribbon panel.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-5B17EB5F-D4B4-472D-9033-B11C35F7E40B-low.png)**Figure 18: Slide-out**

The following example produces the slide-out shown above:

<table summary="" id="GUID-1547E521-59BD-4819-A989-F5A238B9F2B3__TABLE_F322CD0D68E74D41B08EAF48740B8CA0"><tbody><tr><td><b>Code Region: TextBox.EnterPressed event handler</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddSlideOut</span><span>(</span><span>RibbonPanel</span><span> panel</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>string</span><span> assembly </span><span>=</span><span> </span><span>@</span><span>"D:\Sample\HelloWorld\bin\Debug\Hello.dll"</span><span>;</span><span>

        panel</span><span>.</span><span>AddSlideOut</span><span>();</span><span>

        </span><span>// create some controls for the slide out</span><span>
        </span><span>PushButtonData</span><span> b1 </span><span>=</span><span> </span><span>new</span><span> </span><span>PushButtonData</span><span>(</span><span>"ButtonName1"</span><span>,</span><span> </span><span>"Button 1"</span><span>,</span><span> 
                assembly</span><span>,</span><span> </span><span>"Hello.HelloButton"</span><span>);</span><span>
        b1</span><span>.</span><span>LargeImage</span><span> </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\39-Globe_32x32.png"</span><span>));</span><span>
        </span><span>PushButtonData</span><span> b2 </span><span>=</span><span> </span><span>new</span><span> </span><span>PushButtonData</span><span>(</span><span>"ButtonName2"</span><span>,</span><span> </span><span>"Button 2"</span><span>,</span><span> 
                assembly</span><span>,</span><span> </span><span>"Hello.HelloTwo"</span><span>);</span><span>
        b2</span><span>.</span><span>LargeImage</span><span> </span><span>=</span><span>
                </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Media</span><span>.</span><span>Imaging</span><span>.</span><span>BitmapImage</span><span>(</span><span>new</span><span> </span><span>Uri</span><span>(@</span><span>"D:\Sample\HelloWorld\bin\Debug\39-Globe_16x16.png"</span><span>));</span><span>

        </span><span>// items added after call to AddSlideOut() are added to slide-out automatically</span><span>
        panel</span><span>.</span><span>AddItem</span><span>(</span><span>b1</span><span>);</span><span>
        panel</span><span>.</span><span>AddItem</span><span>(</span><span>b2</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Ribbon Panels and Controls  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Revit-style Task Dialogs  Autodesk.md ===== -->

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


<!-- ===== END: Help  Revit-style Task Dialogs  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  DB-level External Applications  Autodesk.md ===== -->

---
created: 2026-01-28T20:40:40 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | DB-level External Applications | Autodesk

> ## Excerpt
> Database-level add-ins are External Applications that do not add anything to the Revit UI. DB-level External Applications can be used when the purpose of the application is to assign events and/or updaters to the Revit session.

---
Database-level add-ins are External Applications that do not add anything to the Revit UI. DB-level External Applications can be used when the purpose of the application is to assign events and/or updaters to the Revit session.

To add a DB-level External Application to Revit, you create an object that implements the IExternalDBApplication interface.

The IExternalDBApplication interface has two abstract methods, OnStartup() and OnShutdown(), which you override in your DB-level external application. Revit calls OnStartup() when it starts, and OnShutdown() when it closes. This is very similar to IExternalApplication, but note that these methods return Autodesk.Revit.DB.ExternalDBApplicationResult rather than Autodesk.Revit.UI.Result and use ControlledApplication rather than UIControlledApplication.

<table summary="" id="GUID-F41AB4DF-5585-4FBD-815E-A26FED38889B__TABLE_4CB2B02571DE4121A6E813B4403A7F36"><tbody><tr><td><b>Code Region: IExternalDBApplication OnShutdown() and OnStartup()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>interface</span><span> </span><span>IExternalDBApplication</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ExternalDBApplicationResult</span><span> </span><span>OnStartup</span><span>(</span><span>ControlledApplication</span><span> application</span><span>);</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ExternalDBApplicationResult</span><span> </span><span>OnShutdown</span><span>(</span><span>ControlledApplication</span><span> application</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The ControlledApplication parameter provides access to Revit \[Database Events\](../../Advanced\_Topics/Events/Database\_Events.html). Events and Updaters to which the database-level application will respond can be registered in the OnStartup method.


<!-- ===== END: Help  DB-level External Applications  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Add-In Registration  Microsoft Learn.md ===== -->

---
created: 2026-01-28T20:38:43 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/previous-versions/19dax6cz(v=vs.140)
author: 
---

# Add-In Registration | Microsoft Learn

> ## Excerpt
> Visual Studio add-ins are deprecated in Visual Studio 2013. You should upgrade your add-ins to VSPackage extensions. For more information about upgrading, see FAQ: Converting Add-ins to VSPackage Extensions.

---
___

#### Share via

___

Visual Studio add-ins are deprecated in Visual Studio 2013. You should upgrade your add-ins to VSPackage extensions. For more information about upgrading, see [FAQ: Converting Add-ins to VSPackage Extensions](https://msdn.microsoft.com/en-us/library/dn246938(v=vs.140)).

After an add-in is created, you must register it with Visual Studio before it can be activated in **Add-In Manager**. This is accomplished by using an XML file that has an .addin file name extension.

The .addin file describes the information that Visual Studio requires to display the add-in in **Add-In Manager**. When Visual Studio starts, it looks in the .addin file location for any available .addin files. If it finds any, it reads the XML file and gives **Add-In Manager** the information it requires to start the add-in when it is clicked.

The .addin file is created automatically when you create an add-in by using the Add-In Wizard. You can also create an .addin file manually by using the information in this topic.

## File Locations

Two copies of the .addin file are automatically created by the Add-In Wizard, as follows:

  
| 
**.Addin File Location**

 | 

**.Dll File Location**

 | 

**Description**

 |
| --- | --- | --- |
| 

Root project folder

\\Documents\\Visual Studio 2013\\Projects\\MyAddin1\\MyAddin1\\

 | 

Local path (MyAddin1.dll)

 | 

Used for deployment of the add-in project. Included in the project for ease of editing and has the local path for xcopy-style deployment.

 |
| 

Add-in folder

\\Documents\\Visual Studio 2013\\Addins\\

\-or-

Shared Documents Location\\Addins\\

 | 

Project debug folder

(For example, \\ Documents\\Visual Studio 2013

Projects\\MyAddin1\\MyAddin1\\bin\\)

 | 

Used for running the add-in in the debugging environment. Should always point to the output path of the current build configuration.

 |

To install the add-in on another computer, the .addin file must be placed in a location where Visual Studio checks for add-ins. These locations are listed in the **Options** dialog box, in the **Environment** node, on the **Add-in Security** page. For more information, see [Add-In Security](https://learn.microsoft.com/en-us/previous-versions/1326zbk3(v=vs.140)).

The .dll file that contains the add-in can be installed anywhere on the client computer. However, we recommend that you put it with the .addin file.

Note

The <Assembly> element of the .addin file must point to the .dll file that contains the binaries for the add-in.

## The .Addin File

The .addin XML file is split into the following tagged sections:

 
| 
**Section**

 | 

**Description**

 |
| --- | --- |
| 

Host Application

 | 

(Required.) Specifies the names and version numbers of the applications that can load the add-in.

 |
| 

Addin

 | 

(Required) Contains the elements that describe the add-in.

 |
| 

Tools Options Page

 | 

(Optional) Specifies a page in the **Options** dialog box where the add-in can be configured. Child nodes specify the category and subcategory of the **Options** page, and also its assembly name and full class name.

 |

The following elements are children of the <Addin> section:

 
| 
**Element**

 | 

**Description**

 |
| --- | --- |
| 

About Box Details

 | 

(Optional) Specifies the text that will be displayed for your add-in in the Visual Studio **About** dialog box.

 |
| 

About Icon Data

 | 

(Optional) Contains binary data that specifies the icon that will be displayed for your add-in in the Visual Studio **About** dialog box.

 |
| 

About Icon Location

 | 

(Optional) Specifies the absolute path or relative path of the icon that will be displayed for your add-in in the Visual Studio **About** dialog box.

 |
| 

Assembly

 | 

(Required.) Specifies the location of the add-in binaries. This field can be set to a local path, a network path, or a URL.

 |
| 

Command Line Safe

 | 

(Optional) Specifies the Visual Studio modes with which the add-in is compatible, for example, command-line only, integrated development environment (IDE)-only, or both.

 |
| 

Command Preload

 | 

(Optional) Specifies the preloaded state of the add-in; that is, whether the add-in should create its UI by using a method such as [Commands.AddNamedCommand](https://msdn.microsoft.com/en-us/library/sa001y04(v=vs.140)).

 |
| 

Full Class Name

 | 

(Required.) Specifies the name of the class that is used to connect to the add-in.

 |
| 

Load Behavior

 | 

(Optional) Defines whether an add-in is loaded at startup or manually.

 |

Here are the details for each setting. For more information about the hierarchical location many of the elements that are described, see "Example .Addin XML File" later in this topic.

## Host Application

The <Name> element in the Host Application section contains the name of the application. This is the name that is displayed on the title bar of the application or is returned by DTE.Name. For example, for Visual Studio, the tag would contain "Microsoft Visual Studio".

There can be more than one Host Application value per .addin file. Every value must be bracketed by using <Name> tags in the <HostApplication> element. In addition to containing a <Name> element, every <HostApplication> element must also include the version number of the application bracketed by <Version> tags. For example,

```
   <HostApplication>
      <!-- First Host App name (required). -->
      <Name>Microsoft Visual Studio</Name>
      <Version>12.0</Version>
   </HostApplication>
   <HostApplication>
      <!-- An additional supported program/version. -->
      <Name>Microsoft Visual Studio</Name>
      <Version>11.0</Version>
   </HostApplication>
```

Alternatively, you can specify an asterisk (\*) to represent the value for <Version> for any version of Visual Studio.

## Friendly Name

The <FriendlyName> element, which is located under the <Addin> element, specifies the string that will be displayed in the **Available Add-ins** column in **Add-in Manager**. For example,

```
   <FriendlyName>My New Super Addin</FriendlyName>
```

## Description

The <Description> element, which is located under the <Addin> element, specifies the string that will be displayed in the **Description** box in **Add-in Manager**. For example,

```
   <Description>This add-in will change your life!</Description>
```

## About Box Details

If you select the option to generate settings for the **About** dialog box when you create your add-in, this element is added to the .addin file. This element specifies the text that will be displayed in the Visual Studio **About** dialog box. For example,

```
   <AboutBoxDetails>For add-in support, call 1-800-xxx-
     xxxx.</AboutBoxDetails>
```

## About Icon Data

If you select the option to generate settings for the **About** dialog box when you create your add-in, this element is added to the .addin file. This element contains binary data that specifies the icon that will be displayed in the Visual Studio **About** dialog box. For example,

```
<AboutIconData>0000010006 . . . FFFF0000</AboutIconData>
```

## Assembly

The <Assembly> element, which is located under the <Addin> element, specifies the location of the add-in binary files. This element can be set to a relative path, an absolute path ("file"), a registered assembly name ("assembly"), or a URL ("url").

-   The following example shows an absolute path location. In this case, the src parameter is set to file to indicate the location of the add-in DLL.
    
    ```
    <Assembly src="file">C:\Documents and Settings\jdoe\Application Data\Microsoft\Visual Studio\12.0\AddIns\MyAddin4.dll</Assembly>
    ```
    
-   The following example shows a registered location. In this case, the src parameter is set to assembly to indicate a registered add-in DLL.
    
    ```
    <Assembly src="assembly">BookshelfDefineAddin</Assembly>
    ```
    
-   The following example shows a URL location. In this case, the src parameter is set to url to indicate the Web-based location of the add-in DLL.
    
    ```
    <Assembly src="url">https://somewebsite.com/MyAddin4.dll</Assembly>
    ```
    

## Full Class Name

The <FullClassName> element specifies the full name of the class that is used to connect to the add-in. This includes the namespace that contains the class. For example,

```
    <FullClassName>MyAddin4.Connect</FullClassName>
```

## Load Behavior

The <LoadBehavior> element defines whether an add-in is loaded automatically at IDE startup or is started manually. The <LoadBehavior> element is under the <Addin> element. For example,

```
    <LoadBehavior>1</LoadBehavior>
```

Although usage of <LoadBehavior> is optional, we recommend that you use it to explicitly define when an add-in loads.

 
| 
Value

 | 

Description

 |
| --- | --- |
| 

0

 | 

The add-in is not loaded at IDE startup and must be started manually.

 |
| 

1

 | 

The add-in is automatically loaded at IDE startup.

 |
| 

4

 | 

The add-in is loaded when devenv is started at a command prompt by using a build switch (**devenv /build**).

 |

## Command Preload

The <CommandPreload> element specifies whether the add-in must be preloaded. Preloading loads the add-in the first time that Visual Studio is started after the .addin file is installed. For example,

```
    <CommandPreload>1</CommandPreload>
```

This element lets you specify that an add-in must be loaded after Visual Studio is started. It gives your add-in a chance to create required UI elements such as command bar buttons, or perform other first-time-only initialization tasks such as creating default add-in settings. The add-in is then unloaded until a user executes one of the commands that the add-in created. Thereafter, the add-in is loaded as needed.

 
| 
Value

 | 

Description

 |
| --- | --- |
| 

0

 | 

The add-in does not load until either the user starts it by using **Add-In Manager** or the add-in is set to load on startup.

 |
| 

1

 | 

The add-in is loaded automatically when Visual Studio starts for the first time after the .addin file is installed.

 |

You can check the **OnConnection** method that you implement to see whether the type of connection, which is specified by using the second argument to **OnConnection**, is **ext\_cm\_UISetup**. If it is, you can perform whatever command placements you want by using either the **AddNamedCommand** or **AddControl** method.

## Command Line Safe

The optional <CommandLineSafe> element indicates whether the add-in was designed to avoid displaying a UI when it is started at a command prompt, for example, when you perform command-line builds or similar operations. (This is done by selecting **My Add-in will never put up a modal UI** in the **Add-in Wizard**.) Also, it specifies the Visual Studio modes with which the add-in is compatible, for example, command-line-only or IDE only. For example,

```
    <CommandLineSafe>0</CommandLineSafe>
```

 
| 
Value

 | 

Description

 |
| --- | --- |
| 

0

 | 

Specifies that the add-in is not command-line safe and may display a UI.

 |
| 

1

 | 

Specifies that the add-in is command-line safe and does not display a UI.

 |

## Tools Options Page

The optional <ToolsOptionsPage> element specifies an **Options** page so that users can configure the add-in. Child nodes specify the category and subcategory that the page appears in, and the assembly name and full class name of the **Options** page. The following example shows the hierarchy of this element:

```
  <ToolsOptionsPage>
    <Category Name="Text Editor">
      <SubCategory Name="General">
        <Assembly>"MyFilePath\MyAddInOptionPage.dll"</Assembly>
        <FullClassName>"MyNamespace.MyAddInOptionPage"</FullClassName>
      </SubCategory>
    </Category>
  </ToolsOptionsPage>
```

## Example .Addin XML File

The following example shows a complete .addin XML file. It shows the hierarchy and locations for the elements that are described in this topic.

```
<?xml version="1.0" encoding="UTF-16" standalone="no"?>
<Extensibility 
  xmlns="https://schemas.microsoft.com/AutomationExtensibility">
    <HostApplication>
        <Name>Microsoft Visual Studio</Name>
        <Version>12.0</Version>
    </HostApplication> 
    <HostApplication>
        <Name>Microsoft Visual Studio</Name>
        <Version>11.0</Version>
    </HostApplication>
    <Addin>
        <FriendlyName>My great new add-in.</FriendlyName>
        <Description>This add-in does it all.</Description>
        <AboutBoxDetails>Copyright 2013.</AboutBoxDetails>
        <AboutIconData>0000 . . . FFFF0000</AboutIconData>
        <Assembly>MyNewAddin.dll</Assembly>
        <FullClassName>MyNewAddin.Connect</FullClassName>
        <LoadBehavior>1</LoadBehavior>
        <CommandPreload>1</CommandPreload>
        <CommandLineSafe>0</CommandLineSafe>
    </Addin>
</Extensibility>
```

## See Also

#### Tasks

[How to: Control Add-Ins By Using the Add-In Manager](https://learn.microsoft.com/en-us/previous-versions/xwdatdwh(v=vs.140))

[How to: Create an Add-In](https://learn.microsoft.com/en-us/previous-versions/80493a3w(v=vs.140))

[Walkthrough: Creating a Wizard](https://learn.microsoft.com/en-us/previous-versions/7k3w6w59(v=vs.140))

#### Reference

[PAVE Visual Studio Commands and Switches](https://learn.microsoft.com/en-us/previous-versions/kcc7tke7(v=vs.140))

#### Concepts

[Automation Object Model Chart](https://learn.microsoft.com/en-us/previous-versions/za2b25t3(v=vs.140))

#### Other Resources

[Creating Add-ins and Wizards](https://learn.microsoft.com/en-us/previous-versions/5abkeks7(v=vs.140))


<!-- ===== END: Add-In Registration  Microsoft Learn.md ===== -->

---



<!-- ===== BEGIN: Commands.AddNamedCommand Method (EnvDTE)  Microsoft Learn.md ===== -->

---
created: 2026-01-28T20:39:52 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/dotnet/api/envdte.commands.addnamedcommand?view=visualstudiosdk-2022&redirectedfrom=MSDN#EnvDTE_Commands_AddNamedCommand_EnvDTE_AddIn_System_String_System_String_System_String_System_Boolean_System_Int32_System_Object____System_Int32_
author: dotnet-bot
---

# Commands.AddNamedCommand Method (EnvDTE) | Microsoft Learn

> ## Excerpt
> Creates a named command that is saved by the environment and made available the next time the environment starts, even if the VSPackage is not loaded on environment startup. Add-ins are now deprecated. For more information, see FAQ: Converting Add-ins to VSPackage Extensions.

---
Important

Some information relates to prerelease product that may be substantially modified before it’s released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Caution

AddIn related extension points are no longer supported in Visual Studio.

Creates a named command that is saved by the environment and made available the next time the environment starts, even if the VSPackage is not loaded on environment startup.

Add-ins are now deprecated. For more information, see [FAQ: Converting Add-ins to VSPackage Extensions](https://learn.microsoft.com/en-us/visualstudio/extensibility/faq-converting-add-ins-to-vspackage-extensions).

C++/WinRT

```
EnvDTE::Command AddNamedCommand(EnvDTE::AddIn const & AddInInstance, std::wstring const & Name, std::wstring const & ButtonText, std::wstring const & Tooltip, bool MSOButton, int Bitmap = 0, std::Array <winrt::Windows::Foundation::IInspectable const &> const & & ContextUIGUIDs, int vsCommandDisabledFlagsValue = 16);
```

#### Parameters

AddInInstance

[AddIn](https://learn.microsoft.com/en-us/dotnet/api/envdte.addin?view=visualstudiosdk-2022)

Required. The [AddIn](https://learn.microsoft.com/en-us/dotnet/api/envdte.addin?view=visualstudiosdk-2022) that adds the new command.

ButtonText

[String](https://learn.microsoft.com/en-us/dotnet/api/system.string)

Required. The name to use if the command is bound to a button that is displayed by name rather than by icon.

Tooltip

[String](https://learn.microsoft.com/en-us/dotnet/api/system.string)

Required. The text displayed when a user hovers the mouse pointer over any control bound to the new command.

MSOButton

[Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean)

Required. Indicates whether the named command's button picture is an Office picture. `True` = button. If `MSOButton` is `False`, then `Bitmap` is the ID of a 16x16 bitmap resource (but not an icon resource) in a Visual C++ resource DLL that must reside in a folder with the language's locale identifier (1033 for English).

Bitmap

[Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32)

Optional. The ID of a bitmap to display on the button.

ContextUIGUIDs

[Object](https://learn.microsoft.com/en-us/dotnet/api/system.object)\[\]

Optional. A SafeArray of GUIDs that determines which environment contexts (that is, debug mode, design mode, and so on) show the command. See [vsCommandDisabledFlags](https://learn.microsoft.com/en-us/dotnet/api/envdte.vscommanddisabledflags?view=visualstudiosdk-2022)..

vsCommandDisabledFlagsValue

[Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32)

#### Returns

A [Command](https://learn.microsoft.com/en-us/dotnet/api/envdte.command?view=visualstudiosdk-2022) object.

Attributes

## Remarks

You can later change the `ButtonText` name by responding to the `QueryStatus` method. If the text begins with "#", then the rest of the string is an integer that represents a resource ID in the registered satellite DLL.

The `ContextUIGUIDs` parameter and the `vsCommandStatusValue` parameter are used when the addin is not loaded and thus cannot respond to the `QueryStatus` method. If `ContextUIGUIDs` is empty, then the command is enabled until the addin is loaded and can respond to `QueryStatus`.

The VSPackage can receive invocation notification through the [IDTCommandTarget](https://learn.microsoft.com/en-us/dotnet/api/envdte.idtcommandtarget?view=visualstudiosdk-2022) interface. A button can be added by using the [OnConnection](https://learn.microsoft.com/en-us/dotnet/api/extensibility.idtextensibility2.onconnection?view=visualstudiosdk-2022) method of the [IDTExtensibility2](https://learn.microsoft.com/en-us/dotnet/api/extensibility.idtextensibility2?view=visualstudiosdk-2022) interface

## Applies to

| Product | Versions _(Obsolete)_ |
| --- | --- |
| Visual Studio SDK | 2015, 2017, 2019 _(2022)_ |


<!-- ===== END: Commands.AddNamedCommand Method (EnvDTE)  Microsoft Learn.md ===== -->

---



<!-- ===== BEGIN: FAQ Converting Add-ins to VSPackage Extensions - Visual Studio 2015  Microsoft Learn.md ===== -->

---
created: 2026-01-28T20:38:57 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/faq-converting-add-ins-to-vspackage-extensions?view=vs-2015&redirectedfrom=MSDN
author: mijacobs
---

# FAQ: Converting Add-ins to VSPackage Extensions - Visual Studio 2015 | Microsoft Learn

> ## Excerpt
> Note

---
___

#### Share via

___

Note

This article applies to Visual Studio 2015. If you're looking for the latest Visual Studio documentation, see [Visual Studio documentation](https://learn.microsoft.com/en-us/visualstudio/windows). We recommend upgrading to the latest version of Visual Studio. [Download it here](https://visualstudio.microsoft.com/downloads)

Add-ins are now deprecated. To make a new Visual Studio extension, you need to create a VSIX extension. Here are the answers to some frequently asked questions about how to convert a Visual Studio add-in to a VSIX extension.

Warning

Starting in Visual Studio 2015, for C# and Visual Basic projects, you can use the VSIX project and add item templates for menu commands, tool windows, and VSPackages. For more information, see [What's New in the Visual Studio 2015 SDK](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/what-s-new-in-the-visual-studio-2015-sdk?view=vs-2015).

## What software do I need to develop VSIX extensions?

Starting in Visual Studio 2015, you do not install the Visual Studio SDK from the download center. It is included as an optional feature in Visual Studio setup. You can also install the VS SDK later on. For more information, see [Installing the Visual Studio SDK](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/installing-the-visual-studio-sdk?view=vs-2015).

## Where's the extension documentation?

Start with [Starting to Develop Visual Studio Extensions](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/starting-to-develop-visual-studio-extensions?view=vs-2015). Other articles about VSSDK extension development on MSDN are below that one.

## Can I convert my add-in project to a VSIX project?

An add-in project can't be converted directly to a VSIX project because the mechanisms used in VSIX projects are not the same as the ones in add-in projects. The VSIX project template, plus the right project item templates have a lot of code that makes it relatively easy to get up and running as a VSIX extension.

## How do I start developing VSIX extensions?

Here’s how you make a VSIX that has a menu command:

#### To make a VSIX extension that has a menu command

1.  Create a VSIX project. (**File**, **New**, **Project**, or type **project** in the **Quick Launch** window). In the **New Project** dialog box, expand **Visual C# / Extensibility** or **Visual Basic / Extensibility** and select **VSIX Project**.) Name the project **TestExtension** and specify a location for it.
    
2.  Add a **Custom Command** project item template. (Right-click the project node in the **Solution Explorer** and select **Add / New Item**. In the **New Project** dialog for either Visual C# or Visual Basic, select the **Extensibility** node and select **Custom Command**.)
    
3.  Press F5 to build and run the project in debug mode.
    
    A second instance of Visual Studio appears. This second instance is called the experimental instance, and it may not have the same settings as the instance of Visual Studio you're using to write code. The first time you run the experimental instance, you will be asked to sign in to VS Online and specify your theme and profile.
    
    On the **Tools** menu (in the experimental instance) you should see a button named **My Command name**. When you choose this button, a message should appear: **Inside TestVSPackagePackage.MenuItemCallback()**.
    

## How can I run my add-in code in a VSPackage?

Add-in code usually runs in one of two ways:

-   Triggered by a menu command (the code is in the `IDTCommandTarget.Exec` method)
    
-   Automatically on startup (the code is in the `OnConnection` event handler.)
    
    You can do the same things in a VSPackage. Here's how to add some add-in code in the callback method:
    

#### To implement a menu command in a VSPackage

1.  Create a VSPackage that has a menu command. (For more information, see [Creating an Extension with a Menu Command](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/creating-an-extension-with-a-menu-command?view=vs-2015).)
    
2.  Open the file that contains the definition of the VSPackage. (In a C# project, it's _<your project name>_Package.cs.)
    
3.  Add the following `using` statements to the file:
    
    ```
    using EnvDTE;  
    using EnvDTE80;  
    ```
    
4.  Find the `MenuItemCallback` method. Add a call to [GetService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package.getservice) to get the [DTE2](https://learn.microsoft.com/en-us/dotnet/api/envdte80.dte2) object:
    
    ```
    DTE2 dte = (DTE2)GetService(typeof(DTE));  
    ```
    
5.  Add the code that your add-in had in its `IDTCommandTarget.Exec` method. For example, here is some code that adds a new pane to the **Output** window and prints "Some Text" in the new pane.
    
    ```
    private void MenuItemCallback(object sender, EventArgs e)  
    {  
        DTE2 dte = (DTE2) GetService(typeof(DTE));  
        OutputWindow outputWindow = dte.ToolWindows.OutputWindow;  
    
        OutputWindowPane outputWindowPane = outputWindow.OutputWindowPanes.Add("A New Pane");  
        outputWindowPane.OutputString("Some Text");  
    }  
    
    ```
    
6.  Build and run this project. Press F5 or select **Start** on the **Debug** toolbar. In the experimental instance of Visual Studio, the **Tools** menu should have a button named **My Command name**. When you choose this button, the words **Some Text** should appear in an **Output** window pane. (You may have to open the **Output** window.)
    
    You can also have your code run on startup. However, this approach is generally discouraged for VSPackage extensions. If too many extensions try to load when Visual Studio starts, the start time might become noticeably longer. A better practice is to load the VSPackage automatically only when some condition is met (like a solution being opened).
    
    This procedure shows how to run add-in code in a VSPackage that loads automatically when a solution is opened:
    

#### To autoload a VSPackage

1.  Create a VSIX project with a Visual Studio Package project item. (For the steps to do this, see [How do I start developing VSIX extensions?](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/faq-converting-add-ins-to-vspackage-extensions?view=vs-2015#BKMK_StartDeveloping). Just add the **Visual Studio Package** project item instead.) Name the VSIX project **TestAutoload**.
    
2.  Open TestAutoloadPackage.cs. Find the line where the package class is declared:
    
    ```
    public sealed class <name of your package>Package : Package  
    ```
    
3.  Above this line is a set of attributes. Add this attribute:
    
    ```
    [ProvideAutoLoad(UIContextGuids80.SolutionExists)]  
    ```
    
4.  Set a breakpoint in the `Initialize()` method and start debugging (F5).
    
5.  In the experimental instance, open a project. The VSPackage should load, and your breakpoint should be hit.
    
    You can specify other contexts in which to load your VSPackage by using the fields of [UIContextGuids80](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.interop.uicontextguids80). For more information, see [Loading VSPackages](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/loading-vspackages?view=vs-2015).
    

## How can I get the DTE object?

If your add-in doesn't display UI—for example, menu commands, toolbar buttons, or tool windows—you may be able to use your code as-is as long as you get the DTE automation object from the VSPackage. Here's how:

#### To get the DTE object from a VSPackage

1.  In a VSIX project with a Visual Studio Package item template, look for the _<project name>_Package.cs file. This is the class that derives from [Package](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package); it can help you interact with Visual Studio. In this case, you use its [GetService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package.getservice) to get the [DTE2](https://learn.microsoft.com/en-us/dotnet/api/envdte80.dte2) object.
    
2.  Add these `using` statements:
    
    ```
    using EnvDTE;  
    using EnvDTE80;  
    ```
    
3.  Find the `Initialize` method. This method handles the command you specified in the package wizard. Add a call to [GetService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package.getservice) to get the DTE object:
    
    ```
    DTE dte = (DTE)GetService(typeof(DTE));  
    ```
    
    After you have the [DTE](https://learn.microsoft.com/en-us/dotnet/api/envdte.dte) automation object, you can add the rest of your add-in code to the project. If you need the [DTE2](https://learn.microsoft.com/en-us/dotnet/api/envdte80.dte2) object, you can do the same thing.
    

VSPackage extensions use the .vsct file to create most of the menu commands, toolbars, toolbar buttons, and other UI. The **Custom Command** project item template gives you the option to create a command on the **Tools** menu. For more information, see [Creating an Extension with a Menu Command](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/creating-an-extension-with-a-menu-command?view=vs-2015).

For more information about .vsct files, see [How VSPackages Add User Interface Elements](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/internals/how-vspackages-add-user-interface-elements?view=vs-2015). For walkthroughs that show how to use the .vsct file to add menu items, toolbars, and toolbar buttons, see [Extending Menus and Commands](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/extending-menus-and-commands?view=vs-2015).

The Custom Tool Window project item template gives you the option to create a tool window. For more information about this project item template, see [Creating an Extension with a Tool Window](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/creating-an-extension-with-a-tool-window?view=vs-2015). For information about tool windows, see [Extending and Customizing Tool Windows](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/extending-and-customizing-tool-windows?view=vs-2015) and the articles under it, especially [Adding a Tool Window](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/adding-a-tool-window?view=vs-2015).

## How do I manage Visual Studio windows in the VSPackage way?

If your add-in manages Visual Studio windows, the add-in code should work in a VSPackage. For example, this procedure shows how to add code that manages the **Task List** to the `MenuItemCallback` method of the VSPackage.

#### To insert window-management code from an add-in into a VSPackage

1.  Create a VSPackage that has a menu command, as in the [How do I start developing VSIX extensions?](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/faq-converting-add-ins-to-vspackage-extensions?view=vs-2015#BKMK_StartDeveloping) section.
    
2.  Open the file that contains the definition of the VSPackage. (In a C# project, it's _<your project name>_Package.cs.)
    
3.  Add these `using` statements:
    
    ```
    using EnvDTE;  
    using EnvDTE80;  
    ```
    
4.  Find the `MenuItemCallback` method. Add a call to [GetService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package.getservice) to get the [DTE2](https://learn.microsoft.com/en-us/dotnet/api/envdte80.dte2) object:
    
    ```
    DTE2 dte = (DTE2)GetService(typeof(DTE));  
    ```
    
5.  Add the code from your add-in. For example, here is some code that adds new tasks to the **Task List**, lists the number of tasks, and then deletes one task.
    
    ```
    private void MenuItemCallback(object sender, EventArgs e)   
    {  
        DTE2 dte = (DTE2) GetService(typeof(DTE));   
    
        TaskList tl = (TaskList)dte.ToolWindows.TaskList;   
        askItem tlItem;   
    
        // Add a couple of tasks to the Task List.   
        tlItem = tl.TaskItems.Add(" ", " ", "Test task 1.",    
            vsTaskPriority.vsTaskPriorityHigh, vsTaskIcon.vsTaskIconUser,   
            true, "", 10, true, true);  
        tlItem = tl.TaskItems.Add(" ", " ", "Test task 2.",   
            vsTaskPriority.vsTaskPriorityLow, vsTaskIcon.vsTaskIconComment, true, "", 20, true,true);  
    
        // List the total number of task list items after adding the new task items.  
        System.Windows.Forms.MessageBox.Show("Task Item 1 description: "+tl.TaskItems.Item(2).Description);  
        System.Windows.Forms.MessageBox.Show("Total number of task items: "+tl.TaskItems.Count);   
    
        // Remove the second task item. The items list in reverse numeric order.   
        System.Windows.Forms.MessageBox.Show("Deleting the second task item");  
        tl.TaskItems.Item(2).Delete();  
        System.Windows.Forms.MessageBox.Show("Total number of task items: "+tl.TaskItems.Count);   
    }  
    ```
    

## How do I manage projects and solutions in a VSPackage?

If your add-in manages projects and solutions, the add-in code should work in a VSPackage. For example, this procedure shows how to add code that gets the startup project.

1.  Create a VSPackage that has a menu command, as in the [How do I start developing VSIX extensions?](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/faq-converting-add-ins-to-vspackage-extensions?view=vs-2015#BKMK_StartDeveloping) section.
    
2.  Open the file that contains the definition of the VSPackage. (In a C# project, it's _<your project name>_Package.cs.)
    
3.  Add these `using` statements:
    
    ```
    using EnvDTE;  
    using EnvDTE80;  
    ```
    
4.  Find the `MenuItemCallback` method. Add a call to [GetService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package.getservice) to get the [DTE2](https://learn.microsoft.com/en-us/dotnet/api/envdte80.dte2) object:
    
    ```
    DTE2 dte = (DTE2)GetService(typeof(DTE));  
    ```
    
5.  Add the code from your add-in. For example, the following code gets the name of the startup project in a solution. (A multi-project solution must be open when this package runs.)
    
    ```
    private void MenuItemCallback(object sender, EventArgs e)  
    {  
        DTE2 dte = (DTE2) GetService(typeof(DTE));   
    
        SolutionBuild2 sb = (SolutionBuild2)dte.Solution.SolutionBuild;   
        Project startupProj;   
        string msg = "";  
    
        foreach (String item in (Array)sb.StartupProjects)   
        {  
            msg += item;   
        }  
        System.Windows.Forms.MessageBox.Show("Solution startup Project: "+msg);   
        startupProj = dte.Solution.Item(msg);   
        System.Windows.Forms.MessageBox.Show("Full name of solution's startup project: "+"/n"+startupProj.FullName);   
    }  
    ```
    

## How do I set keyboard shortcuts in a VSPackage?

You use the `<KeyBindings>` element of the .vsct file. In the following example, the keyboard shortcut for the command `idCommand1` is Alt+A, and the keyboard shortcut for the command `idCommand2` is Alt+Ctrl+A. Notice the syntax for the key names.

```
<KeyBindings>  
    <KeyBinding guid="MyProjectCmdSet" id="idCommand1" editor="guidVSStd97" key1="A" mod1="ALT" />  
    <KeyBinding guid="MyProjectCmdSet" id="idCommand2" editor="guidVSStd97" key1="A" mod1="CONTROL" mod2="ALT" />  
</KeyBindings>  
```

## How do I handle automation events in a VSPackage?

You handle automation events in a VSPackage in the same way as in your add-in. The following code shows how to handle the `OnItemRenamed` event. (This example assumes that you've already gotten the DTE object.)

```
Events2 dteEvents = (Events2)dte.Events;  
dteEvents.ProjectItemsEvents.ItemRenamed += listener1.OnItemRenamed;   
. . .  
public void OnItemRenamed(EnvDTE.ProjectItem projItem, string oldName)   
{  
    string s = "[Event] Renamed " + oldName + " to " + Path.GetFileName(projItem.get_FileNames(1) + " in project " + projItem.ContainingProject.Name;   
}  
```


<!-- ===== END: FAQ Converting Add-ins to VSPackage Extensions - Visual Studio 2015  Microsoft Learn.md ===== -->

---



<!-- ===== BEGIN: FAQ Converting Add-ins to VSPackage Extensions - Visual Studio 2015  Microsoft Learn(1).md ===== -->

---
created: 2026-01-28T20:39:20 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/faq-converting-add-ins-to-vspackage-extensions?view=vs-2015&redirectedfrom=MSDN
author: mijacobs
---

# FAQ: Converting Add-ins to VSPackage Extensions - Visual Studio 2015 | Microsoft Learn

> ## Excerpt
> Note

---
___

#### Share via

___

Note

This article applies to Visual Studio 2015. If you're looking for the latest Visual Studio documentation, see [Visual Studio documentation](https://learn.microsoft.com/en-us/visualstudio/windows). We recommend upgrading to the latest version of Visual Studio. [Download it here](https://visualstudio.microsoft.com/downloads)

Add-ins are now deprecated. To make a new Visual Studio extension, you need to create a VSIX extension. Here are the answers to some frequently asked questions about how to convert a Visual Studio add-in to a VSIX extension.

Warning

Starting in Visual Studio 2015, for C# and Visual Basic projects, you can use the VSIX project and add item templates for menu commands, tool windows, and VSPackages. For more information, see [What's New in the Visual Studio 2015 SDK](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/what-s-new-in-the-visual-studio-2015-sdk?view=vs-2015).

## What software do I need to develop VSIX extensions?

Starting in Visual Studio 2015, you do not install the Visual Studio SDK from the download center. It is included as an optional feature in Visual Studio setup. You can also install the VS SDK later on. For more information, see [Installing the Visual Studio SDK](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/installing-the-visual-studio-sdk?view=vs-2015).

## Where's the extension documentation?

Start with [Starting to Develop Visual Studio Extensions](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/starting-to-develop-visual-studio-extensions?view=vs-2015). Other articles about VSSDK extension development on MSDN are below that one.

## Can I convert my add-in project to a VSIX project?

An add-in project can't be converted directly to a VSIX project because the mechanisms used in VSIX projects are not the same as the ones in add-in projects. The VSIX project template, plus the right project item templates have a lot of code that makes it relatively easy to get up and running as a VSIX extension.

## How do I start developing VSIX extensions?

Here’s how you make a VSIX that has a menu command:

#### To make a VSIX extension that has a menu command

1.  Create a VSIX project. (**File**, **New**, **Project**, or type **project** in the **Quick Launch** window). In the **New Project** dialog box, expand **Visual C# / Extensibility** or **Visual Basic / Extensibility** and select **VSIX Project**.) Name the project **TestExtension** and specify a location for it.
    
2.  Add a **Custom Command** project item template. (Right-click the project node in the **Solution Explorer** and select **Add / New Item**. In the **New Project** dialog for either Visual C# or Visual Basic, select the **Extensibility** node and select **Custom Command**.)
    
3.  Press F5 to build and run the project in debug mode.
    
    A second instance of Visual Studio appears. This second instance is called the experimental instance, and it may not have the same settings as the instance of Visual Studio you're using to write code. The first time you run the experimental instance, you will be asked to sign in to VS Online and specify your theme and profile.
    
    On the **Tools** menu (in the experimental instance) you should see a button named **My Command name**. When you choose this button, a message should appear: **Inside TestVSPackagePackage.MenuItemCallback()**.
    

## How can I run my add-in code in a VSPackage?

Add-in code usually runs in one of two ways:

-   Triggered by a menu command (the code is in the `IDTCommandTarget.Exec` method)
    
-   Automatically on startup (the code is in the `OnConnection` event handler.)
    
    You can do the same things in a VSPackage. Here's how to add some add-in code in the callback method:
    

#### To implement a menu command in a VSPackage

1.  Create a VSPackage that has a menu command. (For more information, see [Creating an Extension with a Menu Command](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/creating-an-extension-with-a-menu-command?view=vs-2015).)
    
2.  Open the file that contains the definition of the VSPackage. (In a C# project, it's _<your project name>_Package.cs.)
    
3.  Add the following `using` statements to the file:
    
    ```
    using EnvDTE;  
    using EnvDTE80;  
    ```
    
4.  Find the `MenuItemCallback` method. Add a call to [GetService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package.getservice) to get the [DTE2](https://learn.microsoft.com/en-us/dotnet/api/envdte80.dte2) object:
    
    ```
    DTE2 dte = (DTE2)GetService(typeof(DTE));  
    ```
    
5.  Add the code that your add-in had in its `IDTCommandTarget.Exec` method. For example, here is some code that adds a new pane to the **Output** window and prints "Some Text" in the new pane.
    
    ```
    private void MenuItemCallback(object sender, EventArgs e)  
    {  
        DTE2 dte = (DTE2) GetService(typeof(DTE));  
        OutputWindow outputWindow = dte.ToolWindows.OutputWindow;  
    
        OutputWindowPane outputWindowPane = outputWindow.OutputWindowPanes.Add("A New Pane");  
        outputWindowPane.OutputString("Some Text");  
    }  
    
    ```
    
6.  Build and run this project. Press F5 or select **Start** on the **Debug** toolbar. In the experimental instance of Visual Studio, the **Tools** menu should have a button named **My Command name**. When you choose this button, the words **Some Text** should appear in an **Output** window pane. (You may have to open the **Output** window.)
    
    You can also have your code run on startup. However, this approach is generally discouraged for VSPackage extensions. If too many extensions try to load when Visual Studio starts, the start time might become noticeably longer. A better practice is to load the VSPackage automatically only when some condition is met (like a solution being opened).
    
    This procedure shows how to run add-in code in a VSPackage that loads automatically when a solution is opened:
    

#### To autoload a VSPackage

1.  Create a VSIX project with a Visual Studio Package project item. (For the steps to do this, see [How do I start developing VSIX extensions?](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/faq-converting-add-ins-to-vspackage-extensions?view=vs-2015#BKMK_StartDeveloping). Just add the **Visual Studio Package** project item instead.) Name the VSIX project **TestAutoload**.
    
2.  Open TestAutoloadPackage.cs. Find the line where the package class is declared:
    
    ```
    public sealed class <name of your package>Package : Package  
    ```
    
3.  Above this line is a set of attributes. Add this attribute:
    
    ```
    [ProvideAutoLoad(UIContextGuids80.SolutionExists)]  
    ```
    
4.  Set a breakpoint in the `Initialize()` method and start debugging (F5).
    
5.  In the experimental instance, open a project. The VSPackage should load, and your breakpoint should be hit.
    
    You can specify other contexts in which to load your VSPackage by using the fields of [UIContextGuids80](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.interop.uicontextguids80). For more information, see [Loading VSPackages](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/loading-vspackages?view=vs-2015).
    

## How can I get the DTE object?

If your add-in doesn't display UI—for example, menu commands, toolbar buttons, or tool windows—you may be able to use your code as-is as long as you get the DTE automation object from the VSPackage. Here's how:

#### To get the DTE object from a VSPackage

1.  In a VSIX project with a Visual Studio Package item template, look for the _<project name>_Package.cs file. This is the class that derives from [Package](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package); it can help you interact with Visual Studio. In this case, you use its [GetService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package.getservice) to get the [DTE2](https://learn.microsoft.com/en-us/dotnet/api/envdte80.dte2) object.
    
2.  Add these `using` statements:
    
    ```
    using EnvDTE;  
    using EnvDTE80;  
    ```
    
3.  Find the `Initialize` method. This method handles the command you specified in the package wizard. Add a call to [GetService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package.getservice) to get the DTE object:
    
    ```
    DTE dte = (DTE)GetService(typeof(DTE));  
    ```
    
    After you have the [DTE](https://learn.microsoft.com/en-us/dotnet/api/envdte.dte) automation object, you can add the rest of your add-in code to the project. If you need the [DTE2](https://learn.microsoft.com/en-us/dotnet/api/envdte80.dte2) object, you can do the same thing.
    

VSPackage extensions use the .vsct file to create most of the menu commands, toolbars, toolbar buttons, and other UI. The **Custom Command** project item template gives you the option to create a command on the **Tools** menu. For more information, see [Creating an Extension with a Menu Command](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/creating-an-extension-with-a-menu-command?view=vs-2015).

For more information about .vsct files, see [How VSPackages Add User Interface Elements](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/internals/how-vspackages-add-user-interface-elements?view=vs-2015). For walkthroughs that show how to use the .vsct file to add menu items, toolbars, and toolbar buttons, see [Extending Menus and Commands](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/extending-menus-and-commands?view=vs-2015).

The Custom Tool Window project item template gives you the option to create a tool window. For more information about this project item template, see [Creating an Extension with a Tool Window](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/creating-an-extension-with-a-tool-window?view=vs-2015). For information about tool windows, see [Extending and Customizing Tool Windows](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/extending-and-customizing-tool-windows?view=vs-2015) and the articles under it, especially [Adding a Tool Window](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/adding-a-tool-window?view=vs-2015).

## How do I manage Visual Studio windows in the VSPackage way?

If your add-in manages Visual Studio windows, the add-in code should work in a VSPackage. For example, this procedure shows how to add code that manages the **Task List** to the `MenuItemCallback` method of the VSPackage.

#### To insert window-management code from an add-in into a VSPackage

1.  Create a VSPackage that has a menu command, as in the [How do I start developing VSIX extensions?](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/faq-converting-add-ins-to-vspackage-extensions?view=vs-2015#BKMK_StartDeveloping) section.
    
2.  Open the file that contains the definition of the VSPackage. (In a C# project, it's _<your project name>_Package.cs.)
    
3.  Add these `using` statements:
    
    ```
    using EnvDTE;  
    using EnvDTE80;  
    ```
    
4.  Find the `MenuItemCallback` method. Add a call to [GetService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package.getservice) to get the [DTE2](https://learn.microsoft.com/en-us/dotnet/api/envdte80.dte2) object:
    
    ```
    DTE2 dte = (DTE2)GetService(typeof(DTE));  
    ```
    
5.  Add the code from your add-in. For example, here is some code that adds new tasks to the **Task List**, lists the number of tasks, and then deletes one task.
    
    ```
    private void MenuItemCallback(object sender, EventArgs e)   
    {  
        DTE2 dte = (DTE2) GetService(typeof(DTE));   
    
        TaskList tl = (TaskList)dte.ToolWindows.TaskList;   
        askItem tlItem;   
    
        // Add a couple of tasks to the Task List.   
        tlItem = tl.TaskItems.Add(" ", " ", "Test task 1.",    
            vsTaskPriority.vsTaskPriorityHigh, vsTaskIcon.vsTaskIconUser,   
            true, "", 10, true, true);  
        tlItem = tl.TaskItems.Add(" ", " ", "Test task 2.",   
            vsTaskPriority.vsTaskPriorityLow, vsTaskIcon.vsTaskIconComment, true, "", 20, true,true);  
    
        // List the total number of task list items after adding the new task items.  
        System.Windows.Forms.MessageBox.Show("Task Item 1 description: "+tl.TaskItems.Item(2).Description);  
        System.Windows.Forms.MessageBox.Show("Total number of task items: "+tl.TaskItems.Count);   
    
        // Remove the second task item. The items list in reverse numeric order.   
        System.Windows.Forms.MessageBox.Show("Deleting the second task item");  
        tl.TaskItems.Item(2).Delete();  
        System.Windows.Forms.MessageBox.Show("Total number of task items: "+tl.TaskItems.Count);   
    }  
    ```
    

## How do I manage projects and solutions in a VSPackage?

If your add-in manages projects and solutions, the add-in code should work in a VSPackage. For example, this procedure shows how to add code that gets the startup project.

1.  Create a VSPackage that has a menu command, as in the [How do I start developing VSIX extensions?](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/faq-converting-add-ins-to-vspackage-extensions?view=vs-2015#BKMK_StartDeveloping) section.
    
2.  Open the file that contains the definition of the VSPackage. (In a C# project, it's _<your project name>_Package.cs.)
    
3.  Add these `using` statements:
    
    ```
    using EnvDTE;  
    using EnvDTE80;  
    ```
    
4.  Find the `MenuItemCallback` method. Add a call to [GetService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.shell.package.getservice) to get the [DTE2](https://learn.microsoft.com/en-us/dotnet/api/envdte80.dte2) object:
    
    ```
    DTE2 dte = (DTE2)GetService(typeof(DTE));  
    ```
    
5.  Add the code from your add-in. For example, the following code gets the name of the startup project in a solution. (A multi-project solution must be open when this package runs.)
    
    ```
    private void MenuItemCallback(object sender, EventArgs e)  
    {  
        DTE2 dte = (DTE2) GetService(typeof(DTE));   
    
        SolutionBuild2 sb = (SolutionBuild2)dte.Solution.SolutionBuild;   
        Project startupProj;   
        string msg = "";  
    
        foreach (String item in (Array)sb.StartupProjects)   
        {  
            msg += item;   
        }  
        System.Windows.Forms.MessageBox.Show("Solution startup Project: "+msg);   
        startupProj = dte.Solution.Item(msg);   
        System.Windows.Forms.MessageBox.Show("Full name of solution's startup project: "+"/n"+startupProj.FullName);   
    }  
    ```
    

## How do I set keyboard shortcuts in a VSPackage?

You use the `<KeyBindings>` element of the .vsct file. In the following example, the keyboard shortcut for the command `idCommand1` is Alt+A, and the keyboard shortcut for the command `idCommand2` is Alt+Ctrl+A. Notice the syntax for the key names.

```
<KeyBindings>  
    <KeyBinding guid="MyProjectCmdSet" id="idCommand1" editor="guidVSStd97" key1="A" mod1="ALT" />  
    <KeyBinding guid="MyProjectCmdSet" id="idCommand2" editor="guidVSStd97" key1="A" mod1="CONTROL" mod2="ALT" />  
</KeyBindings>  
```

## How do I handle automation events in a VSPackage?

You handle automation events in a VSPackage in the same way as in your add-in. The following code shows how to handle the `OnItemRenamed` event. (This example assumes that you've already gotten the DTE object.)

```
Events2 dteEvents = (Events2)dte.Events;  
dteEvents.ProjectItemsEvents.ItemRenamed += listener1.OnItemRenamed;   
. . .  
public void OnItemRenamed(EnvDTE.ProjectItem projItem, string oldName)   
{  
    string s = "[Event] Renamed " + oldName + " to " + Path.GetFileName(projItem.get_FileNames(1) + " in project " + projItem.ContainingProject.Name;   
}  
```


<!-- ===== END: FAQ Converting Add-ins to VSPackage Extensions - Visual Studio 2015  Microsoft Learn(1).md ===== -->

---



<!-- ===== BEGIN: How to Access Resources in Satellite DLLs  Microsoft Learn.md ===== -->

---
created: 2026-01-28T20:38:37 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/previous-versions/ms165653(v=vs.140)
author: 
---

# How to: Access Resources in Satellite DLLs | Microsoft Learn

> ## Excerpt
> Visual Studio add-ins are deprecated in Visual Studio 2013. You should upgrade your add-ins to VSPackage extensions. For more information about upgrading, see FAQ: Converting Add-ins to VSPackage Extensions.

---
___

#### Share via

___

Visual Studio add-ins are deprecated in Visual Studio 2013. You should upgrade your add-ins to VSPackage extensions. For more information about upgrading, see [FAQ: Converting Add-ins to VSPackage Extensions](https://msdn.microsoft.com/en-us/library/dn246938(v=vs.140)).

Once you have created a satellite DLL and added resources to it (icons, bitmaps, resource strings, and so forth), those resources now become available to your add-ins and other automation projects. The procedure below demonstrates how to do this.

Note

The dialog boxes and menu commands you see might differ from those described in Help depending on your active settings or edition. These procedures were developed with the General Development Settings active. To change your settings, choose **Import** and **ExportSettings** on the **Tools** menu. For more information, see [Customizing Development Settings in Visual Studio](https://learn.microsoft.com/en-us/previous-versions/zbhkx167(v=vs.140)).

### Accessing satellite DLL resources

1.  Open Visual Studio and either load an existing add-in project or create a new one.
    
2.  Add the following code example, compile, and run it.
    

## Example

The following is the general algorithm Visual Studio uses to find a satellite DLL. You can use this code to make sure that the satellite DLL is properly built, in the right location, and has the resource name you expect.

```
static void Main(string[] args)
{
    string path = @"<some path here>";
    System.Reflection.Assembly asm =    
    System.Reflection.Assembly.LoadFrom(path);
    // For enhanced security, use the LoadFrom overload 
    // System.Reflection.Assembly.LoadFrom(path, securityInfo);
    // where securityInfo is an instance of an Evidence object.
    System.Reflection.Assembly assemblyForResources = 
    asm.GetSatelliteAssembly(System.Threading.
    Thread.CurrentThread.CurrentCulture);
    System.IO.Stream stream =    
    assemblyForResources.GetManifestResourceStream
    (assemblyForResources.GetManifestResourceNames()[0]);
    ResourceReader resReader = new ResourceReader(stream);
    foreach (System.Collections.DictionaryEntry entry in resReader)
    {
        System.Windows.Forms.MessageBox.Show(entry.Key.ToString());
    }
}
```

## Compiling the Code

To use this example, create a Visual C# console application, add this code in place of the Main() function, and set the path variable to the path of the add-in assembly (not the path to the satellite DLL). When run, you will see all available resources in the satellite DLL.

## See Also

#### Tasks

[Walkthrough: Creating Managed Satellite DLLs](https://learn.microsoft.com/en-us/previous-versions/e9zazcx5(v=vs.140))


<!-- ===== END: How to Access Resources in Satellite DLLs  Microsoft Learn.md ===== -->

---



<!-- ===== BEGIN: Walkthrough Creating a Wizard  Microsoft Learn.md ===== -->

---
created: 2026-01-28T20:39:12 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/previous-versions/7k3w6w59(v=vs.140)
author: 
---

# Walkthrough: Creating a Wizard | Microsoft Learn

> ## Excerpt
> In Visual Studio 2013, add-ins are deprecated. We recommend that you upgrade your add-ins to VSPackage extensions. For more information about how to upgrade, see FAQ: Converting Add-ins to VSPackage Extensions.

---
___

#### Share via

___

In Visual Studio 2013, add-ins are deprecated. We recommend that you upgrade your add-ins to VSPackage extensions. For more information about how to upgrade, see [FAQ: Converting Add-ins to VSPackage Extensions](https://msdn.microsoft.com/en-us/library/dn246938(v=vs.140)).

Wizards, such as the **Add-in Wizard**, are programs that lead a user through a series of actions to accomplish a complex, repetitive, or difficult task. Windows, for example, uses wizards to connect to network resources, connect to printers, and so forth.

In Visual Studio, wizards generally ask a series of questions that solicit input from a user, and then use the results to generate code. Wizards, however, do not always display a user interface (UI). They can be programmed to invisibly generate code behind the scenes.

There are three different kinds of wizards.

-   **New Project wizards**—As the name suggests, these wizards are used to generate new code for a particular type of project, giving the user a starting point from which to add their own code. This is the most commonly used type of wizard.
    
-   **Add New Item wizards**—These wizards are used to add new items, such as Web forms, text files, HTML pages, XML pages, and so forth, to a project.
    
-   **Custom wizards**—These wizards are not called from a dialog box. Instead they are called directly from add-ins, macros, or other types of code. They may or may not display a UI. In either case, they generate code. This type of wizard is used the least often.
    

Regardless of the kind of wizard, they all have common traits.

-   They are .NET objects that implement the [IDTWizard](https://msdn.microsoft.com/en-us/library/feb3h5ea(v=vs.140)) interface and have an associated method, [Execute](https://msdn.microsoft.com/en-us/library/ehf2zfa2(v=vs.140)), which contains the code you want the wizard to run.
    
-   They all use a .vsz file to display themselves in Visual Studio.
    
-   They all generate code or perform some other task.
    

You can customize the appearance of elements in wizards that you create. Wizards most often consist of one or more windows, or pages. Pages can contain a descriptive image, such as on the top or to the left side of the page, a label description, instructions, and an area in which navigation controls such as **Next** and **Previous** can be placed.

The process for creating wizards in Visual C++ is a bit different from creating standard Visual Studio wizards. For additional information about how to create wizards targeted to Visual C++, see [Designing a Wizard](https://learn.microsoft.com/en-us/previous-versions/96xz4cw2(v=vs.140)) and [Creating a Custom Wizard](https://learn.microsoft.com/en-us/previous-versions/bhceedxx(v=vs.140)).

Note

Your computer might show different names or locations for some of the Visual Studio user interface elements in the following instructions. The Visual Studio edition that you have and the settings that you use determine these elements. For more information, see [Customizing Development Settings in Visual Studio](https://learn.microsoft.com/en-us/previous-versions/zbhkx167(v=vs.140)).

## An Example of a Basic Wizard

![Visual Studio Add In Wizard](https://learn.microsoft.com/en-us/previous-versions/images/7k3w6w59.vxadd-inwizardpanel(vs.140).gif "Visual Studio Add In Wizard")

This picture shows a panel of the **Add-In Wizard**, a new-project type of wizard that leads you through a series of steps to create an add-in. You can customize the appearance of your wizards, but the **Add-In Wizard** is a good example of the style of a standard type of wizard. Completed wizards become available templates in the **New Project** or **Add New Item** dialog box.

The following demonstrates how to create a basic wizard and optionally give it a custom icon.

### To create a basic wizard in Visual Basic and Visual C#

1.  Run Visual Studio as an Administrator. Registering the wizard requires updating the registry, so it needs this privilege.
    
2.  Create a new Class Library project named MyNewWizard.
    
3.  Add references to [EnvDTE](https://msdn.microsoft.com/en-us/library/k3dys0y2(v=vs.140)) and [EnvDTE80](https://msdn.microsoft.com/en-us/library/0e105c68(v=vs.140)) to the project.
    
    To do this, right-click the project and click **Add**, **Reference**. On the .NET tab of the **Reference** dialog box, click EnvDTE and EnvDTE80 and then click **OK**.
    

In the class module, include references to [EnvDTE](https://msdn.microsoft.com/en-us/library/k3dys0y2(v=vs.140)) and [EnvDTE80](https://msdn.microsoft.com/en-us/library/0e105c68(v=vs.140)) and implement the [IDTWizard](https://msdn.microsoft.com/en-us/library/feb3h5ea(v=vs.140)) interface. For this Visual C# example, you must also add a reference to **System.Windows.Forms** and **System.Runtime.InteropServices**.

```
Imports EnvDTE 
Imports EnvDTE80
Public Class Class1
    Implements IDTWizard
```

using System.Runtime.InteropServices;

```
namespace MyNewWizard
{
```

\[ComVisible(true)\]

\[Guid("20184B81-7C38-4E02-A1E3-8D564EEC2D25"),

ProgId("MyNewWizard.Class1")\]

```
    public class Class1 : IDTWizard
    {
    }
}
```

When you add the **Implements** statement to Visual Basic, position the cursor at the end of the line and press enter to automatically create an **Execute** method procedure. For Visual C#, however, you must add the **Execute** procedure manually:

```
public class Class1 : IDTWizard
    {
    public void Execute(object Application,  
        int hwndOwner, ref object[] contextParams,  
        ref object[] customParams,  
        ref EnvDTE.wizardResult retval)
```

1.  Add the code you want the wizard to run to the **Execute** procedure. For this example, we will just add a simple message box.
    
    You should have the following:
    
    ```
    Imports EnvDTE
    Imports EnvDTE80
    
    Public Class Class1
        Implements IDTWizard
    
        Public Sub Execute(ByVal Application As Object, ByVal _
        hwndOwner As Integer, ByRef ContextParams() As Object, ByRef _
        CustomParams() As Object, ByRef retval As EnvDTE.wizardResult) _
        Implements EnvDTE.IDTWizard.Execute
            MsgBox("The wizard is now running.")
        End Sub
    End Class 
    ```
    
    The **Execute** procedure is called when the wizard is started.
    
2.  Right-click your project in **Solution Explorer** and click **Properties** to open the **Project Properties** page, click the **Build** tab, and then check the **Register for COM interop** box at the bottom of the page.
    
3.  In the AssemblyInfo.cs file, find the **ComVisible** attribute and set it to true.
    
4.  Build the project to create the class library .dll by clicking **Build Solution** on the **Build** menu.
    
5.  Create a .vsz text file for the wizard named MyNewWizard.vsz.
    
    To do this, make a copy of an existing .vsz file, such as any of those located at <Visual Studio Install Directory>\\VC#\\CSharpProjectItems\\Windows Forms, and rename it "MyNewWizard.vsz".
    
    A .vsz file is a text file that enables Visual Studio to recognize the wizard and display it in the **New Project** or **Add New Item** dialog box. The Wizard parameter should be set to the progID (Project.Classname) of the project or the GUID. For more information, see [Configuring .Vsz Files to Start Wizards](https://learn.microsoft.com/en-us/previous-versions/b48hhx46(v=vs.140)).
    
6.  Replace the contents of MyNewWizard.vsz with the following:
    
    ```
    VSWizard 7.0
    Wizard=MyNewWizard.Class1
    Param=First Item
    Param=Second Item
    ```
    
7.  Save the new .vsz file in the directory where you want the wizard to appear.
    
    For this example, we want the wizard to appear in the **Add New Item** dialog box for Visual Basic projects, so save the .vsz file in the following directory: <Visual Studio Install Directory>\\VB\\VBProjectItems.
    
8.  Exit Visual Studio and then restart it.
    
    This forces Visual Studio to read the new .vsz file.
    
9.  Create a new Visual Basic project, such as a Windows Application project.
    
10.  Right-click the project, point to **Add**, and then click **New Item**.
    
    You should see your new wizard (MyNewWizard) in the **Add New Items** dialog box.
    
11.  Click the wizard and click the **Add** button.
    
    You see the message, "The wizard is now running."
    

### To display a custom icon for the new wizard

-   Place an icon file with the same base file name as the .dll file but with an .ico extension in the same directory as the wizard file.
    
    For example, if the wizard is named MyNewWizard.dll, name the .ico file MyNewWizard.ico.
    
    \-or-
    
-   If you have created a VSDir file, specify a path to the icon (.ico) file there.
    

## See Also

#### Tasks

[How to: Create an Add-In](https://learn.microsoft.com/en-us/previous-versions/80493a3w(v=vs.140))

#### Reference

[IDTWizard](https://msdn.microsoft.com/en-us/library/feb3h5ea(v=vs.140))

[PAVE Visual Studio Commands and Switches](https://learn.microsoft.com/en-us/previous-versions/kcc7tke7(v=vs.140))

#### Concepts

[Automation Object Model Chart](https://learn.microsoft.com/en-us/previous-versions/za2b25t3(v=vs.140))

[Adding Wizards to the Add Item and New Project Dialog Boxes by Using .Vsdir Files](https://learn.microsoft.com/en-us/previous-versions/2sc7ft4a(v=vs.140))

[Configuring .Vsz Files to Start Wizards](https://learn.microsoft.com/en-us/previous-versions/b48hhx46(v=vs.140))

#### Other Resources

[Creating Add-ins and Wizards](https://learn.microsoft.com/en-us/previous-versions/5abkeks7(v=vs.140))


<!-- ===== END: Walkthrough Creating a Wizard  Microsoft Learn.md ===== -->

---



<!-- ===== BEGIN: Walkthrough Creating Managed Satellite DLLs  Microsoft Learn.md ===== -->

---
created: 2026-01-28T20:38:20 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/previous-versions/e9zazcx5(v=vs.140)?redirectedfrom=MSDN
author: 
---

# Walkthrough: Creating Managed Satellite DLLs | Microsoft Learn

> ## Excerpt
> In vs_dev12, add-ins are deprecated. We recommend that you upgrade your add-ins to VSPackage extensions. For more information about how to upgrade, see FAQ: Converting Add-ins to VSPackage Extensions.

---
___

#### Share via

___

In vs\_dev12, add-ins are deprecated. We recommend that you upgrade your add-ins to VSPackage extensions. For more information about how to upgrade, see [FAQ: Converting Add-ins to VSPackage Extensions](https://msdn.microsoft.com/en-us/library/dn246938(v=vs.140)).

Satellite DLLs are useful for storing resource files, for example, icons, bitmaps, and resource strings, in a centralized location for use in add-ins and other automation projects. Satellite DLLs can be reused by other projects or add-ins. Furthermore, separating the strings and other resources from your add-in makes it easier to make centralized changes or localize the resources into different languages.

Earlier versions of Visual Studio used registry entries for SatelliteDllPath and SatelliteDllName. However, registry entries are now superseded by entries in the .addin registration file. When you require a resource in your project, you load the add-in and Visual Studio queries it for the satellite DLL. Consequently, you do not have to hard-code a resource path. Also, instead of using the #id method to specify a resource ID, you use @resource name (where resource name is the name of your resource, for example, @Icon1 or @String1), The @ symbol tells Visual Studio to look in the satellite DLL for the resource.

## Create Managed Satellite DLLs

The following steps show how to create a satellite DLL that contains icon and string resources, and how to modify an add-in to access those resources. It uses an add-in that has an **About** dialog box, which requires icon and string resources. Typically, if you create an add-in that has an **About** dialog box, a default icon and text are provided. The following steps also show how to replace the default icon and text by using your own.

### To create a managed satellite DLL

1.  On the **File** menu, click **New**, and then click **Project**.
    
2.  In the **New Project** dialog box, expand **Other Project Types** and then select **Extensibility Projects**.
    
3.  In the **Templates** pane, select **Visual Studio Add-in**.
    
4.  Follow the directions in the Visual Studio Add-in Wizard. On the **Choosing 'Help About' Information** page, select **Yes, I would like my Add-in to offer 'About' box information**. Accept the remaining default selections.
    
5.  On the **Project** menu, click **Add Reference**.
    
6.  On the **.NET** tab, click System.Drawing, and then click **OK**.
    
7.  Right-click the add-in project in **Solution Explorer**, click **Add**, and then click **New Item**.
    
8.  Select **Resources File** in the Templates list and click **Add**. Accept its default name (Resources1.resx).
    
    By default, this creates a resource file named Resource1.resx and starts the Visual Studio **Resource Editor**.
    
9.  In Resource1.resx, select **Icons** on the **Strings** list (the left-most button at the top).
    
10.  In the **Add Resource** list, click **Add New Icon**. For now, leave the default name (Icon1.bmp) and click **Add**.
    
    Alternatively, you can select an existing bitmap image for the icon, as long as it is 16 x 16 pixels and either 16 Color or True Color.
    
11.  After the icon opens in the **Icon Editor**, use the tools to modify it. When you are done, close the **Icon Editor** and save your changes.
    
12.  Select **Add New String** on the **Add Resource** list.
    
13.  Click the first box in the **Name** column.
    
    This creates a default string resource named String1.
    
14.  Type Line one in the **Value** box.
    
    This is the value for the first string resource.
    
15.  Create two more string resources, and name them "Line two" and "Line three".
    
16.  Close the **Resource Editor** and save the changes.
    
17.  In **Solution Explorer**, right-click Resource1.resx and then click **Properties**.
    
18.  In the **Properties** window, change **Build Action** from **Embedded Resource** to **None**.
    
    This prevents the resource from being built into the add-in assembly.
    
19.  Build the project.
    
20.  Create the satellite resource DLL. This is done in a two-step process by using ResGen and then AL (Assembly Linker) to build the satellite DLL.
    
    1.  Click **Start**, **All Programs**, **Microsoft Visual Studio 2010**, **Visual Studio Tools**, and then click **Microsoft Visual Studio Command Prompt (2010)**.
        
        This sets certain environment variables so that you can more easily reference Visual Studio tools.
        
    2.  At the command prompt, go to the folder that contains the .resx file and type **Resgen Resource1.resx**.
        
        Resgen is a utility that compiles the specified .resx file into a .resources file. For more information, see [Resgen.exe (Resource File Generator)](https://msdn.microsoft.com/en-us/library/ccec7sz1(v=vs.140)).
        
    3.  At the command prompt, type **AL.exe /embed:Resource1.resources /culture:en-US /out:**Add-In Name**.resources.dll**.
        
        Replace Add-In Name by using the name of your add-in. For example, if your add-in project is named MyAddin, then the **/out:** switch would be **/out:MyAddin.resources.dll**. The **/out:** name must match the name of your project; otherwise, the resource DLL will not be found.
        
        AL.exe (Assembly Linker) converts the specified .resources file into a DLL that you can reference in your add-in. (You can change the **/culture** switch to a language other than English.) For more information, see [Al.exe (Assembly Linker)](https://msdn.microsoft.com/en-us/library/c405shex(v=vs.140)).
        
21.  In File Explorer, browse to the DLL directory of the add-in and create a folder named \\en-US\\ (for English US, because you typed en-US as the culture value in AL.exe).
    
22.  Copy the Add-In Name.resources.dll file to the new \\en-US\\ folder.
    
23.  In File Explorer, browse to the \\Addins\\ directory, typically ..\\Documents and Settings\\user name\\My Documents\\Visual Studio 2010\\Addins\\.
    
24.  Modify the Visual Studio add-in definition file as follows:
    
    1.  Right-click the add-in definition file for your add-in, click **Open With**, and then click **Note Pad**.
        
    2.  Replace the following tags:
        
        ```
            <FriendlyName>@String1</FriendlyName>
            <Description>@String2</Description>
            <AboutBoxDetails>@String3</AboutBoxDetails>
            <AboutIconData>@Icon1</AboutIconData>
        ```
        
        The Friendlyname entry renames your add-in to Line1, which is what you entered for String1 in the Resource1.resx file. The Description in the **About** dialog box now contains "Line2", and the AboutIconData entry matches the icon you created for the **About** dialog box.
        
    3.  Insert .resources before the extension of the assembly name.
        
25.  Rebuild the project and select the add-in in **Add-in Manager**.
    
26.  On the **Help** menu, click **About Microsoft Visual Studio** and select **Line1** (the name of your add-in) in the list.
    
    The custom icon and the three strings that you created are displayed.
    

## See Also

#### Tasks

[How to: Access Resources in Satellite DLLs](https://learn.microsoft.com/en-us/previous-versions/ms165653(v=vs.140))

#### Concepts

[Add-In Registration](https://learn.microsoft.com/en-us/previous-versions/19dax6cz(v=vs.140))


<!-- ===== END: Walkthrough Creating Managed Satellite DLLs  Microsoft Learn.md ===== -->

---

