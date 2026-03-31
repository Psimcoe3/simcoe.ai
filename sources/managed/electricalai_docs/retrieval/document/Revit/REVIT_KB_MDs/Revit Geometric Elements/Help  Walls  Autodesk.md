---
created: 2026-01-28T21:04:46 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Walls_html
author: 
---

# Help | Walls | Autodesk

> ## Excerpt
> There are four kinds of Walls represented by the WallType.WallKind enumeration:

---
There are four kinds of Walls represented by the WallType.WallKind enumeration:

-   Stacked
-   Curtain
-   Basic
-   Unknown

The Wall and WallType class work with the Basic wall type while providing limited function to the Stacked and Curtain walls. On occasion you need to check a Wall to determine the wall type. For example, you cannot get sub-walls from a Stacked Wall using the API. WallKind is read only and set by System Family.

The Wall.Flipped property and Wall.flip() method gain access to and control Wall orientation. In the following examples, a Wall is compared before and after calling the flip() method.

-   The Orientation property before is (0.0, 1.0, 0.0).
-   The Orientation property after the flip call is (0.0, -1.0, 0.0).
-   The Wall Location Line (WALL\_KEY\_REF\_PARAM) parameter is 3, which represents Finish Face: Interior in the following table.
-   Taking the line as reference, the Wall is moved but the Location is not changed.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4BFD801E-18BC-4021-8371-C29AF13CF7EE-low.png)**Figure 33: Original wall**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-85CF3DAD-C029-41C5-ACC6-1FEC8CA304E4-low.png)**Figure 34: Wall after flip**

**Table 24: Wall Location Line**

<table summary="" id="GUID-DBFA35F2-854F-458C-8BD4-B886F91981EE__TABLE_D1C2E830D5A34AF387D50C37DC8FF5AC"><tbody><tr><td><b>Location Line Value</b></td><td><b>Description</b></td></tr><tr><td>0</td><td>Wall Centerline</td></tr><tr><td>1</td><td>Core Centerline</td></tr><tr><td>2</td><td>Finish Face: Exterior</td></tr><tr><td>3</td><td>Finish Face: Interior</td></tr><tr><td>4</td><td>Core Face: Exterior</td></tr><tr><td>5</td><td>Core Face: Interior</td></tr></tbody></table>

There are five static override methods in the Wall class to create a Wall:

**Table 25: Create() Overrides**

<table summary="" id="GUID-DBFA35F2-854F-458C-8BD4-B886F91981EE__TABLE_5F0A5294142A40DD9C8382976D7EF4D9"><tbody><tr><td><b>Name</b></td><td><b>Description</b></td></tr><tr><td>Create(Document, Curve, WallType, Level, Double, Double, Boolean, Boolean)</td><td>Creates a new rectangular profile wall within the project using the specified wall type, height, and offset.</td></tr><tr><td>Create(Document, IList Curve , Boolean)</td><td>Creates a non rectangular profile wall within the project using the default wall style.</td></tr><tr><td>Create(Document, Curve, ElementId, Boolean)</td><td>Creates a new rectangular profile wall within the project on the level specified by ElementId using the default wall style.</td></tr><tr><td>Create(Document, IList Curve , ElementId, ElementId, Boolean)</td><td>Creates a non rectangular profile wall within the project using the specified wall type.</td></tr><tr><td>Create(Document, IList Curve , ElementId, ElementId, Boolean, XYZ)</td><td>Creates a non rectangular profile wall within the project using the specified wall type and normal vector.</td></tr></tbody></table>

The WallType Wall Function (WALL\_ATTR\_EXTERIOR) parameter influences the created wall instance Room Bounding and Structural Usage parameter. The WALL\_ATTR\_EXTERIOR value is an integer:

**Table 26: Wall Function**

<table summary="" id="GUID-DBFA35F2-854F-458C-8BD4-B886F91981EE__TABLE_9BB324360ECB41C9887D12CF817A6B8B"><tbody><tr><td><b>Wall Function</b></td><td><b>Interior</b></td><td><b>Exterior</b></td><td><b>Foundation</b></td><td><b>Retaining</b></td><td><b>Soffit</b></td></tr><tr><td>Value</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr></tbody></table>

The following rules apply to Walls created by the API:

-   If the input structural parameter is true or the Wall Function (WALL\_ATTR\_EXTERIOR) parameter is Foundation, the Wall StructuralUsage parameter is Bearing; otherwise it is NonBearing.
-   The created Wall Room Bounding (WALL\_ATTR\_ROOM\_BOUNDING) parameter is false if the Wall Function (WALL\_ATTR\_EXTERIOR) parameter is Retaining.

For more information about structure-related functions such as the AnalyticalModel property, refer to [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html).

## Wall Profile Sketch

These methods provide access to add and remove profile sketches:

-   Wall.CreateProfileSketch()
-   Wall.RemoveProfileSketch()

`Wall.CanHaveProfileSketch()` returns True if the wall supports profile sketch. Arc walls and elliptical walls are two wall geometries that do not support having an edited profile. Once a sketch is added, the profile sketch can be edited using `SketchEditScope`

## Slanted and Tapered Walls

`Wall.CrossSection` lets you get and set a wall to a value of the `WallCrossSection` enum (`SingleSlanted`, `Vertical`, `Tapered`). Wall.IsWallCrossSectionValid() checks if a cross section is valid for a specific wall.

`Autodesk.Revit.DB.WidthMeasuredAt` and `Autodesk.Revit.DB.InsertOrientation` define the shape of the wall and behavior of inserts for non-vertical walls.
