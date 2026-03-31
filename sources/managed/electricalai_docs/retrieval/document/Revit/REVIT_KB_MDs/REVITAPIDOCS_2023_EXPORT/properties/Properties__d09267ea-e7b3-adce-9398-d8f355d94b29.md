[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.ElectricalFailures Members

---



|  |
| --- |
| [BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in FailureDefinitionId instances.

The  [BuiltInFailures ElectricalFailures](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)  type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [AllSlotsOnPanelOccupied](89aa230b-4890-0506-21f5-6d4d59e0e9f8.htm) | All slots on panel: [Panel Name] are occupied. Some circuits will be disconnected from this panel. |
| Public property Static member | [BankDistanceSmallerThanDiameter](c863bca0-0dbc-d24d-044f-d1dafe2947db.htm) | The distance value is smaller than the conduit diameter, please enter a larger value |
| Public property Static member | [CableTrayModified](db9ab6cb-e139-a669-b919-dbb7eae97ed3.htm) | The cable tray has been modified to be in the opposite direction or insufficient space to create the required fittings. |
| Public property Static member | [CannotAddMorePolesToCircuit](6a467701-f6b7-a71d-eba4-3b7c41f4687a.htm) | Empty slots are unavailable to hold the number of poles you specified for this spare. \nTo add more poles to this spare, you must free up slots by moving the circuits below the spare. |
| Public property Static member | [CannotAssignSecondaryDistSysToCircuit](0b4a1f92-32dd-6405-fff4-349d09deadd7.htm) | Cannot assign or add [Element] to Circuit. There is no assigned secondary distribution system for [Element]. |
| Public property Static member | [CannotConnectDifferentDesignOptsObjects](32976c85-58dd-f9ee-96b7-e3a749cf197b.htm) | Cannot add or assign [Element] to circuit. Electrical objects belonging to different design options cannot be connected. |
| Public property Static member | [CannotCreatePanelScheduleDuetoNoDefaultTemplate](8f6d9011-785e-c07f-ad20-90997dc67a08.htm) | A panel schedule cannot be created for these panels. A default panel schedule template must be assigned for this template type. |
| Public property Static member | [CannotRemoveMembersInCircuitHavingParent](39dabe1e-fbcc-273d-a537-1c47f0fd82fe.htm) | You have selected elements that are connected to a Panel object in a Circuit. These elements cannot be removed from the Circuit. |
| Public property Static member | [CircuitOverload](289e61f4-9ac7-f454-7544-f5bd100dec76.htm) | Total connected load for Circuit [Name] is exceeding 80% of the defined rating ([Rating Value]). |
| Public property Static member | [CircuitsOverlapAndDeleteSpareSpace](632ebbe4-9834-856b-da8a-e5c855afb1ec.htm) | More than one Spare/Space falls onto the same slot. These Spares/Spaces will be deleted. |
| Public property Static member | [CircuitsOverlapDisconnectCircuits](deb53a0e-21d3-fa0c-6a08-155b7940b69e.htm) | More than one circuit falls onto the same slot. These circuits will be disconnected. |
| Public property Static member | [ConduitModified](734b7d6c-f47d-a081-4f80-c7e582807362.htm) | The conduit has been modified to be in the opposite direction or insufficient space to create the required fittings. |
| Public property Static member | [ElementsBelongToOtherCircuit](f6dcfbeb-8567-9284-3725-f06c7a2295ab.htm) | You have selected elements that are already part of other Circuits that have assigned Panels. The elements you selected cannot be added to this Circuit. |
| Public property Static member | [FamilyMismatchCircuit](9de8112c-21dc-122e-f9c2-89e57556c374.htm) | The family no longer matches the properties for the Circuit. Disconnect the family from the Circuit? |
| Public property Static member | [FeedThroughLugsIsDisabled](45a6ab8a-f9b2-bcd2-f594-691228dee6e7.htm) | The feed through lugs option is unchecked. |
| Public property Static member | [FeedThroughLugsIsNotEnabledAndBindFormulaInFamily](0c8f369e-06dc-081e-1148-5ae85558fbbc.htm) | Can't change connection type to Feed Through Lugs because Feed Through Lugs is unchecked. Enable Feed Through Lugs with related formula in family editor the Feed Through Lugs is mapped to. Select the panel -> Edit Family -> Family Types. |
| Public property Static member | [FeedThroughLugsIsNotEnabledAndBindGlobalParam](26a580bb-9d70-75e8-8cf3-3c46882e797c.htm) | Can't change connection type to Feed Through Lugs because Feed Through Lugs is not enabled. Enable Feed Through Lugs by enabling the global parameter that Feed Through Lugs is mapping. Click Manage tab -> Settings panel -> Global Parameters. |
| Public property Static member | [FeedThroughLugsIsOccupied](34cc2ad3-6171-5c98-18c2-2794602c3e75.htm) | The feed through lugs is in use by circuit [Element]. |
| Public property Static member | [FeedThroughLugsIsOccupiedAndDisconnectOtherCircuits](7559f1e1-a53b-3350-e1b8-56664d7ce6c7.htm) | The feed through lugs is occupied, so other circuits connected with feed through lugs will be disconnected from this panel [Panel Name]. |
| Public property Static member | [InvalidApparentPowerDensity](5997daf3-d704-ffeb-da55-4ed2b863b56b.htm) | The Apparent Power Density is invalid. Edit the Power Density and/or Power Factor to recalculate the Apparent Power Density. |
| Public property Static member | [InvalidNumberOfCircuitValueForSwitchPanel](b43b73b5-4036-d45c-39e7-93d818d8fb95.htm) | The number of circuits on the switchboard currently exceeds the value you entered. Reduce the number of circuits on the equipment before changing this value. |
| Public property Static member | [InvalidNumwiresSinglephase](f11c5862-7920-3eef-dc71-e25a00a0b8f3.htm) | Invalid number of wires for single phase, only 2 and 3 are valid. |
| Public property Static member | [InvalidPathOfParallelConduits](224931c4-3ca7-2edf-0bc1-5acd93da848f.htm) | Invalid path of parallel conduits |
| Public property Static member | [InvalidSpareSpace](171a9fb5-cfd3-002d-d6b1-d677e49212b5.htm) | The number of poles for a spare/space in a single phase, [wire] wires panel cannot exceed [value]. |
| Public property Static member | [MaximumNumberOfPolesExceeded](16fdfe1d-f3c8-7b82-e579-1fc3e5bca558.htm) | You cannot add more poles to this spare, as doing so would exceed the maximum number of poles set for this equipment. |
| Public property Static member | [MismatchConnectorDistSysToCircuit](c967c7ac-0a2f-0a67-9225-bf368ca2ae32.htm) | Cannot add [Element] to Circuit. The Type for the available connector does not match the Type ([Name]) for the Circuit. |
| Public property Static member | [MismatchNmbAssignedDistSysToCircuit](3da20906-2027-58df-e1fd-a62b1d45d9e3.htm) | Cannot assign or add [Element] to Circuit. There is no assigned distribution system for [Element]. |
| Public property Static member | [MismatchNmbOfPolesToCircuit](b77c9987-cf7a-6c29-f0e7-ecfa22fadbf0.htm) | Cannot add [Element] to Circuit. The Number of Poles for [Element] does not match the Number of Poles ([Name]) for the Circuit. |
| Public property Static member | [MismatchPoleBrakesSlotsNumbers](918a0394-a98f-f920-1756-98fe9ac4a9db.htm) | The number of pole breakers may not be less than the number of occupied slots. |
| Public property Static member | [MismatchVoltageLineToLine](04d6c173-8ab7-dab8-78a8-cd6fc28303f8.htm) | Cannot assign or add [Element] to Circuit. The Voltage ([Voltage Value]) for the Circuit is out of range for the Line to Line Voltage for [Element] (The Line to Line Voltage is specified in the assigned Distribution System). |
| Public property Static member | [MismatchVoltageToCircuit](d1627fab-fd26-d130-c9b4-e4a9567c170b.htm) | Cannot add [Element] to Circuit. The Voltage for [Element] is out of range for the Voltage ([Voltage Value]) for the Circuit. |
| Public property Static member | [MissingOrInvalidWireSizeTable](2d17bbc9-f6cb-089a-210a-157587da0636.htm) | Wire Size Table "[Fail Name]" is missing or invalid. Use Electrical Settings to select a valid Wire Size Table. |
| Public property Static member | [NoAvailableMatchingConnector](79cac0a7-c47c-724d-33f3-e7bc0b3af392.htm) | Cannot add [Element] to Circuit. There is no available connector matching the Type ([Type Name]) for the Circuit. |
| Public property Static member | [NotAllowedCableTrayConduitRotation](81cb7213-47eb-ce6f-cde9-38ce88dcad75.htm) | Don't allow to rotate a horizontal cable tray/conduit like this |
| Public property Static member | [NotEnoughAvailSlotsAndLugsOnPanel](c6e9395d-c554-0ab6-c74e-5cc62cc25d14.htm) | You can't connect to panel [Panel Name] because there aren't enough slots and Feed Through Lugs is occupied. \nYou can increase the [ParameterName] to be greater than [Number] to connect through breaker slots or you can disconnect existing Feed Through Lugs connection. |
| Public property Static member | [NotEnoughAvailSlotsAndLugsOnSwitchPanel](a6d96738-ee1f-b83c-9216-9ef42f490b1c.htm) | You can't connect to switchboard [Panel Name] because there aren't enough space and circuit [Circuit Name] is set to Feed Through Lugs. \nYou can increase the number of circuits to be greater than [Number] to connect through breakers or you can disconnect circuit and select Feed Through Lugs again. |
| Public property Static member | [NotEnoughAvailSlotsOnPanel](592744db-773f-36e5-e5b6-63ec6fab970d.htm) | You can't change the connection type to Breakers connect to panel [Panel Name] because there aren't enough slots. \nYou can increase the [ParameterName] to be greater than [Number] to connect through breaker slots or open the panel schedule and manually reshuffle non - consecutive slots. |
| Public property Static member | [NotEnoughRoomForParallelConduits](6e3bfe2b-f8b1-3f49-3257-5ebf1c79427a.htm) | Due to changes in elevation, there is not enough room to generate all of the parallel conduits. As a result, some conduit segments have not been generated. |
| Public property Static member | [NotEnoughRoomForParallelPipes](fcfa13ce-0cbc-5dfc-752c-0464e76cd9f3.htm) | Due to changes in elevation, there is not enough room to generate all of the parallel pipes. As a result, some pipe segments have not been generated. |
| Public property Static member | [NotEnoughSlotsOnlyLugAvailable](d9089382-a0fb-ba6d-0526-69bcf5361f54.htm) | There aren't enough slots on panel [Panel Name], so the circuit will connect through Feed Through Lugs. |
| Public property Static member | [NotEnoughSlotsOnlyLugAvailableForSwitchPanel](08f088c1-0942-416f-6f29-f11a65065f20.htm) | There aren't enough space on switchboard [Panel Name], so the circuit will connect through Feed Through Lugs. |
| Public property Static member | [NotPositiveBendRadius](be1d3bdf-58c9-a978-5e87-119ca6f2239e.htm) | The value you entered for the bend radius is zero or a negative value. Enter a positive value. |
| Public property Static member | [NotSupportConcentricBend](73d4c2f4-93f9-e3ab-45fe-0319e73dc4fd.htm) | Conduit with Fittings do not support Concentric Bend Radius, the bend radius of the conduit fittings will be same. |
| Public property Static member | [NumberOfCircuitFullOnSwitchPanel](cffe6141-6232-dd6d-d319-650e80b83b57.htm) | You can't change the connection type to Breakers and connect to switchboard [Panel Name] because there aren't enough space. \nYou can increase the number of circuits to be greater than [Number] to connect through breakers. |
| Public property Static member | [ObjsDemolished](136447dc-2cb2-4f22-0483-8b956e5c78a2.htm) | Cannot assign [Element] to circuit. Objects that are demolished cannot be added to a circuit. |
| Public property Static member | [PanelMismatchCircuitType](0bc392e0-5945-8558-fd80-981978fedfa2.htm) | Cannot assign [Element] to Circuit. The Type for the panel does not match the Type ([Name]) for the Circuit. |
| Public property Static member | [PanelMismatchDistSysWhenCircuitAssigned](03e28341-f219-8090-b3cf-df6ce44b3e47.htm) | The selected circuit was added to panel [Element], but the distribution system for the panel does not match the power connector definition on the panel. |
| Public property Static member | [SelectedElementsArePartOfOtherCircuit](8ffe87b6-1fcc-c499-b46d-9c7e2f15137a.htm) | You have selected elements that are already part of other Circuits. They will be removed from the original Circuits and added to this one. |
| Public property Static member | [SmallBendRadius](ffcfd393-0908-0b03-3033-9784ea08a785.htm) | The value you entered for the bend radius for conduit is too small. Enter a larger value. |
| Public property Static member | [UnsignedCircuit](2a2ad6a4-47af-a2d5-1bb4-84c38f9dcf27.htm) | Circuit is not assigned to a panel |
| Public property Static member | [VoltageIsOutOfRange](3a161382-e2bc-e5af-09fb-494107f37b47.htm) | Cannot assign or add [Element] to Circuit. The Voltage ([Voltage Value]) for the Circuit is out of range for the Line to Ground Voltage for [Element] (The Line to Ground Voltage is specified in the assigned Distribution System)." |
| Public property Static member | [WireMaxSizeNonexistent](b2dc7c0d-7e76-d58d-b792-d12f4f65bb22.htm) | Cannot find max size in current wire type's material table. |

# See Also

[BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)