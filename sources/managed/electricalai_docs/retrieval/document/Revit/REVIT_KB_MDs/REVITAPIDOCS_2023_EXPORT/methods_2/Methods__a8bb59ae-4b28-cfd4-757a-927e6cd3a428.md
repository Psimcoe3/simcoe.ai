[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SingleServerService Members

---



|  |
| --- |
| [SingleServerService Class](8491691e-2a26-684e-f43c-e8e0095fd129.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [SingleServerService](8491691e-2a26-684e-f43c-e8e0095fd129.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddServer](6e60c7f3-83f3-dca5-745c-efd995421369.htm) | Registers a server with its service. (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public method | [Dispose](111746bc-4ade-6ef5-bff8-63f14d564166.htm) | (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetActiveServerId](3a297e1f-c338-a53c-24b2-d63ac4c4b844.htm) | Returns the Id of the currently active application-level server of the service. |
| Public method | [GetActiveServerId(Document)](db079180-d2a0-dd63-999c-92b995407bbb.htm) | Returns the Id of the server currently associated with the given document for the service. |
| Public method | [GetDefaultServerId](f348cd43-7480-2799-12ed-9d6dbc2b47b7.htm) | Returns the Id of the default server if one was assigned to the service. (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetOptions](492cc7a7-9493-732e-a6a7-fd00b3b85773.htm) | A copy of the options the service was registered with. (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public method | [GetPublicAccessKey](d40f5730-6deb-2b5c-1d42-b5abfbc2a625.htm) | Access key to use to execute a service. (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public method | [GetRegisteredServerIds](230b50ac-8db7-cf62-2502-3cb0fd217b35.htm) | Returns Ids of all servers registered for the service. (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public method | [GetServer](839e6c3d-1f70-4668-781f-823baf005ff5.htm) | Returns the instance that provides implementation for a registered server. (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [IsRegisteredServerId](24077646-e04a-cd18-c9e9-0bc1f7cfbcba.htm) | Checks if the Id represents a valid server that has been registered for the service. (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public method | [RemoveServer](8659a6ce-c473-987a-beea-388f64c5f0f3.htm) | Removes/unregisters a server from the service. (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public method | [SetActiveServer(Guid)](8d559fcf-ab8b-8104-97a9-460897113bba.htm) | Set an active server applicable application-wide for the service. |
| Public method | [SetActiveServer(Guid, Document)](cd04f63b-9c63-2ea2-d69e-c9fc4bb13dd0.htm) | Change the active server for a specific document. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [UnsetActiveServer](58a704c0-d372-3ab1-60af-041575e8ddd4.htm) | Unset the active server for the particular document. |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Description](d0fd2d4b-9b05-7c57-5918-81ab3140ad96.htm) | The description for the service (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public property | [IsSerializable](11302e75-b2d9-3281-c79d-aa0bf2423588.htm) | Indicates whether executions of the service requires serialization in documents or not. (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public property | [IsValidObject](bc2460fd-30a2-aba0-5e81-ceaa65fc2634.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public property | [Name](dd73f984-ee0e-6e97-241f-53e4a62915e1.htm) | The name of the service (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public property | [NumberOfServers](e78d2848-05b8-2d85-82c8-6f3450ff2c46.htm) | Indicates the number of servers currently registered with the service. (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public property | [ServiceId](a5988799-0b50-7b30-797d-ed7ef569287c.htm) | The Id of the service (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |
| Public property | [VendorId](68781c7a-2932-eeb1-f483-e58fccec7c68.htm) | The vendor who provided the service (Inherited from  [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)  .) |

# See Also

[SingleServerService Class](8491691e-2a26-684e-f43c-e8e0095fd129.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)