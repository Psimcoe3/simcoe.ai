[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SynchronizeWithCentralOptions Members

---



|  |
| --- |
| [SynchronizeWithCentralOptions Class](96eaf3af-971d-da6d-a857-88d6e602ffd4.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [SynchronizeWithCentralOptions](96eaf3af-971d-da6d-a857-88d6e602ffd4.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [SynchronizeWithCentralOptions](cf9b4e29-c004-534f-51b8-56abda16c82b.htm) | Constructs a new instance of SynchronizeWithCentralOptions initialized with default options. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](96380c66-ab5c-bae2-9871-58d3d38100c5.htm) | Releases all resources used by the  [SynchronizeWithCentralOptions](96eaf3af-971d-da6d-a857-88d6e602ffd4.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetRelinquishOptions](445e3c8a-6a98-0c88-a5f7-7c38d0d57fec.htm) | Gets the options which govern whether or not to relinquish elements and workset types. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [SetRelinquishOptions](0ebff269-60c0-6907-b6a9-45cec4e0e447.htm) | Sets the options which govern whether or not to relinquish elements and workset types. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Comment](69f35c0d-2570-8f9d-9518-172b9a22f077.htm) | User description of changes made since the last Sync with Central. Empty by default. |
| Public property | [Compact](23e58fe5-72f4-5d13-1003-d35f8ad3b25f.htm) | Indicates whether Revit should compact the central model while synchronizing with central. This option reduces the size of the central model but many increase the time it takes to perform the save. False by default. |
| Public property | [IsValidObject](03ced8e5-beb5-1582-b43c-5a97b937578c.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [RelinquishBorrowedElements](7e9e417f-2290-7640-8142-56c452b64c13.htm) | Indicates whether Revit should relinquish borrowed elements after synchronizing with central. |
| Public property | [RelinquishFamilyWorksets](31e99e30-5a40-d2c8-f5e0-1c639b392beb.htm) | Indicates whether Revit should relinquish Family worksets after synchronizing with central. |
| Public property | [RelinquishProjectStandardWorksets](c4643179-2e12-dba9-45e2-ac45c4f2014d.htm) | Indicates whether Revit should relinquish Project Standard worksets after synchronizing with central. |
| Public property | [RelinquishUserCreatedWorksets](680601bc-19b8-2ff6-2b8a-75814650b464.htm) | Indicates whether Revit should relinquish user-created Standard worksets after synchronizing with central. |
| Public property | [RelinquishViewWorksets](38ead435-3f4a-993e-9095-e55be8a7e537.htm) | Indicates whether Revit should relinquish View worksets after synchronizing with central. |
| Public property | [SaveLocalAfter](636d5979-3eca-0425-2ef4-352452daeeaf.htm) | True means to save local after saving changes to central. True by default. Silently ignored if the model in the current session is central rather than local. |
| Public property | [SaveLocalBefore](08acd3c1-af30-9cf5-55cb-c09f1df64c20.htm) | True means to save local before the first reload latest if there are changes not yet saved to local. True by default. Silently ignored if the model in the current session is central rather than local. |
| Public property | [SaveLocalFile](02d064b9-a637-b7d3-0f86-3821bcbb472d.htm) | Indicates whether Revit will save the local file at least once while synchronizing with central. |

# See Also

[SynchronizeWithCentralOptions Class](96eaf3af-971d-da6d-a857-88d6e602ffd4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)