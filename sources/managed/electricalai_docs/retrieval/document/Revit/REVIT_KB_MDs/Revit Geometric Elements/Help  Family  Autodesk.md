---
created: 2026-01-28T20:58:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Family_html
author: 
---

# Help | Family | Autodesk

> ## Excerpt
> The Family class represents an entire Revit family. It contains the FamilySymbols used by FamilyInstances.

---
The Family class represents an entire Revit family. It contains the FamilySymbols used by FamilyInstances.

### Loading Families

The Document class contains the LoadFamily() and LoadFamilySymbol() methods.

-   LoadFamily() loads an entire family and all of its types or symbols into the project.
-   LoadFamilySymbol() loads only the specified family symbol from a family file into the project.

Note: To improve the performance of your application and reduce memory usage, if possible load specific FamilySymbols instead of entire Family objects.

-   The family file path is retrieved using the Options.Application object GetLibraryPaths() method.
-   The Options.Application object is retrieved using the Application object Options property.
-   In LoadFamilySymbol(), the input argument Name is the same string value returned by the FamilySymbol object Name property.

For more information, refer to [Code Samples](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Code_Samples_html).

### Categories

The Family.FamilyCategory property indicates the category of the Family such as Columns, Furniture, Structural Framing, or Windows.
