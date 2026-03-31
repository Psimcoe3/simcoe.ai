[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RuledSurface Members

---



|  |
| --- |
| [RuledSurface Class](9a33fec9-bbcd-f035-3194-cf36122b6cc6.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [RuledSurface](9a33fec9-bbcd-f035-3194-cf36122b6cc6.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method Static member | [Create(Curve, Curve)](55c2212e-c46e-4009-bd47-eb64d5667dcd.htm) | Creates a Surface object coincident with the ruled surface joining two bounded generating curves. |
| Public method Static member | [Create(Curve, XYZ)](5dc0d801-bff6-e9d8-98b1-f3f3dbe475c2.htm) | Creates a Surface object coincident with the ruled surface joining a bounded generating curve to a point. |
| Public method | [Dispose](c9ee1344-bc19-d833-52e7-dcc4931fe085.htm) | (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetBoundingBoxUV](5084214f-219f-780f-fe03-f16b62b2660d.htm) | Gets the UV bounding box of the surface. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | [GetFirstProfileCurve](fd892c31-0118-ddef-7396-2e9fc4b0cf27.htm) | Returns a copy of the first profile curve if it is set. |
| Public method | [GetFirstProfilePoint](5e92662a-714e-c214-dd72-33854724d69d.htm) | If a point was used to define the first profile, returns a copy of that point. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetSecondProfileCurve](ed774fa0-6b6b-bdb5-da2e-dba4b122d2a3.htm) | Returns a copy of the second profile curve if it is set. |
| Public method | [GetSecondProfilePoint](25c68423-a251-12a4-4094-b69bf2153a61.htm) | If a point was used to define the second profile, returns a copy of that point. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [HasFirstProfilePoint](f6049f89-38db-e9a8-9a09-f91809f59f64.htm) | Checks if a point was used to define the first profile. |
| Public method | [HasSecondProfilePoint](056030c4-3d30-f9fb-fbaf-fa11763e2304.htm) | Checks if a point was used to define the second profile. |
| Public method | [Project](802cc09b-d0a4-dfc5-8ca1-e8c5e8cd4ced.htm) | Project a 3D point orthogonally onto a surface (to find the nearest point). Throws InvalidOperationException if the projection fails. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | [ProjectWithGuessPoint](db8cc42a-9f34-611a-d9c5-852f3935887f.htm) | Project a 3D point orthogonally onto a surface (to find the nearest point). This method is meant to be used when a good approximate solution for the projection is available. Throws InvalidOperationException if the projection fails. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](6429595a-a6e1-2501-1e60-9c53814a9108.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public property | [OrientationMatchesParametricOrientation](451b549f-2bc4-4f37-9f32-981fe18868a8.htm) | Indicates whether this Surface's orientation is the same as or opposite to its parametric orientation. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |

# See Also

[RuledSurface Class](9a33fec9-bbcd-f035-3194-cf36122b6cc6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)