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
