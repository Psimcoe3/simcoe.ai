---
created: 2026-01-28T21:10:21 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Analysis_Link_html
author: 
---

# Help | Analysis Link | Autodesk

> ## Excerpt
> With Revit, a structural analytical model is automatically generated as you create the physical model. The analytical model is linked to structural analysis applications, and the physical model is automatically updated from the results through the Revit API. Some third-party software developers already provide bi-directional links to their structural analysis applications. These include the following:

---
With Revit, a structural analytical model is automatically generated as you create the physical model. The analytical model is linked to structural analysis applications, and the physical model is automatically updated from the results through the Revit API. Some third-party software developers already provide bi-directional links to their structural analysis applications. These include the following:

-   ADAPT-Builder Suite from ADAPT Corporation ([www.adaptsoft.com/revitstructure/](http://www.adaptsoft.com/revitstructure/))
-   Fastrak and S-Frame from CSC ([www.cscworld.com](http://www.cscworld.com/))
-   ETABS from CSI ([www.csiberkeley.com/](http://www.csiberkeley.com/))
-   RFEM from Dlubal ([www.dlubal.com/en/download/rfem\_revit\_en.pdf](https://www.dlubal.com/en/download/rfem_revit_en.pdf))
-   Advance Design, VisualDesign, Arche, Effel and SuperSTRESS from GRAITEC ([www.graitec.com/En/revit.asp](http://www.graitec.com/En/revit.asp))
-   Scia Engineer from Nemetschek ([www.scia.net/en/software/product-selection/scia-engineer](https://www.scia.net/en/software/product-selection/scia-engineer))
-   GSA from Oasys Software (Arup) ([www.oasys-software.com/products](http://www.oasys-software.com/products))
-   ProDESK from Prokon Software Consultants ([www.prokon.com/](http://www.prokon.com/))
-   RAM Structural System from Bentley ([www.bentley.com/en/products/product-line/structural-analysis-software/ram-structural-system](https://www.bentley.com/en/products/product-line/structural-analysis-software/ram-structural-system))
-   RISA-3D and RISAFloor from RISA Technologies ([www.risatech.com/partner/revit\_structure.asp](http://www.risatech.com/partner/revit_structure.asp))
-   SOFiSTiK Structural Desktop Suite from SOFiSTiK ([www.sofistik.com](http://www.sofistik.com/))
-   SPACE GASS from SPACE GASS ([www.spacegass.com/revit](http://www.spacegass.com/revit))
-   Robot Structural Analysis Professional from Autodesk ([www.autodesk.com/products/robot-structural-analysis](http://www.autodesk.com/products/robot-structural-analysis))

The key to linking Revit to other analysis applications is to set up the mapping relationship between the objects in different object models. That means the difficulty and level of the integration depends on the similarity between the two object models.

For example, during the product design process, design a table with at least the first two columns in the object mapping in the following table: one for the Revit API and the other for the structural analysis application, shown as follows:

**Table 62: Revit and Analysis Application Object Mapping**

<table summary="" id="GUID-0A4C2D6C-725B-4561-A125-7B341BF05C1F__TABLE_D81C0B850B734CE09B6B55768EBBD590"><tbody><tr><td><b>Revit API</b></td><td><b>Analysis Application</b></td><td><b>Import to Revit</b></td></tr><tr><td>StructuralColumn</td><td>Column</td><td>NewStructuralColumn</td></tr><tr><td>Property:</td><td></td><td></td></tr><tr><td>…</td><td></td><td></td></tr><tr><td>Location</td><td></td><td>Read-only;</td></tr><tr><td>Parameter:</td><td></td><td></td></tr><tr><td>…</td><td></td><td></td></tr><tr><td>Analyze as</td><td></td><td>Editable;</td></tr><tr><td>AnalyticalModel:</td><td></td><td></td></tr><tr><td>…</td><td></td><td></td></tr><tr><td>Profile</td><td></td><td>Read-only;</td></tr><tr><td>RigidLink</td><td></td><td>Read-only;</td></tr><tr><td>…</td><td></td><td></td></tr><tr><td>Material:</td><td></td><td></td></tr><tr><td>…</td><td></td><td></td></tr></tbody></table>
