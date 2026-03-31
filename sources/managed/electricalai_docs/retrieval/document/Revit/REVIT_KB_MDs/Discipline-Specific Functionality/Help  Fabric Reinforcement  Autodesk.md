---
created: 2026-01-28T21:09:40 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Fabric_Reinforcement_html
author: 
---

# Help | Fabric Reinforcement | Autodesk

> ## Excerpt
> Fabric reinforcement is a layer of fabric sheets made of welded fabric wire and hosted in concrete slabs or walls.

---
Fabric reinforcement is a layer of fabric sheets made of welded fabric wire and hosted in concrete slabs or walls.

Fabric sheets are typically created in a pattern which results in welded wire sheets overlapping each other to provide continuity of load transfer from one sheet to the next. Sheets may be in one or more layers within a concrete element.

Fabric Sheets are typically specified by a grid spacing and a wire size for each direction. For example: 6x6 - W2.9/W2.9 in US Imperial units (or 152x152-MW18.7/MW18.7 in SI units) would be interpreted as a grid of wires at 6" on center with a wire area of 2.9 hundredths of an inch squared (0.029 sq-in).

In the Revit API, these sheets are represented by the FabricSheet class and they are defined by a FabricSheetType class which controls the number and spacing of wires in each direction, either by a pattern or custom definition. FabricSheetType reference wires as FabricWireItems that are associated with a FabricWireType.

## Fabric Area

The FabricArea class is a container for fabric sheets. When created, fabric sheets are automatically generated for the FabricArea based on the FabricSheetType referenced on creation. The FabricArea class has an overloaded Create() method to create a FabricArea based either on the host boundary or from an array of curves. FabricArea must be hosted by a structural floor, wall, foundation slab or a part created from a structural layer of one of these types.

The example below demonstrates how to create a new FabricArea and get a list of the resulting FabricSheets.

| Code Region: Create a fabric area |
| --- |
| 
```
private FabricArea CreateNewFabricArea(Document document, Element wall)
{
    FabricArea system = null;

    // create default types if they aren't already in the model
    ElementId fabricAreaTypeId = FabricAreaType.CreateDefaultFabricAreaType(document);
    ElementId fabricSheetTypeId = FabricSheetType.CreateDefaultFabricSheetType(document);

    system = FabricArea.Create(document, wall, new XYZ(1, 0, 0), fabricAreaTypeId, fabricSheetTypeId);
    // call regenerate to generate fabric sheets in fabric area
    document.Regenerate();

    // get the list of elementIds for the sheets automatically generated in the fabric area
    IList<ElementId> sheetIds = system.GetFabricSheetElementIds();

    TaskDialog.Show("Revit", string.Format("{0} fabric sheets created", sheetIds.Count));

    return system;
}
```

 |

## Creating fabric sheets

Fabric sheets can be hosted by a container (represented by the FabricArea class), or can exist as single fabric sheets. Single fabric sheets are hosted elements and must be hosted by a structural floor, structural wall, structural foundation slab, or a part created from a structural layer of one of these types. Bent fabric sheets can also be hosted in structural beams, columns and braces.

The FabricSheet class provides an overloaded static Create() method for creating new single fabric sheets in the model. One overload of FabricSheet.Create() creates a flat fabric sheet and requires a reference to the document in which the fabric sheet will be created, a reference to the host element which will host the fabric sheet and the ElementId of the fabric sheet type to create.

Another overload of FabricSheet.Create() can be used to create bent fabric sheets, which is not possible in the Revit user interface. It requires the same input as above, plus a CurveLoop that defines the bending path. This bending path is a profile that defines the bending shape of the fabric sheet. Fabric wires have an allowable bend radiuses so you may provide this CurveLoop profile with or without fillets. In other words, if a U shaped profile is desired, only 3 lines must be specified and the fabric sheet created will be created with the appropriate bend radii at the corners. If the provided profile has no hard corners, (I.e., the curve has a tangent at each point, except the end) no fillets will be created in the final fabric sheet.

The provided CurveLoop is intended to define the centerline of the bent wire. You may specify whether the bend is in the major wires or the minor wires with the BentFabricBendDirection property of the FabricSheet. You may also specify the location of straight wires with respect to bent wires with the BentFabricStraightWiresLocation property.

## Fabric sheet type

