[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalResourceBrowserData Members

---



|  |
| --- |
| [ExternalResourceBrowserData Class](94a46450-5467-45f2-0228-4c9f9821b4c9.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ExternalResourceBrowserData](94a46450-5467-45f2-0228-4c9f9821b4c9.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ExternalResourceBrowserData](eabd8602-8d03-9d9f-455e-bda1d0667f18.htm) | Constructs a new ExternalResourceBrowserData using the given document(optional), server id, folder path and match options. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddResource(String)](94069c9b-d720-6826-bf13-7663e73b08cb.htm) | Adds an external resource to the folder path by supplying the resource name. |
| Public method | [AddResource(String, IDictionary String, String )](44f19e8a-789f-1181-3ec1-def94c1e1a3d.htm) | Adds an external resource to the folder path by supplying the resource name and reference information. |
| Public method | [AddResource(String, String)](62f87583-84e5-1481-35a6-f8610bc4f448.htm) | Adds an external resource to the folder path by supplying the resource name and version. |
| Public method | [AddResource(String, String, IDictionary String, String )](60ea723b-3c92-8408-26f6-08788f29bc25.htm) | Adds an external resource to the folder path by supplying the resource name, version and reference information. |
| Public method | [AddSubFolder(String)](b4156741-2375-50f9-1c33-7efaa42b8b06.htm) | Adds a subfolder to the folder path with the given name. |
| Public method | [AddSubFolder(String, String)](6a60f937-fa5f-55e7-7b16-cc009283990f.htm) | Adds a subfolder to the folder path with the given name and icon type. |
| Public method | [CallingDocumentHasModelPath](7c19b745-83f6-24c9-43e9-0a160eab123b.htm) | Indicates whether the document requesting the external resource browser data has a defined ModelPath. |
| Public method | [Dispose](204149be-eb02-e742-9a6f-5f795cb90afe.htm) | Releases all resources used by the  [ExternalResourceBrowserData](94a46450-5467-45f2-0228-4c9f9821b4c9.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetCallingDocumentModelPath](7a877029-3b5a-3de8-9c35-fe38fa48c82e.htm) | Returns a copy of the ModelPath of the document that is requesting the external resource browser data. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetMatchOptions](18e6e337-9e0e-3c4f-b021-59003c5b4883.htm) | Gets the match options used to filter external resources. |
| Public method | [GetResources](616cff02-a764-70ad-251b-c0b494145c74.htm) | Gets the external resources under the folder path of the browser data. |
| Public method | [GetSubFoldersData](68ac11a5-1134-4944-3d57-e002cd376bec.htm) | Gets the subfolders data under the folder path of the browser data. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [IsValidFolderName](b8e9265b-0a7d-d7fd-8588-c49ef5ab5bb2.htm) | Checks whether the folder name is valid. |
| Public method | [IsValidResourceName](d9deaa7c-6b96-6fad-6f16-426df57e09e7.htm) | Checks whether the resource name is valid. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [FolderPath](3a4e2d9e-41a8-380e-46b1-ab000c4b6a60.htm) | The current folder path to which the new resources and subfolder belong. |
| Public property | [IsValidObject](4b2f627f-7394-baf8-cf33-facd7e6fbe8b.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [ServerId](de683377-f59a-80ee-55e0-cc9be601eaba.htm) | The Id of IExternalResourceServer which handles the external resource load. |

# See Also

[ExternalResourceBrowserData Class](94a46450-5467-45f2-0228-4c9f9821b4c9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)