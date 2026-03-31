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
