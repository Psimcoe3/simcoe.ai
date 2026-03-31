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
