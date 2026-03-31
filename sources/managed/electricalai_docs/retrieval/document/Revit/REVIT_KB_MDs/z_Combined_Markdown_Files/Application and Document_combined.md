


<!-- ===== BEGIN: Help  Application and Document  Autodesk.md ===== -->

---
created: 2026-01-28T20:41:34 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Application and Document | Autodesk

> ## Excerpt
> The top level objects in the Revit Platform API are application and document. These are represented by the classes Application, UIApplication, Document and UIDocument.

---
The top level objects in the Revit Platform API are application and document. These are represented by the classes Application, UIApplication, Document and UIDocument.

-   The application object refers to an individual Revit session, providing access to documents, options, and other application-wide data and settings.
    -   Autodesk.Revit.UI.UIApplication - provides access to UI-level interfaces for the application, including the ability to add RibbonPanels to the user interface, and the ability to obtain the active document in the user interface.
    -   Autodesk.Revit.ApplicationServices.Application - provides access to all other application level properties.
-   The document object is a single Revit project file representing a building model. Revit can have multiple projects open and multiple views for one project.
    -   Autodesk.Revit.UI.UIDocument - provides access to UI-level interfaces for the document, such as the contents of the selection and the ability to prompt the user to make selections and pick points
    -   Autodesk.Revit.DB.Document - provides access to all other document level properties
-   If multiple documents are open, the active document is the one whose view is active in the Revit session.

This chapter identifies all Application and Document functions, and then focuses on file management, settings, and units. For more details about the Element class, refer to [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html)s and [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html) and refer to the [Views](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_html) for more details about the view elements.


<!-- ===== END: Help  Application and Document  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Application Functions  Autodesk.md ===== -->

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


<!-- ===== END: Help  Application Functions  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Discipline Controls  Autodesk.md ===== -->

---
created: 2026-01-28T20:42:11 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Discipline Controls | Autodesk

> ## Excerpt
> The properties:

---
The properties:

-   Application.IsArchitectureEnabled
-   Application.IsStructureEnabled
-   Application.IsStructuralAnalysisEnabled
-   Application.IsMassingEnabled
-   Application.IsEnergyAnalysisEnabled
-   Application.IsSystemsEnabled
-   Application.IsMechanicalEnabled
-   Application.IsMechanicalAnalysisEnabled
-   Application.IsElectricalEnabled
-   Application.IsElectricalAnalysisEnabled
-   Application.IsPipingEnabled
-   Application.IsPipingAnalysisEnabled

provide read and modify access to the available disciplines. An application can read the properties to determine when to enable or disable aspects of it's UI.

When a discipline's status is toggled, Revit's UI will be adjusted, and certain operations and features will be enabled or disabled as appropriate. Enabling an analysis mode will only take effect if the corresponding discipline is enabled. For example, enabling mechanical analysis will not take effect unless the mechanical discipline is also enabled.


<!-- ===== END: Help  Discipline Controls  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  How to use Application properties to enforce a correct version for your add-in  Autodesk.md ===== -->

---
created: 2026-01-28T20:42:16 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | How to use Application properties to enforce a correct version for your add-in | Autodesk

> ## Excerpt
> Sometimes you need your add-in to operate only in the presence of a particular Update Release of Revit due to the presence of specific fixes or compatible APIs.

---
Sometimes you need your add-in to operate only in the presence of a particular Update Release of Revit due to the presence of specific fixes or compatible APIs.

Properties of Application make it possible to check for specific versions of Revit. While the property VersionNumber will return a string representing the primary version number, the VersionBuild property will return the internal build number of the Autodesk Revit application.

Another useful property is the Application.SubVersionNumber property. It returns a string representing the major-minor version number for the Revit application such as "2018.0.0". This string is updated by Autodesk for all major and minor updates. Point releases (such as 2018.1.0) may have additional APIs and functionality not available in the initial customer release (such as 2018.0.0). Add-ins written to support initial releases will likely be compatible with subscription updates, but add-ins using new features in subscription updates would not be compatible with the initial releases.

The following sample code demonstrates a technique to determine if the Revit version is any Update Release after the initial known Revit release.

