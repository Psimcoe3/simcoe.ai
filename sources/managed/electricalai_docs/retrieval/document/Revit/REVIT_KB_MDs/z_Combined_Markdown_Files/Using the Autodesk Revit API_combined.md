


<!-- ===== BEGIN: Help  Using the Autodesk Revit API  Autodesk.md ===== -->

---
created: 2026-01-28T20:17:30 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Welcome_to_the_Revit_Platform_API_User_Manual_html
author: 
---

# Help | Using the Autodesk Revit API | Autodesk

> ## Excerpt
> The Autodesk Revit API Software Development Kit (SDK) is installed from the Tools and Utilities section of the Autodesk Revit installation. In the SDK, there are example files that will help you get a better understanding of the API and its use. Each example file has a sample .addin manifest file with the information that you will need to edit and place into the appropriate folder, which Autodesk Revit will access on launch.

---
## Autodesk Revit SDK and Online Help

The Autodesk Revit API Software Development Kit (SDK) is installed from the Tools and Utilities section of the Autodesk Revit installation. In the SDK, there are example files that will help you get a better understanding of the API and its use. Each example file has a sample .addin manifest file with the information that you will need to edit and place into the appropriate folder, which Autodesk Revit will access on launch.

RevitAPI.chm is the Autodesk Revit API reference documentation help chm file, included with the SDK package in the \\Revit 2018 SDK\\ folder.

**For more information:**

-   [Glossary of Autodesk Revit Terms](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_Glossary_html)
-   [FAQ](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_FAQ_html)

**Resources:**

