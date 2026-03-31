---
created: 2026-01-28T21:00:27 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_Detail_Curve_html
author: 
---

# Help | Detail Curve | Autodesk

> ## Excerpt
> Detail curve is an important Detail component usually used in the detail or drafting view. Detail curves are accessible in the DetailCurve class and its derived classes.

---
Detail curve is an important Detail component usually used in the detail or drafting view. Detail curves are accessible in the DetailCurve class and its derived classes.

DetailCurve is view-specific as are other annotation elements. However, there is no DetailCurve.View property. When creating a detail curve, you must compare the detail curve to the model curve view.

|| |--- | |Code Region 16-4: NewDetailCurve() and NewModelCurve()| |`public DetailCurve NewDetailCurve (View, Curve)`| |`public ModelCurve NewModelCurve (Curve, SketchPlane)`|

Generally only 2D views such as level view and elevation view are acceptable, otherwise an exception is thrown.

Except for view-related features, DetailCurve is very similar to ModelCurve. For more information about ModelCurve properties and usage, see [ModelCurve](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_ModelCurve_html) in the [Sketching](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_html) section.
