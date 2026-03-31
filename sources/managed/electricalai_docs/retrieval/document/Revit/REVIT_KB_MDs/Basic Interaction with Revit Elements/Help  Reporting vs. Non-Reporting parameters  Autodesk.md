---
created: 2026-01-28T20:50:03 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Reporting_vs_Non_Reporting_parameters_html
author: 
---

# Help | Reporting vs. Non-Reporting parameters | Autodesk

> ## Excerpt
> The most significant difference in types of global parameters is whether they are reporting or non-reporting.

---
The most significant difference in types of global parameters is whether they are reporting or non-reporting.

## What are reporting and non-reporting parameters?

There are several ways global parameters can be categorized, but probably the most significant categorization stems from the GlobalParameter.IsReporting property which divides global parameters into two groups - Reporting and Non-Reporting. The significance of reporting parameters lays in the fact that their values are driven by the dimension that has been labeled by a reporting parameter. It means that the value of a reporting parameter reflects the value of a dimension (length or angle) and gets updated anytime the dimension changes. Non-Reporting parameters behave in the opposite manner - they drive value of dimensions that have been labeled by them, which results in controlling the model's geometry through global parameters' values.

Reporting parameters are limited in several ways. They can be only of **Length** or **Angle** type, a requirement due to the fact that a dimension must be able to drive the value. For the same reason reporting parameters may not have formulas.

Non-Reporting parameters, on the other way, can be of almost any type (**Length**, **Integer**, **Area**, etc.) with the exception of ElementId type. Also, Non-Reporting parameters may have assigned formulas in which other global parameters may be used as arguments. This way one global parameter's value can be derived from other parameter (or parameters), and the other parameter can be either reporting or non-reporting.

Other important properties of global parameters are IsDrivenByDimension and IsDrivenByFormula, which are mutually exclusive - a parameter that has a formula assigned cannot be driven by a dimension (nor can be reporting) and vice versa.

## Making a global parameter reporting or non-reporting

Global parameters are initially non-reporting upon creation, but can be set to reporting use the GlobalParameter.IsReporting property once a global parameter is created and is of an eligible type. Use GlobalParameter.HasValidTypeForReporting() to ensure that a certain data type can be made reporting. Note, that a parameter may not be made reporting after more than one dimension has been labeled by it. It is because reporting parameters can label (and be driven) by one dimension only.

An alternative way of making a parameter reporting is via the GlobalParameter.SetDrivingDimension() method which labels one dimension by a global parameter and also makes the parameter reporting if it is not reporting yet.

Although parameters driven by a dimension are automatically made reporting, parameters driven by a formula are not. In order to set a formula, the global parameter must be non-reporting. Therefore a reporting parameter must be changed to non-reporting first before assigning a formula.
