[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UpdaterData Members

---



|  |
| --- |
| [UpdaterData Class](58751d04-6f56-0346-e7ba-f21e61a459be.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [UpdaterData](58751d04-6f56-0346-e7ba-f21e61a459be.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](6ad46f9b-e128-d03a-c017-d5ed70d4438a.htm) | Releases all resources used by the  [UpdaterData](58751d04-6f56-0346-e7ba-f21e61a459be.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetAddedElementIds](b9676f82-ebc4-79f8-160e-4d3c4c1823a2.htm) | Returns set of elements newly added to the document. This set is mutually exclusive of elements returned by getDeletedElementIds() and getModifiedElementIds(). |
| Public method | [GetDeletedElementIds](d19575f3-a6cb-c532-78a2-2b513378af4a.htm) | Returns set of elements that were deleted from the document. This set is mutually exclusive of elements returned by getAddedElementIds() and getModifiedElementIds(). |
| Public method | [GetDocument](cb58fbb1-e923-b2f3-8b74-9aac45ad2d0f.htm) | Returns document associated with this UpdaterData |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetModifiedElementIds](f06a0804-5756-47e7-3dc3-bcc828e5adaf.htm) | Returns set of elements that were modified. This set is mutually exclusive of elements returned by getAddedElementIds() and getDeletedElementIds(). |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [IsChangeTriggered](c5dcda11-ce70-52d3-f415-60dc4c2d88a2.htm) | Allows updater to check if specific change has happened to an element. Compares input type to the types that caused Updater::execute() to be triggered. If input type was not registered as a trigger for the associated Updater, this method will always return false for that ChangeType. For example, if the only trigger registered for UpdaterX is ChangeTypeAny for Element A, then passing in ChangeTypeGeometry will return false even if the geometry of A changed because the registered trigger was ChangeTypeAny. However, passing in ChangeTypeAny will return true. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](d31d4b45-19e4-64c0-875b-f0bfd664320b.htm) | Specifies whether the .NET object represents a valid Revit entity. |

# See Also

[UpdaterData Class](58751d04-6f56-0346-e7ba-f21e61a459be.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)