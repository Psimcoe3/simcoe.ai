---
created: 2026-01-28T20:49:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_html
author: 
---

# Help | Shared Parameters | Autodesk

> ## Excerpt
> Shared Parameters are parameter definitions stored in an external text file.

---
Shared Parameters are parameter definitions stored in an external text file.

The definitions are identified by a unique identifier generated when the definition is created and can be used in multiple projects.

The main objects associated with shared parameters are:

-   DefinitionFile - represents a shared parameters file on disk
-   DefinitionGroup - group of shared parameters which are organized into meaningful sets
-   ExternalDefinition - represents a shared parameter definition, belongs to a DefinitionGroup
-   ExternalDefinitions - supports the creation of new shared parameters definitions
-   Binding - binds a parameter definition to one or more categories
-   BindingMap - contains all the parameter bindings that exist in the Autodesk Revit project
-   ParameterElement - stores information about a particular user-defined parameter in the document
-   SharedParameterElement - derived from ParameterElement, stores the definition of a shared parameter The following sections describe how to gain access to shared parameter definitions through the Revit Platform API, including how to get a shared parameter definition and bind it to Elements in certain Categories.

To access Shared Parameters after they are defined and bound to categories, see [Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Built_In_Parameters_html "Revit provides a general mechanism for giving each element a set of parameters that you can edit.").

## Clearing the value of a parameter

`Parameter.ClearValue()` resets the value of a shared parameter with the HideWhenNoValue flag to a cleared state. This method is not applicable to clear the value of any other parameter type.

### Hiding empty parameters

The property `ExternalDefinition.HideWhenNoValue` indicates if the shared parameter should be hidden from the property palette and `Element.GetOrderedParameters()` when it has no value.

This can be set when creating a shared parameter by setting `ExternalDefinitionCreationOptions.HideWhenNoValue` There is also `SharedParameterElement.ShouldHideWhenNoValue()`

### Filtering by presence or absence of parameter value

These filter classes define filter rules evaluating whether or not a parameter has a value for a specific element:

-   ParameterValuePresenceRule
-   HasValueFilterRule
-   HasNoValueFilterRule

These static methods create an instance of these rules for use in a parameter filter.:

-   FilterRule.CreateHasValueParameterRule()
-   FilterRule.CreateHasNoValueParameterRule()

In schedules, use these new enumerated values with the method `ScheduleDefinition.CanFilterByValuePresence()` to filter based on the presence or absence of a value assigned to that parameter:

-   ScheduleFilterType.HasValue
-   ScheduleFilterType.HasNoValue
