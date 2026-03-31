---
created: 2026-01-28T20:53:16 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Templates_html
author: 
---

# Help | View Templates | Autodesk

> ## Excerpt
> Element.Parameter.Set(integer)

---
View Scale Scale Value VIEW\_SCALE Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.Scale property To include/exclude in non-controlled parameters set, VIEW\_SCALE has to be usedtogether with with the following parameters: VIEW\_SCALE\_PULLDOWN\_IMPERIAL VIEW\_SCALE\_PULLDOWN\_METRIC Display Model VIEW\_MODEL\_DISPLAY\_MODE Valid for all plan views, Section, Elevation, Detail Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Valid values are 0 (Normal), 1 (Halftone) and 2 (Do not display) Detail Level VIEW\_DETAIL\_LEVEL Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.DetailLevel property Use also View.CanModifyDetailLevel() and View.HasDetailLevel() Parts Visibility VIEW\_PARTS\_VISIBILITY Valid for all plan views, all 3D views, Section, Elevation, Detail View.PartsVisibility property V/G Overrides Model VIS\_GRAPHICS\_MODEL Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetCategoryOverrides

View.SetCategoryOverrides

V/G Overrides Annotation VIS\_GRAPHICS\_ANNOTATION Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetCategoryOverrides

View.SetCategoryOverrides

V/G Overrides Analytical Model VIS\_GRAPHICS\_ANALYTICAL\_MODEL Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetCategoryOverrides

View.SetCategoryOverrides

V/G Overrides Import VIS\_GRAPHICS\_IMPORT Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetCategoryOverrides

View.SetCategoryOverrides

Imported categories are not built-in, so they can be found using other API operations V/G Overrides Filters VIS\_GRAPHICS\_FILTERS Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetFilters

View.GetFilterOverrides

View.SetFilterOverrides

V/G Overrides Worksets VIS\_GRAPHICS\_WORKSETS Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetWorksetVisibility

View.SetWorksetVisibility

Valid only if Document.IsWorkshared() is true

Use also View.IsWorksetVisible(�)

V/G Overrides RVT Links VIS\_GRAPHICS\_RVT\_LINKS Valid for all plan views, all 3D views, Section, Elevation, Detail No API access at the time (Revit 2020) Valid only if Revit links are present in the document V/G Overrides Point Clouds VIS\_GRAPHICS\_POINT\_CLOUDS Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetPointCloudOverrides

View.SetPointCloudOverrides

Valid only if PointCloudInstance elements are present in the document

Use also View.ArePointCloudsHidden()

V/G Overrides Coordination Model VIS\_GRAPHICS\_COORDINATION\_MODEL Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.GetDirectContext3DHandleOverrides Valid only if NavisWorks coordination models are linked in the document V/G Overrides Design Options VIS\_GRAPHICS\_DESIGN\_OPTIONS Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView, all schedules No API access at the time (Revit 2020) Valid only if design options other than �Main Model� are present in the document Model Display GRAPHIC\_DISPLAY\_OPTIONS\_MODEL Valid for all plan views, all 3D views, Section, Elevation, Detail View.GetViewDisplayModel

View.SetViewDisplayModel

Shadow GRAPHIC\_DISPLAY\_OPTIONS\_SHADOW Valid for all plan views, all 3D views, Section, Elevation, Detail No API access at the time (Revit 2020) Sketchy Lines GRAPHIC\_DISPLAY\_OPTIONS\_SKETCHY\_LINES Valid for all plan views, all 3D views, Section, Elevation, Detail View.GetSketchyLines

View.SetSketchyLines

Depth Cueing GRAPHIC\_DISPLAY\_OPTIONS\_FOG Valid for all plan views, all 3D views, Section, Elevation, Detail View.GetDepthCueing

View.SetDepthCueing

Use also View.CanUseDepthCueing() Lighting GRAPHIC\_DISPLAY\_OPTIONS\_LIGHTING Valid for all plan views, all 3D views, Section, Elevation, Detail Partial API access at the time (Revit 2020):

View.ShadowIntensity property

