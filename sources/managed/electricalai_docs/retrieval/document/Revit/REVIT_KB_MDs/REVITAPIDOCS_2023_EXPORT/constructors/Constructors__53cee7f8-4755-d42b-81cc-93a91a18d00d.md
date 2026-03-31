[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OBJExportOptions Members

---



|  |
| --- |
| [OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [OBJExportOptions](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [OBJExportOptions](43ae0d7b-847e-80b9-0350-b495fcf3b30b.htm) | Constructs a new instance of OBJExportOptions with default values of all properties. |
| Public method | [OBJExportOptions(ExportResolution)](47145edb-9e79-9cbf-8f33-d47528989442.htm) | Constructs a new instance of OBJExportOptions with all predefined tessellation settings, depending on export resolution type. Note: in case of Custom resolution type, tessellation settings won't be predefined and will have default values. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](fb997601-df3a-2ea0-6dc9-c27f42dcfc29.htm) | (Inherited from  [ATFBaseExportOptions](7087cd85-a366-5f49-65a8-c58ed4bf74d8.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [IsGridAspectRatioSet](5d2857ac-200f-30c9-278c-65184fa75ca9.htm) | Checks whether the GridAspectRatio tessellation parameter is explicitly set. |
| Public method | [IsMaxEdgeLengthSet](fbe632a0-b829-a24d-1e12-32b1de7f3ed8.htm) | Checks whether the MaxEdgeLength tessellation parameter is explicitly set. |
| Public method | [IsNormalToleranceSet](244c5a23-8f09-7ef4-c2ca-0aca09c1c614.htm) | Checks whether the NormalTolerance tessellation parameter is explicitly set. |
| Public method | [IsSurfaceToleranceSet](566566a9-1846-e1e3-8347-085f45023c6f.htm) | Checks whether the SurfaceTolerance tessellation parameter is explicitly set. |
| Public method Static member | [IsValidForGridAspectRatio](c68db8c2-48d0-8b2b-7034-9ce2640206a7.htm) | Checks whether the value is allowed (is in the allowed range) for GridAspectRatio tessellation parameter. |
| Public method Static member | [IsValidForMaxEdgeLength](ffc983cc-bc1f-33fa-9826-9680b6a70ed2.htm) | Checks whether the value is allowed (is in the allowed range) for MaxEdgeLength tessellation parameter. |
| Public method Static member | [IsValidForNormalTolerance](6b4aa9ab-b973-1e3b-20ef-44fc641476d0.htm) | Checks whether the value is allowed (is in the allowed range) for NormalTolerance tessellation parameter. |
| Public method Static member | [IsValidForSurfaceTolerance](97afa54a-57c4-f59d-019d-21f34bf67412.htm) | Checks whether the value is allowed (is in the allowed range) for SurfaceTolerance tessellation parameter. |
| Public method | [SetTessellationSettings](69d6f0a1-0dc0-a607-4b87-503b4a3ed833.htm) | Sets all the tessellation parameters to its predefined values for the given resolution type. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [GridAspectRatio](ee880009-2cb5-fcec-f46f-ffbd0d5c2179.htm) | The maximum aspect ratio allowed in the grid placed across the face. The minimum allowed value is 1.0. The maximum allowed value is 10.0. By default this property is ignored. |
| Public property | [IsValidObject](cbdfc611-e184-36dc-2e95-2845fe2880c1.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [ATFBaseExportOptions](7087cd85-a366-5f49-65a8-c58ed4bf74d8.htm)  .) |
| Public property | [MaxEdgeLength](a7e555ea-8873-79e8-8b89-fc36cfe9035a.htm) | The maximum length allowed for any chord on an edge or between any two adjacent grid lines. This is a percentage value. By exporting, the real value of maximum edge length is calculated as a percent from the length of the diameter of the body bounding box. The minimum allowed value is 0.1%. The maximum allowed value is 10.0%. By default this property is ignored. |
| Public property | [NormalTolerance](929bba33-35bc-a057-7d47-20fae0f99617.htm) | The maximum change in the surface normal between adjacent nodes in the mesh. This property is defined in degrees. The minimum allowed value is 1.0 degrees. The maximum allowed value is 45.0 degrees. Default value is 15.0 degrees. |
| Public property | [SurfaceTolerance](9e1b8007-b1b1-bdc9-69a6-04c60b4ff416.htm) | The maximum distance between mesh triangles and model geometry. This is a percentage value. By exporting, the real value of surface tolerance is calculated as a percent from the length of the diameter of the body bounding box. The minimum allowed value is 0.001%. The maximum allowed value is 1.0%. Default value is 0.1%. |
| Public property | [TargetUnit](a0ae7667-641a-f729-329b-706460172df4.htm) | The unit type of geometry in the resultant OBJ file. Default value is ExportUnit::Default. |
| Public property | [ViewId](4797a173-14f7-4d09-9fe8-bb5d984d1489.htm) | The element id of the 3D view to export. InvalidElementId by default. (Inherited from  [ATFBaseExportOptions](7087cd85-a366-5f49-65a8-c58ed4bf74d8.htm)  .) |

# See Also

[OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)