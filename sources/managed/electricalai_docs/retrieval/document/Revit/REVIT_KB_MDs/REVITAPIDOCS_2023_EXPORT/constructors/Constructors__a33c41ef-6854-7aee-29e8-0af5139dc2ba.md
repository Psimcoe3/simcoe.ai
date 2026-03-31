[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DGNExportOptions Members

---



|  |
| --- |
| [DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [DGNExportOptions](deca8dc2-439f-9567-9c60-70961b3f7c14.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [DGNExportOptions](0997299e-6bc6-21e4-46b0-95a60648421e.htm) | Constructs a new instance of DGNExportOptions with default values of all properties. |
| Public method | [DGNExportOptions(DGNExportOptions)](b83bcfca-cc71-ea34-d243-6d596f4d8128.htm) | Constructs a new instance of DGNExportOptions as a copy of the export options. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](b4c35f2c-100e-c009-ceae-c01ad46f3db8.htm) | (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetExportFontTable](6dc659b4-4131-c1bf-e418-4afc551095d0.htm) | Gets font table. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [GetExportLayerTable](1ce6b604-0b45-f05f-863e-952b85e5a862.htm) | Gets the layer table. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [GetExportLinetypeTable](eba17284-95da-cea8-6b24-4e99bf196629.htm) | Gets a copy of the line type table. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [GetExportLineweightTable](4be0abc7-0033-3f99-52c3-2e407cbd8fa0.htm) | Gets a copy of the line weight table. |
| Public method | [GetExportPatternTable](6f852987-50c6-e44a-398a-b23a01a1a0a5.htm) | Gets a copy of the pattern table. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method Static member | [GetPredefinedOptions](3befd44a-4aee-e83c-369c-4beeebebaef5.htm) | Returns an instance DGNExportOptions containing settings from a predefined export setup. |
| Public method Static member | [GetPredefinedSetupNames](bb5a7586-7d82-6a29-4fad-61ff0ae07ecf.htm) | Returns a list of names of predefined setups of DGN export options. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [SetExportFontTable](86d6662a-fc5b-0027-2167-0f1f70efc923.htm) | Sets font table to option. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [SetExportLayerTable](9d1bb366-8472-4141-945b-47a6b02fe1e7.htm) | Sets layer table back to option (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [SetExportLinetypeTable](7e4e09ba-d012-7ad9-762e-a0eb732b2178.htm) | Sets the line type table to use during export. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [SetExportLineweightTable](fce36964-2004-fb85-dfc3-84d49cd42ffa.htm) | Sets the line weight table to use during export. |
| Public method | [SetExportPatternTable](8050ce21-d4b7-4c46-6fe6-8a065b8a2e36.htm) | Sets the pattern table to use during export. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Colors](29f6fbf4-0651-a3d6-7ee6-86297335b03d.htm) | Export color mode. Default value is ExportColorMode.IndexColors. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [FileVersion](af039e20-22e3-8aa5-cdb0-adff48a92d36.htm) | The DGN file version. Default value of fileVersion is DGNFileFormat.Default. |
| Public property | [HatchPatternsFileName](25578983-c9f4-0e2b-29dd-c0a58fb89b08.htm) | Custom hatch patterns (pat) file name. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [HideReferencePlane](3753cc56-d37a-f099-c028-b9a7051df6dd.htm) | Whether or not to hide reference planes. Default value is false. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [HideScopeBox](92a66243-4918-c1c0-4cf8-933037d17819.htm) | Whether or not to hide the scope box. Default value is false. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [HideUnreferenceViewTags](5507e467-964c-43fd-374e-50d341a25ee2.htm) | Whether or not to hide unreference view tags. Default value is false. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [IsValidObject](787dd92b-1ea4-be3d-7aab-dc061c5b448e.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [LayerMapping](693ca2ec-97d0-a0b4-e5f1-0691b226cfc5.htm) | Name of a layer settings standard or filename (with custom layer settings). Valid standards are: DGNV7 (only for DGN), AIA, CP83, BS1192, and ISO13567. default value is "" (empty) which means if no value is set, if no value is set, Revit will use a default value according to the localization. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [MergedViews](8fa912e0-6671-5970-f44e-39052e285575.htm) | Whether to merge all views in one file (via XRefs). Default value of mergedViews is false. |
| Public property | [PreserveCoincidentLines](2bed75a3-2098-65a4-a170-4cd2d11bfb0f.htm) | Whether or not to preserve coincident lines. Default value is false. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [PropOverrides](e673ff0c-3b14-c06c-d5c2-f762c6ca46d5.htm) | How to export overridden object styles. Default value is PropOverrideMode.ByEntity. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [SeedName](c4990cfe-93c1-34de-667a-d2b7ba735f54.htm) | The name of the DGN seed. Default value of seedName is empty. |
| Public property | [WorkingUnits](a3d77b58-47f4-4c01-e0ac-15f12afa0e4f.htm) | If true, Main Units will be used. If false, Sub Units will be used. Default value of WorkingUnits is true. |

# See Also

[DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)