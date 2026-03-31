---
created: 2026-01-28T20:33:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_External_Applications_html
author: 
---

# Help | External Applications | Autodesk

> ## Excerpt
> Technically, an external application is an exposed .NET object that supports the Autodesk.Revit.IExternalApplication interface. Furthermore, there must be a .addin manifest file in the appropriate directory with one entry for each such object in order for Autodesk Revit to be able to load these applications when Autodesk Revit starts.

---
Technically, an external application is an exposed .NET object that supports the Autodesk.Revit.IExternalApplication interface. Furthermore, there must be a .addin manifest file in the appropriate directory with one entry for each such object in order for Autodesk Revit to be able to load these applications when Autodesk Revit starts.

## The IExternalApplication Interface

The declaration ( C#) of the interface is as follows:

| Code Region: IExternalApplication interface |
| --- |
| 
```
Autodesk.Revit.UI.IExternalApplication.Result OnStartup(Autodesk.Revit.UIControlledApplication application)
```

 |
| 

```
Autodesk.Revit.UI.IExternalApplication.Result OnShutdown(Autodesk.Revit.UIControlledApplication application)
```

 |

### Parameters

-   application: The object passed in this parameter contains information important to the commands OnStartup and OnShutdown that are being called. This object provides limited access methods of Autodesk Revit Application, such as VersionName, VersionNumber; and delegates for some events, such as OnDocumentOpened, OnDocumentSaved
    
    ### Return Value
    

result: The return value can be one of the following:

-   Success: Is returned if the external application succeeded as expected without any unhandled error conditions.
-   Failure: Failure signifies that the external application failed in some manner from which it cannot recover.
-   Cancelled: This value specifies that the external application be cancelled.
    
    ## External Application Object Lifetime
    

When Autodesk Revit starts, the external application object will be created and the OnStartup method called. Once this method returns back successfully to Autodesk Revit the external application object will be held during the entire Autodesk Revit session. The OnShutdown method will be called when Autodesk Revit shuts down.
