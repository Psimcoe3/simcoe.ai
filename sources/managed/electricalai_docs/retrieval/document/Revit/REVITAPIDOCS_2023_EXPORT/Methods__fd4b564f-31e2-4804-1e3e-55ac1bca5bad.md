[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProgressChangedEventArgs Members

---



|  |
| --- |
| [ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ProgressChangedEventArgs](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Cancel](bafd1603-f0db-4efb-e101-9fe0e3f33e85.htm) | Requests to cancel the progress bar's operation. |
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
| Public property | [Caption](1ea0706c-ed5c-91fb-5c01-85c3dec9cdf0.htm) | The text from the progress bar caption that describes the operation in progress |
| Public property | [IsValidObject](35c0066a-b3dc-9d37-c79e-c29f90713b2d.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)  .) |
| Public property | [LowerRange](fd02b552-e0f0-84a1-229f-0c9b6b1cc4f8.htm) | Lower part of progress bar range - always zero |
| Public property | [Position](3a48f343-428e-56f9-36c9-ee82cc732ef8.htm) | Progress bar position - value is always between zero and upperRange and is incremented by one with each event of stage "PositionChanged" |
| Public property | [Stage](3d8ca3f6-2e0d-c45a-c58d-40170ea037d9.htm) | The current stage of the progress bar |
| Public property | [UpperRange](2f7248a7-de59-7352-e8ed-38dfc386b5ab.htm) | Upper part of progress bar range - will be any non-zero number |

# See Also

[ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)