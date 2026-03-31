---
created: 2026-01-28T21:19:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_Place_html
author: 
---

# Help | Place | Autodesk

> ## Excerpt
> In the Revit Platform API, the SiteLocation class contains place information including Latitude, Longitude, and Time Zone. This information identifies where the project is located in the world. When setting either the Latitude or Longitude, note that:

---
## SiteLocation

In the Revit Platform API, the SiteLocation class contains place information including Latitude, Longitude, and Time Zone. This information identifies where the project is located in the world. When setting either the Latitude or Longitude, note that:

1.  Revit will attempt to match the coordinates to a city it knows about, and if a match is found, will set the name accordingly.
2.  Revit will attempt to automatically adjust the time zone value to match the new Longitude or Latitude value set using SunAndShadowSettings.CalculateTimeZone(). For some boundary cases, the time zone calculated may not be correct and the TimeZone property can be set directly if necessary.

Properties include information about the longitude, latitude, place name, and time zone. Its methods are:

-   ConvertFromProjectTime - Converts project time to UTC time
-   ConvertToProjectTime - Converts local time or UTC time to project time
-   IsCompatibleWith - Checks whether the geographic coordinate system of this site is compatible with the given site
-   SiteLocation.SetGeoCoordinateSystem(string coordSystem) - sets the Geo coordinate system for the current document

## InternalOrigin

The InternalOrigin class represents the origin of Revit's internal coordinate system. Each Revit project contains one InternalOrigin. It has the following members:

-   InternalOrigin.Get(Document doc) - Returns the internal origin of the project
-   InternalOrigin.Position - Read-only property which returns the XYZ value of the internal coordinates. The position will always be (0,0,0)
-   InternalOrigin.SharedPosition - Read-only property which returns the shared position of the internal origin based on the active ProjectLocation of its project

## BasePoint

The BasePoint class represents the Project Base Point and Survey Point. Each Revit project contains one project base point and one survey point. The project base point represents the origin of the project coordinate system. The survey point represents the origin of the shared coordinate system.

-   BasePoint.Position - Gets the XYZ value corresponding to the base point's position in Revit's internal coordinates
-   BasePoint.SharedPosition - Gets the XYZ value corresponding to the base point's position in the transformed (shared) coordinates
-   BasePoint.GetProjectBasePoint() - Gets the project base point
-   BasePoint.GetSurveyPoint() - Gets the survey point
-   BasePoint.Clipped gets and sets the clipped state of the survey point BasePoint based on the active ProjectLocation of its Document. For the project base point, it will always return false and attempting to set it will throw an exception.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F3A532FC-E537-4CD5-A351-48AC48C21092-low.png)**Figure 123: Project Place**
