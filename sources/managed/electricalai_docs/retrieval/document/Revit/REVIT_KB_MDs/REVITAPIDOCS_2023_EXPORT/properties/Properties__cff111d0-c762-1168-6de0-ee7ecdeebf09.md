[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.InfillFailures Members

---



|  |
| --- |
| [BuiltInFailures InfillFailures Class](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.htm)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in FailureDefinitionId instances.

The  [BuiltInFailures InfillFailures](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.htm)  type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [CannotDeleteInfill](914040e3-dcd3-b686-53a9-b93b93aa16fb.htm) | Can't delete infilling element without deleting its insert or host. |
| Public property Static member | [FamilyInstanceIsNotCuttingHost](fd95a0c2-367e-00cb-69c3-812819d35e1c.htm) | Instance is not cutting host. |
| Public property Static member | [InfillCannotChangeType](877afc0f-3a3a-484b-0361-65a5738cdab3.htm) | Infilling element replaced by a later phase insert must be the same type as the insert's host. |
| Public property Static member | [InfillCannotHaveDiffThickness](69e99bb2-78d2-d3e0-af2e-71084838b771.htm) | This infilling element must have the same thickness as its host. |
| Public property Static member | [InfillDifferentPhase](7df3db53-ead3-daca-4174-602548754230.htm) | Wall and instance have different phasing settings. Automatic creation of the infilling wall fails. |
| Public property Static member | [InfillLost](bd49fc31-fcc7-8440-bfba-e3047688a6f5.htm) | Standalone infilling Wall is separated from its insert. |
| Public property Static member | [InfillNoSlopeGlazing](00feb0be-205e-2c2d-abdf-939d3a672fb5.htm) | Could not change type due to highlighted infilling element. 'Sloped glazing' infills are not allowed. |
| Public property Static member | [InfillNoThicknessCeiling](f5c1f72a-852f-b090-a83e-871619fcd092.htm) | Could not change type due to highlighted infilling element. 'Basic Ceiling' infills are only compatible with 'Basic Ceiling' hosts. |
| Public property Static member | [InfillNoThicknessMultiface](7930961a-26d0-fa5d-60c1-0598db0896fe.htm) | Highlighted infilling element could not have thickness different from its host because it spans multiple faces. |
| Public property Static member | [InPlaceFamilyNotCuttingHost](d19b81bb-d410-2798-b78a-8b22fa10597e.htm) | Instance of in-place family is not cutting host. |
| Public property Static member | [InsertJoinedWall](f0b21b56-7868-cb17-6436-23adc86199d5.htm) | Insert conflicts with joined Wall. |
| Public property Static member | [InsertOverlapsOrOut](206e7d23-9a5b-7631-ac1d-895bdef74419.htm) | Highlighted inserts overlap with other inserts or completely miss their hosts. |
| Public property Static member | [MovedInfillToHost](03424834-8711-9e91-367b-8c414dc092d3.htm) | Infilling element was automatically moved to keep it aligned to host. |

# See Also

[BuiltInFailures InfillFailures Class](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)