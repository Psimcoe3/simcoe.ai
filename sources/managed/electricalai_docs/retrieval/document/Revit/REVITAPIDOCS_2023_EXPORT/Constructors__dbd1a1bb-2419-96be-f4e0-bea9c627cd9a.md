[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalResourceReference Members

---



|  |
| --- |
| [ExternalResourceReference Class](ffad9c15-8fc9-fbfd-f328-101533f4cf74.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ExternalResourceReference(ExternalResourceReference)](23eafbee-60c6-6c26-e4e1-5ed224d3bd08.htm) | Creates a new ExternalResourceReference from the given ExternalResourceReference. |
| Public method | [ExternalResourceReference(Guid, IDictionary String, String , String, String)](583b476f-68a7-2671-d5f6-0b38834bb39a.htm) | Creates a new ExternalResourceReference from the given data. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method Static member | [CreateLocalResource](457745f0-5346-77ed-444b-554295ebb14b.htm) | Creates an ExternalResourceReference representing a local file managed by Revit's built-in server. |
| Public method | [Dispose](d550b72c-00fd-18e9-c345-721f08a67c4c.htm) | Releases all resources used by the  [ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetReferenceInformation](f02de1b9-6f2b-3c93-f7b1-8db6fa2476fb.htm) | Returns a copy of an object containing previously-stored reference or lookup information about the specific resource provided by the server. |
| Public method | [GetResourceShortDisplayName](f2573abd-b662-1c0c-0005-3bcee6649877.htm) | Gets the short display name of the external resource. |
| Public method | [GetResourceVersionStatus](deda452b-a0de-4431-450e-f2299c81d6d7.htm) | Checks whether this ExternalResourceReference corresponds to the current version of the resource. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [HasValidDisplayPath](a79b2db7-2ef5-fd11-71e2-ecfc84f3acc5.htm) | Checks whether this external Resource has a valid display path. |
| Public method | [IsValidReference](7df2f669-5190-1777-f5d3-6da110240711.htm) | Checks whether the reference is in a valid format. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [InSessionPath](8f8d1ee6-26e4-fbad-b000-709cdc6df801.htm) | The path stores the full display path which includes the server name plus the path provided by ExternalResourceServer.  The path that Revit will present for user recognizing and browsing to this resource during one session of Revit.  This property allows ExternalResourceServers to handle cases where the path to a resource may vary between Revit sessions. For example, if this ExternalResourceReference refers to a resource in a folder, this property can be used to store the current path of the resource. If the resource is moved to another folder later, the ExternalResourceServer could calculate the correct path for the resource from resource identification information when it is loaded and store it in this property, so that it will work correctly even if the rvt file is opened in a different location.  Do not rely on this path to look up an ExternalResourceReference, as the path is neither unique nor stable. It isn't unique because multiple servers might use the same server name and display name format. It isn't stable because some servers allow renaming, and because a server might change its name at some point. |
| Public property | [IsValidObject](19caed9b-7603-1775-a6e4-ab0c148c0f2c.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [ServerId](1f2b2899-334f-b018-7e5a-6c3e17e910ec.htm) | The id of the server that Revit is expecting to provide the external resource. |
| Public property | [Version](04796691-0778-07c2-9b90-ebabeabcb1dc.htm) | The version of the external data that was most recently loaded in Revit. |

# See Also

[ExternalResourceReference Class](ffad9c15-8fc9-fbfd-f328-101533f4cf74.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)