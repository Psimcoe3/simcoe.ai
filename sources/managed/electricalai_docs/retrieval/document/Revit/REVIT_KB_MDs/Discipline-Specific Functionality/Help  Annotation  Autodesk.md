---
created: 2026-01-28T21:09:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Annotation_html
author: 
---

# Help | Annotation | Autodesk

> ## Excerpt
> The MultiReferenceAnnotation can be used to label and dimension Rebar elements, and are labeled in the user interface as "Multi-rebar annotations". The members of this class include:

---
The `MultiReferenceAnnotation` can be used to label and dimension Rebar elements, and are labeled in the user interface as "Multi-rebar annotations". The members of this class include:

-   Create - creates a new MultiReferenceAnnotation based on a document, view, and an instance of the MultiReferenceAnnotationOptions class
-   AreElementsValidForMultiReferenceAnnotation - validates if the input elements match the element category id for the MultiReferenceAnnotationType.
-   is3DViewValidForDimension - Returns True if the view is suitable for placing the MultiReferenceAnnotation
    -   If the DimensionStyle is LinearFixed, it cannot be created in a 3D View.
    -   If the DimensionStyle is Linear, it cannot be created in a 3D View if the view direction is perpendicular to the current work plane normal.
    -   Returns true if the ownerViewId is not a 3D view.

The references of the annoation and placement options are specified in the `MultiReferenceAnnotationOptions` class. Its members include:

-   DimensionLineDirection - The direction vector of the dimension line
-   SetElementsToDimension - The elements referenced by the dimension
-   SetAdditionalReferencesToDimension - Sets the additional references which the dimension will witness. The additional references to dimension cannot come from the same category as the MultiReferenceAnnotationType's reference category.
-   ReferencesDontMatchReferenceCategory - Verifies that all of the references belongs to elements which don't match the reference category required by the MultiReferenceAnnotationType.
-   GetAdditionalReferencesToDimension - Gets the additional references which the dimension will witness

| Code Region: Create MultiReferenceAnnotation |
| --- |
| 
```
public void CreateAnnotation(Document doc)
{
    MultiReferenceAnnotationOptions opt = new MultiReferenceAnnotationOptions(
        new FilteredElementCollector(doc)
        .OfClass(typeof(MultiReferenceAnnotationType))
        .Cast<MultiReferenceAnnotationType>()
        .FirstOrDefault());
    opt.DimensionLineDirection = XYZ.BasisX;
    opt.DimensionPlaneNormal = XYZ.BasisZ;
    opt.DimensionStyleType = DimensionStyleType.Linear;
    opt.SetElementsToDimension(new FilteredElementCollector(doc, doc.ActiveView.Id).OfClass(typeof(Rebar)).ToElementIds());
    using (Transaction t = new Transaction(doc, "MultiReferenceAnnotation"))
    {
        t.Start();
        MultiReferenceAnnotation mra = MultiReferenceAnnotation.Create(doc, doc.ActiveView.Id, opt);
        t.Commit();
    }
}
```

 |
