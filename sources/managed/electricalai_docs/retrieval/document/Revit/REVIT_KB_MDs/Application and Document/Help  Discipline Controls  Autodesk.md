---
created: 2026-01-28T20:42:11 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Discipline Controls | Autodesk

> ## Excerpt
> The properties:

---
The properties:

-   Application.IsArchitectureEnabled
-   Application.IsStructureEnabled
-   Application.IsStructuralAnalysisEnabled
-   Application.IsMassingEnabled
-   Application.IsEnergyAnalysisEnabled
-   Application.IsSystemsEnabled
-   Application.IsMechanicalEnabled
-   Application.IsMechanicalAnalysisEnabled
-   Application.IsElectricalEnabled
-   Application.IsElectricalAnalysisEnabled
-   Application.IsPipingEnabled
-   Application.IsPipingAnalysisEnabled

provide read and modify access to the available disciplines. An application can read the properties to determine when to enable or disable aspects of it's UI.

When a discipline's status is toggled, Revit's UI will be adjusted, and certain operations and features will be enabled or disabled as appropriate. Enabling an analysis mode will only take effect if the corresponding discipline is enabled. For example, enabling mechanical analysis will not take effect unless the mechanical discipline is also enabled.
