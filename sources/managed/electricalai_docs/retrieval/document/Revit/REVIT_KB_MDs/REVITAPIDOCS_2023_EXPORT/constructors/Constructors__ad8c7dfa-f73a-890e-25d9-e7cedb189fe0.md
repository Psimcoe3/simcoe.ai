[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImageTypeOptions Members

---



|  |
| --- |
| [ImageTypeOptions Class](981135c3-777b-df9b-747f-60a35b74e00e.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ImageTypeOptions](981135c3-777b-df9b-747f-60a35b74e00e.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ImageTypeOptions(ExternalResourceReference, ImageTypeSource)](df96413a-2ff3-128b-7276-28980e2689ce.htm) | Constructs a new instance of the ImageTypeOptions object. |
| Public method | [ImageTypeOptions(String, Boolean, ImageTypeSource)](7dda4131-548f-7c39-4dcd-ba9b85846018.htm) | Constructs a new instance of the ImageTypeOptions object.  The provided string path must specify a local file. The path can be absolute or relative to the project's location.  This constructor saves an additional setting that indicates whether the imagetype will be a link or an import. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](8665df9b-7082-9cd5-b4dd-b0f1aa650140.htm) | Releases all resources used by the  [ImageTypeOptions](981135c3-777b-df9b-747f-60a35b74e00e.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [IsValid](47f3832b-9cf5-4628-214d-7e7e7d705393.htm) | If true the ImageTypeOptions can be used to create or reload an ImageType. |
| Public method | [SetExternalResourceReference](0b401f0d-2333-2686-254c-14003c967314.htm) | Update the external resource reference to an image. |
| Public method | [SetPath(String)](3eeb55a9-ced3-165d-5a9e-d75a9d7f2f20.htm) | Update the path of the file that specifies the image to be used.  The provided string path must specify a local file. The path can be absolute or relative to the project's location. ImageType will respectively use an absolute or relative path. |
| Public method | [SetPath(String, Boolean)](9c707780-4777-d34b-adbc-3092b10b42bd.htm) | Update the path of the file that specifies the image to be used.  The provided string path must specify a local file. The path can be absolute or relative to the project's location.  Additionally, indicate whether the path used by ImageType should be absolute or relative. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](d6fccbef-3786-a1ae-cd60-0a54e9ea60e6.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [PageNumber](33b28f56-d107-868c-3554-85fe06c32397.htm) | The page in the file to be used for the image |
| Public property | [Path](322a4a54-839e-f1f4-68ad-7c6194d1c215.htm) | The path of the file that specifies the image to be used. |
| Public property | [Resolution](858dcd6b-5231-fb9b-b43a-7c1397c4265e.htm) | The Resolution of the image is expressed in dots-per-inch and hence determines the size of a pixel in the image. |
| Public property | [SourceType](1d275efe-88ad-da80-d321-b31884f1c369.htm) | Indicates whether the image type is a link or an import. |

# See Also

[ImageTypeOptions Class](981135c3-777b-df9b-747f-60a35b74e00e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)