---
created: 2026-01-28T21:15:37 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Analysis_Visualization_Updating_Analysis_Results_html
author: 
---

# Help | Updating Analysis Results | Autodesk

> ## Excerpt
> The Revit analysis framework does not update results automatically, and potentially any change to Revit model can invalidate results.

---
The Revit analysis framework does not update results automatically, and potentially any change to Revit model can invalidate results.

In order to keep results up to date, API developers should use [Dynamic Model Update](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_html) triggers or subscribe to the [DocumentChanged event](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Database_Events_DocumentChanged_event_html) to be notified when the Revit model has changed and previously calculated results may be invalid and in need of recalculation. For an example showing Dynamic Model Update together with Analysis Visualization, see the DistanceToSurfaces sample in the Revit SDK.
