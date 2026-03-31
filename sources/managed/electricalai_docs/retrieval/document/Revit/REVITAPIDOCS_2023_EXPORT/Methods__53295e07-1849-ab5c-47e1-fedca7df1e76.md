[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DirectShapeType Members

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [DirectShapeType](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddExternallyTaggedGeometry](39c80387-f1ef-b57c-67d1-0231d0ec5068.htm) | Adds the externally tagged geometry object to the DirectShapeType. |
| Public method | [AddReferenceCurve(Curve)](7ea1eedd-87bb-e0db-306c-756c14edfa0b.htm) | Adds a reference curve to the DirectShapeType. |
| Public method | [AddReferenceCurve(Curve, DirectShapeReferenceOptions)](831bc964-0d8f-6db2-6e70-12306c8ef744.htm) | Adds a reference curve to the DirectShapeType. |
| Public method | [AddReferencePlane(Plane)](bdc6e714-a2ab-8a33-95be-657ebb217157.htm) | Adds a reference plane to the DirectShapeType. The reference plane can either be bounded or unbounded. |
| Public method | [AddReferencePlane(Plane, BoundingBoxUV)](0861063f-2f61-cce9-9954-3f8b8606b4bb.htm) | Adds a reference plane to the DirectShapeType. The reference plane can either be bounded or unbounded. |
| Public method | [AddReferencePlane(Plane, DirectShapeReferenceOptions)](1657e034-4bde-914e-35c7-e928d81a1e77.htm) | Adds a reference plane to the DirectShapeType. The reference plane can either be bounded or unbounded. |
| Public method | [AddReferencePlane(Plane, BoundingBoxUV, DirectShapeReferenceOptions)](89bc8899-38bf-f736-fb5c-f3b8ad4c281f.htm) | Adds a reference plane to the DirectShapeType. The reference plane can either be bounded or unbounded. |
| Public method | [AddReferencePoint(XYZ)](f9ba1808-1a7e-c8c4-6ed8-deb4b34b85b2.htm) | Adds a reference point to the DirectShapeType. |
| Public method | [AddReferencePoint(XYZ, DirectShapeReferenceOptions)](f97bae0e-e1fb-76f3-0b8e-868e82a87ac3.htm) | Adds a reference point to the DirectShapeType. |
| Public method | [AppendShape(IList GeometryObject )](4cbd4a0c-f9a2-3cb1-fa4d-0a9244f25ef2.htm) | Appends the collection of GeometryObjects into the model shape representation stored in this DirectShape. |
| Public method | [AppendShape(ShapeBuilder)](561c08af-0524-62b4-2df5-88eb17a221ab.htm) | Append shape built by the supplied ShapeBuilderObject to shape representation stored in this DirectShapeType. The data stored in the supplied ShapeBuilder object will be cleared. |
| Public method | [AppendShape(IList GeometryObject , DirectShapeTargetViewType)](fc51effa-341f-6743-68bc-3c5eff0b2567.htm) | Appends the collection of GeometryObjects into the model or view specific shape representation stored in this DirectShapeType. Passing DirectShapeTargetViewType.Default as view type will cause the model shape to be updated. |
| Public method | [AreOptionsValid](1d5fdef2-42ba-9857-6c20-ee9b6e7eb79d.htm) | Validates that the given DirectShapeTypeOptions are allowed for this particular DirectShapeType. |
| Public method | [ArePhasesModifiable](329b02eb-5ee4-1715-2fbf-2cbbc0d3ff2a.htm) | Returns true if the properties CreatedPhaseId and DemolishedPhaseId can be modified for this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanBeHidden](887010c4-de58-96b6-0931-4c226e6b142b.htm) | Indicates if the element can be hidden in the view. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanBeLocked](5ef8834b-168d-02ac-2f29-5d43f5da87f2.htm) | Identifies if the element can be locked. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanChangeFamilyName](4ebcd220-19aa-3789-672e-18bff44601d2.htm) | Checks whether the DirectShapeType supports a custom family name. |
| Public method | [CanCreateParts](31cfdb04-e1ce-5859-0479-86acabc06d4a.htm) | Indicates if it is possible to create parts from this DirectShapeType element. |
| Public method | [CanDeleteSubelement](c9795398-2d2c-db8e-a4e7-ca99d69fcc1d.htm) | Checks if given subelement can be removed from the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanHaveTypeAssigned](051e2945-b690-5387-d083-7cdb7cb75332.htm) | Identifies if the element can have a type assigned. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [ChangeTypeId(ElementId)](479b5d94-abd3-db42-27d7-6a3eda12f285.htm) | Changes the type of the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method Static member | [Create(Document, String, ElementId)](59f825ef-d5dc-c04d-3252-f91230068305.htm) | Creates a DirectShapeType element. |
| Public method Static member | [Create(Document, String, ElementId, DirectShapeTypeOptions)](be6be1e1-bca3-2431-9000-4481b9f8b98a.htm) | Creates a DirectShapeType element. |
| Public method | [DeleteEntity](ef0fa7d8-8152-6300-285d-1c0cdc08e5a7.htm) | Deletes the existing entity created by %schema% in the element (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [DeleteSubelement](de199938-feea-7437-c19f-162714b70dcd.htm) | Removes a subelement from the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [DeleteSubelements](6410b135-88fe-b111-769f-f14e86b42a05.htm) | Removes the subelements from the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [Dispose](e3b07ee4-f500-1b95-c786-8984289a5143.htm) | (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [Duplicate](b0e7d5d5-f33a-8ff2-b471-78a213f06ef5.htm) | Duplicates an existing element type and assigns it a new name. (Inherited from  [ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)  .) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [GetDependentElements](56e875d3-014b-a996-69c3-e6ed9b885f5c.htm) | Get all elements that, from a logical point of view, are the children of this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetEntity](09d80bf1-c1d0-aa2e-4f18-e5a5e9c9d93f.htm) | Returns the existing entity corresponding to the Schema if it has been saved in the Element, or an invalid entity otherwise. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetEntitySchemaGuids](742313cb-1bea-f873-e5ca-1bfac782286b.htm) | Returns the Schema guids of any Entities stored in this element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalFileReference](e784fb6e-94f4-09bd-1f9c-17e6968e18a5.htm) | Gets information pertaining to the external file referenced by the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternallyTaggedGeometry](60d0ba59-5345-dbd0-e92a-0f2d71d709de.htm) | Gets the externally tagged geometry by its external ID that is stored in this DirectShapeType. |
| Public method | [GetExternalResourceReference](fb4b9493-1d7b-5387-c171-2078225183ca.htm) | Gets the ExternalResourceReference associated with a specified external resource type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalResourceReferenceExpanded](1a28171e-8460-d849-4e7d-9a306a22cd6e.htm) | Gets the collection of ExternalResourceReference associated with a specified external resource type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalResourceReferences](7df4341b-5102-8016-d6fa-45bc27e8c3af.htm) | Gets the map of the external resource references referenced by the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalResourceReferencesExpanded](954cb21e-5c4e-1e52-7e35-1eb0ed4b050b.htm) | Gets the expanded map of the external resource references referenced by the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetGeneratingElementIds](112590d2-de20-dd1f-ae05-df7dfb3b410f.htm) | Returns the ids of the element(s) that generated the input geometry object. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetGeometryObjectFromReference](536b3d7a-ec8d-29f6-5957-751468c98dd0.htm) | Retrieve one geometric primitive contained in the element given a reference. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetMaterialArea](02417c40-bcc4-f04c-9897-cf47737e8739.htm) | Gets the area of the material with the given id. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMaterialIds](6011352e-151b-b8ac-14cc-45970f2fe5ad.htm) | Gets the element ids of all materials present in the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMaterialVolume](99b50d87-bfa6-ca67-e205-47b22cad6587.htm) | Gets the volume of the material with the given id. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMonitoredLinkElementIds](42b25291-f1b9-d240-c876-1b53f24f60e0.htm) | Provides the link instance IDs when the element is monitoring. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMonitoredLocalElementIds](47ca1e8c-f79d-a18b-505b-73a4358d2264.htm) | Provides the local element IDs when the element is monitoring. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetOptions](9f0e48d9-9007-340b-51c6-5fefe3f5379b.htm) | Gets a copy of the current options for this DirectShapeType. |
| Public method | [GetOrderedParameters](4bf4c0da-f841-0943-f9e0-246a666c1775.htm) | Gets the parameters associated to the element in order. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetParameter](fc4e5245-d2e5-e31d-a6e3-177106e75e10.htm) | Retrieves a parameter from the element given identifier. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetParameterFormatOptions](476c8179-f938-d047-db7c-776cf7e2929c.htm) | Returns a FormatOptions override for the element Parameter, or a default FormatOptions if no override exists. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetParameters](0cf342ef-c64f-b0b7-cbec-da8f3428a7dc.htm) | Retrieves the parameters from the element via the given name. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetPhaseStatus](eedf5981-b5e2-dda7-cb5e-01a4d4fc7f6c.htm) | Gets the status of a given element in the input phase (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetPreviewImage](e79da134-713a-2202-4898-cca930202dff.htm) | Get the preview image of an element. This image is similar to what is seen in the Revit UI when selecting the type of an element. (Inherited from  [ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)  .) |
| Public method | [GetSimilarTypes](2719ca23-11c7-dda4-6291-9a4f0cebfb21.htm) | Obtains a set of types that are similar to this type. (Inherited from  [ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)  .) |
| Public method | [GetSubelements](feabfd59-bd0f-ab61-34a1-d0d22f58c881.htm) | Returns the collection of element subelements. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [GetTypeId](cc66ca8e-302e-f072-edca-d847bcf14c86.htm) | Returns the identifier of this element's type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetValidTypes](086554ba-3c70-9c0f-8a09-55a4da4ef905.htm) | Obtains a set of types that are valid for this element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [HasExternalGeometry](331798b3-7509-159a-2f57-04bb6aacf049.htm) | Checks whether the externally tagged geometry is already present in this DirectShapeType. |
| Public method | [HasPhases](5d850f8a-4a50-406b-6c59-b85d49dcbb2e.htm) | Returns true if this Element has the properties CreatedPhaseId and DemolishedPhaseId. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsCreatedPhaseOrderValid](b2bcaf7f-c453-d6e2-fd85-083783e935f3.htm) | Returns true if createdPhaseId and demolishedPhaseId are in order. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsDemolishedPhaseOrderValid](46ec60b6-b1c5-25aa-c544-34379298c7b8.htm) | Returns true if createdPhaseId and demolishedPhaseId are in order. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsExternalFileReference](2bf6162f-0b0f-88cb-9c67-d4bd435537b5.htm) | Determines whether this Element represents an external file. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsHidden](2c3d4123-fded-cd5f-ed0d-12b1e1a3ce42.htm) | Identifies if the element has been permanently hidden in the view. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsMonitoringLinkElement](fde81756-5518-4924-c14e-f9ef2bb3fa6e.htm) | Indicate whether an element is monitoring any elements in any linked models. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsMonitoringLocalElement](9a41a87c-2b3b-b6ed-1743-98c002b20ce3.htm) | Indicate whether an element is monitoring other local elements. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsPhaseCreatedValid](ae48b10d-4a66-ee2c-85bf-f426435d0dbe.htm) | Returns true if createdPhaseId is an allowed value for the property CreatedPhaseId in this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsPhaseDemolishedValid](f97c9af7-fcbe-f617-d7ff-cfd4fb5af37f.htm) | Returns true if demolishedPhaseId is an allowed value for the property DemolishedPhaseId in this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsSimilarType](bd1e5459-4909-dc8a-46fd-54540fe1961e.htm) | Checks if given type is similar to this type. (Inherited from  [ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)  .) |
| Public method | [IsValidDefaultFamilyType](db029b02-e415-3807-d724-ec32b505d23a.htm) | Identifies if this type is a valid default family type for the given family category id. (Inherited from  [ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)  .) |
| Public method Static member | [IsValidReferenceCurve](ad764aa6-881d-658f-633c-8f52c2ffbbc8.htm) | Validates that the input curve is suitable for creating a direct shape type reference curve. Bounded and unbounded lines are accepted. Other bounded and unbounded curve types with natural bounds are accepted if they are not closed. Unbounded periodic curves are not allowed. |
| Public method Static member | [IsValidReferencePlaneBoundingBoxUV](22b216a0-6212-1379-1cc7-2656b395feca.htm) | Validates that the input BoundingBoxUV is suitable for bounding a reference plane surface. The input BoundingBoxUV must be set and not degenerate. |
| Public method | [IsValidShape(IList GeometryObject )](89861b7d-c844-45ff-e9f3-a804602c842e.htm) | Validates shape to be stored in a DirectShapeType. |
| Public method | [IsValidShape(IList GeometryObject , DirectShapeTargetViewType)](f87b331e-3a65-cbfb-8652-1c82a5d57883.htm) | Validates view-specific shape to be stored in a DirectShapeType. Expects a non-default view type. |
| Public method | [IsValidType(ElementId)](c3ca4ee5-c2b3-beb3-ee51-cc6cafc82c93.htm) | Checks if given type is valid for this element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [LookupParameter](4400b9f8-3787-0947-5113-2522ff5e5de2.htm) | Attempts to find a parameter on the element which has the given name. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [RefersToExternalResourceReference](0a4aabb3-f684-0800-7bf5-31540831593f.htm) | Determines whether this Element uses external resources associated with a specified external resource type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [RefersToExternalResourceReferences](387c00cd-3932-76e6-152b-bfe4efb8fbc1.htm) | Determines whether this Element uses external resources. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [RemoveExternallyTaggedGeometry](0fc3b749-bcc3-1472-092d-38475fe2c81d.htm) | Removes the externally tagged geometry object by its external ID from this DirectShapeType. |
| Public method | [ResetExternallyTaggedGeometry](7303e22c-72da-9667-fdaf-521534c444f8.htm) | Removes all of the externally tagged geometry in this DirectShapeType. |
| Public method | [SetEntity](e90c01ab-3d2f-2f46-3e88-8297e686dc80.htm) | Stores the entity in the element. If an Entity described by the same Schema already exists, it is overwritten. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [SetFamilyName](9a54477b-177f-5f9a-4c17-4e66741fc103.htm) | Sets the family name for the DirectShapeType. |
| Public method | [SetOptions](a7ef3f68-713f-5adc-caf9-dcee1e46efb1.htm) | Sets the options to use for this DirectShapeType. |
| Public method | [SetShape(IList GeometryObject )](5c2bf291-537e-0de1-4982-87a7e20c217a.htm) | Builds the type shape from the supplied collection of GeometryObjects. The objects are copied. If the new shape is identical to the old one, the old shape will be kept. |
| Public method | [SetShape(ShapeBuilder)](ba16827c-3c05-ee9d-e1d3-eb60d4f02e3b.htm) | Sets the shape of this object to the one accumulated in the supplied Builder object. If the new shape is identical to the old one, the old shape will be kept. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |
| Public method | [UpdateExternallyTaggedGeometry](0acd0330-9e79-8be8-ff3c-740ed053ea82.htm) | Updates the externally tagged geometry object in the DirectShapeType. |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AssemblyInstanceId](83989f69-1aca-1a49-9647-e57bc2d58b21.htm) | The id of the assembly instance to which the element belongs. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [BoundingBox](def2f9f2-b23a-bcea-43a3-e6de41b014c8.htm) | Retrieves a box that circumscribes all geometry of the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [CanBeCopied](588e4fac-5492-0e1d-c935-dfd53e801c04.htm) | Determine if this ElementType can create a copy (Inherited from  [ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)  .) |
| Public property | [CanBeDeleted](5efe8253-d555-00c2-8db6-9114e328fcc7.htm) | Determine if this ElementType can be deleted (Inherited from  [ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)  .) |
| Public property | [CanBeRenamed](ce2e0f26-deaf-d649-0617-babde54c6bf7.htm) | Determine if this ElementType can be renamed (Inherited from  [ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)  .) |
| Public property | [Category](8990bd36-af08-fc99-496b-f94fcb056b21.htm) | Retrieves a Category object that represents the category or sub category in which the element resides. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [CreatedPhaseId](c6032e01-f7cb-b2ea-3312-697d14216a31.htm) | Id of a Phase at which the Element was created. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [DemolishedPhaseId](7949a983-c5dc-62a3-594a-d685365449d5.htm) | Id of a Phase at which the Element was demolished. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [DesignOption](5c20fe58-e301-6ddb-3438-666db5c586ee.htm) | Returns the design option to which the element belongs. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Document](9e530d25-61ca-3899-a531-cbcfd994358d.htm) | Returns the Document in which the Element resides. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [FamilyName](10de5c66-1b4b-9214-4036-27a6b24e5703.htm) | Gets the family name of this element type. (Inherited from  [ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)  .) |
| Public property | [Geometry](d8a55a5b-2a69-d5ab-3e1f-6cf1ee43c8ec.htm) | Retrieves the geometric representation of the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [GroupId](9508a6c5-9681-bbef-07c5-1351583b0e1e.htm) | The id of the group to which an element belongs. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Id](9235095b-b7ae-b6e5-6cc2-2b8d397644de.htm) | A unique identifier for an Element in an Autodesk Revit project. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [IsModifiable](65f9f835-daaa-3efa-2976-3f932aa18366.htm) | Identifies if the element is modifiable. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [IsTransient](f391d235-555f-6651-99c6-895fc443f8d8.htm) | Indicates whether an element is transient or permanent. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [IsValidObject](0ffcf585-a39d-623c-9b5b-ab63c7bebfb6.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [LevelId](27033fe3-6740-61e3-be82-47a6b8ae77db.htm) | The id of the level associated with the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Location](89438f4f-7e15-835a-0c66-d6adbc8dd00c.htm) | This property is used to find the physical location of an element within a project. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Name](1198805b-fdbf-54bf-64d3-90dbd01b4c5f.htm) | Set the name for the ElementType. (Inherited from  [ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)  .) |
| Public property | [OwnerViewId](174c1adf-0be8-a4b0-41f3-9e3ea1d6b1f1.htm) | The id of the view that owns the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameter Guid](2e852bc4-46c6-5598-cc45-0eaf38cf8973.htm) | Retrieves a parameter from the element given a GUID for a shared parameter. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameter BuiltInParameter](2f91a9f3-7f69-72f9-08d6-a2d71dfb33db.htm) | Retrieves a parameter from the element given a parameter id. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameter Definition](87d8a88c-906e-85a9-f575-f263788b8584.htm) | Retrieves a parameter from the element based on its definition. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameters](7af5d66f-4533-33d2-dd82-d9573eaabf15.htm) | Retrieves a set containing all of the parameters that are contained within the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [ParametersMap](82c45482-a018-32e4-d8e5-9751e10ffeb9.htm) | Retrieves a map containing all of the parameters that are contained within the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Pinned](c37bc7f9-409e-9b8a-f491-f700228985e2.htm) | Identifies if the element has been pinned to prevent changes. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [UniqueId](f9a9cb77-6913-6d41-ecf5-4398a24e8ff8.htm) | A stable unique identifier for an element within the document. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [UserAssignability](3a4036c3-6e64-6b5f-1246-fe8ef68a7526.htm) | An option controlling the ability of DirectShapes to assign this DirectShapeType as its type. |
| Public property | [VersionGuid](2a1eae53-2c5c-a7be-1ef2-0f48626c62f5.htm) | Get the element version Guid. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [ViewSpecific](785b351e-51cb-e3c6-cb91-f307c8e4ba73.htm) | Identifies if the element is owned by a view. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [WorksetId](4b45250a-7a07-a89a-0f63-cf8d142a7b93.htm) | Get Id of the Workset which owns the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)