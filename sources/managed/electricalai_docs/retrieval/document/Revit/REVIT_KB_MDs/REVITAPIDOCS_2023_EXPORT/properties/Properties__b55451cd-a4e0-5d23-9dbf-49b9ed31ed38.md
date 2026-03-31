[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.FaceSplitterFailures Members

---



|  |
| --- |
| [BuiltInFailures FaceSplitterFailures Class](c354be2c-4d56-3ed0-6977-3c5cf6972cdf.htm)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in FailureDefinitionId instances.

The  [BuiltInFailures FaceSplitterFailures](c354be2c-4d56-3ed0-6977-3c5cf6972cdf.htm)  type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [CannotUseCurvesForFaceSplit](7bd8dda8-92d3-bf78-ff59-675025a2f47c.htm) | The sketch cannot split the face of the highlighted element. |
| Public property Static member | [EndsNotOnEdgeError](06d542ee-8006-582f-3eb2-2091438b855e.htm) | Ends of an open loop in sketch splitting face do not lie on an edge of the face to split. |
| Public property Static member | [InvalidClosedLoopsForFaceSplit](ff21648e-5c98-1266-a2fa-94344fcc75b6.htm) | The closed loop used to split the face must lie completely within the face and cannot intersect or overlap any of the face's edges. To split a face at its border, use an open loop that ends on the boundary of the face. |
| Public property Static member | [InvalidOpenLoopsForFaceSplit](995f3404-810c-25ce-8c15-6460b8750948.htm) | The open loops used to split the face must lie completely within the face and cannot intersect or overlap any of the face's edges. |
| Public property Static member | [LoopsDoNotSubdivideFace](6700b99f-c3cc-9bfd-53ad-3d5abf317764.htm) | Sketched loops must sub-divide the face into two or more completely enclosed regions. |
| Public property Static member | [LoopsOutsideFaceSplitError](535caf99-8515-86c5-c505-8f7d6eedaa64.htm) | Some of the lines drawn lie outside of the boundary of the face being split. All lines used to split a face must be contained within the face being split and cannot intersect or overlap any of the boundaries of that face. |
| Public property Static member | [NoFaceForSplit](923a8482-ba81-100c-261c-96802a202ee2.htm) | The highlighted element no longer contains a face that has been split by highlighted sketch. |

# See Also

[BuiltInFailures FaceSplitterFailures Class](c354be2c-4d56-3ed0-6977-3c5cf6972cdf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)