[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.MassFailures Members

---



|  |
| --- |
| [BuiltInFailures MassFailures Class](c9804646-1735-fe87-b758-a466adf5eae8.htm)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in FailureDefinitionId instances.

The  [BuiltInFailures MassFailures](c9804646-1735-fe87-b758-a466adf5eae8.htm)  type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [AutoGlazingFailed](4c14fd5d-451f-2a8e-bba8-0b21f1af9697.htm) | Failure in Auto-Glazing region computation. |
| Public property Static member | [AutoGlazingFailedError](67a7ff7f-ebea-b3ad-6af2-2cad9ee03073.htm) | Failure in Auto-Glazing region computation. |
| Public property Static member | [BooleanUnionFailed](41506bc2-9d2a-5a0d-bd79-814241c15d67.htm) | Failed to merge overlapping solids |
| Public property Static member | [CannotIntegrate](14063952-52cc-bc54-2716-3266f44ff7b3.htm) | In order to restore an element's 'Constrain to Massing' property to 'Dependent', it must be in the main model with the massing. |
| Public property Static member | [CannotMergeGeometry](3d161566-8205-4056-521f-b0a868290170.htm) | The Mass contains geometry that cannot be combined. Mass Floors, volume, and surface area, won't be computed. |
| Public property Static member | [CannotMoveMassing](c72dc4d9-ec06-b938-d43c-ab00e06581ef.htm) | Can't move whole Massing. Move the elements within the Massing instead. |
| Public property Static member | [CreateCoreGeometryFailed](029f4cf1-6c95-745a-7ff9-ed65b20ef35c.htm) | Failed to create core geometries. |
| Public property Static member | [DividePerimeterZoneFailed](4220bc7d-1430-03ae-3bca-d34c2ef88e0a.htm) | Failed to divide perimeter zone. |
| Public property Static member | [FaceRegionCreationFailed](a233005d-9ca5-d3d2-abcf-caf375c39d4e.htm) | Failure in face region creation. |
| Public property Static member | [FaceSplitFailed](d052b690-ccde-a7c4-27ae-c2ddb8c0f5ea.htm) | A face of a joined (i.e. one cuts another) mass could not be split into interior and exterior faces. Remove the cut to resolve. |
| Public property Static member | [FloorAreaFaceFailed](3111f259-14ef-0ff0-d5b2-98c04498fbe2.htm) | Failed to create a Mass Floor. |
| Public property Static member | [FloorMightLookWrong](cc2215ff-d9a2-6e2f-adcd-5d7d4314efc5.htm) | Mass Floors may appear incorrect since the Mass contains mesh and solid geometry. |
| Public property Static member | [FloorRecreateFailed](de55d6ab-1f3c-1b93-a841-2604cca63c9b.htm) | The floor cannot be created. |
| Public property Static member | [FloorRecreateFailedWarning](fbbaaf4f-e89a-3190-f023-14c48eafa48f.htm) | The floor cannot be created because no suitable level in the target document can be found. |
| Public property Static member | [MinSkylightWidthImperial](f533a8f0-2a16-2da5-264f-f5ae656b968b.htm) | The minimum skylight width is 8 inches. |
| Public property Static member | [MinSkylightWidthMetric](b8502ecf-a427-12a3-5ae8-2e22a1342c26.htm) | The minimum skylight width is 203.2 millimeters. |
| Public property Static member | [MultipleMassing](2abfd436-511a-f8b2-7ac9-f0fdb86ef896.htm) | Can't complete operation. Massing can only exist in one Workset. Change Workset of Massing to match in Local and Central Models. |
| Public property Static member | [NoCurtainRoofsInMassing](cd995395-8169-3d87-6564-acd711c91378.htm) | Massing cannot be created with a curtain roof. Please change the default roof type and try again. |
| Public property Static member | [NonOccupiableMassZone](30176548-db94-de41-7049-c177f1a890bc.htm) | For mass zone, if the bottom level ref does not intersect, then this zone is going to be "not occupiable" and a warning is posted for it. |
| Public property Static member | [NoSolidInMass](d8b6d10d-fbb6-c6ac-7b38-6d6c1a00ff38.htm) | Mass contains no solid geometry. Mass Floors, volume, and surface area, won't be computed. |
| Public property Static member | [OpenAndSolidGeometry](9a9234c1-eb45-6067-8506-f8eda5e4c581.htm) | Mass contains both solid and mesh geometry. Mass Floors, volume, and surface area, may appear incorrect. |
| Public property Static member | [OpenGeometryOnly](1ebe908e-59e6-15ba-39ac-1ff9cdcf1ea0.htm) | Mass contains only mesh geometry, which can't be used to compute Mass Floors, volume, or surface area. |
| Public property Static member | [OverlappingSolids](a345a348-5832-254c-b2f0-35d41cba98c8.htm) | Found volumetric overlap between solids. They will be merged into one |
| Public property Static member | [SketchCurveNotModelable](748df7c1-e34e-aa8c-d29f-3b472d7815f1.htm) | This action cannot be completed. An element created by massing has a sketch line that cannot be modeled. |
| Public property Static member | [SplitFacesByGroundPlaneCrashed](b8a1c132-8378-5604-b3d2-6730ef0929c4.htm) | Failed to split face by ground plane. |
| Public property Static member | [SplitFacesByGroundPlaneFailed](47f2c42c-d634-2273-1116-cbc86019eebf.htm) | Failed to split face by ground plane. |
| Public property Static member | [SplitOverlappingFacesFailed](d8768ea5-e9a1-4a1b-086a-e1f370a30cfe.htm) | Failed to resolve all overlaps between faces of the same Mass Energy Analytical Model. |
| Public property Static member | [TooManyGeometries](e5d4f5b0-96ab-6adc-1d5f-72f2508d2d3e.htm) | The geometry in this Mass instance is too complex to take advantage of the capabilities a Mass provides. Please break it down into multiple Mass and family instances that are less complex. |
| Public property Static member | [UpgradedMassingWarning](957336d8-f598-32ef-dd26-202740e50bf4.htm) | Your document contained a Massing element which has been upgraded to a Mass instance. Please review the documentation on the new enhanced Mass capabilities to understand the implications of this change. |

# See Also

[BuiltInFailures MassFailures Class](c9804646-1735-fe87-b758-a466adf5eae8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)