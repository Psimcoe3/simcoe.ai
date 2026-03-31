[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DWGExportOptions Members

---



|  |
| --- |
| [DWGExportOptions Class](3e510f02-1a4c-3e4f-f923-e96972d03862.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [DWGExportOptions](3e510f02-1a4c-3e4f-f923-e96972d03862.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [DWGExportOptions](36314aba-5818-8292-1655-b386f836d10c.htm) | Constructs a new instance of DWGExportOptions with default values of all properties. |
| Public method | [DWGExportOptions(DWGExportOptions)](73eb12c2-04a6-a91d-20f0-a1586f56782a.htm) | Constructs a new instance of DWGExportOptions as a copy of the export options. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](b4c35f2c-100e-c009-ceae-c01ad46f3db8.htm) | (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetExportFontTable](6dc659b4-4131-c1bf-e418-4afc551095d0.htm) | Gets font table. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [GetExportLayerTable](1ce6b604-0b45-f05f-863e-952b85e5a862.htm) | Gets the layer table. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [GetExportLinetypeTable](eba17284-95da-cea8-6b24-4e99bf196629.htm) | Gets a copy of the line type table. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [GetExportPatternTable](6f852987-50c6-e44a-398a-b23a01a1a0a5.htm) | Gets a copy of the pattern table. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method Static member | [GetPredefinedOptions](0ae4a6f6-6a0a-8363-b580-7b61b61bca6d.htm) | Returns an instance DWGExportOptions containing settings from a predefined export setup. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [SetExportFontTable](86d6662a-fc5b-0027-2167-0f1f70efc923.htm) | Sets font table to option. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [SetExportLayerTable](9d1bb366-8472-4141-945b-47a6b02fe1e7.htm) | Sets layer table back to option (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [SetExportLinetypeTable](7e4e09ba-d012-7ad9-762e-a0eb732b2178.htm) | Sets the line type table to use during export. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [SetExportPatternTable](8050ce21-d4b7-4c46-6fe6-8a065b8a2e36.htm) | Sets the pattern table to use during export. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ACAPreference](1a97e079-901e-56e0-252d-2b030d04e595.htm) | The preferred way to generate geometry of ACA objects. Default value is ACAObjectPreference.Object. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [Colors](29f6fbf4-0651-a3d6-7ee6-86297335b03d.htm) | Export color mode. Default value is ExportColorMode.IndexColors. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [ExportingAreas](66795862-f8fb-778a-1413-b3e7f00ea9e5.htm) | True to export area and room geometry, false otherwise. Default value is false. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [ExportOfSolids](bdce5da4-9a31-9be7-4d31-5dad2bc27c43.htm) | The mode used to export solids in 3D views. Default value is SolidGeometry.Polymesh. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [FileVersion](65a691e9-773a-5ec9-2249-5f344bf08e83.htm) | ACADVersion::Default Default value is ACADVersion.Default. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [HatchBackgroundColor](47e158cd-a84e-13c2-8459-e0b0c95cc6f7.htm) | The color that will be set as hatch backgound color on the exported hatch. This color will be used only if useHatchBackgroundColor is true. default value is white (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [HatchPatternsFileName](25578983-c9f4-0e2b-29dd-c0a58fb89b08.htm) | Custom hatch patterns (pat) file name. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [HideReferencePlane](3753cc56-d37a-f099-c028-b9a7051df6dd.htm) | Whether or not to hide reference planes. Default value is false. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [HideScopeBox](92a66243-4918-c1c0-4cf8-933037d17819.htm) | Whether or not to hide the scope box. Default value is false. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [HideUnreferenceViewTags](5507e467-964c-43fd-374e-50d341a25ee2.htm) | Whether or not to hide unreference view tags. Default value is false. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [IsValidObject](787dd92b-1ea4-be3d-7aab-dc061c5b448e.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [LayerMapping](693ca2ec-97d0-a0b4-e5f1-0691b226cfc5.htm) | Name of a layer settings standard or filename (with custom layer settings). Valid standards are: DGNV7 (only for DGN), AIA, CP83, BS1192, and ISO13567. default value is "" (empty) which means if no value is set, if no value is set, Revit will use a default value according to the localization. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [LineScaling](8e197871-e18e-4270-6292-1bbdabe96ff0.htm) | The scaling mode for the line type. Default value is LineScaling.ViewScale. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [LinetypesFileName](8c81b2a0-e9f9-e3e1-4b07-820ad43d8f22.htm) | The custom linetype file name (\*.lin). Default value is empty. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [MarkNonplotLayers](15af29b2-8654-1a8c-a701-849be9bc9288.htm) | If true and the nonplot layer suffix is not empty, all layers whose names contain that suffix will be marked as non-plot. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [MergedViews](28b54043-59a4-a5a7-cca0-7a9aea1f6250.htm) | Whether to merge all views in one file (via XRefs). Default value is false for mergedViews. |
| Public property | [NonplotSuffix](c83da56f-b0e1-5789-2b46-e76728ce5704.htm) | If the MarkNonplotLayers attribute is set to true, all layers with names containing this suffix will be marked as non-plot. No action will be performed if the suffix is empty. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [PreserveCoincidentLines](2bed75a3-2098-65a4-a170-4cd2d11bfb0f.htm) | Whether or not to preserve coincident lines. Default value is false. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [PropOverrides](e673ff0c-3b14-c06c-d5c2-f762c6ca46d5.htm) | How to export overridden object styles. Default value is PropOverrideMode.ByEntity. (Inherited from  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  .) |
| Public property | [SharedCoords](1a291c40-65d6-cae1-a69c-e60ef026645a.htm) | True to use the shared coordinate system's origin, false to use the project origin. Default value is false. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [TargetUnit](3567c8f2-bef5-6872-5766-d5c633742b35.htm) | The target unit type. Default value is ExportUnit.Default. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [TextTreatment](a5c70d54-21b3-c2e7-4d33-4532815111d5.htm) | The text treatment. Deault value is TextTreatment.Exact. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |
| Public property | [UseHatchBackgroundColor](1aa0ce6b-68d1-6643-9491-4b9328cf53e0.htm) | Indicates if hatch background color will be used or not. default value is false. (Inherited from  [ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)  .) |

# See Also

[DWGExportOptions Class](3e510f02-1a4c-3e4f-f923-e96972d03862.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)