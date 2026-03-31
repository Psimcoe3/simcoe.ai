[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarUpdateCurvesData Members

---



|  |
| --- |
| [RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [RebarUpdateCurvesData](ff847aea-8397-8b79-b039-16a72e479c9f.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](ebe006df-3b70-5c5f-c188-c30e3ba723d2.htm) | Releases all resources used by the  [RebarUpdateCurvesData](ff847aea-8397-8b79-b039-16a72e479c9f.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetAttachmentType](4cde7b4f-6636-9ee8-f421-47f8e4887fee.htm) | Returns attachment type for stirrups to be used in cover calculation. |
| Public method | [GetBarGeometry](fdbf4cd8-3066-2768-d94d-d8ebfb92009f.htm) | Returns the geometry for a bar at the specified index currently in the Rebar. |
| Public method | [GetBarModelDiameter](990c08e9-0307-be15-15cf-49d39b942d4c.htm) | Gets the model diameter of the Rebar. |
| Public method | [GetBarNominalDiameter](ba1fe117-b6d2-75ba-86dd-d52590724b36.htm) | Gets the nominal diameter of the Rebar. |
| Public method | [GetBarsNumber](bde20032-f24e-ab77-6636-a59c4cebd5fa.htm) | Gets the number of bars specified in the layout options. This is used to calculate the sets driven by bar number. |
| Public method | [GetBendingRadius](e645dfff-bd07-8997-fd4f-be08cffbfcf0.htm) | Gets the current bending radius of the rebar. |
| Public method | [GetChangedCustomHandles](5e52f5fb-0160-7bde-c9cc-c654129984f6.htm) | Returns an array containing custom handles that were changed since the last regeneration. Array is empty if no handles were changed since the last regeneration. |
| Public method | [GetChangedSharedParameterGUIDs](52f33c35-c8b3-0fce-7f05-5a6280e44a93.htm) | Returns an array containing the shared parameter GUIDs that were changed since the last regeneration. Array is empty if no shared params were changed since the last regeneration. |
| Public method | [GetCustomConstraints](d753c390-8d4c-5193-eef8-ec7b9e7bd875.htm) | Gets all rebar constraints that are attached to custom handles for this rebar. |
| Public method | [GetDocument](ced60288-464b-76e1-8d85-49b691c04a5f.htm) | Gets a reference to the current document. |
| Public method | [GetEndConstraint](bfa1ffbd-d5fa-835b-d628-a9ed97e90017.htm) | Gets the current constraint for the end handle of the Rebar. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetHookOrientationAngle](50bd6278-bbb7-7b6c-029d-e34f7b42ddb9.htm) | Get the hook orientation angle at end that is currently in the rebar. |
| Public method | [GetHookPlaneNormalForBarIdx](ff212171-e964-2045-42f8-1519762cff43.htm) | Returns the normal of plane in which the hook at end of bar with index barPositionIndex that is currently in Rebar. |
| Public method | [GetHostId](4f29a5a7-9703-f0d4-9567-4a042d6b927a.htm) | Gets the id of the host structural for this rebar. |
| Public method | [GetLayoutRule](9948e798-a1d6-6ab0-cd94-57f4e99a9206.htm) | Gets the layout rule for this bar. |
| Public method | [GetNumberOfBars](e48e7c02-53e1-f222-26a3-a80c5f97c9cd.htm) | Returns the number of bars currently in the rebar. |
| Public method | [GetRebarId](ef027bb1-3944-1abd-78ef-02125ec36a9e.htm) | Get the id of the Rebar element currently being calculated. |
| Public method | [GetRebarStyle](f158584c-2a53-8e60-fb50-afcb4bac0d75.htm) | Gets the style of the rebar. |
| Public method | [GetStartConstraint](6f5516f2-6715-c642-4d73-ccf85be35178.htm) | Gets the current constraint for the start handle of the Rebar. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [SetHookOrientationAngle](182e024d-55e6-24e7-4125-a1288a2cb7a1.htm) | Set the hook orientation angle at end. This information is set to the rebar after the API execution is finished successfully. |
| Public method | [SetHookPlaneNormalForBarIdx](e639b633-d0c2-3913-dad4-ad9fde83fc32.htm) | Set the normal of plane in which the hook at end of bar with index barPositionIndex will stay. This information is set to the rebar after the API execution is finished successfully. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AreWorkshopInstructionsChanged](4edc3d5e-dd8c-5549-6766-03319c538b7c.htm) | Indicates if the workshop instructions have changed since the last regeneration. |
| Public property | [ErrorMessage](858682bf-3961-9f2b-c515-6b6178ca7f36.htm) | The reason for calculation failure. If the calculation fails, this message will be shown in an error, or warning if we are editing the constraints. |
| Public property | [HostMirrored](7e5256ff-5025-9091-5056-c2261eadbc71.htm) | If true, then host of the rebar was mirrorred (along with the rebar) before this regeneration. |
| Public property | [IsAttachmentTypeChanged](a4e69222-df6f-43e8-d771-8057ede14f59.htm) | Indicates if the attachment type has changed since the last regeneration. |
| Public property | [IsBarsNumberChanged](f9c25fd6-9a2b-3256-87f5-5263b81b50ae.htm) | Indicates if the bar number has changed since the last regeneration. |
| Public property | [IsBendingRadiusChanged](b2d9fe7c-8574-cbd1-649b-f85e323c9023.htm) | Indicates if the bending radius has changed since the last regeneration. |
| Public property | [IsEndConstraintChanged](e0f39d9d-c6f6-6171-2417-f8955fd9df48.htm) | Indicates if the end handle constraint has changed since the last regeneration. |
| Public property | [IsLayoutChanged](e899e410-1146-0999-bcf7-9c2654edf8cd.htm) | Indicates if the layout has changed since the last regeneration. |
| Public property | [IsReversed](e58025cb-84de-5dd2-afe6-92d811500f16.htm) | Used to store the state of the bar refering to the direction of the bars. This is useful when using face intersection to calculate bars. After mirroring, curves created from intersecting faces may be reversed, so we use this to store the state and keep the rebar pointing in the correct direction. |
| Public property | [IsSpacingChanged](a0777387-3afd-8563-8787-df3b09f68b8f.htm) | Indicates if the spacing has changed since the last regeneration. |
| Public property | [IsStartConstraintChanged](8d7fd7b3-4a9a-bd4a-0dbd-83a7842e4e1b.htm) | Indicates if the start handle constraint has changed since the last regeneration. |
| Public property | [IsStyleChanged](f3703d7b-9bbc-3e47-2cf8-d859018f29a0.htm) | Indicates if the style has changed since the last regeneration. |
| Public property | [IsValidObject](d2640a19-317e-b66d-c8e5-47a321eca59e.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [Spacing](56add314-9f76-d2bd-afa7-fa9fed067ef3.htm) | The spacing between the bars, according to the LayoutRule. |
| Public property | [WorkshopInstructions](6daee31b-85cf-d7f0-1c96-13d3a13a3bc0.htm) | Identifies the workshop instructions of this rebar. |

# See Also

[RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)