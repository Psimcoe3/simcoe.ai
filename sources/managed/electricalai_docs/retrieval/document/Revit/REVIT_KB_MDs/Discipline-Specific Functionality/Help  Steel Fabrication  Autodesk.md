---
created: 2026-01-28T21:10:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Steel_Fabrication_html
author: 
---

# Help | Steel Fabrication | Autodesk

> ## Excerpt
> Autodesk.Revit.DB.Steel.SteelElementProperties attaches steel fabrication information to Revit elements.  Elements which can have fabrication information include:

---
## Linking between Revit elements and steel fabrication elements

Autodesk.Revit.DB.Steel.SteelElementProperties attaches steel fabrication information to Revit elements. Elements which can have fabrication information include:

-   FamilyInstance elements (structural beams and columns)
    
-   StructuralConnectionHandler elements
    
-   Specific steel connection elements (bolts, anchors, plates, etc). These connection elements will be of type Element but with categories related to structural connections, for example:
    
    -   OST\_StructConnectionWelds
    -   OST\_StructConnectionHoles
    -   OST\_StructConnectionShearStuds
    -   OST\_StructConnectionBolts
    -   OST\_StructConnectionAnchors
    -   OST\_StructConnectionPlates
-   Some concrete elements (walls, floors, concrete beams) when they are used as input elements to creation of steel connections.
    

Use SteelElementProperties.GetSteelElementProperties() to obtain the properties if they exist.

The properties contain SteelElementProperties.UniqueID which is the id of the object in fabrication terms, and can be used to determine the Steel Core element corresponding to this Revit element, for use with the Advance Steel API.

You can also look up the id for a Revit element using the static method SteelElementProperties.GetFabricationUniqueID().

For Revit elements which do not currently have a fabrication link, it can be added using: SteelElementProperties.AddFabricationInformationForRevitElements()

If you have a fabrication id, you can lookup the corresponding Revit element using: SteelElementProperties.GetReference(). This may return a reference to an element or a subelement.

## Custom steel connections

StructuralConnectionHandler.CreateGenericConnection() creates a custom StructuralConnectionHandler along with its associated StructuralConnectionHandlerType. Input elements should include structural members and steel connection members, and at least one StructuralConnectionHandler representing the generic connection to replace with the new detailed custom connection.

The methods:

-   StructuralConnectionHandlerType.AddElementsToCustomConnection()
-   StructuralConnectionHandlerType.RemoveMainSubelementsFromCustomConnection()

provide support for adding or removing steel connection elements in a custom connection.

The properties:

-   StructuralConnectionHandler.IsCustom
-   StructuralConnectionHandler.IsDetailed
-   StructuralConnectionHandlerType.IsCustom
-   StructuralConnectionHandlerType.IsDetailed

provide read access to information about the structural connection handler elements.
