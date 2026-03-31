---
created: 2026-01-28T20:52:47 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_Revisions_html
author: 
---

# Help | Revisions | Autodesk

> ## Excerpt
> The Revit API provides several classes and members for accessing project Revisions, their settings and associated Revision Clouds.

---
The Revit API provides several classes and members for accessing project Revisions, their settings and associated Revision Clouds.

## Settings

The RevisionSettings class allows an application to read and modify the project-wide settings that affect Revisions and Revision Clouds. The static RevisionSettings.GetRevisionSettings() method returns the RevisionSettings object for the given project document. The following properties can be used to access project-wide Revision settings:

-   RevisionCloudSpacing - determines the size in paper space of revision clouds drawn in a project.
-   RevisionNumbering - determines whether revision numbers for the project are determined on a per sheet or a whole project basis. The AlphanumericRevisionSettings class contains settings that apply to Revisions with the Alphanumeric RevisionNumberType. The RevisionSettings methods GetAlphanumericRevisionSettings() and SetAlphanumericRevisionSettings() provide read and write access to the AlphanumericRevisionSettings. AlphanumericRevisionSettings offers the following members:

-   Prefix - a prefix to be prepended to each revision number with alphanumeric type.
-   Suffix - a suffix to be appended to each revision number with alphanumeric type.
-   GetSequence() - gets the list of strings to be used as the numbering sequence for revisions with the alphanumeric type.
-   SetSequence() - sets the list of strings for numbering revisions of this type. Similarly, the NumericRevisionSettings class contains settings that apply to Revisions with the Numeric RevisionNumberType. The RevisionSettings methods GetNumericRevisionSettings () and SetNumericRevisionSettings() provide read and write access to these settings. NumericRevisionSettings offers the following members:

-   Prefix - a prefix to be prepended to each revision number with numeric type.
    
-   Suffix - a suffix to be appended to each revision number with numeric type.
    
-   StartNumber property - the value to be used as the first number in the sequence of numeric revisions.
    
    When revision clouds appear on a sheet, the revision number of each revision can be displayed either by tagging the revision cloud or by a revision schedule within the sheet's titleblock. There are two ways the number can be determined:
    
-   **Per project**: The value of the Revision numbers will always correspond to the project-wide Revision Sequence Number assigned to the revision. For example, if revision clouds for revisions with sequence numbers 5, 7, and 8 are placed on a sheet then revision tags and schedules on that sheet would display 5, 7, and 8.
    
-   **Per sheet**: Revision numbers will be assigned consecutive numbers based on the revision clouds visible on that sheet. For example, if revision clouds for revisions assigned project-wide Revision Sequence Numbers 5, 7, and 8 are placed on a sheet then revision tags and schedules on that sheet would display 1, 2, and 3. The sequence on the sheet will still follow the relative ordering of the Revision Sequence Numbers, so in this example revision 5 would be displayed as 1 on the sheet, revision 7 would be displayed as 2, etc.
    

The Revision class allows an application to read and modify the existing revisions in a project and to create new revisions. The Revision object represents the data related to a single revision in the project. It has properties such IssuedBy, IssuedTo, RevisionNumber, SequenceNumber and RevisionDate. Revision clouds and tags can be associated with a particular Revision object to display its properties on sheets.

The revisions in the project are stored in a specific order called the revision sequence. The revision sequence represents the conceptual sequence in which revisions will be issued. The static method Revision.GetAllRevisionIds() will return the ids of all Revisions in this order. The static method Revision.ReorderRevisionSequence() can be used to change the sequence of revisions with the project. Note that the newly specified sequence must include every Revision in the project exactly once and that changing the sequence of Revisions can change the SequenceNumber and RevisionNumber of Revisions that have already been issued.

The `RevisionNumberingSequence` class defines the sequences by which numbers are assigned to Revisions. Revision numbering is either numeric or alphanumeric. Alphanumeric from the API corresponds to the UI concept of "Custom". Members of this class provide the ability to create, read and modify the settings related to Revision numbering sequences.

