[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExporterIFC Members

---



|  |
| --- |
| [ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddBuildingStorey](08c5605c-b66f-baae-5684-d9dc7cf7121a.htm) | Adds building storey to the exporter's internal cache. |
| Public method | [ClearFaceWithElementHandleMap](5f97a843-1df7-64fb-f063-2e8f4899774d.htm) | Clear face with element handle map. |
| Public method | [Dispose](daa92a17-48ad-264e-8a7d-d2a8de070508.htm) | Releases all resources used by the  [ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | [FindSpaceBoundingElementHandle](facc8372-3b66-2b31-135c-852985763186.htm) | Looks up the handle associated to the element and level id from the ExporterIFC's internal cache. |
| Public method | [Get2DContextHandle](9e027616-9f33-ede2-d25f-1fe4e3b38445.htm) | Obtains the IfcRepresentationContext handle to be used for 2D entities (Annotations). |
| Public method | [Get3DContextHandle](e1ea52a9-9e2c-9704-cfab-d43fe87fd53b.htm) | Obtains the IfcRepresentationContext or IfcRepresentationSubContext handle to be used for 3D entities (Model entities). |
| Public method | [GetDoorWindowOpeningHandle](aa17a626-7f33-0984-6b2d-e8ff8b7e6423.htm) | Get the handle to the opening associated with a hosted (door/window) element from the internal cache. |
| Public method | [GetFamilyName](bbab76a2-98c3-e6d3-c8b2-829ebd5e45e5.htm) | Gets the name of the element assigned to the current export state. |
| Public method | [GetFile](1baac5bf-ee32-4d1c-0ba3-6193124c0d9c.htm) | Gets the handle to the IFC file being created during this export operation. |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetHostObjects](39ace44e-26a7-e530-2dc2-737a1e3f1479.htm) | Returns a collection containing the host object handles in the document. |
| Public method | [GetLayerNameForPresentationLayer](9bb2d5c4-40ef-661b-b49e-720e74a1ca57.htm) | Get the layer name associated with an element from the default layer mapping table. |
| Public method | [GetLevelInfo](c404ab36-866c-8ac8-a8b1-c60d963791ed.htm) | Returns an object representing the information about a level in the document. |
| Public method | [GetLevelInfos](c7f1c52a-a0d0-cc15-4a08-1c476bb7509b.htm) | Returns a collection containing the information about all levels in the document. |
| Public method | [GetMaterialIdForCurrentExportState](ea78908e-959b-dca9-06a2-abce0c4cef70.htm) | This gets the material id that is associated with the element in the current export state. |
| Public method | [GetOptions](79e15a6b-3a5d-3aa1-c13a-5155356c5842.htm) | Gets the collection of named options set by the exporter client. |
| Public method | [GetOrCreateFillPattern](13faad3d-86f3-ed60-b3a3-78504c969716.htm) | Get (or create) the IfcFillPatternStyle associated with an ElementId. |
| Public method | [GetPresentationLayerAssignments](7dad2ed6-30a7-1b25-5e5f-8a1d7389f103.htm) | Get the list of the internally IfcPresentationLayerAssignments and their respective shape representations. |
| Public method | [GetRelatedElements](dbab0f38-a7d9-8f42-5217-c41c8a5330f7.htm) | Gets all elements not associated to stories. |
| Public method | [GetRelatedProducts](fa71bbad-420e-d073-7012-da63f6f4bd3e.htm) | Gets all products not associated to stories. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [PopExportState](719e062b-eea9-3010-33ad-e48dae367276.htm) | Resets the internal state of the exporter to process the previously active input element (if any), or the default state if the stack is empty. |
| Public method | [PopTransform](004039fe-8364-af98-6a51-7df026ea4fc0.htm) | Resets the internal transform of the exporter to process the previously active input element (if any), or the default transform if the stack is empty. |
| Public method | [PushExportState](84dee1b6-d008-e039-6f06-6e984920228c.htm) | Sets the internal state of the exporter to process the geometry and properties of the input element. |
| Public method | [PushTransform](bc1f8a42-7cbc-600a-9d1f-bcf80d6186e0.htm) | Sets the internal transform of the exporter to process the geometry and properties of the input element. |
| Public method | [RegisterDoorWindowForUncreatedOpening](688b2144-693c-544c-45db-e6257d21430b.htm) | Registers a door or window in the ExporterIFC's internal cache. The ids registered correspond to openings in walls which have not been processed and created yet. |
| Public method | [RegisterFaceWithElementHandle](f002582a-79a1-23b6-4278-2fabcb133444.htm) | Register face with element handle to make sure the openings created are related to the right element. |
| Public method | [RegisterSpaceBoundingElementHandle](9e2dc4fb-c062-f68d-af7f-fbbe7bd359e1.htm) | Stores a handle representing a space bounding element to the ExporterIFC's internal cache. |
| Public method | [RemoveBuildingStorey](e1dada57-54f4-ecbb-d3bf-75144f65c34e.htm) | Removes an IFCLevelInfo corresponding to a level from the exporter's internal cache. |
| Public method | [Set2DContextHandle](675a5b9e-9fa2-9dca-46c1-214197226adf.htm) | Sets the IfcRepresentationContext handle to be used for 2D entities (Annotations). |
| Public method | [Set3DContextHandle](94faf2de-158e-87bc-a9e0-ad0e6ff8eedc.htm) | Sets the IfcRepresentationContext or IfcRepresentationSubContext handle to be used for 3D entities (Model entities). |
| Public method | [SetFile](30eb507b-8796-ce4e-ec59-1684e1306a0f.htm) | Sets the handle to the IFC file being created during this export operation. |
| Public method | [SetMaterialIdForCurrentExportState](af494e73-5135-bd2b-8d71-389fa5be3ec7.htm) | This sets the material id that is to be associated with the element in the current export state. |
| Public method | [SetOwnerHistoryHandle](dbdb1fba-2cbb-1c18-56b8-f6f35bde1f3f.htm) | Sets the handle to the IfcOwnerHistory for the file. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ExportAs2x2](34c4b8b7-5e12-f337-c16e-23c3012916b0.htm) | Identifies if the file version being exported is 2x2. |
| Public property | [ExportAs2x3](975baaa5-5284-1672-7950-bb6e504df357.htm) | Identifies if the file version being exported is 2x3. |
| Public property | [ExportBaseQuantities](518cc0b7-934a-0110-0102-34aa932c4b0e.htm) | Identifies if the export should include IFC standard quantities currently supported by Revit. |
| Public property | [FileName](9b84d587-4fb1-5fdc-3f8a-c169081c99f5.htm) | The name of the IFC file being exported. |
| Public property | [FileVersion](246014d1-2004-762e-5ee2-6ea84356ff30.htm) | Identifies the file version being exported. |
| Public property | [IsValidObject](f42afa5b-2c19-2684-3ba5-8acf73fad2a1.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [SpaceBoundaryLevel](0beb0795-6270-5141-16df-e51e95acfa73.htm) | Identifies the level of space boundaries being exported. |
| Public property | [WallAndColumnSplitting](860fc0ad-a272-4cdd-9e0a-d360a492900d.htm) | Identifies if division of multi-level walls and columns by levels should take place during this export. |

# See Also

[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)