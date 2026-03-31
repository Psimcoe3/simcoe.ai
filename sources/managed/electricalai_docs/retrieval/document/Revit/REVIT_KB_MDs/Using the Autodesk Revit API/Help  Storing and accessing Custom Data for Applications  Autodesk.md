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
