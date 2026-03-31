[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.SiteImportFailures Members

---



|  |
| --- |
| [BuiltInFailures SiteImportFailures Class](8f9298be-9e12-d84b-8459-c862355e698d.htm)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in FailureDefinitionId instances.

The  [BuiltInFailures SiteImportFailures](8f9298be-9e12-d84b-8459-c862355e698d.htm)  type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [BoundaryDetectError](8c8c3bba-c6e1-d8ee-6738-d87fc72f527d.htm) | A boundary on this surface could not be autodetected. Revit will impose one, but it may be larger than you want. |
| Public property Static member | [ContoursNoncontours](cf2149e8-42af-69b5-8e41-1aef52548631.htm) | The layers you have selected contain both contour lines and non-contour lines (lines of non-constant elevation). You may want to go back and select fewer layers, or you can continue, but the boundary of the site may be larger than you want. |
| Public property Static member | [DifferentEntityTypes](1202ad11-8794-1d55-f063-c42e56caec57.htm) | Can't auto-detect boundary. The layers selected contain data that may make the Toposurface look incorrect. For better results, try selecting only those layers that contain relevant 3D info. |
| Public property Static member | [NoPoints](7bbef7e2-44ac-abf4-51f0-4084369adeae.htm) | No points were found in the file. |
| Public property Static member | [NoViewSpecificSiteImports](c4533c3c-8581-2f27-cf02-ea960a87e4a9.htm) | Can't make Toposurface from View Specific Imports. |
| Public property Static member | [SurfaceExists](3e47440a-9d7f-5ca8-4773-3851d8efa999.htm) | You are importing data into a surface that already contains points. You may want to go back, create a new surface, and import the data into that instead. You can continue, and Revit will sew the meshes together, but the boundary may be larger than you want. |
| Public property Static member | [TooFarAway](bd99be6a-646b-59c3-c69b-75f8b4d0b34a.htm) | Imported Toposurface Points are located a large distance from the model and might not display properly. Points will be centered on the model instead. |
| Public property Static member | [TooLarge](c991d035-dd20-aeb4-c500-7f10ca5bfc8f.htm) | There are too many points on the selected layers of this dataset to place into the toposurface. Try selecting fewer layers to create the surface |
| Public property Static member | [TooManyMeshes](0f1d4267-f6b9-56a1-c4ee-cf1489e335cb.htm) | The layers you have selected contain more than one mesh. You may want to go back and import the meshes separately. If you continue, the meshes will be combined and a new boundary will be created. |
| Public property Static member | [UnusedPoints](7ddd17c9-1d02-c172-ea56-b684505abe0a.htm) | Some rows from the file could not be used. |

# See Also

[BuiltInFailures SiteImportFailures Class](8f9298be-9e12-d84b-8459-c862355e698d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)