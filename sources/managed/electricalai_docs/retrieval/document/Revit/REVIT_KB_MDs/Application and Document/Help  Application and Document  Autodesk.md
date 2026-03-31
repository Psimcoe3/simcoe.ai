---
created: 2026-01-28T20:41:34 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Application and Document | Autodesk

> ## Excerpt
> The top level objects in the Revit Platform API are application and document. These are represented by the classes Application, UIApplication, Document and UIDocument.

---
The top level objects in the Revit Platform API are application and document. These are represented by the classes Application, UIApplication, Document and UIDocument.

-   The application object refers to an individual Revit session, providing access to documents, options, and other application-wide data and settings.
    -   Autodesk.Revit.UI.UIApplication - provides access to UI-level interfaces for the application, including the ability to add RibbonPanels to the user interface, and the ability to obtain the active document in the user interface.
    -   Autodesk.Revit.ApplicationServices.Application - provides access to all other application level properties.
-   The document object is a single Revit project file representing a building model. Revit can have multiple projects open and multiple views for one project.
    -   Autodesk.Revit.UI.UIDocument - provides access to UI-level interfaces for the document, such as the contents of the selection and the ability to prompt the user to make selections and pick points
    -   Autodesk.Revit.DB.Document - provides access to all other document level properties
-   If multiple documents are open, the active document is the one whose view is active in the Revit session.

This chapter identifies all Application and Document functions, and then focuses on file management, settings, and units. For more details about the Element class, refer to [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html)s and [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html) and refer to the [Views](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_html) for more details about the view elements.
