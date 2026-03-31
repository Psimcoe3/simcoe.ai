---
created: 2026-01-28T20:35:21 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Walkthrough: Hello World | Autodesk

> ## Excerpt
> Use the Revit Platform API and C# to create a Hello World program using the directions provided. For information about how to create an add-in application using VB.NET, refer to Hello World for VB.NET .

---
Use the Revit Platform API and C# to create a Hello World program using the directions provided. For information about how to create an add-in application using VB.NET, refer to [Hello World for VB.NET](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_Hello_World_for_VB_NET_html) .

The Hello World walkthrough covers the following topics:

-   Create a new project.
-   Add references.
-   Change the class name.
-   Write the code
-   Debug the add-in.

All operations and code in this section were created using Visual Studio 2019.

## Create a New Project

The first step in writing a C# program with Visual Studio is to choose a project type and create a new Class Library.

1.  From the File menu, select New![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ac.menuaro.gif)Project….
2.  In the Installed Templates frame, click Visual C#.
3.  In the right-hand frame, click Class Library (see Figure 1: Add New Project below). This walkthrough assumes that the project location is: C:\\Samples.
4.  In the Name field, type HelloWorld as the project name.
5.  Click OK.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/VSNewProject.png)

**Figure 1: Add New Project**

## Add References

1.  To add the RevitAPI reference:
    
    -   From the View menu select Solution Explorer if the Solution Explorer window is not open.
        
    -   In the Solution Explorer, right-click References to display a context menu.
        
    -   From the context menu, click Add Reference. The Add Reference dialog box appears.
        
    -   In the Add Reference dialog box, click the Browse tab. Locate the folder where Revit is installed and click the RevitAPI.dll. For example, the installed folder location is usually C:\\Program Files\\Autodesk\\Revit 2018\\RevitAPI.dll.
        
    -   Click OK to select the .dll and close the dialog box. RevitAPI appears in the Solution Explorer reference tree.
        
    -   _Note:_ You should always set the Copy Local property of RevitAPI.dll to false for new projects. This saves disk space, and prevents the Visual Studio debugger from getting confused about which copy of the DLL to use. Right-click the RevitAPI.dll, select Properties, and change the Copy Local setting from true (the default) to false.
        
2.  Repeat the steps above for the RevitAPIUI.dll.
    

## Add Code

Add the following code to create the add-in:

<table summary="" id="GUID-8EB25D2A-3CAF-486A-BA8E-C2BEF3DB68F6__TABLE_A5151A07390C46BF924055A2EC26BB66"><tbody><tr><td>Code Region 2-1: Getting Started</td></tr><tr><td><pre><code><span>   </span><span>[</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>Transaction</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>Manual</span><span>)]</span><span>
   </span><span>public</span><span> </span><span>class</span><span> </span><span>Class1</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
   </span><span>{</span><span>
      </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> revit</span><span>,</span><span>
         </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
      </span><span>{</span><span>
         </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Hello World"</span><span>);</span><span>
         </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
      </span><span>}</span><span>
   </span><span>}</span></code></pre></td></tr></tbody></table>

**Tip**: The Visual Studio Intellisense feature can create a skeleton implementation of an interface for you, adding stubs for all the required methods. After you add ":IExternalCommand" after Class1 in the example above, you can select "Implement IExternalCommand" from the Intellisense menu to get the code:![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/VSIntellisense.png)**Figure 2: Using Intellisense to Implement Interface**

Every Revit add-in application must have an entry point class that implements the IExternalCommand interface, and you must implement the Execute() method. The Execute() method is the entry point for the add-in application similar to the Main() method in other programs. The add-in entry point class definition is contained in an assembly. For more details, refer to [Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html).

## Build the Program

After completing the code, you must build the file. From the Build menu, click Build Solution. Output from the build appears in the Output window indicating that the project compiled without errors.

## Create a .addin manifest file

The HelloWorld.dll file appears in the project output directory. If you want to invoke the application in Revit, create a manifest file to register it into Revit.

1.  To create a manifest file, create a new text file in Notepad.
    
2.  Add the following text:
    
    |  |
    | --- |
    | **Code Region 2-2: Creating a .addin manifest file for an external command** |
    
    ```
     <?xml version="1.0" encoding="utf-8" standalone="no"?>
     <RevitAddIns>
             <AddIn Type="Command">
                     <Assembly>C:\Samples\HelloWorld\HelloWorld\bin\Debug\HelloWorld.dll</Assembly>
                     <AddInId>239BD853-36E4-461f-9171-C5ACEDA4E721</AddInId>
                     <FullClassName>HelloWorld.Class1</FullClassName>
                     <Text>HelloWorld</Text> 
                     <VendorId>NAME</VendorId>
                     <VendorDescription>Your Company Information</VendorDescription> 
             </AddIn>
     </RevitAddIns>
    ```
    
