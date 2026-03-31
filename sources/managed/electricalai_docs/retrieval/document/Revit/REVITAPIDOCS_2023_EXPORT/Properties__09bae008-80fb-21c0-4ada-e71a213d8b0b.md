[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.RebarCouplerFailures Members

---



|  |
| --- |
| [BuiltInFailures RebarCouplerFailures Class](f1af7139-8dc7-c6de-b703-b01eb95fdff3.htm)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in FailureDefinitionId instances.

The  [BuiltInFailures RebarCouplerFailures](f1af7139-8dc7-c6de-b703-b01eb95fdff3.htm)  type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [CantKeepConstraintsToBars](92b1d6c6-5e03-9414-ba4f-66c9090044a2.htm) | The constraints between the coupler and the two connected bars are no longer satisfied. Post error to delete the coupler. |
| Public property Static member | [CouplerRequiredRemoveFromGroup](60730f9c-74a5-9ee9-4acc-d0f96283ee1e.htm) | The coupler is invalid in group. |
| Public property Static member | [CouplerTypeInvalid](83dffa17-a810-b1a1-927b-fd18a76aca5a.htm) | This coupler type does not fit on the selected bar(s). Post error to delete the coupler. |
| Public property Static member | [DisconnectElements](19dafbc8-d4b0-dc39-3242-0a37c95ec44f.htm) | Disconnect the coupler from the connected bar. |
| Public property Static member | [DistanceBetweenBarsError](3874401a-e754-c985-7c7d-0c48c3106257.htm) | This is used to post error. The distance between the connected ends of the bars exceeds 10 bar diameters. |
| Public property Static member | [DistanceBetweenBarsWarning](91b18d1e-0df7-c438-2a0b-54c97c55524e.htm) | This is used to post warning. The distance between the connected ends of the bars exceeds 10 bar diameters. |
| Public property Static member | [EngagementBiggerThanLengthError](2083e5fa-8920-6e91-e9d9-30973b12d409.htm) | This is used to post error. The sum of bar engagements is greater than the total coupler length. |
| Public property Static member | [EngagementBiggerThanLengthWarning](71179097-aa4b-63e8-87a2-765ae08953aa.htm) | This is used to post warning. The sum of bar engagements is greater than the total coupler length. |
| Public property Static member | [LengthParameterError](4e3f31fd-8b17-e0b7-d9a2-5637384ea803.htm) | This is used to post error. The "Total Length" parameter must be set to a strictly positive value. |
| Public property Static member | [LengthParameterWarning](9d841342-d2de-be3b-f034-3a5d986b8f37.htm) | This is used to post warning. The "Total Length" parameter must be set to a strictly positive value. |
| Public property Static member | [MainEngagementParameterError](d23c0c68-b464-b9d3-4385-833edd687207.htm) | This is used to post error. "Bar Engagement 1" has an incorrect value. |
| Public property Static member | [MainEngagementParameterWarning](ad7d5a9b-c776-bfa7-ea1c-4b1a91c3f7c5.htm) | This is used to post warning. "Bar Engagement 1" has an incorrect value. |
| Public property Static member | [NewCouplerTypeCreated](05633cfb-accb-a9fe-15f2-b59bc6990876.htm) | A new coupler type was automatically created to fit the bar diameters. |
| Public property Static member | [NoBarSizeError](9014e174-dd82-a368-48cd-5e398c984777.htm) | This is used to post error. At least Bar Size 1 or Bar Size 2 should have another value than "None". |
| Public property Static member | [NoBarSizeWarning](2dd57241-1e01-291c-52ec-1c279fbbfa2a.htm) | This is used to post warning. At least Bar Size 1 or Bar Size 2 should have a value other than "None". |
| Public property Static member | [NoTypeParamsDefinedWarning](bdfe2f34-b502-1b60-c9cb-d89c3033ed8b.htm) | The parameters of the default type have no values. |
| Public property Static member | [SecondaryEngagementParameterError](2cdc39c6-5ea0-a176-4d98-b62ba650febe.htm) | This is used to post error. "Bar Engagement 2" has an incorrect value. |
| Public property Static member | [SecondaryEngagementParameterWarning](53f0a684-3415-7078-fdd0-1c9bbd0de765.htm) | This is used to post warning. "Bar Engagement 2" has an incorrect value. |
| Public property Static member | [WidthParameterError](3797028d-4955-c2ef-b39a-f8bb1631822a.htm) | This is used to post error.The "External Diameter" parameter must be set to a strictly positive value. |
| Public property Static member | [WidthParameterWarning](a7dc3a0f-981d-6d20-d687-01bc216896b2.htm) | This is used to post warning. The "External Diameter" parameter must be set to a strictly positive value. |

# See Also

[BuiltInFailures RebarCouplerFailures Class](f1af7139-8dc7-c6de-b703-b01eb95fdff3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)