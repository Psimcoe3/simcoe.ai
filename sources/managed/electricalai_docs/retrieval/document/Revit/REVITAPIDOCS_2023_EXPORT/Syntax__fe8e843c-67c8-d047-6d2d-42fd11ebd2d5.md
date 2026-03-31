[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportSlabAsExtrusion Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static bool ExportSlabAsExtrusion( 	ExporterIFC exporterIFC, 	Element pCeilingAndFloor, 	GeometryElement pGRep, 	IFCTransformSetter pTmpTrfSetter, 	IFCAnyHandle localPlacement, 	out IList<IFCAnyHandle> localPlacementAnyArr, 	out IList<IFCAnyHandle> reps, 	out IList<IList<CurveLoop>> extrusionLoops, 	out IList<IFCExtrusionCreationData> loopExtraParams, 	Plane plane ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ExportSlabAsExtrusion ( _ 	exporterIFC As ExporterIFC, _ 	pCeilingAndFloor As Element, _ 	pGRep As GeometryElement, _ 	pTmpTrfSetter As IFCTransformSetter, _ 	localPlacement As IFCAnyHandle, _ 	<OutAttribute> ByRef localPlacementAnyArr As IList(Of IFCAnyHandle), _ 	<OutAttribute> ByRef reps As IList(Of IFCAnyHandle), _ 	<OutAttribute> ByRef extrusionLoops As IList(Of IList(Of CurveLoop)), _ 	<OutAttribute> ByRef loopExtraParams As IList(Of IFCExtrusionCreationData), _ 	plane As Plane _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ExportSlabAsExtrusion( 	ExporterIFC^ exporterIFC,  	Element^ pCeilingAndFloor,  	GeometryElement^ pGRep,  	IFCTransformSetter^ pTmpTrfSetter,  	IFCAnyHandle^ localPlacement,  	[OutAttribute] IList<IFCAnyHandle^>^% localPlacementAnyArr,  	[OutAttribute] IList<IFCAnyHandle^>^% reps,  	[OutAttribute] IList<IList<CurveLoop^>^>^% extrusionLoops,  	[OutAttribute] IList<IFCExtrusionCreationData^>^% loopExtraParams,  	Plane^ plane ) ``` |

#### Parameters

exporterIFC
:   Type:  [Autodesk.Revit.DB.IFC ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.htm)

pCeilingAndFloor
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

pGRep
:   Type:  [Autodesk.Revit.DB GeometryElement](09eaeb08-58bb-8049-8925-f3a5aa846fdc.htm)

pTmpTrfSetter
:   Type:  [Autodesk.Revit.DB.IFC IFCTransformSetter](75b9525d-3b8d-70d8-55de-a193b9eb5e76.htm)

localPlacement
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)

localPlacementAnyArr
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)   %

reps
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)   %

extrusionLoops
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)   %

loopExtraParams
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [IFCExtrusionCreationData](9447a335-6861-0533-6896-e6ff1fd41761.htm)   %

plane
:   Type:  [Autodesk.Revit.DB Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)