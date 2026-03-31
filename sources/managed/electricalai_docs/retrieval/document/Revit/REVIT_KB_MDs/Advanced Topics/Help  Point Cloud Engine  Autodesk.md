---
created: 2026-01-28T21:19:43 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Point_Clouds_Point_Cloud_Engine_html
author: 
---

# Help | Point Cloud Engine | Autodesk

> ## Excerpt
> A custom point cloud engine can be implemented to supply cloud points to Revit.

---
A custom point cloud engine can be implemented to supply cloud points to Revit.

A point cloud engine can be file-based or non-file-based. A file-based implementation requires that each point cloud be mapped to a single file on disk. Revit will allow users to create new point cloud instances in a document directly by selecting point cloud files whose extension matches the engine identifier. These files are treated as external links in Revit and may be reloaded and remapped when necessary from the Manage Links dialog.

A non-file-based engine implementation may obtain point clouds from anywhere (e.g. from a database, from a server, or from one part of a larger aggregate file). Because there is no file that the user may select, Revit's user interface will not allow a user to create a point cloud of this type. Instead, the engine provider supplies a custom command using PointCloudType.Create() and PointCloudInstance.Create() to create and place point clouds of this type. The Manage Links dialog will show the point clouds of this type, but since there is no file associated with the point cloud, the user cannot manage, reload or remap point clouds of this type.

Regardless of the type of implementation, a custom engine implementation consists of the following:

-   An implementation of IPointCloudEngine registered with Revit via the PointCloudEngineRegistry.
-   An implementation of IPointCloudAccess which will respond to inquiries from Revit regarding the properties of a single point cloud.
-   An implementation of IPointSetIterator which will return sets of points to Revit when requested.

In order to supply the points of the point cloud to Revit, there are two ReadPoints() methods which must be implemented:

-   IPointCloudAccess.ReadPoints() - this provides a single set of points in a one-time call, either from Revit or the API. Revit uses this during some display activities including selection pre-highlighting. It is also possible for API clients to call this method directly via PointCloudInstance.GetPoints().
-   IPointSetIterator.ReadPoints() - this provides a subset of points as a part of a larger iteration of points in the cloud. Revit uses this method during normal display of the point cloud; quantities of points will be requested repeatedly until it obtains enough points or until something in the display changes. The engine implementation must keep track of which points have been returned to Revit during any given point set iteration.

See the PointCloudEngine folder under the Samples directory included with the Revit API SDK for a complete example of registering and implementing both file-based and non-file-based point cloud engines.
