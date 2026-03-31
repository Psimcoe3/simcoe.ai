[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeDrivenAccessor Members

---



|  |
| --- |
| [RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [RebarShapeDrivenAccessor](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [ComputeDrivingCurves](46288659-93f8-62ee-2d7b-94b7a84e44ab.htm) | Compute the driving curves. |
| Public method | [Dispose](fa409733-2af6-a937-5907-3c39f0f318cf.htm) | Releases all resources used by the  [RebarShapeDrivenAccessor](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetBarPositionTransform](b3f84e4d-0a50-26ef-2edc-eb0678929f0c.htm) | Return a transform representing the relative position of any individual bar in the set. |
| Public method | [GetDistributionPath](07a6bc0a-4f85-2d2b-c877-426e5024b4a8.htm) | The distribution path of a rebar set. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [ScaleToBox](7d25297a-46f1-7fe9-e815-a7a9c4672567.htm) | Move and resize the bar to fit within a specified box. The arguments are interpreted as an arbitrary rectangle in 3D with vertices: origin, origin+xVec, origin+xVec+yVec, origin+yVec. The algorithm then proceeds as follows. First the bar is given the default values of the shape parameters from the shape definition. Then, if it is possible to do so without violating the shape definition, the parameter values are scaled so that the width and height of the shape (including bar thickness) match the lengths of xVec and yVec. If there is no way to do this within the shape definition due to overconstraining, a compromise is attempted, such as scaling the whole shape until either the width or the height is correct. Finally the shape is rotated to match the coordinate system of the box. The algorithm is the same one used in one-click placement. |
| Public method | [ScaleToBoxFor3D](63da560e-ad71-8421-8a65-c2ba846a289c.htm) | Move and resize a spiral or multiplanar instance to fit within a specified box. The arguments are interpreted as an arbitrary rectangle in 3D with vertices: origin, origin+xVec, origin+xVec+yVec, origin+yVec. One end of the rebar shape is inscribed in this rectangle following the procedure described for the ScaleToBox method. The other end is placed in the parallel plane at distance (center-to-center) given by the height argument, in the direction of (xVec x yVec). Note that spiral shapes interpret the input arguments using a different convention than multiplanar shapes. For spiral shapes, the spiral start will be placed in the rectangle defined by origin, xVec, yVec, and the end of the spiral will be placed in the parallel plane. For multiplanar shapes, the rebar is placed with its primary shape definition located in the parallel plane defined by the height argument, and its connector segments extending in the direction opposite (xVec x yVec). This method replaces ScaleToBoxForSpiral() from prior releases. |
| Public method | [SetLayoutAsFixedNumber](017a567e-6087-745c-ed82-4a71b42ea203.htm) | Sets the Layout Rule property of rebar set to FixedNumber. |
| Public method | [SetLayoutAsMaximumSpacing](fcadb398-7b67-9259-a1a2-c6afd831dc14.htm) | Sets the Layout Rule property of rebar set to MaximumSpacing |
| Public method | [SetLayoutAsMinimumClearSpacing](fafd15e8-dc6b-7cc3-b6ec-c4ce9eb4b1af.htm) | Sets the Layout Rule property of rebar set to MinimumClearSpacing |
| Public method | [SetLayoutAsNumberWithSpacing](3d8b7f68-cfe0-c1ac-c8b3-532a80155e0d.htm) | Sets the Layout Rule property of rebar set to NumberWithSpacing |
| Public method | [SetLayoutAsSingle](d9e95eca-6e25-eb15-3ee9-49e61f9b5e2b.htm) | Sets the Layout Rule property of rebar set to Single. |
| Public method | [SetRebarShapeId](c4f1bdd6-8b80-28da-a88a-e8eb9139cdd8.htm) | Changes the RebarShape element that defines the shape of the rebar. Changing the value of this member causes the Rebar instance to choose values for its shape parameters to preserve its previous shape as closely as possible |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ArrayLength](b9d15e52-d912-a5ad-9fb8-4ff22849ec1f.htm) | Identifies the distribution path length of rebar set. |
| Public property | [BarsOnNormalSide](dc6806bd-c813-1964-b768-2177e718bb5f.htm) | Identifies if the bars of the rebar set are on the same side of the rebar plane indicated by the normal. |
| Public property | [BaseFinishingTurns](5bdafcc3-2ade-3169-83f4-40cd75f42b90.htm) | For a spiral, the number of finishing turns at the lower end of the spiral. |
| Public property | [Height](c51afe43-2b8d-35ef-245d-7e97b6a86057.htm) | For a spiral, the overall height. |
| Public property | [IsValidObject](192f91bf-34dc-7ca0-bb5d-b4c1b7979503.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [MultiplanarDepth](28ff121c-c1a4-6598-f6f5-0b1411d866fd.htm) | For a multiplanar rebar, the depth of the instance. |
| Public property | [Normal](d6ecbc19-e4dd-536c-b83a-1019b1663e04.htm) | A unit-length vector normal to the plane of the rebar |
| Public property | [Pitch](af5eddc3-9560-eddc-e503-10815b4b01c6.htm) | For a spiral, the pitch, or vertical distance traveled in one rotation. |
| Public property | [TopFinishingTurns](131de72d-223e-239f-6522-c62738b96744.htm) | For a spiral, the number of finishing turns at the upper end of the spiral. |

# See Also

[RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)