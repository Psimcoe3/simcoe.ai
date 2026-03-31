[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TaskDialogShowingEventArgs Members

---



|  |
| --- |
| [TaskDialogShowingEventArgs Class](96cc0900-708b-5a2c-8d07-b2596ec20700.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [TaskDialogShowingEventArgs](96cc0900-708b-5a2c-8d07-b2596ec20700.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Cancel](88fa78de-0fff-a85f-0de3-b631673e9e51.htm) | When the event is cancellable, may call the Cancel() method to cancel it. (Inherited from  [RevitAPIPreEventArgs](14097470-c9d9-0143-dc1b-b93a60a460e6.htm)  .) |
| Public method | [Dispose](697794d0-db4b-41ee-90a3-388296ffeefb.htm) | (Inherited from  [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)  .) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [IsCancelled](5627aeaa-9d9c-dcbe-b34f-db40f1c025be.htm) | Indicates whether the event is being cancelled. (Inherited from  [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)  .) |
| Public method | [OverrideResult](49ba2725-74c9-02b3-4321-eac1f2295bd3.htm) | Call this method to cause the Autodesk Revit dialog to be dismissed with the specified return value. (Inherited from  [DialogBoxShowingEventArgs](8b6b969f-45d2-5b90-ca6d-593348ddf8d4.htm)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Cancellable](a393138a-34b5-1724-aa69-92cef651482b.htm) | Indicates whether an event may be cancelled by an event delegate. (Inherited from  [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)  .) |
| Public property | [DialogId](7311c9d6-f223-f4c2-0b7a-197e42e5ee61.htm) | A unique string identifier for DialogBox and TaskDialog type dialogs in Revit. (Inherited from  [DialogBoxShowingEventArgs](8b6b969f-45d2-5b90-ca6d-593348ddf8d4.htm)  .) |
| Public property | [IsValidObject](35c0066a-b3dc-9d37-c79e-c29f90713b2d.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)  .) |
| Public property | [Message](235c3a07-198c-4705-4ace-437efd36a150.htm) | The message that has been displayed in the dialog box. |

# See Also

[TaskDialogShowingEventArgs Class](96cc0900-708b-5a2c-8d07-b2596ec20700.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)