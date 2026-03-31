[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyLoadedIntoDocumentEventArgs Members

---



|  |
| --- |
| [FamilyLoadedIntoDocumentEventArgs Class](a63d4c02-fc75-445b-edf5-d9068465fb1a.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [FamilyLoadedIntoDocumentEventArgs](a63d4c02-fc75-445b-edf5-d9068465fb1a.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](697794d0-db4b-41ee-90a3-388296ffeefb.htm) | (Inherited from  [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)  .) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [IsCancelled](5627aeaa-9d9c-dcbe-b34f-db40f1c025be.htm) | Indicates whether the event is being cancelled. (Inherited from  [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Cancellable](a393138a-34b5-1724-aa69-92cef651482b.htm) | Indicates whether an event may be cancelled by an event delegate. (Inherited from  [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)  .) |
| Public property | [Document](b0a5235e-b2b3-0a29-799c-2ef535a51909.htm) | The document associated with the event. (Inherited from  [RevitAPIPostDocEventArgs](7d3fba7a-5efb-6a4c-a49c-16c25f972830.htm)  .) |
| Public property | [FamilyName](8f15d3b2-1c86-fcd1-6935-73d1af72be21.htm) | The file name of the family that is loaded into the document. |
| Public property | [FamilyPath](4fc97a8e-a29f-8cdf-b567-cc8e95139742.htm) | The file path of the family that is loaded into the document. |
| Public property | [IsValidObject](35c0066a-b3dc-9d37-c79e-c29f90713b2d.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)  .) |
| Public property | [NewFamilyId](98344b60-1514-1cc0-dbd2-0a8032d902d3.htm) | The newly loaded family id. |
| Public property | [OriginalFamilyId](2ec3e15e-4496-4c6c-4fb5-3d056cd28680.htm) | The original family id that is overridden by the newly loaded family. |
| Public property | [Status](01c1c4b6-fc91-0651-3312-4d988073433a.htm) | Indicates whether the action associated with this event succeeded, failed, or was cancelled (by an API event handler). (Inherited from  [RevitAPIPostEventArgs](93554f52-0145-3454-5697-3f1015e46434.htm)  .) |

# See Also

[FamilyLoadedIntoDocumentEventArgs Class](a63d4c02-fc75-445b-edf5-d9068465fb1a.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)