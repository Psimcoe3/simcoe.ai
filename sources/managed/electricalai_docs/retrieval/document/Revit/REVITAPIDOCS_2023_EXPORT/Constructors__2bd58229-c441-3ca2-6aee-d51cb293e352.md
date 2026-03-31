[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Transform2D Members

---



|  |
| --- |
| [Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [Transform2D](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [Transform2D(Transform2D)](ad1bd942-9cbc-c269-e3d6-ee2ad8bedbaf.htm) | The copy constructor. |
| Public method | [Transform2D(UV, UV, UV)](8d260105-fb1c-b915-eb12-e038f536ee63.htm) | Constructs the transformation by specifying the vectors and the origin. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AlmostEqual](149b3851-ba79-c3fa-591e-33496f053962.htm) | Determines whether this transformation and the specified transformation are the same within the tolerance (1.0e-09). |
| Public method | [Assign](5646a58f-270e-aa89-505a-a0f293d76e83.htm) | Assigns values from the input transformation to this transformation. |
| Public method Static member | [CreateIdentity](7035cbd5-61fc-432a-abe9-8ba0200ed4dd.htm) | Creates the identity transformation. |
| Public method | [Dispose](e709cdf9-9203-9272-3c6c-fe5dfa90fbce.htm) | Releases all resources used by the  [Transform2D](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetInverse](511bce10-cd5b-963e-4f4f-86e2b4e7ed73.htm) | Gets the inverse transformation of this transformation. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [Multiply](52de67bf-77eb-6065-c702-589319f3cae5.htm) | Multiplies this transformation by the specified transformation and returns the result. |
| Public method | [OfPoint](083f5a56-31c6-e8b7-dc22-cf0f4c25608a.htm) | Applies the transformation to the point and returns the result. |
| Public method | [OfVector](72a66105-55d1-3930-8934-2d46d5dd064d.htm) | Applies the transformation to the vector and returns the result. |
| Public method | [PostScale](4bd89ff0-75cf-f499-e88e-9ff5aaff27fd.htm) | Scales both the linear and translational parts of this transformation and returns the result. |
| Public method | [PreScale](c1f6f144-e9a3-0efb-4d1d-2eba05d849f1.htm) | Scales the linear part of this transformation and returns the result. |
| Public method | [SetToIdentity](fbc7f0fe-3e4c-f2f0-ce2c-478a202cd1e2.htm) | Set this TrfUV to the identity transform. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |
| Public method | [TransformUVDomainIfPossible](977e71c5-7a76-a4ee-5232-f826a00f7471.htm) | Transforms an envelope (  [BoundingBoxUV](e38a0145-4267-0b3f-0718-adb14e34c94e.htm)  ) for one surface to an envelope for a coincident but differently parameterized surface. |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BasisU](2641df76-4f81-d1bb-0086-a621dd89ed5b.htm) | The image of (1, 0) under  [OfVector(UV)](72a66105-55d1-3930-8934-2d46d5dd064d.htm)  . |
| Public property | [BasisV](a4dcbe9f-812e-af13-09b6-852be713397f.htm) | The image of (0, 1) under  [OfVector(UV)](72a66105-55d1-3930-8934-2d46d5dd064d.htm)  . |
| Public property | [Determinant](bfd34778-23af-005d-0c2f-1c6a77bffe10.htm) | The determinant of this transformation. |
| Public property | [HasReflection](9646b8fb-5ab4-8959-1660-4e3624c6d847.htm) | The boolean value that indicates whether this transformation produces reflection (i.e., is orientation-reversing). |
| Public property | [IsConformal](2a9cdce4-7098-7718-5f66-0a5f3f0df768.htm) | The boolean value that indicates whether this transformation is conformal. |
| Public property | [IsIdentity](7c806384-bfde-4460-740d-f968fbdf36cc.htm) | The boolean value that indicates whether this transformation is an identity. |
| Public property | [IsTranslation](5beef120-3918-7a2e-3ec4-d20445899e40.htm) | The boolean value that indicates whether this transformation is a translation. |
| Public property | [IsValidObject](1b6161d1-42da-1365-f796-382f297730da.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [Origin](5204635c-1eea-58b4-4b75-4cb8b1e04c33.htm) | The image of (0, 0) under  [OfPoint(UV)](083f5a56-31c6-e8b7-dc22-cf0f4c25608a.htm)  . This defines the translational part of the transform. |
| Public property | [Scale](30a3e4d2-d70f-aace-95c1-001884d95e6c.htm) | The real number that represents the scale of the conformal transformation. |

# See Also

[Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)