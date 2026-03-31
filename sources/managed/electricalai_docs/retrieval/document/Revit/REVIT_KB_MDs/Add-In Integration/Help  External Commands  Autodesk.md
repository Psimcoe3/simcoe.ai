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
