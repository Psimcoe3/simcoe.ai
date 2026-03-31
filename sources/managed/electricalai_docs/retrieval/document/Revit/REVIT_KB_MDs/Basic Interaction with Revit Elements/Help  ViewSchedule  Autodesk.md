---
created: 2026-01-28T20:52:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_ViewSchedule_html
author: 
---

# Help | ViewSchedule | Autodesk

> ## Excerpt
> A schedule is a tabular representation of data. A typical schedule shows all elements of a category (doors, rooms, etc.) with each row representing an element and each column representing a parameter.

---
A schedule is a tabular representation of data. A typical schedule shows all elements of a category (doors, rooms, etc.) with each row representing an element and each column representing a parameter.

The ViewSchedule class represents schedules and other schedule-like views, including single-category and multi-category schedules, key schedules, material takeoffs, view lists, sheet lists, keynote legends, revision schedules, and note blocks.

The ViewSchedule.Export() method will export the schedule data to a text file.

TableData.ZoomLevel allows the user to set the zoom level of a schedule in a tabular view. This setting will not change the size of text, rows, or columns in a sheet view. Additionally, the setting is temporary and only applies to the current session.

## Placing Schedules on Sheets

The static ScheduleSheetInstance.Create() method creates an instance of a schedule on a sheet. It requires the ID of the sheet where the schedule will be placed, the ID of the schedule view, and the XYZ location on the sheet where the schedule will be placed. The ScheduleSheetInstance object has properties to access the ID of the "primary" schedule that generates this ScheduleSheetInstance, the rotation of the schedule on the sheet, the location on the sheet where the schedule is placed (in sheet coordinates), as well as a flag that identifies if the ScheduleSheetInstance is a revision schedule in a titleblock family.

The `GetScheduleHeightsOnSheet` method returns the height of the column headers, row heights, and schedule title.

## Striped rows

These properties provide access to read or set if a given schedule is using a striped row display, and whether that display will be used on a sheet that displays this schedule:

-   ViewSchedule.HasStripedRows
-   ViewSchedule.UseStripedRowsOnSheets

These methods get and set the color applied to the indicated part of the pattern for a schedule with striped rows:

-   ViewSchedule.GetStripedRowsColor()
-   ViewSchedule.SetStripedRowsColor()

`ViewSchedule.IsHeaderFrozen` provides access to read or set if the header is frozen on a given schedule.

## Split Schedules

Schedules can be split, and the resulting segments can be split, merged, and deleted. An overload of `ScheduleSheetInstance.Create` exists to place a schedule segment on a sheet.

## Filtering By Sheet

With the `ScheduleDefinition.IsFilteredBySheet` property, you can define if the `ScheduleSheetInstance` will list only the elements visible in the viewports on that sheet.
