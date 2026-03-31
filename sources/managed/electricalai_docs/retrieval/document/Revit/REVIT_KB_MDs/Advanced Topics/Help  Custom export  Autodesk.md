---
created: 2026-01-28T21:18:13 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_Custom_export_html
author: 
---

# Help | Custom export | Autodesk

> ## Excerpt
> Use a custom export process to export views from a Revit document.

---
Use a custom export process to export views from a Revit document.

The Revit API provides a set of classes that make it possible to export views via a custom export context. These classes provide access to the rendering output pipeline through which Revit sends the graphical representation of a model to an output device. In the case of a custom export, the "device" is represented by a context object that could be any kind of a device. A file would be the most common case.

An implementation of a custom exporter provides a context and invokes rendering of a model, upon which Revit starts processing the model and sends graphic data out via methods of the context. The data describes the model exactly as it would have appeared in Revit when the model is rendered. The data includes all geometry and material properties.

## CustomExporter class

The CustomExporter class allows exporting views via a custom export context. The Export() method of this class triggers the standard rendering process in Revit, but instead of displaying the result on screen or printer, the output is channeled through the given custom context that handles processing the geometric as well as non-geometric information.

### CustomExporter support for 2D views

CustomExporter can export 2D plan, section and elevation views.

The method `CustomExporter.Export(IList<ElementId>)` can accept either 3D or 2D views, with the limitation that views in the collection must be either all 3D or all 2D.

For both Export() calls, the exporter context must correspond to the views' type; use IModelExportContext or IPhotoRenderContext for 3D views and IExportContext2D for 2D views.

Several properties for the CustomExporter exist to support 2D objects:

-   CustomExporter.Export2DGeometricObjectsIncludingPatternLines - Indicates whether pattern lines of geometric objects should be exported in a 2D context. Defaults to false.
-   CustomExporter.Export2DIncludingAnnotationObjects - Indicates whether annotation objects should be exported in a 2D context. Defaults to false.
-   CustomExporter.Export2DForceDisplayStyle - Forces a display style for the export. If the style is DisplayStyle.Undefined, then export uses DisplayStyle.Wireframe for wireframe views and DisplayStyle.HLR for other views. Defaults to DisplayStyle.Undefined.

Use the interface `IExportContext2D` for exporting 2D views. It has the following methods in addition to the method inherited from IExportContext:

-   IExportContext2D.OnElementBegin2D()
-   IExportContext2D.OnElementEnd2D()
-   IExportContext2D.OnFaceEdge2D()
-   IExportContext2D.OnFaceSilhouette2D()

To access data for various 2D exported objects, use the classes:

-   ElementNode
-   FaceEdgeNode
-   FaceSilhouetteNode

Some notes on 2D export in DisplayStyle.Wireframe:

1.  Geometric object methods (OnCurve, OnFaceEdge2D, OnFaceSilhouette2D) are called regardless of the object being eventually output, i.e. even if it is occluded by another element.

And in DisplayStyle.HLR:

1.  Tessellated geometry methods (OnLineSegment and OnPolylineSegments) are called regardless of the return value of the respective geometric object methods (OnCurve, OnFaceEdge2D, OnFaceSilhouette2D).
2.  None of these methods are called between the respective pairs of calls OnInstanceBegin/OnInstanceEnd or OnLinkBegin/OnLinkEnd. They are called between OnElementBegin2D/OnElementEnd2D and OnViewBegin/OnViewEnd.

For an example of the use of the API for custom export of 2D views, see the SDK sample CustomExporter/Custom2DExporter.

### CustomExporter events

Subscribe to these events to be notified when Revit is just about to export, or has just exported, one or more views of the document via an export context by CustomExporter:

-   `Autodesk.Revit.ApplicationServices.Application.ViewsExportingByContext`
-   `Autodesk.Revit.ApplicationServices.Application.ViewsExportedByContext`

`Autodesk.Revit.DB.Events.ViewsExportingByContextEventArg` provides information when Revit is just about to export one or more views of the document via an export context by CustomExporter. It has the method `ViewsExportingByContextEventArgs.GetViewIds()` to get the ids of views about to be exported by CustomExporter.

`Autodesk.Revit.DB.Events.ViewsExportedByContextEventArgs` provides information when Revit has just exported one or more views of the document via an export context by CustomExporter. It has the method `ViewsExportedByContextEventArgs.GetViewIds()` - Gets the ids of views that have been exported by CustomExporter.

## IExportContext

An instance of the IExportContext class is passed in as a parameter of the CustomExporter constructor. The methods of this interface are then called as the entities of the model are exported.

Although it is possible to create classes derived from the IExportContext class, it is preferred to use one of its derived classes: IPhotoRenderContext or IModelExportContext. When using an IPhotoRenderContext to perform a custom export, Revit will traverse the model and output the model's geometry as if processing the Render command invoked via the UI. Only elements that have actual geometry and are suitable to appear in a rendered view will be processed and output.

The IModelExportContext should be used for processing elements in the view in the same manner that Revit processes them in 3D views. This context supports additional elements including model curves and text as shown in the 3D views.

## RenderNode classes

RenderNode is the base class for all output nodes in a model-exporting process. A node can be either geometric (such as an element or light) or non-geometric (such as material). Some types of nodes are container nodes, which include other render nodes.

## CameraInfo

The CameraInfo class describes information about projection mapping of a 3D view to a rendered image. An instance of this class can be obtained via a property of ViewNode. If it is null, an orthographic view should be assumed.
