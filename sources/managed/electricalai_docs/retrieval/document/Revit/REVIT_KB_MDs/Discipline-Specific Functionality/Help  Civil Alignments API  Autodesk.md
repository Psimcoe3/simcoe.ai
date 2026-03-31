---
created: 2026-01-28T21:07:53 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Civil_html
author: 
---

# Help | Civil Alignments API | Autodesk

> ## Excerpt
> Revit provides support for Civil Alignments and their associated annotations. Alignments are imported from InfraWorks as a part of the workflow to
transfer Civil Structures. The API supports read of alignment properties and geometric information, along with read/write and create of associated
annotations. All new classes for the Alignments API are exposed through a different assembly in the Revit installation, located at Addins\CivilAlignments
\Autodesk.CivilAlignments.DBApplication.dll

---
Revit provides support for Civil Alignments and their associated annotations. Alignments are imported from InfraWorks as a part of the workflow to transfer Civil Structures. The API supports read of alignment properties and geometric information, along with read/write and create of associated annotations. All new classes for the Alignments API are exposed through a different assembly in the Revit installation, located at Addins\\CivilAlignments \\Autodesk.CivilAlignments.DBApplication.dll

`Autodesk.Revit.DB.Infrastructure.Alignment` represents an alignment and can be used to find alignments in a document, and to query a particular alignment's properties and to analyze alignment geometry. This object is not an Element, but the underlying Element can be obtained from this object if needed.

`Autodesk.Revit.DB.Infrastructure.AlignmentStationLabel` represents an alignment station label annotation and can be used to find such labels in a document as well as to create and modify such labels. This object is not an Element, but the underlying Element (which is a SpotDimension instance) can be obtained from this object if needed.

-   Autodesk.Revit.DB.Infrastructure.AlignmentStationLabelOptions
-   Autodesk.Revit.DB.Infrastructure.AlignmentStationLabelSetOptions provide options for creating a single alignment label or for creating a set of alignment labels.
