[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BasicFileInfo Members

---



|  |
| --- |
| [BasicFileInfo Class](475edc09-cee7-6ff1-a0fa-4e427a56262a.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [BasicFileInfo](475edc09-cee7-6ff1-a0fa-4e427a56262a.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](ea844cc5-ff80-ffc9-2740-1482aca86418.htm) | Releases all resources used by the  [BasicFileInfo](475edc09-cee7-6ff1-a0fa-4e427a56262a.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method Static member | [Extract](05800394-0e43-45f2-6c89-0db484d6a98c.htm) | Returns an instance of BasicFileInfo filled with basic information about a Revit file located at the given file-path |
| Public method | [GetDocumentVersion](117de15c-6642-4216-cd85-8c31eb42cbca.htm) | Gets the DocumentVersion for the file. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AllLocalChangesSavedToCentral](621f9654-180b-4391-9ebc-f1894b74b3b9.htm) | Are all local changes saved to the central file? |
| Public property | [CentralPath](7b646d50-585e-1c52-54f5-5b2eddc546a9.htm) | Returns the central model path. |
| Public property | [Format](b0762e23-5c49-42bf-b3cc-d0b1194543c9.htm) | The file format indicator (currently, the major release version such as "2019") used for saving the file. |
| Public property | [IsCentral](0f412eca-700a-7e9e-570e-117f94c87d29.htm) | Checks if the file is workshared and Central. |
| Public property | [IsCreatedLocal](edb87333-ccef-5cc3-9965-074b69722203.htm) | Checks if the file is local and created by RevitServerTool.exe. |
| Public property | [IsInProgress](d756cb3e-b7b6-b51a-1f0e-90c3cd862632.htm) | Checks if the file is workshared and is in process of becoming Central. |
| Public property | [IsLocal](10c8c9c8-b938-981b-c90e-ceae3de832c8.htm) | Checks if the file is workshared and Local. |
| Public property | [IsSavedInCurrentVersion](d68e377e-690c-0893-f505-003bf3634de5.htm) | Checks if the file is saved in the current version. |
| Public property | [IsSavedInLaterVersion](27a0583a-c2e4-b198-cf60-168f51c07b13.htm) | Checks if the file is saved in a later version of Revit than the running Revit. |
| Public property | [IsValidObject](36688ac8-26a4-51d3-4cac-314e95fcab2d.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [IsWorkshared](7ba0cb4d-5498-567e-e523-5c9229303f9d.htm) | Checks if the file is workshared. |
| Public property | [LanguageWhenSaved](2ea1f11e-1535-89c1-52c5-ee729cbe9b6e.htm) | Return the language active for the last save |
| Public property | [LatestCentralEpisodeGUID](698c403a-f118-3195-249f-7bd20aa18e59.htm) | This is the central model's episode GUID corresponding to the last reload latest done for this model. |
| Public property | [LatestCentralVersion](8f508901-37a3-3f77-1cea-cfdc1a05b37c.htm) | This is the central model's version number corresponding to the last reload latest done for this model. |
| Public property | [Username](896036da-c37a-ce47-82dc-9d26ab722897.htm) | Returns the username. |

# See Also

[BasicFileInfo Class](475edc09-cee7-6ff1-a0fa-4e427a56262a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)