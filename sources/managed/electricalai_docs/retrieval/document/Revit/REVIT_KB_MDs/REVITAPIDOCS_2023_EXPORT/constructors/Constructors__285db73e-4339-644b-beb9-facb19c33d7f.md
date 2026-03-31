[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurveLoop Members

---



|  |
| --- |
| [CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [CurveLoop](24352cb6-d39e-afbc-800e-38d0ebf98fe6.htm) | Constructs a new empty curve loop. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Append](9ecde812-a299-b823-35fc-4428e9298602.htm) | Append the curve to this loop. |
| Public method Static member | [Create](5422ec92-2b9e-6b33-80ac-417b8336ae18.htm) | Creates a new curve loop. |
| Public method Static member | [CreateViaCopy](ea9a14d7-4b74-009e-b26e-5a90da82de2a.htm) | Creates a new curve loop as a copy of the input. |
| Public method Static member | [CreateViaOffset(CurveLoop, IList Double , XYZ)](3097f423-9b0e-5496-bae2-3a82b6875414.htm) | Creates a new curve loop that is an offset of the existing curve loop. |
| Public method Static member | [CreateViaOffset(CurveLoop, Double, XYZ)](6cffc624-d197-0f3b-b68c-26b9c9a0adf8.htm) | Creates a new curve loop that is an offset of the existing curve loop. |
| Public method Static member | [CreateViaThicken(Curve, Double, XYZ)](596ccb71-a32f-0a01-8366-58619263c733.htm) | Creates a new closed curve loop by thickening the input curve with respect to a given plane. |
| Public method Static member | [CreateViaThicken(CurveLoop, Double, XYZ)](1755d6bf-5993-58dd-a966-98c83ef86891.htm) | Creates a new closed curve loop by thickening the input open curve loop with respect to a given plane. |
| Public method Static member | [CreateViaTransform](050e66f2-9202-ef95-2723-f19d8f4dcf5b.htm) | Creates a new curve loop as a transformed copy of the input curve loop. |
| Public method | [Dispose](77bad211-6dcf-cb86-c66f-ac25384ccd31.htm) | Releases all resources used by the  [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [Flip](a7067941-9bcf-791b-9f1f-ae6284332e54.htm) | Reverses the orientation of the curve loop. |
| Protected method | [GetBasicIEnumerator](b55fa6c3-c8fe-38c5-877f-7fdfe3faf4b6.htm) | Returns an enumerator that iterates through a collection. |
| Public method | [GetCurveLoopIterator](56bdb38b-2385-7e32-13db-6cfd6dbe3e65.htm) | Returns a curve that iterates through the curve loop. |
| Public method | [GetEnumerator](4a4f54be-6f2c-e526-8515-58d00364212a.htm) | Returns an enumerator that iterates through a collection. |
| Public method | [GetExactLength](67e54cf8-f9ba-fb2c-5519-6b54bdb1c51d.htm) | Returns the sum of exact lengths of all curves in the loop. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetPlane](87e64330-90d4-c6bb-944d-d2dbb1529948.htm) | Gets the plane of the curve loop, if it is planar. |
| Public method | [GetRectangularHeight](f4bafc6a-1218-6c24-e806-c4d92204cbaa.htm) | Returns the width of a curve loop if it is rectangular with respect to the projection plane. |
| Public method | [GetRectangularWidth](dc6685c1-6c19-34a7-dd7f-5d37b7446649.htm) | Returns the width of a curve loop if it is rectangular with respect to the projection plane. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [HasPlane](69c92503-2025-ddab-ba91-3085aa2e8117.htm) | Identifies if the CurveLoop is planar. |
| Public method | [IsCounterclockwise](ca966f5d-7db8-b28a-928e-12063dd143e6.htm) | Determines if this CurveLoop is oriented counter-clockwise (CCW) or clockwise (CW) with respect to the specified 3D direction. |
| Public method | [IsOpen](ac68d75b-1fda-28f2-c5b2-01c24ff1b8b8.htm) | Returns whether the curve loop is open or closed, as determined by an internal flag. |
| Public method | [IsRectangular](5a82c7ad-4b6e-a62c-6b0c-7fe790886995.htm) | Identifies if the curve loop is rectangular with respect to a given projection plane. |
| Public method | [NumberOfCurves](1b5d6569-0550-4113-f8d1-3cc94201c5a4.htm) | Returns the number of curves in the curve loop. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |
| Public method | [Transform](01e7c70f-9458-128f-b6bc-84acfd658dc5.htm) | Transforms this curve loop and all of its component curves by the supplied transformation. |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](32444567-8b25-6cce-f0de-2bedf9f2da2e.htm) | Specifies whether the .NET object represents a valid Revit entity. |

# See Also

[CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)