[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CylindricalHelix Members

---



|  |
| --- |
| [CylindricalHelix Class](fdaa7f4a-e680-8d7e-3a9b-677b082432f5.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [CylindricalHelix](fdaa7f4a-e680-8d7e-3a9b-677b082432f5.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Clone](071f6ca9-f243-4655-924c-7beb881b100f.htm) | Returns a copy of this curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [ComputeClosestPoints](04ab73d1-bc85-9b87-aace-4272a0c7c3e4.htm) | Find the closest points between two curves. Closest points mean closest pairs of points, each pair consisting of a point on this, say P1, and a point on other curve, say P2. P1 and P2 are closest locally. Each pairs of closest points will be represented by the corresponding parameter values with respect to the two curves and the 3d points. A closest pair is also known as a pair of critical points of the distance function between points of the two curves. If the input parameter returnAllCriticalPoints is set to false, then the function will return only pairs with minimum distance. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [ComputeDerivatives](93092a44-85f1-15be-a618-817c763f8994.htm) | Returns the vectors describing the curve at the specified parameter. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [ComputeNormalizedParameter](d42c45a0-7525-aab6-2527-16148dd6dcc1.htm) | Computes the normalized curve parameter from the raw parameter. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [ComputeRawParameter](ac00deb9-9e8d-6bcb-60ac-b6f6a7520ea2.htm) | Computes the raw parameter from the normalized parameter. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method Static member | [Create](851cb6a7-fcc3-a518-78ae-98c43c728b1b.htm) | Create a cylindrical helix. |
| Public method | [CreateOffset](450217f3-c0b5-42af-3a05-376ae383d28a.htm) | Creates a new curve that is an offset of the existing curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [CreateReversed](722a403d-a95c-557c-e92e-ad6757dc421c.htm) | Creates a new curve with the opposite orientation of the existing curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [CreateTransformed](4f014114-64f7-fff1-f24f-bfc6e0cad82a.htm) | Crates a new instance of a curve as a transformation of this curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [Dispose](7c03212a-b587-1c89-3912-efea0d2619c5.htm) | Causes the object to release immediately any resources it may be utilizing. (Inherited from  [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)  .) |
| Public method | [Distance](95efa592-d444-acb8-6460-e2757b96e053.htm) | Returns the shortest distance from the specified point to this curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [Equals](26d6c913-b5b6-436f-dee9-19ceca7e53c6.htm) | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)  .) |
| Public method | [Evaluate](1145f18e-3e01-60df-e438-e176c38c3ce9.htm) | Evaluates and returns the point that matches a parameter along the curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [GetEndParameter](0f4b2c25-35f8-4e3c-c71a-0d41fb6935ce.htm) | Returns the raw parameter value at the start or end of this curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [GetEndPoint](a02da994-2976-38c0-e16b-20292de9fe57.htm) | Returns the 3D point at the start or end of this curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [GetEndPointReference](5619a3fd-38e1-fb56-7286-2e5f33a3b2b8.htm) | Returns a stable reference to the start point or the end point of the curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [GetHashCode](08e8412d-4002-22a5-858d-f55eba1bed34.htm) | Gets the integer value of the geometry object as hash code (Inherited from  [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [Intersect(Curve)](90e86110-9bce-6e43-c18a-4d67380008bb.htm) | Calculates the intersection of this curve with the specified curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [Intersect(Curve, IntersectionResultArray )](51961478-fb36-e00b-2d1b-7db27b0a09e6.htm) | Calculates the intersection of this curve with the specified curve and returns the intersection results. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [IsInside(Double)](2782b130-915f-8467-22f1-629b9e0c1574.htm) | Indicates whether the specified parameter value is within this curve's bounds. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [IsInside(Double, Int32 )](64b9685d-b790-d2cb-f9f7-7184669a9ee0.htm) | Indicates whether the specified parameter value is within this curve's bounds and outputs the end index. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [MakeBound](f9bc51b4-50a3-de79-4d7e-401ab2dbebb2.htm) | Changes the bounds of this curve to the specified values. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [MakeUnbound](31ef6a2e-0e39-a394-b6ee-4e4df56d8380.htm) | Makes this curve unbound. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [Project](b87fc3e4-ea25-2a75-5b5a-53065b099d2a.htm) | Projects the specified point on this curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [SetGraphicsStyleId](bd71365d-d2f2-2758-c220-a2a5c71cc6e4.htm) | Sets the graphics style id for this curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | [Tessellate](f95f3199-3251-c708-c5a3-a0e9ef95ecfa.htm) | Valid only if the curve is bound. Returns a polyline approximation to the curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ApproximateLength](202c6c2c-23cf-aee3-fc9e-24b24a46e293.htm) | The approximate length of the curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public property | [BasePoint](23159307-9167-7a91-5d8f-87e8bac93571.htm) | The base point of the axis of the cylindrical helix. |
| Public property | [GraphicsStyleId](4103f148-957e-3f44-9ccd-a5ed6702c689.htm) | The ElementId of the GeometryObject's GraphicsStyle (Inherited from  [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)  .) |
| Public property | [Height](98caadf4-9780-2cf9-c089-e3501979250b.htm) | Height of the cylindrical helix. |
| Public property | [Id](abb781de-203f-4035-784b-713e65cca169.htm) | A unique integer identifying the GeometryObject in its associated non view-specific GeometryElement. (Inherited from  [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)  .) |
| Public property | [IsBound](cdf2a8e3-31fe-996a-1e94-e5eb77378279.htm) | Describes whether the parameter of the curve is restricted to a particular interval. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public property | [IsClosed](a8297234-87a1-111c-fb24-ba1a9bd1d8a3.htm) | Describes whether the curve is closed. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public property | [IsCyclic](b3a443d0-db6d-332b-62b4-41b534987608.htm) | The boolean value that indicates whether this curve is cyclic. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public property | [IsElementGeometry](be3ad18d-a9d3-25ed-6200-4f71d3cd4754.htm) | Indicates whether this geometry is obtained directly from an Element. (Inherited from  [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)  .) |
| Public property | [IsReadOnly](d516bcd2-a3fd-a578-58f6-f1add979bd07.htm) | Identifies if the object is read-only or modifiable. (Inherited from  [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)  .) |
| Public property | [IsRightHanded](5fe9f7b7-332c-f33b-ecb2-d9ba1445562f.htm) | True if the helix is right handed, false if the helix is left handed. |
| Public property | [Length](c6bca686-f136-ce45-8668-8d430267cd0d.htm) | The exact length of the curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public property | [Period](30b0f487-7728-9617-be52-616ca42da762.htm) | The period of this curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public property | [Pitch](9c11bf63-8235-b2bc-2f6b-7ce8af45f847.htm) | The pitch of the cylindrical helix. |
| Public property | [Radius](6a8ce591-5c0b-4712-f847-58a2996c7b7e.htm) | The radius of the cylindrical helix. |
| Public property | [Reference](d5e10517-24fa-4627-43be-8981746d30c8.htm) | Returns a stable reference to the curve. (Inherited from  [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)  .) |
| Public property | [Visibility](b504868c-1588-3488-8cdf-d8e45ef23fa0.htm) | The visibility. (Inherited from  [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)  .) |
| Public property | [XVector](cf831523-4e0d-1793-9163-06da91c0ac01.htm) | The X direction vector. |
| Public property | [YVector](6d243b0d-672a-dfeb-3ce0-8f74fd8fc21a.htm) | The Y direction vector. |
| Public property | [ZVector](79b811b5-a7cd-2e6b-bf62-a4942ea57ef9.htm) | The Z direction vector, which is same as the axis direction vector. |

# See Also

[CylindricalHelix Class](fdaa7f4a-e680-8d7e-3a9b-677b082432f5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)