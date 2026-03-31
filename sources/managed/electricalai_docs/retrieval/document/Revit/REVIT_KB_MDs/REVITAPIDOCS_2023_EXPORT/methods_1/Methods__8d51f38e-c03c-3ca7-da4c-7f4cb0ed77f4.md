[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Rebar Members

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [Rebar](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [ArePhasesModifiable](329b02eb-5ee4-1715-2fbf-2cbbc0d3ff2a.htm) | Returns true if the properties CreatedPhaseId and DemolishedPhaseId can be modified for this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanApplyPresentationMode](103b0f74-75ed-3db4-4ae0-645621296d9e.htm) | Checks if a presentation mode can be applied for this rebar in the given view. |
| Public method | [CanBeHidden](887010c4-de58-96b6-0931-4c226e6b142b.htm) | Indicates if the element can be hidden in the view. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanBeLocked](5ef8834b-168d-02ac-2f29-5d43f5da87f2.htm) | Identifies if the element can be locked. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanBeMatchedWithMultipleShapes](82bd14f6-8678-d37c-1848-54a97d2aa7d3.htm) | Checks if this Rebar can be matched with multiple Rebar Shapes. |
| Public method | [CanDeleteSubelement](c9795398-2d2c-db8e-a4e7-ca99d69fcc1d.htm) | Checks if given subelement can be removed from the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanHaveTypeAssigned](051e2945-b690-5387-d083-7cdb7cb75332.htm) | Identifies if the element can have a type assigned. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [CanSuppressFirstOrLastBar](4ed20a6e-a048-e483-3eba-5de536f6cd09.htm) | Checks if the first or last bar in rebar set can be hidden in the given view. |
| Public method | [CanUseHookType](1e62e35b-b85b-5ae0-1908-e697ae47e78d.htm) | Checks if the specified RebarHookType id is of a valid RebarHookType for the Rebar's RebarBarType |
| Public method | [ChangeTypeId(ElementId)](479b5d94-abd3-db42-27d7-6a3eda12f285.htm) | Changes the type of the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [ClearPresentationMode](61ffbfb6-628b-3f41-3cb0-c46406a41a5c.htm) | Sets the presentation mode for this rebar set to the default (either for a single view, or for all views). |
| Public method | [ConstraintsCanBeEdited](37eec9d2-eac9-b7a9-723a-82f1791ee350.htm) | For ShapeDriven Rebar: returns true, if the Rebar element's external constraints are available for editing using the RebarConstraintsManager class. It will return false if Rebar is in Group  For FreeForm rebar: constraints can be edited if there is a valid external server Guid assigned to that Rebar |
| Public method Static member | [ContainsValidArcRadiiForStyleAndBarType](f1db8751-d587-521c-2a5f-77b818d38105.htm) | Checks that all arcs in the chain of curves have radii that are not less than minimum bend radius for bar type and style |
| Public method Static member | [CreateFreeForm(Document, Guid, RebarBarType, Element)](0528ba3a-2893-cc05-0ee6-67fa3eb087e2.htm) | Creates a free form rebar that can have constraints. |
| Public method Static member | [CreateFreeForm(Document, RebarBarType, Element, IList CurveLoop , RebarFreeFormValidationResult )](38767c5e-0196-3359-69db-19d728873b19.htm) | Creates a free form rebar that will be unconstrained. Constraints can't be added later to this rebar. |
| Public method Static member | [CreateFreeForm(Document, RebarBarType, Element, IList IList Curve , RebarFreeFormValidationResult )](e412ef5a-baa0-64e3-858e-65f79316850a.htm) | Creates a free form rebar that will be unconstrained. Constraints can't be added later to this rebar. |
| Public method Static member | [CreateFromCurves(Document, RebarStyle, RebarBarType, RebarHookType, RebarHookType, Element, XYZ, IList Curve , RebarHookOrientation, RebarHookOrientation, Boolean, Boolean)](b020c9d5-6026-b9fa-7e23-f6a7ec2cede3.htm) | Creates a new instance of a shape driven Rebar element within the project. |
| Public method Static member | [CreateFromCurves(Document, RebarStyle, RebarBarType, RebarHookType, RebarHookType, Element, XYZ, IList Curve , RebarHookOrientation, RebarHookOrientation, Double, Double, ElementId, ElementId, Boolean, Boolean)](bc5349d8-fc03-6223-be02-601c4aaa7782.htm) | Creates a new instance of a shape driven Rebar element within the project. |
| Public method Static member | [CreateFromCurvesAndShape(Document, RebarShape, RebarBarType, RebarHookType, RebarHookType, Element, XYZ, IList Curve , RebarHookOrientation, RebarHookOrientation)](10ddc28e-a410-5f29-6fe9-d4b73f917c54.htm) | Creates a new instance of a shape driven Rebar element within the project. The instance will have the default shape parameters from the RebarShape. If the RebarShapeDefinesHooks flag in ReinforcementSettings has been set to true, then both the curves and hooks must match the RebarShape definition. Otherwise, the hooks can be different than the defaults specified in the RebarShape |
| Public method Static member | [CreateFromCurvesAndShape(Document, RebarShape, RebarBarType, RebarHookType, RebarHookType, Element, XYZ, IList Curve , RebarHookOrientation, RebarHookOrientation, Double, Double, ElementId, ElementId)](bba959de-0335-e395-61f9-ce45de268a52.htm) | Creates a new instance of a shape driven Rebar element within the project. The instance will have the default shape parameters from the RebarShape. If the RebarShapeDefinesHooks flag in ReinforcementSettings has been set to true, then curves, hook types and hook rotation angles should match the rebar shape definition. Otherwise, the hooks can be different than the defaults specified in the RebarShape. If the RebarShapeDefinesEndTreatment flag in ReinforcementSettings has been set to true, then curves and end treatment types should match the rebar shape definition. Otherwise, the end treatment types can be different than the defaults specified in the RebarShape. |
| Public method Static member | [CreateFromRebarShape](5e58e3f3-dea6-79cb-9de4-475e6fe5c28b.htm) | Creates a new shape driven Rebar, as an instance of a RebarShape. The instance will have the default shape parameters from the RebarShape, and its location is based on the bounding box of the shape in the shape definition. Hooks are removed from the shape before computing its bounding box. If appropriate hooks can be found in the document, they will be assigned arbitrarily. |
| Public method | [DeleteEntity](ef0fa7d8-8152-6300-285d-1c0cdc08e5a7.htm) | Deletes the existing entity created by %schema% in the element (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [DeleteSubelement](de199938-feea-7437-c19f-162714b70dcd.htm) | Removes a subelement from the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [DeleteSubelements](6410b135-88fe-b111-769f-f14e86b42a05.htm) | Removes the subelements from the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [Dispose](e3b07ee4-f500-1b95-c786-8984289a5143.htm) | (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [DoesBarExistAtPosition](f223b762-1ef9-bf37-29e3-202dd570edb8.htm) | Checks whether a bar is included at the specified position. |
| Public method | [EnableHookLengthOverride](768754cc-5d24-3b25-84f2-82dee640d6ca.htm) | Enables or disables the ability to override hook lengths for this rebar instance. |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [FindMatchingPredefinedPresentationMode](b1cd999d-3630-47df-e357-4149651d9385.htm) | Determines if there is a matching RebarPresentationMode for the current set of selected hidden and unhidden bars assigned to the given view. |
| Public method | [GetAllRebarShapeIds](a4226864-acec-b0b9-ddb2-fae12b48f378.htm) | Gets the ids of the RebarShapes elements that defines the shapes of the rebar. |
| Public method | [GetBarIndexFromReference](6d2769f6-ba8d-5173-0947-9d82aeabefa8.htm) | Given a reference that represents a part of a bar, this method will return the bar index. |
| Public method | [GetBendData](e20b8d30-f5b8-bf5e-4df5-dbb7498e2ccc.htm) | Gets the RebarBendData, containing bar and hook information, of the instance. |
| Public method | [GetCenterlineCurves](7be7e413-bfac-bbd3-17b6-ff2008771afa.htm) | A chain of curves representing the centerline of the rebar. |
| Public method | [GetCouplerId](72b65231-27d4-79b2-1193-136bab814951.htm) | Get the id of the Rebar Coupler that is applied to the rebar at the specified end. |
| Public method | [GetDependentElements](56e875d3-014b-a996-69c3-e6ed9b885f5c.htm) | Get all elements that, from a logical point of view, are the children of this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetEndTreatmentTypeId](3521d0c8-5746-6dde-4839-3e9a14dbd93e.htm) | Get the id of the EndTreatmentType to be applied to the rebar. |
| Public method | [GetEntity](09d80bf1-c1d0-aa2e-4f18-e5a5e9c9d93f.htm) | Returns the existing entity corresponding to the Schema if it has been saved in the Element, or an invalid entity otherwise. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetEntitySchemaGuids](742313cb-1bea-f873-e5ca-1bfac782286b.htm) | Returns the Schema guids of any Entities stored in this element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalFileReference](e784fb6e-94f4-09bd-1f9c-17e6968e18a5.htm) | Gets information pertaining to the external file referenced by the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalResourceReference](fb4b9493-1d7b-5387-c171-2078225183ca.htm) | Gets the ExternalResourceReference associated with a specified external resource type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalResourceReferenceExpanded](1a28171e-8460-d849-4e7d-9a306a22cd6e.htm) | Gets the collection of ExternalResourceReference associated with a specified external resource type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalResourceReferences](7df4341b-5102-8016-d6fa-45bc27e8c3af.htm) | Gets the map of the external resource references referenced by the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetExternalResourceReferencesExpanded](954cb21e-5c4e-1e52-7e35-1eb0ed4b050b.htm) | Gets the expanded map of the external resource references referenced by the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetFreeFormAccessor](67be446c-e2e1-9dfe-315f-f5d6adc779b9.htm) | Returns an interface providing access to free-form properties and methods for this Rebar element. |
| Public method | [GetFullGeometryForView](83481a4d-861e-dd0f-bf8c-d0dbe11a18d5.htm) | Generates full geometry for the Rebar for a specific view. |
| Public method | [GetGeneratingElementIds](112590d2-de20-dd1f-ae05-df7dfb3b410f.htm) | Returns the ids of the element(s) that generated the input geometry object. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetGeometryObjectFromReference](536b3d7a-ec8d-29f6-5957-751468c98dd0.htm) | Retrieve one geometric primitive contained in the element given a reference. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetHookOrientation](0aabc992-1723-9f78-aff7-ef9760f8a64b.htm) | Returns the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal. |
| Public method | [GetHookRotationAngle](0217f682-0c09-2b77-02d4-89c494a11cc9.htm) | Gets the out of plane hook rotation angle at the specified end. |
| Public method | [GetHookTypeId](016d53d9-0ef5-99d1-b12f-089f04df3952.htm) | Get the id of the RebarHookType to be applied to the rebar. |
| Public method | [GetHostId](aa67c490-8875-2756-c621-49484423d026.htm) | The element that contains the rebar. |
| Public method | [GetMaterialArea](02417c40-bcc4-f04c-9897-cf47737e8739.htm) | Gets the area of the material with the given id. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMaterialIds](6011352e-151b-b8ac-14cc-45970f2fe5ad.htm) | Gets the element ids of all materials present in the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMaterialVolume](99b50d87-bfa6-ca67-e205-47b22cad6587.htm) | Gets the volume of the material with the given id. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMonitoredLinkElementIds](42b25291-f1b9-d240-c876-1b53f24f60e0.htm) | Provides the link instance IDs when the element is monitoring. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMonitoredLocalElementIds](47ca1e8c-f79d-a18b-505b-73a4358d2264.htm) | Provides the local element IDs when the element is monitoring. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetMovedBarTransform](8db286b5-f16e-2367-7e1f-de58fe5a84b8.htm) | Returns a transform representing the movement of the bar relative to its default position along the distribution path. |
| Public method | [GetOrderedParameters](4bf4c0da-f841-0943-f9e0-246a666c1775.htm) | Gets the parameters associated to the element in order. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetOverridableHookParameters](40de7723-ff71-2507-7369-56983b8d2842.htm) | Outputs the formula parameter ids defined in the RebarShape family which are associated with hook length and hook tangent length parameters. |
| Public method | [GetParameter](fc4e5245-d2e5-e31d-a6e3-177106e75e10.htm) | Retrieves a parameter from the element given identifier. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetParameterFormatOptions](476c8179-f938-d047-db7c-776cf7e2929c.htm) | Returns a FormatOptions override for the element Parameter, or a default FormatOptions if no override exists. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetParameters](0cf342ef-c64f-b0b7-cbec-da8f3428a7dc.htm) | Retrieves the parameters from the element via the given name. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetParameterValueAtIndex](d4d5a126-4e14-8fda-bbb9-2178b7162486.htm) | Get the parameter value for a bar at the specified index. The parameter Id. The bar index in the rebar distribution. Accepts only values between 0 and NumberOfBarPositions-1. The ParameterValue for given parameterId and barPositionIndex. Throws exception if barPositionIndex is outside boundaries. |
| Public method | [GetPhaseStatus](eedf5981-b5e2-dda7-cb5e-01a4d4fc7f6c.htm) | Gets the status of a given element in the input phase (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetPresentationMode](7f5691ab-c03a-ed42-bf23-aa0a0d849262.htm) | Gets the presentation mode for this rebar set when displayed in the given view. |
| Public method | [GetRebarConstraintsManager](0728a2e5-49db-3a7f-8f83-9db60b92f902.htm) | Returns an object for managing the external constraints on the Rebar element |
| Public method | [GetReinforcementRoundingManager](6d26d7fd-f681-604b-312e-b3395d1e7ca4.htm) | Returns an object for managing reinforcement rounding override settings. |
| Public method | [GetShapeDrivenAccessor](c77085bd-db18-4869-bb2a-1e5c702e273a.htm) | Returns an interface providing access to shape-driven properties and methods for this Rebar element. |
| Public method | [GetShapeId](6edc946f-d8a3-ee78-adbb-7d5359501ed3.htm) | Returns the id of the RebarShape element that defines the shape of the rebar. |
| Public method | [GetSubelements](feabfd59-bd0f-ab61-34a1-d0d22f58c881.htm) | Returns the collection of element subelements. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetTransformedCenterlineCurves](650b9879-3378-77f8-65f0-efeb05daa399.htm) | A chain of curves representing the centerline of the rebar. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [GetTypeId](cc66ca8e-302e-f072-edca-d847bcf14c86.htm) | Returns the identifier of this element's type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [GetValidTypes](086554ba-3c70-9c0f-8a09-55a4da4ef905.htm) | Obtains a set of types that are valid for this element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [HasPhases](5d850f8a-4a50-406b-6c59-b85d49dcbb2e.htm) | Returns true if this Element has the properties CreatedPhaseId and DemolishedPhaseId. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [HasPresentationOverrides](1e74f1a5-0906-c5f0-0cde-0d8b6a6d563d.htm) | Identifies if this Rebar has overridden default presentation settings for the given view. |
| Public method | [HookAngleMatchesRebarShapeDefinition](3a5c4860-23a1-65bc-e825-8277c0720f45.htm) | Checks that the hook angle of the specified RebarHookType matches the hook angle used in the Rebar's RebarShape at the specified end of the bar. |
| Public method | [IsBarHidden](d066eb29-243b-bcc9-2468-c5df0f255a13.htm) | Identifies if a given bar in this rebar set is hidden in this view. |
| Public method | [IsCreatedPhaseOrderValid](b2bcaf7f-c453-d6e2-fd85-083783e935f3.htm) | Returns true if createdPhaseId and demolishedPhaseId are in order. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsDemolishedPhaseOrderValid](46ec60b6-b1c5-25aa-c544-34379298c7b8.htm) | Returns true if createdPhaseId and demolishedPhaseId are in order. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsExternalFileReference](2bf6162f-0b0f-88cb-9c67-d4bd435537b5.htm) | Determines whether this Element represents an external file. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsHidden](2c3d4123-fded-cd5f-ed0d-12b1e1a3ce42.htm) | Identifies if the element has been permanently hidden in the view. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsHookLengthOverrideEnabled](489db44d-08a8-600c-a139-29947eea09ef.htm) | Returns True if the ability to override hook lengths is enabled for this rebar instance, False otherwise. |
| Public method | [IsMonitoringLinkElement](fde81756-5518-4924-c14e-f9ef2bb3fa6e.htm) | Indicate whether an element is monitoring any elements in any linked models. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsMonitoringLocalElement](9a41a87c-2b3b-b6ed-1743-98c002b20ce3.htm) | Indicate whether an element is monitoring other local elements. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsPhaseCreatedValid](ae48b10d-4a66-ee2c-85bf-f426435d0dbe.htm) | Returns true if createdPhaseId is an allowed value for the property CreatedPhaseId in this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsPhaseDemolishedValid](f97c9af7-fcbe-f617-d7ff-cfd4fb5af37f.htm) | Returns true if demolishedPhaseId is an allowed value for the property DemolishedPhaseId in this Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [IsRebarFreeForm](cf39a5b8-d7f3-d073-0120-358dd3afab21.htm) | Returns true if the rebar is free form and false if shape driven. |
| Public method | [IsRebarInSection](49fad033-610a-71b5-60f0-0b3d28d7c2c1.htm) | Identifies if this Rebar is shown as a cross-section in the given view. |
| Public method | [IsRebarShapeDriven](b36327e1-c6be-791c-24a5-cf6d02890dee.htm) | Returns true if the rebar is shape driven and false if free form. |
| Public method | [IsSolidInView](3d59ebc3-3585-0411-f17a-4ec0abebdb8a.htm) | **Obsolete.**   Checks if this rebar element is shown solidly in a 3D view. |
| Public method | [IsUnobscuredInView](f52f0fb5-9ab0-4650-62a4-ed9bf68e888f.htm) | Checks if this rebar element is shown unobscured in a view. |
| Public method | [IsValidType(ElementId)](c3ca4ee5-c2b3-beb3-ee51-cc6cafc82c93.htm) | Checks if given type is valid for this element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [LookupParameter](4400b9f8-3787-0947-5113-2522ff5e5de2.htm) | Attempts to find a parameter on the element which has the given name. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [MoveBarInSet](f1ff60b3-7882-c352-e03c-a00208993e04.htm) | This method applies the transformation matrix to the rebar bar at the desired position in the rebar set. If the bar was already moved, the method will concatenate the transformation matrix with the existing movement. |
| Public method Static member | [RebarShapeMatchesCurvesAndHooks](16036dad-204c-47fa-9ce7-090e964a70d5.htm) | Checks if rebarShape matches curves and hooks. If the RebarShapeDefinesHooks flag in ReinforcementSettings has been set to false, then this method will ignore the hook information. |
| Public method Static member | [RebarShapeMatchesCurvesHooksAndEndTreatment](8fd9c444-b123-7f85-479b-aa55ce74ade6.htm) | Checks if rebarShape matches curves, hooks and end treatment. If the RebarShapeDefinesHooks flag in ReinforcementSettings has been set to false, then this method will ignore the hook information. If the RebarShapeDefinesEndTreatment flag in ReinforcementSettings has been set to false, then this method will ignore the end treatment information. |
| Public method | [RefersToExternalResourceReference](0a4aabb3-f684-0800-7bf5-31540831593f.htm) | Determines whether this Element uses external resources associated with a specified external resource type. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [RefersToExternalResourceReferences](387c00cd-3932-76e6-152b-bfe4efb8fbc1.htm) | Determines whether this Element uses external resources. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [ResetMovedBarTransform](5e2e7166-d294-88a3-5b03-1d38ce930546.htm) | Reset the transformation representing the movement of the bar relative to its default position along the distribution path. The moved bar transform will be set to Identity. |
| Public method | [SetBarHiddenStatus](9f58c248-58b9-47b9-4367-ead7f53695d6.htm) | Sets the bar in this rebar set to be hidden or unhidden in the given view. |
| Public method | [SetBarIncluded](b6bd8b08-36ab-ec51-a533-8c918b2fe42c.htm) | Sets if the bar at the desired index is included or not. |
| Public method | [SetEndTreatmentTypeId](ceb68db2-2053-5911-3318-da05ec742dac.htm) | Sets the id of the EndTreatmentType to be applied to the rebar. This can be done if and only if the end of the bar on which the end treatment is applied has no RebarCoupler on it, otherwise will throw an exception. If a RebarHookType is present at the rebar end, it will automatically set to invalidElementId. |
| Public method | [SetEntity](e90c01ab-3d2f-2f46-3e88-8297e686dc80.htm) | Stores the entity in the element. If an Entity described by the same Schema already exists, it is overwritten. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public method | [SetHookOrientation](d2bb944f-32dd-d6d0-142c-cba3dfd01e5f.htm) | Defines the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal. |
| Public method | [SetHookRotationAngle](399efb81-f360-4e7b-bbc3-938325f0baba.htm) | Sets the out of plane hook rotation angle at the specified end. |
| Public method | [SetHookTypeId](31ce9472-9bf7-3567-eaad-b8b45d587438.htm) | Set the id of the RebarHookType to be applied to the rebar. If an EndTreatmentType is present at the rebar end, it will automatically set to invalidElementId. |
| Public method | [SetHostId](79da5994-50ed-171f-adf2-9a6550c898db.htm) | The element that contains the rebar. |
| Public method | [SetPresentationMode](09b93605-4e24-3cfd-3931-c0f39ae1f6b9.htm) | Sets the presentation mode for this rebar set when displayed in the given view. |
| Public method | [SetSolidInView](f030d783-7390-38dc-a83a-b1afaa895162.htm) | **Obsolete.**   Sets this rebar element to be shown solidly in a 3D view. |
| Public method | [SetUnobscuredInView](ab857136-3b6f-5c0e-b28c-5ea5f7c3be79.htm) | Sets this rebar element to be shown unobscured in a view. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AssemblyInstanceId](83989f69-1aca-1a49-9647-e57bc2d58b21.htm) | The id of the assembly instance to which the element belongs. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [BoundingBox](def2f9f2-b23a-bcea-43a3-e6de41b014c8.htm) | Retrieves a box that circumscribes all geometry of the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Category](8990bd36-af08-fc99-496b-f94fcb056b21.htm) | Retrieves a Category object that represents the category or sub category in which the element resides. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [CreatedPhaseId](c6032e01-f7cb-b2ea-3312-697d14216a31.htm) | Id of a Phase at which the Element was created. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [DemolishedPhaseId](7949a983-c5dc-62a3-594a-d685365449d5.htm) | Id of a Phase at which the Element was demolished. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [DesignOption](5c20fe58-e301-6ddb-3438-666db5c586ee.htm) | Returns the design option to which the element belongs. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [DistributionType](d5518e91-ce1f-7a3f-01bf-e3e3727ed42d.htm) | The type of rebar distribution(also known as Rebar Set Type). |
| Public property | [Document](9e530d25-61ca-3899-a531-cbcfd994358d.htm) | Returns the Document in which the Element resides. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Geometry](d8a55a5b-2a69-d5ab-3e1f-6cf1ee43c8ec.htm) | Retrieves the geometric representation of the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [GroupId](9508a6c5-9681-bbef-07c5-1351583b0e1e.htm) | The id of the group to which an element belongs. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Id](9235095b-b7ae-b6e5-6cc2-2b8d397644de.htm) | A unique identifier for an Element in an Autodesk Revit project. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [IncludeFirstBar](099e72c3-a92f-b14c-fada-ef91241f5152.htm) | Identifies if the first bar in rebar set is shown. |
| Public property | [IncludeLastBar](5b3663d8-9b7f-12de-d20a-895259bea9ac.htm) | Identifies if the last bar in rebar set is shown. |
| Public property | [IsModifiable](65f9f835-daaa-3efa-2976-3f932aa18366.htm) | Identifies if the element is modifiable. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [IsTransient](f391d235-555f-6651-99c6-895fc443f8d8.htm) | Indicates whether an element is transient or permanent. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [IsValidObject](0ffcf585-a39d-623c-9b5b-ab63c7bebfb6.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [LayoutRule](69eb7a49-7e5a-da45-6579-c91386888a7f.htm) | Identifies the layout rule of rebar set. |
| Public property | [LevelId](27033fe3-6740-61e3-be82-47a6b8ae77db.htm) | The id of the level associated with the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Location](89438f4f-7e15-835a-0c66-d6adbc8dd00c.htm) | This property is used to find the physical location of an element within a project. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [MaxSpacing](1e7105e5-8d08-26ed-d97d-76754753fded.htm) | Identifies the maximum spacing between rebar in rebar set. |
| Public property | [Name](e372092e-ff47-71c2-1272-50ab08e5a41d.htm) | A human readable name for the Element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [NumberOfBarPositions](f063cb6e-c159-f0e8-519f-666a797fa53c.htm) | The number of potential bars in the set. |
| Public property | [OwnerViewId](174c1adf-0be8-a4b0-41f3-9e3ea1d6b1f1.htm) | The id of the view that owns the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameter Guid](2e852bc4-46c6-5598-cc45-0eaf38cf8973.htm) | Retrieves a parameter from the element given a GUID for a shared parameter. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameter BuiltInParameter](2f91a9f3-7f69-72f9-08d6-a2d71dfb33db.htm) | Retrieves a parameter from the element given a parameter id. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameter Definition](87d8a88c-906e-85a9-f575-f263788b8584.htm) | Retrieves a parameter from the element based on its definition. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Parameters](7af5d66f-4533-33d2-dd82-d9573eaabf15.htm) | Retrieves a set containing all of the parameters that are contained within the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [ParametersMap](82c45482-a018-32e4-d8e5-9751e10ffeb9.htm) | Retrieves a map containing all of the parameters that are contained within the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Pinned](c37bc7f9-409e-9b8a-f491-f700228985e2.htm) | Identifies if the element has been pinned to prevent changes. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Quantity](6d042353-dea0-e851-bed7-1143559e03db.htm) | Identifies the number of bars in rebar set. |
| Public property | [ReadOnlyParameters](6e992635-8245-ac60-3514-ca02f6b8e85d.htm) | When set to true, Rebar will report all its parameters as read only. For example, the method Parameter::IsReadOnly() for all Rebar Parameters will return true. When set to false, the return value of Parameter::IsReadOnly() will not be affected. |
| Public property | [ScheduleMark](552fe461-637c-5f93-df6b-76c9c85d36be.htm) | The Schedule Mark parameter. On creation, the Schedule Mark is set to a value that is unique to the host, but it can be set to any value. |
| Public property | [TotalLength](69f129e5-5510-53ea-95be-ac0f4dcb2a4f.htm) | The length of an individual bar multiplied by Quantity. |
| Public property | [UniqueId](f9a9cb77-6913-6d41-ecf5-4398a24e8ff8.htm) | A stable unique identifier for an element within the document. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [VersionGuid](2a1eae53-2c5c-a7be-1ef2-0f48626c62f5.htm) | Get the element version Guid. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [ViewSpecific](785b351e-51cb-e3c6-cb91-f307c8e4ba73.htm) | Identifies if the element is owned by a view. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |
| Public property | [Volume](b1111955-446c-2487-151d-faf20ab9414e.htm) | The volume of an individual bar multiplied by Quantity. |
| Public property | [WorksetId](4b45250a-7a07-a89a-0f63-cf8d142a7b93.htm) | Get Id of the Workset which owns the element. (Inherited from  [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)  .) |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)