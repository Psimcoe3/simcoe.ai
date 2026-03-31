---
created: 2026-01-28T20:43:25 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Element Classification | Autodesk

> ## Excerpt
> Revit Elements are divided into six groups: Model, Sketch, View, Group, Annotation and Information. Each group contains related Elements and their corresponding symbols.

---
Revit Elements are divided into six groups: Model, Sketch, View, Group, Annotation and Information. Each group contains related Elements and their corresponding symbols.

### Model Elements

Model Elements represent physical items that exist in a building project. Elements in the Model Elements group can be subdivided into the following:

-   Family Instances - Family Instances contain family instance objects. You can load family objects into your project or create them from family templates. For more information, see [Family Instances](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_html).
-   Host Elements - Host Elements contain system family objects that can contain other model elements, such as wall, roof, ceiling, and floor. For more information about Host Elements, see [Walls, Floors, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html).
-   Structure Elements. - Structure Elements contain elements that are only used in the structural features of Revit. For more information about Structure Elements, see [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html).
    
    ### View Elements
    

View Elements represent the way you view and interact with other objects in Revit. For more information, see [Views](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_html).

### Group Elements

Group Elements represent the assistant Elements such as Array and Group objects in Revit. For more information, see [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html).

### Annotation and Datum Elements

Annotation and Datum Elements contain non-physical items that are visible.

-   Annotation Elements represent 2D components that maintain scale on paper and are only visible in one view. For more information about Annotation Elements, see [Annotation Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_html).

Note Annotation Elements representing 2D components do not exist only in 2D views. For example, dimensions can be drawn in 3D view while the shape they refer to only exists in a 2D planar face.

-   Datum Elements represent non-physical items that are used to establish project context. These elements can exist in views. Datum Elements are further divided into the following:
-   Common Datum Elements - Common Datum Elements represent non-physical visible items used to store data for modeling.
-   Datum FamilyInstance - Datum FamilyInstance represents non-physical visible items loaded into your project or created from family templates. NoteFor more information about Common Datum Elements and Datum FamilyInstance, see [Datum and Information Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_html); for ModelCurve related contents, see [Sketching](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_html).
-   Structural Datum Elements - Structural Datum Elements represent non-physical visible items used to store data for structure modeling. For more information about Structural Datum Elements, see [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html).
    
    ### Sketch Elements
    

Sketch Elements represent temporary items used to sketch 2D/3D form. This group contains the following objects used in family modeling and massing:

-   SketchPlane
-   Sketch
-   Path3D
-   GenericForm.

For Sketch details, see [Sketching](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_html).

### Information Elements

Information Elements contain non-physical invisible items used to store project and application data. Information Elements are further separated into the following:

-   Project Datum Elements
-   Project Datum Elements (Unique).

For more information about Datum Elements, see [Datum and Information Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_html).