View.SunLightIntensity property

Photographic Exposure GRAPHIC\_DISPLAY\_OPTIONS\_PHOTO\_EXPOSURE Valid for all plan views, all 3D views, Section, Elevation, Detail API access provided only for 3D views:

View3D.GetRenderingSettings

View3D.SetRenderingSettings

Background GRAPHIC\_DISPLAY\_OPTIONS\_BACKGROUND Valid for all plan views, all 3D views, Section, Elevation, Detail View.GetBackground

View.SetBackGround

Far Clipping VIEWER\_BOUND\_FAR\_CLIPPING Section, Elevation, Detail Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Phase Filter VIEW\_PHASE\_FILTER Valid for all plan views, all 3D views, Section, Elevation, Detail, all schedules Element.Parameter.AsElementId()

Element.Parameter.Set(ElementId)

Discipline VIEW\_DISCIPLINE Valid for all plan views, all 3D views, Section, Elevation, Detail, DraftingView View.Discipline property Show Hidden Lines VIEW\_SHOW\_HIDDEN\_LINES Valid for all plan views, all 3D views, Section, Elevation, Detail Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Valid values are 0 (None), 1 (By Discipline), 2 (All) Color Scheme Location COLOR\_SCHEME\_LOCATION Valid for all plan views except for ceiling, Section, Elevation, Detail Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Valid values are 0 (Foreground), 1 (Background) Color Scheme VIEW\_SCHEMA\_SETTING\_FOR\_BUILDING Valid for all plan views except for ceiling, Section, Elevation, Detail No API access at the time (Revit 2020) Underlay Orientation VIEW\_UNDERLAY\_ORIENTATION Valid for all plan views ViewPlan.GetUnderlayOrientation

ViewPlan.SetUnderlayOrientation

View Range PLAN\_VIEW\_RANGE Valid for all plan views ViewPlan.GetViewRange

ViewPlan.SetViewRange

Orientation PLAN\_VIEW\_NORTH Valid for all plan views Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Valid values are 0 (Project North), 1 (True North) System Color Schemes VIEW\_SCHEMA\_SETTING\_FOR\_SYSTEM\_TEMPLATE Valid for all plan views except for ceiling No API access at the time (Revit 2020) Depth Clipping VIEW\_BACK\_CLIPPING Valid for all plan views Element.Parameter.AsInteger()

Element.Parameter.Set(integer)

Valid values are 0 (No Clip), 1 (Clip With Line), 2 (Clip With No Line) Rendering Settings VIEWER3D\_RENDER\_SETTINGS Valid for all 3D views View3D.GetRenderingSettings

View3D.SetRenderingSettings

Visual Style MODEL\_GRAPHICS\_STYLE\_ANON\_DRAFT Valid for DraftingView View.DisplayStyle property Use also View.HasDisplayStyle() Fields SCHEDULE\_FIELDS\_PARAM Valid for all schedules ViewSchedule.Definition.GetField

ViewSchedule.Definition.AddField

ViewSchedule.Definition.RemoveField

Filter SCHEDULE\_FILTER\_PARAM Valid for all schedules ViewSchedule.Definition.GetFilter

ViewSchedule.Definition.AddFilter

ViewSchedule.Definition.RemoveFilter

Sorting/Grouping SCHEDULE\_GROUP\_PARAM Valid for all schedules ViewSchedule.Definition.GetSortGroupField

ViewSchedule.Definition.AddSortGroupField

ViewSchedule.Definition.RemoveSortGroupField

Formatting SCHEDULE\_FORMAT\_PARAM Valid for all schedules ViewSchedule.Definition.GetField().IsHidden

ViewSchedule.Definition.GetField().ColumnHeading

ViewSchedule.Definition.GetField().GetFormatOptions

ViewSchedule.Definition.GetField().SetFormatOptions

etc.

Appearance SCHEDULE\_SHEET\_APPEARANCE\_PARAM Valid for all schedules ViewSchedule.Definition.ShowTitle

ViewSchedule.Definition.ShowHeaders

etc.
