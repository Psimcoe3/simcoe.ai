---
created: 2026-01-28T21:16:49 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_html
author: 
---

# Help | Dynamic Model Update | Autodesk

> ## Excerpt
> Dynamic model update offers the ability for a Revit API application to modify the Revit model as a reaction to changes happening in the model when those changes are about to be committed at the end of a transaction. Revit API applications can create updaters by implementing the IUpdater interface and registering it with the UpdaterRegistry class. Registering includes specifying what changes in the model should trigger the updater.

---
Dynamic model update offers the ability for a Revit API application to modify the Revit model as a reaction to changes happening in the model when those changes are about to be committed at the end of a transaction. Revit API applications can create updaters by implementing the IUpdater interface and registering it with the UpdaterRegistry class. Registering includes specifying what changes in the model should trigger the updater.

**Pages in this section**

-   [Implementing IUpdater](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Implementing_IUpdater_html)
-   [The Execute method](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_The_Execute_method_html)
-   [Registering Updaters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Registering_Updaters_html)
-   [Exposure to End-User](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Exposure_to_End_User_html)

**Parent page:** [Advanced Topics](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_html)
