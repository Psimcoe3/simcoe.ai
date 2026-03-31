[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentVersion Members

---



|  |
| --- |
| [DocumentVersion Class](3574fa56-016e-b146-1499-b3b1c9129705.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [DocumentVersion](3574fa56-016e-b146-1499-b3b1c9129705.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](83473a77-badb-5ead-efc5-768ba88b092f.htm) | Releases all resources used by the  [DocumentVersion](3574fa56-016e-b146-1499-b3b1c9129705.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [IsEqual](8464cbda-4d08-cab7-1773-f3cbf73ab584.htm) | Checks whether two DocumentVersions are identical. They are identical if both the GUID and number of saves are equal. If two DocumentVersions are identical, they come from the same document, with the same set of changes. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](37073a30-9b18-1ac8-5c12-5d3a60b86b71.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [NumberOfSaves](27570649-19b7-6906-f25a-b6182bb02e03.htm) | The number of times the document has been saved. The save number and GUID are both necessary to uniquely identify a document version. |
| Public property | [VersionGUID](5c246fe4-cefa-37da-1bb1-1aa2e39b3c60.htm) | The GUID portion of the DocumentVersion. The GUID is updated when changes are made to the document, but may not update with every change to the document. The GUID and save number are both necessary to uniquely identify a document version. |

# See Also

[DocumentVersion Class](3574fa56-016e-b146-1499-b3b1c9129705.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)