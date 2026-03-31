---
created: 2026-01-28T20:53:35 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_Transactions_in_Events_html
author: 
---

# Help | Transactions in Events | Autodesk

> ## Excerpt
> Events do not automatically open transactions. Therefore, the document will not be modified during an event unless one of the event's handlers modifies it by making changes inside a transaction. If an event handler opens a transaction it is required that it will also close it (commit it or roll it back), otherwise all changes will be discarded.

---
### Modifying the document during an event

Events do not automatically open transactions. Therefore, the document will not be modified during an event unless one of the event's handlers modifies it by making changes inside a transaction. If an event handler opens a transaction it is required that it will also close it (commit it or roll it back), otherwise all changes will be discarded.

Please be aware that modifying the active document is not permitted during some events (e.g. the DocumentClosing event). If an event handler attempts to make modifications during such an event, an exception will be thrown. The event documentation indicates whether or not the event is read-only.

### DocumentChanged Event

The DocumentChanged event is raised after every transaction gets committed, undone, or redone. This is a read-only event, designed to allow you to keep external data in synch with the state of the Revit database. To update the Revit database in response to changes in elements, use the [Dynamic Model Update](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_html) framework.
