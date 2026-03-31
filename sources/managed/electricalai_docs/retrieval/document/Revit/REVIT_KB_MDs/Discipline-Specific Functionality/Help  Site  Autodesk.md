---
created: 2026-01-28T21:10:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Site_html
author: 
---

# Help | Site | Autodesk

> ## Excerpt
> The Site API is located in the Autodesk.Revit.DB.Architecture namespace.

---
The Site API is located in the Autodesk.Revit.DB.Architecture namespace.

## Creation

-   TopographySurface.Create(Document doc, IList<XYZ> points, IList<PolymeshFacet> facets) creates a topography surface from a list of triangulation facets.
-   TopographySurface Create(Document, IList<XYZ> points) creates a topography surface from a list of points.

### Validation

TopographySurface.IsValidFaceSet(IList<PolymeshFacet> facets, IList<XYZ> points) checks whether the triangulation data is valid.

### Linked Topography

-   TopographyLinkType represents a site file brought into the current Revit model as a link.
-   TopographyLinkType.Reload() reloads the TopographyLinkType from its current location.

## Editing a TopographySurface

To edit a TopographySurface, create an instance of a TopographyEditScope with the constructor for this class. Then call the TopographyEditScope.Start() method to begin editing and complete the editing operation with TopographyEditScope.Commit().
