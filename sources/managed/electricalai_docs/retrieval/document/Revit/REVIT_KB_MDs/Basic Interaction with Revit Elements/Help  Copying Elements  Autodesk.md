---
created: 2026-01-28T20:50:41 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Copying_Elements_html
author: 
---

# Help | Copying Elements | Autodesk

> ## Excerpt
> The ElementTransformUtils class provides several static methods to copy one or more elements from one place to another, either within the same document or view, or to a different document or view.

---
The ElementTransformUtils class provides several static methods to copy one or more elements from one place to another, either within the same document or view, or to a different document or view.

**Table: Copy Methods**

|  |  |
| --- | --- |
| Member | Description |
| `CopyElement( Document, ElementId, XYZ)` | Copies an element and places the copy at a location indicated by a given transformation.. |
| `CopyElements(Document, ICollection<ElementId>, XYZ)` | Copies a set of elements and places the copies at a location indicated by a given translation. |
| `CopyElements(Document, ICollection<ElementId>, Document, Transform, CopyPasteOptions)` | Copies a set of elements from source document to destination document. |
| `CopyElements(View, ICollection<ElementId>, View, Transform, CopyPasteOptions)` | Copies a set of elements from source view to destination view. |

All of the methods return a collection of ElementIds of the newly created elements, including CopyElement(). The collection includes any elements created due to dependencies.

The method for copying from one document to another can be used for copying non-view specific elements only. Copies are placed at their respective original location or locations specified by the optional transformation.

View-specific elements should be copied using the method that copies from one view to another. That method can be used for both view-specific and model elements however, drafting views cannot be used as a destination for model elements. The pasted elements are repositioned to ensure proper placement in the destination view. For example, the elevation is changed when copying from one level to another. An additional transformation within the destination view can be performed by providing the optional Transform argument. This additional transformation must be within the plane of the destination view.

When copying from one view to another, both the source and destination views must be 2D graphics views capable of drawing details and view-specific elements, such as floor and ceiling plans, elevations, sections, or drafting views. The ElementTransformUtils.GetTransformFromViewToView() method will return the transformation that is applied to elements when copying from a source view to a destination view.

When copying between views or between documents, an optional CopyPasteOptions parameter may be set to override default copy/paste settings. By default, in the event of duplicate type names during a paste operation, Revit displays a modal dialog with options to either copy types with unique names only, or to cancel the operation. CopyPasteOptions can be used to specify a custom handler, using the IDuplicateTypeNamesHandler interface, to handle duplicate type names.

See the Duplicate Views sample in the Revit SDK for a detailed example of copying between documents and between views.
