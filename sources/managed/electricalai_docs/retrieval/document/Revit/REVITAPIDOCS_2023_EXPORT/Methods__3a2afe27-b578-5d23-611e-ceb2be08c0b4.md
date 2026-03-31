[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarConstraint Members

---



|  |
| --- |
| [RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [RebarConstraint](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AreGeometryTargetsTheSame](841c02b2-e2c6-d55c-d4e1-9f1d1d7339a2.htm) | Returns true if the gemetrical targets (ex. face references, other rebar segment references) of "this" constriant are the same as the targets of the "other" constraint. Returns false otherwise. Only the reference to the target piece of geometry is taken into account(ex. only face references, only other rebar segment references). Target Element (elementId) is not taken into account. Distance to target is not taken into account. |
| Public method | [ConstrainsRebarEnds](9d8dc518-0093-3aa8-dc50-26e85df9bf50.htm) | Returns true if this constraint constrains two rebar ends. |
| Public method Static member | [Create](dc2653ae-633a-a9ed-bf08-253c59e5bfd4.htm) | This method creates a constraint for a given Rebar Constrained Handle Tag. Will throw exception if used for Shape Driven Rebar. |
| Public method | [Dispose](b118907f-08c3-742d-01f4-e50db6d065f5.htm) | Releases all resources used by the  [RebarConstraint](748823c8-f059-68c1-d7b5-7cfaba93a445.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [FlipHandleOverTarget](0e5101f2-2ece-c720-ee63-13857754c0c6.htm) | Flips the RebarConstrainedHandle to the other side of the target bar handle, maintaining the distance in absolute value. |
| Public method | [GetConstraintType](5c90f541-5fa5-946b-4b4f-4126a29650f2.htm) | Returns the RebarConstraintType of a RebarConstraint. |
| Public method | [GetCustomHandleTag](019e2c30-c247-2d8a-476b-25be0f547dbb.htm) | Returns the handle tag of the RebarConstrainedHandle. This is valid only for Free Form Rebar. |
| Public method | [GetDistanceToTargetCover](927a9514-0182-1c40-2018-83de25737348.htm) | Returns the distance from the RebarConstrainedHandle to the target Host Cover Element surface. The RebarConstraintType of the RebarConstraint must be 'ToCover.' |
| Public method | [GetDistanceToTargetHostFace](9859e4a1-a5d4-a1e6-d28b-2e69799f2c10.htm) | Returns the distance from the RebarConstrainedHandle to the target Host Element surface. The RebarConstraintType of the RebarConstraint must be 'FixedDistanceToHostFace.' |
| Public method | [GetDistanceToTargetRebar](759f89cb-e28e-cb61-d667-8153e5c432d3.htm) | Gets the distance from the RebarConstrainedHandle to the target Rebar handle surface. The RebarConstraintType of the RebarConstraint must be 'ToOtherRebar.' |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetRebarConstraintTargetHostFaceType](6446870e-2774-3d2f-cb78-0cb39e7dada4.htm) | Returns the RebarConstraintTargetHostFaceType of the host Element face to which the RebarConstraint is attached. The RebarConstraintType of the RebarConstraint must be 'FixedDistanceToHostFace' or 'ToCover.' Will throw exception if it's a multi target constraint. |
| Public method | [GetRebarConstraintTargetHostFaceType(Int32)](f58fe52a-639f-8101-8c9d-fe2354a755d0.htm) | Returns the RebarConstraintTargetHostFaceType of the host Element face to which the RebarConstraint is attached. The RebarConstraintType of the RebarConstraint must be 'FixedDistanceToHostFace' or 'ToCover.' |
| Public method | [GetTargetCoverType](f5ef3d50-d753-2598-7a12-74cc1cb569fa.htm) | Returns the RebarCoverType for the face specified by targetIndex. Returns null if no RebarHostData is present for target element. |
| Public method | [GetTargetElement](75975a79-d608-9210-dbd7-0099a046fa3d.htm) | Gets the Element object (either Host or Rebar) which provides the constraint. Will throw exception if it's a multi target constraint. |
| Public method | [GetTargetElement(Int32)](f20b6107-6c40-860d-2445-4c2fcbde3f29.htm) | Gets the Element object (either Host or Rebar) which provides the constraint. Will return the Element which contains the face at targetIndex. |
| Public method | [GetTargetHostFaceAndTransform](26bfbda5-6121-a44a-b0fd-04533adda39b.htm) | Returns the face to which the RebarConstraint is attached associated to the given target index. The RebarConstraintType of the RebarConstraint must be 'FixedDistanceToHostFace' or 'ToCover.' |
| Public method | [GetTargetHostFaceReference](df4e4eca-c29a-faea-9bb8-26fd1ed12586.htm) | Returns a reference to the host Element face to which the RebarConstraint is attached. The RebarConstraintType of the RebarConstraint must be 'FixedDistanceToHostFace' or 'ToCover.' Will throw exception if it's a multi target constraint. |
| Public method | [GetTargetHostFaceReference(Int32)](8da5f062-8f8f-3151-e029-6492a3978a50.htm) | Returns a reference that corresponds to the face to which the RebarConstraint is attached specified by the targetIndex. The RebarConstraintType of the RebarConstraint must be 'FixedDistanceToHostFace' or 'ToCover.' |
| Public method | [GetTargetRebarAngleOnBarOrHookBend](737fce1f-9ce0-620a-702b-6c01505985c9.htm) | Returns the angular increment along a bar or hook bend to which the RebarConstraint is attached. |
| Public method | [GetTargetRebarBendNumber](134322bb-4c04-d211-bcda-905098f4068d.htm) | Returns the number of the bend on the other Rebar Element to which this RebarConstraint is attached. The RebarConstraint must be of RebarConstraintType 'ToOtherRebar,' and the TargetRebarConstraintType must be 'BarBend.' Rebar must be Shape Driven Rebar element. |
| Public method | [GetTargetRebarConstraintType](282c6cbe-06c7-8f56-e38c-6f8550655cf4.htm) | Returns the TargetRebarConstraintType of the handle on the other Rebar Element to which this RebarConstraint is attached. The RebarConstraintType of the RebarConstraint must be 'ToOtherRebar.' Rebar must be Shape Driven Rebar element. |
| Public method | [GetTargetRebarEdgeNumber](ba6652ad-cc66-349a-87d6-ee8460572791.htm) | Returns the number of the edge on the other Rebar Element to which this RebarConstraint is attached. The RebarConstraint must be of RebarConstraintType 'ToOtherRebar,' and the TargetRebarConstraintType must be 'Edge.' Rebar must be Shape Driven Rebar element. |
| Public method | [GetTargetRebarHookBarEnd](14d3ea55-2756-05de-b5f7-4a2793817099.htm) | Returns 0 or 1 to indicate which end hook on the other Rebar Element to which this RebarConstraint is attached. The RebarConstraint must be of RebarConstraintType 'ToOtherRebar,' and the TargetRebarConstraintType must be 'HookBend.' Rebar must be Shape Driven Rebar element. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [HasAnEdgeNumber](d8150a7f-a810-e4ae-ef8a-dc60545d00a2.htm) | Checks if the getTargetRebarEdgeNumber method can be called for the RebarConstraint. |
| Public method | [IsBindingHandleWithTarget](d51defb0-82be-ff30-c3c4-75eb86fa5bd0.htm) | Gets the relationship between two RebarConstrainedHandles. |
| Public method | [IsEqual](f2d5fb51-542c-6f74-d931-590c9d429e6b.htm) | Returns true if the specified RebarConstraint is the same as 'this.' The method can be used to determine which of the RebarConstraint candidates offered by the RebarConstraintsManager is currently active. |
| Public method | [IsFixedDistanceToHostFace](b81e57f3-802d-3fa9-2e0f-3ec2b26b48cb.htm) | Returns true if the RebarConstraintType of the RebarConstraint is 'FixedDistanceToHostFace.' |
| Public method | [IsReferenceValidForConstraint](728e9832-f292-212e-1579-a34d30954b32.htm) | Checks if the reference provided can be used in creating Rebar constraints |
| Public method | [IsToCover](1d0d12da-826f-cd73-89da-3f6c371331bd.htm) | Returns true if the RebarConstraintType of the RebarConstraint is 'ToCover.' |
| Public method | [IsToHostFaceOrCover](315e8a24-5a63-0310-758d-56420196880c.htm) | Returns true if the RebarConstraintType of the RebarConstraint is either 'FixedDistanceToHostFace' or 'ToCover.' |
| Public method | [IsToOtherRebar](e47bd358-176e-f4fa-40b4-43f1d6c0f4ba.htm) | Returns true if the RebarConstraintType of the RebarConstraint is 'ToOtherRebar.' |
| Public method | [IsUsingClearBarSpacing](13351019-9549-3a83-9d51-7b59d3dbe7bf.htm) | Returns true if the RebarConstrainedHandle to target offset is the clear bar distance, false if the offset is measured between bar centers. |
| Public method | [IsValid](8e6a4ccb-21db-1245-e361-a1341efa5f11.htm) | Checks that the RebarConstraint still has access to valid Rebar constraint data and that its RebarConstraintsManager is still valid. |
| Public method | [ReplaceReferenceTargets](a94d644d-49ce-9b5e-6068-6a6ffe547c29.htm) | Replaces the current set of references, the type of constraint and the offset value, with the newly provided ones. Will throw exception if this is a constraint for Shape Driven Rebar. |
| Public method | [SetDistanceToTargetCover](5c573cf3-7ff8-49a1-7b8e-f78fe2709ea8.htm) | Sets the distance from the RebarConstrainedHandle to the target Host Cover Element surface. The RebarConstraintType of the RebarConstraint must be 'ToCover.' |
| Public method | [SetDistanceToTargetHostFace](87771139-34dd-1135-026b-904e4098bdbc.htm) | Sets the distance from the RebarConstrainedHandle to the target Host Element surface. The RebarConstraintType of the RebarConstraint must be 'FixedDistanceToHostFace.' |
| Public method | [SetDistanceToTargetRebar](e605c253-b628-2db6-48f4-49f9506d4193.htm) | Sets the offset distance between the constrained RebarConstrainedHandle and its target Rebar handle surface. |
| Public method | [SetToBindHandleWithTarget](11d87c14-8f42-3f33-98d5-a03058eec1f4.htm) | Sets the relationship between two RebarConstrainedHandles. |
| Public method | [SetToUseClearBarSpacing](2e8fd543-a754-0c53-6812-e11b4c27f438.htm) | Sets whether the RebarConstrainedHandle to target offset is the clear bar distance, or is measured between bar centers. |
| Public method | [TargetIsBarBend](dea5e5f2-781d-d274-1e4f-fd762cdb48df.htm) | Returns true if the RebarTargetConstraintType of the RebarConstraint is 'BarBend'. |
| Public method | [TargetIsHookBend](fa6154ad-8803-451c-498a-d762ea9f51e8.htm) | Returns true if the RebarTargetConstraintType of the RebarConstraint is 'HookBend'. |
| Public method | [TargetRebarConstraintTypeIsEdge](c9018a04-ebe1-3214-9e4b-7853a79be53c.htm) | Returns true if the RebarConstraintType of the RebarConstraint is 'ToOtherRebar,' and the RebarConstraint is attached to an edge of the other Rebar Element. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](a575e7e8-f425-1295-ec8b-5d8a8b66c56d.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [NumberOfTargets](4c6f7b2a-f0a3-02e1-9927-d635b4aeb8b2.htm) | Identifies the number of references associated to the rebar handle. |

# See Also

[RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)