<table summary="" id="GUID-15B6EF8F-7B1D-4930-9F90-CC116411F398__TABLE_235B206931404F52BAE7FF73D21C21C2"><tbody><tr><td><b>Code Region: Use VersionBuild to identify if your add-in is compatible</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetVersionInfo</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app</span><span>)</span><span>
</span><span>{</span><span> 
   </span><span>// 20110309_2315 is the datecode of the initial release of Revit 2012 </span><span>
   </span><span>if</span><span> </span><span>(</span><span>app</span><span>.</span><span>VersionNumber</span><span> </span><span>==</span><span> </span><span>"2012"</span><span> </span><span>&amp;&amp;</span><span> 
       </span><span>String</span><span>.</span><span>Compare</span><span>(</span><span>app</span><span>.</span><span>VersionBuild</span><span>,</span><span> </span><span>"20110309_2315"</span><span>)</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
   </span><span>{</span><span>
       </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Supported version"</span><span>,</span><span> 
                      </span><span>"This application supported in this version."</span><span>);</span><span>
   </span><span>}</span><span>
   </span><span>else</span><span>
   </span><span>{</span><span>
       </span><span>TaskDialog</span><span> dialog </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Unsupported version."</span><span>);</span><span>
       dialog</span><span>.</span><span>MainIcon</span><span> </span><span>=</span><span> </span><span>TaskDialogIcon</span><span>.</span><span>TaskDialogIconWarning</span><span>;</span><span>
       dialog</span><span>.</span><span>MainInstruction</span><span> </span><span>=</span><span> </span><span>"This Revit 2012 application is supported in UR1 and later releases."</span><span>;</span><span>
       dialog</span><span>.</span><span>Show</span><span>();</span><span>
   </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr></tbody></table>


<!-- ===== END: Help  How to use Application properties to enforce a correct version for your add-in  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Document Functions  Autodesk.md ===== -->

---
created: 2026-01-28T20:42:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Document Functions | Autodesk

> ## Excerpt
> Document stores the Revit Elements, manages the data, and updates multiple data views. The Document class mainly provides the following functions.

---
Document stores the Revit Elements, manages the data, and updates multiple data views. The Document class mainly provides the following functions.

## Document

The Document class represents an open Autodesk Revit project.

### Settings Property

The Settings property returns an object that provides access to general components within Revit projects. For more details, see [Settings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_Settings_html).

### Place and Locations

Each project has only one site location that identifies the physical project location on Earth. There can be several project locations for one project. Each location is an offset, or rotation, of the site location. For more details, see [Place and Locations](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_html).

### View Management

A project document can have multiple views. The ActiveView property returns a View object representing the active view. You can filter the elements in the project to retrieve other views. For more details, see [Views](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_html).

### Element Retrieval

The Document object stores elements in the project. Retrieve specific elements by ElementId or UniqueId using the Element property.

For more details, see [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html).

### File Management

Each Document object represents a Revit project file. Document provides the following functions:

-   Retrieve file information such as file path name and project title.
-   Provides Close() and Save() methods to close and save the document.

For more details, see [Document and File management](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_Document_and_File_Management_html).

### Element Management

Revit maintains all Element objects in a project. To create new elements, use the Create property which returns an Object Factory used to create new project element instances in the Revit Platform API, such as FamilyInstance or Group.

The Document class can also be used to delete elements. Use the Delete() method to delete an element in the project. Deleted elements and any dependent elements are not displayed and are removed from the Document. References to deleted elements are invalid and cause an exception. For more details, see [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html).

### Events

Events are raised on certain actions, such as when you save a project using Save or Save As. To capture the events and respond in the application, you must register the event handlers. For more details, see [Events](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_Glossary_Events_html).

### Document Status

Several properties provide information on the status of the document:

-   IsModifiable - whether the document may currently be modified (meaning that is there is an active transaction in the document and changes are not temporarily blocked by anything else)
-   IsModified - whether the document was changed since it was opened or saved
-   IsReadOnly - if true, the document is currently read-only and cannot be modified
-   IsReadOnlyFile - whether the document was opened in read-only mode
-   IsFamilyDocument - whether the document is a family document
-   IsWorkshared - whether worksets have been enabled in the document

### Others

Document also provides other functions:

-   ParameterBindings Property - Mapping between parameter definitions and categories. For more details, see [Shared Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_html).
-   ReactionsAreUpToDate Property - Reports whether the reactionary loads changed. For more details, see [Loads](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Loads_html).
-   Default Types - Access to the default types for family and non-family elements. For more details, see [Default Types](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_Document_Functions_Default_Types_html).

## UIDocument

The UIDocument class represents an Autodesk Revit project opened in the Revit user interface.

### Element Retrieval in UIDocument

Retrieve selected elements using the Selection property in UIDocument. This property returns an object representing the active selection containing the selected project elements. It also provides UI interaction methods to pick objects in the Revit model.

For more details, see [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html).

### Element Display

The ShowElements() method uses zoom to fit to focus in on one more elements.

### View Management in UIDocument

The UIDocument class can be used to refresh the active view in the active document by calling the RefreshActiveView() method. The ActiveView property can be used to retrieve or set the active view for the document. Changing the active view has some restrictions. It can only be used in an active document, which must not be in read-only state and must not be inside a transaction. Additionally, the active view may not be changed during the ViewActivating or ViewActivated event, or during any pre-action event, such as DocumentSaving, DocumentClosing, or other similar events.

The UIDocument.ActiveGraphicalView property retrieves the active graphical view for the document. Unlike UIDocument.ActiveView, this property will never return auxiliary views like the Project Browser or System Browser if the user has happened to make a selection in one of those views.

The UIDocument can also be used to get a list of all open view windows in the Revit user interface. The GetOpenUIViews method returns a list of UIViews which contain data about the view windows in the Revit user interface.


<!-- ===== END: Help  Document Functions  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Default Types  Autodesk.md ===== -->

---
created: 2026-01-28T20:42:31 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Default Types | Autodesk

> ## Excerpt
> Revit has a default type for different categories. This default type is shown in the Revit User Interface when the related tool is invoked to create an element of this category. The Revit API exposes the default type for both family and non-family types via the Document class.

---
Revit has a default type for different categories. This default type is shown in the Revit User Interface when the related tool is invoked to create an element of this category. The Revit API exposes the default type for both family and non-family types via the Document class.

## Family Types

The document members listed in the table below provide access to the default type for a given family category id

| Document Method | Description |
| --- | --- |
| GetDefaultFamilyTypeId() | Gets the default family type id associated to the given family category id. |
| SetDefaultFamilyTypeId() | Sets the default family type id associated to the given family category id. |
| IsDefaultFamilyTypeIdValid() | Checks whether the family type id is valid to set as default for the given family category id. |

Additionally, given an ElementType, the ElementType.IsValidDefaultFamilyType() identifies if it is a valid default family type for the given family category id.

The example below demonstrates how to get the default family type Id for the structural column category. It then gets the family symbol for the default type and assigns it to a given column.

| Code Region: Get default family type id |
| --- |
| 
```
private void AssignDefaultTypeToColumn(Document document, FamilyInstance column)
{
    ElementId defaultTypeId = document.GetDefaultFamilyTypeId(new ElementId(BuiltInCategory.OST_StructuralColumns));

    if (defaultTypeId != ElementId.InvalidElementId)
    {
        FamilySymbol defaultType = document.GetElement(defaultTypeId) as FamilySymbol;
        if (defaultType != null)
        {
            column.Symbol = defaultType;
        }
    }
}
```

 |

The next example sets the default type for the doors category from a given door, after first checking that it is a valid default family type id.

| Code Region: Set default family type id |
| --- |
| 
```
private void SetDefaultTypeFromDoor(Document document, FamilyInstance door)
{
    ElementId doorCategoryId = new ElementId(BuiltInCategory.OST_Doors);

    // It is necessary to test the type suitability to be a default family type, for not every type can be set as default. 
    // Trying to set a non-qualifying default type will cause an exception
    if (door.Symbol.IsValidDefaultFamilyType(doorCategoryId))
    {
        document.SetDefaultFamilyTypeId(doorCategoryId, door.Symbol.Id);
    }
}
```

 |

## Non-family Types

The document members in the table below provide access to the default types for non-Family element types.

| Document Method | Description |
| --- | --- |
| GetDefaultElementTypeId() | Gets the default element type id for a given non-Family element type. |
| SetDefaultElementTypeId() | Sets the default element type id for a given non-Family element type. |
| IsDefaultElementTypeIdValid() | Checks whether the element type id is valid for a given non-Family element type. |

The example below checks whether a given wall is using the default element type for wall types.

| Code Region: Get default element type id |
| --- |
| 
```
private bool IsWallUsingDefaultType(Document document, Wall wall)
{
    ElementId defaultElementTypeId = document.GetDefaultElementTypeId(ElementTypeGroup.WallType);
    return (wall.WallType.Id == defaultElementTypeId);
}
```

 |


<!-- ===== END: Help  Default Types  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Document and File Management  Autodesk.md ===== -->

---
created: 2026-01-28T20:42:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Document and File Management | Autodesk

> ## Excerpt
> Document and file management make it easy to create and find your documents. For information about cloud-based Revit files, see Cloud Models.

---
Document and file management make it easy to create and find your documents. For information about cloud-based Revit files, see [Cloud Models](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_CloudFiles_html).

### Document Retrieval

The Application class maintains all documents. As previously mentioned, you can open more than one document in a session. The active document is retrieved using the UIApplication class property, ActiveUIDocument.

All open documents, including the active document, are retrieved using the Application class Documents property. The property returns a set containing all open documents in the Revit session.

### Document File Information

The Document class provides two properties for each corresponding file, PathName, and Title.

-   PathName returns the document's fully qualified file path. The PathName returns an empty string if the project has not been saved since it was created.
-   Title is the project title, which is usually derived from the project filename. The returned value varies based on your system settings.

### Basic File Info

BasicFileInfo provides fast access to basic information about a Revit file, including worksharing status, Revit version, username and central path. This is done without fully opening the file.

```
static BasicFileInfo.Extract(string file)
```

Returns a BasicFileInfo object whose properties provide information about the file.

Extract is not forward-compatible, meaning that Calling Extract from a version of Revit prior to Revit 2019 will result in an exception if it is called on a Revit 2019 or later file. This may occur again with future versions of Revit.

### Open a Document

The Application class provides an overloaded method to open an existing project file:

**Table 3: Open Document in API**

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_626DB724E12F4AF7A6D5514683F939F4"><tbody><tr><td><b>Method</b></td><td><b>Event</b></td></tr><tr><td><p><code>Document OpenDocumentFile(string filename)</code></p><p><code>Document OpenDocumentFile(ModelPath modelPath, OpenOptions openOptions)</code></p><p><code>Document OpenDocumentFile(ModelPath modelPath, OpenOptions openOptions, IOpenFromCloudCallback openFromCloudCallback)</code></p></td><td>DocumentOpened</td></tr></tbody></table>

When you specify a string with a fully qualified file path, Revit opens the file and creates a Document instance. Use this method to open a file on other computers by assigning the files Universal Naming Conversion (UNC) name to this method.

The file can be a project file with the extension .rvt, a family file with the extension .rfa, or a template file with the extension .rte.

The second overload takes a path to the model as a ModelPath rather than a string and the OpenOptions parameter offers options for opening the file, such as the ability to detach the opened document from central if applicable, as well as options related to worksharing. For more information about opening a workshared document, see [Opening a Workshared Document](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Opening_a_Workshared_Document_html).

These methods throw specific documented exceptions in the event of a failure. Exceptions fall into 4 main categories.

**Table 4: Types of exceptions thrown**

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_164EE052B85441D78583C6C1043B1088"><tbody><tr><td><b>Type</b></td><td><b>Example</b></td></tr><tr><td>Disk errors</td><td>File does not exist or is wrong version</td></tr><tr><td>Resource errors</td><td>Not enough memory or disk space to open file</td></tr><tr><td>Central model file errors</td><td>File is locked or corrupt</td></tr><tr><td>Central model/server errors</td><td>Network communication error with server</td></tr></tbody></table>

If the document is opened successfully, the DocumentOpened event is raised.

#### Create a Document

Create new documents using the Application methods in the following table.

**Table 5: Create Document in the API**

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_FB13876B60BE4EFEA107B82CDF114FED"><tbody><tr><td><b>Method</b></td><td><b>Event</b></td></tr><tr><td><p><code>Document NewProjectDocument(string templateFileName);</code></p></td><td>DocumentCreated</td></tr><tr><td><p><code>Document NewProjectDocument(UnitSystem unitSystem);</code></p></td><td>DocumentCreated</td></tr><tr><td><p><code>Document NewFamilyDocument(string templateFileName);</code></p></td><td>DocumentCreated</td></tr><tr><td><p><code>Document NewProjectTemplateDocument(string templateFilename);</code></p></td><td>DocumentCreated</td></tr></tbody></table>

For the methods that require a template file name as a parameter, the created document is returned based on the template file. NewProjectDocument(UnitSystem)creates a new imperial or metric project document without a specified template.

#### Save and Close a Document

The Document class provides methods to save or close instances.

**Table 6: Save and Close Document in API**

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_04DB3D7B63204912B4ABA9E24CFD3CF1"><tbody><tr><td><b>Method</b></td><td><b>Event</b></td></tr><tr><td>Save()</td><td>DocumentSaved</td></tr><tr><td>SaveAs()</td><td>DocumentSavedAs</td></tr><tr><td>Close()</td><td>DocumentClosed</td></tr></tbody></table>

Save() has 2 overloads, one with no arguments and one with a SaveOptions argument that can specify whether to force the OS to delete all dead data from the file on disk. If the file has not been previously saved, SaveAs() must be called instead.

SaveAs() has 3 overloads. One overload takes only the filename as an argument and an exception will be thrown if another file exists with the given filename. The other 2 overloads takes a filename as an argument (in the form of a ModelPath in one case) as well as a second SaveAsOptions argument that can be used to specify whether to overwrite an existing file, if it exists. SaveAsOptions can also be used to specify other relevant options such as whether to remove dead data on disk related to the file and worksharing options.

Save() and SaveAs() throw specific documented exceptions in the same 4 categories as when opening a document and listed in Table 4 above.

Close() has two overloads. One takes a Boolean argument that indicates whether to save the file before closing it. The second overload takes no arguments and if the document was modified, the user will be asked if they want to save the file before closing. This method will throw an exception if the document's path name is not already set or if the saving target file is read-only.

Note: The Close() method does not affect the active document or raise the DocumentClosed event, because the document is used by an external application. You can only call this method on non-active documents.

The UIDocument class also provides methods to save and close instances.

**Table 7: Save and Close UIDocument in API**

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_1443F9F4594F424D8C82A53F1A6C4911"><tbody><tr><td><b>Method</b></td><td><b>Event</b></td></tr><tr><td>SaveAndClose()</td><td>DocumentSaved, DocumentClosed</td></tr><tr><td>SaveAs()</td><td>DocumentSavedAs</td></tr></tbody></table>

SaveAndClose() closes the document after saving it. If the document's path name has not been set the "Save As" dialog will be shown to the Revit user to set its name and location.

The SaveAs() method saves the document to a file name and path obtained from the Revit user via the "Save As" dialog.

#### Document Preview

The DocumentPreviewSettings class can be obtained from the Document and contains the settings related to the saving of preview images for a given document.

<table summary="" id="GUID-5282B7DB-E7A7-465B-A925-53BBBC3CC8D7__TABLE_C7DE262D8D244EDBB1BFC7519FFA17E5"><tbody><tr><td><b>Code Region: Document Preview</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SaveActiveViewWithPreview</span><span>(</span><span>UIApplication</span><span> application</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the handle of current document.</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document </span><span>=</span><span> application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>// Get the document's preview settings</span><span>
    </span><span>DocumentPreviewSettings</span><span> settings </span><span>=</span><span> document</span><span>.</span><span>GetDocumentPreviewSettings</span><span>();</span><span>

    </span><span>// Find a candidate 3D view</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>View3D</span><span>));</span><span>

    </span><span>Func</span><span>&lt;</span><span>View3D</span><span>,</span><span> </span><span>bool</span><span>&gt;</span><span> isValidForPreview </span><span>=</span><span> v </span><span>=&gt;</span><span> settings</span><span>.</span><span>IsViewIdValidForPreview</span><span>(</span><span>v</span><span>.</span><span>Id</span><span>);</span><span>

    </span><span>View3D</span><span> viewForPreview </span><span>=</span><span> collector</span><span>.</span><span>OfType</span><span>&lt;</span><span>View3D</span><span>&gt;().</span><span>First</span><span>&lt;</span><span>View3D</span><span>&gt;(</span><span>isValidForPreview</span><span>);</span><span>

    </span><span>// Set the preview settings</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> setTransaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Set preview view id"</span><span>))</span><span>
    </span><span>{</span><span>
        setTransaction</span><span>.</span><span>Start</span><span>();</span><span>
        settings</span><span>.</span><span>PreviewViewId</span><span> </span><span>=</span><span> viewForPreview</span><span>.</span><span>Id</span><span>;</span><span>
        setTransaction</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>// Save the document</span><span>
    document</span><span>.</span><span>Save</span><span>();</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>

#### Load Family

The Document class provides you with the ability to load an entire family and all of its symbols into the project. Because loading an entire family can take a long time and a lot of memory, the Document class provides a similar method, LoadFamilySymbol() to load only specified symbols.

For more details, see [Family](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Family_html).


<!-- ===== END: Help  Document and File Management  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  ForgeTypeId  Autodesk.md ===== -->

---
created: 2026-01-28T20:42:44 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | ForgeTypeId | Autodesk

> ## Excerpt
> Autodesk.Revit.DB.ForgeTypeId is an extensible identifier for a unit, symbol, or other object, and is used throughout the Revit API to identify data such as units of measurement, symbols, and unit types. Unit types are referred to as "specs" to avoid confusion with units themselves.

---
`Autodesk.Revit.DB.ForgeTypeId` is an extensible identifier for a unit, symbol, or other object, and is used throughout the Revit API to identify data such as units of measurement, symbols, and unit types. Unit types are referred to as "specs" to avoid confusion with units themselves.

A `ForgeTypeId` instance holds a string, called a "typeid", that uniquely identifies a Forge schema. A Forge schema is a JSON document describing a data structure, supporting data interchange between applications. A typeid string includes a namespace and version number such as

-   `autodesk.spec.aec:length-1.0.0`
-   `autodesk.unit.unit:meters-1.0.0`
-   `autodesk.revit.category.local:walls-1.0.0`

By default, comparison of ForgeTypeId values in the Revit API ignores the version number.

The members of the following classes have a ForgeTypeId data type:

-   DisciplineTypeId - Product disciplines used in the Revit UI such as Architecture, Electrical, HVAC, Piping, and Structural
-   GroupTypeId - Groupings used for parameters in the Revit UI such as Construction, General, Geometry, IdentityData
-   ParameterTypeId - Type of parameters such as AllModelInstanceComments, InstanceSillHeightParam, WallTopOffset
-   SpecTypeId - Type of quantity to be measured such as Area, Currency, HvacDensity, Wattage
-   SymbolTypeId - Unit symbol displayed in the formatted string representation of a number to indicate the units of the value, such as DegreeC, Ft, KipPerFt, MSup2
-   UnitTypeId - Units and display format used to format numbers as strings or convert units such as Acres, Degrees, Feet, Liters

For example, the following properties all have a ForgeTypeId data type:

-   DisciplineTypeId.Architecture
-   GroupTypeId.Constraints
-   ParameterTypeId.WallTopOffset
-   SpecTypeId.Volume
-   SymbolTypeId.Hour
-   UnitTypeId.Millimeters

These static methods convert a BuiltInCategory to a ForgeTypeId and vice versa.

-   Category.GetBuiltInCategoryTypeId(BuiltInCategory)
-   Category.GetBuiltInCategory(ForgeTypeId)

For example, `Category.GetBuiltInCategoryTypeId(BuiltInCategory.OST_Furniture)` returns a `ForgeTypeId` with a `TypeId` equal to `autodesk.revit.category.family:furniture-1.0.0`


<!-- ===== END: Help  ForgeTypeId  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Import Functions  Autodesk.md ===== -->

---
created: 2026-01-28T20:42:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Import Functions | Autodesk

> ## Excerpt
> The overloads for the Document.Import method allow several different file types to be imported.

---
The overloads for the `Document.Import` method allow several different file types to be imported.

## CAD file import

-   Import(String, SATImportOptions, View) - Imports an SAT file into the document.
-   Import(String, SKPImportOptions, View) - Imports an SKP file into the document.
-   Import(String, DGNImportOptions, View, out ElementId) - Imports a DGN file to the document.
-   Import(String, DWGImportOptions, View, out ElementId) - Imports a DWG or DXF file to the document.

## GBXML import

-   Import(String, GBXMLImportOptions)

## Images and PDF import

Revit can import images (JPG, PNG, etc) and raster images generated from PDF files.

The class `ImageInstance` represents an instance of an ImageType placed in a view. Its members include:

-   Create(Document, View, ElementId, ImagePlacementOptions) - The ImagePlacementOptions describes where an image instance should be placed in a view.
-   GetLocation(BoxPlacement) - The BoxPlacment enumeration is used to specify which corner (or the center) of the image the location pertains to.
-   SetLocation(XYZ, BoxPlacement)
-   property Width
-   property Height
-   property EnableSnaps

The class `ImageType` represents a type containing an image. Its members include:

-   Create(Document, ImageTypeOptions)
-   CanReload() - validates the corresponding image or PDF file and performs additional validation if the file is served by an external provider.
-   ReloadFrom(ImageTypeOptions)
-   property ExternalResourceType - the type of external resources that represents images (and PDF files).
-   property PageNumber
-   property PathType - the type of path that was used to refer to the file from which the ImageType was loaded.

The class `ImageTypeOptions` represents the options that are used when creating or reloading an ImageType, which contains image data corresponding to an image or PDF file. Its members include:

-   IsValid() - tests whether ImageTypeOptions can be used to create or reload an ImageType; additional validation is performed for PDF files and external files.
-   property PageNumber
-   property Path
-   property Resolution - is measured in dpi and relates the number of pixels in raster images to their size.
-   setExternalResourceReference() - specifies the location of an image or PDF file using an external resource reference.

ImageTypeOptions can be used to specify a local file or a file served by an external provider. Local files can be referred to using relative paths. For PDF files, ImageType loads a single page at a time, which is rasterized at the resolution specified in ImageTypeOptions.

The class `ImagePlacementOptions` is used to describe where an ImageInstance should be placed in a view

-   ImagePlacementOptions() constructs a new ImagePlacementOptions that will place an ImageInstance with its center at the origin of the model
-   ImagePlacementOptions(XYZ, BoxPlacement) constructs a new ImagePlacementOptions with the provided Location and PlacementPoint
-   Location specifies where a point of the ImageInstance, determined by the PlacementPoint property, is going to be inserted.
-   PlacementPoint uses a `BoxPlacement` to identify which point of the ImageInstance will be aligned to the Location

### Converting images between links and imports

`ImageTypeOptions.SourceType` along with the new enumerated value `ImageTypeSource` and `ImageType.ReloadFrom()` allow you to create or convert an ImageType to a link or import.

The overall process is:

-   Create a new ImageTypeOptions instance from the existing ImageType properties
-   Modify the ImagesTypeOptions, for example by changing the ImageTypeOptions.SourceType between Link and Import, or change the path with ImageTypeOptions.SetPath()
-   Use those new ImageTypeOptions in ImageType.ReloadFrom

ImageType properties include:

-   ImageType.Source - Indicates how the image is created (as a link, import, or internally-generated image)
-   ImageType.Status - Indicates whether the image is loaded or unloaded (if applicable)

Two constructors take an ImageTypeSource as an argument:

-   ImageTypeOptions(String, Boolean, ImageTypeSource)
-   ImageTypeOptions(ExternalResourceReference, ImageTypeSource)

The enumeration: `ImageTypeStatus` contains possible values for the load status of an ImageType.

`OptionalFunctionalityUtils.isPDFImportAvailable()` checks whether the installed Revit contains optional modules that are necessary for the PDF import functionality.

## Rhino

`Document.Import(String, ImportOptions3DM, View)` and `Document.Link(String, ImportOptions3DM, View)` import or link a 3DM file into the document.


<!-- ===== END: Help  Import Functions  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Settings  Autodesk.md ===== -->

---
created: 2026-01-28T20:42:55 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Settings | Autodesk

> ## Excerpt
> The following table identifies the commands in the Revit Platform UI Manage tab, and corresponding APIs.

---
The following table identifies the commands in the Revit Platform UI Manage tab, and corresponding APIs.

**Table 7: Settings in API and UI**

|  |  |  |
| --- | --- | --- |
| UI command | Associated API | Reference |
| Settings → Project Information | Document.ProjectInformation | See the following note |
| Settings → Project Parameters | Document.ParameterBindings (Only for Shared Parameter) | See [Shared Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_html) |
| Project Location panel | Document.ProjectLocations Document.ActiveProjectLocation | [Place and Locations](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_html) |
| Settings → Additional Settings → Fill Patterns | FilteredElementCollector filtering on class FillPatternElement | See the following note |
| Settings → Materials | FilteredElementCollector filtering on class Material | See [Material Management](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Material_Management_html) |
| Settings → Object Styles | Document.Settings.Categories | See the following note |
| Phasing → Phases | Document.Phases | See the following note |
| Settings → Structural Settings | Loads and related structural settings are available in the API | See [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html) |
| Settings → Project Units | Document.GetUnits() | See [Units](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_Units_html) |
| Area and Volume Calculations (on the Room & Area panel) | AreaVolumeSettings.GetAreaVolumeSettings() | See the following note |

Note: Project Information - The API provides the ProjectInfo class which is retrieved using Document.ProjectInformation to represent project information in the Revit project. The following table identifies the corresponding APIs for the Project Information parameters.

**Table 8: ProjectInformation**

<table summary="" id="GUID-24C1A8C9-03A3-4E6D-B3D9-258BE2A28A79__TABLE_6FEDAA922C3549BEBFBB037FC1C40BC9"><tbody><tr><td><b>Parameters</b></td><td><b>Corresponding API</b></td><td><b>Built-in Parameters</b></td></tr><tr><td>Project Issue Date</td><td>ProjectInfo.IssueDate</td><td>PROJECT_ISSUE_DATE</td></tr><tr><td>Project Status</td><td>ProjectInfo.Status</td><td>PROJECT_STATUS</td></tr><tr><td>Client Name</td><td>ProjectInfo.ClientName</td><td>CLIENT_NAME</td></tr><tr><td>Project Address</td><td>ProjectInfo.Address</td><td>PROJECT_ADDRESS</td></tr><tr><td>Project Name</td><td>ProjectInfo.Name</td><td>PROJECT_NAME</td></tr><tr><td>Project Number</td><td>ProjectInfo.Number</td><td>PROJECT_NUMBER</td></tr></tbody></table>

Use the properties exposed by ProjectInfo to retrieve and set all strings. These properties are implemented by the corresponding built-in parameters. You can get or set the values through built-in parameters directly. For more information about how to gain access to these parameters through the built-in parameters, see [Parameter](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Parameter_html) in the [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html) section. The recommended way to get project information is to use the ProjectInfo properties.

-   Fill Patterns - Retrieve all Fill Patterns in the current document using a FilteredElementCollector filtering on class FillPatternElement. Specific FillPatterns can be retrieved using the static methods FillPatternElement.GetFillPattern(Document, ElementId) or FillPatternElement.GetFillPatternByName (Document, string).
-   Object Styles - Use Settings.Categories to retrieve all information in Category objects except for Line Style. For more details, see [Other Classifications](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_Other_Classifications_html) in the [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html)and [Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_html) sections.
-   Phases - Revit maintains the element lifetime by phases, which are distinct time periods in the project lifecycle. All phases in a document are retrieved using the Document.Phases property. The property returns an array containing Phase class instances. However, the Revit API does not expose functions from the Phase class.
-   Options - The Options command configures project global settings. You can retrieve an Options.Application instance using the Application.Options property. Currently, the Options.Application class only supports access to library paths and shared parameters file.
-   Area and Volume Calculations - The AreaVolumeSettings class allows you to enable or disable volume calculations, and to change the room boundary location.


<!-- ===== END: Help  Settings  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Units  Autodesk.md ===== -->

---
created: 2026-01-28T20:43:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Units | Autodesk

> ## Excerpt
> The two main classes in the Revit API for working with units are Units and FormatOptions. The Units class represents a document's default settings for formatting numbers with units as strings. It contains a FormatOptions object for each unit type as well as settings related to decimal symbol and digit grouping.

---
The two main classes in the Revit API for working with units are Units and FormatOptions. The Units class represents a document's default settings for formatting numbers with units as strings. It contains a FormatOptions object for each unit type as well as settings related to decimal symbol and digit grouping.

The `Units` class stores a `FormatOptions` object for every valid unit type, but not all of them can be directly modified. Some, like `SpecTypeId.Number` and `SpecTypeId.SiteAngle`, have fixed definitions. Others have definitions which are automatically derived from other unit types. For example, `SpecTypeId.SheetLength` is derived from `SpecTypeId.Length` and `SpecTypeId.ForceScale` is derived from `SpecTypeId.Force`.

The FormatOptions class contains settings that control how to format numbers with units as strings. It contains those settings that are typically chosen by an end-user in the Format dialog and stored in the document, such as rounding, accuracy, display units, and whether to suppress spaces or leading or trailing zeros.

The FormatOptions class is used in two different ways. A FormatOptions object in the Units class represents the default settings for the document. A FormatOptions object used elsewhere represents settings that may optionally override the default settings.

The UseDefault property controls whether a FormatOptions object represents default or custom formatting. If UseDefault is true, formatting will be according to the default settings in the Units class, and none of the other settings in the object are meaningful. If UseDefault is false, the object contains custom settings that override the default settings in the Units class. UseDefault is always false for FormatOptions objects in the Units class.

## Unit Conversion

The Revit API provides utility classes to facilitate working with quantities in Revit. The UnitUtils class makes it easy to convert unit data to and from Revit's internal units.

The UnitUtils class offers a set of methods for mapping between enumeration values and ForgeTypeId values to assist clients in migrating code to ForgeTypeId such as:

-   UnitUtils.GetDiscipline()
-   UnitUtils.IsMeasurableSpec()
-   UnitUtils.IsSymbol()

Revit has seven base quantities, each with its own internal unit. These internal units are identified in the following table.

**Table 9: 7 Base Units in Revit Unit System**

<table summary="" id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__TABLE_32F4CA8500D343A8B7A6486F4FFB51DF"><tbody><tr><td><b>Base Unit</b></td><td><b>Unit In Revit</b></td><td><b>Unit System</b></td></tr><tr><td>Length</td><td>Feet (ft)</td><td>Imperial</td></tr><tr><td>Angle</td><td>Radian</td><td>Metric</td></tr><tr><td>Mass</td><td>Kilogram (kg)</td><td>Metric</td></tr><tr><td>Time</td><td>Seconds (s)</td><td>Metric</td></tr><tr><td>Electric Current</td><td>Ampere (A)</td><td>Metric</td></tr><tr><td>Temperature</td><td>Kelvin (K)</td><td>Metric</td></tr><tr><td>Luminous Intensity</td><td>Candela (cd)</td><td>Metric</td></tr></tbody></table>

Note: Since Revit stores lengths in feet and other basic quantities in metric units, a derived unit involving length will be a non-standard unit based on both the Imperial and the Metric systems. For example, since a force is measured in "mass-length per time squared", it is stored in kg-ft / s<sub id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__GUID-CDF72B07-27F9-460A-832A-5784F65CEFCD">2</sub>. The following example uses the UnitUtils.ConvertFromInternalUnits() method to get the minimum yield stress for a material in kips per square inch.

<table summary="" id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__TABLE_5CC927E9E03840619648898E366D1D5E"><tbody><tr><td><b>Code Region: Converting from Revit's internal units</b></td></tr><tr><td><pre><code><span>double</span><span> </span><span>GetYieldStressInKsi</span><span>(</span><span>Material</span><span> material</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>double</span><span> dMinYieldStress </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>// Get the structural asset for the material</span><span>
    </span><span>ElementId</span><span> strucAssetId </span><span>=</span><span> material</span><span>.</span><span>StructuralAssetId</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>strucAssetId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>PropertySetElement</span><span> pse </span><span>=</span><span> material</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>strucAssetId</span><span>)</span><span> </span><span>as</span><span> </span><span>PropertySetElement</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>pse </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>StructuralAsset</span><span> asset </span><span>=</span><span> pse</span><span>.</span><span>GetStructuralAsset</span><span>();</span><span>

            </span><span>// Get the min yield stress and convert to ksi</span><span>
            dMinYieldStress </span><span>=</span><span> asset</span><span>.</span><span>MinimumYieldStress</span><span>;</span><span>
            dMinYieldStress </span><span>=</span><span> </span><span>UnitUtils</span><span>.</span><span>ConvertFromInternalUnits</span><span>(</span><span>dMinYieldStress</span><span>,</span><span>
                </span><span>UnitTypeId</span><span>.</span><span>KipsPerSquareInch</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> dMinYieldStress</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The UnitUtils can also be used to convert a value from one unit type to another, such as square feet to square meters. In the following example, a wall's top offset value that was entered in inches is converted to feet, the expected unit for setting that value.

<table summary="" id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__TABLE_2259B9502C1345ACB412C97DAE113808"><tbody><tr><td><b>Code Region: Converting between units</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>SetTopOffset</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> </span><span>double</span><span> dOffsetInches</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// convert user-defined offset value to feet from inches prior to setting</span><span>
    </span><span>double</span><span> dOffsetFeet </span><span>=</span><span> </span><span>UnitUtils</span><span>.</span><span>Convert</span><span>(</span><span>dOffsetInches</span><span>,</span><span>
                                            </span><span>UnitTypeId</span><span>.</span><span>Inches</span><span>,</span><span>
                                            </span><span>UnitTypeId</span><span>.</span><span>Feet</span><span>);</span><span>

    </span><span>Parameter</span><span> paramTopOffset </span><span>=</span><span> wall</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>WallTopOffset</span><span>);</span><span>
    paramTopOffset</span><span>.</span><span>Set</span><span>(</span><span>dOffsetFeet</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Unit formatting and parsing

Another utility class, UnitFormatUtils, can format data or parse formatted unit data.

The overloaded method Format() can be used to format a value into a string based on formatting options as the following example demonstrates. The material density is retrieved and then the value is then converted to a user-friendly value with unit using the Format() method.

<table summary="" id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__TABLE_6313BAF0D4BC49F48AAA2D7ACE10992E"><tbody><tr><td><b>Code Region: Format value to string</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>DisplayDensityOfMaterial</span><span>(</span><span>Material</span><span> material</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>double</span><span> density </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>// get structural asset of material in order to get the density</span><span>
    </span><span>ElementId</span><span> strucAssetId </span><span>=</span><span> material</span><span>.</span><span>StructuralAssetId</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>strucAssetId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>PropertySetElement</span><span> pse </span><span>=</span><span> material</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>strucAssetId</span><span>)</span><span> </span><span>as</span><span> </span><span>PropertySetElement</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>pse </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>StructuralAsset</span><span> asset </span><span>=</span><span> pse</span><span>.</span><span>GetStructuralAsset</span><span>();</span><span>

            density </span><span>=</span><span> asset</span><span>.</span><span>Density</span><span>;</span><span>
            </span><span>// convert the density value to a user readable string that includes the units</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Units</span><span> units </span><span>=</span><span> material</span><span>.</span><span>Document</span><span>.</span><span>GetUnits</span><span>();</span><span>
            </span><span>// false for maxAccuracy means accuracy specified by the FormatOptions should be used</span><span>
            </span><span>// false for forEditing since this will be for display only and no formatting modifications are necessary</span><span>
            </span><span>string</span><span> strDensity </span><span>=</span><span> </span><span>UnitFormatUtils</span><span>.</span><span>Format</span><span>(</span><span>units</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>UnitWeight</span><span>,</span><span> density</span><span>,</span><span> </span><span>false</span><span>);</span><span>
            </span><span>string</span><span> msg </span><span>=</span><span> </span><span>string</span><span>.</span><span>Format</span><span>(</span><span>"Raw Value: {0}\r\nFormatted Value: {1}"</span><span>,</span><span> density</span><span>,</span><span> strDensity</span><span>);</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Material Density"</span><span>,</span><span> msg</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The overloaded UnitFormatUtils.TryParse() method parses a formatted string, including units, into a value if possible, using the Revit internal units of the specified unit type. The following example takes a user entered length value, assumed to be a number and length unit, and attempts to parse it into a length value. The result is compared with the input string in a TaskDialog for demonstration purposes.

<table summary="" id="GUID-099B3FD9-1C5B-459C-AC1E-EF958551DFB6__TABLE_909C8B62079A453A805F5689AFADBAF9"><tbody><tr><td><b>Code Region: Parse string</b></td></tr><tr><td><pre><code><span>double</span><span> </span><span>GetLengthInput</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>String</span><span> userInputLength</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>double</span><span> dParsedLength </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Units</span><span> units </span><span>=</span><span> document</span><span>.</span><span>GetUnits</span><span>();</span><span>
    </span><span>// try to parse a user entered string (i.e. 100 mm, 1'6")</span><span>
    </span><span>bool</span><span> parsed </span><span>=</span><span> </span><span>UnitFormatUtils</span><span>.</span><span>TryParse</span><span>(</span><span>units</span><span>,</span><span> </span><span>SpecTypeId</span><span>.</span><span>Length</span><span>,</span><span> userInputLength</span><span>,</span><span> </span><span>out</span><span> dParsedLength</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>parsed </span><span>==</span><span> </span><span>true</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>string</span><span> msg </span><span>=</span><span> </span><span>string</span><span>.</span><span>Format</span><span>(</span><span>"User Input: {0}\r\nParsed value: {1}"</span><span>,</span><span> userInputLength</span><span>,</span><span> dParsedLength</span><span>);</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Parsed Data"</span><span>,</span><span> msg</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> dParsedLength</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Units  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Cloud Models  Autodesk.md ===== -->

---
created: 2026-01-28T20:43:07 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Cloud Models | Autodesk

> ## Excerpt
> Autodesk provides two different BIM 360 web portals and regions with different URLs. You can save your Revit cloud models to either:

---
## Basic Info

-   Document.IsModelInCloud indicates if the current document is located in the cloud.
-   Document.GetCloudModelPath() returns the cloud model path.

Autodesk provides two different BIM 360 web portals and regions with different URLs. You can save your Revit cloud models to either:

-   Autodesk Docs US, at [insight.b360.autodesk.com](https://insight.b360.autodesk.com/)
-   Autodesk Docs EU, at [insight.b360.eu.autodesk.com](https://insight.b360.eu.autodesk.com/)

The property

-   ModelPath.Region

returns the region of the account and project which contains this model. `ModelPathUtils.CloudRegionUS` and `ModelPathUtils.CloudRegionEMEA` return the region names of different Autodesk cloud services. They can be used as the first argument of the ModelPathUtils.ConvertCloudGUIDsToCloudPath() method.

## Open

To open a cloud-hosted model with `Application.OpenDocumentFile` a `ModelPath` is needed. Such a ModelPath is returned by the method `ModelPathUtils.ConvertCloudGUIDsToCloudPath()` whose inputs are a region, ProjectGUID, and ModelGUID.

-   Document.CloudModelGUID returns the Model GUID if it is stored in the cloud.
-   ModelPath.GetProjectGUID() returns the Project GUID.
-   Document.GetWorksharingCentralModelPath() returns the model path of the central model.

### Getting the CloudPath for a Model

The region argument for ConvertCloudGUIDsToCloudPath is a string type and should be either "US" or "EMEA", depending on which BIM 360 or Autodesk Docs region account and project the model is stored in.

-   US - [insight.b360.autodesk.com](https://insight.b360.autodesk.com/) - ModelPathUtils.CloudRegionUS
-   EU - [insight.b360.eu.autodesk.com](https://insight.b360.eu.autodesk.com/) - ModelPathUtils.CloudRegionEMEA

Depending on where the cloud model is stored, provide the appropriate region argument "US" or "EMEA", respectively.

To get a valid CloudPath with the Revit API call `ModelPathUtils.ConvertCloudGUIDsToCloudPath()`. You will need to register a Forge application and use the Forge Data Management API to get the project Guid and model Guid as the other two arguments.

The [Forge DM API reference on GET hubs](https://forge.autodesk.com/en/docs/data/v2/reference/http/hubs-GET) shows how to list the hubs your Forge application can access. You can filter out the accounts of interest using the `data.attributes.name` field. You can also get the region information here.

The [Forge DM API reference on GET project folder contents](https://forge.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET) shows how to list the folder contents you plan to open. You can filter out the relevant cloud model using the `included.attributes.name` field; the project Guid and model Guid information is provided in the `included.attributes.extension.data` field.

With these three pieces of information - region, project guid, and model guid - you can obtain a valid cloud path with the ModelPathUtils.ConvertCloudGUIDsToCloudPath method and then open the model with the OpenDocument or OpenAndActivateDocument methods.

### Getting the Forge ID for a Model

These methods allow you to identify the Forge IDs for Cloud Models:

-   Document.GetHubId(): ForgeDM hub id where the model is located
-   Document.GetProjectId(): ForgeDM project id where the model is located
-   Document.GetCloudFolderId(bool forceRefresh): ForgeDM folder id where the model is located
-   Document.GetCloudModelUrn(): A ForgeDM Urn identifying the model They return strings which will be empty for a document which is not a cloud model.

### IOpenFromCloudCallback

An implementation of interface `IOpenFromCloudCallback` can be specified to control Revit's behavior when opening the cloud model. `IOpenFromCloudCallback.OnOpenConflict` method is called when a conflict happens during the model opening.

It receives a value of enum `OpenConflictScenario` that describes the conflict:

-   Rollback indicates that the Central model is restored to an earlier version.
-   Relinquished indicates that Ownership to model elements is relinquished.
-   OutOfDate indicates that the model is out of date
-   VersionArchived indicates that last central version merged into the local model to open has been archived in the central model. Editing is limited to elements and worksets the user owns until Reload Latest or Synchronize with Central is conducted after the model is opened.

And it returns a value of enum `OpenConflictResult` that describes the action Revit should take:

-   KeepLocalChanges - Keeps the local changes and open the model
-   DiscardLocalChangesAndOpenLatestVersion - Discard the local changes and open the latest version of the model
-   DetachFromCentral - Detach the local model from its central model, with worksets preserved
-   Cancel

`DefaultOpenFromCloudCallback` class is the default callback used by an overload of the Application.OpenDocumentFile method. `DiscardLocalChangesAndOpenLatestVersion` is returned for all kinds of conflicts.

## Save

-   Document.SaveAsCloudModel() saves the current model as a cloud model in BIM 360 and supports upload of local workshared file into BIM 360 Design as a Revit Cloud Worksharing central model.
-   Document.SaveCloudModel() saves the current cloud model.

To save a local Revit file to the cloud as a workshared or non-workshared cloud model, you need to get the BIM 360 or Autodesk Docs account id, project id, folder id, and a model name. There are two ways to retrieve this information:

1.  From the web browser
2.  Using the Forge DM API

### SaveAsCloudModel Information from the Web Browser

Open a web browser, navigate to your project home page, and copy the URL: ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/acc_guids_1.png)

The account id and project id are both GUID strings.

They can be extracted from the URL like this: ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/acc_guids_extract_1.png)

Navigate to your target Autodesk Docs folder in the web browser and copy the URL: ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/acc_guids_3.png)

The folder id is embedded in this URL; in this example, it is "urn:adsk.wipprod:fs.folder:co.Foe4ZYNhTTKOhCqKApQkoQ": ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/acc_guids_extract_3.png)

With this information, you can save a local file which is opened in Revit to Autodesk document management as a cloud model with a call like this:

```
public void SaveAsCloud(Document currentDocument)
{
  Guid account = new Guid("a8d3b76e-cf23-4dd7-a090-9e893efcf949");
  Guid project = new Guid("bf46f5e3-285e-496f-be03-b5b1f8b1e154");
  string folder_id = "urn:adsk.wipemea:fs.folder:co.Jo68ieLRRcKvQr4fI2Q8uQ";
  string model_name = "rac_advanced_sample_project.rvt";

  currentDocument.SaveAsCloudModel(
    account, // account id
    project, // project id
    folder_id, // folder id
    model_name // model name
  );
}
```

### SaveAsCloudModel Information with Forge DM API

With your Forge application, you can:

-   List hubs with the [GET hubs API](https://forge.autodesk.com/en/docs/data/v2/reference/http/hubs-GET) to retrieve the region and account ids.
-   List projects the [GET projects API](https://forge.autodesk.com/en/docs/data/v2/reference/http/hubs-hub_id-projects-GET) to get all the projects of the given hub and their project ids.
-   List the top folders with the [GET top folders API](https://forge.autodesk.com/en/docs/data/v2/reference/http/hubs-hub_id-projects-project_id-topFolders-GET) to get all accessible top folders (depending on permission) and you their valid folder ids, or continue to get the nested folders with the [list folder contents API](https://forge.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET) until the target folder and its folder id is found and can be stored for later use.

With this information, you can save a local file opened in Revit to Autodesk document management as a cloud model using the same Revit API call as above.


<!-- ===== END: Help  Cloud Models  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Elements Essentials  Autodesk.md ===== -->

---
created: 2026-01-28T20:43:20 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Elements Essentials | Autodesk

> ## Excerpt
> An Element corresponds to a single building or drawing component, such as a door, a wall, or a dimension. In addition, an Element can be a door type, a view, or a material definition.

---
An Element corresponds to a single building or drawing component, such as a door, a wall, or a dimension. In addition, an Element can be a door type, a view, or a material definition.

**Pages in this section**

-   [Element Classification](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_Element_Classification_html)
-   [Other Classifications](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_Other_Classifications_html)
-   [Element Retrieval](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_Element_Retrieval_html)
-   [General Properties](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_General_Properties_html)

**Parent page:** [Introduction](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_html)


<!-- ===== END: Help  Elements Essentials  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Element Classification  Autodesk.md ===== -->

---
created: 2026-01-28T20:43:25 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Element Classification | Autodesk

> ## Excerpt
> Revit Elements are divided into six groups: Model, Sketch, View, Group, Annotation and Information. Each group contains related Elements and their corresponding symbols.

---
Revit Elements are divided into six groups: Model, Sketch, View, Group, Annotation and Information. Each group contains related Elements and their corresponding symbols.

### Model Elements

Model Elements represent physical items that exist in a building project. Elements in the Model Elements group can be subdivided into the following:

-   Family Instances - Family Instances contain family instance objects. You can load family objects into your project or create them from family templates. For more information, see [Family Instances](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_html).
-   Host Elements - Host Elements contain system family objects that can contain other model elements, such as wall, roof, ceiling, and floor. For more information about Host Elements, see [Walls, Floors, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html).
-   Structure Elements. - Structure Elements contain elements that are only used in the structural features of Revit. For more information about Structure Elements, see [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html).
    
    ### View Elements
    

View Elements represent the way you view and interact with other objects in Revit. For more information, see [Views](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_html).

### Group Elements

Group Elements represent the assistant Elements such as Array and Group objects in Revit. For more information, see [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html).

### Annotation and Datum Elements

Annotation and Datum Elements contain non-physical items that are visible.

-   Annotation Elements represent 2D components that maintain scale on paper and are only visible in one view. For more information about Annotation Elements, see [Annotation Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_html).

Note Annotation Elements representing 2D components do not exist only in 2D views. For example, dimensions can be drawn in 3D view while the shape they refer to only exists in a 2D planar face.

-   Datum Elements represent non-physical items that are used to establish project context. These elements can exist in views. Datum Elements are further divided into the following:
-   Common Datum Elements - Common Datum Elements represent non-physical visible items used to store data for modeling.
-   Datum FamilyInstance - Datum FamilyInstance represents non-physical visible items loaded into your project or created from family templates. NoteFor more information about Common Datum Elements and Datum FamilyInstance, see [Datum and Information Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_html); for ModelCurve related contents, see [Sketching](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_html).
-   Structural Datum Elements - Structural Datum Elements represent non-physical visible items used to store data for structure modeling. For more information about Structural Datum Elements, see [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html).
    
    ### Sketch Elements
    

Sketch Elements represent temporary items used to sketch 2D/3D form. This group contains the following objects used in family modeling and massing:

-   SketchPlane
-   Sketch
-   Path3D
-   GenericForm.

For Sketch details, see [Sketching](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_html).

### Information Elements

Information Elements contain non-physical invisible items used to store project and application data. Information Elements are further separated into the following:

-   Project Datum Elements
-   Project Datum Elements (Unique).

For more information about Datum Elements, see [Datum and Information Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_html).


<!-- ===== END: Help  Element Classification  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Other Classifications  Autodesk.md ===== -->

---
created: 2026-01-28T20:43:31 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Other Classifications | Autodesk

> ## Excerpt
> Elements can be classified by Category, Family, Symbol and Instance.

---
Elements can be classified by Category, Family, Symbol and Instance.

There are some relationships between the classifications. For example:

-   You can distinguish different kinds of FamilyInstances by the category. Items such as structural columns are in the Structural Columns category, beams and braces are in the Structural Framing category, and so on.
-   You can differentiate structural FamilyInstance Elements by their symbol.
    
    ### Category
    

The Element.Category property represents the category or subcategory to which an Element belongs. It is used to identify the Element type. For example, anything in the walls Category is considered a wall. Other categories include doors and rooms.

Categories are the most general class. The Document.Settings.Categories property is a map that contains all Category objects in the document and is subdivided into the following:

-   Model Categories - Model Categories include beams, columns, doors, windows, and walls.
-   Annotation Categories. Annotation Categories include dimensions, grids, levels, and textnotes.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4C0CA7CF-C5CF-4042-B99D-AE185F64D17F-low.png)**Figure 20: Categories**

Note: The following guidelines apply to categories:

-   In general, the following rules apply to categories:
    -   Each family object belongs to a category
    -   Non-family objects, like materials and views, do not belong to a category
    -   There are exceptions such as ProjectInfo, which belongs to the Project Information category.
-   An element and its corresponding symbols are usually in the same category. For example, a basic wall and its wall type Generic - 8" are all in the Walls category.
-   The same type of Elements can be in different categories. For example, SpotDimensions has the SpotDimensionType, but it can belong to two different categories: Spot Elevations and Spot Coordinates.
-   Different Elements can be in the same category because of their similarity or for architectural reasons. ModelLine and DetailLine are in the Lines category.

To gain access to the categories you may access all categories from the document's Settings class (for example, to insert a new category set), or if you only need access to a category object associated with a built-in category, you may access the category object directly from the static overloaded GetCategory() method of the Category class.

To access categories:

-   Get an entire map of Categories from the document properties: Document.Settings.Categories returns a CategoryNameMap containing a map of all Revit categories indexed by their name. `Category.IsVisibleInUI` returns true if the category is visible to the user in lists of categories in the Revit user interface (dialogs such as Visibility Graphics or View Filters)
-   Get a specific built-in category by calling the appropriate overload of the static method Category.GetCategory().
-   Get a specific category or subcategory by its ElementId by calling the corresponding overload of the static method Category.GetCategory().

<table summary="" id="GUID-5D2ED5AF-7D4F-49BE-85E8-68CB49BD8178__TABLE_8F0B43132FB64B63880CFD0EB41FCFA4"><tbody><tr><td><b>Code Region 5-1: Getting categories from document settings</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetCategories</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get settings of current document</span><span>
    </span><span>Settings</span><span> documentSettings </span><span>=</span><span> document</span><span>.</span><span>Settings</span><span>;</span><span>

    </span><span>// Get all categories of current document</span><span>
    </span><span>Categories</span><span> groups </span><span>=</span><span> documentSettings</span><span>.</span><span>Categories</span><span>;</span><span>

    </span><span>// Show the number of all the categories to the user</span><span>
    </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"Number of all categories in current Revit document:"</span><span> </span><span>+</span><span> groups</span><span>.</span><span>Size</span><span>;</span><span> 

    </span><span>// get Floor category according to OST_Floors and show its name</span><span>
    </span><span>Category</span><span> floorCategory </span><span>=</span><span> groups</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Floors</span><span>);</span><span>
    prompt </span><span>+=</span><span> floorCategory</span><span>.</span><span>Name</span><span>;</span><span>

    </span><span>// Give the user some information</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Category is used in the following manner:

-   Category is used to classify elements. The element category determines certain behaviors. For example, all elements in the same category can be included in the same schedule.
-   Elements have parameters based on their categories.
-   Categories are also used for controlling visibility and graphical appearance in Revit.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-FD2C68CC-B442-4A39-B507-8965B15B1DCF-low.png)

**Figure 21: Visibility by Category**

An element's category is determined by the Category ID.

-   Category IDs are represented by the ElementId class.
-   Imported Category IDs correspond to elements in the document.
-   Most categories are built-in and their IDs are constants stored in ElementIds.
-   Each built-in category ID has a corresponding value in the BuiltInCategory Enumeration. They can be converted to corresponding BuiltInCategory enumerated types. `LabelUtils.GetLabelFor(BuiltInCategory)` returns the string name of the given BuiltInCategory in the current Revit language.
-   If the category is not built-in, the ID is converted to a null value.

<table summary="" id="GUID-5D2ED5AF-7D4F-49BE-85E8-68CB49BD8178__TABLE_BB8156D2B13340B8A39BD2CC3F794499"><tbody><tr><td><b>Code Region 5-2: Getting element category</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetElementCategory</span><span>(</span><span>UIDocument</span><span> uidoc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Element</span><span> selectedElement </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>())</span><span>
    </span><span>{</span><span>
        selectedElement </span><span>=</span><span> uidoc</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>break</span><span>;</span><span>  </span><span>// just get one selected element</span><span>
    </span><span>}</span><span>

    </span><span>// Get the category instance from the Category property</span><span>
    </span><span>Category</span><span> category </span><span>=</span><span> selectedElement</span><span>.</span><span>Category</span><span>;</span><span>

    </span><span>BuiltInCategory</span><span> enumCategory </span><span>=</span><span> </span><span>(</span><span>BuiltInCategory</span><span>)</span><span>category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: To avoid Globalization problems when using Category.Name, BuiltInCategory is a better choice. Category.Name can be different in different languages.

### Family

Families are classes of Elements within a category. Families can group Elements by the following:

-   A common set of parameters (properties).
-   Identical use.
-   Similar graphical representation.

Most families are component Family files, meaning that you can load them into your project or create them from Family templates. You determine the property set and the Family graphical representation.

Another family type is the system Family. System Families are not available for loading or creating. Revit predefines the system Family properties and graphical representation; they include walls, dimensions, roofs, floors (or slabs), and levels.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-428BCB2F-3741-4F05-A51A-9D5A9A03813D-low.png)**Figure 22: Families**

In addition to functioning as an Element class, Family is also a template used to generate new items that belong to the Family.

#### Family in the Revit Platform API

In the Revit Platform API, both the Family class and FamilyInstance belong to the Component Family. Other Elements include System Family.

Families in the Revit Platform API are represented by three objects:

-   Family
-   FamilySymbol
-   FamilyInstance.

Each object plays a significant role in the Family structure.

The Family object has the following characteristics:

-   Represents an entire family such as a beam.
-   Represents the entire family file on a disk.
-   Contains a number of FamilySymbols.

The FamilySymbol object represents a specific set of family settings in the Family such as the Type, Concrete-Rectangular Beam: 16×32.

The FamilyInstance object is a FamilySymbol instance representing a single instance in the Revit project. For example, the FamilyInstance can be a single instance of a 16×32 Concrete-Rectangular Beam in the project.

Note: Remember that the FamilyInstance exists in FamilyInstance Elements, Datum Elements, and Annotation Elements.

Consequently, the following rules apply:

-   Each FamilyInstance has one FamilySymbol.
-   Each FamilySymbol belongs to one Family.
-   Each Family contains one or more FamilySymbols.

For more detailed information, see [Family Instances](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_html).

### ElementType

In the Revit Platform API, Symbols are usually non-visible elements used to define instances. Symbols are called Types in the user interface.

-   A type can be a specific size in a family, such as a 1730 × 2032 door, or an 8×4×1/2 angle.
-   A type can be a style, such as default linear or default angular style for dimensions.

Symbols represent Elements that contain shared data for a set of similar elements. In some cases, Symbols represent building components that you can get from a warehouse, such as doors or windows, and can be placed many times in the same building. In other cases, Symbols contain host object parameters or other elements. For example, a WallType Symbol contains the thickness, number of layers, material for each layer, and other properties for a particular wall type.

FamilySymbol is a symbol in the API. It is also called Family Type in the Revit user interface. FamilySymbol is a class of elements in a family with the exact same values for all properties. For example, all 32×78 six-panel doors belong to one type, while all 24×80 six-panel doors belong to another type. Like a Family, a FamilySymbol is also a template. The FamilySymbol object is derived from the ElementType object and the Element object.

### Instance

Instances are items with specific locations in the building (model instances) or on a drawing sheet (annotation instances). Instance represents transformed identical copies of an ElementType. For example, if a building contains 20 windows of a particular type, there is one ElementType with 20 Instances. Instances are called Components in the user interface.

Note: For FamilyInstance, the Symbol property can be used instead of the GetTypeId() method to get the corresponding FamilySymbol. It is convenient and safe since you do not need to do a type conversion.


<!-- ===== END: Help  Other Classifications  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Element Retrieval  Autodesk.md ===== -->

---
created: 2026-01-28T20:43:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Element Retrieval | Autodesk

> ## Excerpt
> Elements in Revit are very common. Retrieving the elements that you want from Revit is necessary before using the API for any Element command. There are several ways to retrieve elements with the Revit API:

---
Elements in Revit are very common. Retrieving the elements that you want from Revit is necessary before using the API for any Element command. There are several ways to retrieve elements with the Revit API:

-   ElementId - If the ElementId of the element is known, the element can be retrieved from the document.
-   Element filtering and iteration - this is a good way to retrieve a set of related elements in the document.
-   Selected elements - retrieves the set of elements that the user has selected
-   Specific elements - some elements are available as properties of the document

Each of these methods of element retrieval is discussed in more details in the following sections.

### Getting an Element by ID

When the ElementId of the desired element is known, use the Document.Element property to get the element.

### Filtering the Elements Collection

The most common way to get elements in the document is to use filtering to retrieve a collection of elements. The Revit API provides the FilteredElementCollector class, and supporting classes, to create filtered collections of element which can then be iterated. See [Filtering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_html) for more information.

### Selection

Rather than getting a filtered collection of all of the elements in the model, you can access just the elements that have been selected. You can get the selected objects from the current active document using the UIDocument.Selection.GetElementIds method. For more information on using the active selection, see [Selection](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_html).

### Accessing Specific Elements from Document

In addition to using the general way to access Elements, the Revit Platform API has properties in the Document class to get the specified Elements from the current active document without iterating all Elements. The specified Elements you can retrieve are listed in the following table.

**Table 11: Retrieving Elements from document properties**

<table summary="" id="GUID-91B255CD-AC00-4EB7-B303-B8096CC2C062__TABLE_E1B9D5982AD1434EA8BC764A62C445D4"><tbody><tr><td><b>Element</b></td><td><b>Access in property of Document</b></td></tr><tr><td>ProjectInfo</td><td>Document.ProjectInformation</td></tr><tr><td>ProjectLocation</td><td>Document.ProjectLocations<p>Document.ActiveProjectLocation</p></td></tr><tr><td>SiteLocation</td><td>Document.SiteLocation</td></tr><tr><td>Phase</td><td>Document.Phases</td></tr></tbody></table>


<!-- ===== END: Help  Element Retrieval  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  General Properties  Autodesk.md ===== -->

---
created: 2026-01-28T20:43:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | General Properties | Autodesk

> ## Excerpt
> The following properties are common to each Element created using Revit.

---
The following properties are common to each Element created using Revit.

### ElementId

Every element in an active document has a unique identifier represented by the ElementId storage type. ElementId objects are project wide. It is a unique number that is never changed in the element model, which allows it to be stored externally to retrieve the element when needed.

In the Revit Platform API, you can create an ElementId directly, and then associate a unique integer value to the new ElementId. The new ElementId value is 0 by default.

<table summary="" id="GUID-BC19ED01-4A0E-48A4-A7F1-4CAFD0A950F6__TABLE_07CCE2108B0F48CAADA10468D09D9A34"><tbody><tr><td><b>Code Region 5-3: Setting ElementId</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>SetElementId</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the id of the element</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> selectedId </span><span>=</span><span> element</span><span>.</span><span>Id</span><span>;</span><span>
    </span><span>int</span><span> idInteger </span><span>=</span><span> selectedId</span><span>.</span><span>IntegerValue</span><span>;</span><span>

    </span><span>// create a new id and set the value</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> id </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>(</span><span>idInteger</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

ElementId has the following uses:

-   Use ElementId to retrieve a specific element from Revit. From the Revit Application class, gain access to the active document, and then get the specified element using the Document.GetElement(ElementId) method.

<table summary="" id="GUID-BC19ED01-4A0E-48A4-A7F1-4CAFD0A950F6__TABLE_814B259DBFC046E79FF7C02BBFB19C0B"><tbody><tr><td><b>Code Region 5-4: Using ElementId</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>UsingElementId</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the id of the element</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> selectedId </span><span>=</span><span> element</span><span>.</span><span>Id</span><span>;</span><span>
    </span><span>int</span><span> idInteger </span><span>=</span><span> selectedId</span><span>.</span><span>IntegerValue</span><span>;</span><span>

    </span><span>// create a new id and set the value</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> id </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>(</span><span>idInteger</span><span>);</span><span>

    </span><span>// Get the element </span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> first </span><span>=</span><span> element</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

If the ID number does not exist in the project, the element you retrieve is null.

-   Use ElementId to check whether two Elements in one project are equal or not. It is not recommended to use the Object.Equal() method.
    
    ### UniqueId
    

Every element has a UniqueId, represented by the String storage type. The UniqueId corresponds to the ElementId. However, unlike ElementId, UniqueId functions like a GUID (Globally Unique Identifier), which is unique across separate Revit projects. UniqueId can help you to track elements when you export Revit project files to other formats.

<table summary="" id="GUID-BC19ED01-4A0E-48A4-A7F1-4CAFD0A950F6__TABLE_BAADEF17FA0A4A06AC7BE10ADFCE6AC6"><tbody><tr><td><b>Code Region 5-5: UniqueId</b></td></tr><tr><td><p><code>string uniqueId = element.UniqueId;</code></p></td></tr></tbody></table>

Note: The ElementId is only unique in the current project. It is not unique across separate Revit projects. UniqueId is always unique across separate projects.

### Location

The location of an object is important in the building modeling process. In Revit, some objects have a point location. For example a table has a point location. Other objects have a line location, representing a location curve or no location at all. A wall is an element that has a line location.

The Revit Platform API provides the Location class and location functionality for most elements. For example, it has the Move() and Rotate() methods to translate and rotate the elements. However, the Location class has no property from which you can get information such as a coordinate. In this situation, downcast the Location object to its subclass-like LocationPoint or LocationCurve-for more detailed location information and control using object derivatives.

Retrieving an element's physical location in a project is useful when you get the geometry of an object. The following rules apply when you retrieve a location:

-   Wall, Beam, and Brace are curve-driven using LocationCurve.
-   Room, RoomTag, SpotDimension, Group, FamilyInstances that are not curve-driven, and all In-Place-FamilyInstances use LocationPoint.

In the Revit Platform API, curve-driven means that the geometry or location of an element is determined by one or more associated curves. Almost all analytical model elements are curve-driven - linear and area loads, walls, framing elements, and so on.

Other Elements cannot retrieve a LocationCurve or LocationPoint. They return Location with no information.

**Table 12: Elements Location Information**

<table summary="" id="GUID-BC19ED01-4A0E-48A4-A7F1-4CAFD0A950F6__TABLE_DC8EA66CC4DB40A7B1BE68D11B0D57ED"><tbody><tr><td><b>Location Information</b></td><td><b>Elements</b></td></tr><tr><td>LocationCurve</td><td>Wall, Beam, Brace, Structural Truss, LineLoad(without host)</td></tr><tr><td>LocationPoint</td><td>Room, RoomTag, SpotDimension, Group, Column, Mass</td></tr><tr><td>Only Location</td><td>Level, Floor, some Tags, BeamSystem, Rebar, Reinforcement, PointLoad, AreaLoad(without Host), Span Direction(IndependentTag)</td></tr><tr><td>No Location</td><td>View, LineLoad(with host), AreaLoad(with Host), BoundaryCondition</td></tr></tbody></table>

Note: There are other Elements without Location information. For example a LineLoad (with host) or an AreaLoad (with host) have no Location.

Some FamilyInstance LocationPoints, such as all in-place-FamilyInstances and masses, are specified to point (0, 0, 0) when they are created. The LocationPoint coordinate is changed if you transform or move the instance.

To change a Group-s LocationPoint, do one of the following:

-   Drag the Group origin in the Revit UI to change the LocationPoint coordinate. In this situation, the Group LocationPoint is changed while the Group-s location is not changed.
-   Move the Group using the ElementTransformUtils.MoveElement() method to change the LocationPoint. This changes both the Group location and the LocationPoint.

For more information about LocationCurve and LocationPoint, see [Moving Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Moving_Elements_html).

### Level

Levels are finite horizontal planes that act as a reference for level-hosted or level-based elements, such as roofs, floors, and ceilings. The Revit Platform API provides a Level class to represent level lines in Revit. Get the Level object to which the element is assigned using the API if the element is level-based.

<table summary="" id="GUID-BC19ED01-4A0E-48A4-A7F1-4CAFD0A950F6__TABLE_874419C0D7FB47C3933E8117BBA29AB7"><tbody><tr><td><b>Code Region 5-6: Assigning Level</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>AssignLevel</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the level object to which the element is assigned.</span><span>
    </span><span>if</span><span> </span><span>(</span><span>element</span><span>.</span><span>LevelId</span><span>.</span><span>Equals</span><span>(</span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"The element isn't based on a level."</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>Level</span><span> level </span><span>=</span><span> element</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>element</span><span>.</span><span>LevelId</span><span>)</span><span> </span><span>as</span><span> </span><span>Level</span><span>;</span><span>

        </span><span>// Format the prompt information(Name and elevation)</span><span>
        </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"The element is based on a level."</span><span>;</span><span>
        prompt </span><span>+=</span><span> </span><span>"\nThe level name is:  "</span><span> </span><span>+</span><span> level</span><span>.</span><span>Name</span><span>;</span><span>
        prompt </span><span>+=</span><span> </span><span>"\nThe level elevation is:  "</span><span> </span><span>+</span><span> level</span><span>.</span><span>Elevation</span><span>;</span><span>

        </span><span>// Show the information to the user.</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>prompt</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

A number of elements, such as a column, use a level as a basic reference. When you get the column level, the level you retrieve is the Base Level.

Note: Get the Beam or Brace level using the Reference Level parameter. From the Level property, you only get null instead of the reference level information.

Level is the most commonly used element in Revit. In the Revit Platform API, retrieve all levels using a Level class filter.

For more Level details, see [Datum and Information Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_html).

### Parameter

Every element has a set of parameters that users can view and edit in Revit. The parameters are visible in the Element Properties dialog box (select any element and click the Properties button next to the type selector). For example, the following image shows Room parameters.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-78903670-DCD6-473B-AA90-45A0AA31B65D-low.png)**Figure 25: Room parameters**

In the Revit Platform API, each Element object has a Parameters property, which is a collection of all the properties attached to the Element. You can change the property values in the collection. For example, you can get the area of a room from the room object parameters; additionally, you can set the room number using the room object parameters. The Parameter is another way to provide access to property information not exposed in the element object.

In general, every element parameter has an associated parameter ID. Parameter IDs are represented by the ElementId class. For user-created parameters, the IDs correspond to real elements in the document. However, most parameters are built-in and their IDs are constants stored in ElementIds.

Parameter is a generic form of data storage in elements. In the Revit Platform API, it is best to use the built-in parameter ID to get the parameter. Revit has a large number of built-in parameters available using the BuiltInParameter enumerated type.

For more details, see [Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_html).


<!-- ===== END: Help  General Properties  Autodesk.md ===== -->

---

