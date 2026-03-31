[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyManager Members

---



|  |
| --- |
| [FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [FamilyManager](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddParameter(ExternalDefinition, BuiltInParameterGroup, Boolean)](bc46a62e-1b2d-d8ad-b90e-9ec7c64ae317.htm) | Add a new shared parameter to the family. |
| Public method | [AddParameter(ExternalDefinition, ForgeTypeId, Boolean)](bff507b1-caa3-bf4c-f7f1-c56cade391f8.htm) | Add a new shared parameter to the family. |
| Public method | [AddParameter(String, BuiltInParameterGroup, Category, Boolean)](d448dd99-5dd3-3828-5f72-461439c36485.htm) | Add a new family type parameter to control the type of a nested family within another family. |
| Public method | [AddParameter(String, ForgeTypeId, Category, Boolean)](8425ca9a-9db2-d06a-7540-bc8e686a7566.htm) | Add a new family type parameter to control the type of a nested family within another family. |
| Public method | [AddParameter(String, ForgeTypeId, ForgeTypeId, Boolean)](3ac89d60-4b71-694f-002f-125d2e6565fc.htm) | Add a new family parameter with a given name. |
| Public method | [AssociateElementParameterToFamilyParameter](a047ea58-0351-b419-d856-85ed23734ee8.htm) | Associates or disassociates the element parameter to an existing family parameter. |
| Public method | [CanElementParameterBeAssociated](ee0cd1df-2342-9e91-cf57-d7eb9d240b90.htm) | Indicates if this element parameter can be associated with a family parameter. |
| Public method | [DeleteCurrentType](9ba3e824-e354-943b-141c-89b5c5e8cea2.htm) | Remove the current family type. |
| Public method | [Dispose](7c03212a-b587-1c89-3912-efea0d2619c5.htm) | Causes the object to release immediately any resources it may be utilizing. (Inherited from  [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetAssociatedFamilyParameter](ada33bdc-f484-c4a6-3713-6946dabd5fcf.htm) | Gets the associated family parameter of an element parameter. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetParameter](9c22c68a-8fd5-850e-9aa8-cf7298ceebd0.htm) | Obtains the family parameter with the given built-in parameter identifier. |
| Public method | [GetParameters](86e30f63-4894-aed9-c6df-0074cdfa89a7.htm) | Gets the parameters associated to family types in order. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [IsParameterLockable](b0ab3d1e-01e7-dc91-373b-c14d396c1a3e.htm) | For Conceptual Mass and Curtain Panel families, indicate whether the specified parameter can be locked. |
| Public method | [IsParameterLocked](b2b1deb8-e2c0-8f48-7b03-368ec43746c5.htm) | For Conceptual Mass and Curtain Panel families, indicate whether the specified dimension-driving parameter is locked. |
| Public method | [IsUserAssignableParameterGroup(BuiltInParameterGroup)](2c81a719-de51-f897-7f7b-8960a502e1de.htm) | Checks if the given parameter group can be assigned to new parameters. |
| Public method | [IsUserAssignableParameterGroup(ForgeTypeId)](414a0359-4e22-26ed-c01c-f52a81dccf06.htm) | Checks if the given parameter group can be assigned to new parameters. |
| Public method | [MakeInstance](4223e8a2-4032-4fb9-b583-43f65dcba53d.htm) | Set the family parameter as an instance parameter. |
| Public method | [MakeNonReporting](c271cd56-7c6b-c1a1-c9fb-05bcd68604fc.htm) | Set the reporting family parameter as a regular/driving parameter. |
| Public method | [MakeReporting](a4ee2a95-1e8f-55e4-fb3b-3a926e7cf668.htm) | Set the family parameter as a reporting parameter. |
| Public method | [MakeType](96f7f8e3-b500-b220-6f08-388b63a0e543.htm) | Set the family parameter as a type parameter. |
| Public method | [NewType](b46e98b1-54a1-7e04-66b7-a35efe5bc3f8.htm) | Add a new family type with a given name and makes it be the current type. |
| Public method | [RemoveParameter](cb266197-b76e-66db-ea15-2cf14bcb4f85.htm) | Remove an existing family parameter from the family. |
| Public method | [RenameCurrentType](ddd98706-5a07-feac-4b1f-49d52471a8c8.htm) | Rename the current family type. |
| Public method | [RenameParameter](19e7d857-9243-95a0-726c-50b5b7482c3e.htm) | Rename a family parameter. |
| Public method | [ReorderParameters](f3e5375b-28d7-d6c6-ea49-bf6f6289fd9a.htm) | Reorders the family parameters by the specified parameters order. |
| Public method | [ReplaceParameter(FamilyParameter, ExternalDefinition, BuiltInParameterGroup, Boolean)](4cb000cc-37ba-11fb-59d2-6790cca209b0.htm) | Replace a family parameter with a shared parameter. |
| Public method | [ReplaceParameter(FamilyParameter, ExternalDefinition, ForgeTypeId, Boolean)](9ddbd75b-887d-397a-14aa-3e4052a2a2eb.htm) | Replace a family parameter with a shared parameter. |
| Public method | [ReplaceParameter(FamilyParameter, String, BuiltInParameterGroup, Boolean)](5eb146f4-968c-332e-b017-b9dd7b27274f.htm) | Replace a shared family parameter with a new non-shared family parameter. |
| Public method | [ReplaceParameter(FamilyParameter, String, ForgeTypeId, Boolean)](b276c350-b06f-69fe-c9e2-a9d938c3e973.htm) | Replace a shared family parameter with a new non-shared family parameter. |
| Public method | [Set(FamilyParameter, ElementId)](5004314a-c77f-e469-1e03-395f5e17de5a.htm) | Set the ElementId value of a family parameter of the current family type. |
| Public method | [Set(FamilyParameter, Double)](7fc40346-6188-66ff-4c00-bd4360e70c6f.htm) | Set the double value of a family parameter of the current family type. |
| Public method | [Set(FamilyParameter, Int32)](f6fab69e-4b4c-002c-ae57-d0120d841ad4.htm) | Set the integer value of a family parameter of the current family type. |
| Public method | [Set(FamilyParameter, String)](428551ba-9037-2e23-7f18-8747624d0ff2.htm) | Set the string value of a family parameter of the current family type. |
| Public method | [SetDescription](d00fb4a4-6e08-784d-3149-31e9b2d61a12.htm) | Set the description for an existing family parameter. The description will be used as tooltip in the Revit UI including in the properties palette. |
| Public method | [SetFormula](cdc3156c-0334-0bba-70af-1df78fb18b50.htm) | Set the formula of a family parameter. |
| Public method | [SetParameterLocked](9ee4b404-c9e9-7d52-389a-a5fa21eae2e5.htm) | For Conceptual Mass and Curtain Panel families, lock or unlock a dimension-driving parameter. |
| Public method | [SetValueString](a7178dc6-34d9-1dc3-d0fa-48454884498b.htm) | Set the string value of a family parameter of the current family type. |
| Public method | [SortParameters](329ceb60-b9b5-d603-a23c-e9fcfc9d2f62.htm) | Sorts the family parameters according to the desired sort order. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [CurrentType](3d37cd81-48ba-4011-82bc-dbb7ae14b270.htm) | The current family type. |
| Public property | [IsReadOnly](d516bcd2-a3fd-a578-58f6-f1add979bd07.htm) | Identifies if the object is read-only or modifiable. (Inherited from  [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)  .) |
| Public property | [Parameter Guid](11dc4a23-df9b-6574-3e4d-c4c03623856c.htm) | Obtains the parameter of this type with a given GUID for a shared parameter. |
| Public property | [Parameter String](13bf2342-3818-d75b-110c-062d034f2cbd.htm) | Obtains the parameter of this type with a given name. |
| Public property | [Parameter BuiltInParameter](58f07dc1-aa80-65d8-a7f7-d60b32366d11.htm) | Obtains the parameter of this type with a given parameter id. |
| Public property | [Parameter Definition](a34849d3-53a8-fe8d-c441-274480da38d2.htm) | Obtains the parameter of this type with a given definition. |
| Public property | [Parameters](bef4c199-44d9-63b9-80e7-1a6b20a1062a.htm) | All family parameters in this family. |
| Public property | [Types](048fbdd1-313f-209e-3046-25c8872bf04e.htm) | All family types in the family. |

# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)