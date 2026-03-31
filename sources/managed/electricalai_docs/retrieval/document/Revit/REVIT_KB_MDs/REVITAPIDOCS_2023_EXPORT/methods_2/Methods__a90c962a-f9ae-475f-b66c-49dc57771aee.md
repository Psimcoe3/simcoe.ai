[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Schema Members

---



|  |
| --- |
| [Schema Class](9817e7db-8367-ea4e-1769-0488f3faa37f.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [Schema](9817e7db-8367-ea4e-1769-0488f3faa37f.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](4b3e5a04-9723-1121-3be5-fd0e8bab390c.htm) | Releases all resources used by the  [Schema](9817e7db-8367-ea4e-1769-0488f3faa37f.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetField](e706cd01-bc50-9a3c-68c1-9bd4507c85e0.htm) | Gets a Field of a given name from the Schema. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [ListFields](c1f24aca-c2a6-4a16-0440-2bd8296aa04e.htm) | The complete list of fields in the Schema, sorted by name. |
| Public method Static member | [ListSchemas](0f49289a-ca96-089e-a1c2-6f5bf80e29eb.htm) | Lists all schemas in memory. |
| Public method Static member | [Lookup](a83707a4-8924-cf77-9d8b-71ce10127f24.htm) | Finds the Schema corresponding to the GUID in memory. |
| Public method | [ReadAccessGranted](e691bb52-66a1-96fd-274d-8ae3f30e5c0c.htm) | Checks whether Entities of this Schema may be retrieved by the current add-in. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |
| Public method | [WriteAccessGranted](3f089f69-3a06-cff9-dbc7-a2ed58192f85.htm) | Checks whether Entities of this Schema may be stored by the current add-in. |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ApplicationGUID](42d848d5-5d83-23ff-f8af-ca48581c7acd.htm) | The GUID of the application or add-in that may access entities of this Schema under the Application access level. |
| Public property | [Documentation](a1d996c8-1ccc-58d1-d708-bd44da7457e6.htm) | The overall description of the Schema. |
| Public property | [GUID](a2aa971a-5270-c35d-74c1-ee8cbec0261b.htm) | The identifier of the Schema. Setter made unavailable, because it would violate set-correctness |
| Public property | [IsValidObject](c4f8e660-70aa-7951-0b7a-6d581b798676.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [ReadAccessLevel](784a6bed-58cb-d3e2-84ea-971863f1ae37.htm) | Read access level of the schema. |
| Public property | [SchemaName](50662a69-4395-40c4-8d10-cda8b728cf8e.htm) | The user-friendly name of the Schema. |
| Public property | [VendorId](4c96e65d-07cc-4e85-a176-b2b8c33ba6b2.htm) | The id of the third-party vendor that may access entities of this Schema under the Vendor access level. |
| Public property | [WriteAccessLevel](d03286f0-aa98-d5c3-83e8-fffb245321e5.htm) | Write access level of the schema. |

# See Also

[Schema Class](9817e7db-8367-ea4e-1769-0488f3faa37f.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)