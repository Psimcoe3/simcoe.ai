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