-   [www.autodesk.com/adn](http://www.autodesk.com/adn) - Autodesk Developer Network home (ADN)
    
-   [www.autodesk.com/developrevit](http://www.autodesk.com/developrevit) - Autodesk Revit development resources
    
-   [http://forums.autodesk.com/t5/Revit-API/bd-p/160](http://forums.autodesk.com/t5/Revit-API/bd-p/160) - Revit API discussion group
    
-   [http://thebuildingcoder.typepad.com/blog/](http://thebuildingcoder.typepad.com/blog/) - The Building Coder, an ADN blog dedicated to Revit coding
    
-   [http://bimapps.typepad.com/](http://bimapps.typepad.com/) - Bim Apps, a blog dedicated to BIM applications


<!-- ===== END: Help  Using the Autodesk Revit API  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Deployment Options  Autodesk.md ===== -->

---
created: 2026-01-28T20:33:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Deployment Options | Autodesk

> ## Excerpt
> The Autodesk Revit API supports in-process DLLs only. This means that your API application will be compiled as a DLL loaded into the Autodesk Revit process.

---
The Autodesk Revit API supports in-process DLLs only. This means that your API application will be compiled as a DLL loaded into the Autodesk Revit process.

The Autodesk Revit API supports single threaded access only. This means that your API application must perform all Autodesk Revit API calls in the main thread (which is called by the Autodesk Revit process at various API entry points), and your API application cannot maintain operations in other threads and expect them to be able to make calls to Autodesk Revit at any time. (For possible exceptions, see the Advanced Topic [External\_Events](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_External_Events_html).)

There are two types of DLLs that you can create with the Autodesk Revit API, External Commands and External Applications.

## External Commands

The Autodesk Revit API enables you to add new commands to the user interface of Autodesk Revit. These commands will appear in the Add-ins tab under the 'External Tools' pulldown, as seen in Figure 1. Through the API, external tool commands have access to the Autodesk Revit database, as well as the currently selected elements.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/HelloWorldCommand.png)Figure 1: External Tool added to Revit

## External Applications

The Autodesk Revit API enables you to also add external applications. These applications are invoked during Autodesk Revit startup and shutdown. They can create new panels in the Add-ins tab, as seen in Figure 2. They can also register handlers that can react to events occurring in the Autodesk Revit user interface.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/HelloWorldRibbonPanel.png)Figure 2: New panels and controls added to Revit

## REX addins

REX (Revit Extensions) is an API framework that lets you build applications for Revit in .NET similar to classes that implement IExternalCommand. REX is meant to give you a more high-level development environment through built-in resources such as:

-   Automatic dialog box creation and display
    
-   Libraries to work with units and geometry
    
-   Built-in command-based architecture to make menu and toolbar development easier.
    
-   A standard mechanism for accessing a reference to the Revit application object.
    
-   Automatic deployment and installation of addins for easy debugging. Please see the "\\Revit 2018 SDK\\REX SDK" folder for more details.


<!-- ===== END: Help  Deployment Options  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Registration of add-ins  Autodesk.md ===== -->

---
created: 2026-01-28T20:33:05 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Registration_of_add_ins_html
author: 
---

# Help | Registration of add-ins | Autodesk

> ## Excerpt
> The Revit API offers the ability to register API applications via a .addin manifest file.

---
The Revit API offers the ability to register API applications via a .addin manifest file.

Manifest files will be read automatically by Revit when they are placed in one of two locations on a user's system:

-   **In a non-user specific location in "application data"**
    
    -   C:\\ProgramData\\Autodesk\\Revit\\Addins\\<version number>\\
-   **In a user specific location in "application data"**
    
    -   C:\\Users\\<user>\\AppData\\Roaming\\Autodesk\\Revit\\Addins\\<version number>\\

All files named .addin in these locations will be read and processed by Revit during startup.

A basic file adding one ExternalCommand looks like this:

| **Code Region: Basic manifest file for an ExternalCommand** |
| --- |
|  |

```
<?xml version="1.0" encoding="utf-16" standalone="no"?>
<RevitAddIns>
  <AddIn Type="Command">
    <Assembly>c:\MyProgram\MyProgram.dll</Assembly>
    <AddInId>76eb700a-2c85-4888-a78d-31429ecae9ed</AddInId>
    <FullClassName>Revit.Samples.SampleCommand</FullClassName>
    <Text>Sample command</Text>
    <VisibilityMode>NotVisibleInFamily</VisibilityMode>
    <VisibilityMode>NotVisibleInMEP</VisibilityMode>
    <AvailabilityClassName>Revit.Samples.SampleAccessibilityCheck </AvailabilityClassName>
  </AddIn>
</RevitAddIns>
```

A basic file adding one ExternalApplication looks like this:

| **Code Region: Basic manifest file for an ExternalApplication** |
| --- |
|  |

```
<?xml version="1.0" encoding="utf-16" standalone="no"?>
<RevitAddIns>
  <AddIn Type="Application">
    <Name>My sample application</Name>
    <Assembly>c:\MyProgram\MyProgram.dll</Assembly>
    <AddInId>604B1052-F742-4951-8576-C261D1993107</AddInId>
    <FullClassName>Revit.Samples.SampleApplication</FullClassName>
  </AddIn>
</RevitAddIns>
```

Multiple AddIn elements may be provided in a single manifest file.

See [Add-in Registration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_Add_in_Registration_html) for more information on the available XML tags for .addin files.


<!-- ===== END: Help  Registration of add-ins  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  External Commands  Autodesk.md ===== -->

---
created: 2026-01-28T20:33:10 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_External_Commands_html
author: 
---

# Help | External Commands | Autodesk

> ## Excerpt
> Technically, an external command is an exposed .NET object that supports the Autodesk.Revit.UI.IExternalCommand interface. Furthermore, there must be a .addin manifest file in the appropriate directory with one entry for each such object in order for Revit to be able to "see" and to use the commands.

---
Technically, an external command is an exposed .NET object that supports the Autodesk.Revit.UI.IExternalCommand interface. Furthermore, there must be a .addin manifest file in the appropriate directory with one entry for each such object in order for Revit to be able to "see" and to use the commands.

## The IExternalCommand Interface

The declaration (VB.NET) of the interface is as follows:

| Code Region: VB.NET IExternalCommand interface |
| --- |
| 
```
Function Execute(ByVal commandData As Autodesk.Revit.UI.ExternalCommandData,
ByRef message As String,
ByVal elements As Autodesk.Revit.DB.ElementSet)
As Result
```

 |

### Parameters

-   commandData : The object passed in this parameter contains information important to the command that is being execute d. This data includes the Autodesk Revit Application object as well as the currently active view.
-   message : The message string can be set to supply a specific message to the user when the command terminates. How this message is displayed is dependent upon the return value of the function. See the remarks section for more details.
-   elements : Initially this is an empty set that can contain Autodesk Revit elements. When the command terminates, the elements within this set may be displayed, based on the return value. See the remarks section for more details.
    
    ### Return value
    

result: The return value can be one of the following:

-   Success : Is returned if the command succeeded as expected without any unhandled error conditions. The external command will appear as an undoable operation in the Autodesk Revit user interface.
-   Cancelled : This value specifies that the user requested that the command be cancelled. Any changes that were made to Autodesk Revit objects during the external commands execution will be undone. A message may be posted, see the Remarks section.
-   Failure : Failure signifies that the external command failed in some manner from which it cannot recover. Any changes made to Autodesk Revit objects during the execution of the external command will be undone. A message will be posted, see the Remarks section.

The message and elements parameters are used if the command was cancelled or failed.

-   Cancelled: If the external command was cancelled and the message parameter was set by the external command then the message is displayed when execution is returned back to Autodesk Revit. If the message parameter was not set then no message is displayed and the command will exit silently.
-   Failed: If the external command failed then the contents of the message parameter will be displayed. If the element set contains Autodesk Revit elements then these elements will be highlighted when the error message is displayed thus giving the developer the ability to show the user the problem elements.
    
    ## Using an Autodesk Revit API External Command
    

1.  User opens/creates a project in Autodesk Revit
2.  User selects the external command from the External Tools pulldown on the Add-ins tab.
3.  The user had the option to select a number of Autodesk Revit elements before invoking the External Tools program. If they did, the program can decide to only perform its function on the selected members.
4.  The API program takes focus from Autodesk Revit and performs the required task. Often a dialog box may be required to obtain user input before the application can complete its work.
5.  Once the add-in tool has completed its function or has been dismissed by the user the program will update the Autodesk Revit model as required and return from the external command, giving focus back to Autodesk Revit.
    
    ## External Command Object Lifetime
    

When no other command or edit modes are active within Autodesk Revit, the registered external command will become enabled. When picked, the command object will be created and the Execute method called. Once this method returns back to Autodesk Revit the command object will be destroyed. Due to this destruction, data cannot persist within the object between command executions. If you wish the data to persist you may use an external file or database to do so. If you wish the data to persist within the Autodesk Revit project you may use the shared parameters mechanism to store this data.


<!-- ===== END: Help  External Commands  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  External Applications  Autodesk.md ===== -->

---
created: 2026-01-28T20:33:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_External_Applications_html
author: 
---

# Help | External Applications | Autodesk

> ## Excerpt
> Technically, an external application is an exposed .NET object that supports the Autodesk.Revit.IExternalApplication interface. Furthermore, there must be a .addin manifest file in the appropriate directory with one entry for each such object in order for Autodesk Revit to be able to load these applications when Autodesk Revit starts.

---
Technically, an external application is an exposed .NET object that supports the Autodesk.Revit.IExternalApplication interface. Furthermore, there must be a .addin manifest file in the appropriate directory with one entry for each such object in order for Autodesk Revit to be able to load these applications when Autodesk Revit starts.

## The IExternalApplication Interface

The declaration ( C#) of the interface is as follows:

| Code Region: IExternalApplication interface |
| --- |
| 
```
Autodesk.Revit.UI.IExternalApplication.Result OnStartup(Autodesk.Revit.UIControlledApplication application)
```

 |
| 

```
Autodesk.Revit.UI.IExternalApplication.Result OnShutdown(Autodesk.Revit.UIControlledApplication application)
```

 |

### Parameters

-   application: The object passed in this parameter contains information important to the commands OnStartup and OnShutdown that are being called. This object provides limited access methods of Autodesk Revit Application, such as VersionName, VersionNumber; and delegates for some events, such as OnDocumentOpened, OnDocumentSaved
    
    ### Return Value
    

result: The return value can be one of the following:

-   Success: Is returned if the external application succeeded as expected without any unhandled error conditions.
-   Failure: Failure signifies that the external application failed in some manner from which it cannot recover.
-   Cancelled: This value specifies that the external application be cancelled.
    
    ## External Application Object Lifetime
    

When Autodesk Revit starts, the external application object will be created and the OnStartup method called. Once this method returns back successfully to Autodesk Revit the external application object will be held during the entire Autodesk Revit session. The OnShutdown method will be called when Autodesk Revit shuts down.


<!-- ===== END: Help  External Applications  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Debugging Your Application in Microsoft Visual Studio  Autodesk.md ===== -->

---
created: 2026-01-28T20:33:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Debugging_Your_Application_in_Microsoft_Visual_Studio_html
author: 
---

# Help | Debugging Your Application in Microsoft Visual Studio | Autodesk

> ## Excerpt
> The following instructions apply to Visual Studio Professional. The relevant option is not available in the Visual Studio Community editions.

---
The following instructions apply to Visual Studio Professional. The relevant option is not available in the Visual Studio Community editions.

There are a few differences between debugging a standalone application (EXE) and an external application (DLL) that needs another program to launch it. To debug an application that is using the Autodesk Revit API it needs to be activated by Autodesk Revit. To do this in the developer environment for debugging you will need to:

1.  Open up the Visual Studio project for the API application. (For example AnalyticalSupportData\_Info.csproj from the Samples folder)
    
2.  From the Project menu select AnalyticalSupportData\_Info Properties
    
    ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/VS1.png)
    
3.  Select the Debug tab on the left
    
4.  Select the "Start external program:" radio button
    
5.  Press the browse button and find the Revit.exe file and press Open
    
    ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/VS2.png)
    
6.  Set some break points in your source code.
    
7.  From Visual Studio, select "Start Debugging". Autodesk Revit will launch.
    
8.  To hit a break point select the option for your program from the External Tools menu. Once the compiler reaches one of your break points it will stop to let you debug your program.


<!-- ===== END: Help  Debugging Your Application in Microsoft Visual Studio  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  The Revit Unit System  Autodesk.md ===== -->

---
created: 2026-01-28T20:33:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_The_Revit_Unit_System_html
author: 
---

# Help | The Revit Unit System | Autodesk

> ## Excerpt
> The Revit Unit System uses the following base units:

---
The Revit Unit System uses the following base units:

| **Base Unit** | **Unit in Revit** | **Unit System** |
| --- | --- | --- |
| Length | Feet (ft) | Imperial |
| Angle | Radian | Metric |
| Mass | Kilogram (kg) | Metric |
| Time | Seconds (s) | Metric |
| Electric Current | Ampere (A) | Metric |
| Temperature | Kelvin (K) | Metric |
| Luminous Intensity | Candela (cd) | Metric |

**Note:** Because Revit stores lengths in feet and other quantities in metric, a derived unit involving length uses a non-standard unit using the Imperial and the Metric systems. For example, force is measured in mass-length per time squared and is stored in kg-ft/s<sup id="GUID-078A40F7-993B-409A-B450-1D3CC548CDED__GUID-DF42C96E-BC65-469A-9980-4A1C0AD20DF2">2</sup>


<!-- ===== END: Help  The Revit Unit System  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Storing and accessing Custom Data for Applications  Autodesk.md ===== -->

---
created: 2026-01-28T20:33:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Storing_and_accessing_Custom_Data_for_Applications_html
author: 
---

# Help | Storing and accessing Custom Data for Applications | Autodesk

> ## Excerpt
> Often programs linked to Autodesk Revit require information that is not available in the Autodesk Revit model database. There are a number of ways for the user to enter such additional information. How and where the information is entered depends on its use:

---
Often programs linked to Autodesk Revit require information that is not available in the Autodesk Revit model database. There are a number of ways for the user to enter such additional information. How and where the information is entered depends on its use:

-   When the information is of a general type and the user will want to see and edit it inside Autodesk Revit, then it should be stored as a visible Project or Shared Parameter.
-   If the information needs to be kept with the Autodesk Revit model as it evolves but does not need to be visible then it can be stored in the Autodesk Revit model as a non-visible Project or Shared Parameter or using Extensible Storage.
-   If the information is specific to a single add-on program, and is too large to practically store within the Autodesk Revit model such as specifications for a multitude of building products subject to change, then the best solution may be to create a concurrent model database that stores the program specific information. In this case it may be useful to use the element UniqueId property for each element as a key for the database, because the element's UniqueId is stable within a model.


<!-- ===== END: Help  Storing and accessing Custom Data for Applications  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Walkthroughs  Autodesk.md ===== -->

---
created: 2026-01-28T20:35:15 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Walkthroughs | Autodesk

> ## Excerpt
> If you are new to the Revit Platform API, the following topics are good starting points to help you understand the product. Walkthroughs provide step-by-step instructions for common scenarios, helping you learn about the product or a particular feature. The following walkthroughs will help you get started using the Revit Platform API:

---
If you are new to the Revit Platform API, the following topics are good starting points to help you understand the product. Walkthroughs provide step-by-step instructions for common scenarios, helping you learn about the product or a particular feature. The following walkthroughs will help you get started using the Revit Platform API:

[Walkthrough: Hello World](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Walkthrough_Hello_World_html) - Illustrates how to create an add-in using the Revit Platform API.

[Walkthrough: Add Hello World Ribbon Panel](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Walkthrough_Add_Hello_World_Ribbon_Panel_html) - Illustrates how to add a custom ribbon panel.

[Walkthrough: Retrieve Selected Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Walkthrough_Retrieve_Selected_Elements_html) - Illustrates how to retrieve selected elements.

[Walkthrough: Retrieve Filtered Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Walkthrough_Retrieve_Filtered_Elements_html) - Illustrates how to retrieve elements based on filter criteria.


<!-- ===== END: Help  Walkthroughs  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Walkthrough Add Hello World Ribbon Panel  Autodesk.md ===== -->

---
created: 2026-01-28T20:35:31 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Walkthrough: Add Hello World Ribbon Panel | Autodesk

> ## Excerpt
> In the Walkthrough: Hello World section you learn how to create an add-in application and invoke it in Revit. You also learn to create a .addin manifest file to register the add-in application as an external tool. Another way to invoke the add-in application in Revit is through a custom ribbon panel.

---
In the Walkthrough: Hello World section you learn how to create an add-in application and invoke it in Revit. You also learn to create a .addin manifest file to register the add-in application as an external tool. Another way to invoke the add-in application in Revit is through a custom ribbon panel.

### Create a New Project

Complete the following steps to create a new project:

1.  Create a C# project in Visual Studio using the Class Library template.
    
2.  Type AddPanel as the project name.
    
3.  Add references to the RevitAPI.dll and RevitAPIUI.dll using the directions in the previous walkthrough, Walkthrough: Hello World.
    
4.  Add the PresentationCore reference:
    
    -   In the Solution Explorer, right-click References to display a context menu.
    -   From the context menu, click Add Reference. The Add Reference dialog box appears.
    -   In the Add Reference dialog box, click the .NET Tab.
    -   From the Component Name list, select PresentationCore.
    -   Click OK to close the dialog box. PresentationCore appears in the Solution Explorer reference tree. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-457989F8-C552-4351-9CD9-E7C94942602F-low.png)**Figure 8: Add Reference**
5.  Add the WindowsBase reference as well as System.Xaml following similar steps as above.
    

### Change the Class Name

To change the class name, complete the following steps:

1.  In the class view window, right-click Class1 to display a context menu.
2.  From the context menu, select Rename and change the class' name to CsAddPanel.
3.  In the Solution Explorer, right-click the Class1.cs file to display a context.
4.  From the context menu, select Rename and change the file's name to CsAddPanel.cs.
5.  Double click CsAddPanel.cs to open it for editing.

### Add Code

The Add Panel project is different from Hello World because it is automatically invoked when Revit runs. Use the IExternalApplication interface for this project. The IExternalApplication interface contains two abstract methods, OnStartup() and OnShutdown(). For more information about IExternalApplication, refer to [Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html).

Add the following code to the file:

#### Code Region 2-5: Adding a ribbon panel

```
using System;
using System.Reflection;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System.Windows.Media.Imaging;

namespace Walkthrough
{
   /// <remarks>
   /// This application's main class. The class must be Public.
   /// </remarks>
   public class CsAddPanel : IExternalApplication
   {
      // Both OnStartup and OnShutdown must be implemented as public method
      public Result OnStartup(UIControlledApplication application)
      {
         // Add a new ribbon panel
         RibbonPanel ribbonPanel = application.CreateRibbonPanel("NewRibbonPanel");

         // Create a push button to trigger a command add it to the ribbon panel.
         string thisAssemblyPath = Assembly.GetExecutingAssembly().Location;
         PushButtonData buttonData = new PushButtonData("cmdHelloWorld",
            "Hello World", thisAssemblyPath, "Walkthrough.HelloWorld");

         PushButton pushButton = ribbonPanel.AddItem(buttonData) as PushButton;

         // Optionally, other properties may be assigned to the button
         // a) tool-tip
         pushButton.ToolTip = "Say hello to the entire world.";

         // b) large bitmap
         Uri uriImage = new Uri(@"D:\Sample\HelloWorld\bin\Debug\39-Globe_32x32.png"");
         BitmapImage largeImage = new BitmapImage(uriImage);
         pushButton.LargeImage = largeImage;

         return Result.Succeeded;
      }

      public Result OnShutdown(UIControlledApplication application)
      {
         // nothing to clean up in this simple case
         return Result.Succeeded;
      }
   }
   /// <remarks>
   /// The "HelloWorld" external command. The class must be Public.
   /// </remarks>
   [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
   public class HelloWorld : IExternalCommand
   {
      // The main Execute method (inherited from IExternalCommand) must be public
      public Autodesk.Revit.UI.Result Execute(ExternalCommandData revit,
          ref string message, ElementSet elements)
      {
         TaskDialog.Show("Revit", "Hello World");
         return Autodesk.Revit.UI.Result.Succeeded;
      }
   }
}
```

### Build the Application

After completing the code, build the application. From the Build menu, click Build Solution. Output from the build appears in the Output window indicating that the project compiled without errors. AddPanel.dll is located in the project output directory.

### Create the .addin manifest file

To invoke the application in Revit, create a manifest file to register it into Revit.

1.  Create a new text file using Notepad.
2.  Add the following text to the file:

#### Code Region 2-6: Creating a .addin file for the external application

```
    <?xml version="1.0" encoding="utf-8" standalone="no"?>
    <RevitAddIns>
      <AddIn Type="Application">
        <Assembly>D:\Sample\AddPanel\AddPanel\bin\Debug\AddPanel.dll</Assembly>
        <AddInId>604b1052-f742-4951-8576-c261d1993108</AddInId>
        <FullClassName>Walkthrough.CsAddPanel</FullClassName>
        <VendorId>NAME</VendorId>
        <VendorDescription>Your Company Information</VendorDescription>
      </AddIn>
    </RevitAddIns>
```

3.  Save the file as HelloWorldRibbon.addin and put it in the following location:
    -   For Windows XP - C:\\Documents and Settings\\All Users\\Application Data\\Autodesk\\Revit\\Addins\\2014\\
    -   For Vista/Windows 7 - C:\\ProgramData\\Autodesk\\Revit\\Addins\\2014\\

Note: The AddPanel.dll file is in the default file folder in a new folder called Debug (D:\\Sample\\HelloWorld\\bin\\Debug\\AddPanel.dll). Use the file path to evaluate Assembly.

Refer to [Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html) for more information about .addin manifest files.

### Debugging

To begin debugging, build the project, and run Revit. A new ribbon panel appears on the Add-Ins tab named NewRibbonPanel and Hello World appears as the only button on the panel, with a large globe image.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-8EBB8680-BCD5-4983-829F-55288BBC16B6-low.png)**Figure 9: Add a new ribbon panel to Revit**

