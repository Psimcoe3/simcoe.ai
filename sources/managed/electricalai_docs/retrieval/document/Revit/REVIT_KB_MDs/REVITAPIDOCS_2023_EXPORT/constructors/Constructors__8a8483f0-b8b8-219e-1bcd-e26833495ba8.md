[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NavisworksExportOptions Members

---



|  |
| --- |
| [NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [NavisworksExportOptions](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [NavisworksExportOptions](49a74067-e7da-903b-83ea-fe51274cbd32.htm) | Create an instance of Navisworks Export Options set with default values. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](6f8c3241-e216-a3df-54da-f80679a66803.htm) | Releases all resources used by the  [NavisworksExportOptions](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetSelectedElementIds](071adb98-310b-3b6a-acc2-e98d9c94771f.htm) | Returns the element ids of the elements to export. Empty by default. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [SetSelectedElementIds](cb60be0c-ceb2-fc2d-97c2-84dc79d6cc72.htm) | Sets the element ids of the elements to export. Used only when ExportScope = SelectedElements. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ConvertElementProperties](22442a29-5fa9-f928-e661-e4e75f83a9c9.htm) | True to convert element properties, false otherwise. Default value is false. |
| Public property | [ConvertLights](4ed38415-7618-db70-8b74-148e39468a79.htm) | True to convert lights, false otherwise. Default value is false. |
| Public property | [ConvertLinkedCADFormats](b0b3caac-3ef7-0408-9ebd-929f51587a53.htm) | True to convert linked CAD formats, false otherwise. Default value is true. |
| Public property | [Coordinates](41d7e690-a9b4-2ff0-71c5-98d7f4877cfb.htm) | Options which specifies the coordinates of Navisworks Exporter. Default value is Shared. |
| Public property | [DivideFileIntoLevels](55cd45cc-496e-70ad-0bef-636182dcd3e8.htm) | True to divide file into levels, false otherwise. Default value is true. |
| Public property | [ExportElementIds](164586b6-5c86-f522-9b62-6999e8c01a16.htm) | True to export Revit element ids, false to skip these values. Default value is true. |
| Public property | [ExportLinks](a7b76450-1c85-6a58-6ffd-1884e28c451f.htm) | True to export Revit links found in the main model, false to skip links. Default value is false. |
| Public property | [ExportParts](9873bff8-39a6-a972-5a28-b955f8eae46d.htm) | True to export Revit part elements, false to export the original parent elements. Default value is false. |
| Public property | [ExportRoomAsAttribute](eef60c23-5cd6-8d69-d75e-54b8c8d24674.htm) | True to export data for each room converts into a single shared room attribute, false otherwise. Default value is true. |
| Public property | [ExportRoomGeometry](1f40544f-1f6a-24d6-6256-8f9f61e6114a.htm) | True to export Revit room geometry, false otherwise. Default value is true. |
| Public property | [ExportScope](3a7ffc07-bd02-39c2-1846-865973db8d7f.htm) | Options which specifies the export scope of Navisworks Exporter. Default value is Model. |
| Public property | [ExportUrls](45656557-82e9-c4a3-a2bc-1924e29cd365.htm) | True to export URL parameters, false otherwise. Default value is true. |
| Public property | [FacetingFactor](a2b7109c-b57e-a0c1-7b22-578214fe0a24.htm) | Faceting factor. Default value is 1.0. |
| Public property | [FindMissingMaterials](100be585-d3c7-344c-b407-8a240e08e233.htm) | True if the file exporter looks for a match for the materials missing from the export, false otherwise. Default value is true. |
| Public property | [IsValidObject](81d64aca-5b15-956f-fd76-5f3ae00084fe.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [Parameters](7bc7e2e4-535a-8975-636f-a3af2ba87d55.htm) | Options which specifies the parameter conversion of Navisworks Exporter. Default value is All. |
| Public property | [ViewId](afec98fb-dba1-2413-baa4-6889550d8087.htm) | The element id of the view to export. InvalidElementId by default. Used only when ExportScope = View. |

# See Also

[NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)