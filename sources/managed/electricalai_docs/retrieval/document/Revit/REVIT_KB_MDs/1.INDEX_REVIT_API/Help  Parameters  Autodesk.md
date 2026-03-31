---
created: 2026-01-28T21:34:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_html
author: 
---

# Help | Parameters | Autodesk

> ## Excerpt
> Revit provides a general mechanism for giving each element a set of parameters that you can edit.

---
Revit provides a general mechanism for giving each element a set of parameters that you can edit.

In the Revit UI, some element parameters are visible in the Element Properties Palette. The following sections describe how to get and use built-in parameters, shared parameters and global parameters.

In the Revit Platform API, Parameters are managed in the Element class. You can access Parameters in these ways:

Common ways to get the value of a parameter are shown below. In this sample, all three lines of code get the same parameter. Because this parameter is stored as a string, the `AsString()` method is used to get its value.

```
private void GetStringParameterValue(Wall wall)
{
    string s1 = wall.LookupParameter("Comments").AsString();
    string s2 = wall.GetParameter(ParameterTypeId.AllModelInstanceComments).AsString();
    string s3 = wall.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS).AsString();
}
```

Other ways to get a parameter are:

-   By iterating through the Element.Parameters collection of all parameters for an Element (for an example, see the sample code in [Walkthrough Get Selected Element Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Walkthrough_Get_Selected_Element_Parameters_html)).
-   By iterating through the collection returned by Element.GetOrderedParameters(), which returns only parameters visible in the Properties Palette.
-   By accessing a parameter by name via the Element.ParametersMap collection or Element.GetParameters()

You can retrieve the Parameter object from an Element using the overloaded Parameter property if you know the built-in ID, definition, or GUID. The Parameter\[GUID\] property overload gets a shared parameter based on its Global Unique ID (GUID), which is assigned to the shared parameter when it's created.

The Element.LookupParameter() method gets a parameter based on its localized name, so your code should handle different languages if it's going to look up parameters by name and needs to run in more than one locale. Also, keep in mind that multiple matches of parameters with the same name can occur because shared parameters or project parameters can be bound to an element category even if there is already a built-in parameter with the same name. For this reason, it is better to use Element.GetParameters() which will return all parameters matching the given name. Element.LookupParameter() will return the first match found.
