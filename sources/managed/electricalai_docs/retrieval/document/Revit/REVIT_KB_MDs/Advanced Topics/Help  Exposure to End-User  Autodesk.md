---
created: 2026-01-28T21:17:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Exposure_to_End_User_html
author: 
---

# Help | Exposure to End-User | Autodesk

> ## Excerpt
> When updaters work as they should, they are transparent to the user. In some special cases though, Revit will display a warning to the user concerning a 3rd party updater. Such messages will use the value of the GetUpdaterName() method to refer to the updater.

---
When updaters work as they should, they are transparent to the user. In some special cases though, Revit will display a warning to the user concerning a 3<sub id="GUID-EEE24659-C2D4-4925-B756-D15A3696D0F8__GUID-CE4AFA9D-ECF1-42D3-B2DE-4CA9C12B9372">rd</sub> party updater. Such messages will use the value of the GetUpdaterName() method to refer to the updater.

### Updater not installed

If a document is modified by a non-optional updater and later loaded when that updater is not installed, a task dialog similar to the following is displayed:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-301A03BC-C348-483D-980C-30B05831F84B-low.png)**Figure 135: Missing Third Party Updater Warning**

### Updater performs invalid operation

If an updater has an error, such as an unhandled exception, a message similar to the following is displayed giving the user the option to disable the updater:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-D68E0684-0F8A-47D5-9803-61523979E454-low.png)**Figure 136: Updater performed an invalid operation**

If the user selects Cancel, the entire transaction is rolled back. In the Wall Updater example from earlier in this chapter, the newly added wall is removed. If the user selects Disable Updater, the updater is no longer called, but the transaction is not rolled back.

### Infinite loop

In the event that an updater falls into an infinite loop, Revit will notify the user and disable the updater for the duration of the Revit session.

### Two updaters attempt to edit same element

If an updater attempts to edit the same parameter of an element that was updated by another updater in the same transaction, or if an updater attempts to edit the geometry of an element in a way that conflicts with a change made by another updater, the updater is canceled, an error message is displayed and the user is given the option to disable the updater.

### Central document modified by updater not present locally

If the user reloads latest or saves to central with a central file that was modified by an updater that is not installed locally, a task dialog is presented giving them the option to continue or cancel the synchronization. The warning indicates that proceeding may cause problems with the central model when it is used with the third party updater at a later time.
