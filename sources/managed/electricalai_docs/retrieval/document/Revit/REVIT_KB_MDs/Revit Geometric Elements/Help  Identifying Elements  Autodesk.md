---
created: 2026-01-28T20:58:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Identifying_Elements_html
author: 
---

# Help | Identifying Elements | Autodesk

> ## Excerpt
> In Revit, the easiest way to judge whether an element is a FamilyInstance or not is by using the properties dialog box.

---
In Revit, the easiest way to judge whether an element is a FamilyInstance or not is by using the properties dialog box.

-   If the family name starts with System Family and the Load button is disabled, it belongs to System Family. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-96BC987E-5C38-45EF-9621-2D6EF89989B1-low.png)**Figure 41: System Family**
    
-   A general FamilyInstance, which belongs to the Component Family, does not start with System Family.
    
-   For example, in the following picture the family name for the desk furniture is Desk. In addition, the Load button is enabled. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-67F1CF63-64EF-40E4-BF92-284873CDDB31-low.png)**Figure 42: Component Family**
    
-   There are some exceptions, for example: Mass and in-place member. The Family and Type fields are blank. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-A2B06CEE-7E4A-494B-8DE8-7131068F182B-low.png)**Figure 43: Mass or in-place member example**
    

Families in the Revit Platform API are represented by three objects:

-   Family
-   FamilySymbol
-   FamilyInstance

Each object plays a significant role in the family structure.

The Family object represents an entire family such as Single-Flush doors. For example, the Single-Flush door Family corresponds to the Single-Flush.rfa file. The Family object contains several FamilySymbols that are used to get all family symbols to facilitate swapping instances from one symbol to another.

The FamilySymbol object represents a specific set of family settings corresponding to a Type in the Revit UI, such as 34"×80".

The FamilyInstance object represents an actual Type (FamilySymbol) instance in the Revit project. For example, in the following picture, the FamilyInstance is a single door in the project.

-   Each FamilyInstance has one FamilySymbol. The door is an instance of a 34"×80".
-   Each FamilySymbol belongs to one Family. The 34"×80" symbol belongs to a Single-Flush family.
-   Each Family contains one or more FamilySymbols. The Single-Flush family contains a 34"×80" symbol, a 34"×84" symbol, a 36"×84" and so on.

Note: While most component elements are exposed through the API classes FamilySymbol and FamilyInstance, some have been wrapped with specific API classes. For example, AnnotationSymbolType wraps FamilySymbol and AnnotationSymbol wraps FamilyInstance.
