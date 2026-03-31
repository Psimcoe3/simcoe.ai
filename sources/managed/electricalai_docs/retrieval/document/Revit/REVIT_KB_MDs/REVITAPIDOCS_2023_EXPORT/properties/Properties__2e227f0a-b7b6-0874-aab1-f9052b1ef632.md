[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalServices.BuiltInExternalServices Members

---



|  |
| --- |
| [ExternalServices BuiltInExternalServices Class](f189eb3f-7a3a-2891-657a-e18cbf014987.htm)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in ExternalServiceId instances.

The  [ExternalServices BuiltInExternalServices](f189eb3f-7a3a-2891-657a-e18cbf014987.htm)  type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [AlignmentService](981a7fce-11a4-9898-c9f9-2e860c4e7f64.htm) | Autodesk Internal: The service for Infrastructure Alignments |
| Public property Static member | [ATFTranslationService](a3ead8b2-3659-64e5-446c-66aecb5401f6.htm) |  |
| Public property Static member | [AXMImporterService](aedb078a-9923-7147-7b26-29edd9275208.htm) | The external service which permits registration of an alternate implementation for AXM import. |
| Public property Static member | [CloudExternalService](5219470f-eb9f-0a96-1301-94e34152b8a6.htm) | The external service which supports get cloud model information from cloud servers such as C4R. |
| Public property Static member | [CodeCheckingParameterService](d40c4e5b-7760-e222-4adb-b559599134f5.htm) | The external service supporting view and modification of the structural code checking parameter in analytical elements. To use this service, programmers implement a server class that derives from  ICodeCheckingParameterServer  . |
| Public property Static member | [ConnectionTypeChangedService](a62d6e7b-9d2a-8eb1-fa57-0e00a7157437.htm) | The external service used to notify when structural connection changed the type. |
| Public property Static member | [DirectContext3DService](eb119187-a1f9-0f3f-0e75-8338d8a48cce.htm) | The external service that provides the facility to draw externally specified geometry in a Revit view in a way that is conceptually similar to a low-level graphics API. To use this service, programmers implement a server class that derives from Autodesk::Revit::DB::DirectContext3D::IDirectContext3DServer. |
| Public property Static member | [DuctFittingAndAccessoryPressureDropService](f9f90d3c-acbc-bb73-ce9e-3730c097f245.htm) | The external service Id which permits registration of an alternate implementation for duct fitting and accessory pressure drop calculation. To use this service, programmers implement a server class that derives from  IDuctFittingAndAccessoryPressureDropServer  . |
| Public property Static member | [DuctFittingAndAccessoryPressureDropUIService](e72d8ea8-98ee-9976-f514-fbe38f1d7182.htm) | The external service which permits registration of an alternate implementation for a duct fitting and accessory pressure drop calculation UI. To use this service, programmers implement a server class that derives from  IDuctFittingAndAccessoryPressureDropUIServer  . |
| Public property Static member | [DuctPressureDropService](81dd634f-cd45-bb04-4854-daff8ed7777a.htm) | The external service which permits registration of an alternate implementation for duct pressure drop calculation. To use this service, programmers implement a server class that derives from  IDuctPressureDropServer  . |
| Public property Static member | [ElectricalAnalyticalLoadSetUIService](378fa29c-ace2-e1d6-e558-729a9f1b8bd8.htm) | The UI service which permits registration of an external server for UI managing Electrical Analytical Load Set. |
| Public property Static member | [EntitlementExternalService](8a28bc7a-11cd-7ca5-c207-6b0c1dd00c93.htm) | The external service which supports get entitlement information. |
| Public property Static member | [ExternalDataManagerService](f2217980-7ebc-b90d-b623-0ec6768243cc.htm) |  |
| Public property Static member | [ExternalDataTypeService](67265a68-c9fe-f313-b491-fceadbaca51a.htm) | Unique service id. |
| Public property Static member | [ExternalParameterService](97afe6a1-147c-bc00-5ec8-a86f76230658.htm) | Autodesk Internal: The service for shared parameter selection. |
| Public property Static member | [ExternalResourceService](b697e2e7-0fe9-07a0-9722-ea7d7f56699a.htm) | The external service which permits registration of an alternate servers for managing external resources such as linked files. |
| Public property Static member | [ExternalResourceUIService](b5f92f62-4f0f-ecb9-9914-4155f6df9019.htm) | The external UI service Id which permits registration of an alternate servers for managing error messages which happen at the loading of the references to external resources such as linked files. |
| Public property Static member | [ExternalUIService](7aec9b28-3d5a-abcd-f487-afffa5504239.htm) | Unique service id. |
| Public property Static member | [FramingProfileService](bc3003b2-11c2-9dfe-46f5-3c29eead76db.htm) | The external service responsible for the generation of the fabrication profile. |
| Public property Static member | [GenericRepoHelperService](fb9286fd-8d3b-04a9-8bcc-1867a917bcf5.htm) | Unique service id. |
| Public property Static member | [HoleDefinitionService](e58d2019-340e-a195-16dd-70338bf2a9fa.htm) | The external service to view and modify hole definition parameters. |
| Public property Static member | [IFCEntityTreeUIService](7a8a2be5-1f3b-52f7-56a3-ffe14857f68e.htm) | The UI service which permits registration of an external server for new UI managing IFCEntity Selection |
| Public property Static member | [IFCExporterService](5afe33cc-fc32-879e-4f51-a0388b2bc8e6.htm) | The external service which permits registration of an alternate implementation for IFC export. |
| Public property Static member | [IFCImporterService](1e52565d-49d8-7081-4379-eba9508315a1.htm) | The external service which permits registration of an alternate implementation for IFC import. |
| Public property Static member | [MemberForcesService](53b97045-eed7-550b-9ed4-5797d1a0f9ca.htm) | The external service supporting view and modification of the member forces in analytical elements. The service is still under development and cannot be used. It means that no server can be external registered from it yet. |
| Public property Static member | [ModelAccessValidationService](9892a90c-e362-beb8-264e-94dc9e9ab88e.htm) | The external service which validates the access to Revit model such as Revit Cloud model. |
| Public property Static member | [ModifyConnectionParametersService](023078b4-3bd8-62a1-28f8-2f0014b3f044.htm) | The external service to view and modify structural connection parameters. |
| Public property Static member | [ModifyConnectionRangesService](bcd433a3-c772-b992-a341-ce454bfabe0a.htm) | The external service to view and modify structural connection ranges of applicability. |
| Public property Static member | [NavisworksExporterService](c0c5897c-315d-effd-e0ab-4627bf678134.htm) | The external service which supports export of the model to Navisworks. |
| Public property Static member | [PathOfTravelCalculationService](43e46774-f3c0-5be9-1b4e-4814a5699504.htm) | Autodesk Internal: The service for path of travel calculations |
| Public property Static member | [PipeFittingAndAccessoryPressureDropService](d415b108-1b39-bdc5-d11b-a9ac0b289221.htm) | The external service which permits registration of an alternate implementation for pipe fitting and accessory pressure drop calculation. To use this service, programmers implement a server class that derives from  IPipeFittingAndAccessoryPressureDropServer  . |
| Public property Static member | [PipeFittingAndAccessoryPressureDropUIService](05be9167-98d5-42f9-9118-d2361292f410.htm) | The external service which permits registration of an alternate implementation for a pipe fitting and accessory pressure drop calculation UI. To use this service, programmers implement a server class that derives from  IPipeFittingAndAccessoryPressureDropUIServer  . |
| Public property Static member | [PipeFrictionFactorService](c121c2bf-1a7c-c3b2-4f44-b51ec6b7cae6.htm) | Pipe friction factor service id |
| Public property Static member | [PipePlumbingFixtureFlowService](b6d5fbde-e368-ff55-b370-fff3db1f7cde.htm) | The external service which permits registration of an alternate implementation for pipe fixture flow calculation. To use this service, programmers implement a server class that derives from  IPipePlumbingFixtureFlowServer  . |
| Public property Static member | [PipePressureDropService](fc160a77-9b51-6df5-a4e3-bf3f16ec3a8c.htm) | The external service which permits registration of an alternate implementation for pipe pressure drop calculation. To use this service, programmers implement a server class that derives from  IPipePressureDropServer  . |
| Public property Static member | [RebarUpdateService](a89644f0-3624-d4e5-fbb6-4f5525d7efee.htm) | Autodesk Internal: The service for updating rebar freeform elements |
| Public property Static member | [SiteInsertService](256ced3f-2af9-482b-6cbf-8ac7774d4321.htm) | The external service which permits registration of an alternate implementation for Site insert. |
| Public property Static member | [SiteLinkerUIService](53745637-c352-75f7-cc20-a47a81c9d92b.htm) | The external UI service which permits registration of an alternate servers for new UI of link topography |
| Public property Static member | [SnappingService](6f58060b-3570-8e09-46c7-8f1875705f03.htm) | Autodesk Internal: The service which provides snap points and lines |
| Public property Static member | [StructuralSectionsService](cbdcebe7-2ef4-d848-6a01-858c2300988d.htm) | The external service supporting view and modification of the structural sections shape in structural elements. The service is still under development and cannot be used. It means that no server can be external registered from it yet. |
| Public property Static member | [TemporaryGraphicsHandlerService](6a94cec2-eabe-8669-e851-7ddbb7b2425c.htm) | The external service Id which permits registration of an callback handler for temporary graphics objects managed by  [!:Autodesk::Revit::DB::TemporaryGraphicsManager]  . To use this service, developers implement a server class that derives from  [!:Autodesk::Revit::UI::ITemporaryGraphicsHandler]  . |
| Public property Static member | [ViewSheetSetUIService](d47040f8-082d-cda1-b7aa-993fd9132d53.htm) | The UI service which permits registration of an external server for new UI managing ViewSheetSet. |

# See Also

[ExternalServices BuiltInExternalServices Class](f189eb3f-7a3a-2891-657a-e18cbf014987.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)