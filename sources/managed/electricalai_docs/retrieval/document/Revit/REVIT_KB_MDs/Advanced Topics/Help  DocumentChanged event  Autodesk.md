---
created: 2026-01-28T21:17:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Database_Events_DocumentChanged_event_html
author: 
---

# Help | DocumentChanged event | Autodesk

> ## Excerpt
> The DocumentChanged event is triggered when the Revit document has changed. This event is raised whenever a Revit transaction is either committed, undone or redone. This is a read-only event, designed to allow external data to be kept in synch with the state of the Revit database. To update the Revit database in response to changes in elements, use the IUpdater framework.

---
The DocumentChanged event is triggered when the Revit document has changed. This event is raised whenever a Revit transaction is either committed, undone or redone. This is a read-only event, designed to allow external data to be kept in synch with the state of the Revit database. To update the Revit database in response to changes in elements, use the IUpdater framework.

The DocumentChangedEventArgs class is used by the DocumentChanged event. This class has several methods to get the element Ids of any newly added elements (GetAddElementIds()), deleted elements (GetDeletedElementIds()) or elements that have been modified (GetModifiedElementIds()). The GetAddElementIds() and GetModifiedElementIds() methods have overloads that take an ElementFilter, which makes it easy to detect only changes of interest.
