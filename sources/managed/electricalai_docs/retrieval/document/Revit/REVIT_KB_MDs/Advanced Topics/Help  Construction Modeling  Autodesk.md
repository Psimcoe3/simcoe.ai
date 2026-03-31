---
created: 2026-01-28T21:16:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Construction_Modeling_html
author: 
---

# Help | Construction Modeling | Autodesk

> ## Excerpt
> The Revit API allows elements to be divided into sub-parts or collected into assemblies to support construction modeling workflows, much the same way as can be done with the Revit user interface. Both parts and assemblies can be independently scheduled, tagged, filtered, and exported. You can also divide a part into smaller parts. After creating an assembly type, you can place additional instances in the project and generate isolated assembly views.

---
The Revit API allows elements to be divided into sub-parts or collected into assemblies to support construction modeling workflows, much the same way as can be done with the Revit user interface. Both parts and assemblies can be independently scheduled, tagged, filtered, and exported. You can also divide a part into smaller parts. After creating an assembly type, you can place additional instances in the project and generate isolated assembly views.

The main classes related to Construction Modeling are:

-   **AssemblyInstance** - This class combines multiple elements for tagging, filtering, scheduling and creating isolated assembly views.
-   **AssemblyType** - Represents a type for construction assembly elements. Each new unique assembly created in the project automatically creats a corresponding AssemblyType. A new AssemblyInstance can be placed in the document from an existing AssemblyType.
-   **PartUtils** - This utility class contains general part utility methods, including the ability to create parts, divide parts, and to get information about parts.
-   **AssemblyViewUtils** - A utility class to create various types of assembly views.
