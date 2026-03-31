---
created: 2026-01-28T21:15:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Analysis_Visualization_html
author: 
---

# Help | Analysis Visualization | Autodesk

> ## Excerpt
> The Revit API provides a mechanism for external analysis applications to easily display the results of their computation in the Revit model. The SpatialFieldManager class is the main class for communicating analysis results back to Revit. It is used to create, delete, and modify the "containers" in which the analysis results are stored. The AnalysisResultSchema class contains all information about one analysis result, such as a description and the names and multipliers of all units for result visualization. Multiple AnalysisResultSchemas can be registered with the SpatialFieldManager.

---
The Revit API provides a mechanism for external analysis applications to easily display the results of their computation in the Revit model. The SpatialFieldManager class is the main class for communicating analysis results back to Revit. It is used to create, delete, and modify the "containers" in which the analysis results are stored. The AnalysisResultSchema class contains all information about one analysis result, such as a description and the names and multipliers of all units for result visualization. Multiple AnalysisResultSchemas can be registered with the SpatialFieldManager.

The AnalysisDisplayStyle class can then be used to control the appearance of the results. Creation and modification of AnalysisDisplayStyle from a plug-in is optional; end users can have the same control over the presentation of the analysis results with the Revit UI.

The data model supported by Revit API requires that analysis results are specified at a certain set of points, and that at each point one or more distinct numbers ("measurements") are computed. The number of measurements must be the same at all model points. The results data is transient; it is stored only in the model until the document is closed. If the model is saved, closed, and reopened the analysis results will not be present.
