---
created: 2026-01-28T21:17:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Registering_Updaters_html
author: 
---

# Help | Registering Updaters | Autodesk

> ## Excerpt
> Updaters must be registered in order to be notified of changes to the model. The application level UpdaterRegistry class provides the ability to register/unregister and manipulate the options set for Updaters. Updaters may be registered from any API callback and can be registered as application-wide or document-specific, meaning they will only be triggered by changes made to the specified document. In order to use the UpdaterRegistry functionality, the Revit add-in must be registered in a manifest file and the Id returned by UpdaterId.GetAddInId() for any Updater (obtained from GetUpdaterId()) must match the AddInId field in the add-in's manifest file. An add-in cannot add, remove, or modify Updaters that do not belong to it.

---
Updaters must be registered in order to be notified of changes to the model. The application level UpdaterRegistry class provides the ability to register/unregister and manipulate the options set for Updaters. Updaters may be registered from any API callback and can be registered as application-wide or document-specific, meaning they will only be triggered by changes made to the specified document. In order to use the UpdaterRegistry functionality, the Revit add-in must be registered in a manifest file and the Id returned by UpdaterId.GetAddInId() for any Updater (obtained from GetUpdaterId()) must match the AddInId field in the add-in's manifest file. An add-in cannot add, remove, or modify Updaters that do not belong to it.

### Triggers

In addition to calling the UpdaterRegistry.RegisterUpdater() method, Updaters should add one or more update triggers via the AddTrigger() methods. These triggers indicate to the UpdaterRegistry what events should trigger the Updaters Execute() method to run. They can be set application-wide, or can apply to changes made in a specific document. Update triggers are specified by pairing a change scope and a change type.

The change scope is one of two things:

-   An explicit list of element Ids in a document - only changes happening to those elements will trigger the Updater
-   An implicit list of elements communicated via an ElementFilter - every changed element will be run against the filter, and if any pass, the Updater is triggered

There are several options available for change type. ChangeTypes are obtained from static methods on the Element class.

-   Element addition - via Element.GetChangeTypeElementAddition()
-   Element deletion - via Element.GetChangeTypeElementDeletion()
-   Change of element geometry (shape or position) - via Element.GetChangeTypeGeometry()
-   Changing value of a specific parameter - via Element.GetChangeTypeParameter()
-   Any change of element - via Element.GetChangeTypeAny().

Note that geometry changes are triggered due to potentially many causes, like a change of element type, modification of properties and parameters, move and rotate, or changes imposed on the element from other modified elements during regeneration.

Also note that the last option, any change of element, only triggers the Updater for modifications of pre-existing elements, and does not trigger the Updater for newly added or deleted elements. Additionally, when using this trigger for an instance, only certain modifications to its type will trigger the Updater. Changes that affect the instance itself, such as modification of the instance's geometry, will trigger the Updater. However, changes that do not modify the instance directly and do not result in any discernable change to the instance, such as changes to text parameters, will not trigger the Updater for the instance. To trigger based on these changes, the Type must also be included in the trigger's change scope.

### Order of Execution

The primary way that Revit sorts multiple Updaters to execute in the correct order is by looking at the ChangePriority returned by a given Updater. An Updater reporting a priority for a more fundamental set of elements (e.g. GridsLevelsReferencePlanes) will execute prior to Updaters reporting a priority for elements driven by these fundamental elements (e.g. Annotations). Reporting a proper change priority for the elements which your Updater modifies benefits users of your application: Revit is less likely to have to execute the Updater a second time due to changes made by another Updater.

For Updaters which report the same change priority, execution is ordered based on a sorting of UpdaterId. The method UpdaterRegistry.SetExecutionOrder() allows you set the execution order between any two registered Updaters (even updaters registered by other API add-ins) so long as your code knows the ids of the two Updaters.
