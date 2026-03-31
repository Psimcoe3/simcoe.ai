---
created: 2026-01-28T21:18:37 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Linked_Files_html
author: 
---

# Help | Linked Files | Autodesk

> ## Excerpt
> The Revit API can determine which elements in Revit are references to external files ("linked files") and can make some modifications to how Revit loads external files.

---
The Revit API can determine which elements in Revit are references to external files ("linked files") and can make some modifications to how Revit loads external files.

An Element which contains an ExternalFileReference is an element which refers to some file outside of the base .rvt file. Examples include Revit links, CAD links, the element which stores the location of the keynote file, and rendering decals. Element.IsExternalFileReference() returns whether or not an element represents an external file. And Element.GetExternalFileReference() returns the ExternalFileReference for a given Element which contains information pertaining to the external file referenced by the element.

The following classes are associated with linked files in the Revit API:

-   **ExternalFileReference** - A non-Element class which contains path and type information for a single external file which a Revit project references.
-   **ExternalFileUtils** - A utility class which allows the user to find all external file references, get the external file reference from an element, or tell whether an element is an external file reference.
-   **RevitLinkType** - An element representing a Revit file linked into a Revit project.
-   **ModelPath** - A non-Element class which contains path information for a file (not necessarily a .rvt file.) Paths can be to a location on a local or network drive, or to a Revit Server location.
-   **ModelPathUtils** - A utility class which provides methods for converting between strings and ModelPaths.
-   **TransmissionData** - A class which stores information about all of the external file references in a document. The TransmissionData for a Revit project can be read without opening the document.
    
    ### ModelPath
    

ModelPaths are paths to another file. They can refer to Revit models, or to any of Revit's external file references such as DWG links. Paths can be relative or absolute, but they must include an extension indicating the file type. Relative paths are generally relative to the currently opened document. If the current document is workshared, paths will be treated as relative to the central model. To create a ModelPath, use one of the derived classes FilePath or ServerPath.

The class ModelPathUtils contains utility functions for converting ModelPaths to and from user-visible path strings, as well as to determine if a string is a valid server path.

Shared Coordinates let the position of one linked file be known to other linked models.

-   Document.AcquireCoordinates acquires the project coordinates from a specified link instance. This works for both Revit links (RevitLinkInstance) and DWG links (ImportInstance).
-   Document.PublishCoordinates - Publishes shared coordinates to a specified ProjectLocation. This method works only on Revit links. These read-only properties provide information on the geographic coordinate system of a SiteLocation. The geographic coordinate system is imported from a DWG file from AutoCAD or Civil 3D. If the SiteLocation has geographic coordinate system information, the latitude and longitude of the SiteLocation will be updated automatically when the model's Survey Point is moved.

-   SiteLocation.GeoCoordinateSystemId - Gets a string corresponding to geographic coordinate system ID, such as "AMG-50" or "Beijing1954/a.GK3d-40" for the SiteLocation. The value will be the empty string if there is no coordinate system specified for the SiteLocation.
-   SiteLocation.GeoCoordinateSystemDefinition - Gets an XML string describing the geographic coordinate system. The value will be the empty string if there is no coordinate system specified for the SiteLocation.
