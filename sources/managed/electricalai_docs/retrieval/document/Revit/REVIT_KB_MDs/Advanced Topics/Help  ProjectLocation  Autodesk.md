---
created: 2026-01-28T21:19:25 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_ProjectLocation_html
author: 
---

# Help | ProjectLocation | Autodesk

> ## Excerpt
> A project only has one site which is the absolute location on the earth. However, it can have different locations relative to the projects around it. Depending on the coordinates and origins in use, there can be many ProjectLocation objects in one project.

---
A project only has one site which is the absolute location on the earth. However, it can have different locations relative to the projects around it. Depending on the coordinates and origins in use, there can be many ProjectLocation objects in one project.

By default each Revit project contains at least one named location, Internal. It is the active project location. You can retrieve it using the Document.ActiveProjectLocation property. All existing ProjectLocation objects are retrieved using the Document.ProjectLocations property.
