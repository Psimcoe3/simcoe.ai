---
created: 2026-01-28T20:41:47 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Application Functions | Autodesk

> ## Excerpt
> Application and UIApplication members provide access to application-wide data and settings as well as the active session of Revit.

---
Application and UIApplication members provide access to application-wide data and settings as well as the active session of Revit.

## Application

The class represents the Autodesk Revit Application, providing access to documents, options and other application wide data and settings.

### Application Version Information

Application properties include VersionBuild, VersionNumber and VersionName. These can be used to provide add-in behavior based on the release and build of Revit, as shown in [How to use Application properties to enforce a correct version for your add-in](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_Application_Functions_How_to_use_Application_properties_to_enforce_a_correct_version_for_your_add_in_html).

#### Application-wide Settings

##### Shared Parameters

Revit uses one shared parameter file at a time. The Application.OpenSharedParameterFile() method accesses the shared parameter file whose path is set in the SharedParametersFilename property. For more details, see [Shared Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_html).

##### Library Content

The GetLibraryPaths() and SetLibraryPaths() methods provide access to the path information identifying where Revit searches for content .

##### Graphical Display

The BackgroundColor property allows read and write of the background color to use for model views in this session. The AllowNavigationDuringRedraw property enables or disables the option to allow view manipulation during redraw. This can be used to optimize performance during a redraw of the model.

#### Document Management

The Application class provides methods to create the following types of documents:

-   Family document
-   Project document
-   Project template

The OpenDocumentFile() method can be used to open any of these document types.

All open documents can be retrieved using the Documents property.

For more details, see [Document and File Management](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_Document_and_File_Management_html).

#### Session Information

Properties such as UserName and methods such as GetRevitServerNetworkHosts() provide read-only access to this session specific information.

#### Login Information

The static IsLoggedIn property checks if the user is logged in from this session to their Autodesk A360 account. If they are logged in, the LoginUserId property will return the user id of the user currently logged in. (The user id will be empty if the user is not logged in.) Unlike the UserName from the section above, the LoginUserId value is not a recognizable value, but an internal id. In conjunction with the Store Entitlement REST API, a publisher of an Autodesk app can verify if the current user has purchased their app from the Autodesk App Store. For more information about Store Entitlement API, please refer to [www.autodesk.com/developapps](http://www.autodesk.com/developapps).

#### Shared Parameter Management

#### Events

The Application class exposes document and application events such as document open and save. Subscribing to these events notifies the application when the events are enabled and acts accordingly. For more details, see [Events](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_Glossary_Events_html) in the [Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html) section.

#### Create

The Create property returns an Object Factory used to create application-wide utility and geometric objects in the Revit Platform API. Create is used when you want to create an object in the Revit application memory rather than your application's memory.

#### Failure Posting and Handling

The FailureDefinitionRegistry, which contains all registered FailureDefinitions is available from the static GetFailureDefinitionRegistry() method. The static method RegisterFailuresProcessor() can be used to register a custom IFailuresProcessor. For more information on posting and handling failures, see [Failure Posting and Handling](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Failure_Posting_and_Handling_html).

#### Disconnect Warnings

The following properties control whether or not to show the graphical warnings for various types of disconnects.

-   ShowGraphicalWarningCableTrayConduitDisconnects
-   ShowGraphicalWarningDuctDisconnects
-   ShowGraphicalWarningElectricalDisconnects
-   ShowGraphicalWarningHangerDisconnects
-   ShowGraphicalWarningPipeDisconnects

### UIApplication

This class represents an active session of the Autodesk Revit user interface, providing access to UI customization methods, events, and the active document.

#### UI Document Management

The UIApplication provides access to the active document using the UIActiveDocument property. Additionally, a Revit document may be opened using the overloaded OpenAndActivateDocument() method. The document will be opened with the default view active. This method may not be called inside a transaction and may only be invoked during an event when no active document is open yet in Revit and the event is not nested inside another event.

#### Add-in Management

The ActiveAddInId property gets the current active external application or external command id, while the LoadedApplications property returns an array of successfully loaded external applications.

#### Ribbon Panel Utility

Use the UIApplication object to add new ribbon panels and controls to Revit.

For more details, see [Ribbon Panel and Controls](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_Ribbon_Panels_and_Controls_html) in the [Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html) section.

#### Extents

The DrawingAreaExtents property returns a rectangle that represents the screen pixel coordinates of drawing area, while the MainWindowExtents property returns the rectangle that represents the screen pixel coordinates of the Revit main window

#### UI Events

The UIApplication class exposes UI related events such as when a dialog box is displayed. Subscribing to these events notifies the application when the events are enabled and acts accordingly. For more details, see [Events](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_Glossary_Events_html) in the [Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html) section.
