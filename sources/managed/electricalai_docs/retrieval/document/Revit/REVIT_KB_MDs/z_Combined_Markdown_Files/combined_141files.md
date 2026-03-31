

<!-- Start of Syntax__fe052840-c872-dcbd-c2b3-ca088be27c4b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Visible Property

---



|  |
| --- |
| [CurveByPoints Class](2df7ab39-1ac0-5803-79fa-b23a959bf8f2.htm)   [See Also](#seeAlsoToggle) |

Whether the point is visible when the family is loaded into a project.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool Visible { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Visible As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool Visible { 	bool get (); 	void set (bool value); } ``` |

# See Also

[CurveByPoints Class](2df7ab39-1ac0-5803-79fa-b23a959bf8f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe078250-71c4-6a19-ac0d-6d674b86fac9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CitySetIterator Class

---



|  |
| --- |
| [Members](3832dfda-4259-8631-6eab-9297156611d6.htm)   [See Also](#seeAlsoToggle) |

An iterator to a city set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public abstract class CitySetIterator : APIObject,  	IEnumerator ``` |

 

| Visual Basic |
| --- |
| ``` Public MustInherit Class CitySetIterator _ 	Inherits APIObject _ 	Implements IEnumerator ``` |

 

| Visual C++ |
| --- |
| ``` public ref class CitySetIterator abstract : public APIObject,  	IEnumerator ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB CitySetIterator

# See Also

[CitySetIterator Members](3832dfda-4259-8631-6eab-9297156611d6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe10010f-e127-7248-1f17-8c1ee0d41ea0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NullParameterValue Class

---



|  |
| --- |
| [Members](e83d2f24-08da-4f7b-9ba5-c35d2c4d8aa5.htm)   [See Also](#seeAlsoToggle) |

A class that represent an empty (null) value of a parameter element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public class NullParameterValue : ParameterValue ``` |

 

| Visual Basic |
| --- |
| ``` Public Class NullParameterValue _ 	Inherits ParameterValue ``` |

 

| Visual C++ |
| --- |
| ``` public ref class NullParameterValue : public ParameterValue ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ParameterValue](366521ef-ecc2-c3e3-feb5-81b3bbd8df0c.htm)    
  Autodesk.Revit.DB NullParameterValue

# See Also

[NullParameterValue Members](e83d2f24-08da-4f7b-9ba5-c35d2c4d8aa5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe14085f-5643-db65-6cd7-05773be33c3b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidGlobalParameter Method

---



|  |
| --- |
| [GlobalParametersManager Class](f3af05ec-1f0c-fe86-6708-0a211a40bcda.htm)   [See Also](#seeAlsoToggle) |

Tests whether an ElementId is of a global parameter in the given document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public static bool IsValidGlobalParameter( 	Document document, 	ElementId parameterId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidGlobalParameter ( _ 	document As Document, _ 	parameterId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidGlobalParameter( 	Document^ document,  	ElementId^ parameterId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the global parameter.

parameterId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of a global parameter

#### Return Value

Returns True if the Id is of a valid global parameter; False otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[GlobalParametersManager Class](f3af05ec-1f0c-fe86-6708-0a211a40bcda.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe28901c-f078-2614-ab6a-1d09dfa18729.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, ElementId, ElementId, XYZ, Int32)

---



|  |
| --- |
| [ScheduleSheetInstance Class](68db8e46-90de-6b54-3dae-598957d94201.htm)   [See Also](#seeAlsoToggle) |

Creates an instance of a schedule segment on a sheet.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022.1

# Syntax

| C# |
| --- |
| ``` public static ScheduleSheetInstance Create( 	Document document, 	ElementId viewSheetId, 	ElementId scheduleId, 	XYZ origin, 	int segmentIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	viewSheetId As ElementId, _ 	scheduleId As ElementId, _ 	origin As XYZ, _ 	segmentIndex As Integer _ ) As ScheduleSheetInstance ``` |

 

| Visual C++ |
| --- |
| ``` public: static ScheduleSheetInstance^ Create( 	Document^ document,  	ElementId^ viewSheetId,  	ElementId^ scheduleId,  	XYZ^ origin,  	int segmentIndex ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document

viewSheetId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the sheet where the schedule segment will be placed.

scheduleId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the schedule view.

origin
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Location on the sheet where the schedule segment will be placed.

segmentIndex
:   Type:  System Int32    
     The schedule segment index of the schedule instance.

#### Return Value

The new ScheduleInstance.

# Remarks

The segment index value could be -1, which means to create an instance for the entire schedule, see  [SegmentIndex](69ecefc6-2bc3-d1b1-0777-b6ada9c4f789.htm)  property for more details.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | scheduleId is not a ViewSchedule that can be added to sheets. "Internal" schedules are not user-visible but are filtered by sheet or used to manage Revisions, which cannot be added to sheets. -or- viewSheetId is not a ViewSheet. -or- segmentIndex is not a valid segment index. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[ScheduleSheetInstance Class](68db8e46-90de-6b54-3dae-598957d94201.htm)

[Create Overload](74edddf6-94b5-db01-d458-3c2d50342957.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe35110e-81fb-b815-440a-38d37bf659a2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointFlexibleConstrained Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Constrained"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PointFlexibleConstrained { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PointFlexibleConstrained As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PointFlexibleConstrained { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe380062-4158-b6ce-2fe0-006585daf3d6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Construction Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Construction"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Construction { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Construction As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Construction { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe4910d2-d336-787b-c914-69fbc7e81db7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [UpdaterInfo Class](839e2681-fa26-6587-5a92-e8dcd88af852.htm)   [See Also](#seeAlsoToggle) |

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

[UpdaterInfo Class](839e2681-fa26-6587-5a92-e8dcd88af852.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe5490b8-134d-009b-b63e-fe46b7e420d1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DivideVolumesProfilesGapForWidthAll Property

---



|  |
| --- |
| [BuiltInFailures DPartFailures Class](60230c02-eb7e-98f0-38c8-8da51b5109a8.htm)   [See Also](#seeAlsoToggle) |

Division family cannot be used with the selected division gap for all widths of hosts

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DivideVolumesProfilesGapForWidthAll { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DivideVolumesProfilesGapForWidthAll As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DivideVolumesProfilesGapForWidthAll { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DPartFailures Class](60230c02-eb7e-98f0-38c8-8da51b5109a8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe6170c6-9e54-fdef-bb16-64833ec4fb76.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetInsulationLiningGeometry Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Gets insulation and lining geometry for this fabrication part.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2019.1

# Syntax

| C# |
| --- |
| ``` public GeometryElement GetInsulationLiningGeometry() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetInsulationLiningGeometry As GeometryElement ``` |

 

| Visual C++ |
| --- |
| ``` public: GeometryElement^ GetInsulationLiningGeometry() ``` |

#### Return Value

Returns any insulation and liner geometry.

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe684616-5a84-6984-d731-b9efe21367ed.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetSpecificFittingAngleStatus Method

---



|  |
| --- |
| [PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.htm)   [See Also](#seeAlsoToggle) |

Sets the status of given specific angle.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetSpecificFittingAngleStatus( 	double angle, 	bool bStatus ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetSpecificFittingAngleStatus ( _ 	angle As Double, _ 	bStatus As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetSpecificFittingAngleStatus( 	double angle,  	bool bStatus ) ``` |

#### Parameters

angle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The specific angle (in degree) that must be one of 60, 45, 30, 22.5 or 11.25 degrees.

bStatus
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     Status, true - using the given angle during the pipe layout.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for angle must be 90, 60, 45, 30, 22.5 or 11.25 degrees. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Can not set an angle status for an invalid angle. |

# See Also

[PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__fe80084f-2b75-cc39-bf64-866bc2c27bb1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FormUtils Class

---



|  |
| --- |
| [Members](53c4ceef-95ff-083d-434f-dc64fa3d8824.htm)   [See Also](#seeAlsoToggle) |

Define Form utility functions

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class FormUtils ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class FormUtils ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FormUtils abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB FormUtils

# See Also

[FormUtils Members](53c4ceef-95ff-083d-434f-dc64fa3d8824.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe81194a-a819-22b4-0900-7d91f6319569.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SheetAssemblyTypeMark Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Assembly: Type Mark"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SheetAssemblyTypeMark { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SheetAssemblyTypeMark As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SheetAssemblyTypeMark { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe8333e0-f250-f86c-0c86-9c30f4b07f07.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarSystemHookTypeFrontDirn2 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Exterior Minor Hook Type"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarSystemHookTypeFrontDirn2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarSystemHookTypeFrontDirn2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarSystemHookTypeFrontDirn2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe946287-80cf-93ab-a10a-4b11f3064c33.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanFilterByValuePresence Method

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Checks whether a field can be used with a value presence-based filter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public bool CanFilterByValuePresence( 	ScheduleFieldId fieldId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanFilterByValuePresence ( _ 	fieldId As ScheduleFieldId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanFilterByValuePresence( 	ScheduleFieldId^ fieldId ) ``` |

#### Parameters

fieldId
:   Type:  [Autodesk.Revit.DB ScheduleFieldId](e437cc01-b976-fe8a-225a-1a0024171fae.htm)    
     The ID of the field to check.

#### Return Value

True if the field can be used with a value presence filter, false otherwise.

# Remarks

The value presence filter types are HasValue and HasNoValue.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | fieldId is not the ID of a field in this ScheduleDefinition. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fea4df07-ac92-08f3-ae93-8d0a512d0e76.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RepeatElements Method

---



|  |
| --- |
| [ComponentRepeater Class](27dbc5bd-40e7-c044-11e6-7053adf92c6f.htm)   [See Also](#seeAlsoToggle) |

Repeats a set of adaptive component hosted on one or more repeating references.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static IList<ComponentRepeater> RepeatElements( 	Document document, 	ICollection<ElementId> elementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function RepeatElements ( _ 	document As Document, _ 	elementIds As ICollection(Of ElementId) _ ) As IList(Of ComponentRepeater) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<ComponentRepeater^>^ RepeatElements( 	Document^ document,  	ICollection<ElementId^>^ elementIds ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document that contains the elements.

elementIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The set of adaptive components used as an input pattern for the repeating operation.

#### Return Value

One or more component repeater objects representing the result pattern of the repeating operation.

# Remarks

All elements must be adaptive family instances and have no shape handles. At least one placement point must be hosted on a 1D or 2D repeating reference. All other placement points can be hosted on a 0D, 1D or 2D repeating reference, or must be unhosted. Use  [CanElementBeRepeated(Document, ElementId)](85030abd-7476-91fc-a67b-50dd8bcf9697.htm)  to test whether an element meets these conditions.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The document does not allow creation of a component repeater. -or- The given element id set is empty. -or- One or more elements in elementIds do not exist in the document. -or- Not all given elements can be repeated. All elements must be adaptive family instances, have no shape handles, and have at least one placement point hosted on a 1D or 2D repeating reference. The remaining placement points must be either unhosted or hosted on another repeating reference. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[ComponentRepeater Class](27dbc5bd-40e7-c044-11e6-7053adf92c6f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fea89647-0f64-62d0-1947-2e167410d531.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FbxLightPhotometricFileCache Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"None"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FbxLightPhotometricFileCache { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FbxLightPhotometricFileCache As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FbxLightPhotometricFileCache { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fea89767-8c2c-6d4b-24b3-bfedea8ffbe4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecAnalyticalLoadSetOnStandby Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Quantity of Standby"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecAnalyticalLoadSetOnStandby { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecAnalyticalLoadSetOnStandby As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecAnalyticalLoadSetOnStandby { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fea89837-310d-f1cd-0026-90b6e9605149.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [LineSegment Class](d67cd999-109a-9465-39d0-99bba3e775cf.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [LineSegment](d67cd999-109a-9465-39d0-99bba3e775cf.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void Dispose() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Dispose ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Dispose() sealed ``` |

#### Implements

 [IDisposable Dispose](http://msdn2.microsoft.com/en-us/library/es4s3w1d)

# See Also

[LineSegment Class](d67cd999-109a-9465-39d0-99bba3e775cf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__feaa00f9-bef4-c7d0-7529-eb71452554c7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.LegendFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](6075d776-64a1-64ed-532c-bd5c4a88d692.htm)   [See Also](#seeAlsoToggle) |

Failures about Legend.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class LegendFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class LegendFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class LegendFailures abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BuiltInFailures LegendFailures

# See Also

[BuiltInFailures LegendFailures Members](6075d776-64a1-64ed-532c-bd5c4a88d692.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__feabfd59-bd0f-ab61-34a1-d0d22f58c881.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSubelements Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Returns the collection of element subelements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public IList<Subelement> GetSubelements() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSubelements As IList(Of Subelement) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Subelement^>^ GetSubelements() ``` |

#### Return Value

The collection of element subelements.

# Remarks

This collection will not include the Element itself.

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__feaf6635-949d-2944-6444-cb42e23a9130.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DecalSubcategoryId Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Subcategory"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DecalSubcategoryId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DecalSubcategoryId As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DecalSubcategoryId { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__feb0c72e-8845-6678-fd43-5fc682c26ce8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasThermalProperties Method

---



|  |
| --- |
| [FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)   [See Also](#seeAlsoToggle) |

Identifies if this FamilySymbol can include thermal properties.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool HasThermalProperties() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function HasThermalProperties As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool HasThermalProperties() ``` |

#### Return Value

True if the FamilySymbol can include thermal properties, false otherwise.

# See Also

[FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__feb28657-1252-f03d-a0b4-fbb3515c8160.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotDrawBlend Property

---



|  |
| --- |
| [BuiltInFailures BlendFailures Class](9d09f095-82d3-e023-d31a-e34b6aa436a6.htm)   [See Also](#seeAlsoToggle) |

Can't create blend.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotDrawBlend { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotDrawBlend As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotDrawBlend { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures BlendFailures Class](9d09f095-82d3-e023-d31a-e34b6aa436a6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__feb61a2e-fe42-b3cb-8ea4-fb33c67a7555.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsParallelconduitsHorizontalNumber Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Horizontal Number for parallel conduits"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsParallelconduitsHorizontalNumber { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsParallelconduitsHorizontalNumber As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsParallelconduitsHorizontalNumber { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__feb70ae9-d577-ca43-0d1c-1fbf6bf00759.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhyMaterialParamTensionParallel Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Tension Parallel to Grain"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PhyMaterialParamTensionParallel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PhyMaterialParamTensionParallel As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PhyMaterialParamTensionParallel { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__febaf468-43ad-4165-fb6d-3ed758e184ac.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FbxLightLumenaireDirt Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Luminaire Dirt Depreciation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FbxLightLumenaireDirt { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FbxLightLumenaireDirt As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FbxLightLumenaireDirt { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__febb3519-72df-7741-e793-21465f9476b1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddConstraintSagittaLength Method

---



|  |
| --- |
| [RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)   [See Also](#seeAlsoToggle) |

Specify a parameter to drive the sagittal length (the height of the circular segment, measured perpendicular to the chord).

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public void AddConstraintSagittaLength( 	ElementId paramId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddConstraintSagittaLength ( _ 	paramId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddConstraintSagittaLength( 	ElementId^ paramId ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of a parameter to drive the constraint. To obtain the id of a shared parameter, call RebarShape.GetElementIdForExternalDefinition().

# Remarks

The sagitta will be measured on the centerline of the bar.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__fec1ec25-47f2-832f-e8ce-9cc8ba02ba6c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlreadyHaveTwoClosurePlanes Property

---



|  |
| --- |
| [BuiltInFailures RefPlaneFailures Class](75323945-7d1e-9488-326d-438194aae8eb.htm)   [See Also](#seeAlsoToggle) |

No more than two closure planes are allowed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId AlreadyHaveTwoClosurePlanes { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AlreadyHaveTwoClosurePlanes As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ AlreadyHaveTwoClosurePlanes { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RefPlaneFailures Class](75323945-7d1e-9488-326d-438194aae8eb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fec3af2e-1c5d-8a84-6bf3-37f1d2633007.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IPrintSetting Interface

---



|  |
| --- |
| [Members](bfd9e268-6a08-e8bb-cea7-4f6f5d69380c.htm)   [See Also](#seeAlsoToggle) |

An interface which represents the Print Setup (Application Menu->Print->Print Setup) within Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public interface IPrintSetting ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IPrintSetting ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IPrintSetting ``` |

# See Also

[IPrintSetting Members](bfd9e268-6a08-e8bb-cea7-4f6f5d69380c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fecb2544-7e93-13a4-3e48-66cfc8689825.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleBaseLevelParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Base Level"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ScheduleBaseLevelParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ScheduleBaseLevelParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ScheduleBaseLevelParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__feccf2ad-3b16-b3ca-5acb-cc4e6f122563.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LipLength Property

---



|  |
| --- |
| [StructuralSectionGeneralC Class](6bb0e7c4-59c9-39a4-2751-f313e928ef46.htm)   [See Also](#seeAlsoToggle) |

Lip segment length.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public double LipLength { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LipLength As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double LipLength { 	double get (); 	void set (double value); } ``` |

# See Also

[StructuralSectionGeneralC Class](6bb0e7c4-59c9-39a4-2751-f313e928ef46.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__fed26b44-d436-fae2-4d3e-ccff6ae337eb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [AnalyticalPanel Class](b88181d3-743b-8cca-8fb3-0cc13e5d70aa.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of an Analytical Panel within the project.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public static AnalyticalPanel Create( 	Document aDoc, 	CurveLoop curveLoop ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	aDoc As Document, _ 	curveLoop As CurveLoop _ ) As AnalyticalPanel ``` |

 

| Visual C++ |
| --- |
| ``` public: static AnalyticalPanel^ Create( 	Document^ aDoc,  	CurveLoop^ curveLoop ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Revit document.

curveLoop
:   Type:  [Autodesk.Revit.DB CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     CurveLoop for the Analytical Panel.

#### Return Value

The newly created AnalyticalPanel instance.

# Remarks

CurveLoop must be planar and not self-intersecting.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One of the following requirements is not satisfied : - curve loop curveLoop is not planar - curve loop curveLoop is self-intersecting - curve loop curveLoop contains zero length curves |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[AnalyticalPanel Class](b88181d3-743b-8cca-8fb3-0cc13e5d70aa.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__fed5122e-b2d2-bfbb-1ca5-db4e8ae9f7c3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateNotEqualsRule Method (ElementId, ElementId)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether ElementId values from the document do not equal a certain value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateNotEqualsRule( 	ElementId parameter, 	ElementId value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateNotEqualsRule ( _ 	parameter As ElementId, _ 	value As ElementId _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateNotEqualsRule( 	ElementId^ parameter,  	ElementId^ value ) ``` |

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

[CreateNotEqualsRule Overload](c3b622c3-1609-9eb7-b3e7-ec13705a24e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fed5f5e3-2f84-1ccf-458d-d2c3f30d3a02.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AncestorIdx Property

---



|  |
| --- |
| [DisplacementPath Class](90ac4bbb-7f65-763a-bf5e-a76b2a167294.htm)   [See Also](#seeAlsoToggle) |

Specifies the end point of the path.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public int AncestorIdx { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AncestorIdx As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int AncestorIdx { 	int get (); 	void set (int value); } ``` |

# See Also

[DisplacementPath Class](90ac4bbb-7f65-763a-bf5e-a76b2a167294.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fed7aa4c-c477-daad-7200-3e20c041d12a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BtuPerDegreeF Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol BTU/Â°F, indicating unit British thermal units per degree Fahrenheit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BtuPerDegreeF { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BtuPerDegreeF As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BtuPerDegreeF { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fed90ae9-3f3b-58fd-a956-fa2f0349be63.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RegionPhaseMismatch Property

---



|  |
| --- |
| [BuiltInFailures SiteFailures Class](7ab66d74-f1ab-17f6-9ecf-e51b3d5326bf.htm)   [See Also](#seeAlsoToggle) |

Subregions must have the same Phase Created parameter and Phase Demolished parameter as the host Toposurface. Subregion phase will be set to match the Toposurface.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RegionPhaseMismatch { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RegionPhaseMismatch As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RegionPhaseMismatch { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SiteFailures Class](7ab66d74-f1ab-17f6-9ecf-e51b3d5326bf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fedd929b-1055-ba78-9e82-a00d98ef0265.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TrussBearingChordTopBottomParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bearing Chord"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TrussBearingChordTopBottomParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TrussBearingChordTopBottomParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TrussBearingChordTopBottomParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fee182d4-5e5e-0b27-58da-5e2ce2b986fb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Viscosity Property

---



|  |
| --- |
| [FluidTemperature Class](e0405486-d484-48cb-716f-5c9ebe6dfcaa.htm)   [See Also](#seeAlsoToggle) |

The dynamic viscosity value

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double Viscosity { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Viscosity As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Viscosity { 	double get (); 	void set (double value); } ``` |

# See Also

[FluidTemperature Class](e0405486-d484-48cb-716f-5c9ebe6dfcaa.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__fee435aa-5e3f-14c6-1566-5c8fd2d63eb8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MetallicPaint Class

---



|  |
| --- |
| [Members](79e7cb65-736a-6548-4a42-5ffbc7b3d692.htm)   [See Also](#seeAlsoToggle) |

A static class that provides access to the property names that appear in the MetallicPaint visual asset schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static class MetallicPaint ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class MetallicPaint ``` |

 

| Visual C++ |
| --- |
| ``` public ref class MetallicPaint abstract sealed ``` |

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB.Visual MetallicPaint

# See Also

[MetallicPaint Members](79e7cb65-736a-6548-4a42-5ffbc7b3d692.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__feeab385-746d-f24c-e480-8c88a7275d01.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetReferences Method

---



|  |
| --- |
| [SelectionChangedEventArgs Class](8a744513-6de0-de55-c44c-bba00b949863.htm)   [See Also](#seeAlsoToggle) |

Returns the references that are currently selected.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public IList<Reference> GetReferences() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetReferences As IList(Of Reference) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Reference^>^ GetReferences() ``` |

#### Return Value

The collection containing the selected references.

# Remarks

The references can be an element or subelement in the host or a linked document.

# See Also

[SelectionChangedEventArgs Class](8a744513-6de0-de55-c44c-bba00b949863.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__fef12e66-7571-43b3-cf9c-c5b903f52eac.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CubicMetersPerHour Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Cubic meters per hour.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CubicMetersPerHour { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CubicMetersPerHour As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CubicMetersPerHour { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fef5982c-3825-eed0-f792-1e0bff5509c2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PolymeshTopology Class

---



|  |
| --- |
| [Members](602fff22-e8dc-e46f-6c92-f997add0ea15.htm)   [See Also](#seeAlsoToggle) |

A class representing topology of a polymesh.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class PolymeshTopology : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PolymeshTopology _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PolymeshTopology : IDisposable ``` |

# Remarks

Topology of a polymesh consists of a number of points and triangular facets formed by the points. Each facet is determined by three indices to the array of points. A polymesh may have UV coordinates assigned, and always has at least one normal associated. There may be more than one normal available for a non-planar polymesh; there may be as many normals as there are either facets or points in the polymesh. The DistributionOfNormals property indicates how normals are distributed along the polymesh.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB PolymeshTopology

# See Also

[PolymeshTopology Members](602fff22-e8dc-e46f-6c92-f997add0ea15.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fef766b5-06f7-fc88-2fe6-695b94f63887.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PanelId Property

---



|  |
| --- |
| [AnalyticalOpening Class](201af27b-c908-83b6-19f2-23d5fa9b69ed.htm)   [See Also](#seeAlsoToggle) |

ElementId of the AnalyticalPanel parent.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public ElementId PanelId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property PanelId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ PanelId { 	ElementId^ get (); } ``` |

# See Also

[AnalyticalOpening Class](201af27b-c908-83b6-19f2-23d5fa9b69ed.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__fef836d9-61bf-4acb-cdeb-7f03d7f23a51.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Set(FieldType) Method (Field, FieldType)

---



|  |
| --- |
| [Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)   [See Also](#seeAlsoToggle) |

Stores the value of the field in the entity.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void Set<FieldType>( 	Field field, 	FieldType value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Set(Of FieldType) ( _ 	field As Field, _ 	value As FieldType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: generic<typename FieldType> void Set( 	Field^ field,  	FieldType value ) ``` |

#### Parameters

field
:   Type:  [Autodesk.Revit.DB.ExtensibleStorage Field](0aeabd09-5c61-0439-e4c7-e1d68d0e1a3b.htm)    
     The field to update.

value
:   Type:   FieldType

# Type Parameters

FieldType
:   The type of the field

# Remarks

The template parameter must match the type of the field (specified when creating the Schema) exactly; this method does not perform data type conversions. The types for containers are IList for arrays and IDictionary for maps.

Note that when string values are specified as map keys, they are case-insensitive.

This method only modifies your copy of the Entity. Store the Entity in an element or another Entity to save the new value. Write access check is not performed on each call to Set. Instead, write access is checked when you try to save the Entity in an Element or another Entity.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The Field belongs to a different Schema from this Entity, or this Entity is invalid. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Requested type does not match the field type. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | For floating-point fields, use the overload taking a ForgeTypeId parameter. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This field's subschema prevents writing. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Invalid floating-point value. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | String is too long; exceeds max length of 16mb characters. |

# See Also

[Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)

[Set Overload](ca7fbcad-94aa-40a0-f77d-1f78c5ecf705.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)

<!-- Start of Syntax__fef8dd39-abf8-f27e-3d32-86667aac8062.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Initialize Method

---



|  |
| --- |
| [ApplicationEntryPoint Class](f18a0fa9-29ba-111e-e1e9-2124ec3c4d2b.htm)   [See Also](#seeAlsoToggle) |

For Revit Macros internal use only.

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Initialize( 	Object obj, 	string addinFolder ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Initialize ( _ 	obj As Object, _ 	addinFolder As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Initialize( 	Object^ obj,  	String^ addinFolder ) sealed ``` |

#### Parameters

obj
:   Type:  [System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)

addinFolder
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

#### Implements

 [IEntryPoint Initialize(Object, String)](7619b903-34aa-32d1-38d9-f7e826828a5f.htm)

# See Also

[ApplicationEntryPoint Class](f18a0fa9-29ba-111e-e1e9-2124ec3c4d2b.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)

<!-- Start of Syntax__fef969d9-4a6a-5aeb-d492-79eee88f9db5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsIntersectorValidForCreation Method

---



|  |
| --- |
| [DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)   [See Also](#seeAlsoToggle) |

This returns true if the intersector is an element that can be used to intersect with a newly created divided path.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool IsIntersectorValidForCreation( 	Document document, 	ElementId intersector ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsIntersectorValidForCreation ( _ 	document As Document, _ 	intersector As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsIntersectorValidForCreation( 	Document^ document,  	ElementId^ intersector ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

intersector
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The intersector.

#### Return Value

True if the reference can be used to create a divided path, false otherwise.

# Remarks

Intersectors can be curve elements, datum planes, or divided paths. This function is should not be used to validate the input to SetIntersectors() because it does not check for self intersection of any other circular dependencies between intersectors. Use isIntersectorValidForDividedPath() instead.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fefb2ddb-ebee-a9d5-327d-dc27be440ed4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarManyLoopsError Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Rebar Sketch contains more than one loop. Can't create Rebar.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RebarManyLoopsError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarManyLoopsError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RebarManyLoopsError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__feff1b91-2f53-22b4-b3d9-5af68a966e8c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WoodLatewoodRatio Property

---



|  |
| --- |
| [AdvancedWood Class](1e8c37ad-69ea-aabc-df91-eda9c7fe54ff.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Percentage of latewood in each ring" from the "AdvancedWood" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string WoodLatewoodRatio { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WoodLatewoodRatio As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ WoodLatewoodRatio { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble".

# See Also

[AdvancedWood Class](1e8c37ad-69ea-aabc-df91-eda9c7fe54ff.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__ff003973-2633-dcdd-7bfe-81ef1e30bd3d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InvalidLocationLineJustificationFailure Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Modify the location justification to a invalid value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId InvalidLocationLineJustificationFailure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InvalidLocationLineJustificationFailure As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ InvalidLocationLineJustificationFailure { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff007b27-8690-1fae-8dbb-2f3ecc6d6149.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsRailingShape Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Rail Shape"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsRailingShape { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsRailingShape As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsRailingShape { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff0bae6e-c1b8-7b7a-cbc9-3b419b7b0c48.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentSynchronizedWithCentralEventArgs Class

---



|  |
| --- |
| [Members](36bfd237-9247-5101-e506-2fb67ddfd108.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by the DocumentSynchronizedWithCentralEventArgs event.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public class DocumentSynchronizedWithCentralEventArgs : RevitAPIPostDocEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DocumentSynchronizedWithCentralEventArgs _ 	Inherits RevitAPIPostDocEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DocumentSynchronizedWithCentralEventArgs : public RevitAPIPostDocEventArgs ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPostEventArgs](93554f52-0145-3454-5697-3f1015e46434.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPostDocEventArgs](7d3fba7a-5efb-6a4c-a49c-16c25f972830.htm)    
  Autodesk.Revit.DB.Events DocumentSynchronizedWithCentralEventArgs

# See Also

[DocumentSynchronizedWithCentralEventArgs Members](36bfd237-9247-5101-e506-2fb67ddfd108.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__ff0d0620-f703-e369-a272-8763272abeaa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarStandardHookBendDiameter Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Standard Hook Bend Diameter"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarStandardHookBendDiameter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarStandardHookBendDiameter As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarStandardHookBendDiameter { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff11b964-e6e7-9dad-fbf1-461244fcf010.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidType Method

---



|  |
| --- |
| [AlignmentStationLabel Class](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.htm)   [See Also](#seeAlsoToggle) |

Checks if the type is a valid alignment station label type.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public static bool IsValidType( 	Element type ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidType ( _ 	type As Element _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidType( 	Element^ type ) ``` |

#### Parameters

type
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element type to validate.

# Remarks

Can be used for finding or types to be set to  [TypeId](86352cb2-b367-a806-7427-2fb08e50b425.htm)  when creating alignment label sets with  [Create(Alignment, View, AlignmentStationLabelOptions)](eb69d2d4-5a55-6402-ae7b-d1049fdba2d4.htm)  ; or types to be set to  [TypeId](5b0dfa5d-bc2f-b097-a8d6-c5e78c569add.htm)  when creating alignment labels with  [CreateSet(Alignment, View, AlignmentStationLabelSetOptions)](bbb3fb20-cbc6-f6aa-cc23-ae7ad73747b3.htm)  .

# See Also

[AlignmentStationLabel Class](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)

<!-- Start of Syntax__ff11f9f7-dd13-7b1b-a7ee-0d1703f7cc75.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HemisphericalLightDistribution Class

---



|  |
| --- |
| [Members](333d6c27-0a83-eebe-360b-a0995278a572.htm)   [See Also](#seeAlsoToggle) |

This class encapsulates a hemispherical light distribution.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class HemisphericalLightDistribution : LightDistribution ``` |

 

| Visual Basic |
| --- |
| ``` Public Class HemisphericalLightDistribution _ 	Inherits LightDistribution ``` |

 

| Visual C++ |
| --- |
| ``` public ref class HemisphericalLightDistribution : public LightDistribution ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB.Lighting LightDistribution](39162cb5-d13b-c7fa-9297-9a70c5678ac6.htm)    
  Autodesk.Revit.DB.Lighting HemisphericalLightDistribution

# See Also

[HemisphericalLightDistribution Members](333d6c27-0a83-eebe-360b-a0995278a572.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__ff14f10a-fc72-f74e-41cb-048d15a69433.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ServiceType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

This enumeration is used for specifying the most predominant service for the building or space.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public enum ServiceType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ServiceType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ServiceType ``` |

# Members

| Member name | Description |
| --- | --- |
| kNoServiceType | Service Type is NoServiceType. |
| kCentralHeatingRadiators | Service Type is CentralHeatingRadiators. |
| kCentralHeatingConvectors | Service Type is CentralHeatingConvectors. |
| kCentralHeatingRadiantFloor | Service Type is CentralHeatingRadiantFloor. |
| kCentralHeatingHotAir | Service Type is CentralHeatingHotAir. |
| kOtherRoomHeater | Service Type is OtherRoomHeater. |
| kRadiantHeaterFlue | Service Type is RadiantHeaterFlue. |
| kRadiantHeaterNoFlue | Service Type is RadiantHeaterNoFlue. |
| kRadiantHeaterMultiburner | Service Type is RadiantHeaterMultiburner. |
| kForcedConvectionHeaterFlue | Service Type is ForcedConvectionHeaterFlue. |
| kForcedConvectionHeaterNoFlue | Service Type is ForcedConvectionHeaterNoFlue. |
| kVAVSingleDuct | Service Type is VAVSingleDuct. |
| kVAVDualDuct | Service Type is VAVDualDuct. |
| kVAVIndoorPackagedCabinet | Service Type is VAVIndoorPackagedCabinet. |
| kVAVTerminalReheat | Service Type is VAVTerminalReheat. |
| kFanCoilSystem | Service Type is FanCoilSystem. |
| kInductionSystem | Service Type is InductionSystem. |
| kConstantVolumeFixedOA | Service Type is ConstantVolumeFixedOA. |
| kConstantVolumeVariableOA | Service Type is ConstantVolumeVariableOA. |
| kConstantVolumeTerminalReheat | Service Type is ConstantVolumeTerminalReheat. |
| kMultizoneHotDeckColdDeck | Service Type is MultizoneHotDeckColdDeck. |
| kConstantVolumeDualDuct | Service Type is ConstantVolumeDualDuct. |
| kRadiantCooledCeilings | Service Type is RadiantCooledCeilings. |
| kActiveChilledBeams | Service Type is ActiveChilledBeams. |
| kWaterLoopHeatPump | Service Type is WaterLoopHeatPump. |
| kVariableRefrigerantFlow | Service Type is VariableRefrigerantFlow. |
| kSplitSystemsWithNaturalVentilation | Service Type is SplitSystemsWithNaturalVentilation. |
| kSplitSystemsWithMechanicalVentilation | Service Type is SplitSystemsWithMechanicalVentilation. |
| kSplitSystemsWithMechanicalVentilationWithCooling | Service Type is SplitSystemsWithMechanicalVentilationWithCooling. |

# Remarks

This enumerated list corresponds to the serviceType attribute in the gbXML (Green Building XML) schema and is primarily used for energy analysis.

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff1d8443-8329-cab4-6d4d-119bbe0b6e41.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AsInteger Method

---



|  |
| --- |
| [IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.htm)   [See Also](#seeAlsoToggle) |

Gets storage value as integer when its PrimitiveType is integer.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public int AsInteger() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AsInteger As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int AsInteger() ``` |

#### Return Value

The int value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | The primitive type is not integer. |

# See Also

[IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__ff212171-e964-2045-42f8-1519762cff43.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetHookPlaneNormalForBarIdx Method

---



|  |
| --- |
| [RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.htm)   [See Also](#seeAlsoToggle) |

Returns the normal of plane in which the hook at end of bar with index barPositionIndex that is currently in Rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public XYZ GetHookPlaneNormalForBarIdx( 	int end, 	int barPositionIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetHookPlaneNormalForBarIdx ( _ 	end As Integer, _ 	barPositionIndex As Integer _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetHookPlaneNormalForBarIdx( 	int end,  	int barPositionIndex ) ``` |

#### Parameters

end
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The end of bar. Should be 0 for start or 1 for end.

barPositionIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     An index between 0 and (GetNumberOfBars()-1).

#### Return Value

The normal of plane in which the hook at end of bar with index barPositionIndex that is currently in Rebar.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex is not in the range [ 0, GetNumberOfBars()-1 ]. -or- Invalid end. |

# See Also

[RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__ff21648e-5c98-1266-a2fa-94344fcc75b6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InvalidClosedLoopsForFaceSplit Property

---



|  |
| --- |
| [BuiltInFailures FaceSplitterFailures Class](c354be2c-4d56-3ed0-6977-3c5cf6972cdf.htm)   [See Also](#seeAlsoToggle) |

The closed loop used to split the face must lie completely within the face and cannot intersect or overlap any of the face's edges. To split a face at its border, use an open loop that ends on the boundary of the face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId InvalidClosedLoopsForFaceSplit { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InvalidClosedLoopsForFaceSplit As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ InvalidClosedLoopsForFaceSplit { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FaceSplitterFailures Class](c354be2c-4d56-3ed0-6977-3c5cf6972cdf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff23277a-3bb1-253d-e158-983b23aaf04a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FindAssociatedPlanViewId Method

---



|  |
| --- |
| [Level Class](577e5d4e-a558-118c-9dea-3b810b061775.htm)   [See Also](#seeAlsoToggle) |

Finds the id of the first available associated floor or structural plan view associated with this level.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public ElementId FindAssociatedPlanViewId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function FindAssociatedPlanViewId As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ FindAssociatedPlanViewId() ``` |

# Remarks

The view id returned is determined by the same rules associated with the Revit tool "Go to Floor Plan". Many levels may actually have more than one associated floor plan id and this routine will only return the first one found. If no associated view is found, InvalidElementId is returned.

# See Also

[Level Class](577e5d4e-a558-118c-9dea-3b810b061775.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff240d42-e18e-d25d-6cf6-7c5e57d9eea8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MillimetersOfMercury Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Millimeters of mercury.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MillimetersOfMercury { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MillimetersOfMercury As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MillimetersOfMercury { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff260f54-ac26-ace8-913d-aa3e00545cce.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### KilogramsPerSecond Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Kilograms per second.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId KilogramsPerSecond { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property KilogramsPerSecond As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ KilogramsPerSecond { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff2ab239-404a-00de-1acd-0a9b38ed486c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsFpSprinklerPressureClassParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Pressure Class"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsFpSprinklerPressureClassParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsFpSprinklerPressureClassParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsFpSprinklerPressureClassParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff2c3e9a-9735-ad10-3aef-426049aa8d27.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [IndexPrimitive Class](b9718ac0-7194-1944-ce7f-a5c618f20ced.htm)   [See Also](#seeAlsoToggle) |

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

[IndexPrimitive Class](b9718ac0-7194-1944-ce7f-a5c618f20ced.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__ff2cf48e-9017-c8ad-c217-9466bfd34e22.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DoesBarExistAtPosition Method

---



|  |
| --- |
| [RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)   [See Also](#seeAlsoToggle) |

Checks whether a bar exists at the specified position.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool DoesBarExistAtPosition( 	int barPosition ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function DoesBarExistAtPosition ( _ 	barPosition As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool DoesBarExistAtPosition( 	int barPosition ) ``` |

#### Parameters

barPosition
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     A bar position index between 0 and NumberOfBarPositions-1.

# Remarks

Returns true, unless the bar position is the first or last in the set and it is suppressed by IncludeFirstBar or IncludeLastBar.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPosition is not in the range [ 0, NumberOfBarPositions-1 ]. |

# See Also

[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__ff2d6432-d624-692e-eb82-dcc98801b3b6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlignmentStationLabelOptions Constructor

---



|  |
| --- |
| [AlignmentStationLabelOptions Class](65682466-07b4-766b-a215-fefcdcfd32ce.htm)   [See Also](#seeAlsoToggle) |

Creates an object with default values.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public AlignmentStationLabelOptions( 	double station ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	station As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: AlignmentStationLabelOptions( 	double station ) ``` |

#### Parameters

station
:   Type:  System Double    
     The station at which the label will be placed.

# See Also

[AlignmentStationLabelOptions Class](65682466-07b4-766b-a215-fefcdcfd32ce.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)

<!-- Start of Syntax__ff300336-bb07-bcc7-0001-c6975783fd52.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarSystemNumberOfLinesTopDir2Generic Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top/Exterior Minor Number Of Lines"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarSystemNumberOfLinesTopDir2Generic { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarSystemNumberOfLinesTopDir2Generic As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarSystemNumberOfLinesTopDir2Generic { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff32938a-b156-4a6e-c7a1-93c100c18612.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Enabled Property

---



|  |
| --- |
| [RibbonPanel Class](544c0af7-6124-4f64-a25d-46e81ac5300f.htm)   [See Also](#seeAlsoToggle) |

Gets or sets a value indicating whether the RibbonPanel can respond to user interaction.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool Enabled { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Enabled As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool Enabled { 	bool get (); 	void set (bool value); } ``` |

#### Field Value

True if the panel allows interaction, false if the panel disallows interaction with all the controls it contains.

# See Also

[RibbonPanel Class](544c0af7-6124-4f64-a25d-46e81ac5300f.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__ff3308db-ae11-d118-5f1e-40e4fdbee72d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasElevationProfile Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Identifies if the wall has a sketched elevation profile.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool HasElevationProfile( 	Wall pVWall ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function HasElevationProfile ( _ 	pVWall As Wall _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool HasElevationProfile( 	Wall^ pVWall ) ``` |

#### Parameters

pVWall
:   Type:  [Autodesk.Revit.DB Wall](b5891733-c602-12df-beab-da414b58d608.htm)    
     The wall.

#### Return Value

True if the wall has a sketch elevation profile, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__ff3595ab-d330-d7e5-8e37-2fb5696e463d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HvacEnergy Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Energy, in discipline Energy.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId HvacEnergy { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property HvacEnergy As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ HvacEnergy { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff38ac8e-6b3b-f9a4-6a26-2669eb661361.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [ViewCropRegionShapeManager Class](2610cb66-5dae-9fc8-4e83-7dfe88085abb.htm)   [See Also](#seeAlsoToggle) |

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

[ViewCropRegionShapeManager Class](2610cb66-5dae-9fc8-4e83-7dfe88085abb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff3b0b97-9b83-e9c2-b5d2-de89b037f329.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureLinkTextureTransforms Property

---



|  |
| --- |
| [Wave Class](9c0cc26f-f6ae-708e-5612-d3d181058174.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Link Transforms" from the "Wave" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TextureLinkTextureTransforms { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextureLinkTextureTransforms As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TextureLinkTextureTransforms { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyBoolean".

# See Also

[Wave Class](9c0cc26f-f6ae-708e-5612-d3d181058174.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__ff3b9be3-836a-84a4-4be9-f098522ff249.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarSystemActiveBackDirn1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Interior Major Direction"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarSystemActiveBackDirn1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarSystemActiveBackDirn1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarSystemActiveBackDirn1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff3ccaf1-c076-9887-9695-43ea562c80f6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DecimalSheetLength Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Decimal Sheet Length, in discipline Common.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DecimalSheetLength { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DecimalSheetLength As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DecimalSheetLength { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff42e969-2daf-d436-2ded-860e87195823.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ActiveAddInId Property

---



|  |
| --- |
| [UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)   [See Also](#seeAlsoToggle) |

Get current active external application or external command id.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public AddInId ActiveAddInId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ActiveAddInId As AddInId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property AddInId^ ActiveAddInId { 	AddInId^ get (); } ``` |

# See Also

[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__ff436771-414c-1144-5474-d5674789cd1c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [IFCTransformSetter Class](75b9525d-3b8d-70d8-55de-a193b9eb5e76.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
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

[IFCTransformSetter Class](75b9525d-3b8d-70d8-55de-a193b9eb5e76.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__ff4993ad-2237-2c11-dc9c-96e7644379a4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationOffsetParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Middle Elevation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FabricationOffsetParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationOffsetParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FabricationOffsetParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff4ecb34-6fef-402a-5cee-c7937974b8d2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Checker Class

---



|  |
| --- |
| [Members](a3cdc3db-11be-b749-cfeb-94576788e4b5.htm)   [See Also](#seeAlsoToggle) |

A static class that provides access to the property names that appear in the Checker visual asset schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static class Checker ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class Checker ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Checker abstract sealed ``` |

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB.Visual Checker

# See Also

[Checker Members](a3cdc3db-11be-b749-cfeb-94576788e4b5.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__ff52a707-e3cc-4b90-d15b-d9db4f52766a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsFromLocalPath Method

---



|  |
| --- |
| [RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)   [See Also](#seeAlsoToggle) |

Checks whether the Revit link uses a local path, such as a hard drive.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool IsFromLocalPath() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsFromLocalPath As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsFromLocalPath() ``` |

#### Return Value

Returns true if the Revit link is from a local drive.

# See Also

[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff54a457-f002-46a3-ad50-b2d1f753559d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralDisplayInHiddenViewsColumn Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Display in Hidden Views"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralDisplayInHiddenViewsColumn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralDisplayInHiddenViewsColumn As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralDisplayInHiddenViewsColumn { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff5b61d4-e802-9e9b-c8b7-e84d53eb3faa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TemperatureRatings Property

---



|  |
| --- |
| [WireMaterialType Class](3d05ec79-0289-c6d1-2a13-7e6b07241afd.htm)   [See Also](#seeAlsoToggle) |

Get all temperature rating type definitions defined in this wire material type.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public TemperatureRatingTypeSet TemperatureRatings { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property TemperatureRatings As TemperatureRatingTypeSet 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property TemperatureRatingTypeSet^ TemperatureRatings { 	TemperatureRatingTypeSet^ get (); } ``` |

# See Also

[WireMaterialType Class](3d05ec79-0289-c6d1-2a13-7e6b07241afd.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__ff5e52b2-b09c-c15d-edbd-988b3f41a6f8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ContainsKey Method

---



|  |
| --- |
| [ExportLinetypeTable Class](136c6197-2f4c-5686-e70c-09cee48b71ad.htm)   [See Also](#seeAlsoToggle) |

Checks whether a pattern key exists in the table.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool ContainsKey( 	ExportLinetypeKey exportLinetypeKey ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ContainsKey ( _ 	exportLinetypeKey As ExportLinetypeKey _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool ContainsKey( 	ExportLinetypeKey^ exportLinetypeKey ) ``` |

#### Parameters

exportLinetypeKey
:   Type:  [Autodesk.Revit.DB ExportLinetypeKey](7f67a1c8-cc9b-9b17-aa87-664657ee9d7d.htm)    
     The export line type key.

#### Return Value

True if the line type exists in the table.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportLinetypeTable Class](136c6197-2f4c-5686-e70c-09cee48b71ad.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff608354-dee5-99f7-fca3-d8b20ff5733d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpaceSet Class

---



|  |
| --- |
| [Members](405e4623-e4a0-d83c-a529-73f00750ec8a.htm)   [See Also](#seeAlsoToggle) |

A set that can contain any type of object.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class SpaceSet : APIObject, IEnumerable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class SpaceSet _ 	Inherits APIObject _ 	Implements IEnumerable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SpaceSet : public APIObject,  	IEnumerable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB.Mechanical SpaceSet

# See Also

[SpaceSet Members](405e4623-e4a0-d83c-a529-73f00750ec8a.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__ff63e780-3232-1413-8a87-d451a7292503.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionGeneralH Constructor

---



|  |
| --- |
| [StructuralSectionGeneralH Class](512d0768-c2d3-f601-fd3e-c1db53d68f27.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of Rectangular Pipe shape.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public StructuralSectionGeneralH( 	double width, 	double height, 	double wallNominalThickness, 	double wallDesignThickness, 	double innerFillet, 	double outerFillet, 	double centroidHorizontal, 	double centroidVertical, 	StructuralSectionAnalysisParams analysisParams ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	width As Double, _ 	height As Double, _ 	wallNominalThickness As Double, _ 	wallDesignThickness As Double, _ 	innerFillet As Double, _ 	outerFillet As Double, _ 	centroidHorizontal As Double, _ 	centroidVertical As Double, _ 	analysisParams As StructuralSectionAnalysisParams _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: StructuralSectionGeneralH( 	double width,  	double height,  	double wallNominalThickness,  	double wallDesignThickness,  	double innerFillet,  	double outerFillet,  	double centroidHorizontal,  	double centroidVertical,  	StructuralSectionAnalysisParams^ analysisParams ) ``` |

#### Parameters

width
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Section width.

height
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Section height, depth.

wallNominalThickness
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Represents wall nominal thickness of rectangle.

wallDesignThickness
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Represents wall design thickness of rectangle.

innerFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Inner Fillet - Corner fillet inner radius.

outerFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Outer Fillet - Corner fillet outer radius.

centroidHorizontal
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Distance from centroid to the left extremites along horizontal axis.

centroidVertical
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Distance from centroid to the upper extremites along vertical axis.

analysisParams
:   Type:  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionAnalysisParams](e5bd2059-9102-0c1c-e9d4-16a015a4cb5e.htm)    
     Common set of parameters for structural analysis.

# See Also

[StructuralSectionGeneralH Class](512d0768-c2d3-f601-fd3e-c1db53d68f27.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__ff64717a-fa49-d828-7daa-941986971a61.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FindByName Method

---



|  |
| --- |
| [AssetProperties Class](45955e9d-7dd4-b06c-f71a-f9ae2cc1c34a.htm)   [See Also](#seeAlsoToggle) |

Gets the property with the given name.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public AssetProperty FindByName( 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function FindByName ( _ 	name As String _ ) As AssetProperty ``` |

 

| Visual C++ |
| --- |
| ``` public: AssetProperty^ FindByName( 	String^ name ) ``` |

#### Parameters

name
:   Type:  System String    
     Name of the property.

#### Return Value

The property with the specified name.

# Remarks

FindByName will not visit the properties of any connected asset on any of the properties.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AssetProperties Class](45955e9d-7dd4-b06c-f71a-f9ae2cc1c34a.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__ff65e8c4-89a6-99f7-2518-ecb5cc2d063b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [SpaceSet Class](ff608354-dee5-99f7-fca3-d8b20ff5733d.htm)   [See Also](#seeAlsoToggle) |

Removes every item from the set, rendering it empty.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual void Clear() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Sub Clear ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Clear() ``` |

# See Also

[SpaceSet Class](ff608354-dee5-99f7-fca3-d8b20ff5733d.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__ff689646-266a-a62f-a044-8849697122c7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DefinitionGroups Class

---



|  |
| --- |
| [Members](2ac8205a-3478-33f7-4618-3162a2281850.htm)   [See Also](#seeAlsoToggle) |

A specialized set of definition groups that allows creation of new groups.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class DefinitionGroups : IEnumerable<DefinitionGroup>,  	IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DefinitionGroups _ 	Implements IEnumerable(Of DefinitionGroup), IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DefinitionGroups : IEnumerable<DefinitionGroup^>,  	IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB DefinitionGroups

# See Also

[DefinitionGroups Members](2ac8205a-3478-33f7-4618-3162a2281850.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff69bcfe-2531-e9dd-279d-e1095c035e19.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ParameterMap Class

---



|  |
| --- |
| [Members](94bdbe04-9006-67c4-24b1-c1abc48ec562.htm)   [See Also](#seeAlsoToggle) |

A map that can contain a mapping of a parameter name (a String) to a parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class ParameterMap : APIObject,  	IEnumerable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ParameterMap _ 	Inherits APIObject _ 	Implements IEnumerable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ParameterMap : public APIObject,  	IEnumerable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB ParameterMap

# See Also

[ParameterMap Members](94bdbe04-9006-67c4-24b1-c1abc48ec562.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff6d35ee-db72-544c-033c-c8372842ebd0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveParameterDownOrder Method

---



|  |
| --- |
| [GlobalParametersManager Class](f3af05ec-1f0c-fe86-6708-0a211a40bcda.htm)   [See Also](#seeAlsoToggle) |

Moves given paramerer Down in the current order.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static bool MoveParameterDownOrder( 	Document document, 	ElementId parameterId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function MoveParameterDownOrder ( _ 	document As Document, _ 	parameterId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool MoveParameterDownOrder( 	Document^ document,  	ElementId^ parameterId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document containing the give global parameter

parameterId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The parameter to move Down

#### Return Value

Indicates whether the parameter could be moved Down in order or not.

# Remarks

A parameter can only be moved within its parameter group, meaning that repeated moving a parameter will not push the parameter out of and into the next (in order) parameter group. When a parameter can no longer move because it is at the boundary of its group, this method returns False.

This operation has no effect on the global parameters themselves. The rearranged order is only visible in the standard Global Parameters dialog. However, the order of parameters is serialized in the document, thus available on the DB level as well.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Global parameters are not supported in the given document. A possible cause is that it is not a project document, for global parameters are not supported in Revit families. -or- The input parameterId is not of a valid global parameter of the given document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[GlobalParametersManager Class](f3af05ec-1f0c-fe86-6708-0a211a40bcda.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff6df064-7a74-9f4c-1185-37ee54f9ac96.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PipeSize Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Pipe Size, in discipline Piping.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PipeSize { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PipeSize As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PipeSize { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff709bd7-493e-62e9-0ee8-67b161a2c497.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [WireMaterialTypeSetIterator Class](222339c6-d45c-ca08-433e-fe327b17ac47.htm)   [See Also](#seeAlsoToggle) |

Retrieves the item that is the current focus of the iterator.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
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

[WireMaterialTypeSetIterator Class](222339c6-d45c-ca08-433e-fe327b17ac47.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__ff71e3b0-4300-7d04-1356-a045b9a90407.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NestedFamilyTypeReference Class

---



|  |
| --- |
| [Members](0a7567d8-da0d-ed80-6b55-317a2353e097.htm)   [See Also](#seeAlsoToggle) |

A proxy element representing a nested family type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public class NestedFamilyTypeReference : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class NestedFamilyTypeReference _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class NestedFamilyTypeReference : public Element ``` |

# Remarks

This element represents a value of a FamilyType Parameter of a Loaded Family. Each such element corresponds to a nested FamilyType Element in the original Family Document where the family was defined.

This element stores only basic information about the nested FamilyType, such as the name of the Type, name of the Family, and a Category.

These elements are very low-level and thus bypassed by standard element filters. However, it is possible to obtain a set of applicable elements of this class for a FamilyType parameter of a family by calling  [!:Autodesk::Revit::DB::Family::GetFamilyTypeParameterValues]

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB NestedFamilyTypeReference

# See Also

[NestedFamilyTypeReference Members](0a7567d8-da0d-ed80-6b55-317a2353e097.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff73932a-dae4-37b3-5b4d-584e4bb95e2a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetProjectPosition Method

---



|  |
| --- |
| [ProjectLocation Class](1249d5fa-74f3-cf64-0a63-7ab370b67a5c.htm)   [See Also](#seeAlsoToggle) |

Sets the coordinates of a point in the ProjectLocation's coordinate system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetProjectPosition( 	XYZ point, 	ProjectPosition position ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetProjectPosition ( _ 	point As XYZ, _ 	position As ProjectPosition _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetProjectPosition( 	XYZ^ point,  	ProjectPosition^ position ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

position
:   Type:  [Autodesk.Revit.DB ProjectPosition](249111cc-c1f3-d3e1-e7bf-dc791327fd4c.htm)

# Remarks

When setting this value, the transformations applied to the location are modified such that the passed point becomes the specified North/South, East/West and Elevation, and the coordinate transform will have the designated angular rotation. This is similar to the Revit command "Specify Coordinates at Point".

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Unable to use the project position's transform to calculate the point. |

# See Also

[ProjectLocation Class](1249d5fa-74f3-cf64-0a63-7ab370b67a5c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff7695bc-b1b1-6cfd-bb74-9cf4ece27f18.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnhideElements Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Sets the elements to be shown in the given view if they are currently hidden.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void UnhideElements( 	ICollection<ElementId> elementIdSet ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub UnhideElements ( _ 	elementIdSet As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void UnhideElements( 	ICollection<ElementId^>^ elementIdSet ) ``` |

#### Parameters

elementIdSet
:   Type:  [System.Collections.Generic ICollection](http://msdn2.microsoft.com/en-us/library/92t2ye13)   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A set of ElementIds to be unhidden.

# Remarks

This change is permanent until the elements are hidden again. All elements in the set must be currently hidden. An application can check this with  [IsHidden(View)](2c3d4123-fded-cd5f-ed0d-12b1e1a3ce42.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when argument is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the set of elements to be unhidden is empty or one of the elements can not be unhidden. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when document regeneration failed. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff77a238-9c2d-2651-8c01-f81a15ab74de.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RailCurveTooShort Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Curve in rail sketch is too short for rail creation and ignored.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RailCurveTooShort { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RailCurveTooShort As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RailCurveTooShort { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImageInstance Class

---



|  |
| --- |
| [Members](6a4190ff-3aa4-21c6-e91f-5a829fbb65c0.htm)   [See Also](#seeAlsoToggle) |

An element that represents an instance of an image placed in a view

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public class ImageInstance : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ImageInstance _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ImageInstance : public Element ``` |

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB ImageInstance

# See Also

[ImageInstance Members](6a4190ff-3aa4-21c6-e91f-5a829fbb65c0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff7c884c-5301-1641-8f11-45264b536cd3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetAttribute Method (String, IList(String))

---



|  |
| --- |
| [IFCAnyHandle Class](8b893943-70fa-94bf-90be-1523d516ecb3.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetAttribute( 	string name, 	IList<string> values ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetAttribute ( _ 	name As String, _ 	values As IList(Of String) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetAttribute( 	String^ name,  	IList<String^>^ values ) ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

values
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

# See Also

[IFCAnyHandle Class](8b893943-70fa-94bf-90be-1523d516ecb3.htm)

[SetAttribute Overload](25c11a79-8e0f-5474-cbf5-6a3e7a2821d2.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__ff7dace3-8a34-3760-042d-21d1da8733f1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PickSupport Method

---



|  |
| --- |
| [SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)   [See Also](#seeAlsoToggle) |

Picks an element to support the slab. This method will define split lines and create constant bearing lines for the slab.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void PickSupport( 	Line gLine ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub PickSupport ( _ 	gLine As Line _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void PickSupport( 	Line^ gLine ) ``` |

#### Parameters

gLine
:   Type:  [Autodesk.Revit.DB Line](e7329450-434a-918b-661c-65e15e0585a5.htm)    
     A line from a support element such as a beam.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input line is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the input line is invalid. |

# See Also

[SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff7e6316-2b9a-ba7b-0895-5d0a47a29349.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralFoundationLength Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Length"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralFoundationLength { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralFoundationLength As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralFoundationLength { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff803f5c-3458-451e-d0b6-0819e6b6da09.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TilePerColumn Property

---



|  |
| --- |
| [Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Every" from the "Tile" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TilePerColumn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TilePerColumn As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TilePerColumn { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyInteger" within the range of "0, 50".

# See Also

[Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__ff842cc8-67a9-2c51-843d-d17767e757a8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FormulaEditing Event

---



|  |
| --- |
| [UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the FormulaEditing event to be notified when the edit formula button has been clicked.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public event EventHandler<FormulaEditingEventArgs> FormulaEditing ``` |

 

| Visual Basic |
| --- |
| ``` Public Event FormulaEditing As EventHandler(Of FormulaEditingEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<FormulaEditingEventArgs^>^ FormulaEditing { 	void add (EventHandler<FormulaEditingEventArgs^>^ value); 	void remove (EventHandler<FormulaEditingEventArgs^>^ value); } ``` |

# See Also

[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__ff847aea-8397-8b79-b039-16a72e479c9f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarUpdateCurvesData Class

---



|  |
| --- |
| [Members](fd45bd17-d74d-7d84-435b-dbccfe226f86.htm)   [See Also](#seeAlsoToggle) |

Class holding the information needed to calculate the rebar curves.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public class RebarUpdateCurvesData : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RebarUpdateCurvesData _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RebarUpdateCurvesData : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Structure RebarUpdateCurvesData

# See Also

[RebarUpdateCurvesData Members](fd45bd17-d74d-7d84-435b-dbccfe226f86.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__ff8a86a4-620e-1077-426b-540bd27027e6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InputFormat Property

---



|  |
| --- |
| [ShapeImporter Class](d6120e08-f260-577d-b6cf-3fe5b042a54e.htm)   [See Also](#seeAlsoToggle) |

The format of the incoming data.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public ShapeImporterSourceFormat InputFormat { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property InputFormat As ShapeImporterSourceFormat 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ShapeImporterSourceFormat InputFormat { 	ShapeImporterSourceFormat get (); 	void set (ShapeImporterSourceFormat value); } ``` |

# Remarks

If this option is set to Auto (the default), the file name extension will be used to determine the input format. That covers most file-based data import workflows. Specify the input format explicitly to perform an additional sanity check or if you are using a non-standard file extension.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ShapeImporter Class](d6120e08-f260-577d-b6cf-3fe5b042a54e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff8bf7b0-c88b-16d3-da58-d67f90df4e27.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DimLeaderType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Leader Type"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DimLeaderType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DimLeaderType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DimLeaderType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff8ea573-fdb2-acdc-b718-3e5c9116a0ba.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EdgeArray Constructor

---



|  |
| --- |
| [EdgeArray Class](7069d0a1-fc52-a347-e0d8-6de1f40797d3.htm)   [See Also](#seeAlsoToggle) |

Initializes a new instance of the  [EdgeArray](7069d0a1-fc52-a347-e0d8-6de1f40797d3.htm)  class

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public EdgeArray() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: EdgeArray() ``` |

# See Also

[EdgeArray Class](7069d0a1-fc52-a347-e0d8-6de1f40797d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff8f9e7f-cc92-fe92-6ea4-9f1b581f2bac.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PickElementsByRectangle Method (String)

---



|  |
| --- |
| [Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Prompts the user to select multiple elements by drawing a rectangle while showing a custom status prompt string.

**Namespace:**   [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IList<Element> PickElementsByRectangle( 	string statusPrompt ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function PickElementsByRectangle ( _ 	statusPrompt As String _ ) As IList(Of Element) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Element^>^ PickElementsByRectangle( 	String^ statusPrompt ) ``` |

#### Parameters

statusPrompt
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The message shown on the status bar.

#### Return Value

A collection of elements selected by the user.

Note: if the user cancels the operation (for example, through ESC), the method will throw an OperationCanceledException instance.

# Remarks

Revit users will be permitted to manipulate the Revit view (zooming, panning, and rotating the view), but will not be permitted to click other items in the Revit user interface. Users are not permitted to switch the active view, close the active document or Revit application in the pick session, otherwise an exception will be thrown.

The selection will not be automatically added to the active selection buffer.

Note: this method must not be called during dynamic update, otherwise ForbiddenForDynamicUpdateException will be thrown.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Use the rectangle picking tool to identify model elements to select.
IList<Element> pickedElements = uidoc.Selection.PickElementsByRectangle("Select by rectangle");
if (pickedElements.Count > 0)
{ 
    // Collect Ids of all picked elements
    IList<ElementId> idsToSelect = new List<ElementId>(pickedElements.Count);
    foreach (Element element in pickedElements)
    {
        idsToSelect.Add(element.Id);
    }

    // Update the current selection
    uidoc.Selection.SetElementIds(idsToSelect);
    TaskDialog.Show("Revit", string.Format("{0} elements added to Selection.", idsToSelect.Count));
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Use the rectangle picking tool to identify model elements to select.
Dim pickedElements As IList(Of Element) = uidoc.Selection.PickElementsByRectangle("Select by rectangle")
If pickedElements.Count > 0 Then
    ' Collect Ids of all picked elements
    Dim idsToSelect As IList(Of ElementId) = New List(Of ElementId)(pickedElements.Count)
    For Each element As Element In pickedElements
        idsToSelect.Add(element.Id)
    Next

    ' Update the current selection
    uidoc.Selection.SetElementIds(idsToSelect)
    TaskDialog.Show("Revit", String.Format("{0} elements added to Selection.", idsToSelect.Count))
End If
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the statusPrompt is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | Thrown when the Revit user cancelled this operation. Thrown when the Revit user tried to switch the active view, close the active document or Revit application when responding to this mode. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | Thrown if this method is called during dynamic update. |

# See Also

[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)

[PickElementsByRectangle Overload](b486efdd-0c0d-589f-2dfd-b16d32dca046.htm)

[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.htm)

<!-- Start of Syntax__ff8feaaf-4938-089b-1f10-abbcb757550b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DesignSupplyAirflow Property

---



|  |
| --- |
| [Space Class](b2c8970e-e554-8d73-06db-b65712c8a2e5.htm)   [See Also](#seeAlsoToggle) |

Get or set the Specified Supply Airflow of the Space.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double DesignSupplyAirflow { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DesignSupplyAirflow As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double DesignSupplyAirflow { 	double get (); 	void set (double value); } ``` |

# Remarks

This property is used to get or set the Specified Supply Airflow (Unit: CFM) of the Space.

# See Also

[Space Class](b2c8970e-e554-8d73-06db-b65712c8a2e5.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__ff978c6c-52dd-9d12-dea4-fb01f8e76fc8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalMemberInstability Property

---



|  |
| --- |
| [BuiltInFailures AnalyticalModelFailures Class](3633d562-0e24-5cad-ec0f-02e6cc6ad731.htm)   [See Also](#seeAlsoToggle) |

Possible Member Instability, based on Release Conditions

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId AnalyticalMemberInstability { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticalMemberInstability As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ AnalyticalMemberInstability { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AnalyticalModelFailures Class](3633d562-0e24-5cad-ec0f-02e6cc6ad731.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff97d96b-a3ed-7ad6-c428-a4a274088c9a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectToUpstreamNode Method

---



|  |
| --- |
| [ElectricalAnalyticalNode Class](562d1f7d-c9df-bee5-4659-4f8607ee4333.htm)   [See Also](#seeAlsoToggle) |

Connects to upstream node.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public void ConnectToUpstreamNode( 	ElementId upstreamNodeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ConnectToUpstreamNode ( _ 	upstreamNodeId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ConnectToUpstreamNode( 	ElementId^ upstreamNodeId ) ``` |

#### Parameters

upstreamNodeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The upstream node id.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The id is not an analytical distribution node id. -or- The analytical distribution node is full of downstream nodes. -or- The analytical distribution node can not connect to the upstream node. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The analytical distribution node is full of upstream nodes. |

# See Also

[ElectricalAnalyticalNode Class](562d1f7d-c9df-bee5-4659-4f8607ee4333.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__ff9e5034-a6ce-b606-e912-d2fd602a1659.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NotAllPartsWereConvertedUnsuportedFittingOffsets Property

---



|  |
| --- |
| [BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)   [See Also](#seeAlsoToggle) |

Not all parts were converted. Eccentric transitions and taps that have offsets from the center line are unsupported and cannot be converted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NotAllPartsWereConvertedUnsuportedFittingOffsets { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NotAllPartsWereConvertedUnsuportedFittingOffsets As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NotAllPartsWereConvertedUnsuportedFittingOffsets { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ff9ef159-5435-7874-842e-7a681735bcc8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TriangleInShellComponent Class

---



|  |
| --- |
| [Members](235e2daa-2107-15e4-aaf9-55a4188f8862.htm)   [See Also](#seeAlsoToggle) |

This class represents a triangle in a TriangulatedShellComponent object. The triangle is defined by its vertices, which are specified by their indices in the TriangulatedShellComponent's array of vertices.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class TriangleInShellComponent : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class TriangleInShellComponent _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class TriangleInShellComponent : IDisposable ``` |

# Remarks

A TriangulatedShellComponent stores an array of TriangleInShellComponent objects representing the triangles of the triangulation. An external class is used because the API does not allow the use of a triple of integers. Note that a TriangleInShellComponent must only be used in the context of a single, fixed TriangulatedShellComponent.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB TriangleInShellComponent

# See Also

[TriangleInShellComponent Members](235e2daa-2107-15e4-aaf9-55a4188f8862.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffa3cea6-e76b-381a-4d95-f6917c2e9452.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NameNotUnique Property

---



|  |
| --- |
| [BuiltInFailures GeneralFailures Class](d4679f32-45d9-bec2-e0ff-168c3aee6de9.htm)   [See Also](#seeAlsoToggle) |

The name entered is already in use. Enter a unique name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NameNotUnique { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NameNotUnique As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NameNotUnique { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GeneralFailures Class](d4679f32-45d9-bec2-e0ff-168c3aee6de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffa4f8e1-f9a6-09d1-2b9d-1e98dada4440.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OnShutdown Method

---



|  |
| --- |
| [IEntryPoint Interface](b12791d1-81ab-b326-2bc7-da785d78e1fc.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` void OnShutdown() ``` |

 

| Visual Basic |
| --- |
| ``` Sub OnShutdown ``` |

 

| Visual C++ |
| --- |
| ``` void OnShutdown() ``` |

# See Also

[IEntryPoint Interface](b12791d1-81ab-b326-2bc7-da785d78e1fc.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)

<!-- Start of Syntax__ffa59457-f0d6-8cdb-012d-ffede3e140c2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpatialFieldMgrCurrentName Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Analysis Configuration"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpatialFieldMgrCurrentName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpatialFieldMgrCurrentName As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpatialFieldMgrCurrentName { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffa5bdb9-b90b-c470-3ddc-0c4c8463c8a3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ColorSelectionDialog Class](3c1ae512-f679-12ec-7b15-7b402ea6db3d.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ColorSelectionDialog](3c1ae512-f679-12ec-7b15-7b402ea6db3d.htm)

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public void Dispose() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Dispose ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Dispose() sealed ``` |

#### Implements

 [IDisposable Dispose](http://msdn2.microsoft.com/en-us/library/es4s3w1d)

# See Also

[ColorSelectionDialog Class](3c1ae512-f679-12ec-7b15-7b402ea6db3d.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__ffa8fc7d-073b-78f8-aee7-3e871681b795.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShowDataDescription Property

---



|  |
| --- |
| [AnalysisDisplayLegendSettings Class](a0362ecb-2442-6371-7e89-7a9ba66a0466.htm)   [See Also](#seeAlsoToggle) |

If true, data description is shown in the legend.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool ShowDataDescription { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ShowDataDescription As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ShowDataDescription { 	bool get (); 	void set (bool value); } ``` |

# See Also

[AnalysisDisplayLegendSettings Class](a0362ecb-2442-6371-7e89-7a9ba66a0466.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__ffaca4d8-ddb4-c21e-7830-b5fffe314fc8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddConstraintToSegment Method

---



|  |
| --- |
| [RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)   [See Also](#seeAlsoToggle) |

Add a constraint that helps determine the length of a segment.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void AddConstraintToSegment( 	int iSegment, 	ElementId paramId, 	double constraintDirCoordX, 	double constraintDirCoordY, 	int signOfZCoordOfCrossProductOfConstraintDirBySegmentDir, 	bool measureToOutsideOfBend0, 	bool measureToOutsideOfBend1 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddConstraintToSegment ( _ 	iSegment As Integer, _ 	paramId As ElementId, _ 	constraintDirCoordX As Double, _ 	constraintDirCoordY As Double, _ 	signOfZCoordOfCrossProductOfConstraintDirBySegmentDir As Integer, _ 	measureToOutsideOfBend0 As Boolean, _ 	measureToOutsideOfBend1 As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddConstraintToSegment( 	int iSegment,  	ElementId^ paramId,  	double constraintDirCoordX,  	double constraintDirCoordY,  	int signOfZCoordOfCrossProductOfConstraintDirBySegmentDir,  	bool measureToOutsideOfBend0,  	bool measureToOutsideOfBend1 ) ``` |

#### Parameters

iSegment
:   Type:  System Int32    
     Index of the segment (0 to NumberOfSegments - 1).

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of a parameter to drive the constraint. To obtain the id of a shared parameter, call RebarShape.GetElementIdForExternalDefinition().

constraintDirCoordX
:   Type:  System Double    
     The x-coordinate of a 2D vector specifying the constraint direction.

constraintDirCoordY
:   Type:  System Double    
     The y-coordinate of a 2D vector specifying the constraint direction.

signOfZCoordOfCrossProductOfConstraintDirBySegmentDir
:   Type:  System Int32    
     Legal values are 1 and -1. For a fixed-direction segment, this value is ignored. For a variable-direction segment, this value is combined with the constraint length (the nonnegative value associated with 'param') to determine the direction of the segment. For example, a segment whose direction vector lies in the upper-right quadrant of the plane, and whose x-axis projected length is A and whose y-axis projected length is B, could be created by calling: AddConstraintToSegment(iSegment, paramA, 1.0, 0.0, 1, ...) AddConstraintToSegment(iSegment, paramB, 0.0, 1.0, -1, ...)

measureToOutsideOfBend0
:   Type:  System Boolean    
     Choose between two possibilities for the first reference of the length dimension. If false, the reference is at the point where the bend begins; equivalently, at the projection of the bend centerpoint onto the segment. If true, the reference is moved outward by a distance equal to the bend radius plus the bar diameter; if the bend is a right angle or greater, this is equivalent to putting the reference at the outer face of the bend.

measureToOutsideOfBend1
:   Type:  System Boolean    
     Choose between two possibilities for the second reference of the length dimension.

# Remarks

The vector defined by (constraintDirCoordX, constraintDirCoordY) must have a positive dot product with the desired direction of the segment. This restriction, combined with the value of signOfZCoordOfCrossProductOfConstraintDirBySegmentDir, defines a quadrant of the plane that limits the variable-angle segment.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | iSegment is not between 0 and NumberOfSegments. -or- paramId is not the id of a shared parameter in the current document, or its unit type is not UT\_Reinforcement\_Length or UT\_Angle. -or- The length of the vector (constraintDirCoordX, constraintDirCoordY) is too close to zero. -or- signOfZCoordOfCrossProductOfConstraintDirBySegmentDir is neither -1 nor 1. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__ffad9c15-8fc9-fbfd-f328-101533f4cf74.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalResourceReference Class

---



|  |
| --- |
| [Members](dbd1a1bb-2419-96be-f4e0-bea9c627cd9a.htm)   [See Also](#seeAlsoToggle) |

This class identifies an external resource provided by an IExternalResourceServer.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class ExternalResourceReference : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExternalResourceReference _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExternalResourceReference : IDisposable ``` |

# Remarks

The class contains:

* The id of the IExternalResourceServer from which the resource was obtained.
* A (String, String) map containing information that is meaningful to the server for accessing the desired data. This could be something as simple as "4" to indicate that Revit wants option 4 from a range of several choices, or something more detailed, such as a filename or directory path.
* A String indicating the version of the resource that was most recently loaded in Revit.
* A (String, String) map containing "in session" information that is meaningful to the server, but which does not need to be saved permanently in the document on disk.

When calling an IExternalResourceServer, Revit will provide an ExternalResourceReference to identify the specific resource that Revit is using from that server. The server can then use the relevant information in the (String, String) maps to retrieve the data from the correct source.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ExternalResourceReference

# See Also

[ExternalResourceReference Members](dbd1a1bb-2419-96be-f4e0-bea9c627cd9a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffb18296-0448-559c-580c-7857cbcdc094.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementType Class

---



|  |
| --- |
| [Members](65dc0795-6495-74c0-92b6-267a18ce4d4e.htm)   [See Also](#seeAlsoToggle) |

Base class for all Types within Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public class ElementType : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ElementType _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ElementType : public Element ``` |

# Remarks

Element types are usually non user visible elements that define instances. For example a wall type is a type that is not visible until an instance of the wall is created.

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB ElementType    
  [Autodesk.Revit.DB.Analysis ConceptualConstructionType](59d96c60-67ae-cb70-d3a6-59e18a434eca.htm)    
  [Autodesk.Revit.DB.Architecture ContinuousRailType](0f4641e3-74e0-0a8e-eb56-fb6f9904b173.htm)    
  [Autodesk.Revit.DB.Architecture CutMarkType](6f2d8dc7-6a19-fba3-00ae-a88cfe0e3d34.htm)    
  [Autodesk.Revit.DB.Architecture RailingType](7e7551fe-1772-f2d3-a8b5-58d4bb42a34e.htm)    
  [Autodesk.Revit.DB.Architecture StairsLandingType](f8f8ec06-3a1d-cb85-2c0b-cb5095c73a08.htm)    
  [Autodesk.Revit.DB.Architecture StairsPathType](36994970-3d80-62a3-df6f-381d38f2eda0.htm)    
  [Autodesk.Revit.DB.Architecture StairsRunType](a76503c0-abd8-0043-883b-134149348542.htm)    
  [Autodesk.Revit.DB.Architecture StairsType](efa84f53-19fa-039b-c5bb-8fcb72e09878.htm)    
  [Autodesk.Revit.DB.Architecture TopographyLinkType](773d38dc-a1c9-a74e-2c4b-70bcb174059b.htm)    
  [Autodesk.Revit.DB AssemblyType](19fb680c-cd62-24e4-2e68-45bfc04207d2.htm)    
  [Autodesk.Revit.DB BeamSystemType](6b42bef4-e54f-db0c-ce13-a097213fbc4f.htm)    
  [Autodesk.Revit.DB BrowserOrganization](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)    
  [Autodesk.Revit.DB CADLinkType](593779f4-d044-ba36-1888-969743ce782a.htm)    
  [Autodesk.Revit.DB DimensionType](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.htm)    
  [Autodesk.Revit.DB DirectShapeType](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)    
  [Autodesk.Revit.DB.Electrical DistributionSysType](03754b33-fd20-b19b-a718-6dc2eeccd76c.htm)    
  [Autodesk.Revit.DB.Electrical InsulationType](3eacc872-bb46-73a5-9ae7-d309d1d3ad64.htm)    
  [Autodesk.Revit.DB.Electrical TemperatureRatingType](fe7e15d7-c31f-b24c-992f-332e54e9a5ba.htm)    
  [Autodesk.Revit.DB.Electrical VoltageType](6b462685-b825-f8f9-f218-035107f7aaf0.htm)    
  [Autodesk.Revit.DB.Electrical WireMaterialType](3d05ec79-0289-c6d1-2a13-7e6b07241afd.htm)    
  [Autodesk.Revit.DB.Electrical WireType](f4d1a1cc-6968-251b-9692-247dc3ff6cff.htm)    
  [Autodesk.Revit.DB FabricationPartType](261b8995-37db-ad23-9ae6-929cb0a77122.htm)    
  [Autodesk.Revit.DB GroupType](5ce7e921-2a43-d7f1-8ef9-8a397dd27b75.htm)    
  [Autodesk.Revit.DB HostObjAttributes](a3d349c5-d457-3b56-eec4-c2fa2757c860.htm)    
  [Autodesk.Revit.DB ImageType](c6213f81-8dc8-158e-0522-70f87e9bdbb9.htm)    
  [Autodesk.Revit.DB InsertableObject](73d870e0-a408-719c-58bd-1fb2ab8f9e5b.htm)    
  [Autodesk.Revit.DB LineAndTextAttrSymbol](1a0a0d23-891b-bf92-6b2b-069704dea9be.htm)    
  [Autodesk.Revit.DB.Mechanical DuctInsulationType](96a17178-1b21-892f-364a-4be11b39b554.htm)    
  [Autodesk.Revit.DB.Mechanical DuctLiningType](4586ac5e-f45d-89b0-842f-e66ae617ae30.htm)    
  [Autodesk.Revit.DB.Mechanical MechanicalEquipmentSetType](d4746a51-5dca-7cb4-d19a-5e1184ee6f39.htm)    
  [Autodesk.Revit.DB.Mechanical MEPBuildingConstruction](3468e6dd-c676-cf39-b851-052b3e3a2f95.htm)    
  [Autodesk.Revit.DB MEPAnalyticalConnectionType](a0840c90-ffe0-fc59-7af3-022967128828.htm)    
  [Autodesk.Revit.DB MEPSystemType](9a14b7f0-1472-4375-c4f0-86f9f2479851.htm)    
  [Autodesk.Revit.DB ModelTextType](54498ab7-d9a1-320b-61c1-ee4b894464bb.htm)    
  [Autodesk.Revit.DB MultiReferenceAnnotationType](046b4d91-40b3-4dd0-be1b-635fb30956c2.htm)    
  [Autodesk.Revit.DB.Plumbing FluidType](6de7a895-6747-7273-55cf-19f917a30c84.htm)    
  [Autodesk.Revit.DB.Plumbing PipeInsulationType](1e9c8ce4-8447-ad6e-d92e-c68ad1a384b5.htm)    
  [Autodesk.Revit.DB.Plumbing PipeScheduleType](d580725f-60f3-034a-e358-d4ed8896d915.htm)    
  [Autodesk.Revit.DB PointCloudType](b7ba9b9c-fd96-7506-1585-6fc2b327e0e9.htm)    
  [Autodesk.Revit.DB RevitLinkType](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)    
  [Autodesk.Revit.DB SiteLocation](9d71159d-514c-c1b3-8673-5c0e7f28b688.htm)    
  [Autodesk.Revit.DB.Structure AnalyticalLinkType](9362135d-6ea6-ff5a-e026-b6c247a497a1.htm)    
  [Autodesk.Revit.DB.Structure AreaReinforcementType](1fb9f43b-e9d7-89b9-104f-2dd57e84fbe2.htm)    
  [Autodesk.Revit.DB.Structure EndTreatmentType](107f2dd4-7a92-e67e-0b79-a1c8c87dbf35.htm)    
  [Autodesk.Revit.DB.Structure FabricAreaType](ac1e177f-5041-418f-c220-962887091d3c.htm)    
  [Autodesk.Revit.DB.Structure FabricSheetType](892f0ce6-5548-d299-c976-9355ac4109ee.htm)    
  [Autodesk.Revit.DB.Structure FabricWireType](e492fc52-b8a5-c12f-b73d-2fd1c29a331b.htm)    
  [Autodesk.Revit.DB.Structure LoadTypeBase](01b08561-f396-1475-6e90-05c2e9f41d48.htm)    
  [Autodesk.Revit.DB.Structure PathReinforcementType](3bddfeb2-4db2-1bf1-b7e8-09238c8dfb32.htm)    
  [Autodesk.Revit.DB.Structure RebarBarType](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)    
  [Autodesk.Revit.DB.Structure RebarContainerType](944b0bbc-92e0-123f-12c8-a01feca40e72.htm)    
  [Autodesk.Revit.DB.Structure RebarCoverType](b90685db-d2c5-aecb-ff1f-425ca2e5fae9.htm)    
  [Autodesk.Revit.DB.Structure RebarHookType](3c7a78d5-f92b-e58b-e7c9-7927537498fd.htm)    
  [Autodesk.Revit.DB.Structure RebarShape](0a370e32-eaba-785e-7e1f-9330929525fc.htm)    
  [Autodesk.Revit.DB.Structure StructuralConnectionApprovalType](7e250cb2-63d0-aa26-5361-4f0a2a2b4a34.htm)    
  [Autodesk.Revit.DB.Structure StructuralConnectionHandlerType](e948a909-1b00-8789-6302-b46015c9cb47.htm)    
  [Autodesk.Revit.DB.Structure StructuralConnectionType](e3b74cf3-71d8-a230-7fb6-0fdc4c81fca2.htm)    
  [Autodesk.Revit.DB TilePattern](ed67a003-617e-1532-cd94-4faaa2bffc91.htm)    
  [Autodesk.Revit.DB ViewFamilyType](e0edeb6d-1627-3e3f-e386-be182a9dd8cb.htm)

# See Also

[ElementType Members](65dc0795-6495-74c0-92b6-267a18ce4d4e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffb25c4f-cd7a-bd51-8f78-3107a0955fc9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DuctFittingAndAccessoryConnectorData Class

---



|  |
| --- |
| [Members](d864c874-8d8d-13d4-5de1-ad15b280252e.htm)   [See Also](#seeAlsoToggle) |

The input data used by external servers for calculation of the duct fitting and duct accessory coefficient.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class DuctFittingAndAccessoryConnectorData : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DuctFittingAndAccessoryConnectorData _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DuctFittingAndAccessoryConnectorData : IDisposable ``` |

# Remarks

width, height, diameter, flow, velocity pressure and connector index are input data for the calculation,

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Mechanical DuctFittingAndAccessoryConnectorData

# See Also

[DuctFittingAndAccessoryConnectorData Members](d864c874-8d8d-13d4-5de1-ad15b280252e.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__ffb5fa8d-1001-de54-358b-08b24422698e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [RebarHandlesData Class](7ce5c75a-c1e9-016b-02cf-1118b6fbefad.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [RebarHandlesData](7ce5c75a-c1e9-016b-02cf-1118b6fbefad.htm)

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public void Dispose() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Dispose ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Dispose() sealed ``` |

#### Implements

 [IDisposable Dispose](http://msdn2.microsoft.com/en-us/library/es4s3w1d)

# See Also

[RebarHandlesData Class](7ce5c75a-c1e9-016b-02cf-1118b6fbefad.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__ffbcdc6e-d0d1-598f-0ce3-1eb9b53bb7d2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDWGExportAvailable Method

---



|  |
| --- |
| [OptionalFunctionalityUtils Class](98d35b3b-34ec-4105-f7c5-16e9215b6b52.htm)   [See Also](#seeAlsoToggle) |

Checks whether the DWG Export functionality is available in the installed Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static bool IsDWGExportAvailable() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsDWGExportAvailable As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsDWGExportAvailable() ``` |

#### Return Value

True if the DWG Export functionality is available in the installed Revit.

# Remarks

DWG Export requires presence of certain modules that are optional and may not be part of the installed Revit.

# See Also

[OptionalFunctionalityUtils Class](98d35b3b-34ec-4105-f7c5-16e9215b6b52.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffbddd87-8c48-78a1-34d1-5d073861751f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaterialAssetParamAssetLibId Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Asset library id"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MaterialAssetParamAssetLibId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MaterialAssetParamAssetLibId As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MaterialAssetParamAssetLibId { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffc40d36-2092-a63c-ce8c-a72ee8430d3d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsolateElementsTemporary Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Set multiple elements to be temporarily isolated in the view. To isolate a group completely, you must also include all members of all groups and nested groups in your input.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void IsolateElementsTemporary( 	ICollection<ElementId> elementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub IsolateElementsTemporary ( _ 	elementIds As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void IsolateElementsTemporary( 	ICollection<ElementId^>^ elementIds ) ``` |

#### Parameters

elementIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Ids of elements to be isolated.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffc4e960-25e8-9edb-f660-d328c57e65d0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TransferringProjectStandardsEventArgs Class

---



|  |
| --- |
| [Members](cac8a60f-f3e5-0e7e-df73-d19550160634.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by the TransferringProjectStandards event.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017.2

# Syntax

| C# |
| --- |
| ``` public class TransferringProjectStandardsEventArgs : RevitAPIPreDocEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class TransferringProjectStandardsEventArgs _ 	Inherits RevitAPIPreDocEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class TransferringProjectStandardsEventArgs : public RevitAPIPreDocEventArgs ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPreEventArgs](14097470-c9d9-0143-dc1b-b93a60a460e6.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPreDocEventArgs](ef0073c4-f86b-64b9-12f2-268f4e1b8bbe.htm)    
  Autodesk.Revit.UI.Events TransferringProjectStandardsEventArgs

# See Also

[TransferringProjectStandardsEventArgs Members](cac8a60f-f3e5-0e7e-df73-d19550160634.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__ffc983cc-bc1f-33fa-9826-9680b6a70ed2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidForMaxEdgeLength Method

---



|  |
| --- |
| [OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)   [See Also](#seeAlsoToggle) |

Checks whether the value is allowed (is in the allowed range) for MaxEdgeLength tessellation parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public static bool IsValidForMaxEdgeLength( 	double value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidForMaxEdgeLength ( _ 	value As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidForMaxEdgeLength( 	double value ) ``` |

#### Parameters

value
:   Type:  System Double    
     The value to be checked.

#### Return Value

True if the value is valid for MaxEdgeLength, false otherwise.

# See Also

[OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffcdceb3-baf6-593f-75c7-eccc849d7f28.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnconnectedDevice Property

---



|  |
| --- |
| [BuiltInFailures ConnectorFailures Class](6a9d497c-6923-0689-e0bd-2cd00fb792f8.htm)   [See Also](#seeAlsoToggle) |

Device has an unconnected [Type Name] connector (index = [Index Number]).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId UnconnectedDevice { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property UnconnectedDevice As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ UnconnectedDevice { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ConnectorFailures Class](6a9d497c-6923-0689-e0bd-2cd00fb792f8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffcfd393-0908-0b03-3033-9784ea08a785.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SmallBendRadius Property

---



|  |
| --- |
| [BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)   [See Also](#seeAlsoToggle) |

The value you entered for the bend radius for conduit is too small. Enter a larger value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SmallBendRadius { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SmallBendRadius As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SmallBendRadius { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffd259c2-53ec-f232-02e1-135ba0a6ccfd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetObjectData Method

---



|  |
| --- |
| [ArgumentException Class](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm)   [See Also](#seeAlsoToggle) |

Retrieves data needed to serialize the target object.

**Namespace:**   [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public override void GetObjectData( 	SerializationInfo info, 	StreamingContext context ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Sub GetObjectData ( _ 	info As SerializationInfo, _ 	context As StreamingContext _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void GetObjectData( 	SerializationInfo^ info,  	StreamingContext context ) override ``` |

#### Parameters

info
:   Type:  [System.Runtime.Serialization SerializationInfo](http://msdn2.microsoft.com/en-us/library/a9b6042e)    
     Data needed to serialize or deserialize the object.

context
:   Type:  [System.Runtime.Serialization StreamingContext](http://msdn2.microsoft.com/en-us/library/t16abws5)    
     The destination of the serialized stream.

#### Implements

 [ISerializable GetObjectData(SerializationInfo, StreamingContext)](http://msdn2.microsoft.com/en-us/library/27cxsdk6)    
  [\_Exception GetObjectData(SerializationInfo, StreamingContext)](http://msdn2.microsoft.com/en-us/library/854b9522)

# See Also

[ArgumentException Class](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__ffd4d6b9-a4cb-b091-d77f-c480be8aeb44.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TemperatureLossFactor Property

---



|  |
| --- |
| [AdvancedLossFactor Class](30e62a9d-eb01-8830-f897-dc8f32b486da.htm)   [See Also](#seeAlsoToggle) |

The temperature loss factor.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double TemperatureLossFactor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property TemperatureLossFactor As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double TemperatureLossFactor { 	double get (); 	void set (double value); } ``` |

#### Field Value

The loss factor as a numerical value between 0.0 and 2.0

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The loss factor is not valid because it is not between 0.0 and 2.0. |

# See Also

[AdvancedLossFactor Class](30e62a9d-eb01-8830-f897-dc8f32b486da.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__ffd4fb7b-2c5f-aaf3-4344-898ab488a237.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCreateSpline Property

---



|  |
| --- |
| [BuiltInFailures SplineFailures Class](e88537cf-2462-ba91-30de-b02885663425.htm)   [See Also](#seeAlsoToggle) |

Can't make Spline.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCreateSpline { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCreateSpline As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCreateSpline { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SplineFailures Class](e88537cf-2462-ba91-30de-b02885663425.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffd530da-8ea9-738a-078f-077d2806144b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ThermalResistance Property

---



|  |
| --- |
| [FamilyThermalProperties Class](9d9b2125-8398-9b55-8219-cbda4456ab7b.htm)   [See Also](#seeAlsoToggle) |

The calculated thermal resistance value (R-Value). The units are meter-squared kelvin per watt ((m^2\*K)/Watt).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double ThermalResistance { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ThermalResistance As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ThermalResistance { 	double get (); } ``` |

# See Also

[FamilyThermalProperties Class](9d9b2125-8398-9b55-8219-cbda4456ab7b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffd840cd-932a-41cb-4d87-2dc2420aaa24.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HeightOfRunIsTooSmall Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Height of run is too small.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId HeightOfRunIsTooSmall { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property HeightOfRunIsTooSmall As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ HeightOfRunIsTooSmall { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__ffe123f8-618c-7d57-40fd-cb9ab5707679.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SeparationNotAtJunction Property

---



|  |
| --- |
| [BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)   [See Also](#seeAlsoToggle) |

This hydraulic loop is not separated at any junction. Use the Remove Separation tool to clean up undesired hydraulic separations.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SeparationNotAtJunction { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SeparationNotAtJunction As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SeparationNotAtJunction { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fff0c470-7d98-53c4-d6fc-435714195a74.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecPanelBranchCircuitApparentLoadPhasea Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Branch Circuit Apparent Load Phase A"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecPanelBranchCircuitApparentLoadPhasea { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecPanelBranchCircuitApparentLoadPhasea As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecPanelBranchCircuitApparentLoadPhasea { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fff3da7f-b885-f543-e12d-3f75e9b5bd94.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConvertToIndependent Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Convert the dependent view to independent.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void ConvertToIndependent() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ConvertToIndependent ``` |

 

| Visual C++ |
| --- |
| ``` public: void ConvertToIndependent() ``` |

# Remarks

This method can be only applied to a dependent view. A dependent view can be created from another view using method View.Duplicate(ViewDuplicateOption.AsDependent). Dependent views have a valid primary view element ID that can be obtained via method View.GetPrimaryViewId(); Independent views have InvalidElementId as their primary view ID.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void MakeViewIndependent(View view)
{
    // Independent views will have an InvalidElementId for the Primary View Id
    if (view.GetPrimaryViewId() != ElementId.InvalidElementId)
    {
        view.ConvertToIndependent();
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub MakeViewIndependent(view As View)
    ' Independent views will have an InvalidElementId for the Primary View Id
    If view.GetPrimaryViewId() <> ElementId.InvalidElementId Then
        view.ConvertToIndependent()
    End If
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This view is not dependent. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fff3e88e-358c-e6d0-d539-61517f53140c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Start Method

---



|  |
| --- |
| [TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)   [See Also](#seeAlsoToggle) |

Starts the transaction group

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public TransactionStatus Start() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Start As TransactionStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: TransactionStatus Start() ``` |

#### Return Value

If started successfully, this method returns TransactionStatus.Started.

# Remarks

A transaction group can be started only when there is no transaction started currently. It can be started inside another transaction group. When groups are nested inside each other it is required that inner transaction groups are finished (i.e. rolled back, committed, or assimilated) before outer groups are.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Cannot modify the document for either a read-only external command is being executed, or changes to the document are temporarily disabled. -or- Transaction group cannot be started during an active transaction. -or- The Transaction group has already been started. |

# See Also

[TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)

[Start Overload](d215f800-ea30-f580-ae72-9845e915fa6e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fff7440d-6c63-f9cd-20a3-389eef8e1680.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [LineProperties Class](baddd6a0-35a8-c547-2566-ae7846799856.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
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

[LineProperties Class](baddd6a0-35a8-c547-2566-ae7846799856.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fff8becb-ceed-55e1-3977-8ea49762b48b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [MeshFromGeometryOperationResult Class](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm)   [See Also](#seeAlsoToggle) |

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

[MeshFromGeometryOperationResult Class](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fffd3894-02ab-5c2c-f56c-363042a0879c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Mbh Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol MBH, indicating unit Thousand British thermal units per hour.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Mbh { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Mbh As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Mbh { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fffd52f7-044c-1a46-6943-ff877dec3279.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AirDensity Property

---



|  |
| --- |
| [DuctSettings Class](cd632c8e-a520-2efb-a417-9dfa5677d134.htm)   [See Also](#seeAlsoToggle) |

The air density.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public double AirDensity { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AirDensity As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double AirDensity { 	double get (); 	void set (double value); } ``` |

# See Also

[DuctSettings Class](cd632c8e-a520-2efb-a417-9dfa5677d134.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)