Click Hello World to run the application and display the following dialog box.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-2C537699-4312-459B-A8E4-224F8C7C163A-low.png)**Figure 10: Hello World dialog box**


<!-- ===== END: Help  Walkthrough Add Hello World Ribbon Panel  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Walkthrough Hello World  Autodesk.md ===== -->

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


<!-- ===== END: Help  Walkthrough Hello World  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Walkthrough Retrieve Filtered Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:35:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Walkthrough: Retrieve Filtered Elements | Autodesk

> ## Excerpt
> You can use a filter to select only elements that meet certain criteria. For more information on creating and using element filters, see Element Retrieval.

---
You can use a filter to select only elements that meet certain criteria. For more information on creating and using element filters, see [Element Retrieval](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_Element_Retrieval_html).

This example retrieves all the doors in the document and returns the list of door elements.

<table summary="" id="GUID-5231B53E-DD08-4F05-8BF2-E23E11C314D4__TABLE_1BDED93854BC4A5B9D4795804F23BAE6"><tbody><tr><td><b>Code Region 2-8: Retrieve filtered elements</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> </span><span>CreateLogicAndFilter</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find all door instances in the project by finding all elements that both belong to the door </span><span>
    </span><span>// category and are family instances.</span><span>
    </span><span>ElementClassFilter</span><span> familyInstanceFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>FamilyInstance</span><span>));</span><span>

    </span><span>// Create a category filter for Doors</span><span>
    </span><span>ElementCategoryFilter</span><span> doorsCategoryfilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementCategoryFilter</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Doors</span><span>);</span><span>

    </span><span>// Create a logic And filter for all Door FamilyInstances</span><span>
    </span><span>LogicalAndFilter</span><span> doorInstancesFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>LogicalAndFilter</span><span>(</span><span>familyInstanceFilter</span><span>,</span><span> doorsCategoryfilter</span><span>);</span><span>

    </span><span>// Apply the filter to the elements in the active document</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> doors </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>doorInstancesFilter</span><span>).</span><span>ToElements</span><span>();</span><span>

    </span><span>return</span><span> doors</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Walkthrough Retrieve Filtered Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Walkthrough Retrieve Selected Elements  Autodesk.md ===== -->

