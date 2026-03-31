---
created: 2026-01-28T21:20:00 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Worksharing_Overview_html
author: 
---

# Help | Worksharing Overview | Autodesk

> ## Excerpt
> When creating add-ins for Revit, it is important to understand how documents function in a workshared environment. Whether the file is local, central or managed by Revit server affects how changes to the model will impact other users, or whether a model is potentially out of date or has worksets locked by another user.

---
When creating add-ins for Revit, it is important to understand how documents function in a workshared environment. Whether the file is local, central or managed by Revit server affects how changes to the model will impact other users, or whether a model is potentially out of date or has worksets locked by another user.

## Workflow

This is the worksharing workflow from a high level perspective. When the user opens a central model, they get a local copy of the model. When they edit elements, the elements are checked out from the central model so that no one else can edit them. Local changes are only committed to the central model when a Synchronize with Central is performed. Once committed, other users can get the changes by performing a Reload Latest.

## Worksets

Elements are placed in worksets. An entire workset can be checked out so that the user has exclusive editing rights to all the elements in the workset. If new elements are added, they are placed in the active workset in the local model.

Specific worksets can be opened with the model. Only opened worksets are visible, but all elements are available in the model. A workshared model may also be open "detached", in which there is no possibility of updating the central model. In this case, no workset management is required.

## Worksharing types

There are three types of worksharing:

-   **File-based** - The central model is accessible on disk over the network
-   **Server-based** - Revit server manages the central model and possibly locally available accelerators
-   **Cloud-based** - Uses the Revit Cloud Worksharing service to author Revit models in the cloud concurrently with other team members
