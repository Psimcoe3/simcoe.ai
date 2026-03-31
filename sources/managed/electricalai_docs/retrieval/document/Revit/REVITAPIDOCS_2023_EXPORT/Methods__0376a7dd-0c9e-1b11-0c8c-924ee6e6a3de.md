[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleField Members

---



|  |
| --- |
| [ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ScheduleField](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CanDisplayMinMax](092ec46b-89b2-c8e9-7b5f-4abc9e5313c1.htm) | Indicates if this field can display minimum and maximum values. |
| Public method | [CanTotal](88ffc634-bae0-0ef7-b232-81cd80a391fe.htm) | Indicates if totals can be enabled for this field. |
| Public method | [CanTotalByAssemblyType](bb92f36f-f3ef-9aa5-eb1e-50f830726f51.htm) | Indicates if totals by assembly type can be enabled for this field. |
| Public method | [CreatesCircularReferences](51554332-14f6-ea80-7d5a-ad1f8dc76627.htm) | Checks whether a field ID would create a circular chain of references when used by the PercentageOf property of this field. |
| Public method | [Dispose](85dd2541-33d1-9fc9-4769-73cafd256d3e.htm) | Releases all resources used by the  [ScheduleField](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetCombinedParameters](fe772ceb-b239-4da3-e3c3-5fb4a42d1f88.htm) | Gets this field's combine parameter array if applicable |
| Public method | [GetFormatOptions](c0f20eb6-3e5e-11b3-458c-f38acbe2cddd.htm) | Gets the FormatOptions to optionally override the default settings in the Units class. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetName](33d57eac-bbf6-1852-ea11-7e99b0ffbbff.htm) | Gets the name of the field. |
| Public method | [GetSchedulableField](cf6a6ae1-a693-a35b-3051-b34475ea574c.htm) | Gets a SchedulableField object representing this field. |
| Public method | [GetSpecTypeId](dbd738d0-9b8b-4792-34a9-5b64a1063083.htm) | The spec describing values of this field, if applicable. |
| Public method | [GetStyle](9f52cffd-3219-fc71-df91-0302a56cc299.htm) | Gets the style of this field. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [IsValidCombinedParameters](a8021755-2f5d-719b-23d5-a613ec5957a6.htm) | Checks if data is valid for combined parameters |
| Public method | [ResetOverride](accf7307-7f8f-3876-a478-09ffc96fd7ae.htm) | Resets the override of this field. |
| Public method | [SetCombinedParameters](b216f232-52b8-fbff-a0f7-649834dd213e.htm) | Sets this field's combine parameter array if applicable |
| Public method | [SetFormatOptions](853a134b-205d-5642-15cb-4e8d0db2ca86.htm) | Sets the FormatOptions to optionally override the default settings in the Units class. |
| Public method | [SetStyle](9f0d0e2a-436d-85a6-e2ca-c703e6d11fb9.htm) | Sets the style of this field. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ColumnHeading](3890f745-6f24-f81a-9f8f-d8b47c8e3f94.htm) | The column heading text. |
| Public property | [Definition](0fa34479-59f2-7f67-4d16-48238dc4d2af.htm) | The ScheduleDefinition that this field belongs to. |
| Public property | [DisplayType](ca5cd7f7-081e-65f3-b671-2a1c780a5b09.htm) | Indicates the chosen display type for the field. |
| Public property | [FieldId](e7b1a3c3-1ab5-9e65-a59e-fed8a7d27d42.htm) | The ID of the field in the containing ScheduleDefinition. |
| Public property | [FieldIndex](9abc75e0-3ae0-9ed8-c6b3-9bc352e4a862.htm) | The index of the field in the containing ScheduleDefinition. |
| Public property | [FieldType](e73df1b3-d424-afe4-e1fe-dc434eadbc76.htm) | The type of data displayed by the field. |
| Public property | [GridColumnWidth](061bfa96-9775-32a8-f66d-858990d96f3b.htm) | The width of the column in the editable grid view, measured in feet. |
| Public property | [HasSchedulableField](263d2b9f-68e3-48a1-5757-4700ba3b1e73.htm) | Identifies if this ScheduleField object has access to a SchedulableField. Calculated and combined parameter fields will not have the access. |
| Public property | [HeadingOrientation](1b39a6a8-e775-d37b-99d5-e93165f350bb.htm) | The orientation of the column heading text. |
| Public property | [HorizontalAlignment](d204d391-a453-2793-db9e-1e30716edbaf.htm) | The horizontal alignment of text in the column. |
| Public property | [IsCalculatedField](b33bd011-f26c-e617-5b6d-27968c7b09eb.htm) | Indicates if the field is a calculated field (Formula or Percentage). |
| Public property | [IsCombinedParameterField](52da022b-4dcd-09dd-3137-d32f47ccbfee.htm) | Indicates if the field is a combined parameter field. |
| Public property | [IsHidden](ee90c427-f957-515b-8d93-252b9da0a40d.htm) | Indicates if the field is hidden in the schedule. |
| Public property | [IsOverridden](04fe4475-4173-f7eb-6c0f-11ee1d11f0f4.htm) | Indicates if the field is overridden or not. |
| Public property | [IsValidObject](73bbfcdf-4760-b676-98d7-f54e44912457.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [MultipleValuesCustomText](9f57808d-f3cc-cb93-edbd-dcfaad79bb95.htm) | The custom multiple values text to be used when the schedule field displays multiple element values, used when  [MultipleValuesDisplayType](64592725-4f20-d2a0-010d-220a9315ff39.htm)  is set to  [Custom](cc6f0e5f-958c-8062-2b8f-b443b0fae708.htm)  . |
| Public property | [MultipleValuesDisplayType](64592725-4f20-d2a0-010d-220a9315ff39.htm) | Determines the type of multiple value indication to be used when the schedule field displays multiple element values. |
| Public property | [MultipleValuesText](321d43b7-416b-06fd-54c3-15d8d2605f34.htm) | The multiple values text to be used when the schedule field displays multiple element values, as specified by the display type  [MultipleValuesDisplayType](64592725-4f20-d2a0-010d-220a9315ff39.htm)  . |
| Public property | [ParameterId](ecad009d-a968-2adc-9891-128e9ee8074a.htm) | The ID of the parameter displayed by the field. |
| Public property | [PercentageBy](7c606b36-212f-0392-6eb5-799ab748a330.htm) | The ID of the grouped schedule field used to calculate percentage totals. |
| Public property | [PercentageOf](12f76318-e8fa-d5b8-d52e-434a07f159f9.htm) | The ID of the field to calculate percentages of. |
| Public property | [Schedule](1b5f2a55-5ea2-e468-b887-7f3c98aa6e85.htm) | The schedule that this field belongs to. |
| Public property | [SheetColumnWidth](999e9e46-2259-19f4-cfc1-9c52509a2385.htm) | The width of the column on a sheet, measured in feet. |
| Public property | [TotalByAssemblyType](672a1283-cdb4-f7fb-b697-f67238c8755c.htm) | In an assembly schedule view, indicates if totals are calculated for all assembly instances of the same type or only for a single instance. |

# See Also

[ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)