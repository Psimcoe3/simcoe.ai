---
created: 2026-01-28T21:00:46 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_Color_Fill_html
author: 
---

# Help | Color Fill | Autodesk

> ## Excerpt
> Autodesk.Revit.DB.ColorFillLegend supports creating, reading and modifying properties of color fill legend annotation elements in a particular view. The static method ColorFillLegend.Create(document, viewId, categoryId, origin) lets you to create a new color fill legend in a view.

---
## Color Fill Legend

`Autodesk.Revit.DB.ColorFillLegend` supports creating, reading and modifying properties of color fill legend annotation elements in a particular view. The static method `ColorFillLegend.Create(document, viewId, categoryId, origin)` lets you to create a new color fill legend in a view.

## Color Fill Scheme

The color fill scheme definition includes:

-   The category (such as Rooms).
-   The parameter whose value will be used to color the elements (such as Name, Floor Finish, or Department).
-   If the coloring will be done by range of values (such as at least 40SF' and less than 80SF') or by specific values (such as equal to 40SF').
-   The list of `ColorFillSchemeEntry` items.

Key members of `Autodesk.Revit.DB.ColorFillScheme` relating to these attributes are:

-   CategoryId
-   ParameterDefinition
-   IsByRange
-   AddEntry()/DeleteEntry()
-   GetEntries()/SetEntries()

### Color Fills Schemes used by a view

A view can define one `ColorFillScheme` for spatial elements (rooms, zones, spaces, and areas), one for pipes, and one for ducts. You can get and set these schemes with

-   View.GetColorFillSchemeId(categoryId)
-   View.SetColorFillSchemeId(categoryId, schemeId)

## Color Fill Scheme Entries

The color fill scheme entry definition includes:

-   The color.
-   The fill pattern.
-   The caption shown in the Color Fill Legend (such as 100 SF' or more).
-   The parameter value that will apply to this entry.

The `Autodesk.Revit.DB.ColorFillSchemeEntry` class provides all functionality needed to create, read, and modify these entries

**Code Region: Creating a Color Fill Legend**

```
private void CreateColorFill(View v)
{
    Document doc = v.Document;
    ElementId roomCatId = new ElementId(BuiltInCategory.OST_Rooms);
    using (Transaction t = new Transaction(v.Document, "Create Color Fill Legend"))
    {
        t.Start();
        if (v.GetColorFillSchemeId(roomCatId) == ElementId.InvalidElementId)
        {
            v.SetColorFillSchemeId(
                roomCatId, 
                new FilteredElementCollector(doc)
                    .OfClass(typeof(ColorFillScheme))
                    .Cast<ColorFillScheme>()
                    .First(q => q.CategoryId == roomCatId).Id);
        }
        ColorFillLegend.Create(v.Document, v.Id, roomCatId, XYZ.Zero);
        t.Commit();
    }
}
```

**Code Sample - Create and Apply a Color Fill Scheme**

```
private void NewColorScheme(View v)
{
    Document doc = v.Document;
    ColorFillScheme scheme = doc.GetElement(
        v.GetColorFillSchemeId(
            new ElementId(BuiltInCategory.OST_Rooms))) as ColorFillScheme;

    using (Transaction t = new Transaction(doc, "New Color Scheme"))
    {
        t.Start();

        ElementId newSchemeId = scheme.Duplicate("Color By Room Finish");
        ColorFillScheme newScheme = doc.GetElement(newSchemeId) as ColorFillScheme;
        newScheme.Title = "Room Finish";
        newScheme.ParameterDefinition = new ElementId(BuiltInParameter.ROOM_FINISH_BASE);        

        v.SetColorFillSchemeId(new ElementId(BuiltInCategory.OST_Rooms), newSchemeId);

        t.Commit();
    }
}
```

**Code Sample - Add an entry to a ColorFillScheme**

```
private void AddColorFillSchemeEntry(ColorFillScheme scheme)
{
    Document doc = scheme.Document;
    ColorFillSchemeEntry entry = new ColorFillSchemeEntry(StorageType.String)
    {
        Color = new Color(25, 0, 0),
        FillPatternId = new FilteredElementCollector(doc)
            .OfClass(typeof(FillPatternElement))
            .Cast<FillPatternElement>()
            .First(a => a.GetFillPattern().IsSolidFill)
            .Id
    };
    entry.SetStringValue("Tile");
    using (Transaction t = new Transaction(doc, "Add Scheme Entry"))
    {
        t.Start();
        scheme.AddEntry(entry);
        t.Commit();
    }
}
```

**Code Sample - Modify entries of a ColorFillScheme**

```
private void ModifyColorFillSchemeEntries(ColorFillScheme scheme)
{
    Document doc = scheme.Document;
    IList<ColorFillSchemeEntry> entries = scheme.GetEntries();
    foreach (ColorFillSchemeEntry entry in entries)
    {
        entry.FillPatternId = new FilteredElementCollector(doc)
        .OfClass(typeof(FillPatternElement))
        .Cast<FillPatternElement>()
        .First(a => a.Name == "Crosshatch")
        .Id;
    }
    using (Transaction t = new Transaction(doc, "Modify entry"))
    {
        t.Start();
        scheme.SetEntries(entries);
        t.Commit();
    }
}
```
