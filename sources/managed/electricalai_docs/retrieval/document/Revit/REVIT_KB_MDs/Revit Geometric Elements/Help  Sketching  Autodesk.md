---
created: 2026-01-28T21:03:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_html
author: 
---

# Help | Sketching | Autodesk

> ## Excerpt
> Sketches define the shape of many elements in Revit such as:

---
Sketches define the shape of many elements in Revit such as:

-   Ceiling
-   Extrusion
-   Filled Region
-   Floor
-   Opening
-   Stair
-   Railing
-   Roof

In addition to Sketch Elements, ModelCurve is also described in this chapter. For more details about Element Classification, see [Element Classification](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_Element_Classification_html) in the [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html) section.

## Sketches of Ceilings, Floors, Walls, or Openings

### Getting the Sketch

You cannot retrieve a Sketch object by iterating the Document with a FilteredElementCollector. Instead, use these properties to get the element id of the element's sketch.

-   Ceiling.SketchId
-   Floor.SketchId
-   Opening.SketchId
-   Wall.SketchId

For a given sketch, you can get element (Floor, Wall...) that owns the sketch with the `Sketch.OwnerId` property. `Sketch.GetAllElements()` returns all elements (ModelCurve, ReferencePlane, Dimension) that belong to a sketch.

### Editing and Validating the Sketch

Use the `SketchEditScope` class to edit the sketch. While a Sketch editing session is active, you can add, delete or modify Sketch elements (curves, dimensions, reference planes). A transaction will be needed to make the changes. When you finish the session, the Sketch-based element will be updated.

Key methods include:

-   SketchEditScope constructor - Creates a new SketchEditScope
-   Start() - Starts editing a particular sketch. After this is started only elements owned by the Sketch and new elements to be added to the Sketch may be modified
-   StartWithNewSketch() - Because a valid sketch may not initially exist for some Revit elements (such as Walls or Analytical Elements), a valid sketch will need to be created before it can be edited.
-   Commit() - Commits the changes
-   IsSketchEditingSupported() - Checks if a sketch can be edited with a SketchEditScope

#### Boundary Validation

The `BoundaryValidation` class provides methods to validate curve loops for sketching:

-   `IsValidHorizontalBoundary` identifies whether the provided curve loops create a valid horizontal boundary
-   `IsValidBoundaryOnView` checks that a curve loop boundary is valid on the view's sketch plane.
-   `IsValidBoundaryOnSketchPlane` checks that a curve loop boundary is valid on a sketch plane

**Code Region: Edit a Floor Sketch**

```
private void EditSketch(Floor floor)
{
 // Delete all lines in the sketch & create two new arcs that form a circle
 Document doc = floor.Document;
 Sketch sketch = doc.GetElement(floor.SketchId) as Sketch;
 using (SketchEditScope edit = new SketchEditScope(doc, "Edit Floor"))
 {
  edit.Start(floor.SketchId);
  using (Transaction t = new Transaction(doc, "Edit Sketch"))
  {
   t.Start();

   doc.Delete(sketch.GetAllElements());

   doc.Create.NewModelCurve(
    Arc.Create(sketch.SketchPlane.GetPlane(), 5, 0, Math.PI * 2),
    sketch.SketchPlane);

   t.Commit();
  }
  edit.Commit(new failuresPreprocessor());
 }
}

private class failuresPreprocessor : IFailuresPreprocessor
{
 public FailureProcessingResult PreprocessFailures(FailuresAccessor failuresAccessor)
 {
  return FailureProcessingResult.Continue;
 }
}
```
