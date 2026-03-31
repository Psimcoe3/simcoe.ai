---
created: 2026-01-28T21:19:51 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Window_Handle_html
author: 
---

# Help | Window Handle | Autodesk

> ## Excerpt
> Two properties allow access to the handle of the Revit main window:

---
Two properties allow access to the handle of the Revit main window:

-   Autodesk.Revit.UI.UIApplication.MainWindowHandle
-   Autodesk.Revit.UI.UIControlledApplication.MainWindowHandle

This handle should be used when displaying modal dialogs and message windows to insure that they are properly parented. Use these properties instead of System.Diagnostics.Process.GetCurrentProcess().MainWindowHandle, which is not a reliable method for retrieving the main window handle.

**Parent page:** [Advanced Topics](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_html)