---
created: 2026-01-28T20:35:38 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Walkthrough: Retrieve Selected Elements | Autodesk

> ## Excerpt
> This section introduces you to an add-in application that gets selected elements from Revit.

---
This section introduces you to an add-in application that gets selected elements from Revit.

In add-in applications, you can perform a specific operation on a specific element. For example, you can get or change an element's parameter value. Complete the following steps to get a parameter value:

1.  Create a new project and add the references as summarized in the previous walkthroughs.
2.  Use the UIApplication.ActiveUIDocument.Selection.GetElementIds() method to retrieve the selected elements.
3.  Create a .addin file as explained in previous walkthroughs.

GetElementIds() returns a collection of ElementIds of the selected elements. It can be iterated with a foreach loop. Use the Document.GetElement() method to get the Element object for each ElementId in the selection.

The following code is an example of how to retrieve the ids of the selected element.

<table summary="" id="GUID-C67BE1BC-50D6-403C-8458-61BEBADFC6CE__TABLE_302F3DC2772F4788A5FEE2300F6F2C3A"><tbody><tr><td><b>Code Region 2-7: Retrieving selected elements</b></td></tr><tr><td><pre><code><span>[</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>Transaction</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>ReadOnly</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>Document_Selection</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
    </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span>
        </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>try</span><span>
        </span><span>{</span><span>
            </span><span>// Select some elements in Revit before invoking this command</span><span>

            </span><span>// Get the handle of current document.</span><span>
            </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>;</span><span>

            </span><span>// Get the element selection of current document.</span><span>
            </span><span>Selection</span><span> selection </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>;</span><span>
            </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

            </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>==</span><span> selectedIds</span><span>.</span><span>Count</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// If no elements selected.</span><span>
                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"You haven't selected any elements."</span><span>);</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span>
            </span><span>{</span><span>
                </span><span>String</span><span> info </span><span>=</span><span> </span><span>"Ids of selected elements in the document are: "</span><span>;</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
                </span><span>{</span><span>
                    info </span><span>+=</span><span> </span><span>"\n\t"</span><span> </span><span>+</span><span> id</span><span>.</span><span>IntegerValue</span><span>;</span><span>
                </span><span>}</span><span>

                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>info</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span> e</span><span>)</span><span>
        </span><span>{</span><span>
            message </span><span>=</span><span> e</span><span>.</span><span>Message</span><span>;</span><span>
            </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>/// &lt;/ExampleMethod&gt;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

After you get the selected elements, you can get the properties or parameters for the elements. For more information, see [Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_html).


<!-- ===== END: Help  Walkthrough Retrieve Selected Elements  Autodesk.md ===== -->

---

