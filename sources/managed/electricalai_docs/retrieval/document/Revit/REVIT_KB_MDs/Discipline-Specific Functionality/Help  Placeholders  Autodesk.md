---
created: 2026-01-28T21:08:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Element_Creation_Placeholders_html
author: 
---

# Help | Placeholders | Autodesk

> ## Excerpt
> The Revit API provides the ability to put placeholder elements into a system when the exact design of the layout is not yet know. Using placeholder ducts and pipes can allow for a well-connected system while the design is still unknown, and then which can then be elaborated in the final design at a later stage.

---
### Placeholder ducts and pipes

The Revit API provides the ability to put placeholder elements into a system when the exact design of the layout is not yet know. Using placeholder ducts and pipes can allow for a well-connected system while the design is still unknown, and then which can then be elaborated in the final design at a later stage.

The two static methods Duct.CreatePlaceholder() and Pipe.CreatePlaceholder() create placeholder elements. The IsPlaceholder property of Duct and Pipe indicates whether they are a placeholder element or not.

When ready to create actual ducts and pipes from the placeholders, use the MechanicalUtils.ConvertDuctPlaceholders() and PlumbingUtils.ConvertPipePlaceholders() methods to convert a set of placeholder elements to ducts and pipes. Once conversion succeeds, the placeholder elements are deleted. The new duct, pipe and fitting elements are created and connections are established.
