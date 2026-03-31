[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TransactionGroup Members

---



|  |
| --- |
| [TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [TransactionGroup](f1113d30-4c36-7844-1537-aad7f095cea0.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [TransactionGroup(Document)](74cff3fa-9380-2c30-9fa9-b0e839a2c8e4.htm) | Constructs a transaction group object. |
| Public method | [TransactionGroup(Document, String)](bc63bb0d-fc22-9419-cec9-ea8c92b368b6.htm) | It constructs a transaction group object |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Assimilate](158471e4-5554-16ed-f9bf-f7499b86309c.htm) | Assimilates all inner transactions by merging them into a single undo item. |
| Public method | [Commit](11878443-43f2-63fb-a95d-baa1eeab776d.htm) | Commits the transaction group. |
| Public method | [Dispose](eb2b4351-d808-9232-fab8-d21aee6d705b.htm) | Releases all resources used by the  [TransactionGroup](f1113d30-4c36-7844-1537-aad7f095cea0.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetName](58789072-9fe1-a08d-7b3b-1c28239e6115.htm) | Returns the transaction group's name. It could be an empty string. |
| Public method | [GetStatus](80db1b02-e36c-1c4e-1788-fd92b0d20a1f.htm) | Gets the current status of the transaction group. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [HasEnded](e559d859-b429-f052-16ce-541e4ddb0227.htm) | Determines whether the transaction group has ended already. |
| Public method | [HasStarted](730a43e9-026e-2989-dc58-cef21cd81798.htm) | Determines whether the transaction has been started yet. |
| Public method | [RollBack](2efcf628-bb40-bf36-a2e4-eaeca4cca461.htm) | Rolls back the transaction group, which effectively undoes all transactions committed inside the group. |
| Public method | [SetName](6b009b31-5ee4-dc76-2c3e-b3867ffee33c.htm) | Sets the transaction group's name. |
| Public method | [Start](fff3e88e-358c-e6d0-d539-61517f53140c.htm) | Starts the transaction group |
| Public method | [Start(String)](5debe7ea-7131-58d1-c9bb-3286a8d5895d.htm) | Starts the transaction group with an assigned name. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsFailureHandlingForcedModal](2365a964-dd55-0727-9f5d-f54df40da118.htm) | Forces all transactions finished inside this group to use modal failure handling regardless of what failure handling options are set for those transactions. |
| Public property | [IsValidObject](34580d0f-a9ba-1981-8bc0-ae6144585c74.htm) | Specifies whether the .NET object represents a valid Revit entity. |

# See Also

[TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)