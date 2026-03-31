[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalDefinitionCreationOptions Members

---



|  |
| --- |
| [ExternalDefinitionCreationOptions Class](1cd9e425-23a3-04f8-c130-4d4a799abd13.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ExternalDefinitionCreationOptions](1cd9e425-23a3-04f8-c130-4d4a799abd13.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ExternalDefinitionCreationOptions](449e1cdb-ae48-6474-4da5-979c14b408f8.htm) | Constructs the options using a specified name and type. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](2430f321-c208-95fd-05d1-abe28f9d2858.htm) | Releases all resources used by the  [ExternalDefinitionCreationOptions](1cd9e425-23a3-04f8-c130-4d4a799abd13.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetDataType](1c61fba2-6eaf-a1ba-44f9-38ca6b29105f.htm) | Gets the identifier describing the parameter's data type. The identifier may belong to either a spec or a category. If it is a category, the parameter is a Family Type parameter of that category. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [SetDataType](2996abcb-0293-a469-6669-58fd39084594.htm) | Sets the parameter's data type. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Description](6872b1db-5f9e-72bb-b66f-b9c20f7cc597.htm) | The description of the parameter definition to be created. The description will be used as tooltip in the Revit UI including in the properties palette. The default is an empty string. |
| Public property | [GUID](c86d0033-8200-15ee-070c-d0a606ed3b2a.htm) | The GUID to use for this parameter definition. If not explicitly set, a random GUID is used. |
| Public property | [HideWhenNoValue](2a3a90d6-cf4b-ae88-b587-612dc96c0bc2.htm) | This property indicates whether this parameter should be hidden from the properties palette when it doesn't have a value. |
| Public property | [IsValidObject](6ae1426b-0034-4ad7-e380-b33493c5ca19.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [Name](e53f799e-fd7b-04b3-1a01-767896d6f89f.htm) | The name of the parameter definition to be created. |
| Public property | [UserModifiable](a4063402-872a-294c-184c-f445c195b91d.htm) | This property indicates whether this parameter can be modified by UI user or not. |
| Public property | [Visible](139a89a6-9544-4f29-a510-75ddf1367827.htm) | True if the parameter is visible to the user, false if it is hidden and accessible only via the API. The default is true. |

# See Also

[ExternalDefinitionCreationOptions Class](1cd9e425-23a3-04f8-c130-4d4a799abd13.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)