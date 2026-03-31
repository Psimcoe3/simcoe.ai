[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SchemaBuilder Members

---



|  |
| --- |
| [SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [SchemaBuilder](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [SchemaBuilder](e2dd3c2d-f72c-a393-a802-2b7d3a595482.htm) | Constructs a new SchemaBuilder where the resulting Schema will use the input GUID. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AcceptableName](0ac1f229-14e3-6039-22f1-1d6b40a000de.htm) | Checks whether a string is an acceptable name for a Schema or a Field. |
| Public method | [AddArrayField](f20f39f5-152c-98e9-32b7-b8c3bd575e4b.htm) | Creates a field containing an array of values in the Schema, with given name and type of contained values. |
| Public method | [AddMapField](ed30389b-a527-c867-3903-ce033f55552c.htm) | Creates a field containing an ordered key-value map in the Schema, with given name and type of contained values. |
| Public method | [AddSimpleField](5de0ea30-a58e-4db2-373c-05222a139465.htm) | Creates a field containing a single value in the Schema, with given name and type. |
| Public method | [Dispose](29acd183-7869-e155-1842-6a32ab108fd0.htm) | Releases all resources used by the  [SchemaBuilder](e74f9357-cc3c-558e-73b8-38ce6d247869.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [Finish](399ce458-d43f-57a1-52f4-f862b243edec.htm) | Registers and returns the created Schema object. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method Static member | [GUIDIsValid](8b959aef-0601-e3e0-38ed-5cd98323fa50.htm) | Checks whether the supplied GUID value is valid. |
| Public method | [Ready](d839c136-a715-3de4-6b69-22cd65d39f81.htm) | Checks whether the builder may be used. |
| Public method | [SetApplicationGUID](c94ecbf6-126b-60e6-cff1-42fb93e85c81.htm) | Sets the GUID of the application or add-in that may access entities of this Schema under the Application acess level. |
| Public method | [SetDocumentation](e712e079-d5fe-fcbb-ab78-90e8608a82a4.htm) | Sets the documentation string for the Schema. |
| Public method | [SetReadAccessLevel](48aa900b-69fa-df08-132b-5046447e9dc1.htm) | Sets top level read access (for entities) |
| Public method | [SetSchemaName](f53b3048-99f8-0dbc-f623-f997ab673932.htm) | Sets the name of the Schema. |
| Public method | [SetVendorId](4b94c68b-5f9c-f798-2619-0bd88a856f37.htm) | Sets the ID of the third-party vendor that may access entities of this Schema under the Vendor acess level, and to generally identify the owner of this Schema. |
| Public method | [SetWriteAccessLevel](5d9b9a09-dd20-a79f-4e43-1f0365ed75be.htm) | Sets top level write access (for entities) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method Static member | [VendorIdIsValid](66fc864b-ed7a-c9f9-7eae-209a9aa5c1b6.htm) | Checks whether the given vendor ID string is valid. A valid vendor ID string: 1. Has a length of at least 4 characters and no more than 253 characters, and 2. Contains only letters, digits, or any of the following special characters: ! " # & \ ( ) + , . - : ; < = > ? \_ ` | ~ |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](eb116832-fc35-09d3-b76f-8276e8038154.htm) | Specifies whether the .NET object represents a valid Revit entity. |

# See Also

[SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)