A FabricSheet is associated with a FabricSheetType, which is used in the generation of wires for the sheet in the major and minor directions. The FabricSheetLayoutPattern for the wires in a FabricSheetType can be defined as:

-   ActualSpacing - spacing of rebars is fixed
-   FixedNumber - spacing of rebars is adjustable, but the number of bars is constant
-   MaximumSpacing - number of rebars depends on length of rebar set with a maximum spacing constraint specified
-   NumberWithSpacing - spacing and number of rebars are fixed
-   QuantitativeSpacing - multiple groups of wires with a specific spacing and diameter For the first 4 options, FabricSheetType has methods to set the layout pattern with given information for either the minor or major direction, such as SetMajorLayoutAsFixedNumber() or SetMinorAsActualSpacing(). The layout pattern can be retrieved with the properties MajorLayoutPattern and MinorLayoutPattern.

QuantitativeSpacing is for custom patterns. Use SetLayoutAsCustomPattern() to set the major and minor layout patterns to QuantitativeSpacing. If the layout pattern for the FabricSheetType is custom, the MajorDirectionWireType, MinorDirectionWireType, MajorSpacing and MinorSpacing properties do not apply. The SetLayoutAsCustomPattern() method has parameters for the start overlaps for the major and minor directions (both end overhangs are read only and computed internally), as well as a list of FabricWireItems for each direction.

| Code Region: Fabric sheet with custom wire pattern |
| --- |
| 
```
private FabricSheet CreateCustomFabricSheet(Document document, Element wall)
{
    if (FabricSheet.IsValidHost(wall) == false)
        return null;

    // Create a new type for custom FabricSheet
    ElementId fabricSheetTypeId = FabricSheetType.CreateDefaultFabricSheetType(document);
    FabricSheetType fst = document.GetElement(fabricSheetTypeId) as FabricSheetType;

    // Create some fabric wire types
    ElementId idWireType1 = FabricWireType.CreateDefaultFabricWireType(document);
    FabricWireType wireType1 = document.GetElement(idWireType1) as FabricWireType;
    wireType1.WireDiameter = 3.5 / 12.0;

    ElementId idWireType2 = FabricWireType.CreateDefaultFabricWireType(document);
    FabricWireType wireType2 = document.GetElement(idWireType1) as FabricWireType;
    wireType2.WireDiameter = 2.0 / 12.0;

    // Create the wires for the custom pattern
    IList<FabricWireItem> majorWires = new List<FabricWireItem>();
    IList<FabricWireItem> minorWires = new List<FabricWireItem>();
    FabricWireItem item = FabricWireItem.Create(2.0 / 12.0, 1, idWireType1, 0);
    majorWires.Add(item);
    majorWires.Add(item);
    item = FabricWireItem.Create(1.5 / 12.0, 10.0 / 12.0, idWireType2, 0);
    majorWires.Add(item);

    item = FabricWireItem.Create(3.0 / 12.0, 1, idWireType2, 0);
    minorWires.Add(item);
    item = FabricWireItem.Create(3.0 / 12.0, 10.0 / 12.0, idWireType2, 0);
    minorWires.Add(item);

    fst.SetLayoutAsCustomPattern(6.0 / 12.0, 4.0 / 12.0, minorWires, majorWires);

    FabricSheet sheet = FabricSheet.Create(document, wall, fabricSheetTypeId);
    // Regeneration is required before setting any property to object that was created in the same transaction.
    document.Regenerate();

    AnalyticalMember member = (AnalyticalMember)document.GetElement(AnalyticalToPhysicalAssociationManager.GetAnalyticalToPhysicalAssociationManager(document)
    .GetAssociatedElementId(wall.Id));
    sheet.PlaceInHost(wall, member.GetTransform());

    // Give the user some information
    TaskDialog.Show("Revit", string.Format("Flat Fabric Sheet ID='{0}' created successfully.", sheet.Id.IntegerValue));

    return sheet;   
}
```

 |

## Single fabric sheets

When fabric sheets are created, they are not yet placed in their host. You must call the method FabricSheet.PlaceInHost() and pass in the host element as well as a transform which describes the final position of the fabric sheet. The element passed for the host must support hosting fabric sheets. Note that only bent fabric sheets can be hosted in beams, columns or braces, while both bent and flat fabric sheets can be hosted in structural floors, walls and foundation slabs, or parts created from a structural layer of one of these types.