`Revision.GetRevisionNumberingSequenceId()` and Revision.SetRevisionNumberingSequenceId()\` provide access to the sequence which controls a revision's numbering.

The static Create() method will create a new Revision in the specified document. In the sample below, multiple revisions are added and their properties are set.

| Code Region: Creating new revisions |
| --- |
| 
```
public IList<Revision> AddRevisions(Document document)
{
    IList<Revision> newRevisions = new List<Revision>();
    using (Transaction createRevision = new Transaction(document, "createRevision"))
    {
        createRevision.Start();
        newRevisions.Add(AddNewRevision(document, "Include door tags", "manager1", "employee1", 1, DateTime.Now));
        newRevisions.Add(AddNewRevision(document, "Add a section view", "manager1", "employee1", 2, DateTime.Now));
        newRevisions.Add(AddNewRevision(document, "Make callout view larger", "manager1", "employee1", 3, DateTime.Now));
        createRevision.Commit();
    }

    return newRevisions;
}

private Revision AddNewRevision(Document document, string description, string issuedBy, string issuedTo, int sequenceNumber, DateTime date)
{
    Revision newRevision = Revision.Create(document);
    newRevision.Description = description;
    newRevision.IssuedBy = issuedBy;
    newRevision.IssuedTo = issuedTo;

    AlphanumericRevisionSettings ars = new AlphanumericRevisionSettings();
    RevisionNumberingSequence sequence = RevisionNumberingSequence.CreateAlphanumericSequence(document, "name", ars);
    newRevision.RevisionNumberingSequenceId = sequence.Id;

    newRevision.RevisionDate = date.ToShortDateString();
    return newRevision;
}
```

 |

Two methods, CombineWithNext() and CombineWithPrevious() allow an application to combine a specified Revision with the next or previous Revision in the model. Combining the Revisions means that the RevisionClouds and revision tags associated with the specified Revision will be reassociated with the next Revision and the specified Revision will be deleted from the model. This method returns the ids of the RevisionClouds that were reassociated. However, these operations can only be implemented if neither Revision has been issued.

The following example demonstrates use of the CombineWithNext() method. It also uses the GetAllRevisionIds() method to find the next revision to be sure the CombineWithNext() method will be successful.

| Code Region: Combining revisions |
| --- |
| 
```
private bool CombineRevision(Document document, Revision revision)
{
    bool combined = false;
    // Can only combine two revisions if neither have been issued
    if (revision.Issued == false)
    {
        ElementId revisionId = revision.Id;
        Revision nextRevsion = GetNextRevision(document, revisionId);
        if (nextRevsion != null && nextRevsion.Issued == false)
        {
            ISet<ElementId> revisionCloudIds = Revision.CombineWithNext(document, revisionId);
            combined = true;
            int movedClouds = revisionCloudIds.Count;
            if (movedClouds > 0)
            {
                RevisionCloud cloud = document.GetElement(revisionCloudIds.ElementAt(0)) as RevisionCloud;
                if (cloud != null)
                {
                    string msg = string.Format("Revision {0} deleted and {1} revision clouds were added to Revsion {2}",
                        revisionId.ToString(), movedClouds, cloud.RevisionId.ToString());
                    TaskDialog.Show("Revision Combined", msg);
                }
            }
        }
    }

    return combined;
}

