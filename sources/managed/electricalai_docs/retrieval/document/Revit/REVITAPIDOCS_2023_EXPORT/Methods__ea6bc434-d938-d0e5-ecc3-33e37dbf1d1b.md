[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyInstance Members

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddCoping](a0fc20d1-36fc-a230-d41f-f7163184d328.htm) | Adds a coping (cut) to a steel beam. |
| Public method | [ArePhasesModifiable](329b02eb-5ee4-1715-2fbf-2cbbc0d3ff2a.htm) | Returns true if the properties CreatedPhaseId and DemolishedPhaseId can be modified for this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanBeHidden](887010c4-de58-96b6-0931-4c226e6b142b.htm) | Indicates if the element can be hidden in the view. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanBeLocked](5ef8834b-168d-02ac-2f29-5d43f5da87f2.htm) | Identifies if the element can be locked. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanDeleteSubelement](c9795398-2d2c-db8e-a4e7-ca99d69fcc1d.htm) | Checks if given subelement can be removed from the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanHaveTypeAssigned](051e2945-b690-5387-d083-7cdb7cb75332.htm) | Identifies if the element can have a type assigned. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [ChangeTypeId(ElementId)](479b5d94-abd3-db42-27d7-6a3eda12f285.htm) | Changes the type of the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [DeleteEntity](ef0fa7d8-8152-6300-285d-1c0cdc08e5a7.htm) | Deletes the existing entity created by %schema% in the element (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [DeleteSubelement](de199938-feea-7437-c19f-162714b70dcd.htm) | Removes a subelement from the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [DeleteSubelements](6410b135-88fe-b111-769f-f14e86b42a05.htm) | Removes the subelements from the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [Dispose](e3b07ee4-f500-1b95-c786-8984289a5143.htm) | (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [flipFacing](66eb8785-4225-509c-b6a3-0bf9fe1612b2.htm) | The orientation of family instance facing will be flipped. If it can not be flipped, return false, otherwise return true. |
| Public method | [FlipFromToRoom](ae1158c1-1fb0-0558-0ea4-e1cf76bb8a1e.htm) | Flips the settings of "From Room" and "To Room" for the door or window instance. |
| Public method | [flipHand](c31b55a1-ce2e-a86c-ede0-21a883e7d4e4.htm) | The orientation of family instance hand will be flipped. If it can not be flipped, return false, otherwise return true. |
| Public method | [GetCopingIds](6886b519-4a44-373f-59ab-4ceee51dd096.htm) | Lists the elements currently used as coping cutters for this element. |
| Public method | [GetDependentElements](56e875d3-014b-a996-69c3-e6ed9b885f5c.htm) | Get all elements that, from a logical point of view, are the children of this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetEntity](09d80bf1-c1d0-aa2e-4f18-e5a5e9c9d93f.htm) | Returns the existing entity corresponding to the Schema if it has been saved in the Element, or an invalid entity otherwise. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetEntitySchemaGuids](742313cb-1bea-f873-e5ca-1bfac782286b.htm) | Returns the Schema guids of any Entities stored in this element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalFileReference](e784fb6e-94f4-09bd-1f9c-17e6968e18a5.htm) | Gets information pertaining to the external file referenced by the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalResourceReference](fb4b9493-1d7b-5387-c171-2078225183ca.htm) | Gets the ExternalResourceReference associated with a specified external resource type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalResourceReferenceExpanded](1a28171e-8460-d849-4e7d-9a306a22cd6e.htm) | Gets the collection of ExternalResourceReference associated with a specified external resource type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalResourceReferences](7df4341b-5102-8016-d6fa-45bc27e8c3af.htm) | Gets the map of the external resource references referenced by the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalResourceReferencesExpanded](954cb21e-5c4e-1e52-7e35-1eb0ed4b050b.htm) | Gets the expanded map of the external resource references referenced by the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetFamilyPointPlacementReferences](59db15da-7e87-a85f-bacf-e8a636d17022.htm) | Returns the Point Placement References for the Family Instance. |
| Public method | [GetGeneratingElementIds](112590d2-de20-dd1f-ae05-df7dfb3b410f.htm) | Returns the ids of the element(s) that generated the input geometry object. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetGeometryObjectFromReference](536b3d7a-ec8d-29f6-5957-751468c98dd0.htm) | Retrieve one geometric primitive contained in the element given a reference. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetMaterialArea](02417c40-bcc4-f04c-9897-cf47737e8739.htm) | Gets the area of the material with the given id. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMaterialIds](6011352e-151b-b8ac-14cc-45970f2fe5ad.htm) | Gets the element ids of all materials present in the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMaterialVolume](99b50d87-bfa6-ca67-e205-47b22cad6587.htm) | Gets the volume of the material with the given id. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMonitoredLinkElementIds](42b25291-f1b9-d240-c876-1b53f24f60e0.htm) | Provides the link instance IDs when the element is monitoring. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMonitoredLocalElementIds](47ca1e8c-f79d-a18b-505b-73a4358d2264.htm) | Provides the local element IDs when the element is monitoring. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetOrderedParameters](4bf4c0da-f841-0943-f9e0-246a666c1775.htm) | Gets the parameters associated to the element in order. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetOriginalGeometry](d28a0880-bff8-1acc-ddf1-ce3205f2e8b3.htm) | Returns the original geometry of the instance, before the instance is modified by joins, cuts, coping, extensions, or other post-processing. |
| Public method | [GetParameter](fc4e5245-d2e5-e31d-a6e3-177106e75e10.htm) | Retrieves a parameter from the element given identifier. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetParameterFormatOptions](476c8179-f938-d047-db7c-776cf7e2929c.htm) | Returns a FormatOptions override for the element Parameter, or a default FormatOptions if no override exists. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetParameters](0cf342ef-c64f-b0b7-cbec-da8f3428a7dc.htm) | Retrieves the parameters from the element via the given name. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetPhaseStatus](eedf5981-b5e2-dda7-cb5e-01a4d4fc7f6c.htm) | Gets the status of a given element in the input phase (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetReferenceByName](d44a95cc-f2c7-1fa9-9180-fefed6d70ed6.htm) | Gets the family instance reference corresponding to the named reference plane in the instance's family. |
| Public method | [GetReferenceName](aaf6b45c-9139-b984-b824-2888ca32a95a.htm) | Gets the name of the reference plane in the family corresponding to the given family instance reference. |
| Public method | [GetReferences](a8a7dc74-db8e-a7b6-a9c8-869397cca6b4.htm) | Gets family instance references corresponding to the reference planes or reference lines of the given reference type in the instance's family. |
| Public method | [GetReferenceType](0405fced-1ac6-a6a9-9f59-21eb81ca2241.htm) | Gets the type of the reference plane or reference line in the instance's family corresponding to the given family instance reference. |
| Public method | [GetSpatialElementCalculationPoint](433caf59-49b1-97df-38ac-8f01a620bef5.htm) | Gets the location of the calculation point for this instance. |
| Public method | [GetSpatialElementFromToCalculationPoints](21810873-d413-f6e4-ca33-d2ee4e93643e.htm) | Gets the locations for the calculation points for this instance. |
| Public method | [GetSubComponentIds](be37702c-1dcd-bc14-aa35-45f06f20210a.htm) | Gets the sub component ElementIds of the current family instance. |
| Public method | [GetSubelements](feabfd59-bd0f-ab61-34a1-d0d22f58c881.htm) | Returns the collection of element subelements. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetSweptProfile](9bc9e2db-5ef1-8264-1426-01f4a6081844.htm) | Gets the object that describes the profile that is swept along the driving curve for this instance. |
| Public method | [GetTotalTransform](8c8aff2b-5ff9-e43a-3b5c-308cd0174f1f.htm) | Gets the total transform, which includes the true north transform for instances like import instances. (Inherited from  [Instance](08603dd9-976d-a9fe-add7-2a8450b8006c.htm)  .) |
| Public method | [GetTransform](50aa275d-031e-ce19-9cfd-18a7a341ed19.htm) | Gets the transform of the instance. (Inherited from  [Instance](08603dd9-976d-a9fe-add7-2a8450b8006c.htm)  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [GetTypeId](cc66ca8e-302e-f072-edca-d847bcf14c86.htm) | Returns the identifier of this element's type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetValidTypes](086554ba-3c70-9c0f-8a09-55a4da4ef905.htm) | Obtains a set of types that are valid for this element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [HasModifiedGeometry](0f1f1713-8013-2f62-6e84-41749e1dcc95.htm) | Identifies if the geometry of this FamilyInstance has been modified from the automatically generated default. |
| Public method | [HasPhases](5d850f8a-4a50-406b-6c59-b85d49dcbb2e.htm) | Returns true if this Element has the properties CreatedPhaseId and DemolishedPhaseId. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [HasSweptProfile](dbbd4aa9-720b-3a1c-3085-7b94b6d73b58.htm) | Indicates if this instance can be represented as a swept profile. |
| Public method | [IsCreatedPhaseOrderValid](b2bcaf7f-c453-d6e2-fd85-083783e935f3.htm) | Returns true if createdPhaseId and demolishedPhaseId are in order. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsDemolishedPhaseOrderValid](46ec60b6-b1c5-25aa-c544-34379298c7b8.htm) | Returns true if createdPhaseId and demolishedPhaseId are in order. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsExternalFileReference](2bf6162f-0b0f-88cb-9c67-d4bd435537b5.htm) | Determines whether this Element represents an external file. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsHidden](2c3d4123-fded-cd5f-ed0d-12b1e1a3ce42.htm) | Identifies if the element has been permanently hidden in the view. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsMonitoringLinkElement](fde81756-5518-4924-c14e-f9ef2bb3fa6e.htm) | Indicate whether an element is monitoring any elements in any linked models. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsMonitoringLocalElement](9a41a87c-2b3b-b6ed-1743-98c002b20ce3.htm) | Indicate whether an element is monitoring other local elements. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsPhaseCreatedValid](ae48b10d-4a66-ee2c-85bf-f426435d0dbe.htm) | Returns true if createdPhaseId is an allowed value for the property CreatedPhaseId in this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsPhaseDemolishedValid](f97c9af7-fcbe-f617-d7ff-cfd4fb5af37f.htm) | Returns true if demolishedPhaseId is an allowed value for the property DemolishedPhaseId in this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsValidType(ElementId)](c3ca4ee5-c2b3-beb3-ee51-cc6cafc82c93.htm) | Checks if given type is valid for this element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [LookupParameter](4400b9f8-3787-0947-5113-2522ff5e5de2.htm) | Attempts to find a parameter on the element which has the given name. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [RefersToExternalResourceReference](0a4aabb3-f684-0800-7bf5-31540831593f.htm) | Determines whether this Element uses external resources associated with a specified external resource type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [RefersToExternalResourceReferences](387c00cd-3932-76e6-152b-bfe4efb8fbc1.htm) | Determines whether this Element uses external resources. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [RemoveCoping](c0ccd04c-f952-011f-4b0f-25862792d619.htm) | Removes a coping (cut) from a steel beam. |
| Public method | [rotate](634dc711-7d00-a176-9c61-c53c27c89849.htm) | The family instance will be flipped by 180 degrees. If it can not be rotated, return false, otherwise return true. |
| Public method | [SetCopingIds](751280c8-4507-4837-add9-f6a83a1997fe.htm) | Specifies the set of coping cutters on this element. |
| Public method | [SetEntity](e90c01ab-3d2f-2f46-3e88-8297e686dc80.htm) | Stores the entity in the element. If an Entity described by the same Schema already exists, it is overwritten. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [Split](8f32a065-ba3c-79c7-8141-63183b4cdece.htm) | Splits the family instance element at a point on its defining curve. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AssemblyInstanceId](83989f69-1aca-1a49-9647-e57bc2d58b21.htm) | The id of the assembly instance to which the element belongs. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [BoundingBox](def2f9f2-b23a-bcea-43a3-e6de41b014c8.htm) | Retrieves a box that circumscribes all geometry of the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [CanFlipFacing](13991f6f-3eab-0efc-8d9d-c30bfc9b1ae5.htm) | Property to test whether the orientation of family instance facing can be flipped. |
| Public property | [CanFlipHand](dc405f3d-888f-2831-c14a-4ffc315795d7.htm) | Property to test whether the orientation of family instance hand can be flipped. |
| Public property | [CanFlipWorkPlane](b108f031-40e0-bb91-6408-69c4d045db5a.htm) | Identifies if the instance can flip its work plane. |
| Public property | [CanRotate](36f8d40d-6322-1cb8-a5e2-2215da9ce45e.htm) | Property to test whether the family instance can be rotated by 180 degrees. |
| Public property | [CanSplit](a5075af4-0664-ed10-8303-665f0024c30a.htm) | Identifies whether a particular family instance can be split at a point on it's defining curve (by  [Split(Double)](8f32a065-ba3c-79c7-8141-63183b4cdece.htm)  ). |
| Public property | [Category](8990bd36-af08-fc99-496b-f94fcb056b21.htm) | Retrieves a Category object that represents the category or sub category in which the element resides. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [CreatedPhaseId](c6032e01-f7cb-b2ea-3312-697d14216a31.htm) | Id of a Phase at which the Element was created. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [DemolishedPhaseId](7949a983-c5dc-62a3-594a-d685365449d5.htm) | Id of a Phase at which the Element was demolished. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [DesignOption](5c20fe58-e301-6ddb-3438-666db5c586ee.htm) | Returns the design option to which the element belongs. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Document](9e530d25-61ca-3899-a531-cbcfd994358d.htm) | Returns the Document in which the Element resides. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [ExtensionUtility](2ff87911-3c17-babc-781d-e2c68e62d4e9.htm) | Property to check whether the instance can be extended and return the interface for extension operation. |
| Public property | [FacingFlipped](85483f11-1f76-594b-d1cc-6acf8f4fc368.htm) | Property to test whether the orientation of family instance facing is flipped. |
| Public property | [FacingOrientation](989288ad-d81c-9ee6-4351-21daf93d9cf0.htm) | Property to get the orientation of family instance facing. |
| Public property | [FromRoom](d6658841-da29-ead4-049b-3036cbd4951a.htm) | The "From Room" set for the door or window in the last phase of the project. |
| Public property | [FromRoom Phase](c4a37990-0603-50e0-ca97-1cd5449940dd.htm) |  |
| Public property | [Geometry](d8a55a5b-2a69-d5ab-3e1f-6cf1ee43c8ec.htm) | Retrieves the geometric representation of the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [GroupId](9508a6c5-9681-bbef-07c5-1351583b0e1e.htm) | The id of the group to which an element belongs. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [HandFlipped](7065faa0-00ac-93f1-427b-88496c53235e.htm) | Property to test whether the orientation of family instance hand is flipped. |
| Public property | [HandOrientation](a11ec72c-2498-aaea-4b2e-2adac454856c.htm) | Property to get the orientation of family instance hand. |
| Public property | [HasSpatialElementCalculationPoint](eb1b4c8b-8b8a-1247-4150-b5d55231363b.htm) | Identifies if this instance has a single SpatialElementCalculationPoint used as the search point for Revit to identify if the instance is inside a room or space. |
| Public property | [HasSpatialElementFromToCalculationPoints](eef2d8ce-6070-d666-b03d-480ef87d04a3.htm) | Identifies if this instance has a pair of SpatialElementCalculationPoints used as the search points for Revit to identify if the instance lies between up to two rooms or spaces. |
| Public property | [Host](69f30141-bd3b-8bdd-7a63-6353d4d495f9.htm) | If the instance is contained within another element, this property returns the containing element. An instance that is face hosted will return the element containing the face. |
| Public property | [HostFace](e795508b-bb6a-4f76-e282-57aa6f7074e5.htm) | Property to get the reference to the host face of family instance. |
| Public property | [HostParameter](bcf1a885-5015-0b87-dfe8-9109d499f4e7.htm) | If the instance is hosted by a wall, this property returns the parameter value of the insertion point of the instance along the wall's location curve, as long as the family of the instance isn't work plane based. |
| Public property | [Id](9235095b-b7ae-b6e5-6cc2-2b8d397644de.htm) | A unique identifier for an Element in an Autodesk Revit project. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Invisible](a60ebd06-8939-807f-9749-4510991bdff4.htm) | Property to test whether the family instance is invisible. |
| Public property | [IsModifiable](65f9f835-daaa-3efa-2976-3f932aa18366.htm) | Identifies if the element is modifiable. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [IsSlantedColumn](14ca80b4-8cc8-2af7-3a72-db734b51eb79.htm) | Indicates if the family instance is a slanted column. |
| Public property | [IsTransient](f391d235-555f-6651-99c6-895fc443f8d8.htm) | Indicates whether an element is transient or permanent. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [IsValidObject](0ffcf585-a39d-623c-9b5b-ab63c7bebfb6.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [IsWorkPlaneFlipped](33d135c3-d887-c574-a049-f8abdcb01ded.htm) | Identifies if the instance's work plane is flipped. |
| Public property | [LevelId](27033fe3-6740-61e3-be82-47a6b8ae77db.htm) | The id of the level associated with the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Location](847ff799-9b1b-0982-f55a-7273c55b196d.htm) | This property is used to find the physical location of an instance within project. (Overrides  [Element Location](89438f4f-7e15-835a-0c66-d6adbc8dd00c.htm)  .) |
| Public property | [MEPModel](34173003-db39-bfa9-fa59-f7b5ac8da794.htm) | Retrieves the MEP model for the family instance. |
| Public property | [Mirrored](20ab2f32-e3ca-8173-aac3-a03e998fd0ab.htm) | Property to test whether the family instance is mirrored. (only one axis is flipped) |
| Public property | [Name](e372092e-ff47-71c2-1272-50ab08e5a41d.htm) | A human readable name for the Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [OwnerViewId](174c1adf-0be8-a4b0-41f3-9e3ea1d6b1f1.htm) | The id of the view that owns the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameter Guid](2e852bc4-46c6-5598-cc45-0eaf38cf8973.htm) | Retrieves a parameter from the element given a GUID for a shared parameter. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameter BuiltInParameter](2f91a9f3-7f69-72f9-08d6-a2d71dfb33db.htm) | Retrieves a parameter from the element given a parameter id. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameter Definition](87d8a88c-906e-85a9-f575-f263788b8584.htm) | Retrieves a parameter from the element based on its definition. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameters](7af5d66f-4533-33d2-dd82-d9573eaabf15.htm) | Retrieves a set containing all of the parameters that are contained within the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [ParametersMap](82c45482-a018-32e4-d8e5-9751e10ffeb9.htm) | Retrieves a map containing all of the parameters that are contained within the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Pinned](c37bc7f9-409e-9b8a-f491-f700228985e2.htm) | Identifies if the element has been pinned to prevent changes. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Room](37944e7a-f298-9c25-20bb-9c0c1da46f41.htm) | The room in which the instance is located (during the last phase of the project). |
| Public property | [Room Phase](5c1ed572-e744-3ab6-9b10-bb258a66f23a.htm) |  |
| Public property | [Space](3c81b4e4-de4b-44df-8f80-d90c60976dec.htm) | The space in which the instance is located (during the last phase of the project). |
| Public property | [Space Phase](36fcee11-77d9-80a7-2321-5bf163137ac3.htm) |  |
| Public property | [StructuralMaterialId](856b95a1-38c9-4d61-59cd-2844f7348984.htm) | Identifies the material that defines the instance's structural analysis properties. |
| Public property | [StructuralMaterialType](042b7922-53d9-d0ee-2f57-ce32cf5c5e4e.htm) | This property returns the physical material from which the instance is made. |
| Public property | [StructuralType](5072fbf4-e8e5-21df-d92e-476104c1418c.htm) | Provides the primary structural type of the instance, such as beam or column etc. |
| Public property | [StructuralUsage](52fe2ab8-d038-df14-fb12-e4f9c036dd7d.htm) | Provides the primary structural usage of the instance, such as brace, girder etc. |
| Public property | [SuperComponent](1dcf3123-c2ea-867a-7b9a-73173343121e.htm) | Property to get the super component of current family instance. |
| Public property | [Symbol](4157fff5-cde3-cbb7-1df8-03f77d64712f.htm) | Returns or changes the FamilySymbol object that represents the type of the instance. |
| Public property | [ToRoom](939e9c7b-072a-7be9-105f-64e1aa1f3a97.htm) | The "To Room" set for the door or window in the last phase of the project. |
| Public property | [ToRoom Phase](94e34f74-b6d1-2e4b-df44-b93aac5543c6.htm) |  |
| Public property | [UniqueId](f9a9cb77-6913-6d41-ecf5-4398a24e8ff8.htm) | A stable unique identifier for an element within the document. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [VersionGuid](2a1eae53-2c5c-a7be-1ef2-0f48626c62f5.htm) | Get the element version Guid. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [ViewSpecific](785b351e-51cb-e3c6-cb91-f307c8e4ba73.htm) | Identifies if the element is owned by a view. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [WorksetId](4b45250a-7a07-a89a-0f63-cf8d142a7b93.htm) | Get Id of the Workset which owns the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)