---
created: 2026-01-28T20:51:07 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Creating_Arrays_of_Elements_html
author: 
---

# Help | Creating Arrays of Elements | Autodesk

> ## Excerpt
> The Revit Platform API provides two classes, LinearArray and RadialArray to array one or more elements in the project. These classes provide static methods to create a linear or radial array of one or more selected components. Linear arrays represent an array created along a line from one point, while radial arrays represent an array created along an arc.

---
The Revit Platform API provides two classes, LinearArray and RadialArray to array one or more elements in the project. These classes provide static methods to create a linear or radial array of one or more selected components. Linear arrays represent an array created along a line from one point, while radial arrays represent an array created along an arc.

As an example of using an array, you can select a door and windows located in the same wall and then create multiple instances of the door, wall, and window configuration.

Both LinearArray and RadialArray also provide methods to array one or several elements without being grouped and associated. Although similar to the Create() methods for arraying elements, each resulting element is independent of the others, and can be manipulated without affecting the other elements. See the tables below for more information on the methods available to create linear or radial arrays.

**Table 22: LinearArray Methods**

|  |  |
| --- | --- |
| Member | Description |
| `Create(Document, View, ElementId, int, XYZ, ArrayAnchorMember)` | Array one element in the project by a specified number. |
| `Create(Document, View, ICollection<ElementId>, int, XYZ, ArrayAnchorMember)` | Array a set of elements in the project by a specified number. |
| `ArrayElementWithoutAssociation(Document, View, ElementId, int, XYZ, ArrayAnchorMember)` | Array one element in the project by a specified number. The resulting elements are not associated with a linear array. |
| `ArrayElementsWithoutAssociation(Document, View, ICollection<ElementId>, int, XYZ, ArrayAnchorMember)` | Array a set of elements in the project by a specified number. The resulting elements are not associated with a linear array. |

**Table 23: RadialArray Methods**

|  |  |
| --- | --- |
| Member | Description |
| `Create(Document, View, ElementId, int, Line, double, ArrayAnchorMember)` | Array one element in the project based on an input rotation axis. |
| `ArrayElementWithoutAssociation(Document, View, ElementId, int, Line, double, ArrayAnchorMember)` | Array one element in the project based on an input rotation axis.. The resulting elements are not associated with a linear array. |
| `ArrayElementsWithoutAssociation(Document, View, ICollection<ElementId>, int, Line, double, ArrayAnchorMember)` | Array a set of elements in the project based on an input rotation axis.. The resulting elements are not associated with a linear array. |

The methods for arraying elements are useful if you need to create several instances of a component and manipulate them simultaneously. Every instance in an array can be a member of a group.

Note: When using the methods for arraying elements, the following rules apply:

-   When performing Linear and Radial Array operations, elements dependent on the arrayed elements are also arrayed.
-   Some elements cannot be arrayed because they cannot be grouped. See the Revit User's Guide for more information about restrictions on groups and arrays.
-   Arrays are not supported by most annotation symbols.
