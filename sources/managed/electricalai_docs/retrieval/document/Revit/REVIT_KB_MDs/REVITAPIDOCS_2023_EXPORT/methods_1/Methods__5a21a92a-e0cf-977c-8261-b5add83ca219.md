[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BaseExportOptions Members

---



|  |
| --- |
| [BaseExportOptions Class](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](b4c35f2c-100e-c009-ceae-c01ad46f3db8.htm) | Releases all resources used by the  [BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetExportFontTable](6dc659b4-4131-c1bf-e418-4afc551095d0.htm) | Gets font table. |
| Public method | [GetExportLayerTable](1ce6b604-0b45-f05f-863e-952b85e5a862.htm) | Gets the layer table. |
| Public method | [GetExportLinetypeTable](eba17284-95da-cea8-6b24-4e99bf196629.htm) | Gets a copy of the line type table. |
| Public method | [GetExportPatternTable](6f852987-50c6-e44a-398a-b23a01a1a0a5.htm) | Gets a copy of the pattern table. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method Static member | [GetPredefinedSetupNames](815928cf-5c0e-ceda-c9ac-a3b1c992e27b.htm) | Returns a list of names of predefined setups of export options. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [SetExportFontTable](86d6662a-fc5b-0027-2167-0f1f70efc923.htm) | Sets font table to option. |
| Public method | [SetExportLayerTable](9d1bb366-8472-4141-945b-47a6b02fe1e7.htm) | Sets layer table back to option |
| Public method | [SetExportLinetypeTable](7e4e09ba-d012-7ad9-762e-a0eb732b2178.htm) | Sets the line type table to use during export. |
| Public method | [SetExportPatternTable](8050ce21-d4b7-4c46-6fe6-8a065b8a2e36.htm) | Sets the pattern table to use during export. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Colors](29f6fbf4-0651-a3d6-7ee6-86297335b03d.htm) | Export color mode. Default value is ExportColorMode.IndexColors. |
| Public property | [HatchPatternsFileName](25578983-c9f4-0e2b-29dd-c0a58fb89b08.htm) | Custom hatch patterns (pat) file name. |
| Public property | [HideReferencePlane](3753cc56-d37a-f099-c028-b9a7051df6dd.htm) | Whether or not to hide reference planes. Default value is false. |
| Public property | [HideScopeBox](92a66243-4918-c1c0-4cf8-933037d17819.htm) | Whether or not to hide the scope box. Default value is false. |
| Public property | [HideUnreferenceViewTags](5507e467-964c-43fd-374e-50d341a25ee2.htm) | Whether or not to hide unreference view tags. Default value is false. |
| Public property | [IsValidObject](787dd92b-1ea4-be3d-7aab-dc061c5b448e.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [LayerMapping](693ca2ec-97d0-a0b4-e5f1-0691b226cfc5.htm) | Name of a layer settings standard or filename (with custom layer settings). Valid standards are: DGNV7 (only for DGN), AIA, CP83, BS1192, and ISO13567. default value is "" (empty) which means if no value is set, if no value is set, Revit will use a default value according to the localization. |
| Public property | [PreserveCoincidentLines](2bed75a3-2098-65a4-a170-4cd2d11bfb0f.htm) | Whether or not to preserve coincident lines. Default value is false. |
| Public property | [PropOverrides](e673ff0c-3b14-c06c-d5c2-f762c6ca46d5.htm) | How to export overridden object styles. Default value is PropOverrideMode.ByEntity. |

# See Also

[BaseExportOptions Class](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)