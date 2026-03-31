[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NurbsSurfaceData Members

---



|  |
| --- |
| [NurbsSurfaceData Class](7d65dbde-8aac-7d7d-e811-a6c91a541de4.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [NurbsSurfaceData](7d65dbde-8aac-7d7d-e811-a6c91a541de4.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [NurbsSurfaceData](6fdc9f8a-a443-a69f-2d9b-82cad9bf7544.htm) | Copy constructor. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method Static member | [Create](94b4c433-5458-d1ab-d5c9-f526f288d1ff.htm) | Construct NurbsSurfaceData based on NURBS surface data, where the weights are supplied. The NURBS surface will be (piecewise) polynomial if all the weights are equal, rational if not. Note: A rational polynomial is a quotient of two polynomials; this includes a polynomial, which can be thought of as a quotient with denominator equal to 1. |
| Public method | [Dispose](27a918fc-a321-7712-4594-9dd7eb2d2140.htm) | Releases all resources used by the  [NurbsSurfaceData](7d65dbde-8aac-7d7d-e811-a6c91a541de4.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetControlPoints](409fe43e-03a5-b9d6-5bf4-4f6427e3606e.htm) | Get the list of control points. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetKnotsU](e280fd98-bad6-3fb3-547f-a829ab23a9de.htm) | Get the list of knots in the u-direction. |
| Public method | [GetKnotsV](1b0fea7f-4fd0-bee4-cc1b-773b13b2e36b.htm) | Get the list of knots in the v-direction. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetWeights](a1eec836-1db9-00ef-98eb-923c6a77a952.htm) | Get the list of weights. |
| Public method | [IsValid](6ca835bb-02f9-fe37-01ef-618310cef5ab.htm) | Check if the object contains a valid NurbsSurfaceData. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [DegreeU](fc2de49b-75ef-b407-cecf-3dd0199b775a.htm) | The degree of the spline in the u-direction. |
| Public property | [DegreeV](7bc890a0-c3d3-8e7f-5d9d-148a69de4813.htm) | The degree of the spline in the v-direction. |
| Public property | [IsRational](da17256f-3c20-22c0-1619-5fe2d847752a.htm) | Tells if the spline is rational or not. If it is true (rational), then the NURBS is a piecewise rational polynomial function. If it is false (non-rational), then the NURBS is a piecewise polynomial function. |
| Public property | [IsValidObject](b9517067-344b-5d1b-8c5d-664b7e7115e1.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [ReverseOrientation](57ca8156-bae7-58fc-89a4-88f08aa1f756.htm) | If true, the surface's orientation is opposite to the canonical parametric orientation, otherwise it is the same. The canonical parametric orientation is a counter-clockwise sense of rotation in the uv-parameter plane. Extrinsically, the oriented normal vector for the canonical parametric orientation points in the direction of the cross product dS/du x dS/dv, which S(u, v) is the parameterized surface. |

# See Also

[NurbsSurfaceData Class](7d65dbde-8aac-7d7d-e811-a6c91a541de4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)