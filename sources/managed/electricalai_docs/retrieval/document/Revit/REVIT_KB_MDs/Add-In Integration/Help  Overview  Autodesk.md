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
