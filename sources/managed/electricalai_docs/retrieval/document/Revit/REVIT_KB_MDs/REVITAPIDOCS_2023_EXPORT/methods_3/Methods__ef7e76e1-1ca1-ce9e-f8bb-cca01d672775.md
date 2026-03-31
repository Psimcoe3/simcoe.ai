[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Plane Members

---



|  |
| --- |
| [Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method Static member | [Create](38aeacdd-59c5-7741-2802-6de25838130f.htm) | Creates a Plane object defined by a local frame of reference. |
| Public method Static member | [CreateByNormalAndOrigin](ab735815-f6bc-aae1-8afc-8505bba18cb5.htm) | Constructs a Plane object from a normal and an origin represented as XYZ objects. Follows the standard conventions for a planar surface. The constructed Plane object will pass through origin and be perpendicular to normal. The X and Y axes of the plane will be defined arbitrarily. |
| Public method Static member | [CreateByOriginAndBasis](425db4fe-1368-0a48-6fb0-9c458035ea6a.htm) | Creates a Plane object defined by the two orthogonal unit vectors and passing through the origin point supplied as arguments. |
| Public method Static member | [CreateByThreePoints](a18aa7a2-71b6-5fa2-8ca8-abadedb638d7.htm) | Creates a Plane object passing through three points supplied as arguments. |
| Public method | [Dispose](c9ee1344-bc19-d833-52e7-dcc4931fe085.htm) | (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetBoundingBoxUV](5084214f-219f-780f-fe03-f16b62b2660d.htm) | Gets the UV bounding box of the surface. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [Project](802cc09b-d0a4-dfc5-8ca1-e8c5e8cd4ced.htm) | Project a 3D point orthogonally onto a surface (to find the nearest point). Throws InvalidOperationException if the projection fails. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | [ProjectWithGuessPoint](db8cc42a-9f34-611a-d9c5-852f3935887f.htm) | Project a 3D point orthogonally onto a surface (to find the nearest point). This method is meant to be used when a good approximate solution for the projection is available. Throws InvalidOperationException if the projection fails. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](6429595a-a6e1-2501-1e60-9c53814a9108.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public property | [Normal](480fe97b-26fd-6376-ab66-bb204862572b.htm) | Plane normal. |
| Public property | [OrientationMatchesParametricOrientation](451b549f-2bc4-4f37-9f32-981fe18868a8.htm) | Indicates whether this Surface's orientation is the same as or opposite to its parametric orientation. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public property | [Origin](65f19b4f-d73c-25ef-0c88-ce2ebade5bcf.htm) | Plane origin. |
| Public property | [XVec](94bf72b9-4df7-07f2-00d9-8b350622695a.htm) | Axis defining the first parametric direction of the plane. |
| Public property | [YVec](b1acdb7b-b830-8adc-fb01-fd809c21d310.htm) | Axis defining the second parametric direction of the plane. |

# See Also

[Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)