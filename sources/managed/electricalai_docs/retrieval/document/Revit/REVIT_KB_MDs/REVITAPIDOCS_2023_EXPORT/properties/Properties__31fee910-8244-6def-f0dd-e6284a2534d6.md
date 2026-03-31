[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.PerformanceFailures Members

---



|  |
| --- |
| [BuiltInFailures PerformanceFailures Class](d008a572-b1aa-1e46-0c4e-f760c50776fd.htm)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in FailureDefinitionId instances.

The  [BuiltInFailures PerformanceFailures](d008a572-b1aa-1e46-0c4e-f760c50776fd.htm)  type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [ClippingIsDisabled](6c5f6778-bf8d-b66f-4683-934bd0f66fe7.htm) | View has clipping disabled. It causes view to draw too many elements. |
| Public property Static member | [DisjoinedSolidsInInPlaceFamily](1b474262-8b56-a5f0-9ecb-ffe07afd8732.htm) | In-place family contains multiple disjoined solids. Consider splitting in several in-place families. |
| Public property Static member | [DuplicateInstances](4720819c-25b8-a25d-ee4e-530e043cb60f.htm) | There are duplicate instances of the same family in the same place. Delete duplicate instances to improve performance. |
| Public property Static member | [FamilyContainsViewSpecificImports](f7a2ba82-9924-bb46-3f42-bed1ff81a21f.htm) | Family definition contains view-specific imports. Such imports are inaccessible in the project - consider removal. |
| Public property Static member | [HostHasTooManyInserts](d2097449-8e90-bab6-6070-16c491bde85c.htm) | Host object contains too many cutting inserts - it may take long time to update. Consider splitting host object into smaller pieces or using stacked walls. |
| Public property Static member | [InteriorCategoriesEnabledInLargeView](0c61e6e2-df5d-d232-6a33-bdd397a2dbaa.htm) | Interior categories are enabled in a large view. Even though these objects may be obscured and invisible, they still have negative impact on performance. |
| Public property Static member | [LargeFamilyFile](e1c15eb8-63c3-7d9a-b917-7f72cf49523d.htm) | Family occupies XXX kilobytes of memory. Consider simplification of the family. |
| Public property Static member | [ManyElementInFamily](f3e4a8bc-a119-adc6-6011-5ca35736da66.htm) | Family definition contains too many elements. Consider simplification of the family. |
| Public property Static member | [ManyUnusedNestedFamilies](152d7d7a-b1e6-593b-76f0-30ff5de01895.htm) | Family contains other families loaded into it but not used. Consider purging family document from unused families and types. |
| Public property Static member | [MultipleLoopsInSketch](e347f2de-272c-9ae1-f008-94e3842dd53c.htm) | Sketch of <element> contains multiple independent loops - splitting it in few independent elements might improve performance. |
| Public property Static member | [TooLargeSketch](e4b7ae47-1123-19b0-a857-6d70fd995761.htm) | Sketch of <element> has large area - it may slow down selection, drawing and geometric computations. |
| Public property Static member | [TooManyAreaBoundaryLinesFound](92bd9600-db50-0b61-8745-f8e371fb9afd.htm) | There are too many area boundary lines in area scheme <element> might result in increased model sizes on disk and in memory. Please investigate if area scheme is used in a proper way. |
| Public property Static member | [TooManyElementsInSketch](1c6d3046-c762-8656-1cd3-173f05c7a5af.htm) | Sketch of <element> contains too many objects - it may take long time to solve. |
| Public property Static member | [UnjoinedRoomSeparationLinesFound](f6225ba1-9429-72a3-1bde-d3c5b3e468e6.htm) | Room Separation of <element> is not joined, might cause performance issue with room boundaries computations. |
| Public property Static member | [UnusedTypesInTheProject](1065d4e6-23fd-a48d-0a4d-eaa096ad1036.htm) | Project contains unused families and/or types. Consider purging them out. |
| Public property Static member | [ViewDetailLevelIsHighInLargeView](80df7346-e018-338f-b41b-b5d95aebd53a.htm) | A large view has view detail level set to medium or coarse. Generation of extraneous details harms performance. |
| Public property Static member | [WallsOverlap](8688de5f-6398-1ee2-adc2-9b7f8b7f1edc.htm) | Walls overlap. Consider embedding walls, editing their extents or profile to avoid overlapping. |

# See Also

[BuiltInFailures PerformanceFailures Class](d008a572-b1aa-1e46-0c4e-f760c50776fd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)