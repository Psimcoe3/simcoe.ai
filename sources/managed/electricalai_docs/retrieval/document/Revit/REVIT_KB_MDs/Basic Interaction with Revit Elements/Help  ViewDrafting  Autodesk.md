---
created: 2026-01-28T20:51:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_ViewDrafting_html
author: 
---

# Help | ViewDrafting | Autodesk

> ## Excerpt
> Views to create unassociated, view-specific details that are not part of the modeled design.

---
Views to create unassociated, view-specific details that are not part of the modeled design.

The drafting view is not associated with the model. It allows the user to create detail drawings that are not included in the model.

-   In the drafting view, the user can create details in different view scales (coarse, fine, or medium).
    
-   You can use 2D detailing tools, including:
    
    <table summary="" id="GUID-217A0AFB-5A0C-4EC3-A417-C7F8F78D05B5__TABLE_4FA9C3F4D7BF4A4F91790596A66C169B"><tbody><tr><td><ul><li>Detail lines</li><li>Detail regions</li><li>Detail components</li><li>Insulation</li></ul></td><td><ul><li>Reference planes</li><li>Dimensions</li><li>Symbols</li><li>Text</li></ul></td></tr></tbody></table>
    

These tools are the same tools used to create a detail view.

-   Drafting views do not display model elements.

Use the static ViewDrafting.Create() method to create a drafting view. Model elements are not displayed in the drafting view.

### ImageView

The ImageView class is derived from ViewDrafting. It can be used to create rendering views containing images imported from disk. Use the static ImageView.Create(Document, ImageTypeOptions) method to create new rendering views.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/RenderingView-76170.jpg)
