---
created: 2026-01-28T20:53:11 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_UIView_html
author: 
---

# Help | UIView | Autodesk

> ## Excerpt
> While the View class is the base class for all view types in Revit and keeps tracks of elements in the view, the UIView class contains data about the view windows in the Revit user interface. A list of all open views can be retrieved from the UIDocument using the GetOpenUIViews() method. The UIView class has methods to get information about the views drawing area as well as to pan and zoom the active view.

---
While the View class is the base class for all view types in Revit and keeps tracks of elements in the view, the UIView class contains data about the view windows in the Revit user interface. A list of all open views can be retrieved from the UIDocument using the GetOpenUIViews() method. The UIView class has methods to get information about the views drawing area as well as to pan and zoom the active view.

UIView.GetWindowRectangle() returns a rectangle that describes the size and placement of the UIView window. It does not include the window border or title bar.

### Zoom Operations

UIView has several methods related to zooming the active view. UIView.GetZoomCorners() gets the corners of the view's rectangle in model coordinates and UIView.ZoomAndCenterRectangle() offers the ability to zoom and pan the active view to center on the input region of the model.

The ZoomToFit() and ZoomSheetSize() methods provide quick ways to adjust the zoom of the window, while the Zoom() method can be used to zoom in or out by a specified factor.

### Closing a View

UIView.Close() can close a visible window. However, it cannot be used to close the last active window. Attempting to close the last active window will throw an exception.
