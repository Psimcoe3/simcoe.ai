---
created: 2026-01-28T20:42:31 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Default Types | Autodesk

> ## Excerpt
> Revit has a default type for different categories. This default type is shown in the Revit User Interface when the related tool is invoked to create an element of this category. The Revit API exposes the default type for both family and non-family types via the Document class.

---
Revit has a default type for different categories. This default type is shown in the Revit User Interface when the related tool is invoked to create an element of this category. The Revit API exposes the default type for both family and non-family types via the Document class.

## Family Types

The document members listed in the table below provide access to the default type for a given family category id

| Document Method | Description |
| --- | --- |
| GetDefaultFamilyTypeId() | Gets the default family type id associated to the given family category id. |
| SetDefaultFamilyTypeId() | Sets the default family type id associated to the given family category id. |
| IsDefaultFamilyTypeIdValid() | Checks whether the family type id is valid to set as default for the given family category id. |

Additionally, given an ElementType, the ElementType.IsValidDefaultFamilyType() identifies if it is a valid default family type for the given family category id.

The example below demonstrates how to get the default family type Id for the structural column category. It then gets the family symbol for the default type and assigns it to a given column.

| Code Region: Get default family type id |
| --- |
| 
```
private void AssignDefaultTypeToColumn(Document document, FamilyInstance column)
{
    ElementId defaultTypeId = document.GetDefaultFamilyTypeId(new ElementId(BuiltInCategory.OST_StructuralColumns));

    if (defaultTypeId != ElementId.InvalidElementId)
    {
        FamilySymbol defaultType = document.GetElement(defaultTypeId) as FamilySymbol;
        if (defaultType != null)
        {
            column.Symbol = defaultType;
        }
    }
}
```

 |

The next example sets the default type for the doors category from a given door, after first checking that it is a valid default family type id.

| Code Region: Set default family type id |
| --- |
| 
```
private void SetDefaultTypeFromDoor(Document document, FamilyInstance door)
{
    ElementId doorCategoryId = new ElementId(BuiltInCategory.OST_Doors);

    // It is necessary to test the type suitability to be a default family type, for not every type can be set as default. 
    // Trying to set a non-qualifying default type will cause an exception
    if (door.Symbol.IsValidDefaultFamilyType(doorCategoryId))
    {
        document.SetDefaultFamilyTypeId(doorCategoryId, door.Symbol.Id);
    }
}
```

 |

## Non-family Types

The document members in the table below provide access to the default types for non-Family element types.

| Document Method | Description |
| --- | --- |
| GetDefaultElementTypeId() | Gets the default element type id for a given non-Family element type. |
| SetDefaultElementTypeId() | Sets the default element type id for a given non-Family element type. |
| IsDefaultElementTypeIdValid() | Checks whether the element type id is valid for a given non-Family element type. |

The example below checks whether a given wall is using the default element type for wall types.

| Code Region: Get default element type id |
| --- |
| 
```
private bool IsWallUsingDefaultType(Document document, Wall wall)
{
    ElementId defaultElementTypeId = document.GetDefaultElementTypeId(ElementTypeGroup.WallType);
    return (wall.WallType.Id == defaultElementTypeId);
}
```

 |
