---
created: 2026-01-28T21:27:02 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_External_Commands_html
author: 
---

# Help | External Commands | Autodesk

> ## Excerpt
> Technically, an external command is an exposed .NET object that supports the Autodesk.Revit.UI.IExternalCommand interface. Furthermore, there must be a .addin manifest file in the appropriate directory with one entry for each such object in order for Revit to be able to "see" and to use the commands.

---
Technically, an external command is an exposed .NET object that supports the Autodesk.Revit.UI.IExternalCommand interface. Furthermore, there must be a .addin manifest file in the appropriate directory with one entry for each such object in order for Revit to be able to "see" and to use the commands.

## The IExternalCommand Interface

The declaration (VB.NET) of the interface is as follows:

| Code Region: VB.NET IExternalCommand interface |
| --- |
| 
```
Function Execute(ByVal commandData As Autodesk.Revit.UI.ExternalCommandData,
ByRef message As String,
ByVal elements As Autodesk.Revit.DB.ElementSet)
As Result
```

 |

### Parameters

-   commandData : The object passed in this parameter contains information important to the command that is being execute d. This data includes the Autodesk Revit Application object as well as the currently active view.
-   message : The message string can be set to supply a specific message to the user when the command terminates. How this message is displayed is dependent upon the return value of the function. See the remarks section for more details.
-   elements : Initially this is an empty set that can contain Autodesk Revit elements. When the command terminates, the elements within this set may be displayed, based on the return value. See the remarks section for more details.
    
    ### Return value
    

result: The return value can be one of the following:

-   Success : Is returned if the command succeeded as expected without any unhandled error conditions. The external command will appear as an undoable operation in the Autodesk Revit user interface.
-   Cancelled : This value specifies that the user requested that the command be cancelled. Any changes that were made to Autodesk Revit objects during the external commands execution will be undone. A message may be posted, see the Remarks section.
-   Failure : Failure signifies that the external command failed in some manner from which it cannot recover. Any changes made to Autodesk Revit objects during the execution of the external command will be undone. A message will be posted, see the Remarks section.

The message and elements parameters are used if the command was cancelled or failed.

-   Cancelled: If the external command was cancelled and the message parameter was set by the external command then the message is displayed when execution is returned back to Autodesk Revit. If the message parameter was not set then no message is displayed and the command will exit silently.
-   Failed: If the external command failed then the contents of the message parameter will be displayed. If the element set contains Autodesk Revit elements then these elements will be highlighted when the error message is displayed thus giving the developer the ability to show the user the problem elements.
    
    ## Using an Autodesk Revit API External Command
    

1.  User opens/creates a project in Autodesk Revit
2.  User selects the external command from the External Tools pulldown on the Add-ins tab.
3.  The user had the option to select a number of Autodesk Revit elements before invoking the External Tools program. If they did, the program can decide to only perform its function on the selected members.
4.  The API program takes focus from Autodesk Revit and performs the required task. Often a dialog box may be required to obtain user input before the application can complete its work.
5.  Once the add-in tool has completed its function or has been dismissed by the user the program will update the Autodesk Revit model as required and return from the external command, giving focus back to Autodesk Revit.
    
    ## External Command Object Lifetime
    

When no other command or edit modes are active within Autodesk Revit, the registered external command will become enabled. When picked, the command object will be created and the Execute method called. Once this method returns back to Autodesk Revit the command object will be destroyed. Due to this destruction, data cannot persist within the object between command executions. If you wish the data to persist you may use an external file or database to do so. If you wish the data to persist within the Autodesk Revit project you may use the shared parameters mechanism to store this data.
