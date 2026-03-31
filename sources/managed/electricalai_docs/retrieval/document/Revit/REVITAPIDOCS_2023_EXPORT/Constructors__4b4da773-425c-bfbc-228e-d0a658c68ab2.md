[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Transform Members

---



|  |
| --- |
| [Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Operators](#operatorTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [Transform](5ad3cfba-926d-26ef-9dd0-02c8acb2c854.htm) | The copy constructor. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AlmostEqual](91717709-a62e-9880-527e-d52a9a0ae048.htm) | Determines whether this transformation and the specified transformation are the same within the tolerance (1.0e-09). |
| Public method Static member | [CreateReflection](7c6c9293-64ca-ef47-3365-803e7f802883.htm) | Creates a transform that represents a reflection across the given plane. |
| Public method Static member | [CreateRotation](01cddc01-b348-3c51-d2ad-c61ac64c6da4.htm) | Creates a transform that represents a rotation about the given axis at (0, 0, 0). |
| Public method Static member | [CreateRotationAtPoint](8da64cca-bea9-4750-1f79-f6de3867191e.htm) | Creates a transform that represents a rotation about the given axis at the specified point. |
| Public method Static member | [CreateTranslation](b1a26f8c-1593-5b74-d78e-d4261ec5ebe5.htm) | Creates a transform that represents a translation via the specified vector. |
| Public method | [Dispose](7c03212a-b587-1c89-3912-efea0d2619c5.htm) | Causes the object to release immediately any resources it may be utilizing. (Inherited from  [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)  .) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [Multiply](dca45f2a-e404-765e-4bb8-cf39982bf034.htm) | Multiplies this transformation by the specified transformation and returns the result. |
| Public method | [OfPoint](55c834aa-ef75-f6f1-4c89-d908d842e9d6.htm) | Applies the transformation to the point and returns the result. |
| Public method | [OfVector](4d5b7075-1b79-639d-5da2-eb23372bc888.htm) | Applies the transform to the vector |
| Public method | [ScaleBasis](35360886-77c5-4117-e395-b83b95f9c884.htm) | Scales the basis vectors of this transformation and returns the result. |
| Public method | [ScaleBasisAndOrigin](460caa53-d288-7cfe-dbb8-eadf4682329d.htm) | Scales the basis vectors and the origin of this transformation and returns the result. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Operators

|  | Name | Description |
| --- | --- | --- |
| Public operator Static member | [Multiply](d1ff39c4-3abd-f69c-d73d-c008b38f2d8c.htm) | Multiplies the two specified transforms. |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Basis](00944fa6-49d9-4564-9f55-c0f71fa14706.htm) | Defines the basis of the old coordinate system in the new coordinate system. |
| Public property | [BasisX](ac4f8d40-cd21-a6ed-0366-61cb86edb757.htm) | The basis of the X axis of this transformation. |
| Public property | [BasisY](dfae1c2b-d0fd-0b56-3610-b7055f4169d3.htm) | The basis of the Y axis of this transformation. |
| Public property | [BasisZ](f0a5bbf5-41f2-ec36-80c4-207e9bae36d9.htm) | The basis of the Z axis of this transformation. |
| Public property | [Determinant](4bf53ffc-c955-ad6c-a446-263cbb9e8b28.htm) | The determinant of this transformation. |
| Public property | [HasReflection](dbdbb5b6-157a-9b89-b9ee-03cf1fe4d58f.htm) | The boolean value that indicates whether this transformation produces reflection. |
| Public property Static member | [Identity](2eb2a180-c7ef-a0c0-0fa4-baef2901c351.htm) | The identity transformation. |
| Public property | [Inverse](10b30358-917f-31f3-d17e-24f64d157a68.htm) | The inverse transformation of this transformation. |
| Public property | [IsConformal](e8d5bf2d-810b-5062-04c6-df09819dac47.htm) | The boolean value that indicates whether this transformation is conformal. |
| Public property | [IsIdentity](67276072-ca45-6c26-a249-fa6804d13053.htm) | The boolean value that indicates whether this transformation is an identity. |
| Public property | [IsReadOnly](d516bcd2-a3fd-a578-58f6-f1add979bd07.htm) | Identifies if the object is read-only or modifiable. (Inherited from  [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)  .) |
| Public property | [IsTranslation](cc5067ec-8f08-a8cd-bdd9-88c10e17a08d.htm) | The boolean value that indicates whether this transformation is a translation. |
| Public property | [Origin](9c67a7e5-c869-bfb9-c6fa-e5ac356868f0.htm) | Defines the origin of the old coordinate system in the new coordinate system. |
| Public property | [Scale](767a8668-6153-b003-1027-e8a9de3b2f7d.htm) | The real number that represents the scale of the transformation. |

# See Also

[Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)