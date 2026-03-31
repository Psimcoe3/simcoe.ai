[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConicalSurface Members

---



|  |
| --- |
| [ConicalSurface Class](bcc299b6-ff1a-7f0c-c5da-8b040a326899.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ConicalSurface](bcc299b6-ff1a-7f0c-c5da-8b040a326899.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method Static member | [Create](fc1bff98-15ce-be6e-5a23-89e20aad9e1d.htm) | Creates a conical surface defined by a local reference frame and a half angle. |
| Public method | [Dispose](c9ee1344-bc19-d833-52e7-dcc4931fe085.htm) | (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetBoundingBoxUV](5084214f-219f-780f-fe03-f16b62b2660d.htm) | Gets the UV bounding box of the surface. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | [GetFrameOfReference](59ae1045-6128-4daa-ca37-db36309d9905.htm) | Returns frame of reference associated with this ConicalSurface. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method Static member | [IsValidConeAngle](33f4d39f-a8b1-ef85-d423-fdc5044b8253.htm) | Checks whether the input value lies is not 0, greater than -PI/2 and lesser than PI/2. |
| Public method | [Project](802cc09b-d0a4-dfc5-8ca1-e8c5e8cd4ced.htm) | Project a 3D point orthogonally onto a surface (to find the nearest point). Throws InvalidOperationException if the projection fails. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | [ProjectWithGuessPoint](db8cc42a-9f34-611a-d9c5-852f3935887f.htm) | Project a 3D point orthogonally onto a surface (to find the nearest point). This method is meant to be used when a good approximate solution for the projection is available. Throws InvalidOperationException if the projection fails. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Axis](a50b1b88-0918-cb30-b5f8-84e1f1d2dd6c.htm) | Axis of the cone. This is the Z axis of the local coordinate system associated with this cone. |
| Public property | [HalfAngle](6f71508a-2228-bd57-f851-d2d540f4704e.htm) | Cone angle. |
| Public property | [IsValidObject](6429595a-a6e1-2501-1e60-9c53814a9108.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public property | [OrientationMatchesParametricOrientation](451b549f-2bc4-4f37-9f32-981fe18868a8.htm) | Indicates whether this Surface's orientation is the same as or opposite to its parametric orientation. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public property | [Origin](41ec6924-4e43-9375-31a4-bdbcf209b454.htm) | Apex of the cone. This is the origin of the local coordinate system associated with this cone. |
| Public property | [XDir](9f38585d-9ab8-5f41-7713-14f7acd5760e.htm) | X axis of the local coordinate system associated with this cone. |
| Public property | [YDir](04a0fdd6-3ee4-df1f-c571-5e81550c65cf.htm) | X axis of the local coordinate system associated with this cone. |

# See Also

[ConicalSurface Class](bcc299b6-ff1a-7f0c-c5da-8b040a326899.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)