| Code Region: Creating a bent fabric sheet |
| --- |
| 
```
private FabricSheet CreateBentFabricSheet(Document document, Element column)
{
    if (FabricSheet.IsValidHost(column) == false)
        return null;

    CurveLoop bendingProfile = new CurveLoop();
    Line line1 = Line.CreateBound(new XYZ(2, 0.8, 0), new XYZ(6, 0.8, 0));
    Line line2 = Line.CreateBound(new XYZ(6, -0.8, 0), new XYZ(4, -2, 0));
    Arc arc = Arc.Create(line1.GetEndPoint(1), line2.GetEndPoint(0), new XYZ(7, 0, 0));
    bendingProfile.Append(line1);
    bendingProfile.Append(arc);
    bendingProfile.Append(line2);

    ElementId fabricSheetTypeId = document.GetDefaultElementTypeId(ElementTypeGroup.FabricSheetType);
    FabricSheetType fst = document.GetElement(fabricSheetTypeId) as FabricSheetType;
    fst.SetMajorLayoutAsFixedNumber(12.0, 1.0, 0.8, 4);
    fst.SetMinorLayoutAsMaximumSpacing(10.0, .75, .90, 3.0);

    FabricSheet bentFabricSheet = FabricSheet.Create(document, column.Id, fabricSheetTypeId, bendingProfile);
    // Regeneration is required before setting any property to object that was created in the same transaction.
    document.Regenerate();

    bentFabricSheet.BentFabricBendDirection = BentFabricBendDirection.Major;

    AnalyticalMember amc = (AnalyticalMember)document.GetElement(AnalyticalToPhysicalAssociationManager.GetAnalyticalToPhysicalAssociationManager(document)
        .GetAssociatedElementId(column.Id));
    bentFabricSheet.PlaceInHost(column, amc.GetTransform());

    // Give the user some information
    TaskDialog.Show("Revit", string.Format("Bent Fabric Sheet ID='{0}' created successfully.", bentFabricSheet.Id.IntegerValue));

    return bentFabricSheet;
}
```

 |

## Bent fabric sheets

The IsBent property indicates if the fabric sheet is a bent fabric sheet or not. It is not possible to convert a Fabric Sheet between flat and bent.

You may obtain the curves for a bent sheet or set new curves by calling GetBendProfile() or SetBendProfile() respectively.

| Code Region: Change the bend profile of a fabric sheet |
| --- |
| 
```
private void ModifyBentFabricSheet(Document document, FabricSheet bentFabricSheet)
{
    CurveLoop newBendingProfile = CurveLoop.CreateViaOffset(bentFabricSheet.GetBendProfile(), 0.5, new XYZ(0, 0, -1));
    bentFabricSheet.SetBendProfile(newBendingProfile);

    // Give the user some information
    TaskDialog.Show("Revit", string.Format("Bent Fabric Sheet ID='{0}' modified successfully.", bentFabricSheet.Id.IntegerValue));
}
```

 |

The GetSegmentParameterIdsAndLengths() method will return a dictionary with segment parameter ids as the keys and length as the values. These correspond to segments of a bent fabric sheet (like A, B, C, D etc.), but are not in alphabetical or any other order. (An empty dictionary is returned for flat fabric sheets.) To set the length of a bent fabric sheet segment, use SetSegmentLength().

| Code Region: Get segment ids and lengths |
| --- |
| 
```
private void GetBentFabricSheetData(FabricSheet fabricSheet)
{
    string fabricNumber = fabricSheet.FabricNumber;
    IDictionary<ElementId, double> idsAndLengths = fabricSheet.GetSegmentParameterIdsAndLengths(true);
    StringBuilder displayInfo = new StringBuilder();
    displayInfo.AppendLine(string.Format("Parameter Ids and segment lengths for FabricSheet {0}:", fabricNumber));

    foreach (ElementId key in idsAndLengths.Keys)
    {
        displayInfo.AppendLine(string.Format("Parameter Id: {0}, Length: {1}", key, idsAndLengths[key]));
    }

    TaskDialog.Show("Revit", displayInfo.ToString());
}
```

 |

The FabricNumber property used in the example above, specifies the numerical parameter assigned to the fabric sheet and any sheet of the same type, dimension, material, shape, and partition.