private Revision GetNextRevision(Document document, ElementId currentRevisionId)
{
    Revision nextRevision = null;
    IList<ElementId> revisionIds = Revision.GetAllRevisionIds(document);
    int currentRevisionIndex = -1;
    for (int n = 0; n < revisionIds.Count; n++)
    {
        if (revisionIds[n] == currentRevisionId)
        {
            currentRevisionIndex = n;
            break;
        }
    }

    // if the current revision id was found and is not the last index
    if (currentRevisionIndex >= 0 && currentRevisionIndex < revisionIds.Count - 1)
    {
        ElementId nextRevisionId = revisionIds[currentRevisionIndex + 1];
        nextRevision = document.GetElement(nextRevisionId) as Revision;
    }

    return nextRevision;
}
```

 |

## Revision clouds

A RevisionCloud is a graphical "cloud" that can be displayed on a view or sheet to indicate where revisions in the model have occurred. The RevisionCloud class allows an application to access information about the revision clouds that are present within a model and to create new revision clouds.

RevisionClouds are view specific and can be created in most graphical views, except 3D.

Note also that when a RevisionCloud is created in a ViewLegend, it is treated as a legend representation of what a RevisionCloud looks like rather than as an actual indication of a change to the model. As a result, RevisionClouds in ViewLegends will not affect the contents of revision schedules.

### Creating revision clouds

The static Create() methodallows an application to create a new RevisionCloud in a specified view based on a series of lines and curves. RevisionClouds can only be created if the associated Revision has not yet been issued.

RevisionClouds can be created in most graphical Views, excepting 3D views and graphical column schedules. Unlike most other Elements, RevisionClouds can be created directly on a ViewSheet.

RevisionClouds are created based on a series of sketched curves. There is no requirement that the curves form closed loops and self-intersections are also permitted. The curves will be automatically projected onto the appropriate plane for the View. The list of curves cannot be empty and no lines can be perpendicular to the View's plane. If the View is a model View, the coordinates specified for the curves will be interpreted in model space. If the View is a non-model View (such as a ViewSheet) then the coordinates will be interpreted in the View's space.

Each curve will have a series of "cloud bumps" drawn along it to form the appearance of a cloud. The cloud graphics will be attached to the curves under the assumption that each curve is oriented in a clockwise direction. For lines, this means that the outside of the cloud is in the direction of the line's normal vector within the View's plane. Any closed loops should therefore be oriented clockwise to create the typical cloud shape.

| Code Region: Create revision cloud |
| --- |
| 
```
private void CreateRevisionCloudInActiveView(Document document, Revision revision, IList<Curve> curves)
{
    using (Transaction newRevisionCloud = new Transaction(document, "Create Revision Cloud"))
    {
        newRevisionCloud.Start();
        // Can only create revision cloud for revision that is not issued
        if (revision.Issued == false)
        {
            RevisionCloud.Create(document, document.ActiveView, revision.Id, curves);
            newRevisionCloud.Commit();
        }
        else
        {
            newRevisionCloud.RollBack();
        }
    }
}
```

 |

### Revision cloud geometry

RevisionCloud is derived from the Element class. The Element.Geometry property for revision clouds will return the actual curved lines that make up the cloud. The RevisionCloud.GetSketchCurves() method on the other hand,will return the sketched curves that define the basic outline of the cloud and not the arcs that Revit attaches to these curves to create the cloud appearance.

### Revision Associated with RevisionCloud

Each RevisionCloud is associated with one Revision. The associated revision id is specified when calling Create() and can be retrieved from the RevisionCloud.RevisionId property. The RevisionId property for a RevisionCloud can be changed if it is not associated with a Revision that has already been issued. It can only be changed to the id of another Revision that has also not been issued. RevisionCloud.IsRevisionIssued() returns whether the associated Revision has been issued.

### ViewSheets

When a RevisionCloud is visible on a ViewSheet (either because it is directly placed on that ViewSheet or because it is visible in a View placed on the ViewSheet), any revision schedules displayed on the ViewSheet will automatically include the Revision associated with the RevisionCloud.

The RevisionCloud.GetSheetIds() method returns the ids of the ViewSheets where it may appear and contribute to the sheet's revision schedule. A RevisionCloud can appear on a ViewSheet because it is drawn directly on the ViewSheet or because its owner view is placed on the ViewSheet. If the RevisionCloud is owned by a view that is a dependent view or has associated dependent views, then the RevisionCloud can also be visible on the sheets where the related dependent or primary views have been placed.

This RevisionCloud may not be visible in all ViewSheets reported by this method. Additional factors, such as the visibility settings or annotation crop of the Views or the visibility settings of the associated Revision may still cause this RevisionCloud to not appear on a particular ViewSheet.

If this RevisionCloud is owned by a ViewLegend, no sheets will be returned because the RevisionCloud will not participate in revision schedules. The ViewSheet class includes methods for working with Revisions and RevisionClouds on sheets. See the [ViewSheet](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_ViewSheet_html) topic for more information.
