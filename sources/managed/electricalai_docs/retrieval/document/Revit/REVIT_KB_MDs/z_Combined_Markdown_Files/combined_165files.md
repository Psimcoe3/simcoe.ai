

<!-- Start of Syntax__088afc2a-b150-9d1e-4af8-319acad99828.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GeoCoordinateSystemDefinition Property

---



|  |
| --- |
| [SiteLocation Class](9d71159d-514c-c1b3-8673-5c0e7f28b688.htm)   [See Also](#seeAlsoToggle) |

The XML string which describes the geographic coordinate system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public string GeoCoordinateSystemDefinition { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property GeoCoordinateSystemDefinition As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ GeoCoordinateSystemDefinition { 	String^ get (); } ``` |

# Remarks

If the site does not have a geographic coordinate system, it returns an empty string for this property.

# See Also

[SiteLocation Class](9d71159d-514c-c1b3-8673-5c0e7f28b688.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__088c995c-1d57-efd5-bc7f-7f9a193018aa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveAdaptiveComponentInstance Method

---



|  |
| --- |
| [AdaptiveComponentInstanceUtils Class](786db8ac-a051-37e4-7b4c-dbf286fe9a7c.htm)   [See Also](#seeAlsoToggle) |

Moves Adaptive Component Instance by the specified transformation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static void MoveAdaptiveComponentInstance( 	FamilyInstance famInst, 	Transform trf, 	bool unHost ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub MoveAdaptiveComponentInstance ( _ 	famInst As FamilyInstance, _ 	trf As Transform, _ 	unHost As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void MoveAdaptiveComponentInstance( 	FamilyInstance^ famInst,  	Transform^ trf,  	bool unHost ) ``` |

#### Parameters

famInst
:   Type:  [Autodesk.Revit.DB FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)    
     The FamilyInstance

trf
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     The Transformation

unHost
:   Type:  System Boolean    
     True if the move should disassociate the Point Element Refs from their hosts. False if the Point Element Refs remain hosted.

# Remarks

This method will attempt a rigid body motion of all the individual references and hence the instance itself. However if unHost parameter is 'false' and any of the instance's references are hosted to any geometry, then those references will move within the constraints. The instance then adapts to where its references are moved to.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | trf is not a rigid body transformation. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Unable to move the adaptive component instance. |

# See Also

[AdaptiveComponentInstanceUtils Class](786db8ac-a051-37e4-7b4c-dbf286fe9a7c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__089c01dd-030f-2621-cf30-0e60cb7c5868.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VariesAcrossGroups Property

---



|  |
| --- |
| [InternalDefinition Class](97f42435-3067-622e-7a34-919f42f6ab97.htm)   [See Also](#seeAlsoToggle) |

Whether or not the parameter values can vary across group members.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool VariesAcrossGroups { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property VariesAcrossGroups As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool VariesAcrossGroups { 	bool get (); } ``` |

#### Field Value

True if the values of this parameter can vary across the related members of group instances. False if the values will be consistent across the related members in group instances.

# See Also

[InternalDefinition Class](97f42435-3067-622e-7a34-919f42f6ab97.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__089c388d-6531-0022-4500-961bb03e433b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotDrawRoofError Property

---



|  |
| --- |
| [BuiltInFailures CreationFailures Class](62f22d53-ffd1-5c31-12c2-9bf34a79f079.htm)   [See Also](#seeAlsoToggle) |

Can't make roof.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotDrawRoofError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotDrawRoofError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotDrawRoofError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CreationFailures Class](62f22d53-ffd1-5c31-12c2-9bf34a79f079.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__089c5517-8e5d-7c74-b53b-d59dacb06c5d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [ExportPDFSettings Class](66156539-3f22-d986-ea46-49e772d1c451.htm)   [See Also](#seeAlsoToggle) |

Returns an new created ExportPDFSettings element in the document with specified settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static ExportPDFSettings Create( 	Document document, 	string name, 	PDFExportOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	name As String, _ 	options As PDFExportOptions _ ) As ExportPDFSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: static ExportPDFSettings^ Create( 	Document^ document,  	String^ name,  	PDFExportOptions^ options ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document where the settings will be created.

name
:   Type:  System String    
     Name to the settings.

options
:   Type:  [Autodesk.Revit.DB PDFExportOptions](e4236fc8-f8e7-fc74-1b81-9e3a4d9e966b.htm)    
     The options to be set.

#### Return Value

New instance of ExportPDFSettings just created in the document.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name is an empty string or contains only whitespace. -or- name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". -or- Setting name. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[ExportPDFSettings Class](66156539-3f22-d986-ea46-49e772d1c451.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__090c0da6-db59-d1e6-5dcf-4335c531ee9f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [RevisionCloud Class](43bdb2c4-2b9c-e3fa-4d6a-8c9970a9f7b6.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new RevisionCloud in the model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static RevisionCloud Create( 	Document document, 	View view, 	ElementId revisionId, 	IList<Curve> curves ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	view As View, _ 	revisionId As ElementId, _ 	curves As IList(Of Curve) _ ) As RevisionCloud ``` |

 

| Visual C++ |
| --- |
| ``` public: static RevisionCloud^ Create( 	Document^ document,  	View^ view,  	ElementId^ revisionId,  	IList<Curve^>^ curves ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which the RevisionCloud should be created.

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The View in which the RevisionCloud should appear.

revisionId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The Revision to associate with the new RevisionCloud.

curves
:   Type:  System.Collections.Generic IList   [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The curves that will form the RevisionCloud's sketch.

#### Return Value

The newly created RevisionCloud.

# Remarks

Creates a new RevisionCloud in the specified View. The new RevisionCloud will be associated with the specified Revision. RevisionClouds can only be created if the Revision has not yet been issued.

RevisionClouds can be created in most graphical Views, excepting 3D views and graphical column schedules. Unlike most other Elements, RevisionClouds can be created directly on a ViewSheet.

RevisionClouds are created based on a series of sketched curves. There is no requirement that the curves form closed loops and self-intersections are also permitted. The curves will be automatically projected onto the appropriate plane for the View. The list of curves cannot be empty and any lines cannot be perpendicular to the View's plane. If the View is a model View, the coordinates specified for the curves will be interpreted in model space. If the View is a non-model View (such as a ViewSheet) then the coordinates will be interpreted in the View's space.

The cloud graphics will be attached to the curves under the assumption that each curve is oriented in a clockwise direction. For lines, this means that the outside of the cloud is in the direction of the line's normal vector within the View's plane. Any closed loops should therefore be oriented clockwise to create the typical cloud shape.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void CreateRevisionCloudInActiveView(Document document, Revision revision, IList<Curve> curves)
{
    using (Transaction newRevisionCloud = new Transaction(document, "Create Revision Cloud"))
    {
        newRevisionCloud.Start();
        // Can only create revision cloud for revision that is not issued
        if (revision.Issued == false)
        {
            RevisionCloud.Create(document, document.ActiveView, revision.Id, curves);
            newRevisionCloud.Commit();
        }
        else
        {
            newRevisionCloud.RollBack();
        }
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub CreateRevisionCloudInActiveView(document As Document, revision As Revision, curves As IList(Of Curve))
    Using newRevisionCloud As New Transaction(document, "Create Revision Cloud")
        newRevisionCloud.Start()
        ' Can only create revision cloud for revision that is not issued
        If revision.Issued = False Then
            RevisionCloud.Create(document, document.ActiveView, revision.Id, curves)
            newRevisionCloud.Commit()
        Else
            newRevisionCloud.RollBack()
        End If
    End Using
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- revisionId is not a valid Revision. -or- This operation cannot be performed because revisionId is an issued Revision. -or- view is not a View that can support RevisionClouds. -or- The provided Curves curves cannot be used as the basis for a RevisionCloud. Either the list is empty or one or more of the Curves could not be projected onto the View's plane. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RevisionCloud Class](43bdb2c4-2b9c-e3fa-4d6a-8c9970a9f7b6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__090cf63a-e63b-9468-586a-7a0140173e16.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DecalHeight Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Height"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DecalHeight { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DecalHeight As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DecalHeight { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__090ee075-cff2-fd8d-5a1a-6c79a7c50a4b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDocument Method

---



|  |
| --- |
| [GeometryInstance Class](fe25b14f-5866-ca0f-a660-c157484c3a56.htm)   [See Also](#seeAlsoToggle) |

Gets the document that contains the symbol of this instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public Document GetDocument() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDocument As Document ``` |

 

| Visual C++ |
| --- |
| ``` public: Document^ GetDocument() ``` |

#### Return Value

Returns the document that contains the symbol of this instance.

# See Also

[GeometryInstance Class](fe25b14f-5866-ca0f-a660-c157484c3a56.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__091b888e-4712-9cd4-32ca-3932de0c13c3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRenderingQualitySettings Method

---



|  |
| --- |
| [RenderingSettings Class](7ba669f3-bd38-464b-f3f7-8a0b4e513a0a.htm)   [See Also](#seeAlsoToggle) |

Returns an object that represents the rendering quality settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public RenderingQualitySettings GetRenderingQualitySettings() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRenderingQualitySettings As RenderingQualitySettings ``` |

 

| Visual C++ |
| --- |
| ``` public: RenderingQualitySettings^ GetRenderingQualitySettings() ``` |

#### Return Value

The rendering quality settings.

# See Also

[RenderingSettings Class](7ba669f3-bd38-464b-f3f7-8a0b4e513a0a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__091e627f-bad4-cfd8-5a2a-bda3157e6d0f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadLinearForceFx2 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Fx 2"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LoadLinearForceFx2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoadLinearForceFx2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LoadLinearForceFx2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87a734f3-ccd0-78cc-a2f5-f5f2ef6fb9be.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AssociatedBuildingPadId Property

---



|  |
| --- |
| [TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.htm)   [See Also](#seeAlsoToggle) |

The element id of the building pad which causes this topography surface to be formed.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public ElementId AssociatedBuildingPadId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property AssociatedBuildingPadId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ AssociatedBuildingPadId { 	ElementId^ get (); } ``` |

# Remarks

InvalidElementId returned signals that there is no associated building pad.

# See Also

[TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__87a7be79-852d-6ac8-208d-e90fe98a9086.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImportSymbolBaseLevelInvalid Property

---



|  |
| --- |
| [BuiltInFailures ImportFailures Class](37a5e9d1-ffe4-363f-2033-1cabbf5634aa.htm)   [See Also](#seeAlsoToggle) |

An import instance has become invalid. The host work plane of the import can no longer be used. Click "Rehost" to maintain the position of the import and rehost its work plane to the lowest level.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ImportSymbolBaseLevelInvalid { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ImportSymbolBaseLevelInvalid As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ImportSymbolBaseLevelInvalid { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ImportFailures Class](37a5e9d1-ffe4-363f-2033-1cabbf5634aa.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87a7da58-056c-970b-b08f-ee94c209b077.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TotalCoefficient Property

---



|  |
| --- |
| [MEPSection Class](a618b793-4084-a631-191a-043aac84d039.htm)   [See Also](#seeAlsoToggle) |

The loss coefficient of the section.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double TotalCoefficient { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property TotalCoefficient As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double TotalCoefficient { 	double get (); } ``` |

# Remarks

It's total of all fittings and segments. Coefficient is a number. The unit type is UT\_Number.

# See Also

[MEPSection Class](a618b793-4084-a631-191a-043aac84d039.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__87a9e2e8-a675-10a9-b8c5-a3b1e7db2535.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsResourceWellFormed Method

---



|  |
| --- |
| [IExternalResourceServer Interface](c2ad8eee-b358-012b-a09b-8fbc3229652d.htm)   [See Also](#seeAlsoToggle) |

Implement this method to check whether the given ExternalResourceReference is formatted correctly for this server.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` bool IsResourceWellFormed( 	ExternalResourceReference extRef ) ``` |

 

| Visual Basic |
| --- |
| ``` Function IsResourceWellFormed ( _ 	extRef As ExternalResourceReference _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` bool IsResourceWellFormed( 	ExternalResourceReference^ extRef ) ``` |

#### Parameters

extRef
:   Type:  [Autodesk.Revit.DB ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.htm)    
     The ExternalResourceReference to check.

#### Return Value

True if the ExternalResourceReference represents a well-formed resource. False otherwise.

# Remarks

Different servers will have different requirements.

A server which loads references from a website might require that the reference map contain a key called "URL" and a value that is a valid URL.

A server which loads references from a network drive might require a key called "Drive" with a value that represents a drive name, plus a key called "Path" with a value that corresponds to a path relative to the root of the drive.

This function should not check that the resource exists on the server. It should only check that the resource is formatted correctly.

# See Also

[IExternalResourceServer Interface](c2ad8eee-b358-012b-a09b-8fbc3229652d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87b03ae6-a808-7180-30e6-b22fac2d5168.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportObjectData Property

---



|  |
| --- |
| [DWFExportOptions Class](e83b223d-b846-027e-8859-7ea5b89ea685.htm)   [See Also](#seeAlsoToggle) |

Whether to include properties associated with elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool ExportObjectData { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExportObjectData As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ExportObjectData { 	bool get (); 	void set (bool value); } ``` |

# Remarks

ExportObjectData must be enabled (true) in order to also enable exporting rooms and areas (ExportingAreas). If ExportObjectData is disabled, the ExportingAreas property will be ignored.

# See Also

[DWFExportOptions Class](e83b223d-b846-027e-8859-7ea5b89ea685.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87b08f87-6c4a-054d-1ff1-1bed4ee9db62.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TransactionFailedWarn Property

---



|  |
| --- |
| [BuiltInFailures GeneralFailures Class](d4679f32-45d9-bec2-e0ff-168c3aee6de9.htm)   [See Also](#seeAlsoToggle) |

[Description]

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId TransactionFailedWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TransactionFailedWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ TransactionFailedWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GeneralFailures Class](d4679f32-45d9-bec2-e0ff-168c3aee6de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87b4d0ea-c7bb-8063-b4d4-c81b9213ca55.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalResourceType Property

---



|  |
| --- |
| [ImageType Class](c6213f81-8dc8-158e-0522-70f87e9bdbb9.htm)   [See Also](#seeAlsoToggle) |

The type of external resources that represents images.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public static ExternalResourceType ExternalResourceType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ExternalResourceType As ExternalResourceType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ExternalResourceType^ ExternalResourceType { 	ExternalResourceType^ get (); } ``` |

# See Also

[ImageType Class](c6213f81-8dc8-158e-0522-70f87e9bdbb9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87b78710-ab83-e54d-7649-8b82fedd3632.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRowHeight Method

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Returns a row's height in feet

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double GetRowHeight( 	int nRow ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRowHeight ( _ 	nRow As Integer _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetRowHeight( 	int nRow ) ``` |

#### Parameters

nRow
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given row number nRow is invalid. |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87b87625-91d5-4e99-a4a3-58357bf8b0a7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpotElevationLostEdgeReferences Property

---



|  |
| --- |
| [BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)   [See Also](#seeAlsoToggle) |

Some Spot Dimensions lost their References. Those Spot Dimensions will be deleted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SpotElevationLostEdgeReferences { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpotElevationLostEdgeReferences As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SpotElevationLostEdgeReferences { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87bc8919-4eee-ac76-2e94-4a3d70e2826c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, ElementId, ElementId, ElementId, IList(XYZ))

---



|  |
| --- |
| [FlexPipe Class](4b0e0656-4760-4a91-a777-ce50869a827a.htm)   [See Also](#seeAlsoToggle) |

Creates a new flexible pipe into the document, using a point array and flex pipe type.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static FlexPipe Create( 	Document document, 	ElementId systemTypeId, 	ElementId pipeTypeId, 	ElementId levelId, 	IList<XYZ> points ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	systemTypeId As ElementId, _ 	pipeTypeId As ElementId, _ 	levelId As ElementId, _ 	points As IList(Of XYZ) _ ) As FlexPipe ``` |

 

| Visual C++ |
| --- |
| ``` public: static FlexPipe^ Create( 	Document^ document,  	ElementId^ systemTypeId,  	ElementId^ pipeTypeId,  	ElementId^ levelId,  	IList<XYZ^>^ points ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

systemTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the piping system type.

pipeTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the flexible pipe.

levelId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The level id for the flexible pipe.

points
:   Type:  System.Collections.Generic IList   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The point array indicating the path of the flexible pipe, including the end point.

#### Return Value

If creation was successful then a new flexible pipe is returned, otherwise an exception with failure information will be thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The systemTypeId is not valid piping system type. -or- The type pipeTypeId is not valid flexible pipe type. -or- The ElementId levelId is not a Level. -or- The valid number of points is less than two. In order to create a flex curve, at least two points are required. Note the duplicate points don't take into account. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[FlexPipe Class](4b0e0656-4760-4a91-a777-ce50869a827a.htm)

[Create Overload](1d67d898-28eb-647e-5ece-4982613de792.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__87be3885-b1aa-ba8c-f82e-a5a0f7455c3a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProjectLocations Property

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Retrieve all the project locations associated with this project

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ProjectLocationSet ProjectLocations { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ProjectLocations As ProjectLocationSet 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ProjectLocationSet^ ProjectLocations { 	ProjectLocationSet^ get (); } ``` |

# Remarks

This property returns all the locations of the project. A project can have one site location but many project locations within that site. Each project location object is an offset and rotation from the site location.

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87c25f73-664f-3ab5-b916-106ced80d75f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ClearWebHeight Property

---



|  |
| --- |
| [StructuralSectionCParallelFlange Class](b57802df-6b61-72c0-d4c9-ab2b7449696e.htm)   [See Also](#seeAlsoToggle) |

Detailing depth between the web toes of the fillets, in.(mm)

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public double ClearWebHeight { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ClearWebHeight As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ClearWebHeight { 	double get (); 	void set (double value); } ``` |

# See Also

[StructuralSectionCParallelFlange Class](b57802df-6b61-72c0-d4c9-ab2b7449696e.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__87c916ca-4e5a-15a3-3aef-d0f65a796a3f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### memberTypeKey Property

---



|  |
| --- |
| [TrussMemberInfo Class](4d22fb31-c93c-7d65-31c3-49175eb3469d.htm)   [See Also](#seeAlsoToggle) |

Kind of the member in the truss.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public TrussMemberType memberTypeKey { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property memberTypeKey As TrussMemberType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property TrussMemberType memberTypeKey { 	TrussMemberType get (); 	void set (TrussMemberType value); } ``` |

# See Also

[TrussMemberInfo Class](4d22fb31-c93c-7d65-31c3-49175eb3469d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__87cb048e-99cf-0ef3-5326-45ad795e9482.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DimLeaderArrowhead Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Tick Mark"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DimLeaderArrowhead { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DimLeaderArrowhead As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DimLeaderArrowhead { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87d195c8-6a51-0f61-3bbc-c9f7d54dc567.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceRotation Property

---



|  |
| --- |
| [AdvancedMetal Class](762ef4cc-3219-0f8a-8cd5-137e20225eb0.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Rotation" from the "AdvancedMetal" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string SurfaceRotation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SurfaceRotation As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ SurfaceRotation { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble". This property allows a connected asset.

# See Also

[AdvancedMetal Class](762ef4cc-3219-0f8a-8cd5-137e20225eb0.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__87d53eae-bd18-3ff0-e5e6-38de5a018cdf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetNamingRule Method

---



|  |
| --- |
| [PDFExportOptions Class](e4236fc8-f8e7-fc74-1b81-9e3a4d9e966b.htm)   [See Also](#seeAlsoToggle) |

Sets the naming rule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void SetNamingRule( 	IList<TableCellCombinedParameterData> namingRule ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetNamingRule ( _ 	namingRule As IList(Of TableCellCombinedParameterData) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetNamingRule( 	IList<TableCellCombinedParameterData^>^ namingRule ) ``` |

#### Parameters

namingRule
:   Type:  System.Collections.Generic IList   [TableCellCombinedParameterData](f2303148-6e5e-d143-3725-3ac12c04ea86.htm)    
     The naming rule.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The namingRule is empty or contains illegal characters. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PDFExportOptions Class](e4236fc8-f8e7-fc74-1b81-9e3a4d9e966b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87d62116-cdb4-efc4-e2e2-e4f5b41b3441.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetExecutionOrder Method

---



|  |
| --- |
| [UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.htm)   [See Also](#seeAlsoToggle) |

Forces execution order between two updaters Execution order: first before second

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static void SetExecutionOrder( 	UpdaterId first, 	UpdaterId second ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SetExecutionOrder ( _ 	first As UpdaterId, _ 	second As UpdaterId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SetExecutionOrder( 	UpdaterId^ first,  	UpdaterId^ second ) ``` |

#### Parameters

first
:   Type:  [Autodesk.Revit.DB UpdaterId](16a9604f-51bd-ce34-f145-17ae06b7c1cf.htm)    
     Id of first Updater

second
:   Type:  [Autodesk.Revit.DB UpdaterId](16a9604f-51bd-ce34-f145-17ae06b7c1cf.htm)    
     Id of second Updater

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One or both inputs are not valid UpdaterIds -or- One or both of the Updaters are not registered -or- first and second are the same id |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | The updaters do not report the same ChangePriority |

# See Also

[UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87d64bab-218f-7dab-8e0a-7e2a8be2543f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRepresentations Method

---



|  |
| --- |
| [IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)   [See Also](#seeAlsoToggle) |

Gets the representation handles created representing the processed geometry and stored in this object.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ICollection<IFCAnyHandle> GetRepresentations() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRepresentations As ICollection(Of IFCAnyHandle) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<IFCAnyHandle^>^ GetRepresentations() ``` |

#### Return Value

The collection of representation handles.

# See Also

[IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__87d8a88c-906e-85a9-f575-f263788b8584.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Parameter Property (Definition)

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Retrieves a parameter from the element based on its definition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Parameter this[ 	Definition definition ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Parameter ( _ 	definition As Definition _ ) As Parameter 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Parameter^ Parameter[Definition^ definition] { 	Parameter^ get (Definition^ definition); } ``` |

#### Parameters

definition
:   Type:  [Autodesk.Revit.DB Definition](8fe04f37-04e1-9e93-ffdb-e3900908e42a.htm)    
     The internal or external definition of the parameter.

# Remarks

Parameters are a generic form of data storage within elements. The parameters are visible through the Autodesk Revit user interface in the Element Properties dialog. An element can only have one instance of a parameter with a specific definition. By using this method you can retrieve that parameter based on definition.

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Parameter Overload](a742d71a-b415-9e99-2978-abd3b5bae7f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87dd3a6a-97e8-6b89-7ac9-b495d109996b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetConstraints Method

---



|  |
| --- |
| [RebarShapeSegment Class](4fd9ba08-b5a3-39c8-9666-fc0a105615c6.htm)   [See Also](#seeAlsoToggle) |

Retrieve the list of constraints associated with this segment.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<RebarShapeConstraint> GetConstraints() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetConstraints As IList(Of RebarShapeConstraint) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<RebarShapeConstraint^>^ GetConstraints() ``` |

#### Return Value

The list of constraints.

# See Also

[RebarShapeSegment Class](4fd9ba08-b5a3-39c8-9666-fc0a105615c6.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__87e2b7d1-c42c-8c24-fdd2-21ee5f757800.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [ExportFontTable Class](b3b4f237-f7f3-ced4-be3d-721f7ac05832.htm)   [See Also](#seeAlsoToggle) |

Removes all contents stored in the table.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Clear() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Clear ``` |

 

| Visual C++ |
| --- |
| ``` public: void Clear() ``` |

# See Also

[ExportFontTable Class](b3b4f237-f7f3-ced4-be3d-721f7ac05832.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87e64330-90d4-c6bb-944d-d2dbb1529948.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPlane Method

---



|  |
| --- |
| [CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)   [See Also](#seeAlsoToggle) |

Gets the plane of the curve loop, if it is planar.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public Plane GetPlane() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPlane As Plane ``` |

 

| Visual C++ |
| --- |
| ``` public: Plane^ GetPlane() ``` |

#### Return Value

The plane of the curve loop.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The curve loop does not lie in a single plane. |

# See Also

[CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87e6bdea-ffa7-fdf1-d190-db9ae56e9bb3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RevealHiddenElements Property

---



|  |
| --- |
| [TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.htm)   [See Also](#seeAlsoToggle) |

The current state of the RevealHiddenElements mode in the associated view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public bool RevealHiddenElements { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RevealHiddenElements As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool RevealHiddenElements { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The RevealHiddenElements mode is either disabled or inapplicable in the associated view. |

# See Also

[TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87e73d21-a6db-d252-3921-edf499500468.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EndJoinCutback Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"End Join Cutback"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId EndJoinCutback { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property EndJoinCutback As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ EndJoinCutback { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87e9896d-863b-22e0-482c-92e032d42144.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)   [See Also](#seeAlsoToggle) |

Creates a new RebarBarType object

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static RebarBarType Create( 	Document ADoc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	ADoc As Document _ ) As RebarBarType ``` |

 

| Visual C++ |
| --- |
| ``` public: static RebarBarType^ Create( 	Document^ ADoc ) ``` |

#### Parameters

ADoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__87e9a80c-7e7d-4087-035d-dd993abee73c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Name Property

---



|  |
| --- |
| [ModuleSettings Class](2a0c5aed-a80e-6c91-0525-ad8d42d613a6.htm)   [See Also](#seeAlsoToggle) |

The module name.

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPIMacros  (in RevitAPIMacros.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public string Name { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Name As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Name { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ModuleSettings Class](2a0c5aed-a80e-6c91-0525-ad8d42d613a6.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)

<!-- Start of Syntax__87eecc9e-09a0-4f7c-0b7d-d1930b363b53.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StoryAboveMoved Property

---



|  |
| --- |
| [BuiltInFailures LevelFailures Class](fda0bd98-2636-3483-fb7e-de406b1bd252.htm)   [See Also](#seeAlsoToggle) |

The level set as the Story Above for these levels has moved below these levels. This change will cause these levels to revert to the default Story Above.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId StoryAboveMoved { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StoryAboveMoved As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ StoryAboveMoved { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures LevelFailures Class](fda0bd98-2636-3483-fb7e-de406b1bd252.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87f3e9ad-042d-6ef8-a1f7-c12ebfcac7d7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalResourceUIBrowseResultType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Describes the type of external resource browsing result.

Describes the type of external resource browsing result.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public enum ExternalResourceUIBrowseResultType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ExternalResourceUIBrowseResultType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ExternalResourceUIBrowseResultType ``` |

# Members

| Member name | Description |
| --- | --- |
| Success | There is no predefined error happened during this browse operation. The DB server can store any errors itself in this case. |
| FolderNotFound | The specified external resource folder cannot be found by external resource server. |
| ResourceNotFound | The specified external resource cannot be found by external resource server. |

# Remarks

This enum is used to describe the type of external resources browsing operation result ( the browsing operation include list folders and resources of an external server or a folder, or open an external resource in browsing dialog.) The meaning of each enum value:

* There is no predefined error happened during this browse operation. The DB server can store any errors itself in this case.
* FolderNotFound means the external resource folder want to browse could not be founded in external server.
* ResourceNotFound means the external resource want to open could not be founded in external server.

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87f5b053-2c42-7b57-a58d-4b2489f461cc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FileImportedEventArgs Class

---



|  |
| --- |
| [Members](e4b85914-1008-e826-0246-e7baf888c7d8.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by the FileImported event.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public class FileImportedEventArgs : RevitAPIPostDocEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FileImportedEventArgs _ 	Inherits RevitAPIPostDocEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FileImportedEventArgs : public RevitAPIPostDocEventArgs ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPostEventArgs](93554f52-0145-3454-5697-3f1015e46434.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPostDocEventArgs](7d3fba7a-5efb-6a4c-a49c-16c25f972830.htm)    
  Autodesk.Revit.DB.Events FileImportedEventArgs

# See Also

[FileImportedEventArgs Members](e4b85914-1008-e826-0246-e7baf888c7d8.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__87f69e88-bc72-c3b3-c294-cc6e61344f85.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsPipeTypeParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Pipe Type"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsPipeTypeParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsPipeTypeParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsPipeTypeParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87f92ee2-7560-ea25-d04a-de3e772043be.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyParameterSet Constructor

---



|  |
| --- |
| [FamilyParameterSet Class](f2ee1ee9-0605-9353-b83b-57db865119fc.htm)   [See Also](#seeAlsoToggle) |

Initializes a new instance of the  [FamilyParameterSet](f2ee1ee9-0605-9353-b83b-57db865119fc.htm)  class

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyParameterSet() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: FamilyParameterSet() ``` |

# See Also

[FamilyParameterSet Class](f2ee1ee9-0605-9353-b83b-57db865119fc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87f96f35-e3bf-42a7-829a-e2a63834f49d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FtOfWater Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol FT, indicating unit Feet of water (39.2 Â°F).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FtOfWater { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FtOfWater As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FtOfWater { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87ffc778-3ed5-568d-ccb9-61105bc03171.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecCircuitWireNumRunsParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"# of Runs"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecCircuitWireNumRunsParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecCircuitWireNumRunsParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecCircuitWireNumRunsParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88a11273-7d05-76e7-9613-0de1b5335d13.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BadReferenceToSecondaryWarn Property

---



|  |
| --- |
| [BuiltInFailures DesignOptionFailures Class](306b7ebc-5d5e-e53f-d5e4-9a5da4162068.htm)   [See Also](#seeAlsoToggle) |

No element in a secondary Option can be referenced by an element outside that Option.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId BadReferenceToSecondaryWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BadReferenceToSecondaryWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ BadReferenceToSecondaryWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DesignOptionFailures Class](306b7ebc-5d5e-e53f-d5e4-9a5da4162068.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88a5ae8c-cb5f-4f64-dc25-9a5be661c26e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetThermalProperties Method

---



|  |
| --- |
| [FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)   [See Also](#seeAlsoToggle) |

Sets the thermal properties for the given FamilySymbol.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetThermalProperties( 	FamilyThermalProperties thermalProperties ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetThermalProperties ( _ 	thermalProperties As FamilyThermalProperties _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetThermalProperties( 	FamilyThermalProperties^ thermalProperties ) ``` |

#### Parameters

thermalProperties
:   Type:  [Autodesk.Revit.DB FamilyThermalProperties](9d9b2125-8398-9b55-8219-cbda4456ab7b.htm)    
     The new thermal properties. If    a null reference (  Nothing  in Visual Basic)  , this unsets custom thermal properties for this FamilySymbol.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The thermal properties are not valid for assignment. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FamilySymbol does not contain thermal properties. |

# See Also

[FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88a7bfc8-cc82-5134-c5fb-6d9e322430d7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FloorAttrDefaultThicknessParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Default Thickness"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FloorAttrDefaultThicknessParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FloorAttrDefaultThicknessParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FloorAttrDefaultThicknessParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88a99694-968a-99f7-870a-f46737bd5927.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportLayerInfo Class

---



|  |
| --- |
| [Members](38ec2833-de1c-d8ad-8388-307607bb852a.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A value used to represent the info stored in the  [ExportLayerTable](e68ce1c7-a922-d1b7-53bb-f832a4bad273.htm)  .

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class ExportLayerInfo : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExportLayerInfo _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExportLayerInfo : IDisposable ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public bool ExportDWGModifyLayerTable(Document document, View view)
{
    bool exported = false;
    IList<string> setupNames = BaseExportOptions.GetPredefinedSetupNames(document);
    if (setupNames.Count > 0)
    {
        // Get the export options for the first predefined setup
        DWGExportOptions dwgOptions = DWGExportOptions.GetPredefinedOptions(document, setupNames[0]);

        // Get the export layer table
        ExportLayerTable layerTable = dwgOptions.GetExportLayerTable();

        // Find the first mapping for the Ceilings category
        string category = "Ceilings";
        ExportLayerKey targetKey = layerTable.GetKeys().First<ExportLayerKey>(layerKey => layerKey.CategoryName == category);
        ExportLayerInfo targetInfo = layerTable[targetKey];

        // change the color name and cut color number for this mapping
        targetInfo.ColorName = "31";
        targetInfo.CutColorNumber = 31;

        // Set the change back to the map
        layerTable[targetKey] = targetInfo;

        // Set the modified table back to the options
        dwgOptions.SetExportLayerTable(layerTable);

        ICollection<ElementId> views = new List<ElementId>();
        views.Add(view.Id);

        exported = document.Export(Path.GetDirectoryName(document.PathName),
            Path.GetFileNameWithoutExtension(document.PathName), views, dwgOptions);
    }

    return exported;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Function ExportDWGModifyLayerTable(document As Document, view As View) As Boolean
    Dim exported As Boolean = False
    Dim setupNames As IList(Of String) = BaseExportOptions.GetPredefinedSetupNames(document)
    If setupNames.Count > 0 Then
        ' Get the export options for the first predefined setup
        Dim dwgOptions As DWGExportOptions = DWGExportOptions.GetPredefinedOptions(document, setupNames(0))

        ' Get the export layer table
        Dim layerTable As ExportLayerTable = dwgOptions.GetExportLayerTable()

        ' Find the first mapping for the Ceilings category
        Dim category As String = "Ceilings"
        Dim targetKey As ExportLayerKey = layerTable.GetKeys().First(Function(layerKey) layerKey.CategoryName = category)
        Dim targetInfo As ExportLayerInfo = layerTable(targetKey)

        ' change the color name and cut color number for this mapping
        targetInfo.ColorName = "31"
        targetInfo.CutColorNumber = 31

        ' Set the change back to the map
        layerTable(targetKey) = targetInfo

        ' Set the modified table back to the options
        dwgOptions.SetExportLayerTable(layerTable)

        Dim views As ICollection(Of ElementId) = New List(Of ElementId)()
        views.Add(view.Id)

        exported = document.Export(Path.GetDirectoryName(document.PathName), Path.GetFileNameWithoutExtension(document.PathName), views, dwgOptions)
    End If

    Return exported
End Function
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ExportLayerInfo

# See Also

[ExportLayerInfo Members](38ec2833-de1c-d8ad-8388-307607bb852a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88ab89de-0fbc-9750-cbfe-cacd637b3f00.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateGreaterOrEqualRule Method (ElementId, ElementId)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether ElementId values from the document are greater than or equal to a certain value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateGreaterOrEqualRule( 	ElementId parameter, 	ElementId value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateGreaterOrEqualRule ( _ 	parameter As ElementId, _ 	value As ElementId _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateGreaterOrEqualRule( 	ElementId^ parameter,  	ElementId^ value ) ``` |

#### Parameters

parameter
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     An ElementId-typed parameter used to get values from the document for a given element.

value
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The user-supplied value against which values from the document will be compared.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)

[CreateGreaterOrEqualRule Overload](14d42cfa-d1e6-d955-f2d6-6cabd71679c0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88ae5dbc-6d26-3db2-f7c2-e0a3e49920db.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Ampacity Property

---



|  |
| --- |
| [WireSize Class](e4a5cfed-7952-4622-5fca-b556703e36b6.htm)   [See Also](#seeAlsoToggle) |

Get ampacity which be used for specifying size, the unit is ampere.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public long Ampacity { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Ampacity As Long 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property long long Ampacity { 	long long get (); } ``` |

# See Also

[WireSize Class](e4a5cfed-7952-4622-5fca-b556703e36b6.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__88b19b82-f5ca-9952-b935-4228715291b5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MappedWidthDiameter Property

---



|  |
| --- |
| [FabricationPartSizeMap Class](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.htm)   [See Also](#seeAlsoToggle) |

The mapped size for the width or diameter of the straight.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.2

# Syntax

| C# |
| --- |
| ``` public double MappedWidthDiameter { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MappedWidthDiameter As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double MappedWidthDiameter { 	double get (); 	void set (double value); } ``` |

# See Also

[FabricationPartSizeMap Class](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)

<!-- Start of Syntax__88b1f0db-86ac-e2a1-496d-8b7cfbc44396.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CantMoveFrozenInstance Property

---



|  |
| --- |
| [BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)   [See Also](#seeAlsoToggle) |

A family instance placed on a curved surface of a linked file can't be moved while the link is unloaded. To move the instance, reload the link or rehost the instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CantMoveFrozenInstance { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CantMoveFrozenInstance As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CantMoveFrozenInstance { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88b6cda8-792a-1b8d-7254-0fee2bf2bc7d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Cmh Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol CMH, indicating unit Cubic meters per hour.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Cmh { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Cmh As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Cmh { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88b77d6f-cb23-83fd-72c9-86c3bc39e872.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidRungSpace Method

---



|  |
| --- |
| [CableTray Class](86d92fdc-69d4-ce86-5222-8cc2a8073132.htm)   [See Also](#seeAlsoToggle) |

Identifies if the input rung space is valid.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsValidRungSpace( 	double rungSpace ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidRungSpace ( _ 	rungSpace As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidRungSpace( 	double rungSpace ) ``` |

#### Parameters

rungSpace
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The rung space to check.

#### Return Value

True if the value is acceptable, false otherwise.

# Remarks

rung space should be at least equal to or larger than rang width which is 1 inch.

# See Also

[CableTray Class](86d92fdc-69d4-ce86-5222-8cc2a8073132.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__88b89c56-f323-0088-238d-9aed69c06570.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomDesignLightingLoadPerAreaParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Specified Lighting Load per area"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RoomDesignLightingLoadPerAreaParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoomDesignLightingLoadPerAreaParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RoomDesignLightingLoadPerAreaParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88b8fb84-023d-8d0c-83da-13af6bee640b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LooseLabeledDimensionRegenFailure Property

---



|  |
| --- |
| [BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)   [See Also](#seeAlsoToggle) |

Failed to Regenerate Family

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId LooseLabeledDimensionRegenFailure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LooseLabeledDimensionRegenFailure As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ LooseLabeledDimensionRegenFailure { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88bc5cb5-6fc5-7c8a-ef1b-0f548dc648ea.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomUpperOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Limit Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RoomUpperOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoomUpperOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RoomUpperOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88bcefd6-2d2d-1c7e-b630-ed252ae965b4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Mullion Class

---



|  |
| --- |
| [Members](ee6418c8-dd20-32cf-5a9e-f95bf155c49d.htm)   [See Also](#seeAlsoToggle) |

Represents a CurtainGrid within Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class Mullion : FamilyInstance ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Mullion _ 	Inherits FamilyInstance ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Mullion : public FamilyInstance ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB Instance](08603dd9-976d-a9fe-add7-2a8450b8006c.htm)    
  [Autodesk.Revit.DB FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)    
  Autodesk.Revit.DB Mullion

# See Also

[Mullion Members](ee6418c8-dd20-32cf-5a9e-f95bf155c49d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88bd730d-4905-3c3b-4bd1-4c308d4ca425.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomOutdoorAirflowParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Outdoor Airflow"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RoomOutdoorAirflowParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoomOutdoorAirflowParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RoomOutdoorAirflowParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88be30fb-288e-01ee-3ca3-c1b303ee8b56.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CheckConstructionSetElement Method

---



|  |
| --- |
| [EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)   [See Also](#seeAlsoToggle) |

Checks that the construction set ElementId is acceptable.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool CheckConstructionSetElement( 	ElementId constructionSetElementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CheckConstructionSetElement ( _ 	constructionSetElementId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CheckConstructionSetElement( 	ElementId^ constructionSetElementId ) ``` |

#### Parameters

constructionSetElementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The construction set ElementId to be checked.

#### Return Value

True if the construction set ElementId is a valid construction set element, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__88c0876f-0999-547a-5cff-72e895c67acf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotConvertToDouble Property

---



|  |
| --- |
| [BuiltInFailures ConversionFailures Class](9b6a7523-0468-4589-5127-159c35928f39.htm)   [See Also](#seeAlsoToggle) |

Cannot convert '[Text] ' to double value

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotConvertToDouble { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotConvertToDouble As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotConvertToDouble { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ConversionFailures Class](9b6a7523-0468-4589-5127-159c35928f39.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88c1d83c-5dd0-d010-0c85-5bcb827eeb75.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DontEditNestedGroup Property

---



|  |
| --- |
| [BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)   [See Also](#seeAlsoToggle) |

Cannot edit nested Groups while inside Edit Group mode for its host Group. To edit the nested Group finish editing all Groups. Use the Tab key to select the nested Group and edit it directly.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DontEditNestedGroup { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DontEditNestedGroup As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DontEditNestedGroup { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88c6bc2d-aaa4-a2fe-7b0b-a062f7d96c52.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BeforeSaveToCentral Property

---



|  |
| --- |
| [DocumentSaveToLocalProgressChangedEventArgs Class](a3a774b8-2913-5de6-e7ad-5daa24a9c172.htm)   [See Also](#seeAlsoToggle) |

True if the "save to local" operation is occurring before "save to central"; false if after.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public bool BeforeSaveToCentral { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property BeforeSaveToCentral As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool BeforeSaveToCentral { 	bool get (); } ``` |

# See Also

[DocumentSaveToLocalProgressChangedEventArgs Class](a3a774b8-2913-5de6-e7ad-5daa24a9c172.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__88c95a30-6091-0f42-9c4a-ff326afd0d86.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElemPlateWeight Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Weight"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SteelElemPlateWeight { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElemPlateWeight As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SteelElemPlateWeight { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88ca947e-5580-9276-7716-ba4d2142c766.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleGroupParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Sorting/Grouping"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ScheduleGroupParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ScheduleGroupParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ScheduleGroupParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88cb5514-1aa3-4501-40fe-412e7db40848.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HeatingCoilType Property

---



|  |
| --- |
| [AirSystemData Class](4a7c39a1-cd35-4828-97b7-f70cbd3fdab8.htm)   [See Also](#seeAlsoToggle) |

The heating coil type. Note this property change would reset the heating water loop.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public AirHeatingCoilType HeatingCoilType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property HeatingCoilType As AirHeatingCoilType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property AirHeatingCoilType HeatingCoilType { 	AirHeatingCoilType get (); 	void set (AirHeatingCoilType value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[AirSystemData Class](4a7c39a1-cd35-4828-97b7-f70cbd3fdab8.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__88cc063a-b8f9-27d1-8487-529bdcfaf6d5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhaseDemolished Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Phase Demolished"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PhaseDemolished { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PhaseDemolished As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PhaseDemolished { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88cdc3bf-a26f-be67-5f13-1d5d73b2d5f0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [ReferenceArrayIterator Class](5b4e4948-c5f0-1e38-d461-7353561774e8.htm)   [See Also](#seeAlsoToggle) |

Retrieves the item that is the current focus of the iterator.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual Object Current { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property Current As Object 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property Object^ Current { 	Object^ get (); } ``` |

#### Implements

 [IEnumerator Current](http://msdn2.microsoft.com/en-us/library/khfze649)

# Remarks

A new or Reset iterator must have MoveNext called on it before Current will return a valid item as per expected behavior of IEnumerator.

# See Also

[ReferenceArrayIterator Class](5b4e4948-c5f0-1e38-d461-7353561774e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88d0cd4a-1709-198d-34a7-47cd28e7aad6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReinforcementCover Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Reinforcement Cover, in discipline Structural.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ReinforcementCover { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ReinforcementCover As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ReinforcementCover { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88de4671-37ce-e6c5-cb56-5a8758fee195.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetTypeName Method

---



|  |
| --- |
| [AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.htm)   [See Also](#seeAlsoToggle) |

Get the name of the AssetProperty

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public static string GetTypeName( 	AssetPropertyType type ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetTypeName ( _ 	type As AssetPropertyType _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ GetTypeName( 	AssetPropertyType type ) ``` |

#### Parameters

type
:   Type:  [Autodesk.Revit.DB.Visual AssetPropertyType](3463b8a3-5c87-63c0-03d1-a20e442f6f28.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when type is AssetPropertyType::Unknown. |

# See Also

[AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__88de72a4-cf23-c2e7-7b38-acadc45591e7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetOpenWorksetsConfiguration Method

---



|  |
| --- |
| [OpenOptions Class](c0004971-3810-eeb8-72bd-e116886ec3c8.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Sets the object used to configure the worksets to open when the model is opened.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetOpenWorksetsConfiguration( 	WorksetConfiguration openConfiguration ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetOpenWorksetsConfiguration ( _ 	openConfiguration As WorksetConfiguration _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetOpenWorksetsConfiguration( 	WorksetConfiguration^ openConfiguration ) ``` |

#### Parameters

openConfiguration
:   Type:  [Autodesk.Revit.DB WorksetConfiguration](eefef6f4-0892-4bb5-8840-5e99aebc65c9.htm)    
     The options. If    a null reference (  Nothing  in Visual Basic)  , all user-created worksets will be opened.

# Remarks

These options are ignored for non-workshared models.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
Document OpenDocumentWithWorksets(Application app, ModelPath projectPath)
{
    Document doc = null;
    try
    {
        // Get info on all the user worksets in the project prior to opening
        IList<WorksetPreview> worksets = WorksharingUtils.GetUserWorksetInfo(projectPath);
        IList<WorksetId> worksetIds = new List<WorksetId>();
        // Find two predetermined worksets
        foreach (WorksetPreview worksetPrev in worksets)
        {
            if (worksetPrev.Name.CompareTo("Workset1") == 0 ||
                worksetPrev.Name.CompareTo("Workset2") == 0)
            {
                worksetIds.Add(worksetPrev.Id);
            }
        }

        OpenOptions openOptions = new OpenOptions();
        // Setup config to close all worksets by default
        WorksetConfiguration openConfig = new WorksetConfiguration(WorksetConfigurationOption.CloseAllWorksets);
        // Set list of worksets for opening 
        openConfig.Open(worksetIds);
        openOptions.SetOpenWorksetsConfiguration(openConfig);
        doc = app.OpenDocumentFile(projectPath, openOptions);
    }
    catch (Exception e)
    {
        TaskDialog.Show("Open File Failed", e.Message);
    }

    return doc;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Function OpenDocumentWithWorksets(app As Application, projectPath As ModelPath) As Document
    Dim doc As Document = Nothing
    Try
        ' Get info on all the user worksets in the project prior to opening
        Dim worksets As IList(Of WorksetPreview) = WorksharingUtils.GetUserWorksetInfo(projectPath)
        Dim worksetIds As IList(Of WorksetId) = New List(Of WorksetId)()
        ' Find two predetermined worksets
        For Each worksetPrev As WorksetPreview In worksets
            If worksetPrev.Name.CompareTo("Workset1") = 0 OrElse worksetPrev.Name.CompareTo("Workset2") = 0 Then
                worksetIds.Add(worksetPrev.Id)
            End If
        Next

        Dim openOptions As New OpenOptions()
        ' Setup config to close all worksets by default
        Dim openConfig As New WorksetConfiguration(WorksetConfigurationOption.CloseAllWorksets)
        ' Set list of worksets for opening 
        openConfig.Open(worksetIds)
        openOptions.SetOpenWorksetsConfiguration(openConfig)
        doc = app.OpenDocumentFile(projectPath, openOptions)
    Catch e As Exception
        TaskDialog.Show("Open File Failed", e.Message)
    End Try

    Return doc
End Function
```

# See Also

[OpenOptions Class](c0004971-3810-eeb8-72bd-e116886ec3c8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88df87e1-8312-cfc8-d00e-d53bd406277b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallSweepInfo Constructor (WallSweepType, Boolean)

---



|  |
| --- |
| [WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)   [See Also](#seeAlsoToggle) |

Constructs a new WallSweepInfo instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public WallSweepInfo( 	WallSweepType type, 	bool vertical ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	type As WallSweepType, _ 	vertical As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: WallSweepInfo( 	WallSweepType type,  	bool vertical ) ``` |

#### Parameters

type
:   Type:  [Autodesk.Revit.DB WallSweepType](f66354e5-a9c6-de97-695c-4a2fba036232.htm)    
     The type of the WallSweepInfo instance.

vertical
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     True to construct a vertical wall sweep, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)

[WallSweepInfo Overload](46b56f68-7843-62e8-26ca-962b34fb86ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88dfb312-9117-3c0f-d81d-0eb2b8737fb5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Insulation Property

---



|  |
| --- |
| [WireType Class](f4d1a1cc-6968-251b-9692-247dc3ff6cff.htm)   [See Also](#seeAlsoToggle) |

The insulation type.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public InsulationType Insulation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Insulation As InsulationType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property InsulationType^ Insulation { 	InsulationType^ get (); 	void set (InsulationType^ value); } ``` |

# See Also

[WireType Class](f4d1a1cc-6968-251b-9692-247dc3ff6cff.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__88e34cf9-778b-cdc1-15dd-d574bfc7c005.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [PolymeshFacet Class](a7315aaf-631d-96af-368c-65f86b6c00ef.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsValidObject { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsValidObject As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsValidObject { 	bool get (); } ``` |

#### Return Value

True if the API object holds a valid Revit native object, false otherwise.

# Remarks

This property is always True for a polymesh facet.

# See Also

[PolymeshFacet Class](a7315aaf-631d-96af-368c-65f86b6c00ef.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88e6bdfe-1991-203a-cf1b-9b45c49816f6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LessThanTwoBars Property

---



|  |
| --- |
| [BuiltInFailures RebarSystemFailures Class](ef87224e-09b6-8d07-3b24-3a3b322a9ae5.htm)   [See Also](#seeAlsoToggle) |

Each reinforcement direction requires at least 2 bars. Please increase the number of bars.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId LessThanTwoBars { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LessThanTwoBars As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ LessThanTwoBars { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarSystemFailures Class](ef87224e-09b6-8d07-3b24-3a3b322a9ae5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88e85cfe-217f-9a7e-fd47-19bc8e033b0a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BorderRightLineStyle Property

---



|  |
| --- |
| [TableCellStyle Class](e9a5280b-4009-004f-57a4-af1f292f9619.htm)   [See Also](#seeAlsoToggle) |

The element id (GraphicsStyle element) for the right line of the cell border.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public ElementId BorderRightLineStyle { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BorderRightLineStyle As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ BorderRightLineStyle { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[TableCellStyle Class](e9a5280b-4009-004f-57a4-af1f292f9619.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88ecc3db-1c91-a22a-da37-197fdd14a50d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DollarPerW Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol $/W, indicating unit Cost per watt.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DollarPerW { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DollarPerW As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DollarPerW { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88ed10dc-950f-79a7-a59e-18a7c95b6cbe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsValidObject { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsValidObject As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsValidObject { 	bool get (); } ``` |

#### Return Value

True if the API object holds a valid Revit native object, false otherwise.

# Remarks

If the corresponding Revit native object is destroyed, or creation of the corresponding object is undone, a managed API object containing it is no longer valid. API methods cannot be called on invalidated wrapper objects.

# See Also

[MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88ede5e0-76a3-5fb0-d86b-dce75f75fb23.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DoubleParameterValue Constructor

---



|  |
| --- |
| [DoubleParameterValue Class](561ef32b-c3bc-3847-ef2a-27f4a011e650.htm)   [See Also](#seeAlsoToggle) |

Default constructor

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public DoubleParameterValue() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: DoubleParameterValue() ``` |

# See Also

[DoubleParameterValue Class](561ef32b-c3bc-3847-ef2a-27f4a011e650.htm)

[DoubleParameterValue Overload](0aa0f74f-099c-4bb2-fce1-fbd9a5d8ac91.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88f2e133-fe80-f35a-4e8f-e9c0870f5448.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LossFactor Property

---



|  |
| --- |
| [BasicLossFactor Class](4ae30f40-0afb-176a-1b90-61ac2ac2727f.htm)   [See Also](#seeAlsoToggle) |

The loss factor.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double LossFactor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LossFactor As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double LossFactor { 	double get (); 	void set (double value); } ``` |

#### Field Value

The loss factor as a numerical value between 0.0 and 4.0

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The loss factor is not valid because it is not between 0.0 and 4.0. |

# See Also

[BasicLossFactor Class](4ae30f40-0afb-176a-1b90-61ac2ac2727f.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__88f2f8f0-d495-dab8-86ee-931682dc0ff8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OpeningNegativeHeight Property

---



|  |
| --- |
| [BuiltInFailures OpeningFailures Class](7857c588-1861-cfd1-1423-7b950a01aba1.htm)   [See Also](#seeAlsoToggle) |

The top of the Opening is lower than the bottom of the Opening or coincident with it.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId OpeningNegativeHeight { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property OpeningNegativeHeight As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ OpeningNegativeHeight { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures OpeningFailures Class](7857c588-1861-cfd1-1423-7b950a01aba1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88f32eaa-bf1e-63f7-4ee5-b9a9ba612553.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyNamePseudoParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Family"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FamilyNamePseudoParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FamilyNamePseudoParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FamilyNamePseudoParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88fa37fb-cfa5-3301-af50-dec7beb3121d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeImage Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Shape Image"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarShapeImage { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarShapeImage As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarShapeImage { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__88fa78de-0fff-a85f-0de3-b631673e9e51.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Cancel Method

---



|  |
| --- |
| [RevitAPIPreEventArgs Class](14097470-c9d9-0143-dc1b-b93a60a460e6.htm)   [See Also](#seeAlsoToggle) |

When the event is cancellable, may call the Cancel() method to cancel it.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void Cancel() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Cancel ``` |

 

| Visual C++ |
| --- |
| ``` public: void Cancel() ``` |

# Remarks

Not every event is cancellable. Whether or not an event may be cancelled is indicated by IsCancellable() method.

# See Also

[RevitAPIPreEventArgs Class](14097470-c9d9-0143-dc1b-b93a60a460e6.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__88ffc634-bae0-0ef7-b232-81cd80a391fe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanTotal Method

---



|  |
| --- |
| [ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)   [See Also](#seeAlsoToggle) |

Indicates if totals can be enabled for this field.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool CanTotal() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanTotal As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanTotal() ``` |

#### Return Value

True if this field can be totaled, false otherwise.

# See Also

[ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89a08906-2560-8b51-51d0-67e85b4780b6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Support Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Supports"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Support { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Support As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Support { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89a0ca1b-e434-75d0-526b-3ec001faa3b3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VisGraphicsWorksets Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"V/G Overrides Worksets"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId VisGraphicsWorksets { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property VisGraphicsWorksets As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ VisGraphicsWorksets { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89a23ed6-a01c-a35e-1fde-78bb7a16c122.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElementInvisibleInCurrentLevelOfDetailWarn Property

---



|  |
| --- |
| [BuiltInFailures SteelElementsFailures Class](f85c5c93-90cd-5888-b8ac-c1ba6f7b2040.htm)   [See Also](#seeAlsoToggle) |

The created elements are only visible in Detail Level: Fine.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SteelElementInvisibleInCurrentLevelOfDetailWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElementInvisibleInCurrentLevelOfDetailWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SteelElementInvisibleInCurrentLevelOfDetailWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SteelElementsFailures Class](f85c5c93-90cd-5888-b8ac-c1ba6f7b2040.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89a36389-2694-4d88-d3eb-906cafde1619.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IntegerRange Class

---



|  |
| --- |
| [Members](13407f78-3a74-49c7-ea18-70186aa23c41.htm)   [See Also](#seeAlsoToggle) |

A class to define a range of a sequence of consecutive integer numbers

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class IntegerRange : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class IntegerRange _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class IntegerRange : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB IntegerRange

# See Also

[IntegerRange Members](13407f78-3a74-49c7-ea18-70186aa23c41.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89a8f1d5-0468-b276-b44e-da40549329d8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricParamCutOverallLength Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Cut Overall Length": Provides a real sheet Length after definition

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FabricParamCutOverallLength { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricParamCutOverallLength As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FabricParamCutOverallLength { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89aa230b-4890-0506-21f5-6d4d59e0e9f8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AllSlotsOnPanelOccupied Property

---



|  |
| --- |
| [BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)   [See Also](#seeAlsoToggle) |

All slots on panel: [Panel Name] are occupied. Some circuits will be disconnected from this panel.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId AllSlotsOnPanelOccupied { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AllSlotsOnPanelOccupied As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ AllSlotsOnPanelOccupied { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89b8e17b-bf07-6ed4-e237-862fdd035386.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateRibbonTab Method

---



|  |
| --- |
| [ApplicationEntryPoint Class](7ff0ad2b-7713-ec77-ccc9-8a01fffcf83e.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.UI.Macros](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public override void CreateRibbonTab( 	string tabName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Sub CreateRibbonTab ( _ 	tabName As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void CreateRibbonTab( 	String^ tabName ) override ``` |

#### Parameters

tabName
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

# See Also

[ApplicationEntryPoint Class](7ff0ad2b-7713-ec77-ccc9-8a01fffcf83e.htm)

[Autodesk.Revit.UI.Macros Namespace](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)

<!-- Start of Syntax__89bc8899-38bf-f736-fb5c-f3b8ad4c281f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddReferencePlane Method (Plane, BoundingBoxUV, DirectShapeReferenceOptions)

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

Adds a reference plane to the DirectShapeType. The reference plane can either be bounded or unbounded.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void AddReferencePlane( 	Plane refPlane, 	BoundingBoxUV boundingBoxUV, 	DirectShapeReferenceOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddReferencePlane ( _ 	refPlane As Plane, _ 	boundingBoxUV As BoundingBoxUV, _ 	options As DirectShapeReferenceOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddReferencePlane( 	Plane^ refPlane,  	BoundingBoxUV^ boundingBoxUV,  	DirectShapeReferenceOptions^ options ) ``` |

#### Parameters

refPlane
:   Type:  [Autodesk.Revit.DB Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)    
     The geometry of the new reference plane.

boundingBoxUV
:   Type:  [Autodesk.Revit.DB BoundingBoxUV](e38a0145-4267-0b3f-0718-adb14e34c94e.htm)    
     If boundingBoxUV is set, the resulting reference plane that is added to the DirectShapeType will be displayed with those bounds. Note that the specified bounds must not be degenerate. If boundingBoxUV is not set, reasonable bounds are automatically calculated and applied to the input plane. The automatic bounds are based on the host direct shape's geometry.

options
:   Type:  [Autodesk.Revit.DB DirectShapeReferenceOptions](c77da180-10dd-8e8a-d5d4-01cfc06135e5.htm)    
     The options that are used to configure the new reference plane.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | boundingBoxUV cannot be used as a BoundingBoxUV for the reference plane surface. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[AddReferencePlane Overload](af371761-785f-82f8-6c56-5037e961ba01.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89bd462f-a178-5c9b-a897-44423c97bd2d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsPipingSystemTypeId Method

---



|  |
| --- |
| [FlexPipe Class](4b0e0656-4760-4a91-a777-ce50869a827a.htm)   [See Also](#seeAlsoToggle) |

Checks if given type is valid piping system type.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool IsPipingSystemTypeId( 	Document document, 	ElementId systemTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsPipingSystemTypeId ( _ 	document As Document, _ 	systemTypeId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsPipingSystemTypeId( 	Document^ document,  	ElementId^ systemTypeId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

systemTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     ElementId of the piping system type to check.

#### Return Value

True if the given systemTypeId is the piping system type, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FlexPipe Class](4b0e0656-4760-4a91-a777-ce50869a827a.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__89c19f58-4556-ecb6-1110-ff69e55436b4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ResetSupportPosition Method

---



|  |
| --- |
| [Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)   [See Also](#seeAlsoToggle) |

Resets the continuous rails support subelements position data.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void ResetSupportPosition() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ResetSupportPosition ``` |

 

| Visual C++ |
| --- |
| ``` public: void ResetSupportPosition() ``` |

# See Also

[Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__89c48f40-ccec-5acd-f165-06b01004e80f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurveLoopReferencesOnProfile Property

---



|  |
| --- |
| [Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)   [See Also](#seeAlsoToggle) |

The curve references in certain curve loop, specified by profile index and curve loop index.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ReferenceArray this[ 	int profileIndex, 	int curveLoopIndex ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property CurveLoopReferencesOnProfile ( _ 	profileIndex As Integer, _ 	curveLoopIndex As Integer _ ) As ReferenceArray 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ReferenceArray^ CurveLoopReferencesOnProfile[int profileIndex, int curveLoopIndex] { 	ReferenceArray^ get (int profileIndex, int curveLoopIndex); } ``` |

#### Parameters

profileIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index to specify the profile, should be within 0 and (ProfileCount - 1).

curveLoopIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index to specify the curve loop, should be within 0 and (CurveLoopCount - 1).

# See Also

[Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89cb7975-cc76-65ba-b996-bcb78d12161a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExecuteBooleanOperation Method

---



|  |
| --- |
| [BooleanOperationsUtils Class](a7be98f3-9e8a-ee51-f46c-2479cb72c598.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Perform a boolean geometric operation between two solids, and return a new solid to represent the result.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static Solid ExecuteBooleanOperation( 	Solid solid0, 	Solid solid1, 	BooleanOperationsType booleanType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ExecuteBooleanOperation ( _ 	solid0 As Solid, _ 	solid1 As Solid, _ 	booleanType As BooleanOperationsType _ ) As Solid ``` |

 

| Visual C++ |
| --- |
| ``` public: static Solid^ ExecuteBooleanOperation( 	Solid^ solid0,  	Solid^ solid1,  	BooleanOperationsType booleanType ) ``` |

#### Parameters

solid0
:   Type:  [Autodesk.Revit.DB Solid](7a3b5ac1-c66d-9f81-a11d-9bcd4e026295.htm)    
     The first solid object. A copy will be taken of the input object, so any solid whether obtained from a Revit element or not would be accepted.

solid1
:   Type:  [Autodesk.Revit.DB Solid](7a3b5ac1-c66d-9f81-a11d-9bcd4e026295.htm)    
     The second solid object. A copy will be taken of the input object, so any solid whether obtained from a Revit element or not would be accepted.

booleanType
:   Type:  [Autodesk.Revit.DB BooleanOperationsType](46aeb9cd-4b44-0dcf-6f78-469c1271f5d4.htm)    
     boolean operation type.

#### Return Value

The result geometry.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void ComputeIntersectionVolume(Solid solidA, Solid solidB)
{
    Solid intersection = BooleanOperationsUtils.ExecuteBooleanOperation(solidA, solidB, BooleanOperationsType.Intersect);
    double volumeOfIntersection = intersection.Volume;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub ComputeIntersectionVolume(solidA As Solid, solidB As Solid)
    Dim intersection As Solid = BooleanOperationsUtils.ExecuteBooleanOperation(solidA, solidB, BooleanOperationsType.Intersect)
    Dim volumeOfIntersection As Double = intersection.Volume
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to perform the Boolean operation for the two solids. This may be due to geometric inaccuracies in the solids, such as slightly misaligned faces or edges. If so, eliminating the inaccuracies by making sure the solids are accurately aligned may solve the problem. This also may be due to one or both solids having complexities such as more than two faces geometrically meeting along a single edge, or two coincident edges, etc. Eliminating such conditions, or performing a sequence of Boolean operations in an order that avoids such conditions, may solve the problem. |

# See Also

[BooleanOperationsUtils Class](a7be98f3-9e8a-ee51-f46c-2479cb72c598.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89cd38a7-94b6-dca7-8f92-9f2cf5f43fa9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UniformatCode Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Assembly Code"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId UniformatCode { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property UniformatCode As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ UniformatCode { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89cfbb29-5f7c-bd05-e216-0befff791ae5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExecuteService Method (Guid, IExternalData)

---



|  |
| --- |
| [ExternalServiceRegistry Class](fa14442f-3d47-2c21-467c-6d19e4cc0d9e.htm)   [See Also](#seeAlsoToggle) |

Execute a service independently of any document.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ExternalServiceResult ExecuteService( 	Guid executionKey, 	IExternalData data ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ExecuteService ( _ 	executionKey As Guid, _ 	data As IExternalData _ ) As ExternalServiceResult ``` |

 

| Visual C++ |
| --- |
| ``` public: static ExternalServiceResult ExecuteService( 	Guid executionKey,  	IExternalData^ data ) ``` |

#### Parameters

executionKey
:   Type:  System Guid    
     Access key of the service to be executed. The key is not the same as the service's Id. It is the value that was returned to the caller who registered the service.

data
:   Type:  [Autodesk.Revit.DB.ExternalService IExternalData](d4f0854f-3b67-c60e-1696-8cffbaba065a.htm)    
     The associated data. The type is defined by the service.

#### Return Value

The result of executing the external service.

# Remarks

Execution of a service should be invoked only by the application that registered the service. The execution will use the currently active server (or servers in the case of a multi-server service).

This method does not take a document as one of its arguments and therefore it is not intended for executions of recordable services that may modify documents. If the service (recordable) or its server(s) is expected to modify documents, the other ExecuteService method -- the one that takes a document as one of its arguments -- is supposed to be used.

Non-recordable services are free to modify documents during this ExecuteService call, because activities of non-recordable services are not recorded; the changes those services made are assumed to be independent of the presence of the service and/or its servers.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The execution key is either invalid or of a service that is not registered. To execute a service, the key returned by RegisterService method must be used. -or- The execution key is of a service that is already being executed. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternalServiceRegistry Class](fa14442f-3d47-2c21-467c-6d19e4cc0d9e.htm)

[ExecuteService Overload](441ae935-fa59-aa1e-23ba-57e334974c7f.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)

<!-- Start of Syntax__89d71e79-0770-b235-db89-80b80dd331af.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EnableTemporaryViewPropertiesMode Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Turns Temporary View Properties mode on or off. In this mode, any changes made to the view are temporary and will be discarded once the mode is disabled.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool EnableTemporaryViewPropertiesMode( 	ElementId viewTemplateId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function EnableTemporaryViewPropertiesMode ( _ 	viewTemplateId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool EnableTemporaryViewPropertiesMode( 	ElementId^ viewTemplateId ) ``` |

#### Parameters

viewTemplateId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     If the id of a view template is provided, Temporary View Properties mode is turned on and the settings from the template are applied to the view for the duration of the mode. If the id provided is not that of a template but the id of the view itself, Temporary View Properties mode is turned on without any changes to the view. If ElementId.InvalidElementId is provided, Temporary View Properties mode is turned off.

#### Return Value

Returns true when the view template provided by viewTemplateId was applied and Temporary View Properties was successfully turned on. Also returns true if ElementId.InvalidElementId was provided as input and Temporary View Properties was successfully turned off.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | View cannot use Temporary View Properties mode in current state. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89d83c57-01e4-d9fd-245a-ce67aed98214.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElemHoleDepthOfBoltHead Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Depth of bolt head"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SteelElemHoleDepthOfBoltHead { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElemHoleDepthOfBoltHead As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SteelElemHoleDepthOfBoltHead { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89d89465-897f-4105-b935-27edf67aab3e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Units Class

---



|  |
| --- |
| [Members](de96b3ae-d662-2f9a-2724-955cbce03719.htm)   [See Also](#seeAlsoToggle) |

A document's default settings for formatting numbers with units.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class Units : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Units _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Units : IDisposable ``` |

# Remarks

The Units class represents a document's default settings for formatting numbers with units as strings. It contains a  [FormatOptions](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)  object for each unit type as well as settings related to decimal symbol and digit grouping.

The Units class stores a FormatOptions object for every valid unit type, but not all of them can be directly modified. Some, like UT\_Number and UT\_SiteAngle, have fixed definitions. Others have definitions which are automatically derived from other unit types. For example, UT\_SheetLength is derived from UT\_Length and UT\_ForceScale is derived from UT\_Force. See  [IsModifiableUnitType()](8c60b3e9-d996-435d-33fb-e475ee78a41e.htm)  and  [GetModifiableUnitTypes()](480ae2b2-e543-5156-ac1e-650756d6669d.htm)  .

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB Units

# See Also

[Units Members](de96b3ae-d662-2f9a-2724-955cbce03719.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89da057e-f826-1f1e-dd71-9df4ce7f38cf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FlexPipeType Class

---



|  |
| --- |
| [Members](265bb674-73f8-84a9-72ee-cfe519f10a8e.htm)   [See Also](#seeAlsoToggle) |

A flex pipe type in the Autodesk Revit MEP product.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class FlexPipeType : MEPCurveType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FlexPipeType _ 	Inherits MEPCurveType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FlexPipeType : public MEPCurveType ``` |

# Remarks

The flex pipe type is only available in the Autodesk Revit MEP product.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  [Autodesk.Revit.DB HostObjAttributes](a3d349c5-d457-3b56-eec4-c2fa2757c860.htm)    
  [Autodesk.Revit.DB MEPCurveType](97c98bd6-0966-5b0c-6f75-4c34f16adce1.htm)    
  Autodesk.Revit.DB.Plumbing FlexPipeType

# See Also

[FlexPipeType Members](265bb674-73f8-84a9-72ee-cfe519f10a8e.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__89daf55c-217b-4daa-3be5-bc89fe1c4972.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### YoungModulus Property

---



|  |
| --- |
| [StructuralAsset Class](39c2e2ad-474e-2514-bc15-07c24a989a61.htm)   [See Also](#seeAlsoToggle) |

The Young's modulus of the asset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public XYZ YoungModulus { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property YoungModulus As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ YoungModulus { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

This property cannot be used to set the Young's modulus for wood-based and isotropic materials. For such assets, use setYoungModulus instead. The value is in Newtons per foot meter (N/(ft Â· m)).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | When setting this property: the material type is wood. -or- When setting this property: the behavior is isotropic. |

# See Also

[StructuralAsset Class](39c2e2ad-474e-2514-bc15-07c24a989a61.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89dc8618-3109-4905-36b0-a8017044e651.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetHookTangentLength Method

---



|  |
| --- |
| [RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)   [See Also](#seeAlsoToggle) |

Identifies the hook tangent length for a hook type

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public double GetHookTangentLength( 	ElementId hookId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetHookTangentLength ( _ 	hookId As ElementId _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetHookTangentLength( 	ElementId^ hookId ) ``` |

#### Parameters

hookId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     id of the hook type

#### Return Value

The hook tangent length for a hook type

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | the rebar hook type id hookId is not valid |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__89de4a10-562f-977f-02be-9f0333fad993.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Evaluate Method

---



|  |
| --- |
| [FormulaManager Class](d061dadf-70da-a883-ec12-5cf98ded069e.htm)   [See Also](#seeAlsoToggle) |

Evaluates value of the formula

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static string Evaluate( 	ElementId parameterId, 	Document document, 	string formula ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Evaluate ( _ 	parameterId As ElementId, _ 	document As Document, _ 	formula As String _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ Evaluate( 	ElementId^ parameterId,  	Document^ document,  	String^ formula ) ``` |

#### Parameters

parameterId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

formula
:   Type:  System String

# Remarks

It evaluates formula using list of global or family parameters depends on document type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FormulaManager Class](d061dadf-70da-a883-ec12-5cf98ded069e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89deea46-e7ab-6e7a-a363-665a2eb4b012.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidSubelementReference Method

---



|  |
| --- |
| [Subelement Class](2d15bb45-70af-5f84-e899-322742591251.htm)   [See Also](#seeAlsoToggle) |

Checks if given Reference identifies either a valid element or subelement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static bool IsValidSubelementReference( 	Document aDoc, 	Reference reference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidSubelementReference ( _ 	aDoc As Document, _ 	reference As Reference _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidSubelementReference( 	Document^ aDoc,  	Reference^ reference ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

reference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The reference that identifies an element or subelement.

#### Return Value

True if %reference% identifies a valid element or subelement, false otherwise.

# Remarks

A reference to an element or subelement in a linked document is acceptable.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Subelement Class](2d15bb45-70af-5f84-e899-322742591251.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89e824ff-5721-78bf-ba75-9774852fa7e0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CoverOffset Property

---



|  |
| --- |
| [FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)   [See Also](#seeAlsoToggle) |

The additional cover offset of the Fabric Sheet.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public double CoverOffset { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CoverOffset As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double CoverOffset { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for coverOffset is not a number -or- When setting this property: coverOffset is greater then the host thickness. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for coverOffset must be between 0 and 30000 feet. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: |

# See Also

[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__89eb1cc7-515a-839c-dc7a-9d52879b451f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (IList(XYZ), Boolean)

---



|  |
| --- |
| [HermiteSpline Class](6852ca4c-2fad-cda1-be75-54e712a39318.htm)   [See Also](#seeAlsoToggle) |

Creates a Hermite spline with default tangency at its endpoints.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static HermiteSpline Create( 	IList<XYZ> controlPoints, 	bool periodic ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	controlPoints As IList(Of XYZ), _ 	periodic As Boolean _ ) As HermiteSpline ``` |

 

| Visual C++ |
| --- |
| ``` public: static HermiteSpline^ Create( 	IList<XYZ^>^ controlPoints,  	bool periodic ) ``` |

#### Parameters

controlPoints
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The control points of the Hermite spline.

periodic
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     True if the Hermite spline is to be periodic, false otherwise.

#### Return Value

The new HermiteSpline object.

# Remarks

The tangents at the ends of the spline are computed from the control points.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The control points array is invalid, because it doesn't contain the minimum number of points (2). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | Curve length is too small for Revit's tolerance (as identified by Application.ShortCurveTolerance). |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Unable to construct valid HermiteSpline from given inputs. |

# See Also

[HermiteSpline Class](6852ca4c-2fad-cda1-be75-54e712a39318.htm)

[Create Overload](7c7dc39c-7a31-4257-3b7b-4041c48ddacb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89eb43f4-6527-3056-6418-83cec873b232.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DollarPerFtSup2 Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol $/ftÂ², indicating unit Cost per square foot.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DollarPerFtSup2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DollarPerFtSup2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DollarPerFtSup2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89ebaf9b-a5fa-a1a8-6036-69596f58f663.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotHaveArcs Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Sorry, we can't use arcs here.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotHaveArcs { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotHaveArcs As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotHaveArcs { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89ed06e9-ad4c-d8a1-e4e8-d6ad772224fb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FlangeThickness Property

---



|  |
| --- |
| [StructuralSectionHotRolled Class](60cc6328-1e99-2a7b-03fb-983e52350e55.htm)   [See Also](#seeAlsoToggle) |

Flange Thickness.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public double FlangeThickness { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FlangeThickness As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double FlangeThickness { 	double get (); 	void set (double value); } ``` |

# See Also

[StructuralSectionHotRolled Class](60cc6328-1e99-2a7b-03fb-983e52350e55.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__89f0bc3d-1f6b-6fef-8b93-effa6b175445.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReverseIterator Method

---



|  |
| --- |
| [WireSet Class](44035985-f6a1-72de-ae57-ac08507c8bbb.htm)   [See Also](#seeAlsoToggle) |

Retrieve a backward moving iterator to the set.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual WireSetIterator ReverseIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ReverseIterator As WireSetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual WireSetIterator^ ReverseIterator() ``` |

#### Return Value

Returns a backward moving iterator to the set.

# See Also

[WireSet Class](44035985-f6a1-72de-ae57-ac08507c8bbb.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__89f301c6-4688-fd2b-e827-68339bac8dd5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Prefix Property

---



|  |
| --- |
| [TableCellCombinedParameterData Class](f2303148-6e5e-d143-3725-3ac12c04ea86.htm)   [See Also](#seeAlsoToggle) |

The prefix for this parameter

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public string Prefix { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Prefix As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Prefix { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[TableCellCombinedParameterData Class](f2303148-6e5e-d143-3725-3ac12c04ea86.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89f514bf-f067-308d-0518-f050450bde72.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentCreated Event

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the DocumentCreated event to be notified immediately after Revit has finished creating a new document.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<DocumentCreatedEventArgs> DocumentCreated ``` |

 

| Visual Basic |
| --- |
| ``` Public Event DocumentCreated As EventHandler(Of DocumentCreatedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<DocumentCreatedEventArgs^>^ DocumentCreated { 	void add (EventHandler<DocumentCreatedEventArgs^>^ value); 	void remove (EventHandler<DocumentCreatedEventArgs^>^ value); } ``` |

# Remarks

This event is raised immediately after Revit has finished creating a new document. It is raised even when document creation failed or was cancelled (during DocumentCreating event).

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Check the 'Status' field in event's argument to see whether the action itself was successful or not. This event is not cancellable, for the process of document creation has already been finished.

If the action was not successful, the document may not be modified and new transactions may not be started.

The following API functions are not available for the current document during this event:

* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__89fced22-a3f1-42ef-d928-b912f2eaa8a5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElemPatternTotalLength Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Length on side 1"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SteelElemPatternTotalLength { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElemPatternTotalLength As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SteelElemPatternTotalLength { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89fe31e2-42bb-7a25-caa3-6254b0105173.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRebarUpdateCurvesData Method

---



|  |
| --- |
| [RebarCurvesData Class](71996f44-c8f9-7695-ccb9-efae09726c9c.htm)   [See Also](#seeAlsoToggle) |

Gets a class that contains information used as input and output for rebar free form calculation.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public RebarUpdateCurvesData GetRebarUpdateCurvesData() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRebarUpdateCurvesData As RebarUpdateCurvesData ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarUpdateCurvesData^ GetRebarUpdateCurvesData() ``` |

#### Return Value

Gets a class that contains information used as input and output for rebar free form calculation.

# See Also

[RebarCurvesData Class](71996f44-c8f9-7695-ccb9-efae09726c9c.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__89fe9654-9f1c-6ba8-d87c-1b38b63feb31.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDefaultHookAngle Method

---



|  |
| --- |
| [RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)   [See Also](#seeAlsoToggle) |

Get the hook angle, expressed as an integral number of degrees (common values are 0, 90, 135, and 180).

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public int GetDefaultHookAngle( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDefaultHookAngle ( _ 	index As Integer _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int GetDefaultHookAngle( 	int index ) ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     0 for the starting hook, 1 for the ending hook.

# Remarks

Replaces the method GetHookAngle() from prior releases.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | index must be 0 or 1. |

# See Also

[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__89ff9f32-0abe-ed50-b25b-3d0cc7c89689.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BaseLoadOn Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all the possible power load use types for a space object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public enum BaseLoadOn ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration BaseLoadOn ``` |

 

| Visual C++ |
| --- |
| ``` public enum class BaseLoadOn ``` |

# Members

| Member name | Description |
| --- | --- |
| kUseDefaultLoad | Return BaseLoadOn is UseDefaultLoad. Obsoleted from 2018, use kBySpaceType instead. |
| kBySpaceType | Return BaseLoadOn is BySpaceType. |
| kUseEnteredLoad | Return BaseLoadOn is UseEnteredLoad. |
| kUseCalculatedLoad | Return BaseLoadOn is UseCalculatedLoad. |
| kUseActualLoad | Return BaseLoadOn is UseActualLoad. |
| kNoOfBaseLoadOnMethods | Return BaseLoadOn is NoOfBaseLoadOnMethods. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__89ffea83-f105-0468-af9b-eb00d5de1b97.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Equals Method

---



|  |
| --- |
| [ForgeTypeId Class](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)   [See Also](#seeAlsoToggle) |

Determines whether this ForgeTypeId is equal to another.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public override bool Equals( 	Object other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Function Equals ( _ 	other As Object _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Equals( 	Object^ other ) override ``` |

#### Parameters

other
:   Type:  System Object    
     The ForgeTypeId with which to compare this ForgeTypeId.

#### Return Value

True if the given ForgeTypeId is equal to this one, or false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |

# See Also

[ForgeTypeId Class](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90ac4bbb-7f65-763a-bf5e-a76b2a167294.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DisplacementPath Class

---



|  |
| --- |
| [Members](a4946353-194c-b567-57f2-2170d7028645.htm)   [See Also](#seeAlsoToggle) |

A view-specific annotation related to a DisplacementElement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class DisplacementPath : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DisplacementPath _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DisplacementPath : public Element ``` |

# Remarks

The DisplacementPath is anchored to the DisplacementElement by a reference to a point on an edge of a source element of the DisplacementElement. It is represented by a single line, or a series of jogged lines, originating at the specified point on the displaced element.

The associated DisplacementElement may have a parent DisplacementElement and this parent may have its own parent DisplacementElement, producing a series of ancestors. The terminal point may be the point's original (un-displaced) location, or the corresponding point on any of the intermediate displaced locations corresponding to these ancestor DisplacementElements.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB DisplacementPath

# See Also

[DisplacementPath Members](a4946353-194c-b567-57f2-2170d7028645.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90b42598-db00-cd08-c0ee-f7dda098560d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveNext Method

---



|  |
| --- |
| [PhaseArrayIterator Class](c6aebfe6-d774-32a7-f908-7c6493d5bed9.htm)   [See Also](#seeAlsoToggle) |

Move the iterator one item forward.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool MoveNext() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function MoveNext As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool MoveNext() ``` |

#### Return Value

Returns True if the iterator was successfully moved forward one item and the Current property will return a valid item. False will be returned it the iterator has reached the end of the array.

#### Implements

 [IEnumerator MoveNext](http://msdn2.microsoft.com/en-us/library/ycwa4b0c)

# Remarks

MoveNext must be called before the Current property is valid with a new or Reset iterator in line with the expected behavior of IEnumerator.

# See Also

[PhaseArrayIterator Class](c6aebfe6-d774-32a7-f908-7c6493d5bed9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90b4e1f7-8509-eb98-fb2f-1bac72a7208b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [AnalysisDisplayColorEntry Class](71d66cd5-6dae-22f0-f364-838e13cfbf8e.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsValidObject { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsValidObject As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsValidObject { 	bool get (); } ``` |

#### Return Value

True if the API object holds a valid Revit native object, false otherwise.

# Remarks

If the corresponding Revit native object is destroyed, or creation of the corresponding object is undone, a managed API object containing it is no longer valid. API methods cannot be called on invalidated wrapper objects.

# See Also

[AnalysisDisplayColorEntry Class](71d66cd5-6dae-22f0-f364-838e13cfbf8e.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__90bee174-b359-f0c6-fbb8-8422a5c870e6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WattsPerSquareFoot Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Watts per square foot.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId WattsPerSquareFoot { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WattsPerSquareFoot As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ WattsPerSquareFoot { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90bf5784-0076-ded0-41fb-38fcb8ed6abe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HVACLoadType Class

---



|  |
| --- |
| [Members](52327db5-656f-d858-d116-85bfe6912127.htm)   [See Also](#seeAlsoToggle) |

The base class for building type and space type.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public class HVACLoadType : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class HVACLoadType _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class HVACLoadType : public Element ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB.Analysis HVACLoadType    
  [Autodesk.Revit.DB.Analysis HVACLoadBuildingType](db7c8da2-260f-94b7-990e-f32ad234ec87.htm)    
  [Autodesk.Revit.DB.Analysis HVACLoadSpaceType](0fcf26fe-8542-3dc7-b9e8-8c89eda1a48d.htm)

# See Also

[HVACLoadType Members](52327db5-656f-d858-d116-85bfe6912127.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__90c2ea06-4e80-c8c0-dbde-1b3f831c2de5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CompoundStructureLayer Constructor (Double, MaterialFunctionAssignment, ElementId)

---



|  |
| --- |
| [CompoundStructureLayer Class](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.htm)   [See Also](#seeAlsoToggle) |

Creates a default compound structure layer based on the given width, function and material element id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public CompoundStructureLayer( 	double width, 	MaterialFunctionAssignment function, 	ElementId materialId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	width As Double, _ 	function As MaterialFunctionAssignment, _ 	materialId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: CompoundStructureLayer( 	double width,  	MaterialFunctionAssignment function,  	ElementId^ materialId ) ``` |

#### Parameters

width
:   Type:  System Double    
     The width of the layer.

function
:   Type:  [Autodesk.Revit.DB MaterialFunctionAssignment](1cbeb006-f7a2-f6d2-491f-faa0b9a006fc.htm)    
     The function of the layer.

materialId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The material element id of the layer.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[CompoundStructureLayer Class](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.htm)

[CompoundStructureLayer Overload](d891bb72-066f-caeb-4322-81e30ae45a24.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90c56de3-99ff-cb0d-2303-576cf0e06d1d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Product Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

The product type for the current session of Revit.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ProductType Product { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Product As ProductType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ProductType Product { 	ProductType get (); } ``` |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__90c888b4-ccc4-41ec-7ab1-c6bf9ede8cc0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumCurveLoops Property

---



|  |
| --- |
| [Path3d Class](459b6d79-a4e7-06f5-ab30-4ec8cffab15b.htm)   [See Also](#seeAlsoToggle) |

Get the Number of Curve Loops of Path3d.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int NumCurveLoops { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property NumCurveLoops As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int NumCurveLoops { 	int get (); } ``` |

# Remarks

Returns the Number of Curve Loops of Path3d.

# See Also

[Path3d Class](459b6d79-a4e7-06f5-ab30-4ec8cffab15b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90cb589c-9d50-c4f1-1217-9d19ee85af0d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpacingNumDivisions Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Number"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpacingNumDivisions { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpacingNumDivisions As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpacingNumDivisions { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90ce7009-7629-9395-8266-b0d94cc6df93.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### JoulesPerGramDegreeCelsius Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Joules per gram degree Celsius.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId JoulesPerGramDegreeCelsius { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property JoulesPerGramDegreeCelsius As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ JoulesPerGramDegreeCelsius { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90d2062e-8e6e-a69e-68de-bef31a7810c2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FilterOperatorAndTextString Class

---



|  |
| --- |
| [Members](1a60fc50-f262-e036-c86f-b6785762efa9.htm)   [See Also](#seeAlsoToggle) |

An instance of this class holds a filter operator and a text string that denotes the operator in a particular context. For example, the text string for ScheduleFilterType::LessThan may be "is less than" for a filter rule based on a parameter with numerical values or "is below" for a filter rule based on a parameter representing a Level.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public class FilterOperatorAndTextString : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FilterOperatorAndTextString _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FilterOperatorAndTextString : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB FilterOperatorAndTextString

# See Also

[FilterOperatorAndTextString Members](1a60fc50-f262-e036-c86f-b6785762efa9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90d4aafe-0c68-e02f-2a3c-2971d320c739.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [PaperSourceSetIterator Class](dd316cd4-ac08-b1e2-2d36-4cc9250d0e78.htm)   [See Also](#seeAlsoToggle) |

Retrieves the item that is the current focus of the iterator.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual Object Current { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property Current As Object 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property Object^ Current { 	Object^ get (); } ``` |

#### Implements

 [IEnumerator Current](http://msdn2.microsoft.com/en-us/library/khfze649)

# Remarks

A new or Reset iterator must have MoveNext called on it before Current will return a valid item as per expected behavior of IEnumerator.

# See Also

[PaperSourceSetIterator Class](dd316cd4-ac08-b1e2-2d36-4cc9250d0e78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90d5ad07-8b4f-87fd-7ba1-4942496df7d5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnboundedHeight Property

---



|  |
| --- |
| [Room Class](75c9d2c7-a402-ea8b-9e7c-f8bc3510bbd5.htm)   [See Also](#seeAlsoToggle) |

Get the Unbounded Height of the Room.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double UnboundedHeight { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property UnboundedHeight As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double UnboundedHeight { 	double get (); } ``` |

# Remarks

This property is used to get the Unbounded Height of the Room.

# See Also

[Room Class](75c9d2c7-a402-ea8b-9e7c-f8bc3510bbd5.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__90d75bb8-07ce-eee9-0995-838c2f1576f1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HeatTransferCoefficient Property

---



|  |
| --- |
| [FamilyThermalProperties Class](9d9b2125-8398-9b55-8219-cbda4456ab7b.htm)   [See Also](#seeAlsoToggle) |

The heat transfer coefficient value (U-Value). The units are watts per meter-squared kelvin (W/(m^2\*K)).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double HeatTransferCoefficient { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HeatTransferCoefficient As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double HeatTransferCoefficient { 	double get (); } ``` |

# See Also

[FamilyThermalProperties Class](9d9b2125-8398-9b55-8219-cbda4456ab7b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90dd0996-ed6b-b8e6-2b53-151434c6abc8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, AnalyticalSystemDomain, String)

---



|  |
| --- |
| [ZoneEquipment Class](62330781-b72c-02ae-0c30-c557decfc38a.htm)   [See Also](#seeAlsoToggle) |

Creates a new zone equipment

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` [ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit.")] public static ZoneEquipment Create( 	Document document, 	AnalyticalSystemDomain systemDomain, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` <ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit.")> _ Public Shared Function Create ( _ 	document As Document, _ 	systemDomain As AnalyticalSystemDomain, _ 	name As String _ ) As ZoneEquipment ``` |

 

| Visual C++ |
| --- |
| ``` [ObsoleteAttribute(L"This method is deprecated in Revit 2023 and may be removed in a later version of Revit.")] public: static ZoneEquipment^ Create( 	Document^ document,  	AnalyticalSystemDomain systemDomain,  	String^ name ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document where the new element will be created.

systemDomain
:   Type:  [Autodesk.Revit.DB.Mechanical AnalyticalSystemDomain](01a07a9f-5cea-42e2-6630-88a032e88f85.htm)    
     The system domain of zone equipment.

name
:   Type:  System String    
     The name of new zone equipment. The actual name may be post-fixed if already exists.

#### Return Value

The newly created zone equipment.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". -or- name is an empty string. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[ZoneEquipment Class](62330781-b72c-02ae-0c30-c557decfc38a.htm)

[Create Overload](66d277a9-5ef0-41e8-3410-63403be0b3c3.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__90e19864-52cf-2f0c-4792-698236b03c9b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSelectionFilter Method

---



|  |
| --- |
| [PointCloudInstance Class](d17686cb-b8c5-bee5-44d3-0311d27678e0.htm)   [See Also](#seeAlsoToggle) |

Returns the currently active selection filter for this point cloud.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PointCloudFilter GetSelectionFilter() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSelectionFilter As PointCloudFilter ``` |

 

| Visual C++ |
| --- |
| ``` public: PointCloudFilter^ GetSelectionFilter() ``` |

#### Return Value

Currently active selection filter or    a null reference (  Nothing  in Visual Basic)  if none is active.

# See Also

[PointCloudInstance Class](d17686cb-b8c5-bee5-44d3-0311d27678e0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90e1b29d-7e8f-428d-3d88-4a80560b455a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsJoinAllowedAtEnd Method

---



|  |
| --- |
| [StructuralFramingUtils Class](93d93c87-dfa2-12d5-dcb0-13d5cb0c0696.htm)   [See Also](#seeAlsoToggle) |

Identifies if the indicated end of the framing element is allowed to join to others.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static bool IsJoinAllowedAtEnd( 	FamilyInstance familyInstance, 	int end ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsJoinAllowedAtEnd ( _ 	familyInstance As FamilyInstance, _ 	end As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsJoinAllowedAtEnd( 	FamilyInstance^ familyInstance,  	int end ) ``` |

#### Parameters

familyInstance
:   Type:  [Autodesk.Revit.DB FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)    
     The FamilyInstance, which must be of a structural framing category.

end
:   Type:  System Int32    
     The index of the end (0 for the start, 1 for the end).

#### Return Value

True if it is allowed to join. False if it is disallowed.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1. |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | The input familyInstance is not of a structural framing category. |

# See Also

[StructuralFramingUtils Class](93d93c87-dfa2-12d5-dcb0-13d5cb0c0696.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__90e28a35-e861-6b38-3c5b-3ba14db0c5cf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotChangeUserSketchPlaneError Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Can't change plane of [Element Name] Sketch.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotChangeUserSketchPlaneError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotChangeUserSketchPlaneError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotChangeUserSketchPlaneError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90e2fdde-5052-90fa-1cb2-06303c2991b4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsPipeInsulationThickness Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Insulation Thickness"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsPipeInsulationThickness { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsPipeInsulationThickness As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsPipeInsulationThickness { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90e66b0d-9710-07c9-4c78-80cbf722e262.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EdgeEndPoint Constructor (Edge, Int32)

---



|  |
| --- |
| [EdgeEndPoint Class](3388e8f3-22d4-a411-a3da-450c16a31bc5.htm)   [See Also](#seeAlsoToggle) |

Constructs an instance of EdgeEndPoint.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public EdgeEndPoint( 	Edge edge, 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	edge As Edge, _ 	index As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: EdgeEndPoint( 	Edge^ edge,  	int index ) ``` |

#### Parameters

edge
:   Type:  [Autodesk.Revit.DB Edge](7155ef49-fcd9-c80a-6232-70189a617bcc.htm)    
     The Edge.

index
:   Type:  System Int32    
     Use 0 for the start point, 1 for the end point of an Edge.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for index is not 0 or 1. |

# See Also

[EdgeEndPoint Class](3388e8f3-22d4-a411-a3da-450c16a31bc5.htm)

[EdgeEndPoint Overload](eb9f37f5-e13f-8a3c-69b0-6117ab440dcf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90e86110-9bce-6e43-c18a-4d67380008bb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Intersect Method (Curve)

---



|  |
| --- |
| [Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)   [See Also](#seeAlsoToggle) |

Calculates the intersection of this curve with the specified curve.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public SetComparisonResult Intersect( 	Curve curve ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Intersect ( _ 	curve As Curve _ ) As SetComparisonResult ``` |

 

| Visual C++ |
| --- |
| ``` public: SetComparisonResult Intersect( 	Curve^ curve ) ``` |

#### Parameters

curve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The specified curve to intersect with this curve.

#### Return Value

* SetComparisonResult.Overlap - One or more intersections were encountered.
* SetComparisonResult.Subset - The inputs are parallel lines with only one common intersection point, or the curve used to invoke the intersection check is a line entirely within the unbound line passed as argument curve.
* SetComparisonResult.Superset - The input curve is entirely within the unbound line used to invoke the intersection check.
* SetComparisonResult.Disjoint - There is no intersection found between the two curves.
* SetComparisonResult.Equal - The two curves are identical.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | The specified curve is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to calculate the intersection. |

# See Also

[Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)

[Intersect Overload](570fb842-cac3-83f5-1ab9-621e55186ead.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90e9a3c7-e10c-ac6c-3d9c-923c39d3acdd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsHvacloadSkylightAreaParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Skylight Area"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsHvacloadSkylightAreaParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsHvacloadSkylightAreaParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsHvacloadSkylightAreaParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90f1e5b9-8d0c-8761-ed77-d7b9ff5cd764.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VertexPosition Constructor

---



|  |
| --- |
| [VertexPosition Class](718e49aa-9e17-6f2d-2013-141b5cfeefdd.htm)   [See Also](#seeAlsoToggle) |

Constructs the vertex from a point.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public VertexPosition( 	XYZ position ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	position As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: VertexPosition( 	XYZ^ position ) ``` |

#### Parameters

position
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vertex's position.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[VertexPosition Class](718e49aa-9e17-6f2d-2013-141b5cfeefdd.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__90f62108-9cd1-a66a-a123-8372307f4e7f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElectricalSystemType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all the possible electrical system types for a connector object.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public enum ElectricalSystemType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ElectricalSystemType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ElectricalSystemType ``` |

# Members

| Member name | Description |
| --- | --- |
| UndefinedSystemType | Undefined system type |
| Data | Electrical System Type is Data. |
| PowerCircuit | Electrical System Type is PowerCircuit. |
| Telephone | Electrical System Type is Telephone. |
| Security | Electrical System Type is Security |
| FireAlarm | Electrical System Type is FireAlarm |
| NurseCall | System Type is NurseCall. |
| Controls | Electrical System Type is Controls. |
| Communication | Electrical System Type is Communication. |
| PowerBalanced | Electrical System Type is PowerBalanced. |
| PowerUnBalanced | Electrical System Type is PowerUnBalanced. |

# See Also

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__90f7d182-95df-673e-4a24-f2111ff3c6cf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsValidObject { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsValidObject As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsValidObject { 	bool get (); } ``` |

#### Return Value

True if the API object holds a valid Revit native object, false otherwise.

# Remarks

If the corresponding Revit native object is destroyed, or creation of the corresponding object is undone, a managed API object containing it is no longer valid. API methods cannot be called on invalidated wrapper objects.

# See Also

[VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__90f7dec1-5c06-1411-098f-a5e076be5406.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetConduitSettings Method

---



|  |
| --- |
| [ConduitSettings Class](c86a1700-e477-3888-7647-3eafa528fe5d.htm)   [See Also](#seeAlsoToggle) |

Gets the conduit settings of the project.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static ConduitSettings GetConduitSettings( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetConduitSettings ( _ 	document As Document _ ) As ConduitSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: static ConduitSettings^ GetConduitSettings( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

#### Return Value

The conduit settings of the project.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ConduitSettings Class](c86a1700-e477-3888-7647-3eafa528fe5d.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__90fba405-1ce0-1a4c-f601-3a4e91d34eaf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OmniclassCode Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"OmniClass Number"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId OmniclassCode { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property OmniclassCode As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ OmniclassCode { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__90ff0a2e-7a57-b692-aa0d-c589c91479b7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TopWebFillet Property

---



|  |
| --- |
| [StructuralSectionGeneralT Class](308dc954-e403-b95c-3f1c-3a9a4c22beaf.htm)   [See Also](#seeAlsoToggle) |

Top Web Fillet - fillet radius at the top of web.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public double TopWebFillet { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property TopWebFillet As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double TopWebFillet { 	double get (); 	void set (double value); } ``` |

# See Also

[StructuralSectionGeneralT Class](308dc954-e403-b95c-3f1c-3a9a4c22beaf.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__91a00b03-40ef-3411-61a8-fd4cee173e92.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SymbolNameParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Type Name"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SymbolNameParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SymbolNameParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SymbolNameParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91a3b412-b96a-a754-45c7-0864e7c75c06.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanViewBeDuplicated Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Identifies if this view can be duplicated.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool CanViewBeDuplicated( 	ViewDuplicateOption duplicateOption ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanViewBeDuplicated ( _ 	duplicateOption As ViewDuplicateOption _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanViewBeDuplicated( 	ViewDuplicateOption duplicateOption ) ``` |

#### Parameters

duplicateOption
:   Type:  [Autodesk.Revit.DB ViewDuplicateOption](a67f43c7-d350-ca90-ec69-304bde9c7262.htm)    
     The option to use when duplicating the view.

#### Return Value

True if the view can be duplicated, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91a559a5-75ed-398d-b0c5-67a9962b652d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PreserveOverrides Property

---



|  |
| --- |
| [CADLinkOptions Class](a5d5d78c-cc65-c7a5-0bc8-4413156a2114.htm)   [See Also](#seeAlsoToggle) |

Whether Revit should preserve the link's graphic overrides on reload.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool PreserveOverrides { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PreserveOverrides As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool PreserveOverrides { 	bool get (); 	void set (bool value); } ``` |

# See Also

[CADLinkOptions Class](a5d5d78c-cc65-c7a5-0bc8-4413156a2114.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91ab315a-b3ba-0fae-1c52-c750037a6fe8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveTemperature Method

---



|  |
| --- |
| [FluidType Class](6de7a895-6747-7273-55cf-19f917a30c84.htm)   [See Also](#seeAlsoToggle) |

Removes a fluid temperature via the temperature value from the set.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void RemoveTemperature( 	double temperature ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveTemperature ( _ 	temperature As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveTemperature( 	double temperature ) ``` |

#### Parameters

temperature
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The temperature value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the temperature that will be removed doesn't exist in the fluid type or the temperature that will be removed is in use. |

# See Also

[FluidType Class](6de7a895-6747-7273-55cf-19f917a30c84.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__91abfaff-2abe-225d-ab00-f8b301b81392.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFlags Method (IList(Int32))

---



|  |
| --- |
| [ValueAtPointBase Class](67c49547-b5b9-59ad-8106-65d90886a381.htm)   [See Also](#seeAlsoToggle) |

Independently sets the flags associated to all measurements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetFlags( 	IList<int> flags ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFlags ( _ 	flags As IList(Of Integer) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFlags( 	IList<int>^ flags ) ``` |

#### Parameters

flags
:   Type:  System.Collections.Generic IList   Int32    
     An array of flags values. Each member corresponds to a measurement. Flags values are defined in the enumerated class ValueAtPointFlags and are combined into the int value. Number of measurements is set at creation of SpatialFieldManager in method createSpatialFieldManager.

# Remarks

If you set the array of flags to only contain one value, this flags value will apply to all measurements

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ValueAtPointBase Class](67c49547-b5b9-59ad-8106-65d90886a381.htm)

[SetFlags Overload](dff6d4fa-7c12-ca4e-0439-75b1e4f80b9e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91ad316c-109c-7295-af34-c61d1bfaa2ec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Empty Method

---



|  |
| --- |
| [ForgeTypeId Class](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)   [See Also](#seeAlsoToggle) |

Checks if the typeId is an empty string

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public bool Empty() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Empty As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Empty() ``` |

# See Also

[ForgeTypeId Class](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91ae4538-e1f5-7183-9490-63721418d287.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NotOneCCWLoop Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

This sketch defines more than one footprint. Make sure the sketch contains only one outermost loop and that there are no loops inside inner loops.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NotOneCCWLoop { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NotOneCCWLoop As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NotOneCCWLoop { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91b18d1e-0df7-c438-2a0b-54c97c55524e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DistanceBetweenBarsWarning Property

---



|  |
| --- |
| [BuiltInFailures RebarCouplerFailures Class](f1af7139-8dc7-c6de-b703-b01eb95fdff3.htm)   [See Also](#seeAlsoToggle) |

This is used to post warning. The distance between the connected ends of the bars exceeds 10 bar diameters.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DistanceBetweenBarsWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DistanceBetweenBarsWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DistanceBetweenBarsWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarCouplerFailures Class](f1af7139-8dc7-c6de-b703-b01eb95fdff3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91b5e6fb-386a-eed2-6c65-59342a14b304.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEmpty Property

---



|  |
| --- |
| [ElementArray Class](6a3046e5-aad4-f1fa-b733-bfd57bc9cbc5.htm)   [See Also](#seeAlsoToggle) |

Test to see if the array is empty.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool IsEmpty { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property IsEmpty As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property bool IsEmpty { 	bool get (); } ``` |

# Remarks

If the array is empty then True will be returned, otherwise False.

# See Also

[ElementArray Class](6a3046e5-aad4-f1fa-b733-bfd57bc9cbc5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91b85bbf-4ae5-883f-3f51-f7720b1ca964.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomLevelElevs Property

---



|  |
| --- |
| [BuiltInFailures RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.htm)   [See Also](#seeAlsoToggle) |

A [Room]s Upper Limit must be above its Base Level.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RoomLevelElevs { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoomLevelElevs As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RoomLevelElevs { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91bda73b-c1e6-9ce6-0c5a-1cfc626a6ec4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationPartCannotChangeTypeWarning Property

---



|  |
| --- |
| [BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)   [See Also](#seeAlsoToggle) |

The selected fitting(s) cannot maintain connections to existing fabrication parts due to size, direction or angle differences. You must manually reconnect the open connections.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FabricationPartCannotChangeTypeWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationPartCannotChangeTypeWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FabricationPartCannotChangeTypeWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91be7b3c-ccd9-400a-9791-1bac6faba8ec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Size Property

---



|  |
| --- |
| [ModelCurveArray Class](c7852e5b-0a34-771f-584f-3e9513bca50e.htm)   [See Also](#seeAlsoToggle) |

Returns the number of model curves that are in the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual int Size { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property Size As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property int Size { 	int get (); } ``` |

# See Also

[ModelCurveArray Class](c7852e5b-0a34-771f-584f-3e9513bca50e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91c25df5-078c-de36-76c7-6520d65882cc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BadClassificationLevel Property

---



|  |
| --- |
| [BuiltInFailures KeyBasedTreeEntryFailures Class](c9cc2403-573b-9327-37fe-3fc4e5eb485d.htm)   [See Also](#seeAlsoToggle) |

Level [Level] of Classification [Code] is not an integer from 1 to 5.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId BadClassificationLevel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BadClassificationLevel As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ BadClassificationLevel { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures KeyBasedTreeEntryFailures Class](c9cc2403-573b-9327-37fe-3fc4e5eb485d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91c2c764-9d24-7b8d-e6ff-3ae861f3bb1e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ZoneUseOutsideAirPerAreaParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Use Outside Air Per Area"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ZoneUseOutsideAirPerAreaParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ZoneUseOutsideAirPerAreaParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ZoneUseOutsideAirPerAreaParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91c4f3e9-d268-dfcb-fed4-fcee840ceb3a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallSide Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Represents the possible sides of a wall where a sweep or reveal may be attached.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public enum WallSide ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration WallSide ``` |

 

| Visual C++ |
| --- |
| ``` public enum class WallSide ``` |

# Members

| Member name | Description |
| --- | --- |
| Exterior | The exterior of the wall. |
| Interior | The interior of the wall. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91cce146-1392-ceea-80d8-f29d96915bd7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadMomentMy1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"My 1"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LoadMomentMy1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoadMomentMy1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LoadMomentMy1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91ce3b83-4d34-c62c-8b17-da062790c851.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricSheetMinorSpacing Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Minor Spacing": Minor Spacing

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FabricSheetMinorSpacing { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricSheetMinorSpacing As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FabricSheetMinorSpacing { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__91cf0879-d401-4f6b-c26b-6b3ece4200db.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSolidFill Property

---



|  |
| --- |
| [FillPattern Class](cc546ee9-ba80-c13d-4b74-8c0e2517bc28.htm)   [See Also](#seeAlsoToggle) |

Check if the fill pattern is a solid fill pattern.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsSolidFill { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsSolidFill As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsSolidFill { 	bool get (); } ``` |

# See Also

[FillPattern Class](cc546ee9-ba80-c13d-4b74-8c0e2517bc28.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)