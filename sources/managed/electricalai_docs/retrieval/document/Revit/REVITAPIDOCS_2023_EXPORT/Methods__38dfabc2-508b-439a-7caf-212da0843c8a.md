[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MeshFromGeometryOperationResult Members

---



|  |
| --- |
| [MeshFromGeometryOperationResult Class](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [MeshFromGeometryOperationResult](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](1232a220-124f-f1ed-adcf-9234bf17e2ed.htm) | Releases all resources used by the  [MeshFromGeometryOperationResult](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetIssues](0a0dded2-d7d7-9d7e-424d-ffb09051a690.htm) | Returns the array of issues encountered while building a mesh. |
| Public method | [GetMesh](bd2901fe-9510-612a-f383-cb8caaee62ed.htm) | This returns a valid mesh only for the first call. Later calls will throw an exception as the mesh is no longer valid in this object. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [HasInvalidData](2ceba862-dbcf-348e-4aec-9e676a093d60.htm) | Whether the provided data for which this result was obtained were internally inconsistent and could not be used in its entirety. For example, for extrusion operation, profile loops were degenerate or improperly oriented with respect to the extrsuion direction. |
| Public property | [IsMeshAvailable](9d587518-ed0c-5199-47b3-2f3c0fa69cb8.htm) | Shows whether the result still contains the mesh which was constructed, if any, or whether it has been relinquished by 'getMesh'. The former is true, the later is false. |
| Public property | [IsValidObject](fff8becb-ceed-55e1-3977-8ea49762b48b.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [Tessellated](30d4e459-7217-20bd-9192-b5253ea78792.htm) | Whether while constructing a mesh, it was necessary to extrude polylines instead of non-linear curves from the profile loops. |

# See Also

[MeshFromGeometryOperationResult Class](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)