[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PanelScheduleData Members

---



|  |
| --- |
| [PanelScheduleData Class](d24fcc19-3240-8f07-68ca-ce7b62f7aac3.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [PanelScheduleData](d24fcc19-3240-8f07-68ca-ce7b62f7aac3.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddLoadClassification](756df300-6d02-f9b3-e57b-165eb7900179.htm) | Add a Load Classification Id to the array of Load Classifications. |
| Public method | [Dispose](51795d34-2cc1-a54f-26ac-c6876d778f60.htm) | (Inherited from  [TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetLoadClassifications](bdcb0fa5-478c-c968-d224-9444bc850fd7.htm) | Gets an array of the load classifications associated with this panel schedule |
| Public method | [GetNumberOfCircuitRows](458f766e-e8b2-9f0a-2931-e61ebb6489fb.htm) | Gets the number of rows in the circuit table |
| Public method | [GetSectionData(Int32)](ac5594a4-3b6e-9a85-ac7c-363340f09aac.htm) | Returns the section data array element at the specified index. (Inherited from  [TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)  .) |
| Public method | [GetSectionData(SectionType)](154fcb09-0a96-d795-5df2-e2ec6ad244d5.htm) | Returns the pointer to the section data array element at the specified section type. (Inherited from  [TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [IsEqual](1dbaa75b-3eca-c000-807c-5cac1cfc5fdb.htm) | Checks if this element is equal in value to the other element. (Inherited from  [TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)  .) |
| Public method | [IsSymmetric](edd480ed-6368-da6c-2dec-2602ce106035.htm) | Check if this panel schedule is symmetric |
| Public method | [IsValidZoomLevel](0b29dd56-50f3-1768-513f-545bfa4db09f.htm) | Verifies if the value of zoom level is valid. (Inherited from  [TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)  .) |
| Public method | [RemoveLoadClassification](4cae60f4-6694-24db-0c46-b6d6fbdaae75.htm) | Remove a Load Classification Id from the array of Load Classifications |
| Public method | [SetBorderAroundSchedule](5b406f92-7dc3-7946-d2e7-f35751038945.htm) | Adds a border around the schedule |
| Public method | [SetBorderAroundSections](c25694a5-1778-1223-df13-f55ecd02d8ad.htm) | Adds a border around the sections |
| Public method | [SetLoadClassifications](1394dc62-5e84-151a-e801-5556d66f6aea.htm) | Sets the Load Classifications associated with this panel schedule |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |
| Public method | [UpdateCircuitTableForInstance](617774de-9234-6347-051d-203cdf8172ed.htm) | Redraw the circuit table for the given panel with the given parameter updates |
| Public method | [UpdateCircuitTableForTemplate](9453a173-c467-0c49-9c1e-a5f413d95dec.htm) | Redraw the circuit table for a template with the given parameter updates |
| Public method | [UpdateIsSectionHidden](a8832575-8ce9-9af4-d8a8-8241bc5fb882.htm) | Update if this section is hidden or not |
| Public method | [UpdateLoadSummary](124f82f2-b09c-7941-bb9d-96cc8f285eef.htm) | Update the load summary section |
| Public method | [UpdateVerticalHeadersInSection](cfee3750-8e7f-a593-7adc-702f56b0a9c1.htm) | Sets if this header should have vertical text |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BodyShowsVerticalHeaders](405680fb-34f3-97b1-557f-0966257b5dbe.htm) | Shows text in the Load Summary section's headers vertically instead of horizontally |
| Public property | [BorderAroundSchedule](4e87fd46-6762-6ec0-5bf9-896825205572.htm) | Places a border (GraphicStyle element) around the entire schedule, visible only on the instance and sheet |
| Public property | [BorderAroundSections](ee887897-cd12-99ae-f6f3-a0cd96fe4818.htm) | Places a border (GraphicStyle element) around each section, visible only on the instance and sheet |
| Public property | [FreezeColumnsAndRows](6de1e628-31ce-7de1-d53d-9d1b57553bb1.htm) | set to true if the columns and rows should be unmovable by the slider grips (Inherited from  [TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)  .) |
| Public property | [IsAutoShadingForLoadDisplay](9668b833-8b16-6cc9-01dc-c04456cf3ed6.htm) | Display shading of load cells automatically or not. |
| Public property | [IsFooterSectionHidden](3998d37a-3293-5fe8-866d-96993fae4f49.htm) | True if the user wishes to hide the footer section; setting this value must go through the appropriate update function |
| Public property | [IsHeaderSectionHidden](e2e39d21-7934-f3eb-3a69-54d308b10971.htm) | True if the user wishes to hide the header section; setting this value must go through the appropriate update function |
| Public property | [IsPanelSinglePhase](57c53807-579e-d23c-2e3c-bb08b5ca9440.htm) | Identifies if the panel is single phase. |
| Public property | [IsSummarySectionHidden](79e785de-d4e7-9a84-ab8c-eece28c42b1f.htm) | True if the user wishes to hide the summary section; setting this value must go through the appropriate update function |
| Public property | [IsUnusedPhaseHidden](522a3c15-d46e-19dc-2a01-7482ba87d935.htm) | True if the user wishes to hide the unused phase column of a single phase panel, false otherwise. |
| Public property | [IsValidObject](c7fa73f8-59df-dd41-c8e6-4b98093e9a19.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)  .) |
| Public property | [NumberOfSections](4f57f099-a0cb-6d95-2716-a5c3417654d4.htm) | Gets the number of items in section data array. (Inherited from  [TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)  .) |
| Public property | [NumberOfSlots](ad720121-48c1-c2a4-57a7-fec1543fa865.htm) | The number of slots in the panel schedule; setting this value must go through the appropriate update function |
| Public property | [PanelConfiguration](e89fdc67-fd93-2ce5-6592-adeafa6f1179.htm) | The panel configuration of this panel schedule |
| Public property | [PhaseLoadType](ccdab100-5dfb-10ff-1e7c-1910c049d0a3.htm) | This property determines the layout of the phase load columns; setting this value must go through the updateCircuitTable function |
| Public property | [PhasesAsCurrents](50bd4c92-f81a-7f5c-01cc-92d49e7fd56f.htm) | If true, the phase columns are currents (A), otherwise they are loads (VA); setting this value must go through the appropriate update function |
| Public property | [ScheduleType](3fb70110-d4d9-55ef-aac0-bd12df07786c.htm) | The panel schedule type of this panel schedule |
| Public property | [ShowCircuitNumberOnOneRowForMultiphaseCircuits](2c400aa9-7d56-e1fb-8762-2ec3b603ddfe.htm) | Shows the circuit number broken up on each row of the multiphase circuit rows if true, all on the first row otherwise |
| Public property | [ShowMultipleRowsForMultiphaseCircuits](4ccaca7c-243a-4264-5703-868836f13d6f.htm) | shows extra rows below multiphase circuits to indicate how many slots they take up if true, all on a single row otherwise |
| Public property | [ShowSlotFromDeviceInsteadOfTemplate](c5ea28f4-3388-5e21-54a7-750f6a433aa0.htm) | When true, the number of rows in an instance will be the number of poles on the associated device, not a set number |
| Public property | [SummaryShowsGroups](9244a87e-c35f-b6df-9e13-8b1246a27f25.htm) | Show groups of load classifications in the load summary section |
| Public property | [SummaryShowsOnlyConnectedLoads](e259c5ea-cfac-5e82-e147-3fab28f2a21d.htm) | Show only the connected load classifications in the summary section |
| Public property | [SummaryShowsVerticalHeaders](81aa76f2-38cb-afc3-8ddc-991affadcde7.htm) | Shows text in the Load Summary section's headers vertically instead of horizontally |
| Public property | [Width](2501ac82-ebc3-10e6-1740-29ef3c81d3ed.htm) | Gets or sets the table width in feet (Inherited from  [TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)  .) |
| Public property | [WidthInPixels](67af51c2-1c2b-64e0-35fa-448033fb4810.htm) | Gets the width of the panel schedule in logical pixels (Inherited from  [TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)  .) |
| Public property | [ZoomLevel](ead726cc-7695-e71d-e4a6-919319bb58db.htm) | The value of zoom level for corresponding TableView. (Inherited from  [TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)  .) |

# See Also

[PanelScheduleData Class](d24fcc19-3240-8f07-68ca-ce7b62f7aac3.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)