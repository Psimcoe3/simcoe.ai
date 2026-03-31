---
created: 2026-01-28T21:17:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_The_Execute_method_html
author: 
---

# Help | The Execute method | Autodesk

> ## Excerpt
> The purpose of the Execute() method is to allow your Updater to react to changes that have been made to the document, and make appropriate related. This method is invoked by Revit at the end of a document transaction in which elements that matched the UpdateTrigger for this Updater were added, changed or deleted. The method may be invoked more than once for the same transaction due to changes made by other Updaters. Updaters are invoked before the DocumentChanged event, so this event will contain changes made by all updaters.

---
The purpose of the Execute() method is to allow your Updater to react to changes that have been made to the document, and make appropriate related. This method is invoked by Revit at the end of a document transaction in which elements that matched the UpdateTrigger for this Updater were added, changed or deleted. The method may be invoked more than once for the same transaction due to changes made by other Updaters. Updaters are invoked before the DocumentChanged event, so this event will contain changes made by all updaters.

All changes to the document made during the invocation of this method will become a part of the invoking transaction, and maintained for undo and redo operations. When implementing this method you may not open any new transactions (an exception will be thrown), but you may use sub-transactions as required.

Although it can be used to also update data outside of the document, such changes will not become part of the original transaction and will not be subject to undo or redo when the original transaction is undone or redone. If you do use this method to modify data outside of the document, you should also subscribe to the DocumentChanged event to update your data when the original transaction is undone or redone.

### Scope of Changes

The Execute() method has an UpdaterData parameter that provides all necessary data needed to perform the update, including the document and information about the changes that triggered the update. Three basic methods (GetAddedElementIds(),GetDeletedElementIds(), and GetModifiedElementIds()) identify the elements that triggered the update. The Updater can also check specifically if a particular change triggered the update by using the IsChangeTriggered() method.

### Forbidden and Cautionary Changes

The following methods may not be called while executing an Updater, because they introduce cross references between elements. (This can result in document corruption when these changes are combined with workset operations). A ForbiddenForDynamicUpdateException will be thrown when an updater attempts to call any of these methods:

-   Autodesk.Revit.DB.ViewSheet.AddView()
-   Autodesk.Revit.DB.Document.LoadFamily(Autodesk.Revit.DB.Document, Autodesk.Revit.DB.IFamilyLoadOptions)
-   AreaReinforcement.Create()
-   PathReinforcement.Create()

In addition to the forbidden methods listed above, other API methods that require documents to be in transaction-free state may not be called either. Such methods include but are not limited to Save(), SaveAs(), Close(), LoadFamily(), etc. Please refer to the documentation of the respective methods for more information.

Calls to the UpdaterRegistry class, such as RegistryUpdater() or AddTrigger(), from within the Execute() method of an updater are also forbidden. Calling any of the UpdaterRegistry methods will throw an exception. The one exception to this rule is the UpdaterRegistry.UnregisterUpdater() method, which may be called during execution of an updater as long as the updater to be unregistered is not the one currently being executed.

Although the following methods are allowed during execution of an Updater, they can also throw ForbiddenForDynamicUpdateException when cross-references between elements are established as a result of the call. One such example could be creating a face wall that intersects with an existing face wall, so those two would have to be joined together. Apply caution when calling these methods from an Updater:

-   Autodesk.Revit.Creation.ItemFactoryBase.NewFamilyInstances2()
-   Autodesk.Revit.Creation.ItemFactoryBase.NewFamilyInstance(Autodesk.Revit.DB.XYZ, Autodesk.Revit.DB.FamilySymbol, Autodesk.Revit.DB.Element,Autodesk.Revit.DB.Structure.StructuralType)
-   Autodesk.Revit.Creation.Document.NewFamilyInstance(Autodesk.Revit.DB.XYZ, Autodesk.Revit.DB.FamilySymbol, Autodesk.Revit.DB.Element, Autodesk.Revit.DB.Level, Autodesk.Revit.DB.Structure.StructuralType)
-   Autodesk.Revit.DB.FaceWall.Create()

It should also be noted that deleting and recreating existing elements should be avoided if modifying them would suffice. While deleting elements may be a simpler solution, it will not only affect Revit's performance, but it will also destroy any references to "recreated" objects from other elements. This could cause the user to lose work they have done to constrain and annotate the elements in question.

### Managing Changes

Updaters need to be able to handle complex issues that may arise from their use, possibly reconciling subsequent changes to an element. Elements modified by an updater may change by the time the updater is next invoked, and those changes may impact information modified by the updater. For example, the element may be explicitly edited by the user, or implicitly edited due to propagated changes triggered by a regeneration.

It is also possible that the same element may be modified by another updater, possibly even within the same transaction. Although explicit changes of exactly the same data is tracked and prohibited, indirect or propagated changes are still possible. Perhaps the most complex case is that an element could be changed by the user and/or the same updater in different versions of the file. After the user reloads the latest or saves to central, the modified target element will be brought from the other file and the updater will need to reconcile changes.

It is also important to realize that when a document synchs with the central file, the ElementId of elements may be affected. If new elements have been added to two versions of the same file and the same ElementId is used in both places, this will be reconciled when the files are synched to the central database. For this reason, when using updaters to cross-reference one element in another element, they should use Element.UniqueId which is guaranteed to be unique.

Another issue to consider is if an updater attaches some data (i.e. as a parameter) to an element, it not only must be sure to maintain that information in the element to which it was added, but also to reconcile data in cases when that element is duplicated via copy/paste or group propagation. For example, if an updater adds a parameter "Total weight of rebar" to a rebar host, that parameter and its value will be copied to the duplicated rebar host even though the rebar itself may be not copied with the host. In this case the updater needs to ensure the parameter value is reset in the newly copied rebar host.
