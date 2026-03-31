[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HermiteSurface Members

---



|  |
| --- |
| [HermiteSurface Class](55ff0501-286a-79d6-0530-b34ce6ce09af.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [HermiteSurface](55ff0501-286a-79d6-0530-b34ce6ce09af.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method Static member | [Create(Int32, Int32, IList XYZ )](cf4eb83b-5e6a-8f36-7c24-b215815b850b.htm) | Create a non-periodic Hermite surface using a net of 3D points as input. |
| Public method Static member | [Create(Int32, Int32, IList XYZ , Boolean, Boolean)](e4480853-0cfd-3856-d931-a0b456a09fe5.htm) | Create a Hermite surface using a net of 3D points as input. Specify periodicity in U and V direction. |
| Public method | [Dispose](c9ee1344-bc19-d833-52e7-dcc4931fe085.htm) | (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetBoundingBoxUV](5084214f-219f-780f-fe03-f16b62b2660d.htm) | Gets the UV bounding box of the surface. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [IsValid](bcd3ba1e-de42-cca3-3815-4c8f41c690a4.htm) | Checks whether this HermiteSurface object is valid. |
| Public method | [Project](802cc09b-d0a4-dfc5-8ca1-e8c5e8cd4ced.htm) | Project a 3D point orthogonally onto a surface (to find the nearest point). Throws InvalidOperationException if the projection fails. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | [ProjectWithGuessPoint](db8cc42a-9f34-611a-d9c5-852f3935887f.htm) | Project a 3D point orthogonally onto a surface (to find the nearest point). This method is meant to be used when a good approximate solution for the projection is available. Throws InvalidOperationException if the projection fails. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](6429595a-a6e1-2501-1e60-9c53814a9108.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |
| Public property | [OrientationMatchesParametricOrientation](451b549f-2bc4-4f37-9f32-981fe18868a8.htm) | Indicates whether this Surface's orientation is the same as or opposite to its parametric orientation. (Inherited from  [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)  .) |

# See Also

[HermiteSurface Class](55ff0501-286a-79d6-0530-b34ce6ce09af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)