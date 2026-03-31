[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCImportOptions Members

---



|  |
| --- |
| [IFCImportOptions Class](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [IFCImportOptions](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [IFCImportOptions](303d5cc5-8885-e5ad-fd84-304abda7ee5b.htm) | Constructs a new IFCImportOptions using default settings. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](fc622f9f-c5df-7755-e519-71d663b2ae40.htm) | Releases all resources used by the  [IFCImportOptions](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetConversionData](e4cd397e-8e29-ca75-4a92-ab8efd557ea1.htm) | Get the data used in the creation of the associated Revit file for an IFC link operation, if it exists. |
| Public method | [GetExtraOptions](b47a34ec-ea49-7f3d-ce78-782222abf96e.htm) | Get the list of extra options to be passed into the importer. Each entry in the map is a pair of option name and value. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [SetExtraOptions](a2800b08-bb26-a9c7-0cdf-c995c9e2be63.htm) | Set the list of extra options to be passed into the importer. Each entry in the map is a pair of option name and value. Note that any value here will overwrite the other values in the IFCImportOptions, if it has the same name. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Action](070af608-cb1e-43d5-f3ca-6d53150f9dbb.htm) | The action of the import. |
| Public property | [AutocorrectOffAxisLines](7c134ff4-e2e3-c74e-e828-079963d773a8.htm) | Enable or disable correcting lines that are slight off-axis. |
| Public property | [AutoJoin](abf3e142-3f21-9161-e799-7a6b6e3c30b0.htm) | Enable or disable auto-join at the end of import. |
| Public property | [CreateLinkInstanceOnly](47219405-9a1f-3e60-1c1c-bc88586d487e.htm) | Determines whether to create a linked symbol element or not. |
| Public property | [ForceImport](f9fcc2e6-4e4e-94bd-2646-801f7f487612.htm) | Force the IFC file to be imported regardless of an existing corresponding Revit file. |
| Public property | [Intent](6200e560-88d8-d10d-0cf9-ceb18ca15f3f.htm) | The intent of the import. |
| Public property | [IsValidObject](a4e4a737-c53c-62e5-a9c2-c424f1f80951.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [RevitLinkFileName](34cbbeb3-4be9-42c9-bc0c-9e411c2d3184.htm) | The full path of the intermediate Revit file created during a previous link action. This is used during "Reload From" to determine the path to the previous generated Revit file. |

# See Also

[IFCImportOptions Class](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)