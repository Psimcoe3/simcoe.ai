[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImagePlacementOptions Constructor (XYZ, BoxPlacement)

---



|  |
| --- |
| [ImagePlacementOptions Class](20d793a0-4309-dac8-1e43-61d275237887.htm)   [See Also](#seeAlsoToggle) |

Constructs a new ImagePlacementOptions for placing an  [ImageInstance](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public ImagePlacementOptions( 	XYZ location, 	BoxPlacement placementPoint ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	location As XYZ, _ 	placementPoint As BoxPlacement _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ImagePlacementOptions( 	XYZ^ location,  	BoxPlacement placementPoint ) ``` |

#### Parameters

location
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The location where the image will be placed

placementPoint
:   Type:  [Autodesk.Revit.DB BoxPlacement](2ecf1f45-4890-8b9f-3de7-8d0eebeb7ce7.htm)    
     The point of the image that will be aligned to the location in the view

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ImagePlacementOptions Class](20d793a0-4309-dac8-1e43-61d275237887.htm)

[ImagePlacementOptions Overload](661d96a0-406a-8c3b-955a-f0e3337d5597.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)