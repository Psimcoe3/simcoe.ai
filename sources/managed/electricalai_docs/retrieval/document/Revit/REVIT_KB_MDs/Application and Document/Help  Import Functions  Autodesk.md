---
created: 2026-01-28T20:42:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Import Functions | Autodesk

> ## Excerpt
> The overloads for the Document.Import method allow several different file types to be imported.

---
The overloads for the `Document.Import` method allow several different file types to be imported.

## CAD file import

-   Import(String, SATImportOptions, View) - Imports an SAT file into the document.
-   Import(String, SKPImportOptions, View) - Imports an SKP file into the document.
-   Import(String, DGNImportOptions, View, out ElementId) - Imports a DGN file to the document.
-   Import(String, DWGImportOptions, View, out ElementId) - Imports a DWG or DXF file to the document.

## GBXML import

-   Import(String, GBXMLImportOptions)

## Images and PDF import

Revit can import images (JPG, PNG, etc) and raster images generated from PDF files.

The class `ImageInstance` represents an instance of an ImageType placed in a view. Its members include:

-   Create(Document, View, ElementId, ImagePlacementOptions) - The ImagePlacementOptions describes where an image instance should be placed in a view.
-   GetLocation(BoxPlacement) - The BoxPlacment enumeration is used to specify which corner (or the center) of the image the location pertains to.
-   SetLocation(XYZ, BoxPlacement)
-   property Width
-   property Height
-   property EnableSnaps

The class `ImageType` represents a type containing an image. Its members include:

-   Create(Document, ImageTypeOptions)
-   CanReload() - validates the corresponding image or PDF file and performs additional validation if the file is served by an external provider.
-   ReloadFrom(ImageTypeOptions)
-   property ExternalResourceType - the type of external resources that represents images (and PDF files).
-   property PageNumber
-   property PathType - the type of path that was used to refer to the file from which the ImageType was loaded.

The class `ImageTypeOptions` represents the options that are used when creating or reloading an ImageType, which contains image data corresponding to an image or PDF file. Its members include:

-   IsValid() - tests whether ImageTypeOptions can be used to create or reload an ImageType; additional validation is performed for PDF files and external files.
-   property PageNumber
-   property Path
-   property Resolution - is measured in dpi and relates the number of pixels in raster images to their size.
-   setExternalResourceReference() - specifies the location of an image or PDF file using an external resource reference.

ImageTypeOptions can be used to specify a local file or a file served by an external provider. Local files can be referred to using relative paths. For PDF files, ImageType loads a single page at a time, which is rasterized at the resolution specified in ImageTypeOptions.

The class `ImagePlacementOptions` is used to describe where an ImageInstance should be placed in a view

-   ImagePlacementOptions() constructs a new ImagePlacementOptions that will place an ImageInstance with its center at the origin of the model
-   ImagePlacementOptions(XYZ, BoxPlacement) constructs a new ImagePlacementOptions with the provided Location and PlacementPoint
-   Location specifies where a point of the ImageInstance, determined by the PlacementPoint property, is going to be inserted.
-   PlacementPoint uses a `BoxPlacement` to identify which point of the ImageInstance will be aligned to the Location

### Converting images between links and imports

`ImageTypeOptions.SourceType` along with the new enumerated value `ImageTypeSource` and `ImageType.ReloadFrom()` allow you to create or convert an ImageType to a link or import.

The overall process is:

-   Create a new ImageTypeOptions instance from the existing ImageType properties
-   Modify the ImagesTypeOptions, for example by changing the ImageTypeOptions.SourceType between Link and Import, or change the path with ImageTypeOptions.SetPath()
-   Use those new ImageTypeOptions in ImageType.ReloadFrom

ImageType properties include:

-   ImageType.Source - Indicates how the image is created (as a link, import, or internally-generated image)
-   ImageType.Status - Indicates whether the image is loaded or unloaded (if applicable)

Two constructors take an ImageTypeSource as an argument:

-   ImageTypeOptions(String, Boolean, ImageTypeSource)
-   ImageTypeOptions(ExternalResourceReference, ImageTypeSource)

The enumeration: `ImageTypeStatus` contains possible values for the load status of an ImageType.

`OptionalFunctionalityUtils.isPDFImportAvailable()` checks whether the installed Revit contains optional modules that are necessary for the PDF import functionality.

## Rhino

`Document.Import(String, ImportOptions3DM, View)` and `Document.Link(String, ImportOptions3DM, View)` import or link a 3DM file into the document.