3.  Save the file as HelloWorld.addin and put it in the following location:
    
    -   C:\\ProgramData\\Autodesk\\Revit\\Addins{{RelYear}}\\
        
    -   If your application assembly dll is on a network share instead of your local hard drive, you must modify Revit.exe.config to allow .NET assemblies outside your local machine to be loaded. In the "runtime" node in Revit.exe.config, add the element `<loadFromRemoteSources enabled="true"/>` as shown below.
        
        ```
          <runtime>
                  <generatePublisherEvidence enabled="false" />
                  <loadFromRemoteSources enabled="true"/> 
          </runtime>
        ```
        

Refer to [Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html) for more details using manifest files.

## Debug the Add-in

Running a program in Debug mode uses breakpoints to pause the program so that you can examine the state of variables and objects. If there is an error, you can check the variables as the program runs to deduce why the value is not what you might expect.

1.  In the Solution Explorer window, right-click the HelloWorld project to display a context menu.
    
2.  From the context menu, click Properties. The Properties window appears.
    
3.  Click the Debug tab.
    
4.  Under the Start Action section, click Start external program and browse to the Revit.exe file. By default, the file is located at the following path, C:\\Program Files\\Autodesk\\Revit 2018\\Revit.exe.
    
    ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/VS2.png)
    
    **Figure 3: Set debug environment**
    
5.  From the Debug menu, select Toggle Breakpoint (or press F9) to set a breakpoint on the following line.
    
    `TaskDialog.Show("Revit", "Hello World");`
    
6.  Press F5 to start the debug procedure.
    

Test debugging:

-   On the Add-Ins tab, HelloWorld appears in the External Tools menu-button. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/HelloWorldCommand.png)**Figure 4: HelloWorld External Tools command**
    
-   Click HelloWorld to execute the program, activating the breakpoint.
    
-   Press F5 to continue executing the program. The following system message appears. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-960D9FBA-7665-4867-9E29-15B733C19107-low.png)**Figure 5: TaskDialog message**
    

## Troubleshooting

_Q:_ My add-in application will not compile.

_A:_ If an error appears when you compile the sample code, the problem may be with the version of the RevitAPI used to compile the add-in. Delete the old RevitAPI reference and load a new one. For more details, refer to [Walkthrough: Hello World](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Walkthrough_Hello_World_html).

_Q:_ Why is there no Add-Ins tab or why isn't my add-in application displayed under External Tools?

_A:_ In many cases, if an add-in application fails to load, Revit will display an error dialog on startup with information about the failure. For example, if the add-in DLL cannot be found in the location specified in the manifest file, a message similar to the following appears.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-DDC17E45-124F-498A-B54C-70BC64D12C55-low.png)**Figure 6: External Tools Error Message**

In this case, ensure that the .addin file has the correct path to the assembly.

Error messages will also be displayed if the class name specified in FullClassName is not found or does not inherit from IExternalCommand.

However, in some cases, an add-in application may fail to load without any message. Possible causes include:

-   The add-in application is compiled with a different RevitAPI version
-   The manifest file is not found
-   There is a formatting error in the .addin manifest file

_Q:_ Why does my add-in application not work?

_A:_ Even though your add-in application is available under External Tools, it may not work. This is most often caused by an exception in the code.

Revit will display an error dialog with information about the exception when the command fails.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-79F4204F-9BB0-471D-86F2-6E709681001F-low.png)**Figure 7: Unhandled exception in External Command**

This is intended as an aid to debugging your command; commands deployed to users should use try..catch..finally in the example entry method to prevent the exception from being caught by Revit. Here is an example:

<table summary="" id="GUID-8EB25D2A-3CAF-486A-BA8E-C2BEF3DB68F6__TABLE_9DD97EC397A740A5A75072C1DE5006B8"><tbody><tr><td><b>Code Region 2-4: Using try catch in execute:</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>ExternalCommandData</span><span> cdata </span><span>=</span><span> commandData</span><span>;</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span> cdata</span><span>.</span><span>Application</span><span>.</span><span>Application</span><span>;</span><span>

        </span><span>try</span><span>
        </span><span>{</span><span>
                </span><span>// Your code here</span><span>
        </span><span>}</span><span>

        </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span> ex</span><span>)</span><span>
        </span><span>{</span><span>
                message </span><span>=</span><span> ex</span><span>.</span><span>Message</span><span>;</span><span>
                </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>
                </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>   
</span><span>}</span></code></pre></td></tr></tbody></table>
