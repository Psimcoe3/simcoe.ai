---
created: 2026-01-28T20:42:44 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | ForgeTypeId | Autodesk

> ## Excerpt
> Autodesk.Revit.DB.ForgeTypeId is an extensible identifier for a unit, symbol, or other object, and is used throughout the Revit API to identify data such as units of measurement, symbols, and unit types. Unit types are referred to as "specs" to avoid confusion with units themselves.

---
`Autodesk.Revit.DB.ForgeTypeId` is an extensible identifier for a unit, symbol, or other object, and is used throughout the Revit API to identify data such as units of measurement, symbols, and unit types. Unit types are referred to as "specs" to avoid confusion with units themselves.

A `ForgeTypeId` instance holds a string, called a "typeid", that uniquely identifies a Forge schema. A Forge schema is a JSON document describing a data structure, supporting data interchange between applications. A typeid string includes a namespace and version number such as

-   `autodesk.spec.aec:length-1.0.0`
-   `autodesk.unit.unit:meters-1.0.0`
-   `autodesk.revit.category.local:walls-1.0.0`

By default, comparison of ForgeTypeId values in the Revit API ignores the version number.

The members of the following classes have a ForgeTypeId data type:

-   DisciplineTypeId - Product disciplines used in the Revit UI such as Architecture, Electrical, HVAC, Piping, and Structural
-   GroupTypeId - Groupings used for parameters in the Revit UI such as Construction, General, Geometry, IdentityData
-   ParameterTypeId - Type of parameters such as AllModelInstanceComments, InstanceSillHeightParam, WallTopOffset
-   SpecTypeId - Type of quantity to be measured such as Area, Currency, HvacDensity, Wattage
-   SymbolTypeId - Unit symbol displayed in the formatted string representation of a number to indicate the units of the value, such as DegreeC, Ft, KipPerFt, MSup2
-   UnitTypeId - Units and display format used to format numbers as strings or convert units such as Acres, Degrees, Feet, Liters

For example, the following properties all have a ForgeTypeId data type:

-   DisciplineTypeId.Architecture
-   GroupTypeId.Constraints
-   ParameterTypeId.WallTopOffset
-   SpecTypeId.Volume
-   SymbolTypeId.Hour
-   UnitTypeId.Millimeters

These static methods convert a BuiltInCategory to a ForgeTypeId and vice versa.

-   Category.GetBuiltInCategoryTypeId(BuiltInCategory)
-   Category.GetBuiltInCategory(ForgeTypeId)

For example, `Category.GetBuiltInCategoryTypeId(BuiltInCategory.OST_Furniture)` returns a `ForgeTypeId` with a `TypeId` equal to `autodesk.revit.category.family:furniture-1.0.0`
