---
created: 2026-01-28T21:15:51 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_BrowserOrganization_html
author: 
---

# Help | Browser Organization | Autodesk

> ## Excerpt
> The BrowserOrganization class provides read-access to the settings for grouping, sorting, and filtering of items in the project browser.

---
The BrowserOrganization class provides read-access to the settings for grouping, sorting, and filtering of items in the project browser.

BrowserOrganization.AreFiltersSatisfied() determines if the given element satisfies the filters defined by the browser organization.

## Getting the current organization

-   GetCurrentBrowserOrganizationForViews() gets the BrowserOrganization that applies to the Views section of the project browser.
-   GetCurrentBrowserOrganizationForSheets() gets the BrowserOrganization that applies to the Sheets section of the project browser.
-   BrowserOrganization.GetCurrentBrowserOrganizationForSchedules() gets the BrowserOrganization that applies to the Schedules section of the project browser

## Sorting

-   SortingOrder – The sorting order if sorting of items is applicable in the browser.
-   SortingParameterId – The id of the parameter used to determine the sorting order of items in the browser.

## FolderItemInfo

BrowserOrganization.GetFolderItems(ElementId) returns a collection of leaf FolderItemInfo objects each containing the given element Id.

FolderItemInfo contains the ElementId and Name info for each item in the organization settings of the project browser.
