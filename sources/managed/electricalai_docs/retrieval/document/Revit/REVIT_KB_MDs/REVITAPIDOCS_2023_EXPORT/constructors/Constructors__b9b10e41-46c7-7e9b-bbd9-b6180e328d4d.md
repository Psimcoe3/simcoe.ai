[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### XYZ Members

---



|  |
| --- |
| [XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Operators](#operatorTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [XYZ](a50bf8d1-dced-8a0f-78e1-5b45d5022f20.htm) | Creates a default XYZ with the values (0, 0, 0). |
| Public method | [XYZ(Double, Double, Double)](fcb91231-2665-54b9-11d6-7ebcb7f235e2.htm) | Creates an XYZ with the supplied coordinates. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Add](f6f3d7e1-7a31-d4ac-f268-5cb977aed424.htm) | Adds the specified vector to this vector and returns the result. |
| Public method | [AngleOnPlaneTo](417e2c71-f806-746c-c638-d54d220f8476.htm) | Returns the angle between this vector and the specified vector projected to the specified plane. |
| Public method | [AngleTo](4251dd2b-1b48-8b2e-7159-02333cdf39e6.htm) | Returns the angle between this vector and the specified vector. |
| Public method | [CrossProduct](c5c099ad-e9f5-976b-94ee-d96af1c677f3.htm) | The cross product of this vector and the specified vector. |
| Public method | [DistanceTo](ecbbee02-8f32-d5e9-a565-9c072543ea4f.htm) | Returns the distance from this point to the specified point. |
| Public method | [Divide](263802a2-959a-5a44-4991-26964943ca75.htm) | Divides this vector by the specified value and returns the result. |
| Public method | [DotProduct](63e0ee6c-b612-7140-7805-d32c10f7a8bc.htm) | The dot product of this vector and the specified vector. |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetLength](73e56449-890f-e446-9190-6e787f928886.htm) | Gets the length of this vector. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [IsAlmostEqualTo(XYZ)](72feac6d-3f77-10ea-8ba8-087ab43e76b2.htm) | Determines whether this vector and the specified vector are the same within the tolerance (1.0e-09). |
| Public method | [IsAlmostEqualTo(XYZ, Double)](81a72471-bfa6-18ec-db83-911a49c3f4e8.htm) | Determines whether 2 vectors are the same within the given tolerance. |
| Public method | [IsUnitLength](83fd26c0-15dc-ac21-a2af-9567438b0605.htm) | The boolean value that indicates whether this vector is of unit length. |
| Public method Static member | [IsWithinLengthLimits](ac2171af-4250-8a30-faa7-4d7030d29a03.htm) | Validates that the input point is within Revit design limits. |
| Public method | [IsZeroLength](c49661af-4fea-861d-2fcd-c54b6db50d9a.htm) | The boolean value that indicates whether this vector is a zero vector. |
| Public method | [Multiply](81e7b833-bed9-f797-e4ad-9e6df4b0cc12.htm) | Multiplies this vector by the specified value and returns the result. |
| Public method | [Negate](a49329de-862d-cdfd-4154-6260a74507a1.htm) | Negates this vector. |
| Public method | [Normalize](6228ceb8-100b-daf8-78cf-0b7f514a1338.htm) | Returns a new XYZ whose coordinates are the normalized values from this vector. |
| Public method | [Subtract](2ef3475e-245b-7988-062d-966d213b7863.htm) | Subtracts the specified vector from this vector and returns the result. |
| Public method | [ToString](634eeb2a-2ca8-7950-8b79-6cfdc4f1ba73.htm) | Gets formatted string showing (X, Y, Z) with values formatted to 9 decimal places. (Overrides  Object ToString  .) |
| Public method | [TripleProduct](d6e9b965-f5ed-60c2-2575-ac2999e76eb5.htm) | The triple product of this vector and the two specified vectors. |

# Operators

|  | Name | Description |
| --- | --- | --- |
| Public operator Static member | [Addition](e19b0989-f628-ba42-a67e-7e3cad42df4c.htm) | Adds the two specified vectors and returns the result. |
| Public operator Static member | [Division](33091c6f-88ed-1263-33d6-2b0070b24268.htm) | Divides the specified vector by the specified value. |
| Public operator Static member | [Multiply(Double, XYZ)](4fd3fab2-424f-907b-b3b9-6507eebb2e5a.htm) | Multiplies the specified number and the specified vector. |
| Public operator Static member | [Multiply(XYZ, Double)](f86834d9-8bc4-3f1d-0032-ca9d9d5cd5a6.htm) | Multiplies the specified number and the specified vector. |
| Public operator Static member | [Subtraction](bc4fdb82-362f-864d-beb4-2292091ec49c.htm) | Subtracts the two specified vectors and returns the result. |
| Public operator Static member | [UnaryNegation](c9c8953a-7999-cc2b-3dc5-d27e2229563a.htm) | Negates the specified vector and returns the result. |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [BasisX](a3d8e6ab-72ef-84c6-d058-dc67b4090219.htm) | The basis of the X axis. |
| Public property Static member | [BasisY](3ace8772-001c-443d-ab7d-46ada4dba628.htm) | The basis of the Y axis. |
| Public property Static member | [BasisZ](b4c898a3-d1c7-4655-7b9a-3f139e8db9b1.htm) | The basis of the Z axis. |
| Public property | [Item](400363d5-88fa-6586-6a2b-ef0a0ed8d0e2.htm) | Indexed access to coordinates. |
| Public property | [X](b4d890c1-d278-c8a0-c4c9-6dfe9c7e68df.htm) | Gets the first coordinate. |
| Public property | [Y](10f45749-699b-33fa-22e0-c5bed400f097.htm) | Gets the second coordinate. |
| Public property | [Z](645a3f94-30c9-18b5-947d-c06ddd760691.htm) | Gets the third coordinate. |
| Public property Static member | [Zero](666188ff-d3a5-73e0-b0a6-a269e2767526.htm) | The coordinate origin or zero vector. |

# See Also

[XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)