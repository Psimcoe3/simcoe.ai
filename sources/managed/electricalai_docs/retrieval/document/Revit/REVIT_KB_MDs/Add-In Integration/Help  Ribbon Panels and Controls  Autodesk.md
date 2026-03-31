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
