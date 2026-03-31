---
created: 2026-01-28T21:01:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Working_with_Curves_html
author: 
---

# Help | Working with Curves | Autodesk

> ## Excerpt
> The Curve class provides useful methods for working with curves.

---
The Curve class provides useful methods for working with curves.

In addition to [methods that are useful for analysis](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Curves_Curve_analysis_html "There are several Curve methods which are tools suitable for use in geometric analysis.") , the Curve class provides properties and methods to modify a curve or get basic information about it.

## Changing bounds

The MakeBound() method can be used to change the bounds of a curve or to create bounds for a previously unbound curve. MakeUnbound() will make the curve unbound. For both methods, if the curve is marked as read-only (because it was extracted directly from a Revit element or collection/aggregation object), calling this method causes the object to be changed to carry a disconnected copy of the original curve. The modification will not affect the original curve or the object that supplied it.

## Graphics style

Curve inherits the GraphicsStyleId read-only property from GeometryObject, which provides the ElementId of the GraphicsStyle assigned to the Curve. The method Curve.SetGraphicsStyleId() can be used to set the GraphicsStyle Id of the Curve. Many methods in the Revit API will not use the graphics style associated to this curve. For example, curves used as portions of the sketch of an element will not read this property. Newly created curve elements will not use this value either, as they inherit their graphical properties from their associated category.

## Curve length

Curve has two properties associated with length. The Length property will return the exact length of the curve. I computes the length of the curve using analytical or numeric integration. There is no performance hit for lines and arcs. For a faster approximation, the ApproximateLength property quickly estimates the length of the curve, but it may deviate by a factor of 2 in some cases. This computation is exact for lines and arcs.
