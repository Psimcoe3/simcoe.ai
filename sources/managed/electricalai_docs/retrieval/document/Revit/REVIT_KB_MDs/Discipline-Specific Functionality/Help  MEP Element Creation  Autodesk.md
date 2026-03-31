---
created: 2026-01-28T21:08:03 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Element_Creation_html
author: 
---

# Help | MEP Element Creation | Autodesk

> ## Excerpt
> MEP Elements can be created using the Revit API.

---
MEP Elements can be created using the Revit API.

Many elements related to duct, pipe and electrical systems can be created using the following methods available in the Autodesk.Revit.Creation.Document class:

-   NewFlexDuct
-   NewFlexPipe
-   NewMechanicalSystem
-   NewPipingSystem
-   NewCrossFitting
-   NewElbowFitting
-   NewTakeoffFitting
-   NewTeeFitting
-   NewTransitionFitting
-   NewUnionFitting

Other MEP elements, such as pipes, can only be created using the static Create() method of its corresponding class. Some MEP elements, such as ducts, can be created by a static method of the corresponding class (i.e. Duct) or by a method of the Autodesk.Revit.Creation.Document class. For these elements, the static Create() method is preferred.

-   Duct
-   FlexDuct
-   Pipe
-   FlexPipe
-   PipingSystem
-   Wire
