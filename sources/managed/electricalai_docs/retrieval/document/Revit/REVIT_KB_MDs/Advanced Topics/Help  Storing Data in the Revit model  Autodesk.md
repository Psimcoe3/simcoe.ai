---
created: 2026-01-28T21:17:20 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Storing_Data_in_the_Revit_model_html
author: 
---

# Help | Storing Data in the Revit model | Autodesk

> ## Excerpt
> Use shared parameters or extensible storage to store data in the Revit model.

---
Use shared parameters or extensible storage to store data in the Revit model.

The Revit API provides two methods for storing data in the Revit model. The first is using shared parameters. The Revit API gives programmatic access to the same shared parameters feature that is available through the Revit UI. Shared parameters, if defined as visible, will be viewable to the user in an element's property window. Shared parameters can be assigned to many, but not all, categories of elements. For more information, see [Shared Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_html "Shared Parameters are parameter definitions stored in an external text file").

The other option is extensible storage, which allows you to create custom data structures and then assign instances of that data to elements in the model. This data is never visible to the user in the Revit UI, but may be accessible to other third party applications via the Revit API depending on the read/write access assigned to the schema when it is defined. Unlike Shared Parameters, extensible storage is not limited to certain categories of elements. Extensible storage data can be assigned to any object that derives from the base class Element in the Revit model.
