---
created: 2026-01-28T21:17:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_html
author: 
---

# Help | Events | Autodesk

> ## Excerpt
> Events are notifications that are triggered on specific actions in the Revit user interface or API workflows. By subscribing to events, an add-in application can be notified when an action is about to happen or has just happened and take some action related to that event. Some events come in pairs around actions, one occurring before the action takes place ("pre" event) and the other happening after the action takes place ("post" event). Events that do not occur in these pre/post pairs are called "single" events.

---
Events are notifications that are triggered on specific actions in the Revit user interface or API workflows. By subscribing to events, an add-in application can be notified when an action is about to happen or has just happened and take some action related to that event. Some events come in pairs around actions, one occurring before the action takes place ("pre" event) and the other happening after the action takes place ("post" event). Events that do not occur in these pre/post pairs are called "single" events.

Revit provides access to events at both the Application level (such as ApplicationClosing or DocumentOpened) and the Document level (such as DocumentClosing and DocumentPrinting). The same application level events available from the Application class are also available from the ControlledApplication class, which represents the Revit application with no access to documents. It is ControlledApplication that is available to add-ins from the OnStartup() and OnShutdown() methods. In terms of subscribing and unsubscribing to events, these classes are interchangeable; subscribing to an event from the ControlledApplication class is the same as subscribing from the Application class.

Events can also be categorized as database (DB) events or user interface (UI) events. DB events are available from the Application and Document classes, while UI events are available from the UIApplication class. (Currently all UI events are at the application level only).

Some events are considered read-only, which means that during their execution the model may not be modified. The fact that an event is read-only is documented in the API help file. It is important to know that even during regular events (i.e. not read-only events), the model may be in a state in which it cannot be modified. The programmer should check the properties Document.IsModifiable and Document.IsReadOnly to determine whether the model may be modified.
