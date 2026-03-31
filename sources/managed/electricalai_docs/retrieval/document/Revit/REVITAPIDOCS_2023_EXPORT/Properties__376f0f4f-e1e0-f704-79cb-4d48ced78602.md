[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.CurtainWallFailures Members

---



|  |
| --- |
| [BuiltInFailures CurtainWallFailures Class](a3d691c9-5f8f-29ca-cfad-fa1d1d66f203.htm)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in FailureDefinitionId instances.

The  [BuiltInFailures CurtainWallFailures](a3d691c9-5f8f-29ca-cfad-fa1d1d66f203.htm)  type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [AdjustEndCurtainWallParameterNoCorners](d46aa2ba-8710-94a7-b659-15e7d1f5bc6a.htm) | Can't put Corner Mullion at end joined to non-Curtain Wall. |
| Public property Static member | [AllGridSegmentsRemoved](cf2be07a-fd1e-0963-6c70-4b7cc3a1d169.htm) | Curtain grid lines must have at least one segment. |
| Public property Static member | [CannotApplyGridSpecification](c395b525-ac89-eeff-f8f9-563696385fa9.htm) | It is not possible to apply the host family's grid specification to this instance. |
| Public property Static member | [CannotDivideCurtainGrid](83f2b024-78ad-2f9f-6d17-0e0d33061010.htm) | Can't divide Curtain Grid by Grid Line. |
| Public property Static member | [CannotGroupCurtainGridHost](1f8a1286-40fe-e825-7656-c2f37810d949.htm) | Curtain grid based elements cannot be grouped. |
| Public property Static member | [CannotHaveIndependentOverlappingGrids](3f02ab20-256e-31e8-f283-fba52ae70e53.htm) | Overlapping independent type associated gridlines are not allowed. |
| Public property Static member | [CannotPlaceSplitMullions](427acb7e-d7c1-81e7-d45d-83d8baad21bb.htm) | Could not determine how to place the highlighted mullions after the wall was split. |
| Public property Static member | [CannotSplitOldMullions](3a555f5f-3a8d-ab45-395e-8bdd8a5d40e8.htm) | Split does not work on curtain walls containing mullions created in Revit prior to version 4.0. You may delete the mullions, place them again, and then proceed with splitting the wall. |
| Public property Static member | [CannotSwitchToCurtainWall](b54800f2-6979-8a80-80cc-3b1bae28831b.htm) | Can't switch type to Curtain Wall after Edit Elevation Profile. |
| Public property Static member | [CannotUseCornerMullion](489b61fb-2664-a298-8078-605a196d9e34.htm) | Corner Mullions must be placed at a location that can have neighboring Panels that are not tangent. With the exception of Wall Join locations, Corner Mullions are not currently supported on the external boundaries of Curtain elements. |
| Public property Static member | [CurtainGridFaceCannotBeReparamForGridRotation](15c228bb-051f-9f3c-216b-dc8826b578b4.htm) | Curtain grids cannot be rotated exactly as requested. Push "Adjust Grids" to get the nearest valid rotation. |
| Public property Static member | [CurtainGridOffHost](e15d5350-573e-9dd3-c444-2552597efa45.htm) | Curtain grid has left its host. |
| Public property Static member | [CurtainSystemHostInvisible](709d37cc-3a03-7acd-26cd-9906ae318371.htm) | Element defining the Curtain System is invisible in the current view. |
| Public property Static member | [DanglingCurtainWallCorner](e891b828-d356-7b55-3725-9d6799287771.htm) | A Corner Mullion has been placed at the end of a Curtain Wall that is not joined to another Curtain Wall. The angle of the Corner Mullion will default to 90 degrees. |
| Public property Static member | [DeletingCurtainSystemFaceGridLines](ae8245be-b61e-49e5-18da-5817928c5e30.htm) | Deleting Grid Lines residing on faces that no longer are part of a Curtain System. |
| Public property Static member | [DependentGridlineMayBeDeleted](17799f50-6032-1bd2-add8-f526a8959102.htm) | Type generated gridlines will become non-associated due to changes in the type. Press delete if you wish to remove them instead. |
| Public property Static member | [ExceedMaxDrivenGridlines](bdf311ea-38d9-7543-0f80-7bef44da4e91.htm) | Changes have been made that cause a curtain wall with type driven grid lines to exceed the maximum allowed number of type driven lines (200 in direction (1) and 200 in direction (2)). If you really need this many type driven grid lines, please split the affected wall before proceeding. |
| Public property Static member | [ExessiveBeltDistance](8b20a18b-a810-6fc8-afd5-f35b650dc3fa.htm) | The requested Measurement Line Offset would place the put the Measurement Line of the face boundaries. |
| Public property Static member | [GridlinesOutOfBounds](1f9d6bc6-5a36-52d8-23b9-f24ed897613f.htm) | Manually placed curtain grid lines are on the wall edges or outside the wall boundaries. |
| Public property Static member | [GridlinesOutOfBoundsWarn](04122bd2-195a-44b4-4e2f-e3ff6bc99984.htm) | Manually placed curtain grid lines are on the wall edges or outside the wall boundaries. |
| Public property Static member | [GridlinesOutsideWillBeRedependent](d9e1e49b-89ee-d0c8-8036-43d5e43138d8.htm) | Type associated curtain grid lines outside of the edited wall boundaries will be made dependent again in order that they remain on the wall. |
| Public property Static member | [GridlinesOverlap](ce1d3f12-bc14-ed2f-262b-8021e9522432.htm) | Overlapping gridlines should be avoided, unless there are only two and one is host type dependent and the other is not. |
| Public property Static member | [GridlinesWerePushed](4e085ac4-4e7e-072c-b9ef-52a07fc9ec7c.htm) | Panels and mullions created by a curtain grid were created with slight inaccuracies. |
| Public property Static member | [GridOutOfOrder](0bbd2076-5980-acff-0a17-eb4c0bcf203d.htm) | Curtain wall grid lines have changed order. |
| Public property Static member | [GridOutOfOrderError](2ea2531d-dfd0-a899-9aa8-6426e3c7f928.htm) | Curtain wall grid lines have changed order. |
| Public property Static member | [GridOutsideWall](06c715b9-3ce6-d927-56e2-548ef0c34762.htm) | Curtain wall grid lines are outside wall. If you are trying to shorten the wall, please remove grid lines, including mullions on top of them. |
| Public property Static member | [InvalidSkipSegments](ef0a2495-3ca7-aae9-b637-33e6701c974d.htm) | A curtain grid line had invalid removed segment data. When correcting data, Revit may have split curtain panels that should be combined. |
| Public property Static member | [MullionLostRefReorder](6bead2ba-5e80-27e3-efa9-150c84a6cea1.htm) | Mullions have lost references as a result of gridlines changing order. These mullions must be deleted. |
| Public property Static member | [MullionsWillBeDeleted](e4a9c6af-46bc-3bec-6b9c-d62d077cb51e.htm) | The Mullions between the Panels being joined will be deleted. |
| Public property Static member | [MultipleDominatingMullions](3fa90830-f434-d5f7-caea-55ad8583fb0c.htm) | Multiple dominating mullions on a grid face may cause ambiguous automatic adjustment of margins. |
| Public property Static member | [MultipleIdsInCurtainSystem](be6e2c31-7b9c-5487-0e7d-8323dcc7e030.htm) | A Curtain System cannot be based on faces from multiple elements. |
| Public property Static member | [MustReplacePanels](0a94dad4-55d7-fa94-45df-022ce30b9805.htm) | Missing Curtain Panels will be replaced with System Panels to complete command. |
| Public property Static member | [NegativeBeltDistance](cc9fca51-0b1b-da5a-1a6e-4f40cdac47f2.htm) | Measurement Line Offset cannot be negative. |
| Public property Static member | [NonSupportedCurtainWall](e2ac28bf-79ee-4b86-161f-dc98413ad32e.htm) | Currently, only straight Walls with straight or arc edges are supported for non-rectangular Curtain Walls. |
| Public property Static member | [NoPanelsLoaded](4ab0805f-998b-2f5f-1ee0-011f71a27d62.htm) | No Curtain Panel Families loaded. Can't make arced Curtain Wall. |
| Public property Static member | [RequestOrphanMullionDeletion](cd1f2826-b53e-3af7-1623-4c6e4ceb5776.htm) | Due to the changes in parameters of their hosts some mullions became non-type driven. |
| Public property Static member | [RuledCurtainElementLostCurves](6ae248fa-e4d9-3c59-8499-ac7a342c11dc.htm) | Ruled Curtain System cannot be built. The Lines or Edges used to create it cannot be found. |
| Public property Static member | [TypePanelsFronNonRectCellsUnlocked](14ce6ee2-999d-0221-c008-725016fc6de4.htm) | Loaded family curtain panels cannot be used in non-rectangular cells of the curtain host. Type-driven panels from non-rectangular cells were unlocked and left unchanged. |

# See Also

[BuiltInFailures CurtainWallFailures Class](a3d691c9-5f8f-29ca-cfad-fa1d1d66f203.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)