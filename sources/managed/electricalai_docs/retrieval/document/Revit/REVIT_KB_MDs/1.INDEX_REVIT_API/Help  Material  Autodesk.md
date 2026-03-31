---
created: 2026-01-28T21:34:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_html
author: 
---

# Help | Material | Autodesk

> ## Excerpt
> In the Revit Platform API, material data is stored and managed as an Element. Just as in the Revit UI, a material can have several assets associated with it, but only thermal and structural (referred to as Physical in the Revit UI) assets can be assigned using the API.

---
In the Revit Platform API, material data is stored and managed as an Element. Just as in the Revit UI, a material can have several assets associated with it, but only thermal and structural (referred to as Physical in the Revit UI) assets can be assigned using the API.

Some material features are represented by properties on the Material class itself, such as FillPattern, Color, or Render while others are available as properties of either a structural or thermal asset associated with the material.

In this chapter, you learn how to access material elements and how to manage the Material objects in the document. [Element Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Element_Material_html) provides a walkthrough showing how to get a window material.
