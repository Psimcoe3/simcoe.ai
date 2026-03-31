[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TessellatedShapeBuilder Members

---



|  |
| --- |
| [TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [TessellatedShapeBuilder](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [TessellatedShapeBuilder](2018769c-6575-1926-7978-539291b3ff8b.htm) | Constructs a new instance of a TessellatedShapeBuilder. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddFace](401c4066-4ec1-be8c-53ae-daea44f3244d.htm) | Adds a face to the currently open connected face set. |
| Public method | [AreTargetAndFallbackCompatible](fc565805-bda1-2cd3-6bf0-e0defa4edfc9.htm) | Checks whether this combination of fallback and target parameters can be used as a valid combination of inputs. |
| Public method | [Build](3b67078d-f8fd-83f4-ee2e-b83e8ec23a23.htm) | Builds the designated geometrical objects from the stored face sets. Stores the result in this TessellatedShapeBuilder object. |
| Public method | [CancelConnectedFaceSet](11a71aab-1685-27ad-10c4-328e4a02b4fb.htm) | Cancels the current face set - i.e., all data from it will be lost and the builder will have no open connected face set anymore. |
| Public method | [Clear](8c2cd942-f8c3-3288-bac6-8d4d1f064714.htm) | Erases all face set and clears the logs, if any. |
| Public method | [CloseConnectedFaceSet](0bebb71c-317e-3dbc-1304-169561e22214.htm) | Closes the currently open connected face set. |
| Public method Static member | [CreateMeshByExtrusion](16bfff9e-b581-94b8-4797-cb880d79e793.htm) | Builds a mesh by extruding curve loop(s) along extrusion distance. |
| Public method | [Dispose](efbfadf8-519d-7f66-8553-e887ed3058f1.htm) | (Inherited from  [ShapeBuilder](66c1678c-2e01-e0de-1386-5a0e1eb3ccff.htm)  .) |
| Public method | [DoesFaceHaveEnoughLoopsAndVertices](894594d4-e75a-843e-ed5f-c9554feec2f4.htm) | Checks whether 'face' has enough loops and vertcies to be valid. |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetBuildResult](136e8763-4156-4ffe-0fcc-45af9dbb6c14.htm) | Get the built geometry, build status and other data stored in TessellatedShapeBuilderResult. Clears the stored data. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [OpenConnectedFaceSet](186da29a-caa2-99ea-1b2a-722c1656c44a.htm) | Opens a new connected face set. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Fallback](59acf1d0-742a-45eb-df1c-edbb136279a4.htm) | Defines acceptable fallback if the desired type of geometry can't be built. |
| Public property | [GraphicsStyleId](b52fe304-95a0-77c8-4b4c-e3c18c16677d.htm) | Optional - if set, the built geometry will use that graphics style. |
| Public property | [IsFaceSetOpen](0da2193e-aebc-5eb4-353e-ea72a12868bc.htm) | Flag whether the current set of connected faces is open and additional tessellation faces can be added to it. |
| Public property | [IsValidObject](6a5c7474-6ea6-4886-d356-204405406596.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [ShapeBuilder](66c1678c-2e01-e0de-1386-5a0e1eb3ccff.htm)  .) |
| Public property | [LogInteger](c6a84d2a-824d-07e9-4559-79bb80d25e8e.htm) | Integer value used for logging, if it is performed. Usually the number of the face set(s) in the IFC file, from which they are imported. Any value is acceptable. |
| Public property | [LogString](dbfa746b-807f-d58a-cd1c-67ff07f4b968.htm) | String used for logging, if any. Usually the name of the file from which face sets were imported. |
| Public property | [NumberOfCompletedFaceSets](aacc351c-0e65-7d1d-c177-627de5e9974a.htm) | Number of completed face sets. |
| Public property | [OwnerInfo](5c2c3e95-ae6e-f303-a770-662acf186181.htm) | String used for logging, if any. Usually describes the element or object, which either defined or will own the geoemtrical objects to be built. |
| Public property | [Target](2e6f38a0-cabd-5fac-34dc-40af993135c7.htm) | Requests the type of geometry to be built. |

# See Also

[TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)