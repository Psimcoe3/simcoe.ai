---
created: 2026-01-28T21:15:47 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Path_Of_Travel_html
author: 
---

# Help | Path Of Travel | Autodesk

> ## Excerpt
> The path of travel element allows you to analyze travel distances and times between 2 selected points in your model. The path of travel is generated based on the model elements acting as obstacles along the path of travel. It avoids contact with model elements in the analysis zone and calculates the shortest distance between the start and end points.

---
The path of travel element allows you to analyze travel distances and times between 2 selected points in your model. The path of travel is generated based on the model elements acting as obstacles along the path of travel. It avoids contact with model elements in the analysis zone and calculates the shortest distance between the start and end points. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/PathOfTravel.png)

The class `Autodesk.Revit.DB.Analysis.PathOfTravel` represents this path element.

Members of this class include:

-   PathOfTravel.Create() - creates a single PathOfTravel element given a start and end point.
-   PathOfTravel.CreateMultiple() - creates multiple PathOfTravel elements given arrays of start and end points.
-   PathOfTravel.CreateMapped() - creates multiple PathOfTravel elements by mapping each of a set of start points to each of a set of end points.
-   PathOfTravel.GetCurves()
-   PathOfTravel.LineStyle
-   PathOfTravel.PathStart
-   PathOfTravel.PathMidpoint
-   PathOfTravel.PathEnd
-   PathOfTravel.Update()
-   PathOfTravel.UpdateMultiple()

The class `Autodesk.Revit.DB.Analysis.RouteAnalysisSettings` represents a settings element which contains project-wide settings for route calculations in plan views. Currently, these settings are only used by the Autodesk.Revit.DB.Analysis.PathOfTravel element, but in the future they can be used by any other functionalities which do route calculations.

Members of this class include:

-   RouteAnalysisSettings.EnableIgnoredCategoryIds() - enable ignoring specified categories of elements during calculations
-   RouteAnalysisSettings.SetIgnoredCategoryIds() - sets the categories to be ignored during calculations
-   RouteAnalysisSettings.AnalysisZoneTopOffset - the analysis zone top (an offset above the level of the plan view)
-   RouteAnalysisSettings.AnalysisZoneBottomOffset - the analysis zone bottom (an offset above the level of the plan view)
-   RouteAnalysisSettings.IgnoreImports - If true, import instances are ignored by route calculation

## Reveal Obstacles mode for Path of Travel

The Reveal Obstacles view mode highlights elements in the plan view when those elements will act as obstacles for the current Path of Travel calculation settings. These methods provide access to read or set if a view is displaying this mode:

-   PathOfTravel.IsInRevealObstaclesMode()
-   PathOfTravel.SetRevealObstaclesMode()

## Path finding analysis for Path of Travel

`List<XYZ> PathOfTravel.FindStartsOfLongestPathsFromRooms(View view, List<XYZ> destinationPoints)` For a floor plan view, calculates paths from points inside rooms to the closests of the destinations. Returns the start points of the longest path(s). If multiple paths have the same longest length, returns multiple start points. The entire plan is divided in small tiles, and the distance to the closest destination point is calculated for each tile center point. Only tile center points that are located in rooms in the view are taken into account.

`List<XYZ> PathOfTravel.FindEndsOfShortestPaths(View view, List<XYZ> destinationPoints, List<XYZ> startPoints)` For a floor plan view, calculates the paths from each start point to its closest destination and return the path end points. The calculation is done in a floor plan with one or more destinationPoints and one or more startPoints. The shortest path is calculated from each start point to its corresponding closest destination.

`List<List<XYZ>> PathOfTravel.FindShortestPaths(View view, List<XYZ> destinationPoints, List<XYZ> startPoints)` For a floor plan view, calculates paths from each start point to its closest destinations. Returns the path, represented by an array of XYZ points. The calculation is done in a floor plan with one or more destinationPoints and one or more startPoints. The shortest path is calculated from each start point to its closest destination point.

## Waypoints

These methods provide access to read and modify the waypoints associated to a particular PathOfTravel element. Waypoints force the path of travel calculation to ensure that the path includes each of the specified points, in the order specified, between the start and end points.

-   PathOfTravel.GetWaypoints()
-   PathOfTravel.InsertWaypoint()
-   PathOfTravel.SetWaypoint()
-   PathOfTravel.RemoveWaypoint()
