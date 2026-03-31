---
created: 2026-01-28T21:17:44 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_User_Inteface_Events_html
author: 
---

# Help | User Inteface Events | Autodesk

> ## Excerpt
> The following table lists user interface events, their type and whether they are available at the application and/or document level:

---
The following table lists user interface events, their type and whether they are available at the application and/or document level:

**Table 54: UI Event Types**

<table summary="" id="GUID-062C0D65-EF26-4341-B1E5-C532AF0767D6__TABLE_4CEFEB89263846C6851A67D24CF2DD5E"><tbody><tr><td><b>Event</b></td><td><b>Type</b></td><td><b>UIApplication</b></td><td><b>ControlledApplication</b></td><td><b>UIDocument</b></td></tr><tr><td>ApplicationClosing</td><td>pre</td><td>X</td><td>&nbsp;</td><td></td></tr><tr><td>ApplicationInitialized</td><td>single</td><td>&nbsp;</td><td>X</td><td>&nbsp;</td></tr><tr><td>DialogBoxShowing</td><td>single</td><td>X</td><td>&nbsp;</td><td></td></tr><tr><td>DisplayingOptionsDialog</td><td>single</td><td>X</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>Idling</td><td>single</td><td>X</td><td>&nbsp;</td><td></td></tr><tr><td>ViewActivating</td><td>pre</td><td>X</td><td>&nbsp;</td><td></td></tr><tr><td>ViewActivated</td><td>post</td><td>X</td><td>&nbsp;</td><td></td></tr></tbody></table>

-   ApplicationClosing - notification when the Revit application is about to be closed
-   ApplicationInitialized - notification after the Revit application has been initialized, after all external applications have been started and the application is ready to work with documents
-   DialogBoxShowing - notification when Revit is showing a dialog or message box
-   DisplayingOptionsDialog - notification when Revit options dialog is displaying
-   Idling - notification when Revit is not in an active tool or transaction
-   ViewActivating - notification when Revit is about to activate a view of the document
-   ViewActivated - notification just after Revit has activated a view of the document
