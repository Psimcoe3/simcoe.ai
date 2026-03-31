

<!-- Start of Syntax__5a016f27-e9ef-d26e-1c0d-0379f0f3101c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLocation Method

---



|  |
| --- |
| [FamilyPointLocation Class](c91d861a-ee45-48a7-103a-7dd33cac54a9.htm)   [See Also](#seeAlsoToggle) |

Gets the location of the point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public Transform GetLocation() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLocation As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform^ GetLocation() ``` |

#### Return Value

The location of the point.

# See Also

[FamilyPointLocation Class](c91d861a-ee45-48a7-103a-7dd33cac54a9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a017f48-0d40-74d5-787b-df9e3edf983b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RailingSystemFamilyHandrails Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Handrail 1"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RailingSystemFamilyHandrails { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RailingSystemFamilyHandrails As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RailingSystemFamilyHandrails { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a129f2d-da07-ec25-2a0d-aabb91ce6e33.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reset Method

---



|  |
| --- |
| [ProjectLocationSetIterator Class](ab766dbe-0b3a-908a-d952-2b1974584823.htm)   [See Also](#seeAlsoToggle) |

Bring the iterator back to the start of the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual void Reset() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Sub Reset ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Reset() ``` |

#### Implements

 [IEnumerator Reset](http://msdn2.microsoft.com/en-us/library/8ks8wf62)

# Remarks

The Reset method will return the iterator back to the start of the set in line with the definition of IEnumerator. Note that you must call MoveNext before the first item can be accessed via the Current property.

# See Also

[ProjectLocationSetIterator Class](ab766dbe-0b3a-908a-d952-2b1974584823.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a1440e5-ac5f-a412-9e6f-72735fbdc22c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [ElementArray Class](6a3046e5-aad4-f1fa-b733-bfd57bc9cbc5.htm)   [See Also](#seeAlsoToggle) |

Removes every element from the array, rendering it empty.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
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

[ElementArray Class](6a3046e5-aad4-f1fa-b733-bfd57bc9cbc5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a16e592-7d9c-ce2c-e789-351cad27d829.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PanelScheduleLoadClassInconsistency Property

---



|  |
| --- |
| [BuiltInFailures ScheduleViewFailures Class](13d33852-f996-21d4-3d9b-f37c90785120.htm)   [See Also](#seeAlsoToggle) |

You have one or more loads connected to this panel that are not displayed in the panel schedule. Add the load classification(s) to the associated template to report this information in the Loads Summary.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId PanelScheduleLoadClassInconsistency { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PanelScheduleLoadClassInconsistency As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ PanelScheduleLoadClassInconsistency { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ScheduleViewFailures Class](13d33852-f996-21d4-3d9b-f37c90785120.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a17aba8-7f52-ba4c-c465-6734099530a5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WrappingAtInsertsParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Wrapping at Inserts"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId WrappingAtInsertsParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WrappingAtInsertsParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ WrappingAtInsertsParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a2007d2-79ab-57fb-0975-10b7329b9b1c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [LightDistribution Class](39162cb5-d13b-c7fa-9297-9a70c5678ac6.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [LightDistribution](39162cb5-d13b-c7fa-9297-9a70c5678ac6.htm)

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

[LightDistribution Class](39162cb5-d13b-c7fa-9297-9a70c5678ac6.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__5a2f488f-8dbc-4746-50cd-2d408793bb9b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsHvacloadSkylightCoolingLoadParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Skylight Cooling Load"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsHvacloadSkylightCoolingLoadParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsHvacloadSkylightCoolingLoadParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsHvacloadSkylightCoolingLoadParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a2fba89-766c-6b1a-caa4-5a17e17c81d9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [GroupSet Class](cac73a6e-e521-7af1-281c-22c8e5245c03.htm)   [See Also](#seeAlsoToggle) |

Removes every group from the set, rendering it empty.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
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

[GroupSet Class](cac73a6e-e521-7af1-281c-22c8e5245c03.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a3127c7-f77b-5a39-ffa3-e0c0bd960113.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsMechanicalAnalysisEnabled Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Checks whether or not mechanical analysis is enabled, and enable or disable it.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsMechanicalAnalysisEnabled { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsMechanicalAnalysisEnabled As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsMechanicalAnalysisEnabled { 	bool get (); 	void set (bool value); } ``` |

# Remarks

Enabling mechanical analysis will not take effect unless the mechanical discipline is also enabled.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The current product type is not ProductType.Revit and discipline controls are not enabled. |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__5a363d30-712c-8706-bf44-9967cf764265.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LockedStartOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Negative Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LockedStartOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LockedStartOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LockedStartOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a3a761b-a17d-8084-3dd4-8cf5832cf68f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Transform1D Constructor (Double)

---



|  |
| --- |
| [Transform1D Class](7366ab0c-173e-ff4b-fb56-4f307cf16bc9.htm)   [See Also](#seeAlsoToggle) |

Constructs the transformation by specifying the scale only.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public Transform1D( 	double scale ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	scale As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform1D( 	double scale ) ``` |

#### Parameters

scale
:   Type:  System Double    
     The scale of the transformation.

# Remarks

The translation is set to zero. 1D space is tranformed according to the following formula: t --> scale\*t + translation This constructor sets translation to zero.

# See Also

[Transform1D Class](7366ab0c-173e-ff4b-fb56-4f307cf16bc9.htm)

[Transform1D Overload](c8d61a46-2668-7dea-1df8-f625081d6258.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a435471-42b2-880e-e189-9baba8b18b21.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasCircuitsWithoutElectricalLoadAreas Method

---



|  |
| --- |
| [ElectricalLoadAreaData Class](abb42f97-928b-337f-26f7-ba939682c546.htm)   [See Also](#seeAlsoToggle) |

Checks whether there are any empty plan circuits in which there are no electrical load areas.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public static bool HasCircuitsWithoutElectricalLoadAreas( 	Document doc, 	ElementId levelId, 	ElementId phaseId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function HasCircuitsWithoutElectricalLoadAreas ( _ 	doc As Document, _ 	levelId As ElementId, _ 	phaseId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool HasCircuitsWithoutElectricalLoadAreas( 	Document^ doc,  	ElementId^ levelId,  	ElementId^ phaseId ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to check.

levelId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The base level on which the empty plan circuits to check.

phaseId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The associated phase in which the empty plan circuits to check.

#### Return Value

True if there are empty plan circuits in which there are no electrical load areas, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | doc is not a project document. -or- The ElementId levelId is not a Level. -or- The id does not represent a valid phase. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). |

# See Also

[ElectricalLoadAreaData Class](abb42f97-928b-337f-26f7-ba939682c546.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__5a4be39d-5915-df82-2c0b-56eb676ad3df.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProfileCrossesRevolutionAxis Property

---



|  |
| --- |
| [BuiltInFailures RevolutionFailures Class](b359fd82-5bf1-b5a5-babe-c5670b4792a7.htm)   [See Also](#seeAlsoToggle) |

The profile must not cross the axis of revolution.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ProfileCrossesRevolutionAxis { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ProfileCrossesRevolutionAxis As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ProfileCrossesRevolutionAxis { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RevolutionFailures Class](b359fd82-5bf1-b5a5-babe-c5670b4792a7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a4c70fa-83cc-d594-2dda-84f3386ceae7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NamingCategoryId Property

---



|  |
| --- |
| [AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.htm)   [See Also](#seeAlsoToggle) |

Id of the category that drives the default naming scheme for the assembly instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementId NamingCategoryId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property NamingCategoryId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ NamingCategoryId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: This naming category was not valid for an assembly instance containing the proposed members. The naming category should match one of the member element categories. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a50cc4a-5430-2d11-2796-948c99bcafe8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DockableFrameShown Property

---



|  |
| --- |
| [DockableFrameVisibilityChangedEventArgs Class](bc6bbc27-ed14-c79d-9e00-5c43b9cf978c.htm)   [See Also](#seeAlsoToggle) |

True if the pane is being shown, false if it is being hidden.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool DockableFrameShown { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property DockableFrameShown As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool DockableFrameShown { 	bool get (); } ``` |

# See Also

[DockableFrameVisibilityChangedEventArgs Class](bc6bbc27-ed14-c79d-9e00-5c43b9cf978c.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__5a51a5dc-1bbc-84d8-ed17-2586026aadd8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [FluidTemperatureSetIterator Class](94e43dde-d2f5-1e7c-8c34-04b34ed190c1.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [FluidTemperatureSetIterator](94e43dde-d2f5-1e7c-8c34-04b34ed190c1.htm)

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

# See Also

[FluidTemperatureSetIterator Class](94e43dde-d2f5-1e7c-8c34-04b34ed190c1.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__5a521e68-0dd5-b622-4845-6f0b32d7536e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralWallUsage Property

---



|  |
| --- |
| [StructuralWallUsageFilter Class](43b4c666-5f81-bd42-dfb5-d1d86f517dee.htm)   [See Also](#seeAlsoToggle) |

The wall structural usage.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public StructuralWallUsage StructuralWallUsage { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property StructuralWallUsage As StructuralWallUsage 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property StructuralWallUsage StructuralWallUsage { 	StructuralWallUsage get (); } ``` |

# See Also

[StructuralWallUsageFilter Class](43b4c666-5f81-bd42-dfb5-d1d86f517dee.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5a546e8b-5003-315d-981f-56b5e619760f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### KilonewtonsPerSquareMeter Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Kilonewtons per square meter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId KilonewtonsPerSquareMeter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property KilonewtonsPerSquareMeter As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ KilonewtonsPerSquareMeter { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a585ab7-7610-6b22-21d3-d9e30a70d3ba.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Contains Method

---



|  |
| --- |
| [CitySet Class](9184332e-1167-a3c1-b2c1-58e9409817f3.htm)   [See Also](#seeAlsoToggle) |

Tests for the existence of a city within the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool Contains( 	City item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Contains ( _ 	item As City _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Contains( 	City^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB City](2ceeb3cd-05a1-02c6-3d95-ef689221acdc.htm)    
     The city to be searched for.

#### Return Value

The Contains method returns True if the city is within the set, otherwise False.

# See Also

[CitySet Class](9184332e-1167-a3c1-b2c1-58e9409817f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a5b827a-44dd-f67c-dd4d-1d1e958c9bc4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MinValue Property

---



|  |
| --- |
| [VoltageType Class](6b462685-b825-f8f9-f218-035107f7aaf0.htm)   [See Also](#seeAlsoToggle) |

Get lower boundary of voltage value of this voltage definition, the unit is volt.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double MinValue { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property MinValue As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double MinValue { 	double get (); } ``` |

# See Also

[VoltageType Class](6b462685-b825-f8f9-f218-035107f7aaf0.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__5a5e5fb9-d295-1bbd-de8d-c595584c037e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ThermalAsset Constructor

---



|  |
| --- |
| [ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)   [See Also](#seeAlsoToggle) |

Constructs an instance of ThermalAsset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ThermalAsset( 	string name, 	ThermalMaterialType materialType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	name As String, _ 	materialType As ThermalMaterialType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ThermalAsset( 	String^ name,  	ThermalMaterialType materialType ) ``` |

#### Parameters

name
:   Type:  System String    
     The name of the asset.

materialType
:   Type:  [Autodesk.Revit.DB ThermalMaterialType](73446ebc-6ebf-855c-aadc-a4d4291cc082.htm)    
     The type of thermal material that this asset will describe.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name is an empty string. -or- name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a648f8c-62a0-d4c7-873c-8eab9f7abe7d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Export Method (View)

---



|  |
| --- |
| [CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)   [See Also](#seeAlsoToggle) |

Exports one 3D or 2D view

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Export( 	View view ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Export ( _ 	view As View _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Export( 	View^ view ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     An instance of the view to export

# Remarks

Note that the actual export process may differ depending on the type of export context used. For example, when the  [IModelExportContext](4309af43-f04e-4e42-2539-3fd1d64cdc6d.htm)  is used, Revit is likely to perform several rounds of traversing each view, which may result in invoking the OnViewBegin/OnViewEnd method multiple times for every one view. It is because Revit draws objects in several layers (model layer, annotation layer, etc.) and will traverse each layer individually. In the most common scenario the user will receive two invocations of OnViewBegin/OnViewEnd: In the first round, all model entities will be received, while in the second round all text annotation elements will be received, if any present in the given view.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The view is not exportable, such as a template view or wrong type view, for example. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The instance of IExportContext is not valid. -or- Rendering is currently not supported in the running instance of Revit. One reason for that to happen is that rendering and material libraries are not currently available. |

# See Also

[CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)

[Export Overload](da0f2a1b-6ba3-583b-9cb6-9dcef35951bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a68e38b-2156-eab1-c08b-dbc9a815b618.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentSavedAs Event

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the DocumentSavedAs event to be notified immediately after Revit has finished saving document with a new file name.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<DocumentSavedAsEventArgs> DocumentSavedAs ``` |

 

| Visual Basic |
| --- |
| ``` Public Event DocumentSavedAs As EventHandler(Of DocumentSavedAsEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<DocumentSavedAsEventArgs^>^ DocumentSavedAs { 	void add (EventHandler<DocumentSavedAsEventArgs^>^ value); 	void remove (EventHandler<DocumentSavedAsEventArgs^>^ value); } ``` |

# Remarks

This event is raised immediately after Revit has finished saving document with a new file name. Note that the first save of a newly created document will raise DocumentSavedAs rather than  [DocumentSaved](3eef29c9-7384-77e7-e4c1-d2149ea79e95.htm)  event. It is raised even when document saving failed or was cancelled (during DocumentSavingAs event).

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Check the 'Status' property in event's argument to see whether the action itself was successful or not.

This event is not cancellable, for the process of saving document has already been finished.

The following API functions are not available for the current document during this event:

* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  .
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__5a6b5313-eca3-8929-4fd2-750d924f06d7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HandleLoadResourceResults Method

---



|  |
| --- |
| [IExternalResourceUIServer Interface](aee37f3f-98e9-79c6-e02d-1b07e3ffd89c.htm)   [See Also](#seeAlsoToggle) |

Implement this method to display any UI related to messages or errors that result when the DB server associated with this UI server attempts to load an external resource.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` void HandleLoadResourceResults( 	Document document, 	IList<ExternalResourceLoadData> loadData ) ``` |

 

| Visual Basic |
| --- |
| ``` Sub HandleLoadResourceResults ( _ 	document As Document, _ 	loadData As IList(Of ExternalResourceLoadData) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` void HandleLoadResourceResults( 	Document^ document,  	IList<ExternalResourceLoadData^>^ loadData ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document into which resources were loaded.

loadData
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [ExternalResourceLoadData](e2156349-e735-775f-8cfa-4eaa6bda9f3b.htm)    
     A collection of ExternalResourceLoadData objects containing information about an attempt to load one or more external resources, including:

    * the load request Id
    * the type of resource that was loaded
    * information to identify the particular resource that was loaded
    * the actual content obtained during the load attempt
    * the context of the load operations, e.g. LoadOperationType::Explicit for an explicit loading, LoadOperationType::Automatic for an automatic loading
    * a settable property indicating whether the server reported any errors for the resource

    The ExternalResourceLoadData contains a property, ErrorsReported, which the server can use to indicate whether it handled any errors for the resource.

    For Revit links specifically, Revit will check this value to see if it should report errors about a given link in the Unresolved References dialog. An IExternalResourceUIServer can set this value to true to avoid redundant messages.

    Note that it is possible for Revit to encounter errors internally even if the server successfully provides a reference. In general, this value should only be set to true if the server has reported an error condition.

# Remarks

This method will be called automatically by Revit after the external resource load process is complete.

Note that automatic loads can occur in the context of other operations such as opening a file. During automatic loads, it is therefore recommended that the server only display UI that is critical for the user to see (such as error message).

The loading operation type is Explicit when the user is specifically trying to reload the resource. During explicit loads, it may be desirable to provide more feedback to the user, such as specific feedback that the load operation succeeded.

The loading operation type can be accessed through  [ExternalResourceLoadContext](225225cb-6161-4681-34f9-1da4a6d50856.htm)  .

Note that providing messages and other UI feedback for Revit links is more complicated, because links can be nested. The UI server may wish to provide different messages and take different actions, depending on whether a link loaded from the DB server was a "top-level" link, or was nested. For example, while it may be possible to correct an error that occurred with a top-level link by loading it directly, this cannot be done with a nested link, as Revit will throw an exception.

To complicate things further, the same Revit document may appear more than once in a tree of nested links, and the UI server should avoid repeatedly posting the same message for instances of that document.

To help UI servers handle situations where a nested tree of links is loaded:

* Each UI server whose DB server loaded one or more links in the tree will only be called once.
* The collection of ExternalResourceLoadData objects passed into this method will include  *only those for links loaded by this server's DB server*  .
* The LinkLoadResults object contained in all ExternalResourceLoadData objects will always be the results for the  *top-level*  link, even if the top-level link was not loaded by this server's DB server. The LinkLoadResults class contains methods for navigating the full tree of load results (starting with the top node), so the UI server will be able to determine the complete context in which one of its DB server's resources was loaded.
* Servers should only report results for their own link, whether they are nested or not.

# See Also

[IExternalResourceUIServer Interface](aee37f3f-98e9-79c6-e02d-1b07e3ffd89c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__5a6ba592-c453-5658-f0c6-1ec34052b9be.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Subcategory Property

---



|  |
| --- |
| [ModelText Class](3a51d58c-3e29-b641-e8bb-4d8a17c31527.htm)   [See Also](#seeAlsoToggle) |

The subcategory.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Category Subcategory { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Subcategory As Category 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Category^ Subcategory { 	Category^ get (); 	void set (Category^ value); } ``` |

# Remarks

The subcategory can be set to either the family category or one of its subcategories.

# See Also

[ModelText Class](3a51d58c-3e29-b641-e8bb-4d8a17c31527.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a720a82-a1cf-ea8c-ad12-bad2dd3a19e4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ColumnTopAttachmentOffsetParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Offset From Attachment At Top"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ColumnTopAttachmentOffsetParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ColumnTopAttachmentOffsetParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ColumnTopAttachmentOffsetParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a74bb7c-bc69-12f7-a9fc-4cb54d42a452.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureVRepeat Property

---



|  |
| --- |
| [Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)   [See Also](#seeAlsoToggle) |

The property labeled "V Repeat" from the "Tile" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TextureVRepeat { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextureVRepeat As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TextureVRepeat { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyBoolean".

# See Also

[Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__5a7635a2-04f5-d322-8b91-8b5584bff327.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddReferencePlane Method (Plane, BoundingBoxUV)

---



|  |
| --- |
| [DirectShape Class](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.htm)   [See Also](#seeAlsoToggle) |

Adds a reference plane to the DirectShape. The reference plane can either be bounded or unbounded.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void AddReferencePlane( 	Plane refPlane, 	BoundingBoxUV boundingBoxUV ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddReferencePlane ( _ 	refPlane As Plane, _ 	boundingBoxUV As BoundingBoxUV _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddReferencePlane( 	Plane^ refPlane,  	BoundingBoxUV^ boundingBoxUV ) ``` |

#### Parameters

refPlane
:   Type:  [Autodesk.Revit.DB Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)    
     The geometry of the new reference plane.

boundingBoxUV
:   Type:  [Autodesk.Revit.DB BoundingBoxUV](e38a0145-4267-0b3f-0718-adb14e34c94e.htm)    
     If boundingBoxUV is set, the resulting reference plane that is added to the DirectShape will be displayed with those bounds. Note that the specified bounds must not be degenerate. If boundingBoxUV is not set, reasonable bounds are automatically calculated and applied to the input plane. The automatic bounds are based on the host direct shape's geometry.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | boundingBoxUV cannot be used as a BoundingBoxUV for the reference plane surface. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShape Class](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.htm)

[AddReferencePlane Overload](f650779d-7f62-082d-28e5-d4e73e1b20ef.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a765ce4-da82-c9fd-cd6d-289df73c6b29.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FieldDelimiter Property

---



|  |
| --- |
| [ViewScheduleExportOptions Class](f0bde7ea-ceab-820d-7c55-b09819f21607.htm)   [See Also](#seeAlsoToggle) |

How to delimit fields. Default is Tab.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public string FieldDelimiter { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FieldDelimiter As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ FieldDelimiter { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ViewScheduleExportOptions Class](f0bde7ea-ceab-820d-7c55-b09819f21607.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a80585c-198b-040e-f889-481214cceb8f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeDefinitionByArc Constructor (Document, Double, Double, Int32, Int32)

---



|  |
| --- |
| [RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)   [See Also](#seeAlsoToggle) |

Create a spiral shape definition.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public RebarShapeDefinitionByArc( 	Document doc, 	double height, 	double pitch, 	int baseFinishingTurns, 	int topFinishingTurns ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	doc As Document, _ 	height As Double, _ 	pitch As Double, _ 	baseFinishingTurns As Integer, _ 	topFinishingTurns As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarShapeDefinitionByArc( 	Document^ doc,  	double height,  	double pitch,  	int baseFinishingTurns,  	int topFinishingTurns ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

height
:   Type:  System Double    
     The height of the spiral (assuming the spiral is vertical).

pitch
:   Type:  System Double    
     The pitch, or vertical distance traveled in one rotation.

baseFinishingTurns
:   Type:  System Int32    
     The number of finishing turns at the lower end of the spiral.

topFinishingTurns
:   Type:  System Int32    
     The number of finishing turns at the upper end of the spiral.

# Remarks

In order to create a spiral definition, you must provide default values for the spiral-specific parameters. Replaces RebarShape.NewDefinitionByArc() from prior versions.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | baseFinishingTurns is not between 0 and 100. -or- topFinishingTurns is not between 0 and 100. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for height must be greater than 0 and no more than 30000 feet. -or- The given value for pitch must be greater than 0 and no more than 30000 feet. |

# See Also

[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)

[RebarShapeDefinitionByArc Overload](69c14c72-4c10-1840-014b-b48646d003f1.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5a82c7ad-4b6e-a62c-6b0c-7fe790886995.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsRectangular Method

---



|  |
| --- |
| [CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)   [See Also](#seeAlsoToggle) |

Identifies if the curve loop is rectangular with respect to a given projection plane.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsRectangular( 	Plane plane ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsRectangular ( _ 	plane As Plane _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsRectangular( 	Plane^ plane ) ``` |

#### Parameters

plane
:   Type:  [Autodesk.Revit.DB Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)    
     The plane to which the curves will be projected to determine if they represent a rectangle.

#### Return Value

True if the curve loop is rectangular, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a835fdc-3bbe-a89d-7dd5-f9a2b22741b3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecDistributionNodeSupplyFrom1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Supply From 1"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecDistributionNodeSupplyFrom1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecDistributionNodeSupplyFrom1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecDistributionNodeSupplyFrom1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a860cc6-63a2-942b-f44f-1330a5bc777d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotRemoveSubordFromGroupWarn Property

---



|  |
| --- |
| [BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)   [See Also](#seeAlsoToggle) |

Element can't be removed or excluded from the Group because it is required by another Group element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotRemoveSubordFromGroupWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotRemoveSubordFromGroupWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotRemoveSubordFromGroupWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a8adeed-72ce-9eae-eca0-1d7225fcf2c5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ExtrusionAnalyzer Class](ba9e3283-6868-8834-e8bf-2ea9e7358930.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ExtrusionAnalyzer](ba9e3283-6868-8834-e8bf-2ea9e7358930.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

[ExtrusionAnalyzer Class](ba9e3283-6868-8834-e8bf-2ea9e7358930.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a8e17be-3239-342e-d3fd-875f7e79137d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecLoadsummaryDemandFactorRuleParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Description"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecLoadsummaryDemandFactorRuleParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecLoadsummaryDemandFactorRuleParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecLoadsummaryDemandFactorRuleParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a90ff84-c233-50b6-4eb8-70cf17461f70.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEmpty Property

---



|  |
| --- |
| [CurveByPointsArray Class](05d7b8f5-e891-e58f-c1aa-3e0e5d96d19c.htm)   [See Also](#seeAlsoToggle) |

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

[CurveByPointsArray Class](05d7b8f5-e891-e58f-c1aa-3e0e5d96d19c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5a96c36b-097c-0f79-1919-595c1aa7a351.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ClearHandleConstraintPairHighlighting Method

---



|  |
| --- |
| [RebarConstraintsManager Class](32fe1ec6-ddb3-feac-f18c-8683b054f639.htm)   [See Also](#seeAlsoToggle) |

Clears all highlighting in all views.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void ClearHandleConstraintPairHighlighting( 	Document aDoc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ClearHandleConstraintPairHighlighting ( _ 	aDoc As Document _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ClearHandleConstraintPairHighlighting( 	Document^ aDoc ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

# Remarks

If highlightHandleConstraintPairInAllViews has been called, then this method can be used to remove all highlighting.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarConstraintsManager Class](32fe1ec6-ddb3-feac-f18c-8683b054f639.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5aa0bc88-1b77-b112-d752-ec7ebf0aa396.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BarTypeDiameterOptions Constructor

---



|  |
| --- |
| [BarTypeDiameterOptions Class](a4f6aef6-f961-7b77-7c4b-6248193c258a.htm)   [See Also](#seeAlsoToggle) |

Constructs a new BarTypeDiameterOptions with default settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public BarTypeDiameterOptions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: BarTypeDiameterOptions() ``` |

# See Also

[BarTypeDiameterOptions Class](a4f6aef6-f961-7b77-7c4b-6248193c258a.htm)

[BarTypeDiameterOptions Overload](fa5ac00b-2bde-ab00-3f26-c3fff68cd1a0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5aa1ae64-d85c-d760-e366-23bef6fd3f73.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OutdoorAirFlowStandard Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all the possible outdoor airflow standard for a space type.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public enum OutdoorAirFlowStandard ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration OutdoorAirFlowStandard ``` |

 

| Visual C++ |
| --- |
| ``` public enum class OutdoorAirFlowStandard ``` |

# Members

| Member name | Description |
| --- | --- |
| ByPeopleAndByArea | By people and by area. |
| ByACH | By ACH. |
| MaxByPeople\_ByArea | Maximum(by people, by area). |
| MaxByACH\_ByPeopleByArea | Maximum(by ACH, by people and by area). |
| MaxByACH\_ByArea\_ByPeople | Maximum(by ACH, by area, by people). |

# See Also

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__5aa60856-8737-395d-8870-087f67c1da66.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExtendBelowBaseGreaterThanRunTopElevation Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Extend Below Base needs to be less than Run Top Elevation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ExtendBelowBaseGreaterThanRunTopElevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ExtendBelowBaseGreaterThanRunTopElevation As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ExtendBelowBaseGreaterThanRunTopElevation { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5aaa0247-7707-7508-4973-009b01669297.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TaskDialog Constructor

---



|  |
| --- |
| [TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)   [See Also](#seeAlsoToggle) |

Creates a task dialog with title.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public TaskDialog( 	string title ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	title As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: TaskDialog( 	String^ title ) ``` |

#### Parameters

title
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when title is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when title is an empty string. |

# See Also

[TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__5aabd0a2-ad24-2456-c163-68bd06914073.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.SlabShapeFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](488fea20-610c-c1f2-f3dc-0ea56966e892.htm)   [See Also](#seeAlsoToggle) |

Failures about SlabShape.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class SlabShapeFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class SlabShapeFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SlabShapeFailures abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BuiltInFailures SlabShapeFailures

# See Also

[BuiltInFailures SlabShapeFailures Members](488fea20-610c-c1f2-f3dc-0ea56966e892.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5aaeefcb-2f36-6f44-0c84-f48fad404a99.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewShapeBuilder Constructor (DirectShapeTargetViewType)

---



|  |
| --- |
| [ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)   [See Also](#seeAlsoToggle) |

A constructor for an ViewShapeBuilder object that takes a view type. It will infer the view normal from view type. View normal and view type are used to validate the geometry to be stored as a view-specific shape representation of a DirectShape object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public ViewShapeBuilder( 	DirectShapeTargetViewType targetViewType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	targetViewType As DirectShapeTargetViewType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ViewShapeBuilder( 	DirectShapeTargetViewType targetViewType ) ``` |

#### Parameters

targetViewType
:   Type:  [Autodesk.Revit.DB DirectShapeTargetViewType](1c5cd94e-3804-54da-73af-505655b0948f.htm)    
     View type for which this shape representation is intended. Currently limited to Plan Views.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | targetViewType is not DirectShapeTargetViewType::Plan |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)

[ViewShapeBuilder Overload](ca873c2a-8ad3-328f-9da4-010428bcb160.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5abb7cd1-e4c1-7565-e591-a9d79ccb46c0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidFilledRegionTypeId Method

---



|  |
| --- |
| [FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the given Id is a valid filled region type Id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool IsValidFilledRegionTypeId( 	Document document, 	ElementId typeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidFilledRegionTypeId ( _ 	document As Document, _ 	typeId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidFilledRegionTypeId( 	Document^ document,  	ElementId^ typeId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The filled region type Id.

#### Return Value

True if it is a valid filled region type Id, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ac029c0-7345-16eb-3ea7-8028eff9a121.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForegroundPatternId Property

---



|  |
| --- |
| [FilledRegionType Class](850ae173-379b-bfd6-7295-3950ccc229ca.htm)   [See Also](#seeAlsoToggle) |

The foreground fill pattern Id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public ElementId ForegroundPatternId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ForegroundPatternId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ForegroundPatternId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

When the FilledRegionAttributes element is in a family then the FillPattern used for a foreground pattern must have a 'Drafting' target.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The element id must represent a valid FillPatternElement. -or- When setting this property: The FillPattern target must be a drafting pattern. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[FilledRegionType Class](850ae173-379b-bfd6-7295-3950ccc229ca.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ac22a0f-5d83-bf91-d7db-75b17138c784.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpotSlopeReferencePointIsSingular Property

---



|  |
| --- |
| [BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)   [See Also](#seeAlsoToggle) |

The highlighted Spot Slope references an element point that is singular.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SpotSlopeReferencePointIsSingular { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpotSlopeReferencePointIsSingular As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SpotSlopeReferencePointIsSingular { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ac2ce35-d2a8-4074-ef33-5093b7e960aa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Extension Property

---



|  |
| --- |
| [ViewDisplaySketchyLines Class](c92b463b-1b59-695d-f06b-a76dacfaf2f0.htm)   [See Also](#seeAlsoToggle) |

The extension scale value. Controls the magnitude of line's extension. Values between 0 and 10.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public int Extension { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Extension As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int Extension { 	int get (); 	void set (int value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The extension value is not valid. The valid range is 0 to 10. |

# See Also

[ViewDisplaySketchyLines Class](c92b463b-1b59-695d-f06b-a76dacfaf2f0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ac42661-00c3-2c66-8a1d-0db1a1731217.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VisualLightTransmittance Property

---



|  |
| --- |
| [FamilyThermalProperties Class](9d9b2125-8398-9b55-8219-cbda4456ab7b.htm)   [See Also](#seeAlsoToggle) |

The visual light transmittance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double VisualLightTransmittance { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property VisualLightTransmittance As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double VisualLightTransmittance { 	double get (); } ``` |

# See Also

[FamilyThermalProperties Class](9d9b2125-8398-9b55-8219-cbda4456ab7b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ac59a63-16a4-1eb3-76e8-c37e5d5e3286.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsLandingtypeStructure Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Structure": Structure

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsLandingtypeStructure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsLandingtypeStructure As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsLandingtypeStructure { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ac5e53b-c8d1-538d-40ba-7e8a5e936341.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LightShapeStyle Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Tags for specific light shape styles

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum LightShapeStyle ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration LightShapeStyle ``` |

 

| Visual C++ |
| --- |
| ``` public enum class LightShapeStyle ``` |

# Members

| Member name | Description |
| --- | --- |
| Point | Point light shape. |
| Line | Line light shape. |
| Rectangle | Rectangular light shape. |
| Circle | Circular light shape. |

# See Also

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__5ac83612-a3da-02fd-57e9-ac4afac49ddd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Evaluate Method

---



|  |
| --- |
| [EdgeEndPoint Class](3388e8f3-22d4-a411-a3da-450c16a31bc5.htm)   [See Also](#seeAlsoToggle) |

Evaluate the end point of the edge in 3d coordinates.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public XYZ Evaluate() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Evaluate As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ Evaluate() ``` |

#### Return Value

The end point of the edge in 3d coordinates.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to evaluate the end point of the edge. |

# See Also

[EdgeEndPoint Class](3388e8f3-22d4-a411-a3da-450c16a31bc5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5acc523b-0e2a-1b49-6139-304522c0acf5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConditionType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all the possible condition types for a space object.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum ConditionType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ConditionType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ConditionType ``` |

# Members

| Member name | Description |
| --- | --- |
| Heated | Condition Type is Heated. |
| Cooled | Condition Type is Cooled. |
| HeatedAndCooled | Condition Type is HeatedAndCooled. |
| Unconditioned | Condition Type is Unconditioned. |
| Vented | Condition Type is Vented. |
| NaturallyVentedOnly | Condition Type is NaturallyVentedOnly. |
| NoOfConditionTypes | Condition Type is NoOfConditionTypes. |

# See Also

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__5ad1c0b7-e095-9a16-b94e-3242a28e2a90.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DefaultJoinOption Property

---



|  |
| --- |
| [ContinuousRailType Class](0f4641e3-74e0-0a8e-eb56-fb6f9904b173.htm)   [See Also](#seeAlsoToggle) |

The default join option between two rails.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public RailTypeDefaultJoinOption DefaultJoinOption { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DefaultJoinOption As RailTypeDefaultJoinOption 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property RailTypeDefaultJoinOption DefaultJoinOption { 	RailTypeDefaultJoinOption get (); 	void set (RailTypeDefaultJoinOption value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ContinuousRailType Class](0f4641e3-74e0-0a8e-eb56-fb6f9904b173.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__5ad3cfba-926d-26ef-9dd0-02c8acb2c854.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Transform Constructor

---



|  |
| --- |
| [Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)   [See Also](#seeAlsoToggle) |

The copy constructor.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Transform( 	Transform source ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	source As Transform _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform( 	Transform^ source ) ``` |

#### Parameters

source
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)

# See Also

[Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ad703b4-2fc2-b5aa-ef66-879888cc5c81.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanViewCutPlaneHeight Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Cut Plane Height"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PlanViewCutPlaneHeight { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PlanViewCutPlaneHeight As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PlanViewCutPlaneHeight { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ad8b6fc-936c-156c-09d8-b47708477e84.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElectricalLoadClassificationSpace Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

This enum is used by the ElectricalLoadClassification to specify the load class for use with spaces.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public enum ElectricalLoadClassificationSpace ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ElectricalLoadClassificationSpace ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ElectricalLoadClassificationSpace ``` |

# Members

| Member name | Description |
| --- | --- |
| None |  |
| Lighting |  |
| Power |  |

# See Also

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__5ada3cdc-d6c5-9260-68f8-cf6267604038.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddHolesForTaps Property

---



|  |
| --- |
| [FabricationSaveJobOptions Class](20934444-987d-1169-1619-2adb54377e7d.htm)   [See Also](#seeAlsoToggle) |

Set true to have holes for taps on straights added to the created fabrication job.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public bool AddHolesForTaps { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AddHolesForTaps As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool AddHolesForTaps { 	bool get (); 	void set (bool value); } ``` |

# See Also

[FabricationSaveJobOptions Class](20934444-987d-1169-1619-2adb54377e7d.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)

<!-- Start of Syntax__5ada6a0c-c3b5-d7dc-cae9-0f06074dbaaa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElemHoleTappingHole Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Tapping hole"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SteelElemHoleTappingHole { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElemHoleTappingHole As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SteelElemHoleTappingHole { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5adf8036-f82c-171c-8dc8-890f86b702c6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotPlaceFabricAreaWarn Property

---



|  |
| --- |
| [BuiltInFailures FabricFailures Class](1e10bead-55d2-51cb-dd33-80ed534cb0a8.htm)   [See Also](#seeAlsoToggle) |

Can't find a host for Fabric Area.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotPlaceFabricAreaWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotPlaceFabricAreaWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotPlaceFabricAreaWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FabricFailures Class](1e10bead-55d2-51cb-dd33-80ed534cb0a8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ae0964a-266b-ba4f-5e7d-c4b82bd636cc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextOrientation Property

---



|  |
| --- |
| [TableCellStyle Class](e9a5280b-4009-004f-57a4-af1f292f9619.htm)   [See Also](#seeAlsoToggle) |

The orientation of the cell (for vertical/horizontal text) with input in degrees multiplied by 10

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int TextOrientation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property TextOrientation As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int TextOrientation { 	int get (); 	void set (int value); } ``` |

# See Also

[TableCellStyle Class](e9a5280b-4009-004f-57a4-af1f292f9619.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ae26bdd-b1f8-3771-c02f-538a523f8457.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsRevisionIssued Method

---



|  |
| --- |
| [RevisionCloud Class](43bdb2c4-2b9c-e3fa-4d6a-8c9970a9f7b6.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the Revision associated with this RevisionCloud has been issued.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool IsRevisionIssued() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsRevisionIssued As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsRevisionIssued() ``` |

#### Return Value

True if the Revision has been issued, False otherwise.

# See Also

[RevisionCloud Class](43bdb2c4-2b9c-e3fa-4d6a-8c9970a9f7b6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ae36133-1359-8afe-4ff2-295d042b2501.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DegreeFInterval Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol Â°F, indicating unit Fahrenheit interval.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DegreeFInterval { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DegreeFInterval As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DegreeFInterval { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ae69c95-3892-a491-742e-6a8a8a91f99b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FailureMessage Constructor

---



|  |
| --- |
| [FailureMessage Class](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)   [See Also](#seeAlsoToggle) |

Creates a new FailureMessage related to a given FailureDefinition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FailureMessage( 	FailureDefinitionId id ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	id As FailureDefinitionId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: FailureMessage( 	FailureDefinitionId^ id ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.DB FailureDefinitionId](b6ada360-a6fe-ebb6-b095-d74b37ade9bf.htm)    
     Id of FailureDefinition.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | id is valid or does not have corresponding failure definition. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FailureMessage Class](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ae89d17-e1ff-2a14-9929-562a5555d78b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [LinkOperations Class](882834db-0bdc-4a40-ac75-4135d27bfb46.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
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

[LinkOperations Class](882834db-0bdc-4a40-ac75-4135d27bfb46.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5af1a48b-6353-0878-9d34-5b49ecfecb83.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GUID Property

---



|  |
| --- |
| [FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

The globally unique identifier

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public Guid GUID { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property GUID As Guid 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Guid GUID { 	Guid get (); } ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
foreach (FamilyParameter familyParam in familyDoc.FamilyManager.Parameters)
{
    string familyParamName = familyParam.Definition.Name;
    try
    {
        Guid guid = familyParam.GUID;
        TaskDialog.Show("Revit",familyParamName + " is shared. Guid is " + guid);
    }
    catch (System.Exception)
    {
        TaskDialog.Show("Revit",familyParamName + " is NOT shared");
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
For Each familyParam As FamilyParameter In familyDoc.FamilyManager.Parameters
    Dim familyParamName As String = familyParam.Definition.Name
    Try
        Dim guid As Guid = familyParam.GUID
        TaskDialog.Show("Revit", familyParamName & " is shared. Guid is " & Convert.ToString(guid))
    Catch generatedExceptionName As System.Exception
        TaskDialog.Show("Revit", familyParamName & " is NOT shared")
    End Try
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the parameter is not a shared parameter. |

# See Also

[FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5af53553-e052-e6a3-9849-ff59b5112651.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FbxLightBallastLoss Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Ballast Loss"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FbxLightBallastLoss { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FbxLightBallastLoss As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FbxLightBallastLoss { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5af5678f-9f6f-a135-b5c1-1448bdd17f7b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCellCategoryId Method (Int32)

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Returns a column's ParamId Associated with the paramId to find the correct element

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ElementId GetCellCategoryId( 	int nCol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCellCategoryId ( _ 	nCol As Integer _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetCellCategoryId( 	int nCol ) ``` |

#### Parameters

nCol
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given column number nCol is invalid. |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[GetCellCategoryId Overload](43e99cf4-5187-4fae-9268-504b0e6ee8ac.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5af8b8cf-b9bc-bbc6-76e3-87539afab783.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, String, ElementId, LoadCaseCategory)

---



|  |
| --- |
| [LoadCase Class](2a215599-9c4c-d817-e170-605fd705699d.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new LoadCase.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static LoadCase Create( 	Document document, 	string name, 	ElementId natureId, 	LoadCaseCategory loadCaseCategory ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	name As String, _ 	natureId As ElementId, _ 	loadCaseCategory As LoadCaseCategory _ ) As LoadCase ``` |

 

| Visual C++ |
| --- |
| ``` public: static LoadCase^ Create( 	Document^ document,  	String^ name,  	ElementId^ natureId,  	LoadCaseCategory loadCaseCategory ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document to which new load case element will be added.

name
:   Type:  System String    
     The name of the load case.

natureId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The load nature ID.

loadCaseCategory
:   Type:  [Autodesk.Revit.DB.Structure LoadCaseCategory](33f1eed5-e7d8-c12c-596c-55e10ac14c15.htm)    
     The predefined load case category.

#### Return Value

The newly created load case element if successful,    a null reference (  Nothing  in Visual Basic)  otherwise.

# Remarks

This method is designed to create LoadCase that is associated with one of the predefined category.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
#region Autodesk.Revit.DB.Structure.LoadUsage.Create(Autodesk.Revit.DB.Document,string)
#region Autodesk.Revit.DB.Structure.LoadComponent.#ctor(Autodesk.Revit.DB.ElementId,System.Double)
#region Autodesk.Revit.DB.Structure.LoadCombination.SetComponents(System.Collections.Generic.IList{Autodesk.Revit.DB.Structure.LoadComponent})
#region Autodesk.Revit.DB.Structure.LoadCombination.SetUsageIds(System.Collections.Generic.IList{Autodesk.Revit.DB.ElementId})
LoadCombination CreateLoadCombinationLoadCaseLoadUsageLoadNatureAndLoadComponent(Document document)
{
    // Create a new load combination
    LoadCombination loadCombination = LoadCombination.Create(document, "DL1 + RAIN1", LoadCombinationType.Combination, LoadCombinationState.Ultimate);
    if (loadCombination == null)
       throw new Exception("Create new load combination failed.");

    // Get all existing LoadCase
    FilteredElementCollector collector = new FilteredElementCollector(document);
    ICollection<Element> collection = collector.OfClass(typeof(LoadCase)).ToElements();

    // Find LoadCase "DL1"
    LoadCase case1 = null;
    foreach (Element e in collection)
    {
       LoadCase loadCase = e as LoadCase;
       if (loadCase.Name == "DL1")
       {
          case1 = loadCase;
          break;
       }
    }

    // Get all existing LoadNature
    collector = new FilteredElementCollector(document);
    collection = collector.OfClass(typeof(LoadNature)).ToElements();

    // Find LoadNature "Dead"
    LoadNature nature1 = null;
    foreach (Element e in collection)
    {
       LoadNature loadNature = e as LoadNature;
       if (loadNature.Name == "Dead")
       {
          nature1 = loadNature;
          break;
       }
    }

    // Create LoadNature "Dead" if not exist
    if (nature1 == null)
       nature1 = LoadNature.Create(document, "Dead");

    // Create LoadCase "DL1" if not exist
    if (case1 == null)
       case1 = LoadCase.Create(document, "DL1", nature1.Id, LoadCaseCategory.Dead);

    // Create LoadNature "Rain"
    LoadNature nature2 = LoadNature.Create(document, "Rain");
    if (nature2 == null)
       throw new Exception("Create new load nature failed.");

    // Create LoadCase "RAIN1"
    LoadCase case2 = LoadCase.Create(document, "RAIN1", nature2.Id, LoadCaseCategory.Snow);
    if (case1 == null || case2 == null)
       throw new Exception("Create new load case failed.");

    // Create LoadComponents - they consist of LoadCases or nested LoadCombination and Factors
    List<LoadComponent> components = new List<LoadComponent>();
    components.Add(new LoadComponent(case1.Id, 2.0));
    components.Add(new LoadComponent(case2.Id, 1.5));

    // Add components to combination
    loadCombination.SetComponents(components);

    // Create LoadUsages
    LoadUsage usage1 = LoadUsage.Create(document, "Frequent");
    LoadUsage usage2 = LoadUsage.Create(document, "Rare");

    if (usage1 == null || usage2 == null)
       throw new Exception("Create new load usage failed.");

    // Add load usages to combination
    loadCombination.SetUsageIds(new List<ElementId>() {usage1.Id, usage2.Id});

    // Give the user some information
    TaskDialog.Show("Revit", string.Format("Load Combination ID='{0}' created successfully.", loadCombination.Id.ToString()));

    return loadCombination;
}
#endregion
#endregion
#endregion
#endregion
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
#Region "Autodesk.Revit.DB.Structure.LoadUsage.Create(Autodesk.Revit.DB.Document,string)"
#Region "Autodesk.Revit.DB.Structure.LoadComponent.#ctor(Autodesk.Revit.DB.ElementId,System.Double)"
#Region "Autodesk.Revit.DB.Structure.LoadCombination.SetComponents(System.Collections.Generic.IList{Autodesk.Revit.DB.Structure.LoadComponent})"
#Region "Autodesk.Revit.DB.Structure.LoadCombination.SetUsageIds(System.Collections.Generic.IList{Autodesk.Revit.DB.ElementId})"
        Private Function CreateLoadCombinationLoadCaseLoadUsageLoadNatureAndLoadComponent(document As Document) As LoadCombination
            ' Create a new load combination
            Dim loadCombination__1 As LoadCombination = LoadCombination.Create(document, "DL1 + RAIN1", LoadCombinationType.Combination, LoadCombinationState.Ultimate)
            If loadCombination__1 Is Nothing Then
                Throw New Exception("Create new load combination failed.")
            End If

            ' Get all existing LoadCase
            Dim collector As New FilteredElementCollector(document)
            Dim collection As ICollection(Of Element) = collector.OfClass(GetType(LoadCase)).ToElements()

            ' Find LoadCase "DL1"
            Dim case1 As LoadCase = Nothing
            For Each e As Element In collection
                Dim loadCase__2 As LoadCase = TryCast(e, LoadCase)
                If loadCase__2.Name = "DL1" Then
                    case1 = loadCase__2
                    Exit For
                End If
            Next

            ' Get all existing LoadNature
            collector = New FilteredElementCollector(document)
            collection = collector.OfClass(GetType(LoadNature)).ToElements()

            ' Find LoadNature "Dead"
            Dim nature1 As LoadNature = Nothing
            For Each e As Element In collection
                Dim loadNature__3 As LoadNature = TryCast(e, LoadNature)
                If loadNature__3.Name = "Dead" Then
                    nature1 = loadNature__3
                    Exit For
                End If
            Next

            ' Create LoadNature "Dead" if not exist
            If nature1 Is Nothing Then
                nature1 = LoadNature.Create(document, "Dead")
            End If

            ' Create LoadCase "DL1" if not exist
            If case1 Is Nothing Then
                case1 = LoadCase.Create(document, "DL1", nature1.Id, LoadCaseCategory.Dead)
            End If

            ' Create LoadNature "Rain"
            Dim nature2 As LoadNature = LoadNature.Create(document, "Rain")
            If nature2 Is Nothing Then
                Throw New Exception("Create new load nature failed.")
            End If

            ' Create LoadCase "RAIN1"
            Dim case2 As LoadCase = LoadCase.Create(document, "RAIN1", nature2.Id, LoadCaseCategory.Snow)
            If case1 Is Nothing OrElse case2 Is Nothing Then
                Throw New Exception("Create new load case failed.")
            End If

            ' Create LoadComponents - they consist of LoadCases or nested LoadCombination and Factors
            Dim components As New List(Of LoadComponent)()
            components.Add(New LoadComponent(case1.Id, 2.0))
            components.Add(New LoadComponent(case2.Id, 1.5))

            ' Add components to combination
            loadCombination__1.SetComponents(components)

            ' Create LoadUsages
            Dim usage1 As LoadUsage = LoadUsage.Create(document, "Frequent")
            Dim usage2 As LoadUsage = LoadUsage.Create(document, "Rare")

            If usage1 Is Nothing OrElse usage2 Is Nothing Then
                Throw New Exception("Create new load usage failed.")
            End If

            ' Add load usages to combination
            loadCombination__1.SetUsageIds(New List(Of ElementId)() From {
                usage1.Id,
                usage2.Id
            })

            ' Give the user some information
            TaskDialog.Show("Revit", String.Format("Load Combination ID='{0}' created successfully.", loadCombination__1.Id.ToString()))

            Return loadCombination__1
        End Function
#End Region
#End Region
#End Region
#End Region
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given name is not unique. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[LoadCase Class](2a215599-9c4c-d817-e170-605fd705699d.htm)

[Create Overload](740a8253-95ee-dfd1-0367-733f2612435d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5afe33cc-fc32-879e-4f51-a0388b2bc8e6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCExporterService Property

---



|  |
| --- |
| [ExternalServices BuiltInExternalServices Class](f189eb3f-7a3a-2891-657a-e18cbf014987.htm)   [See Also](#seeAlsoToggle) |

The external service which permits registration of an alternate implementation for IFC export.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static ExternalServiceId IFCExporterService { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property IFCExporterService As ExternalServiceId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ExternalServiceId^ IFCExporterService { 	ExternalServiceId^ get (); } ``` |

# See Also

[ExternalServices BuiltInExternalServices Class](f189eb3f-7a3a-2891-657a-e18cbf014987.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)

<!-- Start of Syntax__5afe890a-cdb3-db2e-86d9-4a862a2533e0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.WorksharingFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](6b5eb89a-5cc3-d85c-68d2-be1a6122f194.htm)   [See Also](#seeAlsoToggle) |

Failures about WorksharingFailures.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class WorksharingFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class WorksharingFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class WorksharingFailures abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BuiltInFailures WorksharingFailures

# See Also

[BuiltInFailures WorksharingFailures Members](6b5eb89a-5cc3-d85c-68d2-be1a6122f194.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b0d01ea-5be3-ef0e-2062-dd979a4e6e2a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewSolarstudySingledayPresetIndex Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Single day presets combo"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ViewSolarstudySingledayPresetIndex { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewSolarstudySingledayPresetIndex As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ViewSolarstudySingledayPresetIndex { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b0dfa5d-bc2f-b097-a8d6-c5e78c569add.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TypeId Property

---



|  |
| --- |
| [AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.htm)   [See Also](#seeAlsoToggle) |

Specifies the ElementId of the labels' type. The default value is InvalidElementId. in this case,  [CreateSet(Alignment, View, AlignmentStationLabelSetOptions)](bbb3fb20-cbc6-f6aa-cc23-ae7ad73747b3.htm)  will throw an exception.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public ElementId TypeId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property TypeId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ TypeId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

Recommended types can be found using  [IsRecommendedTypeForSet(Element)](df3f1355-5c15-5665-23e6-520ce91c8815.htm)  Other valid types can be found using  [IsValidType(Element)](ff11b964-e6e7-9dad-fbf1-461244fcf010.htm)  .

# See Also

[AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)

<!-- Start of Syntax__5b10a892-0a51-73e7-f8b1-73cca20c206d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [MEPAnalyticalConnectionType Class](a0840c90-ffe0-fc59-7af3-022967128828.htm)   [See Also](#seeAlsoToggle) |

Creates an analytical connection type element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static MEPAnalyticalConnectionType Create( 	Document doc, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	doc As Document, _ 	name As String _ ) As MEPAnalyticalConnectionType ``` |

 

| Visual C++ |
| --- |
| ``` public: static MEPAnalyticalConnectionType^ Create( 	Document^ doc,  	String^ name ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

name
:   Type:  System String    
     The name of the analytical type to be created.

#### Return Value

The created analytical connection type element.

# Remarks

The newly created type would have the default pressure loss being 0. Use ElementType.duplicate to copy from any existing type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This name is already used by an existing analytical connection type in the document. -or- name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". -or- name is an empty string. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MEPAnalyticalConnectionType Class](a0840c90-ffe0-fc59-7af3-022967128828.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b145517-1904-4b5f-2f66-0d84b259335b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FieldDomainPoints Class

---



|  |
| --- |
| [Members](2d20125e-aa71-7233-32b0-142371d519da.htm)   [See Also](#seeAlsoToggle) |

Abstract base class for various classes of field domain points

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class FieldDomainPoints : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FieldDomainPoints _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FieldDomainPoints : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Analysis FieldDomainPoints    
  [Autodesk.Revit.DB.Analysis FieldDomainPointsByParameter](6fbc455e-bb1d-b812-ccb1-c49dbcb15d74.htm)    
  [Autodesk.Revit.DB.Analysis FieldDomainPointsByUV](aa1eb974-d283-f16e-8431-a7e02fe4e076.htm)    
  [Autodesk.Revit.DB.Analysis FieldDomainPointsByXYZ](e3715e8d-786b-e04e-f03b-a1b9b1c86ba8.htm)

# See Also

[FieldDomainPoints Members](2d20125e-aa71-7233-32b0-142371d519da.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__5b150bae-ce98-4ad1-9531-7b8caa5f3dd1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ZoneEquipmentHvacType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The type of zone equipment.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public enum ZoneEquipmentHvacType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ZoneEquipmentHvacType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ZoneEquipmentHvacType ``` |

# Members

| Member name | Description |
| --- | --- |
| Undefined |  |
| ChilledBeamActive |  |
| FourPipeFanCoil |  |
| PackagedTerminalAirConditioner |  |
| PackagedTerminalHeatPump |  |
| ParallelFanPoweredBox |  |
| VAVBox |  |
| CAVBox |  |
| RadiantPanel |  |
| SeriesFanPoweredBox |  |
| UnitHeater |  |
| UnitVentilator |  |
| WaterSourceHeatPump |  |
| ChilledBeamPassive |  |
| Unconditioned |  |
| VRFFanCoil |  |

# See Also

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__5b19788c-7d38-ce48-00a4-c4937e00854a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OpeningPartiallyCutsHost Property

---



|  |
| --- |
| [BuiltInFailures OpeningFailures Class](7857c588-1861-cfd1-1423-7b950a01aba1.htm)   [See Also](#seeAlsoToggle) |

Opening partially cuts its host.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId OpeningPartiallyCutsHost { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property OpeningPartiallyCutsHost As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ OpeningPartiallyCutsHost { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures OpeningFailures Class](7857c588-1861-cfd1-1423-7b950a01aba1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b1b694c-0977-23cb-1799-1264ffa4a3dd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reset Method

---



|  |
| --- |
| [ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)   [See Also](#seeAlsoToggle) |

Clears the accumulated geometry and resets other ViewShapeBuilder parameters to invalid values.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void Reset() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Reset ``` |

 

| Visual C++ |
| --- |
| ``` public: void Reset() ``` |

# See Also

[ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b1c116a-a1a9-c2a1-91fd-d96805d309ce.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateEqualsRule Method (ElementId, Double, Double)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether double-precision values from the document equal a certain value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateEqualsRule( 	ElementId parameter, 	double value, 	double epsilon ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateEqualsRule ( _ 	parameter As ElementId, _ 	value As Double, _ 	epsilon As Double _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateEqualsRule( 	ElementId^ parameter,  	double value,  	double epsilon ) ``` |

#### Parameters

parameter
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A double-typed parameter used to get values from the document for a given element.

value
:   Type:  System Double    
     The user-supplied value against which values from the document will be compared.

epsilon
:   Type:  System Double    
     Defines the tolerance within which two values may be considered equal.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for value is not finite -or- The given value for value is not a number -or- The given value for epsilon is not finite -or- The given value for epsilon is not a number |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)

[CreateEqualsRule Overload](0637b53b-96aa-7683-6535-8a1217c5809e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b1d6c9f-bc94-9dd1-76eb-2cdb3df34c0c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsWireNeutralMultiplierParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Neutral Multiplier"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsWireNeutralMultiplierParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsWireNeutralMultiplierParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsWireNeutralMultiplierParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b1e9dee-f52a-03ad-af80-733c7b9866eb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCoincidentMassZoneFaceReferences Method

---



|  |
| --- |
| [MassEnergyAnalyticalModel Class](1e8b2837-0572-d788-a6eb-db5060fc423c.htm)   [See Also](#seeAlsoToggle) |

Returns References to Faces from MassZones coincident with an input Face from a MassEnergyAnalyticalModel.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static IList<Reference> GetCoincidentMassZoneFaceReferences( 	Document document, 	Reference referenceToFace ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetCoincidentMassZoneFaceReferences ( _ 	document As Document, _ 	referenceToFace As Reference _ ) As IList(Of Reference) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<Reference^>^ GetCoincidentMassZoneFaceReferences( 	Document^ document,  	Reference^ referenceToFace ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document.

referenceToFace
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     A Reference to a Face of a MassEnergyAnalyticalModel.

#### Return Value

Returns References to Faces from MassZones coincident with an input Face from a MassEnergyAnalyticalModel.

# Remarks

The results are always References to Faces. The Reference Type should report as REFERENCE\_TYPE\_SURFACE. Currently Revit improperly reports it as REFERENCE\_TYPE\_NONE.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The Reference is not a Face of a MassEnergyAnalyticalModel. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MassEnergyAnalyticalModel Class](1e8b2837-0572-d788-a6eb-db5060fc423c.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__5b204fc8-7702-cf7e-346a-3a4c1767924b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IntersectWith Method

---



|  |
| --- |
| [FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)   [See Also](#seeAlsoToggle) |

Intersects the set of elements passing the filter in this collector with the set of elements passing the filter in another collector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FilteredElementCollector IntersectWith( 	FilteredElementCollector other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IntersectWith ( _ 	other As FilteredElementCollector _ ) As FilteredElementCollector ``` |

 

| Visual C++ |
| --- |
| ``` public: FilteredElementCollector^ IntersectWith( 	FilteredElementCollector^ other ) ``` |

#### Parameters

other
:   Type:  [Autodesk.Revit.DB FilteredElementCollector](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)    
     The other collector

#### Return Value

A handle to this collector. This is the same collector that has just been modified, returned so you can chain multiple calls together in one line.

# Remarks

The result will be the same as using a LogicalAndFilter to connect this filter with another. If you have an active iterator to this collector it will be stopped by this call.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The collector does not have a filter applied. Extraction or iteration of elements is not permitted without a filter. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The collector does not have a filter applied. Extraction or iteration of elements is not permitted without a filter. |

# See Also

[FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b20c5e2-9ee4-c3a9-0820-a7e370f104f9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [FabricReinSpanSymbol Class](ed051a39-7717-6be5-43a9-6f6598fd82f7.htm)   [See Also](#seeAlsoToggle) |

Places a new instance of the Structural Fabric Reinforcement Symbol into the project relative to a particular FabricSheet and View.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static FabricReinSpanSymbol Create( 	Document document, 	ElementId viewId, 	LinkElementId hostId, 	XYZ point, 	ElementId symbolId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	viewId As ElementId, _ 	hostId As LinkElementId, _ 	point As XYZ, _ 	symbolId As ElementId _ ) As FabricReinSpanSymbol ``` |

 

| Visual C++ |
| --- |
| ``` public: static FabricReinSpanSymbol^ Create( 	Document^ document,  	ElementId^ viewId,  	LinkElementId^ hostId,  	XYZ^ point,  	ElementId^ symbolId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

viewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the view in which the symbol should appear.

hostId
:   Type:  [Autodesk.Revit.DB LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)    
     The ElementId of FabricSheet (either in the document, or linked from another document).

point
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The span symbol's head position.

symbolId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the family symbol of this symbol.

#### Return Value

A reference to the newly-created symbol.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | hostId should refer to a FabricSheet element. -or- viewId does not refer to a valid view type for FabricReinSpanSymbol - only floor plan, reflected ceiling plans and elevations are permitted. -or- symbolId should refer to a FamilySymbol of category OST\_FabricReinSpanSymbol. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[FabricReinSpanSymbol Class](ed051a39-7717-6be5-43a9-6f6598fd82f7.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5b21cada-9846-35fa-0a1e-e661d3d916c0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Unlimited Property

---



|  |
| --- |
| [PlanViewRange Class](7edc5f13-a5fa-5c7a-9a03-ac6cbed1f005.htm)   [See Also](#seeAlsoToggle) |

View range is unlimited

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ElementId Unlimited { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Unlimited As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ElementId^ Unlimited { 	ElementId^ get (); } ``` |

# See Also

[PlanViewRange Class](7edc5f13-a5fa-5c7a-9a03-ac6cbed1f005.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b21fca4-97da-09bb-9f83-c26c0741940a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ServiceName Property

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

The name of the service associated with the fabrication part.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public string ServiceName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ServiceName As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ ServiceName { 	String^ get (); } ``` |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b2588f2-62a5-f395-33d9-8d75355bf0b6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LightingFixture Class

---



|  |
| --- |
| [Members](4a44c541-28f3-a6ff-68bc-cbbfa1e3978d.htm)   [See Also](#seeAlsoToggle) |

Provides access to the Lighting Fixture in Autodesk Revit MEP.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class LightingFixture : MEPModel ``` |

 

| Visual Basic |
| --- |
| ``` Public Class LightingFixture _ 	Inherits MEPModel ``` |

 

| Visual C++ |
| --- |
| ``` public ref class LightingFixture : public MEPModel ``` |

# Remarks

The Lighting Fixture object can only be queried in Autodesk Revit MEP.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  [Autodesk.Revit.DB MEPModel](dd78bce5-2ed6-ed3c-f329-1663bf08afa6.htm)    
  Autodesk.Revit.DB.Electrical LightingFixture

# See Also

[LightingFixture Members](4a44c541-28f3-a6ff-68bc-cbbfa1e3978d.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__5b25c3c6-3f83-95bf-b7c3-c868c431e0fa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLineWeight Method

---



|  |
| --- |
| [Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)   [See Also](#seeAlsoToggle) |

Retrieves the line weight assigned to the category for the given graphics style type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Nullable<int> GetLineWeight( 	GraphicsStyleType graphicsStyleType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLineWeight ( _ 	graphicsStyleType As GraphicsStyleType _ ) As Nullable(Of Integer) ``` |

 

| Visual C++ |
| --- |
| ``` public: Nullable<int> GetLineWeight( 	GraphicsStyleType graphicsStyleType ) ``` |

#### Parameters

graphicsStyleType
:   Type:  [Autodesk.Revit.DB GraphicsStyleType](60a5cce6-2cdc-dd63-e737-f584582ceeca.htm)    
     The type of graphics style.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the input argument-"graphicsStyleType"-is out of range. |

# See Also

[Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b264752-8085-3b07-18a9-4f5ab62ff03e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairstypeNotchHorizontalGap Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Horizontal Gap Distance":

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairstypeNotchHorizontalGap { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairstypeNotchHorizontalGap As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairstypeNotchHorizontalGap { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b2ccc42-7130-5d2c-38e8-b6e84a290b35.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Document Property

---



|  |
| --- |
| [ImporterIFC Class](87327a4b-94fd-5a21-df33-9beb1921cb4d.htm)   [See Also](#seeAlsoToggle) |

Gets the document associated with the import.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public Document Document { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Document As Document 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Document^ Document { 	Document^ get (); } ``` |

# See Also

[ImporterIFC Class](87327a4b-94fd-5a21-df33-9beb1921cb4d.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__5b2f204a-a2b7-b207-9d99-2073d3ddf779.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewerCropRegion Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Crop View"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ViewerCropRegion { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewerCropRegion As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ViewerCropRegion { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b3250ab-f70b-6f87-afbf-dd049a64c29e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportLineweightKey Class

---



|  |
| --- |
| [Members](1cf88c59-0eec-ccb1-b403-3417f0cebf50.htm)   [See Also](#seeAlsoToggle) |

A key used to represent an item stored in an  [ExportLineweightTable](5620708e-0c7c-ced6-9887-0237a9229800.htm)  .

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class ExportLineweightKey : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExportLineweightKey _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExportLineweightKey : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ExportLineweightKey

# See Also

[ExportLineweightKey Members](1cf88c59-0eec-ccb1-b403-3417f0cebf50.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b3663d8-9b7f-12de-d20a-895259bea9ac.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IncludeLastBar Property

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Identifies if the last bar in rebar set is shown.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public bool IncludeLastBar { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IncludeLastBar As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IncludeLastBar { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | This rebar element represents a single bar (the layout rule is Single). |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5b3927f6-7554-85f5-d860-be43520a9d61.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WhitePoint Property

---



|  |
| --- |
| [RenderingImageExposureSettings Class](94e2205c-ae49-e3a4-35e5-93d91f1bafb3.htm)   [See Also](#seeAlsoToggle) |

The white point value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double WhitePoint { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property WhitePoint As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double WhitePoint { 	double get (); 	void set (double value); } ``` |

# Remarks

Specify the white balance of the rendering(measured in Kelvin). Incandescent lighting:2800 K; Daylight 6500K.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The value of white point is not valid. The valid range is 1800 to 15000. |

# See Also

[RenderingImageExposureSettings Class](94e2205c-ae49-e3a4-35e5-93d91f1bafb3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b3e8e0a-4957-981d-9900-0847178f1d2f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidValue Method

---



|  |
| --- |
| [AssetPropertyList Class](8f1e901e-d1a6-e8f1-0e10-d8b28e0ad073.htm)   [See Also](#seeAlsoToggle) |

Check that value is valid.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public bool IsValidValue( 	IList<AssetProperty> value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidValue ( _ 	value As IList(Of AssetProperty) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidValue( 	IList<AssetProperty^>^ value ) ``` |

#### Parameters

value
:   Type:  System.Collections.Generic IList   [AssetProperty](7be89499-d011-ab43-4715-0ee6f9335970.htm)    
     The array of properties to validate.

#### Return Value

Returns true if the array of properties is valid, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Cannot check validity for a property not being edited in AppearanceAssetEditScope. |

# See Also

[AssetPropertyList Class](8f1e901e-d1a6-e8f1-0e10-d8b28e0ad073.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__5b406f92-7dc3-7946-d2e7-f35751038945.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetBorderAroundSchedule Method

---



|  |
| --- |
| [PanelScheduleData Class](d24fcc19-3240-8f07-68ca-ce7b62f7aac3.htm)   [See Also](#seeAlsoToggle) |

Adds a border around the schedule

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetBorderAroundSchedule( 	ElementId borderId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetBorderAroundSchedule ( _ 	borderId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetBorderAroundSchedule( 	ElementId^ borderId ) ``` |

#### Parameters

borderId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The border to set around the schedule

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PanelScheduleData Class](d24fcc19-3240-8f07-68ca-ce7b62f7aac3.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__5b40d8de-ea17-5bbd-6abd-80d7df3cfeb9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InstanceProfileNotMatchWithHostError Property

---



|  |
| --- |
| [BuiltInFailures MEPSupportFailures Class](fa184122-8900-646e-1cca-ff3ae7123be6.htm)   [See Also](#seeAlsoToggle) |

The [Symbol]'s profile does not match the host. Instances of [Symbol] will be deleted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId InstanceProfileNotMatchWithHostError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InstanceProfileNotMatchWithHostError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ InstanceProfileNotMatchWithHostError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPSupportFailures Class](fa184122-8900-646e-1cca-ff3ae7123be6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b4e4948-c5f0-1e38-d461-7353561774e8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReferenceArrayIterator Class

---



|  |
| --- |
| [Members](9b01c5d3-28fe-6b68-2d8c-af147738bc4a.htm)   [See Also](#seeAlsoToggle) |

An iterator to a reference array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public abstract class ReferenceArrayIterator : APIObject,  	IEnumerator ``` |

 

| Visual Basic |
| --- |
| ``` Public MustInherit Class ReferenceArrayIterator _ 	Inherits APIObject _ 	Implements IEnumerator ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ReferenceArrayIterator abstract : public APIObject,  	IEnumerator ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB ReferenceArrayIterator

# See Also

[ReferenceArrayIterator Members](9b01c5d3-28fe-6b68-2d8c-af147738bc4a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b4f569e-097d-d878-1052-30a3123779a9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallMeetsRoofTangentially Property

---



|  |
| --- |
| [BuiltInFailures WallJoinRoofFailures Class](b752987a-9e5b-5ea8-be98-faf22647b6f7.htm)   [See Also](#seeAlsoToggle) |

The highlighted wall cannot be joined to the highlighted roof because the wall meets the roof tangentially.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId WallMeetsRoofTangentially { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WallMeetsRoofTangentially As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ WallMeetsRoofTangentially { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures WallJoinRoofFailures Class](b752987a-9e5b-5ea8-be98-faf22647b6f7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b50abdd-b0d3-df6b-82de-e6901da52ac9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Kilojoules Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Kilojoules.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Kilojoules { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Kilojoules As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Kilojoules { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b557a04-b06c-893d-dabf-c0e18d64fc42.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeStirrupTieAttachment Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Stirrup/Tie Attachment"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarShapeStirrupTieAttachment { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarShapeStirrupTieAttachment As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarShapeStirrupTieAttachment { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b5eca12-3510-a86b-e8ef-e76c20b4f01d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDone Method

---



|  |
| --- |
| [ComponentRepeaterIterator Class](d2bc2d9c-ae40-4e5e-a56a-9e5e8e7057cf.htm)   [See Also](#seeAlsoToggle) |

Identifies if the iteration has completed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public virtual bool IsDone() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function IsDone As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool IsDone() ``` |

#### Return Value

True if the iteration has no more items. False if there are more items to be iterated.

# See Also

[ComponentRepeaterIterator Class](d2bc2d9c-ae40-4e5e-a56a-9e5e8e7057cf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b5f1e73-8f56-538d-138d-05d7143bb055.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [LightType Class](42c83d85-60cd-52c3-7b97-b89e81d7d9fe.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
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

[LightType Class](42c83d85-60cd-52c3-7b97-b89e81d7d9fe.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__5b62432d-4486-5df5-fc6a-1b2387924d64.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StirrupTieBendDiameter Property

---



|  |
| --- |
| [RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)   [See Also](#seeAlsoToggle) |

Defines bar and hook bend diameter for rebar whose style is stirrup/tie

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double StirrupTieBendDiameter { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property StirrupTieBendDiameter As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double StirrupTieBendDiameter { 	double get (); 	void set (double value); } ``` |

#### Field Value

The bar and hook bend diameter for rebar whose style is stirrup/tie

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: the bend diameter stirrupTieBendDiam isn't between bar diameter and 99.0 |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5b6cf262-3ac4-5892-3b00-7ff599b38afc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Common Property

---



|  |
| --- |
| [DisciplineTypeId Class](1f44ffd1-9851-60b4-2754-e82d785bad40.htm)   [See Also](#seeAlsoToggle) |

Common.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Common { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Common As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Common { 	ForgeTypeId^ get (); } ``` |

# See Also

[DisciplineTypeId Class](1f44ffd1-9851-60b4-2754-e82d785bad40.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b71bce4-f161-6f8c-48dd-96f745990157.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Lookup Method

---



|  |
| --- |
| [FabricationPartType Class](261b8995-37db-ad23-9ae6-929cb0a77122.htm)   [See Also](#seeAlsoToggle) |

Looks up an existing fabrication part type based on a specfic fabrication service button and condition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static ElementId Lookup( 	Document document, 	FabricationServiceButton button, 	int condition ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Lookup ( _ 	document As Document, _ 	button As FabricationServiceButton, _ 	condition As Integer _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ Lookup( 	Document^ document,  	FabricationServiceButton^ button,  	int condition ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

button
:   Type:  [Autodesk.Revit.DB FabricationServiceButton](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)    
     The fabrication service button.

condition
:   Type:  System Int32    
     The condition index.

#### Return Value

Identifier of the fabrication part type element or invalidElementId if no fabrication part type exist for the specific fabrication service button and condition

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the index condition is not larger or equal to 0 and less than ConditionCount |

# See Also

[FabricationPartType Class](261b8995-37db-ad23-9ae6-929cb0a77122.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b738d41-b620-a2b4-d8bf-008ea34532ac.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveNext Method

---



|  |
| --- |
| [ElementArrayIterator Class](fc1af4a8-d97f-da4e-97bd-d97061977360.htm)   [See Also](#seeAlsoToggle) |

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

[ElementArrayIterator Class](fc1af4a8-d97f-da4e-97bd-d97061977360.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b743cdd-3049-e09f-aaf4-3a1d6f5c1745.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NoFittingInProjectError Property

---



|  |
| --- |
| [BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)   [See Also](#seeAlsoToggle) |

The routing solution failed because there is no default fitting type specified or the fitting cannot be found in the project. Ensure the fitting is loaded in the project and try again.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NoFittingInProjectError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NoFittingInProjectError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NoFittingInProjectError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b761477-a851-2662-8d78-c4ba3909b3de.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalModelColumnTopExtension Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top x Projection"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnalyticalModelColumnTopExtension { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticalModelColumnTopExtension As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnalyticalModelColumnTopExtension { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b772943-2d9b-f145-eaf0-7a7c138aae05.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaterialParamTransparency Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Transparency"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MaterialParamTransparency { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MaterialParamTransparency As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MaterialParamTransparency { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b78eda1-9ad6-9c9d-bfe4-bdb6752c262f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetMinimumNumberOfDigits Method

---



|  |
| --- |
| [NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)   [See Also](#seeAlsoToggle) |

Sets a new value for the minimum number of digits to be used for formating the Number parameter of all numbered elements of the given document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static void SetMinimumNumberOfDigits( 	Document document, 	int value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SetMinimumNumberOfDigits ( _ 	document As Document, _ 	value As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SetMinimumNumberOfDigits( 	Document^ document,  	int value ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which the new value will be in applied.

value
:   Type:  System Int32    
     New value for the minimum number of digits.

# Remarks

Valid values range from 1 to 10. Numbers with fewer digits than the minimum number will be padded with leading zeros.

The value affects all numbering schemas. Thus, once set, numbers for Rebar and Reinforcement Fabric will be formatted with the same minimum number of digits.

The current value can obtained by invoking the  [GetMinimumNumberOfDigits(Document)](80ac3f63-6383-ba62-380f-0e61b98e8dd7.htm)  method.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The minimum number of digits must be in range from 1 to 10. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b7a1f72-6095-4137-9838-a7b6564624f4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetInapplicableParameters Method

---



|  |
| --- |
| [ParameterFilterUtilities Class](50afdc29-3a0c-e3d9-c547-0fcdb40d3ce8.htm)   [See Also](#seeAlsoToggle) |

Returns the parameters that are not among the set of filterable parameters common to the given categories.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static IList<ElementId> GetInapplicableParameters( 	Document aDoc, 	ICollection<ElementId> categories, 	IList<ElementId> parameters ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetInapplicableParameters ( _ 	aDoc As Document, _ 	categories As ICollection(Of ElementId), _ 	parameters As IList(Of ElementId) _ ) As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<ElementId^>^ GetInapplicableParameters( 	Document^ aDoc,  	ICollection<ElementId^>^ categories,  	IList<ElementId^>^ parameters ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the categories and parameters to query.

categories
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The categories that define the set of possibly filterable parameters.

parameters
:   Type:  System.Collections.Generic IList   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The parameters desired for use in a parameter filter.

#### Return Value

A list of parameters from the given array that are not valid for use in a parameter filter with the given categories.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterUtilities Class](50afdc29-3a0c-e3d9-c547-0fcdb40d3ce8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b7ab8d0-bd8d-f834-5d2e-a2504d3a91ce.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FlexPipeType Property

---



|  |
| --- |
| [FlexPipe Class](4b0e0656-4760-4a91-a777-ce50869a827a.htm)   [See Also](#seeAlsoToggle) |

The flex pipe type of this flex pipe.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FlexPipeType FlexPipeType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FlexPipeType As FlexPipeType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property FlexPipeType^ FlexPipeType { 	FlexPipeType^ get (); 	void set (FlexPipeType^ value); } ``` |

# See Also

[FlexPipe Class](4b0e0656-4760-4a91-a777-ce50869a827a.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__5b7b6a05-44d9-5552-0ee2-5df84232fa13.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCutJoinedElement Property

---



|  |
| --- |
| [BuiltInFailures CutFailures Class](6bec436a-fefb-b90c-454f-ce494f3b06c5.htm)   [See Also](#seeAlsoToggle) |

Can't cut joined element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCutJoinedElement { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCutJoinedElement As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCutJoinedElement { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CutFailures Class](6bec436a-fefb-b90c-454f-ce494f3b06c5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b80b774-9bd3-10be-5524-f5eb0460c8d9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ExternalResourceLoadData Class](e2156349-e735-775f-8cfa-4eaa6bda9f3b.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ExternalResourceLoadData](e2156349-e735-775f-8cfa-4eaa6bda9f3b.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

[ExternalResourceLoadData Class](e2156349-e735-775f-8cfa-4eaa6bda9f3b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b80ebe4-b085-5851-b412-0ad1dd5025bf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAllDisciplines Method

---



|  |
| --- |
| [UnitUtils Class](128dd879-fea8-5d7b-1eb2-d64f87753990.htm)   [See Also](#seeAlsoToggle) |

Gets the identifiers of all available disciplines.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static IList<ForgeTypeId> GetAllDisciplines() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetAllDisciplines As IList(Of ForgeTypeId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<ForgeTypeId^>^ GetAllDisciplines() ``` |

#### Return Value

The discipline identifiers.

# See Also

[UnitUtils Class](128dd879-fea8-5d7b-1eb2-d64f87753990.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b8669c5-0c9a-756d-6a30-d465bc043dae.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetEnumerator Method

---



|  |
| --- |
| [ProjectLocationSet Class](f61b39ab-704a-8981-419f-c2f64521f181.htm)   [See Also](#seeAlsoToggle) |

Retrieve a forward moving iterator to the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual IEnumerator GetEnumerator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function GetEnumerator As IEnumerator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual IEnumerator^ GetEnumerator() ``` |

#### Return Value

Returns a forward moving iterator to the set.

#### Implements

 [IEnumerable GetEnumerator](http://msdn2.microsoft.com/en-us/library/5zae5365)

# See Also

[ProjectLocationSet Class](f61b39ab-704a-8981-419f-c2f64521f181.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b886218-356e-0e03-4c77-f4d08a62386d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurtainMullionn1 Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Grid 1 Mullions"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CurtainMullionn1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CurtainMullionn1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CurtainMullionn1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b8babd9-cef5-c666-ddb0-7e048e2a8a19.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPointIterator Method

---



|  |
| --- |
| [PointCollection Class](3eaab06f-0da5-dd0a-6063-b3907f6de7a8.htm)   [See Also](#seeAlsoToggle) |

Creates and returns an iterator for the points contained in this collection.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public PointIterator GetPointIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPointIterator As PointIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: PointIterator^ GetPointIterator() ``` |

#### Return Value

New iterator created, make sure to call 'free' on it when finished using it.

# See Also

[PointCollection Class](3eaab06f-0da5-dd0a-6063-b3907f6de7a8.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__5b8c2d9e-c136-f63f-3596-6a8a383fd798.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsTreadsRisers Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Threads/Risers"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsTreadsRisers { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsTreadsRisers As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsTreadsRisers { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b90c02e-8b63-cd76-5951-fbb60327a420.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetColor Method

---



|  |
| --- |
| [VertexPositionColored Class](f99deacd-3167-46ff-6abf-5d27bdbd2c6a.htm)   [See Also](#seeAlsoToggle) |

Sets the vertex's color.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetColor( 	ColorWithTransparency color ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetColor ( _ 	color As ColorWithTransparency _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetColor( 	ColorWithTransparency^ color ) ``` |

#### Parameters

color
:   Type:  [Autodesk.Revit.DB ColorWithTransparency](b68f80e1-5ea0-a485-ec3e-7dd077043230.htm)    
     The vertex's color.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[VertexPositionColored Class](f99deacd-3167-46ff-6abf-5d27bdbd2c6a.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__5b91bd1f-ec3b-d31f-4e0a-6c532990bfca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PipeFittingAndAccessoryPressureDropCalculatorNotAvailable Property

---



|  |
| --- |
| [BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)   [See Also](#seeAlsoToggle) |

Pipe Fitting/Accessory Pressure Drop Calculator Not Available: [Calculator Name]

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId PipeFittingAndAccessoryPressureDropCalculatorNotAvailable { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PipeFittingAndAccessoryPressureDropCalculatorNotAvailable As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ PipeFittingAndAccessoryPressureDropCalculatorNotAvailable { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b93b125-c1f4-ad4c-6f51-e87b322f82a5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasDoubleWallConnector Method

---



|  |
| --- |
| [FabricationConnectorInfo Class](5da97d87-a3f6-f239-3c5c-102d2d82f942.htm)   [See Also](#seeAlsoToggle) |

Checks if there are any double wall connectors fabricated.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool HasDoubleWallConnector() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function HasDoubleWallConnector As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool HasDoubleWallConnector() ``` |

#### Return Value

True if there are any double wall connectors fabricated.

# See Also

[FabricationConnectorInfo Class](5da97d87-a3f6-f239-3c5c-102d2d82f942.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b944368-4ce5-d523-5fd5-29d0363861ae.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateFromIFC Method

---



|  |
| --- |
| [RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)   [See Also](#seeAlsoToggle) |

Creates a new Revit link type from an existing Revit file created via import by reference of an asscoiated IFC file.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static LinkLoadResult CreateFromIFC( 	Document document, 	string ifcFilePath, 	string revitLinkedFilePath, 	bool recreateLink, 	RevitLinkOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateFromIFC ( _ 	document As Document, _ 	ifcFilePath As String, _ 	revitLinkedFilePath As String, _ 	recreateLink As Boolean, _ 	options As RevitLinkOptions _ ) As LinkLoadResult ``` |

 

| Visual C++ |
| --- |
| ``` public: static LinkLoadResult^ CreateFromIFC( 	Document^ document,  	String^ ifcFilePath,  	String^ revitLinkedFilePath,  	bool recreateLink,  	RevitLinkOptions^ options ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to create the Revit link.

ifcFilePath
:   Type:  System String    
     The path of the associated IFC file. This must be a full path.

revitLinkedFilePath
:   Type:  System String    
     The path of the existing Revit file that contains elements created via an import by reference operation. This must be a full path.

recreateLink
:   Type:  System Boolean    
     If true, the existing Revit file created via an import by reference operation will be updated based on the information in the IFC file. If false, the existing Revit file will be used as-is.

options
:   Type:  [Autodesk.Revit.DB RevitLinkOptions](3f710983-5a4d-d515-a633-12b06a419b30.htm)    
     An options class for loading Revit links.

#### Return Value

An object containing the results of creating and loading the Revit link type. It contains the ElementId of the new link.

# Remarks

This function is one of a series of steps necessary for linking an IFC file. To understand how it is used in context, please download the IFC open source code, and look in the Revit.IFC.Import project at Importer.ImportIFC(ImporterIFC importer), under the IFCImportAction.Link branch.

This function regenerates the input document. While the options argument allows specification of a path type, the input path argument must be a full path. Relative vs. absolute determines how Revit will store the path, but it needs a complete path to find the linked document initially.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- The input path "ifcFilePath" does not represent an IFC file. -or- document already contains a linked model at path revitLinkedFilePath. -or- The document is a cloud model. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileAccessException](187d56d7-0b37-699f-2abd-6ddebfa93f1e.htm) | The model cannot be accessed due to lack of access privileges. |
| [Autodesk.Revit.Exceptions FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | There is not a valid Revit file at ifcFilePath's location -or- There is not a valid Revit file at revitLinkedFilePath's location |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The file is not allowed to access. -or- Revit cannot customize worksets for this model. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)

[CreateFromIFC Overload](45ca28bf-edd4-4726-43a9-62c71356cba6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b991fda-55b5-9d0f-25e2-e9fe6ad89a2f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionIshapeWebthickness Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Web Thickness"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralSectionIshapeWebthickness { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralSectionIshapeWebthickness As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralSectionIshapeWebthickness { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5b9b34c5-9e7b-1b20-54a9-572a6459a075.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsNumberSystemReferenceOption Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The reference types permitted for a number system to refer to the geometry of a stairs run.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum StairsNumberSystemReferenceOption ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration StairsNumberSystemReferenceOption ``` |

 

| Visual C++ |
| --- |
| ``` public enum class StairsNumberSystemReferenceOption ``` |

# Members

| Member name | Description |
| --- | --- |
| Center | The number system reference to stairs path. |
| Left | The number system reference to left boundary of stairs. |
| Right | The number system reference to right boundary of stairs. |
| LeftQuarter | The number system reference to left quarter of stairs |
| RightQuarter | The number system reference to right quarter of stairs |

# See Also

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__5b9d7c92-9468-9b47-3340-0e850fae2e23.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DoubleArrayIterator Constructor

---



|  |
| --- |
| [DoubleArrayIterator Class](29cad534-21a2-82c0-2859-0279f3367166.htm)   [See Also](#seeAlsoToggle) |

For Internal Use Only.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public DoubleArrayIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: DoubleArrayIterator() ``` |

# Remarks

This constructor is exposed to enable support for COM interop only. This object should never be created by the developer.

# See Also

[DoubleArrayIterator Class](29cad534-21a2-82c0-2859-0279f3367166.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ba5320b-8200-5d21-e5b2-2e08cb72c709.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProfileCurveLoopCount Property

---



|  |
| --- |
| [Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)   [See Also](#seeAlsoToggle) |

The number of curve loops in certain profile, specified by profile index.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int this[ 	int index ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ProfileCurveLoopCount ( _ 	index As Integer _ ) As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int ProfileCurveLoopCount[int index] { 	int get (int index); } ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index to specify the profile, should be within 0 and (ProfileCount - 1).

# See Also

[Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ba58430-ab72-cf13-a942-4f43873ad9c6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecPanelTotalestloadParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Total Estimated Demand"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecPanelTotalestloadParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecPanelTotalestloadParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecPanelTotalestloadParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ba825fb-fa63-50db-ae7c-0b6fc54a68bf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WoodUseLatewoodBump Property

---



|  |
| --- |
| [AdvancedWood Class](1e8c37ad-69ea-aabc-df91-eda9c7fe54ff.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Use latewood bump" from the "AdvancedWood" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string WoodUseLatewoodBump { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WoodUseLatewoodBump As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ WoodUseLatewoodBump { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyBoolean".

# See Also

[AdvancedWood Class](1e8c37ad-69ea-aabc-df91-eda9c7fe54ff.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__5bab696d-a8bc-1bf4-67f1-ca6b9b064812.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCreateOpenMiddleStringers Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Can't cut open/middle stringers geometry.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCreateOpenMiddleStringers { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCreateOpenMiddleStringers As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCreateOpenMiddleStringers { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bae121e-96b0-8c54-6419-8f6252aba6d5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureRealWorldOffsetZ Property

---



|  |
| --- |
| [Marble Class](729b243c-c4ee-64bd-f482-7164ab4dcffc.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Offset Z" from the "Marble" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TextureRealWorldOffsetZ { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextureRealWorldOffsetZ As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TextureRealWorldOffsetZ { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDistance".

# See Also

[Marble Class](729b243c-c4ee-64bd-f482-7164ab4dcffc.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__5bae32ca-edb3-80b4-e809-50cb7e0e720d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Custom Property

---



|  |
| --- |
| [MultipleValuesIndicationSettings Class](f23f984b-7cbf-54be-b2b9-a7069adaa339.htm)   [See Also](#seeAlsoToggle) |

If true,  [CustomValue](c1d337d1-c676-cdd5-0945-bb60c0b1d2ee.htm)  is used as multiple values indication, otherwise a hardcoded standard value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public bool Custom { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Custom As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool Custom { 	bool get (); 	void set (bool value); } ``` |

# See Also

[MultipleValuesIndicationSettings Class](f23f984b-7cbf-54be-b2b9-a7069adaa339.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5baf8951-9e05-5a7d-a507-ec2a0161d3da.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalResourceTypes Class

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in ExternalResourceType instances.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class ExternalResourceTypes ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class ExternalResourceTypes ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExternalResourceTypes abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ExternalResourceTypes

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bb1f156-f5c1-a87c-e212-c16ff20f639a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AutoPanel Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Curtain Panel"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AutoPanel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AutoPanel As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AutoPanel { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bb46529-85cf-18d8-d8ec-9b77c3b78f88.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionsServiceData Class

---



|  |
| --- |
| [Members](ecb7772d-d8c2-13eb-504f-2fa598f4ad20.htm)   [See Also](#seeAlsoToggle) |

The data needed by section type server to perform type definition.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class StructuralSectionsServiceData : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class StructuralSectionsServiceData _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class StructuralSectionsServiceData : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Structure StructuralSectionsServiceData

# See Also

[StructuralSectionsServiceData Members](ecb7772d-d8c2-13eb-504f-2fa598f4ad20.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5bb6c5f5-27af-9f63-503d-20a2fa9556fa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpecificHeat Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Specific Heat, in discipline Energy.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpecificHeat { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpecificHeat As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpecificHeat { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bb6d514-66ec-24a5-8560-7bdd92a6b766.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [CameraInfo Class](facf52cc-bc82-0008-9e4c-60e6a335ef40.htm)   [See Also](#seeAlsoToggle) |

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

[CameraInfo Class](facf52cc-bc82-0008-9e4c-60e6a335ef40.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bb8f467-d26c-449d-9031-ba072fcb48b4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDefaultFamilyTypeIdValid Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Checks whether the family type id is valid for the give family category.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool IsDefaultFamilyTypeIdValid( 	ElementId familyCategoryId, 	ElementId familyTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsDefaultFamilyTypeIdValid ( _ 	familyCategoryId As ElementId, _ 	familyTypeId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsDefaultFamilyTypeIdValid( 	ElementId^ familyCategoryId,  	ElementId^ familyTypeId ) ``` |

#### Parameters

familyCategoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The family category id.

familyTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The default family type id.

#### Return Value

True if the family type id is valid for the give family category, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bbb8498-1f18-0cf3-eef6-f4aca5327291.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CheckerSoften Property

---



|  |
| --- |
| [Checker Class](ff4ecb34-6fef-402a-5cee-c7937974b8d2.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Soften" from the "Checker" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string CheckerSoften { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CheckerSoften As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ CheckerSoften { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble" within the range of "0, 5".

# See Also

[Checker Class](ff4ecb34-6fef-402a-5cee-c7937974b8d2.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__5bbbca1e-5577-1ce0-6d74-01809d084d21.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDesignOptionId Method

---



|  |
| --- |
| [ElementRecord Class](d0b04b59-347d-a34a-3127-053985ff2674.htm)   [See Also](#seeAlsoToggle) |

Gets the design option id of the element record.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElementId GetDesignOptionId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDesignOptionId As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetDesignOptionId() ``` |

#### Return Value

The design option id.

# See Also

[ElementRecord Class](d0b04b59-347d-a34a-3127-053985ff2674.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bbd827f-37de-bfd5-de3f-ecac0179eb3b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Element Property

---



|  |
| --- |
| [Alignment Class](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)   [See Also](#seeAlsoToggle) |

The underlying  [DirectShape](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.htm)  element.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public Element Element { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Element As Element 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Element^ Element { 	Element^ get (); } ``` |

# See Also

[Alignment Class](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)

<!-- Start of Syntax__5bbed76e-f811-b98b-288a-6f74aa2b0f2c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RectangularDuctSizeSeparator Property

---



|  |
| --- |
| [DuctSettings Class](cd632c8e-a520-2efb-a417-9dfa5677d134.htm)   [See Also](#seeAlsoToggle) |

The rectangular duct size separator string.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public string RectangularDuctSizeSeparator { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RectangularDuctSizeSeparator As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ RectangularDuctSizeSeparator { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[DuctSettings Class](cd632c8e-a520-2efb-a417-9dfa5677d134.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__5bc2e2e4-cdf8-18ad-d910-31f5fe400b74.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnpostFailure Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Deletes the posted failure message associated with a given FailureMessageKey.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void UnpostFailure( 	FailureMessageKey messageKey ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub UnpostFailure ( _ 	messageKey As FailureMessageKey _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void UnpostFailure( 	FailureMessageKey^ messageKey ) ``` |

#### Parameters

messageKey
:   Type:  [Autodesk.Revit.DB FailureMessageKey](f0fa1b40-5df3-ddaf-e38d-85bd438a89e3.htm)    
     The key of the FailureMessage to be deleted.

# Remarks

If code that previously has posted a failure is executed again or otherwise detects that failure conditions do not exist anymore and the failure is not longer relevant, it should delete a failure message in order to let transaction to be committed. In order to delete the failure, it should invoke this method with a message key that was returned when the failure was posted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | messageKey is invalid |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bd5286a-612f-e12f-e200-6a8763bb2aee.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FilterStringRule Constructor (FilterableValueProvider, FilterStringRuleEvaluator, String)

---



|  |
| --- |
| [FilterStringRule Class](166d75f9-1088-3275-2219-867c1142d8da.htm)   [See Also](#seeAlsoToggle) |

Constructs an instance of FilterStringRule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public FilterStringRule( 	FilterableValueProvider valueProvider, 	FilterStringRuleEvaluator evaluator, 	string ruleString ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	valueProvider As FilterableValueProvider, _ 	evaluator As FilterStringRuleEvaluator, _ 	ruleString As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: FilterStringRule( 	FilterableValueProvider^ valueProvider,  	FilterStringRuleEvaluator^ evaluator,  	String^ ruleString ) ``` |

#### Parameters

valueProvider
:   Type:  [Autodesk.Revit.DB FilterableValueProvider](50829fa2-03f1-9d4b-a3cd-2935d3bf8a8c.htm)    
     A pointer to a "value provider" object that will extract values from a Revit document.

evaluator
:   Type:  [Autodesk.Revit.DB FilterStringRuleEvaluator](ba8dad25-3f85-1fbb-a164-323c3750018c.htm)    
     A pointer to the filter rule evaluator object that implements the desired test. The built-in evaluators implement commonly used tests for strings such as begins-with, ends-with, contains, equal, etc.

ruleString
:   Type:  System String    
     The user-supplied string against which strings from a Revit document will be tested.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FilterStringRule Class](166d75f9-1088-3275-2219-867c1142d8da.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bd545da-3d76-7293-6a31-ada090d08b1e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [SlabShapeCreaseArray Class](dbb7004c-920c-74ce-bde2-834d46b0c132.htm)   [See Also](#seeAlsoToggle) |

Removes every item from the array, rendering it empty.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
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

[SlabShapeCreaseArray Class](dbb7004c-920c-74ce-bde2-834d46b0c132.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bdae35f-f688-519e-6f13-64515ad8e384.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDone Method

---



|  |
| --- |
| [MacroModuleIterator Class](320b8746-c7b2-797a-6764-babdf0c79715.htm)   [See Also](#seeAlsoToggle) |

Identifies if the iteration has completed.

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPIMacros  (in RevitAPIMacros.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public virtual bool IsDone() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function IsDone As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool IsDone() ``` |

#### Return Value

True if the iteration has no more items. False if there are more items to be iterated.

# See Also

[MacroModuleIterator Class](320b8746-c7b2-797a-6764-babdf0c79715.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)

<!-- Start of Syntax__5bdafcc3-2ade-3169-83f4-40cd75f42b90.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BaseFinishingTurns Property

---



|  |
| --- |
| [RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)   [See Also](#seeAlsoToggle) |

For a spiral, the number of finishing turns at the lower end of the spiral.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public int BaseFinishingTurns { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BaseFinishingTurns As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int BaseFinishingTurns { 	int get (); 	void set (int value); } ``` |

# Remarks

Applies only to instances where RebarShape.Definition is of type RebarShapeDefinitionByArc, and its Type property is equal to the value RebarShapeDefinitionByArcType.Spiral.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: turns must be between 0 and 100. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RebarShapeDrivenAccessor is not an instance of a spiral shape. -or- This RebarShapeDrivenAccessor doesn't contain a valid rebar reference. |

# See Also

[RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5bdcec64-1c38-33a6-e5ec-3a906b59fda5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TemperatureRatingTypeSetIterator Constructor

---



|  |
| --- |
| [TemperatureRatingTypeSetIterator Class](1164738d-a4b8-2868-492d-c34b63c94815.htm)   [See Also](#seeAlsoToggle) |

For Internal Use Only.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public TemperatureRatingTypeSetIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: TemperatureRatingTypeSetIterator() ``` |

# Remarks

This constructor is exposed to enable support for COM interop only. This object should never be created by the developer.

# See Also

[TemperatureRatingTypeSetIterator Class](1164738d-a4b8-2868-492d-c34b63c94815.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__5be67985-96f3-4dc4-2f97-6ce9f3b61649.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FormElemRegenSelfIntersectionResetConnections Property

---



|  |
| --- |
| [BuiltInFailures FormFailures Class](2d71ddb7-b11f-3d2b-8f8e-c3771b131b7a.htm)   [See Also](#seeAlsoToggle) |

This form cannot be created due to self-intersecting geometry. Clicking the Reset Connections button will attempt to solve this problem.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FormElemRegenSelfIntersectionResetConnections { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FormElemRegenSelfIntersectionResetConnections As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FormElemRegenSelfIntersectionResetConnections { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FormFailures Class](2d71ddb7-b11f-3d2b-8f8e-c3771b131b7a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5beafb2e-8863-6602-7c5f-38daa3a69a81.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectPipePlaceholdersAtElbow Method (Document, Connector, Connector)

---



|  |
| --- |
| [PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.htm)   [See Also](#seeAlsoToggle) |

Connects placeholders that looks like elbow connection.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool ConnectPipePlaceholdersAtElbow( 	Document document, 	Connector connector1, 	Connector connector2 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ConnectPipePlaceholdersAtElbow ( _ 	document As Document, _ 	connector1 As Connector, _ 	connector2 As Connector _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ConnectPipePlaceholdersAtElbow( 	Document^ document,  	Connector^ connector1,  	Connector^ connector2 ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

connector1
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The first end connector of placeholder to be connected to.

connector2
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The second end connector of placeholder to be connected to.

#### Return Value

True if connection succeeds, false otherwise.

# Remarks

The placeholders may have physical connection or may not connect at all. In the latter case, the first one connects to the end of second one. If connection fails, the placeholders cannot be physically connected.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The owner of connector is not pipe placeholder. -or- The owners of connectors belong to different types of system. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.htm)

[ConnectPipePlaceholdersAtElbow Overload](7c2063f9-d469-1e24-2eb9-602d96a8b635.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__5beef120-3918-7a2e-3ec4-d20445899e40.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsTranslation Property

---



|  |
| --- |
| [Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)   [See Also](#seeAlsoToggle) |

The boolean value that indicates whether this transformation is a translation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public bool IsTranslation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsTranslation As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsTranslation { 	bool get (); } ``` |

# Remarks

This property is true if the only effect of transformation is translation. It checks that the linear part of the transform is identity. The translation vector may be zero (which would make this an identity transformation) or nonzero (which would make this a non-trivial translation).

# See Also

[Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bef06b9-9257-9fd6-d6ca-01fc9d0f5f9e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateGreaterOrEqualRule Method (ElementId, Int32)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether integer values from the document are greater than or equal to a certain value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateGreaterOrEqualRule( 	ElementId parameter, 	int value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateGreaterOrEqualRule ( _ 	parameter As ElementId, _ 	value As Integer _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateGreaterOrEqualRule( 	ElementId^ parameter,  	int value ) ``` |

#### Parameters

parameter
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     An integer-typed parameter used to get values from the document for a given element.

value
:   Type:  System Int32    
     The user-supplied value against which values from the document will be compared.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)

[CreateGreaterOrEqualRule Overload](14d42cfa-d1e6-d955-f2d6-6cabd71679c0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bef94a2-0891-3db6-45ab-210cc0d55e35.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalysisDisplayMarkersAndTextSettings Constructor

---



|  |
| --- |
| [AnalysisDisplayMarkersAndTextSettings Class](bb940def-7483-32c6-01cb-1c79e6666290.htm)   [See Also](#seeAlsoToggle) |

Constructs a default instance of markers and text settings.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public AnalysisDisplayMarkersAndTextSettings() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: AnalysisDisplayMarkersAndTextSettings() ``` |

# See Also

[AnalysisDisplayMarkersAndTextSettings Class](bb940def-7483-32c6-01cb-1c79e6666290.htm)

[AnalysisDisplayMarkersAndTextSettings Overload](da6cac08-c86c-20f2-9fbf-cddec88fe041.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__5bf35b73-6d40-9c5b-9f0b-de7763bc0b83.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WorksetHasChangedInCentralFile Property

---



|  |
| --- |
| [BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)   [See Also](#seeAlsoToggle) |

This workset has changed in the Central Model. Please Reload Latest before making this workset editable.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId WorksetHasChangedInCentralFile { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WorksetHasChangedInCentralFile As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ WorksetHasChangedInCentralFile { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bfdd63e-7f73-b15a-bab9-57f6f3ca6064.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ActualRiserHeightChanged Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

The actual riser height for one or more stairs violates the maximum set in the type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ActualRiserHeightChanged { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ActualRiserHeightChanged As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ActualRiserHeightChanged { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5bffa9a5-a459-5bb0-2f75-3723560cbe3f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Tf Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol Tf, indicating unit Tonnes force.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Tf { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Tf As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Tf { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c027e93-1dff-9a6e-8602-5b3a3da60ada.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumberSystem Class

---



|  |
| --- |
| [Members](88c7fd64-07ae-7385-ef0b-e911224cd663.htm)   [See Also](#seeAlsoToggle) |

An annotation that consists of a series of numeric tags attached to and describing a host element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class NumberSystem : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class NumberSystem _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class NumberSystem : public Element ``` |

# Remarks

For a component-based stair, you can display tread/riser numbers for a run in plan, elevation, or section view. Sketch-based stair is not supported.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB NumberSystem

# See Also

[NumberSystem Members](88c7fd64-07ae-7385-ef0b-e911224cd663.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c02aea5-6258-4801-e7ba-4865e3eae2d9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StoneBumpAmount Property

---



|  |
| --- |
| [Stone Class](b7458faa-8242-d2b7-44a5-7df042a67ac3.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Amount" from the "Stone" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string StoneBumpAmount { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StoneBumpAmount As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ StoneBumpAmount { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble" within the range of "0, 1".

# See Also

[Stone Class](b7458faa-8242-d2b7-44a5-7df042a67ac3.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__5c041522-2f60-8034-15a6-b7a53743a9b5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsAttrRiserMaterial Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Riser Material"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsAttrRiserMaterial { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsAttrRiserMaterial As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsAttrRiserMaterial { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c042f62-87f2-98b1-e7b8-4fc2ebbe0a54.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationLevelParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Reference Level"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FabricationLevelParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationLevelParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FabricationLevelParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c064e7c-4fc6-035f-7c35-3e6a735e552f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidForSaveToProjectAsImage Method

---



|  |
| --- |
| [ImageExportOptions Class](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.htm)   [See Also](#seeAlsoToggle) |

Verify if ImageExportOptions object is valid for calling saveToProjectAsImage

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static bool IsValidForSaveToProjectAsImage( 	ImageExportOptions options, 	Document doc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidForSaveToProjectAsImage ( _ 	options As ImageExportOptions, _ 	doc As Document _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidForSaveToProjectAsImage( 	ImageExportOptions^ options,  	Document^ doc ) ``` |

#### Parameters

options
:   Type:  [Autodesk.Revit.DB ImageExportOptions](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.htm)    
     ImageExportOptions object to be validated

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document for view name verification

#### Return Value

True if ImageExportOptions object is valid for calling saveToProjectAsImage; false otherwise

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ImageExportOptions Class](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c108c6c-7446-66f3-5551-7427409186d2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### KipPerFt Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol kip/ft, indicating unit Kips per foot.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId KipPerFt { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property KipPerFt As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ KipPerFt { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c154b53-f671-12c3-05eb-96c70ca62744.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CfmPerFtSup2 Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol CFM/ftÂ², indicating unit Cubic feet per minute square foot.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CfmPerFtSup2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CfmPerFtSup2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CfmPerFtSup2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c15c70b-d3e2-cc7a-0e6b-e9b2aa90890a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EnergyAnalysisMasszoneDivideperimeter Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Perimeter Zone Division"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId EnergyAnalysisMasszoneDivideperimeter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property EnergyAnalysisMasszoneDivideperimeter As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ EnergyAnalysisMasszoneDivideperimeter { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c174925-079f-53f6-70cb-f9d3870d3fc7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### YJustification Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"y Justification"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId YJustification { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property YJustification As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ YJustification { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c189fd7-6881-976e-5ab1-ffd349c67ef3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Item Property

---



|  |
| --- |
| [CategoryNameMap Class](d452bf69-eef2-2d6c-1e8d-cc059c0fe513.htm)   [See Also](#seeAlsoToggle) |

Gets or sets a category at a specified name within the map.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual Category this[ 	string key ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Property Item ( _ 	key As String _ ) As Category 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property Category^ Item[String^ key] { 	Category^ get (String^ key); 	void set (String^ key, Category^ value); } ``` |

#### Parameters

key
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The name of the category to be set or retrieved.

#### Return Value

Returns the category at the specified name.

# See Also

[CategoryNameMap Class](d452bf69-eef2-2d6c-1e8d-cc059c0fe513.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c1a86f8-8c09-6186-6a4c-3fe0bb9c5034.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Params Property

---



|  |
| --- |
| [HermiteFace Class](cc020c7b-e36a-7e30-c227-28dbbd520b2d.htm)   [See Also](#seeAlsoToggle) |

Parameters of the surface.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public DoubleArray this[ 	int index ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Params ( _ 	index As Integer _ ) As DoubleArray 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property DoubleArray^ Params[int index] { 	DoubleArray^ get (int index); } ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

# See Also

[HermiteFace Class](cc020c7b-e36a-7e30-c227-28dbbd520b2d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c1c2ef6-f1e5-3e37-ab49-dce1d2502f0c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Fy Property

---



|  |
| --- |
| [ReleaseConditions Class](f742770e-6b65-f237-5851-ccdf16cfc1b5.htm)   [See Also](#seeAlsoToggle) |

Gets or Sets the Fy of the release type.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public bool Fy { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Fy As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool Fy { 	bool get (); 	void set (bool value); } ``` |

# See Also

[ReleaseConditions Class](f742770e-6b65-f237-5851-ccdf16cfc1b5.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5c1cb742-5936-bba2-85df-dfa09bbcd372.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [AnalyticalEquipmentLoadData Class](f0db67d1-7fe9-6ada-8e0a-f51614751edd.htm)   [See Also](#seeAlsoToggle) |

The current of the analytical equipment load.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public double Current { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Current As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Current { 	double get (); } ``` |

# See Also

[AnalyticalEquipmentLoadData Class](f0db67d1-7fe9-6ada-8e0a-f51614751edd.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__5c1e1b04-67ed-7e6a-22da-181b5062d6a4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InDashWgPer100ft Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol in-wg/100ft, indicating unit Inches of water (60 Â°F) per 100 feet.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId InDashWgPer100ft { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InDashWgPer100ft As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ InDashWgPer100ft { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c1ed572-e744-3ab6-9b10-bb258a66f23a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Room Property (Phase)

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Room this[ 	Phase phase ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Room ( _ 	phase As Phase _ ) As Room 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Room^ Room[Phase^ phase] { 	Room^ get (Phase^ phase); } ``` |

#### Parameters

phase
:   Type:  [Autodesk.Revit.DB Phase](ab01f390-a8e8-c21c-b2d0-6dd21056cdec.htm)

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Room Overload](6044a7f3-bf19-498b-2724-c1458429423c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c1fd73a-5d75-e003-200a-5378e55512ca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NotEnoughPointsInSurface Property

---



|  |
| --- |
| [BuiltInFailures SiteFailures Class](7ab66d74-f1ab-17f6-9ecf-e51b3d5326bf.htm)   [See Also](#seeAlsoToggle) |

The surface must have at least three distinct Points.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NotEnoughPointsInSurface { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NotEnoughPointsInSurface As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NotEnoughPointsInSurface { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SiteFailures Class](7ab66d74-f1ab-17f6-9ecf-e51b3d5326bf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c20fe58-e301-6ddb-3438-666db5c586ee.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DesignOption Property

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Returns the design option to which the element belongs.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public DesignOption DesignOption { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property DesignOption As DesignOption 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property DesignOption^ DesignOption { 	DesignOption^ get (); } ``` |

# Remarks

If the element is not in a design option, i.e. in the main model, then this property will return    a null reference (  Nothing  in Visual Basic)  .

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
void Getinfo_DesignOption(Document document)
{
    // Get the selected Elements in the Active Document
    UIDocument uidoc = new UIDocument(document);
    ICollection<ElementId> selectedIds = uidoc.Selection.GetElementIds();

    foreach (ElementId id in selectedIds)
    {
        Element element = document.GetElement(id);
        //Use the DesignOption property of Element
        if (element.DesignOption != null)
        {
            TaskDialog.Show("Revit",element.DesignOption.Name.ToString());
        }
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub Getinfo_DesignOption(document As Document)
    ' Get the selected Elements in the Active Document
    Dim uidoc As New UIDocument(document)
    Dim selectedIds As ICollection(Of ElementId) = uidoc.Selection.GetElementIds()

    For Each id As ElementId In selectedIds
        Dim element As Element = document.GetElement(id)
        'Use the DesignOption property of Element
        If element.DesignOption IsNot Nothing Then
            TaskDialog.Show("Revit", element.DesignOption.Name.ToString())
        End If
    Next
End Sub
```

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c22d48b-59b3-2599-7c7a-83257cddf0df.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateRibbonPanel Method (String, String)

---



|  |
| --- |
| [UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)   [See Also](#seeAlsoToggle) |

Create a new RibbonPanel on the specified tab.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual RibbonPanel CreateRibbonPanel( 	string tabName, 	string panelName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function CreateRibbonPanel ( _ 	tabName As String, _ 	panelName As String _ ) As RibbonPanel ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual RibbonPanel^ CreateRibbonPanel( 	String^ tabName,  	String^ panelName ) ``` |

#### Parameters

tabName
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The name of the tab, on which the new panel will be created.

panelName
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The name of the panel to be created.

# Remarks

This method will create a custom panel appending to the specified tab. This method is not supported in Macros.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | tabName or panelName is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | tabName or panelName is Empty. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Too many panels have been added to this tab (Maximum is 100). |

# See Also

[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)

[CreateRibbonPanel Overload](f10d6cf3-0e12-ccaa-e368-e32eef3ec088.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__5c246fe4-cefa-37da-1bb1-1aa2e39b3c60.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VersionGUID Property

---



|  |
| --- |
| [DocumentVersion Class](3574fa56-016e-b146-1499-b3b1c9129705.htm)   [See Also](#seeAlsoToggle) |

The GUID portion of the DocumentVersion. The GUID is updated when changes are made to the document, but may not update with every change to the document. The GUID and save number are both necessary to uniquely identify a document version.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public Guid VersionGUID { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property VersionGUID As Guid 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Guid VersionGUID { 	Guid get (); } ``` |

# See Also

[DocumentVersion Class](3574fa56-016e-b146-1499-b3b1c9129705.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c274484-2617-79e2-8593-9af4c70f8a59.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetJournalData Method

---



|  |
| --- |
| [ExecutedEventArgs Class](701d2fb4-1402-e2f7-6e09-d4cb955ee7da.htm)   [See Also](#seeAlsoToggle) |

Sets the journal data associated to this command (on journal playback).

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetJournalData( 	IDictionary<string, string> data ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetJournalData ( _ 	data As IDictionary(Of String, String) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetJournalData( 	IDictionary<String^, String^>^ data ) ``` |

#### Parameters

data
:   Type:  [System.Collections.Generic IDictionary](http://msdn2.microsoft.com/en-us/library/s4ys34ea)   [String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)  ,  [String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

# Remarks

For details about the use of journal data associated to a command, see ExternalCommandData.JournalData.

# See Also

[ExecutedEventArgs Class](701d2fb4-1402-e2f7-6e09-d4cb955ee7da.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__5c28c137-8545-8ab2-e104-1da715b3e483.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RailingNotConnectedError Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

The Railing line must be a single connected Sketch. If you want separate pieces of Railing, create two or more separate Railings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RailingNotConnectedError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RailingNotConnectedError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RailingNotConnectedError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c2aa975-9b44-f5b8-bf9b-519deeb015b4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateFailureDefinition Method

---



|  |
| --- |
| [FailureDefinition Class](b0c061b0-d712-0c41-6054-b8ce8f996256.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates an instance of a FailureDefinition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FailureDefinition CreateFailureDefinition( 	FailureDefinitionId id, 	FailureSeverity severity, 	string messageString ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateFailureDefinition ( _ 	id As FailureDefinitionId, _ 	severity As FailureSeverity, _ 	messageString As String _ ) As FailureDefinition ``` |

 

| Visual C++ |
| --- |
| ``` public: static FailureDefinition^ CreateFailureDefinition( 	FailureDefinitionId^ id,  	FailureSeverity severity,  	String^ messageString ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.DB FailureDefinitionId](b6ada360-a6fe-ebb6-b095-d74b37ade9bf.htm)    
     Unique identifier of the failure.

severity
:   Type:  [Autodesk.Revit.DB FailureSeverity](d0cdffe3-22c5-b764-8090-5104f044b000.htm)    
     The severity of the failure. Cannot be FailureSeverity::None.

messageString
:   Type:  System String    
     A user-visible string describing the failure.

#### Return Value

The created FailureDefinition instance.

# Remarks

The newly created FailureDefinition will be added to the FailureDefinitionRegistry. Because FailureDefinition could only be registered when Revit starting up, this function cannot be used after Revit has already started. Throws InvalidOperationException if invoked after Revit start-up is completed.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// define a new failure id for a warning about walls
FailureDefinitionId warnId = 
    new FailureDefinitionId(new Guid("FB4F5AF3-42BB-4371-B559-FB1648D5B4D1"));

// register the new warning using FailureDefinition
FailureDefinition failDef = FailureDefinition.CreateFailureDefinition(warnId, 
    FailureSeverity.Warning, 
    "Wall is too big (>100'). Performance problems may result.");
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' define a new failure id for a warning about walls
Dim warnId As New FailureDefinitionId(New Guid("FB4F5AF3-42BB-4371-B559-FB1648D5B4D1"))

' register the new warning using FailureDefinition
Dim failDef As FailureDefinition = FailureDefinition.CreateFailureDefinition(warnId, FailureSeverity.Warning, "Wall is too big (>100'). Performance problems may result.")
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The id of failure definition is not valid. -or- The id of failure definition is already used to register another FailureDefinition. -or- The severity of failures cannot be FailureSeverity::None. -or- Message string is empty or contains invalid characters. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[FailureDefinition Class](b0c061b0-d712-0c41-6054-b8ce8f996256.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c2ae0de-d9d0-5f2b-1bcc-2e2f544163f1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetObjectData Method

---



|  |
| --- |
| [InvalidOperationException Class](9e715f03-3884-e539-4dd6-8d7545733adc.htm)   [See Also](#seeAlsoToggle) |

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

[InvalidOperationException Class](9e715f03-3884-e539-4dd6-8d7545733adc.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__5c2bf291-537e-0de1-4982-87a7e20c217a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetShape Method

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

Builds the type shape from the supplied collection of GeometryObjects. The objects are copied. If the new shape is identical to the old one, the old shape will be kept.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void SetShape( 	IList<GeometryObject> pGeomArr ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetShape ( _ 	pGeomArr As IList(Of GeometryObject) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetShape( 	IList<GeometryObject^>^ pGeomArr ) ``` |

#### Parameters

pGeomArr
:   Type:  System.Collections.Generic IList   [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
     Shape of this object expressed as a collection of GeometryObjects. These will be copied. Shape and Category should be consistent: geometry supplied as shape should be valid for the Category the type object is associated with. The supported types of GeometryObjects are: Solid, Mesh, GeometryInstance, Point, Curve and PolyLine.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | At least one member of pGeomArr does not satisfy DirectShapeType validation criteria. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[SetShape Overload](a2008089-b24d-a663-c1a7-6c8d877ef4ce.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c2c3e95-ae6e-f303-a770-662acf186181.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OwnerInfo Property

---



|  |
| --- |
| [TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)   [See Also](#seeAlsoToggle) |

String used for logging, if any. Usually describes the element or object, which either defined or will own the geoemtrical objects to be built.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public string OwnerInfo { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property OwnerInfo As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ OwnerInfo { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c2f17c8-6be8-b344-74fd-1d5c47cf7bca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidSectionType Method

---



|  |
| --- |
| [TableView Class](ba608411-21af-e924-2aa2-3595548ab39f.htm)   [See Also](#seeAlsoToggle) |

Identifies if the section type is valid for this view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsValidSectionType( 	SectionType sectionType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidSectionType ( _ 	sectionType As SectionType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidSectionType( 	SectionType sectionType ) ``` |

#### Parameters

sectionType
:   Type:  [Autodesk.Revit.DB SectionType](ad9a6cf0-aa1a-d011-b399-658345721aab.htm)    
     The section type.

#### Return Value

True if the Section Type is valid, false otherwise.

# Remarks

Some TableViews do not contain all of the possible section types. For example, standard schedules have only a Heading and Body.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[TableView Class](ba608411-21af-e924-2aa2-3595548ab39f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c30ebed-0bf6-ec46-a932-054f57db2df2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsCurveDiameterParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Diameter"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsCurveDiameterParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsCurveDiameterParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsCurveDiameterParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c33a711-2891-f353-5f39-24ba175be452.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CombineElements Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Combine a set of combinable elements into a geometry combination.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public GeomCombination CombineElements( 	CombinableElementArray members ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CombineElements ( _ 	members As CombinableElementArray _ ) As GeomCombination ``` |

 

| Visual C++ |
| --- |
| ``` public: GeomCombination^ CombineElements( 	CombinableElementArray^ members ) ``` |

#### Parameters

members
:   Type:  [Autodesk.Revit.DB CombinableElementArray](dc5f6afb-a30d-dc82-fcd3-340eff1685c7.htm)    
     A list of combinable elements to be combined.

#### Return Value

If successful, the newly created geometry combination is returned, otherwise an exception with error information will be thrown.

# Remarks

If one or more existing geometry combinations are included as input, the return value may be one of those pre-existing combinations. The rest of the pre-existing geometry combinations will be consumed into the new combination; those handles are no longer valid.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when members contains less than two elements. Thrown when members contains    a null reference (  Nothing  in Visual Basic)  elements. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when creation of the combination failed. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c37fcb1-0aee-c188-71dc-ab1cb3da072d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SquareInchesPerFoot Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Square inches per foot.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SquareInchesPerFoot { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SquareInchesPerFoot As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SquareInchesPerFoot { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c3c90a6-699d-b6cf-44f7-405986d13073.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ZoneEquipmentData Class

---



|  |
| --- |
| [Members](a96f7951-53b7-5462-435b-87a19ebe2c76.htm)   [See Also](#seeAlsoToggle) |

Represents the data and parameters of analytical zone equipment.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public class ZoneEquipmentData : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ZoneEquipmentData _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ZoneEquipmentData : IDisposable ``` |

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB.Mechanical ZoneEquipmentData

# See Also

[ZoneEquipmentData Members](a96f7951-53b7-5462-435b-87a19ebe2c76.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__5c42f213-1bd5-bcb0-acbe-0997d0609574.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Add Method

---



|  |
| --- |
| [ExportLinetypeTable Class](136c6197-2f4c-5686-e70c-09cee48b71ad.htm)   [See Also](#seeAlsoToggle) |

Inserts a (key, info) pair into Export line type table.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void Add( 	ExportLinetypeKey exportLinetypeKey, 	ExportLinetypeInfo exportLinetypeInfo ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Add ( _ 	exportLinetypeKey As ExportLinetypeKey, _ 	exportLinetypeInfo As ExportLinetypeInfo _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Add( 	ExportLinetypeKey^ exportLinetypeKey,  	ExportLinetypeInfo^ exportLinetypeInfo ) ``` |

#### Parameters

exportLinetypeKey
:   Type:  [Autodesk.Revit.DB ExportLinetypeKey](7f67a1c8-cc9b-9b17-aa87-664657ee9d7d.htm)    
     The export line type Key to be added.

exportLinetypeInfo
:   Type:  [Autodesk.Revit.DB ExportLinetypeInfo](f7ae5495-2fe3-02be-a803-873ab4b97aa6.htm)    
     The export line type info to be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The key already exists in the table. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportLinetypeTable Class](136c6197-2f4c-5686-e70c-09cee48b71ad.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c4367bd-eb48-b634-2b9a-bfaba9c3a5ca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Volume Property

---



|  |
| --- |
| [RebarInSystem Class](c0bd03fa-78f4-eb67-54e8-e28368e94beb.htm)   [See Also](#seeAlsoToggle) |

The volume of an individual bar multiplied by Quantity.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double Volume { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Volume As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Volume { 	double get (); } ``` |

# See Also

[RebarInSystem Class](c0bd03fa-78f4-eb67-54e8-e28368e94beb.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5c43fb93-bf62-2011-1303-9c50d6a47632.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PipeFlowConfigurationType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all connector flow configuration

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum PipeFlowConfigurationType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration PipeFlowConfigurationType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class PipeFlowConfigurationType ``` |

# Members

| Member name | Description |
| --- | --- |
| Calculated | Flow configuration is calculated |
| Preset | Flow configuration is Preset |
| System | Flow configuration depends on system |
| Demand | Flow configuration depends on demand |

# See Also

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__5c454c40-9624-28b2-6e9a-1cf4e03b94d6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [FilterableValueProvider Class](50829fa2-03f1-9d4b-a3cd-2935d3bf8a8c.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [FilterableValueProvider](50829fa2-03f1-9d4b-a3cd-2935d3bf8a8c.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

[FilterableValueProvider Class](50829fa2-03f1-9d4b-a3cd-2935d3bf8a8c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c470551-dd56-fb62-40a6-0cb2d65b04b4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [WorksharingDisplayGraphicSettings Class](994d2fb5-11cc-6756-155b-d496eedbe800.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [WorksharingDisplayGraphicSettings](994d2fb5-11cc-6756-155b-d496eedbe800.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

[WorksharingDisplayGraphicSettings Class](994d2fb5-11cc-6756-155b-d496eedbe800.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c48beb7-a81a-605f-da5e-0778274c7671.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecPanelFeedThruLugsCurrentPhasec Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Feed Through Lugs Current Phase C"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecPanelFeedThruLugsCurrentPhasec { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecPanelFeedThruLugsCurrentPhasec As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecPanelFeedThruLugsCurrentPhasec { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c4a3c78-b527-31c8-aeb8-b9d51c2b56e4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddAllSegments Method

---



|  |
| --- |
| [CurtainGridLine Class](42c94f55-1972-5f12-1dd4-db15ad1af3d3.htm)   [See Also](#seeAlsoToggle) |

All the segments on this grid line will be added.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void AddAllSegments() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddAllSegments ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddAllSegments() ``` |

# See Also

[CurtainGridLine Class](42c94f55-1972-5f12-1dd4-db15ad1af3d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c4e3445-11c4-c260-930c-8bf8451c21ad.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetDirectContext3DHandleSettings Method

---



|  |
| --- |
| [DirectContext3DHandleOverrides Class](8bef65c6-70bc-1a10-a9a4-47c8ec2cd842.htm)   [See Also](#seeAlsoToggle) |

Assigns override settings associated with a DirectContext3D handle instance or type.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void SetDirectContext3DHandleSettings( 	Document aDoc, 	ElementId elementId, 	DirectContext3DHandleSettings newSettings ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetDirectContext3DHandleSettings ( _ 	aDoc As Document, _ 	elementId As ElementId, _ 	newSettings As DirectContext3DHandleSettings _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetDirectContext3DHandleSettings( 	Document^ aDoc,  	ElementId^ elementId,  	DirectContext3DHandleSettings^ newSettings ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document where elementId resides.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of the element to be overridden.

newSettings
:   Type:  [Autodesk.Revit.DB.DirectContext3D DirectContext3DHandleSettings](cc9d7b07-a4d9-8570-9ed8-c953e241c0d6.htm)    
     The override settings to be assigned to the handle element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The ElementId elementId is not a valid DirectContext3D handle instance or type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectContext3DHandleOverrides Class](8bef65c6-70bc-1a10-a9a4-47c8ec2cd842.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlignmentStationLabel Class

---



|  |
| --- |
| [Members](c1e852d4-7674-3c96-1330-c4feb39a3a72.htm)   [See Also](#seeAlsoToggle) |

Represents an object which provides access to a specialized Revit annotation element used for labeling  [Alignment](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)  stations.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public class AlignmentStationLabel ``` |

 

| Visual Basic |
| --- |
| ``` Public Class AlignmentStationLabel ``` |

 

| Visual C++ |
| --- |
| ``` public ref class AlignmentStationLabel ``` |

# Remarks

The element is a  [SpotDimension](f3c633ac-1595-cb8d-5c1b-66eb3eefb433.htm)  . The element's category is  [OST\_AlignmentStationLabels](ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.htm)  or, if in a set of labels,  [OST\_AlignmentStationLabelSets](ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.htm)  . The element's type is a  [SpotDimensionType](06ffc197-308a-a350-6dd7-6f812e175bb6.htm)  with  [DimensionStyleType](130b0264-615d-610e-38e0-4ce2a8e2aecd.htm)  equal to  [AlignmentStationLabel](130b0264-615d-610e-38e0-4ce2a8e2aecd.htm)  . The element's  [Origin](df8b9dc6-9d36-ac2b-04cf-816d88f039b8.htm)  is a point on the tessellated representation of an alignment. To get the precise point on the alignment's curve, use  [GetPointAtStation(Double)](1b4cc73b-dc00-0439-5480-fd7979b1e106.htm)  with input obtained from  [Station](1558579e-cdee-03ca-58b1-5630fe0fa0c1.htm)  .

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB.Infrastructure AlignmentStationLabel

# See Also

[AlignmentStationLabel Members](c1e852d4-7674-3c96-1330-c4feb39a3a72.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)

<!-- Start of Syntax__5c5562cc-c39c-e800-b8a1-4861ba2c13b7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [InitialIntensity Class](557d9e25-430a-2f92-3dbc-c9ec84e07900.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
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

[InitialIntensity Class](557d9e25-430a-2f92-3dbc-c9ec84e07900.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__5c573cf3-7ff8-49a1-7b8e-f78fe2709ea8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetDistanceToTargetCover Method

---



|  |
| --- |
| [RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)   [See Also](#seeAlsoToggle) |

Sets the distance from the RebarConstrainedHandle to the target Host Cover Element surface. The RebarConstraintType of the RebarConstraint must be 'ToCover.'

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void SetDistanceToTargetCover( 	double distanceToTargetCover ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetDistanceToTargetCover ( _ 	distanceToTargetCover As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetDistanceToTargetCover( 	double distanceToTargetCover ) ``` |

#### Parameters

distanceToTargetCover
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The distance is given as an offset value, the sign of which depends on Host Cover direction.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for distanceToTargetCover must be no more than 30000 feet in absolute value. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | RebarConstraint is no longer valid. -or- The RebarConstraint is not of RebarConstraintType 'ToCover.' |

# See Also

[RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5c578e87-b296-0676-2e52-12862fd1ad0d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddVertex Method

---



|  |
| --- |
| [VertexStreamPositionNormalColored Class](2b52610e-fbc2-d983-d28c-6fd05a7a215e.htm)   [See Also](#seeAlsoToggle) |

Inserts a  [VertexStreamPositionNormalColored](2b52610e-fbc2-d983-d28c-6fd05a7a215e.htm)  into the stream and associated buffer.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void AddVertex( 	VertexPositionNormalColored vertex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddVertex ( _ 	vertex As VertexPositionNormalColored _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddVertex( 	VertexPositionNormalColored^ vertex ) ``` |

#### Parameters

vertex
:   Type:  [Autodesk.Revit.DB.DirectContext3D VertexPositionNormalColored](aa354e03-2b25-b5a4-5634-c3518518c0d3.htm)    
     The vertex to be inserted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if the associated buffer is not mapped. -or- Thrown if the associated buffer has insufficient space. |

# See Also

[VertexStreamPositionNormalColored Class](2b52610e-fbc2-d983-d28c-6fd05a7a215e.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__5c588f69-25c7-b65f-ac2f-25c870437ca4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Function Property

---



|  |
| --- |
| [FunctionId Class](f510babd-969e-98fd-530e-c58fe4c9e5ca.htm)   [See Also](#seeAlsoToggle) |

The name of the function throwing an exception.

**Namespace:**   [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public string Function { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Function As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Function { 	String^ get (); } ``` |

# See Also

[FunctionId Class](f510babd-969e-98fd-530e-c58fe4c9e5ca.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__5c58ac2c-7cf7-3fe1-dab4-7749c1b5a055.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DefaultFamilyType Property

---



|  |
| --- |
| [ComponentRepeater Class](27dbc5bd-40e7-c044-11e6-7053adf92c6f.htm)   [See Also](#seeAlsoToggle) |

The default family type for the component repeater.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ElementId DefaultFamilyType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DefaultFamilyType As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ DefaultFamilyType { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

The default family type is the type of the instances in default slots. This includes slots that are added when the repeater grows. When setting this property, all slots with instances of the default type will change their components to an instance of the new default type. Empty slots will remain unchanged. Slots with non-default family instances will remain unchanged.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: Invalid type for the repeater. The type must be an adaptive family with no shape handles. In addition, it must have same category and same number of placement points as the current type of the repeater. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ComponentRepeater Class](27dbc5bd-40e7-c044-11e6-7053adf92c6f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c5ad800-7512-be12-dc1a-ebcda5513622.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MergeElbows Property

---



|  |
| --- |
| [IndependentTag Class](e52073e2-9d98-6fb5-eb43-288cf9ed2e28.htm)   [See Also](#seeAlsoToggle) |

Identifies if the leaders' elbows are merged or not. If they are are merged, all elbows are in the same point and they move together.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public bool MergeElbows { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MergeElbows As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool MergeElbows { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: For this tag leaders are not allowed. -or- When setting this property: Can't merge elbows for tags that are part of a multi-reference annotation. |

# See Also

[IndependentTag Class](e52073e2-9d98-6fb5-eb43-288cf9ed2e28.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c5f1d32-0df7-6c62-edb2-31758a0654f0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Rename Method

---



|  |
| --- |
| [ViewSheetSetting Class](e85ce148-ef47-7640-1864-6035b6773411.htm)   [See Also](#seeAlsoToggle) |

Rename the current view sheet set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool Rename( 	string newName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Rename ( _ 	newName As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Rename( 	String^ newName ) ``` |

#### Parameters

newName
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     View sheet set name to be renamed as.

#### Return Value

False if Rename operation fails, otherwise True.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the input name is already existed in current view sheet set list. |

# See Also

[ViewSheetSetting Class](e85ce148-ef47-7640-1864-6035b6773411.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c6052e1-ed1f-4785-d54f-17b7f53b01dc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionTopCutWidth Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top Cut Width"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralSectionTopCutWidth { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralSectionTopCutWidth As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralSectionTopCutWidth { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c606162-9576-0790-78dd-a5bffd83a1ef.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewId Property

---



|  |
| --- |
| [PreviewControl Class](50112279-5c9d-0351-bbd1-698e76be9e36.htm)   [See Also](#seeAlsoToggle) |

The view Id.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId ViewId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ViewId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ViewId { 	ElementId^ get (); } ``` |

# See Also

[PreviewControl Class](50112279-5c9d-0351-bbd1-698e76be9e36.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__5c621413-d7ad-a3cd-f165-eb21ceb5580d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [PointCollection Class](3eaab06f-0da5-dd0a-6063-b3907f6de7a8.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
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

[PointCollection Class](3eaab06f-0da5-dd0a-6063-b3907f6de7a8.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__5c649267-6475-9a7b-4ca5-0986bd8c8800.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ModelTextType Property

---



|  |
| --- |
| [ModelText Class](3a51d58c-3e29-b641-e8bb-4d8a17c31527.htm)   [See Also](#seeAlsoToggle) |

The type for the model text.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ModelTextType ModelTextType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ModelTextType As ModelTextType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ModelTextType^ ModelTextType { 	ModelTextType^ get (); 	void set (ModelTextType^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when    a null reference (  Nothing  in Visual Basic)  is assigned to this property. |

# See Also

[ModelText Class](3a51d58c-3e29-b641-e8bb-4d8a17c31527.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c6c9daf-4547-01f1-9ba8-39a970ca9e68.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationPartJustification Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Fabrication part eccentric justifications for alignment for flat edged parts.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public enum FabricationPartJustification ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration FabricationPartJustification ``` |

 

| Visual C++ |
| --- |
| ``` public enum class FabricationPartJustification ``` |

# Members

| Member name | Description |
| --- | --- |
| Middle | Default middle justification to the connector |
| Bottom | Outside edge justification to the bottom |
| Top | Outside edge justification to the top |

# See Also

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)

<!-- Start of Syntax__5c6d36f6-8c0d-1570-07aa-3cabb05b268a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TriangulatedSolidOrShell Class

---



|  |
| --- |
| [Members](7a7bb7d2-f442-ecef-5517-c16ea67d9fbe.htm)   [See Also](#seeAlsoToggle) |

This class represents a triangulated solid or shell.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class TriangulatedSolidOrShell : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class TriangulatedSolidOrShell _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class TriangulatedSolidOrShell : IDisposable ``` |

# Remarks

The triangulation consists of a number of TriangulatedShellComponents. For a solid, there will be one TriangulatedShellComponent for each component of the solid's boundary. For example, a solid cube has just one boundary component (containing six faces), so there will be just one TriangulatedShellComponent. A solid consisting of two disjoint cubes has two boundary components (the boundaries of the two cubes), so there will be two TriangulatedShellComponents. A solid consisting of a sphere with a round void (or hole) inside it also has two boundary components (the outer sphere and the inner sphere), so there will be two TriangulatedShellComponents.

For a shell, there will be one TriangulatedShellComponent for each component of the shell.

Note that this class does not contain information on the containment structure of the boundary components of a solid.

Be careful not to confuse the components of a solid with the solid's boundary components. This class deals only with the boundary components.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB TriangulatedSolidOrShell

# See Also

[TriangulatedSolidOrShell Members](7a7bb7d2-f442-ecef-5517-c16ea67d9fbe.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c6dfd11-3bb4-8d71-0b82-9147ca6d52a3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DistanceToCutMark Property

---



|  |
| --- |
| [StairsPathType Class](36994970-3d80-62a3-df6f-381d38f2eda0.htm)   [See Also](#seeAlsoToggle) |

The distance from the stairs path arrow to cut mark.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double DistanceToCutMark { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DistanceToCutMark As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double DistanceToCutMark { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for distanceToCutMark must be between 0 and 30000 feet. |

# See Also

[StairsPathType Class](36994970-3d80-62a3-df6f-381d38f2eda0.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__5c70f0d8-1a1c-e850-eb69-52d36070eba9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [SelectionFilterElement Class](b0aaf230-e034-8466-c1e4-1d91e7162d19.htm)   [See Also](#seeAlsoToggle) |

Creates a new SelectionFilterElement in the given document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static SelectionFilterElement Create( 	Document document, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	name As String _ ) As SelectionFilterElement ``` |

 

| Visual C++ |
| --- |
| ``` public: static SelectionFilterElement^ Create( 	Document^ document,  	String^ name ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to create the SelectionFilterElement.

name
:   Type:  System String    
     The name for the new SelectionFilterElement.

#### Return Value

The new SelectionFilterElement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name is an empty string or contains only whitespace. -or- name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". -or- The given value for name is already in use as a filter element name. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SelectionFilterElement Class](b0aaf230-e034-8466-c1e4-1d91e7162d19.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c71f259-82a2-7c4a-dadb-b822271442bd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PoundsMass Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Pounds mass.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PoundsMass { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PoundsMass As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PoundsMass { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c72f0d1-a411-a0dc-9254-45aac63a2a2a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMappedHandle Method

---



|  |
| --- |
| [VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)   [See Also](#seeAlsoToggle) |

Gets a handle to the buffer's memory that has been mapped. Writing data to the buffer using the handle is an alternative to using stream objects.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public IntPtr GetMappedHandle() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMappedHandle As IntPtr ``` |

 

| Visual C++ |
| --- |
| ``` public: IntPtr GetMappedHandle() ``` |

#### Return Value

The handle to the mapped memory or nullptr when the buffer is not mapped.

# See Also

[VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__5c73d2f2-c7c4-fbcb-881d-2603a268dcf8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralBeamCutbackForColumn Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Beam cutback in plan"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralBeamCutbackForColumn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralBeamCutbackForColumn As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralBeamCutbackForColumn { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c74eaa0-bca8-10a8-a901-78de4111477b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StartStation Property

---



|  |
| --- |
| [AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.htm)   [See Also](#seeAlsoToggle) |

The starting station for creating labels in the set, in Revit internal model units (standard Imperial feet). The default value is null. When null, the station value corresponding to the alignment's  [DisplayedStartStation](0a17ad4e-4a52-a955-c1af-882e2123bf49.htm)  is used.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public Nullable<double> StartStation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property StartStation As Nullable(Of Double) 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Nullable<double> StartStation { 	Nullable<double> get (); 	void set (Nullable<double> value); } ``` |

# See Also

[AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)

<!-- Start of Syntax__5c7871e8-778c-3c08-58c0-97a8d01bd308.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextDistToLine Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Text Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TextDistToLine { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextDistToLine As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TextDistToLine { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c7c33a6-8c2b-05e2-7088-3199f1a26e34.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalDataInstanceRemovingFromDocumentEventArgs Class

---



|  |
| --- |
| [Members](953d88a0-6bb3-13ad-1100-b0e8cee15aa2.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by the ExternalDataInstanceRemovingFrom event.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public class ExternalDataInstanceRemovingFromDocumentEventArgs : RevitAPIPreDocEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExternalDataInstanceRemovingFromDocumentEventArgs _ 	Inherits RevitAPIPreDocEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExternalDataInstanceRemovingFromDocumentEventArgs : public RevitAPIPreDocEventArgs ``` |

# Inheritance Hierarchy

System Object    
  System EventArgs    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPreEventArgs](14097470-c9d9-0143-dc1b-b93a60a460e6.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPreDocEventArgs](ef0073c4-f86b-64b9-12f2-268f4e1b8bbe.htm)    
  Autodesk.Revit.DB.Events ExternalDataInstanceRemovingFromDocumentEventArgs

# See Also

[ExternalDataInstanceRemovingFromDocumentEventArgs Members](953d88a0-6bb3-13ad-1100-b0e8cee15aa2.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__5c7cd324-0c8b-e60e-617a-d9d594f40b4d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InaccurateGrid Property

---



|  |
| --- |
| [BuiltInFailures InaccurateFailures Class](1cd8eae9-aab1-2808-fbaa-b95bdf9ff3eb.htm)   [See Also](#seeAlsoToggle) |

Grid is slightly off axis and may cause inaccuracies.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId InaccurateGrid { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InaccurateGrid As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ InaccurateGrid { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures InaccurateFailures Class](1cd8eae9-aab1-2808-fbaa-b95bdf9ff3eb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c818638-328f-555e-a668-674d9f585775.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentSaveToCentralProgressChangedEventArgs Class

---



|  |
| --- |
| [Members](4f1a7763-d33e-6ffd-5988-3cd22878f18e.htm)   [See Also](#seeAlsoToggle) |

The event arguments used during the save to central phase of  [!:Autodesk::Revit::ApplicationServices::Application::WorksharedOperationProgressChanged]  .

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public class DocumentSaveToCentralProgressChangedEventArgs : DataTransferProgressChangedEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DocumentSaveToCentralProgressChangedEventArgs _ 	Inherits DataTransferProgressChangedEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DocumentSaveToCentralProgressChangedEventArgs : public DataTransferProgressChangedEventArgs ``` |

# Remarks

It is NOT recommended to do any time-consuming work when handling WorksharedOperationProgressChanged event. This can increase workshared operation time. Name correction - it is renamed from 'DocumentSaveToCentralProgessChangedEventArgs' released since 2017 Subscription Update.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPISingleEventArgs](446fa3c6-4f35-47f4-e8c2-e5235c321836.htm)    
  [Autodesk.Revit.DB.Events WorksharedOperationProgressChangedEventArgs](110ee5e7-4cc1-3dbb-c824-6fd7bb5a8061.htm)    
  [Autodesk.Revit.DB.Events DataTransferProgressChangedEventArgs](a5a0081b-e990-ac8f-68dc-be0915955d1d.htm)    
  Autodesk.Revit.DB.Events DocumentSaveToCentralProgressChangedEventArgs

# See Also

[DocumentSaveToCentralProgressChangedEventArgs Members](4f1a7763-d33e-6ffd-5988-3cd22878f18e.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__5c81eabb-0622-f97b-fe4c-8fae55f6ff68.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProcessIFCProject Method (IFCAnyHandle)

---



|  |
| --- |
| [ImporterIFC Class](87327a4b-94fd-5a21-df33-9beb1921cb4d.htm)   [See Also](#seeAlsoToggle) |

The entry point to the native IFC import function. Processes the main IfcProject and creates appropriate Revit elements.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void ProcessIFCProject( 	IFCAnyHandle ifcProject ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ProcessIFCProject ( _ 	ifcProject As IFCAnyHandle _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ProcessIFCProject( 	IFCAnyHandle^ ifcProject ) ``` |

#### Parameters

ifcProject
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)    
     The IfcProject containing the entities in the IFC file.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ImporterIFC Class](87327a4b-94fd-5a21-df33-9beb1921cb4d.htm)

[ProcessIFCProject Overload](2c440232-e770-1a51-a9bf-2070ff1310cd.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__5c820dcf-f2dc-5d96-edc7-31c0ce7b94f9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumberOfFrames Property

---



|  |
| --- |
| [SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.htm)   [See Also](#seeAlsoToggle) |

Identifies the total number of animation frames for a single-day or multi-day study.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public double NumberOfFrames { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property NumberOfFrames As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double NumberOfFrames { 	double get (); } ``` |

# See Also

[SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c88b083-2c49-b8be-07d3-017bfd73a051.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, String, ICollection(ElementId), ElementFilter)

---



|  |
| --- |
| [ParameterFilterElement Class](b231dc85-516a-5e75-c634-c6cd81b43fc5.htm)   [See Also](#seeAlsoToggle) |

Creates a new ParameterFilterElement in the given document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public static ParameterFilterElement Create( 	Document aDocument, 	string name, 	ICollection<ElementId> categories, 	ElementFilter elementFilter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	aDocument As Document, _ 	name As String, _ 	categories As ICollection(Of ElementId), _ 	elementFilter As ElementFilter _ ) As ParameterFilterElement ``` |

 

| Visual C++ |
| --- |
| ``` public: static ParameterFilterElement^ Create( 	Document^ aDocument,  	String^ name,  	ICollection<ElementId^>^ categories,  	ElementFilter^ elementFilter ) ``` |

#### Parameters

aDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to create the ParameterFilterElement.

name
:   Type:  System String    
     The user-visible name for the new ParameterFilterElement.

categories
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The categories for the new ParameterFilterElement.

elementFilter
:   Type:  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
     The rules for the new ParameterFilterElement, represented as an ElementFilter. ElementFilter is either an ElementParameterFilter or an ElementLogicalFilter representing a Boolean combination of ElementParameterFilters. In addition, we check that each ElementParameterFilter satisfies the following conditions: Its array of FilterRules is not empty and contains:

    * Any number of FilterRules of type FilterValueRule, FilterInverseRule, and SharedParameterApplicableRule or
    * Exactly one FilterCategoryRule containing only one category from categories stored by this ParameterFilterElement or
    * Exactly two rules: the first one is a FilterCategoryRule containing only one category from categories stored by this ParameterFilterElement and the second one is a FilterRule of type FilterValueRule, FilterInverseRule, or SharedParameterApplicableRule.

    Note that cases in the second and third bullet are currently allowed only if the parent node of ElementParameterFilter is LogicalOrFilter.

#### Return Value

A pointer to the new ParameterFilterElement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name is an empty string or contains only whitespace. -or- name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". -or- The given value for name is already in use as a filter element name. -or- One of the given rules refers to a parameter that does not apply to this filter's categories. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | The ElementFilter is not acceptable for use by a ParameterFilterElement. |

# See Also

[ParameterFilterElement Class](b231dc85-516a-5e75-c634-c6cd81b43fc5.htm)

[Create Overload](13c3ae39-309b-3071-530e-912337a59452.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c8b40be-22c0-451e-14ed-b99ba5720a24.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Show Method (String, String)

---



|  |
| --- |
| [TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)   [See Also](#seeAlsoToggle) |

Shows a task dialog with title, main instruction and a Close button.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static TaskDialogResult Show( 	string title, 	string mainInstruction ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Show ( _ 	title As String, _ 	mainInstruction As String _ ) As TaskDialogResult ``` |

 

| Visual C++ |
| --- |
| ``` public: static TaskDialogResult Show( 	String^ title,  	String^ mainInstruction ) ``` |

#### Parameters

title
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The title of the task dialog.

mainInstruction
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The main instruction of the task dialog.

#### Return Value

The user's response to the task dialog.

# See Also

[TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)

[Show Overload](77990692-a24d-eb40-5872-f3ceb2f76e60.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__5c8ced09-06c7-7d23-0f24-01feacb35237.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundaryParamPresetLinear Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"State"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BoundaryParamPresetLinear { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BoundaryParamPresetLinear As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BoundaryParamPresetLinear { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c8ec772-b72c-ded9-9eb5-d6e1a55877c3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetObjectData Method

---



|  |
| --- |
| [OptionalFunctionalityNotAvailableException Class](0612a676-b6ba-8c37-2e28-b197438305ab.htm)   [See Also](#seeAlsoToggle) |

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

[OptionalFunctionalityNotAvailableException Class](0612a676-b6ba-8c37-2e28-b197438305ab.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__5c90f541-5fa5-946b-4b4f-4126a29650f2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetConstraintType Method

---



|  |
| --- |
| [RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)   [See Also](#seeAlsoToggle) |

Returns the RebarConstraintType of a RebarConstraint.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public RebarConstraintType GetConstraintType() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetConstraintType As RebarConstraintType ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarConstraintType GetConstraintType() ``` |

#### Return Value

The RebarConstraintType of the specified RebarConstraint.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | RebarConstraint is no longer valid. |

# See Also

[RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5c949009-22c5-df87-72c7-e8a8c88aa26b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ThermalMaterialParamLiquidViscosity Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Liquid Viscosity"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ThermalMaterialParamLiquidViscosity { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ThermalMaterialParamLiquidViscosity As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ThermalMaterialParamLiquidViscosity { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c97b79a-6d6b-5f74-fa3f-c35fbc96d01c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ArrayElementsWithoutAssociation Method

---



|  |
| --- |
| [LinearArray Class](58e47064-607e-d52b-5930-7e371851a678.htm)   [See Also](#seeAlsoToggle) |

Creates a new linear array from a set of elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> ArrayElementsWithoutAssociation( 	Document aDoc, 	View dBView, 	ICollection<ElementId> ids, 	int count, 	XYZ translationToAnchorMember, 	ArrayAnchorMember anchorMember ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ArrayElementsWithoutAssociation ( _ 	aDoc As Document, _ 	dBView As View, _ 	ids As ICollection(Of ElementId), _ 	count As Integer, _ 	translationToAnchorMember As XYZ, _ 	anchorMember As ArrayAnchorMember _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ ArrayElementsWithoutAssociation( 	Document^ aDoc,  	View^ dBView,  	ICollection<ElementId^>^ ids,  	int count,  	XYZ^ translationToAnchorMember,  	ArrayAnchorMember anchorMember ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

dBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view. If it is a 2d view, translation vector must be in the view plane if elements include view-specific elements. If elements include view-specific elements, they must belong to this view.

ids
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The elements to array.

count
:   Type:  System Int32    
     The number of array members to create including the initial element grouping. Must between 2 and 200.

translationToAnchorMember
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The translation vector for the array.

anchorMember
:   Type:  [Autodesk.Revit.DB ArrayAnchorMember](4e138a54-bc03-a66f-831b-7ab88f15677e.htm)    
     Indicates if the translation vector specifies the location of the second member of the array, or the last member of the array.

#### Return Value

The ids of the elements created during the operation.

# Remarks

The resulting elements will not be associated with an array element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given element id set is empty. -or- One or more elements in ids do not exist in the document. -or- One or more elements in ids is owned by different views and thus cannot be arrayed together. -or- One or more elements in ids is not arrayable. -or- count must be between 2 and 200. -or- The view is invalid for specific view elements array. -or- The translation point vector is invalid to array the element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to create the linear array. |

# See Also

[LinearArray Class](58e47064-607e-d52b-5930-7e371851a678.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c980ee3-7647-0f3d-5a0d-24b43356997f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateString Method

---



|  |
| --- |
| [IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.htm)   [See Also](#seeAlsoToggle) |

Creates a string data object.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static IFCData CreateString( 	string value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateString ( _ 	value As String _ ) As IFCData ``` |

 

| Visual C++ |
| --- |
| ``` public: static IFCData^ CreateString( 	String^ value ) ``` |

#### Parameters

value
:   Type:  System String    
     The string value.

#### Return Value

The IFCData object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__5c9a9f68-7521-94bc-3bc1-7a3f5aa6ac69.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SystemClassification Property

---



|  |
| --- |
| [ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)   [See Also](#seeAlsoToggle) |

The system classification of the connector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public MEPSystemClassification SystemClassification { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SystemClassification As MEPSystemClassification 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property MEPSystemClassification SystemClassification { 	MEPSystemClassification get (); 	void set (MEPSystemClassification value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | When setting this property: The MEPSystemType is not valid for the domain of this connector. |

# See Also

[ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c9afcd0-f20c-519a-1a8c-938ceafdeb2a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasAssociatedParts Method (Document, LinkElementId)

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Checks if an element has associated parts.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool HasAssociatedParts( 	Document hostDocument, 	LinkElementId hostOrLinkElementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function HasAssociatedParts ( _ 	hostDocument As Document, _ 	hostOrLinkElementId As LinkElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool HasAssociatedParts( 	Document^ hostDocument,  	LinkElementId^ hostOrLinkElementId ) ``` |

#### Parameters

hostDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

hostOrLinkElementId
:   Type:  [Autodesk.Revit.DB LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)    
     The element to be checked for associated Parts.

#### Return Value

True if the element has associated Parts.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[HasAssociatedParts Overload](55cd42e2-3eca-3592-336c-197c0c525c52.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5c9dca6a-77dd-9631-47f8-b0f02c8ca905.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetElementIdOverrideValue Method

---



|  |
| --- |
| [RebarContainerParameterManager Class](a0e5db38-c482-7232-df45-b0cdbcebac7d.htm)   [See Also](#seeAlsoToggle) |

Get the ElementId value for an overriden parameter.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public ElementId GetElementIdOverrideValue( 	ElementId paramId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetElementIdOverrideValue ( _ 	paramId As ElementId _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetElementIdOverrideValue( 	ElementId^ paramId ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the parameter

#### Return Value

The override value of the parameter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId is not the id of a parameter in the current document, or its value type is not ElementId. -or- paramId is not a Rebar Container parameter -or- paramId has no override |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarContainerParameterManager Class](a0e5db38-c482-7232-df45-b0cdbcebac7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5ca02b0e-289a-f1ef-7ce2-8b3f175fe402.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Parameter Property

---



|  |
| --- |
| [IntersectionResult Class](0b6f0c2e-e3a2-3e27-fa52-0f4f9f2ca6f0.htm)   [See Also](#seeAlsoToggle) |

1d parameter of the point of intersection.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double Parameter { get; internal set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Parameter As Double 	Get 	Friend Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Parameter { 	double get (); 	internal: void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown in the getter when this property has not been set by the method providing the result. |

# See Also

[IntersectionResult Class](0b6f0c2e-e3a2-3e27-fa52-0f4f9f2ca6f0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ca1b4b1-a140-df5e-579d-839e57ba729c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCopySunAndShadowSettings Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

SunAndShadowSettings cannot be copied.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCopySunAndShadowSettings { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCopySunAndShadowSettings As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCopySunAndShadowSettings { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5caa4a80-2b34-3148-6227-fdd21f0c3611.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Lx Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol lx, indicating unit Lux.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Lx { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Lx As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Lx { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cad9946-8498-9b0f-544d-d2328e5960b7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnifiedbitmapBitmap Property

---



|  |
| --- |
| [UnifiedBitmap Class](de22f405-e0d8-e50a-096f-7e199c64fd00.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Source" from the "UnifiedBitmap" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static string UnifiedbitmapBitmap { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property UnifiedbitmapBitmap As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ UnifiedbitmapBitmap { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyString" and will contain a relative path.

# See Also

[UnifiedBitmap Class](de22f405-e0d8-e50a-096f-7e199c64fd00.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__5cb33cf3-5870-2afa-6ad1-e3fafc0a640a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SchemaName Property

---



|  |
| --- |
| [IFCFileModelOptions Class](9cd09052-e2e2-84e3-c500-9b492ad8d78b.htm)   [See Also](#seeAlsoToggle) |

The name of the schema.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public string SchemaName { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SchemaName As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ SchemaName { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[IFCFileModelOptions Class](9cd09052-e2e2-84e3-c500-9b492ad8d78b.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__5cb403b7-e705-d6ef-fcd6-e690831948ca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElemWeldContinuous Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Continuous"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SteelElemWeldContinuous { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElemWeldContinuous As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SteelElemWeldContinuous { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cb46dcb-decb-b928-89b8-4c8524ec7c8a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DimStyleLeaderTickMark Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Leader Tick Mark"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DimStyleLeaderTickMark { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DimStyleLeaderTickMark As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DimStyleLeaderTickMark { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cb6e92e-80b0-24e3-943c-a246566e4318.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentSynchronizedWithCentral Event

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the DocumentSynchronizedWithCentral event to be notified immediately after Revit has finished synchronizing a document with central model.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<DocumentSynchronizedWithCentralEventArgs> DocumentSynchronizedWithCentral ``` |

 

| Visual Basic |
| --- |
| ``` Public Event DocumentSynchronizedWithCentral As EventHandler(Of DocumentSynchronizedWithCentralEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<DocumentSynchronizedWithCentralEventArgs^>^ DocumentSynchronizedWithCentral { 	void add (EventHandler<DocumentSynchronizedWithCentralEventArgs^>^ value); 	void remove (EventHandler<DocumentSynchronizedWithCentralEventArgs^>^ value); } ``` |

# Remarks

This event is raised immediately after Revit has finished synchronizing a document with central model. It is raised even when document synchronizing with central model failed or was cancelled (during DocumentSynchronizingWithCentral event).

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Check the 'Status' field in event's argument to see whether the action itself was successful or not.

This event is not cancellable, for the process of synchronizing a document with central model has already been finished.

If the action was not successful, the document may not be modified and new transactions may not be started.

The following API functions are not available for the current document during this event:

* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  .
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__5cb6f01e-3e59-dfa7-03ca-82337a357062.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationPartDepthIn Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Main Primary Depth"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FabricationPartDepthIn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationPartDepthIn As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FabricationPartDepthIn { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cb877fa-8a44-118f-b52f-3ecda9b5fc47.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [CurveExtents Class](d974db89-6e5c-d777-9d1f-08e2561feba5.htm)   [See Also](#seeAlsoToggle) |

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

[CurveExtents Class](d974db89-6e5c-d777-9d1f-08e2561feba5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cbb637f-85f3-a74c-4613-2fab0d3668e3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalModelPhysicalType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Family Type": the Family Type of the physical element associated with the Analytical Model

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnalyticalModelPhysicalType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticalModelPhysicalType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnalyticalModelPhysicalType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cbd9192-b16a-d34e-9cba-75d8a34e3424.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreElementsValidForCreateParts Method

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Identifies if the given elements can be used to create parts.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool AreElementsValidForCreateParts( 	Document document, 	ICollection<ElementId> elementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function AreElementsValidForCreateParts ( _ 	document As Document, _ 	elementIds As ICollection(Of ElementId) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool AreElementsValidForCreateParts( 	Document^ document,  	ICollection<ElementId^>^ elementIds ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

elementIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Element ids to be tested for validity for creating parts.

#### Return Value

True if all member ids are valid, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cbf5a07-7043-e8b3-def5-6ea4380c22a9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddSpatialFieldPrimitive Method (Curve, Transform)

---



|  |
| --- |
| [SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)   [See Also](#seeAlsoToggle) |

Creates empty analysis results primitive associated with a curve and a transform.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public int AddSpatialFieldPrimitive( 	Curve curve, 	Transform trf ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddSpatialFieldPrimitive ( _ 	curve As Curve, _ 	trf As Transform _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int AddSpatialFieldPrimitive( 	Curve^ curve,  	Transform^ trf ) ``` |

#### Parameters

curve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     Curve to be associated with the primitive. %curve% does NOT correspond to actual Revit geometry, i.e. it cannot be associated with reference; otherwise the other overload of the method must be used (taking "reference" as the input)

trf
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     Conformal Transform to be applied to %curve%.

#### Return Value

Unique index of primitive for future references

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input curve points to a helical curve and is not supported for this operation. -or- Argument trf is not a conformal transform (see property Revit::DB::Transform::IsConformal) |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)

[AddSpatialFieldPrimitive Overload](125b85d3-9b44-c90d-2eab-7334be74117f.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__5cc3231e-ee7e-e1fc-2bd6-d164da617954.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UpdateAllOpenViews Method

---



|  |
| --- |
| [UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)   [See Also](#seeAlsoToggle) |

Update all open views in this document after elements have been changed, deleted, selected or de-selected. Graphics in the views are fully redrawn regardless of which elements have changed.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void UpdateAllOpenViews() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub UpdateAllOpenViews ``` |

 

| Visual C++ |
| --- |
| ``` public: void UpdateAllOpenViews() ``` |

# Remarks

This function should only rarely be needed, but might be required when working with graphics drawn from outside of Revit's transactions and elements, for example, when using  [IDirectContext3DServer](7709521d-9954-ef80-1f13-3bc6ee660d5d.htm)  . This function is potentially expensive as many views may be updated at once, including regeneration of view's geometry and redisplay of graphics. Thus for most situations it is recommended that API applications rely on the Revit application framework to update views more deliberately.

# See Also

[UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__5cc4eec1-7ec6-ad73-48b9-b8797f2a00ce.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpoolName Property

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

The spool name of the fabrication part.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public string SpoolName { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SpoolName As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ SpoolName { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cd014e3-447e-c847-98f0-5b177e65efca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceTriangulationFailed Property

---



|  |
| --- |
| [BuiltInFailures SiteFailures Class](7ab66d74-f1ab-17f6-9ecf-e51b3d5326bf.htm)   [See Also](#seeAlsoToggle) |

The Site Surface failed to triangulate.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SurfaceTriangulationFailed { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SurfaceTriangulationFailed As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SurfaceTriangulationFailed { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SiteFailures Class](7ab66d74-f1ab-17f6-9ecf-e51b3d5326bf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cd40e6c-3912-6189-87bf-9eb7d9e131dd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetParts Method

---



|  |
| --- |
| [ConnectionValidationWarning Class](610c2f13-1d95-3a43-b845-b39ab3f02d46.htm)   [See Also](#seeAlsoToggle) |

Get ElementIds of affected parts.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public ISet<ElementId> GetParts() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetParts As ISet(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ISet<ElementId^>^ GetParts() ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[ConnectionValidationWarning Class](610c2f13-1d95-3a43-b845-b39ab3f02d46.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cd9ac35-6b1f-1084-c1f2-55d7dbc3b3ff.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FileImporting Event

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the FileImporting event to be notified when Revit is just about to import a file of format supported by the API.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<FileImportingEventArgs> FileImporting ``` |

 

| Visual Basic |
| --- |
| ``` Public Event FileImporting As EventHandler(Of FileImportingEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<FileImportingEventArgs^>^ FileImporting { 	void add (EventHandler<FileImportingEventArgs^>^ value); 	void remove (EventHandler<FileImportingEventArgs^>^ value); } ``` |

# Remarks

This event is raised when Revit is just about to import a file of format supported by the API.

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Event is cancellable. To cancel it, call the 'Cancel()' method in event's argument to True. Your application is responsible for providing feedback to the user about the reason for the cancellation.

The following API functions are not available for the current document during this event:

* All overloads of Autodesk.Revit.DB.Document.Import()
* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  .
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

Another  [FileImported](f72dee18-1a0d-dc0c-eb72-b75b0939c7c9.htm)  event will be raised immediately after file importing is finished.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__5cdd56ef-334d-b638-4118-0033fadc9613.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MepEquipmentCalcPipingpressuredropParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Calculated Pressure Drop"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MepEquipmentCalcPipingpressuredropParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MepEquipmentCalcPipingpressuredropParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MepEquipmentCalcPipingpressuredropParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cdebb2b-28d5-c269-77a9-88397ec71ab8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InsulationTypes Property

---



|  |
| --- |
| [TemperatureRatingType Class](fe7e15d7-c31f-b24c-992f-332e54e9a5ba.htm)   [See Also](#seeAlsoToggle) |

Get all insulation types defined in this temperature rating type and its corresponding material type.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public InsulationTypeSet InsulationTypes { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property InsulationTypes As InsulationTypeSet 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property InsulationTypeSet^ InsulationTypes { 	InsulationTypeSet^ get (); } ``` |

# See Also

[TemperatureRatingType Class](fe7e15d7-c31f-b24c-992f-332e54e9a5ba.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__5ce1e6a9-1ba9-fb09-1185-31956ce421bd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PreviewViewId Property

---



|  |
| --- |
| [DocumentPreviewSettings Class](e38ea350-9951-ee05-5e3d-ab7f31815fb3.htm)   [See Also](#seeAlsoToggle) |

The view id that will be used to generate the preview.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementId PreviewViewId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PreviewViewId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ PreviewViewId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

#### Field Value

InvalidElementId signals that there is no permanent preview view for the document. Where possible the document's active view will be used to generate the preview upon save; where there is no active view the document will not include a preview.

# Remarks

This view will always be saved as the preview view for the document unless it is overridden by the value used in SaveOptions or SaveAsOptions.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The view id is not valid to use as a preview view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[DocumentPreviewSettings Class](e38ea350-9951-ee05-5e3d-ab7f31815fb3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ce1f39f-01d5-a0d9-6fc5-6a9e8d5418f5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ChillerType Property

---



|  |
| --- |
| [WaterLoopData Class](2860db31-4947-5332-27c2-fac4caf7cc12.htm)   [See Also](#seeAlsoToggle) |

The type of water chiller. Note this property change would reset the condenser water loop.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public WaterChillerType ChillerType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ChillerType As WaterChillerType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property WaterChillerType ChillerType { 	WaterChillerType get (); 	void set (WaterChillerType value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[WaterLoopData Class](2860db31-4947-5332-27c2-fac4caf7cc12.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__5ce21226-0a63-c759-aff7-0ac08ec6bc73.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAddInName Method

---



|  |
| --- |
| [AddInId Class](31859d69-72c7-03fb-83e1-5c7719dca253.htm)   [See Also](#seeAlsoToggle) |

name of addin associated with this AddInId Attempts to obtain the name from loaded Third Party AddIns

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string GetAddInName() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAddInName As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetAddInName() ``` |

#### Return Value

name of addin

# See Also

[AddInId Class](31859d69-72c7-03fb-83e1-5c7719dca253.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ce3fa96-81d0-6f32-99b9-b19cda8b8193.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLoops Method

---



|  |
| --- |
| [IFCExtrusionData Class](c10272e7-741d-1aca-9f64-cc51d0b14e54.htm)   [See Also](#seeAlsoToggle) |

Gets the curve loops that form the base shape of the extrusion.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<CurveLoop> GetLoops() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLoops As IList(Of CurveLoop) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<CurveLoop^>^ GetLoops() ``` |

#### Return Value

The collection of loops.

# See Also

[IFCExtrusionData Class](c10272e7-741d-1aca-9f64-cc51d0b14e54.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__5ce7e921-2a43-d7f1-8ef9-8a397dd27b75.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GroupType Class

---



|  |
| --- |
| [Members](7644d345-6c8b-9b28-a2f0-418614cad687.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

An element representing a group of elements that may be placed many times in a project or family.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public class GroupType : ElementType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class GroupType _ 	Inherits ElementType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class GroupType : public ElementType ``` |

# Remarks

Grouping elements is useful when you need to create entities that represent repeating layouts or are common to many building projects, such as hotel rooms, apartments, or repeating floors.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetInfo_GroupType(GroupType groupType)
{
    string message = "GroupType";
    //Retrieve a set of all the groups that have this type.
    foreach (Group group in groupType.Groups)
    {
        // Get GroupType group name
        message = "\nThe group type name is : " + groupType.Name;
        //Returns all the members of the group.
        message += "\nThe types and ids of the group members are : ";
        IList<ElementId> groupMembers = group.GetMemberIds();
        foreach (ElementId memberId in groupMembers)
        {
            Element element = group.Document.GetElement(memberId);
            // Get GroupType group element id
            message += "\n\t" + element.GetType().Name + " : " + memberId.ToString();
        }
    }
    TaskDialog.Show("Revit",message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetInfo_GroupType(groupType As GroupType)
    Dim message As String = "GroupType"
    'Retrieve a set of all the groups that have this type.
    For Each group As Group In groupType.Groups
        ' Get GroupType group name
        message = vbLf & "The group type name is : " & Convert.ToString(groupType.Name)
        'Returns all the members of the group.
        message += vbLf & "The types and ids of the group members are : "
        Dim groupMembers As IList(Of ElementId) = group.GetMemberIds()
        For Each memberId As ElementId In groupMembers
            Dim element As Element = group.Document.GetElement(memberId)
            ' Get GroupType group element id
            message += (vbLf & vbTab + element.[GetType]().Name & " : ") + memberId.IntegerValue
        Next
    Next
    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  Autodesk.Revit.DB GroupType

# See Also

[GroupType Members](7644d345-6c8b-9b28-a2f0-418614cad687.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5ceb005d-c8a9-045a-00bf-b9ef3059a78a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanarMultiPlanarShape Property

---



|  |
| --- |
| [BuiltInFailures RebarShapeFailures Class](7e0a8c39-c873-730e-6ffd-2fc6d6f71f3e.htm)   [See Also](#seeAlsoToggle) |

The current shape is only bent in a single plane. A multi-planar definition is not required. Please redefine the shape on the top plane only.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId PlanarMultiPlanarShape { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PlanarMultiPlanarShape As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ PlanarMultiPlanarShape { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarShapeFailures Class](7e0a8c39-c873-730e-6ffd-2fc6d6f71f3e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cf10123-13e7-b4e1-b925-334beb837ee6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsCellOverridden Method (Int32)

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Indicates if the column is overridden or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsCellOverridden( 	int nCol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsCellOverridden ( _ 	nCol As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsCellOverridden( 	int nCol ) ``` |

#### Parameters

nCol
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given column number nCol is invalid. |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[IsCellOverridden Overload](91ac6cb2-f7f0-ea1d-ea5f-32afa5d3a083.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cf36a8f-dc5f-bb00-8819-8c40a75969e3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Value Property

---



|  |
| --- |
| [VendorIdAttribute Class](789e2e36-a560-cbf4-ed62-186d78ba4d51.htm)   [See Also](#seeAlsoToggle) |

AddInId VendorId value.

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public string Value { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Value As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Value { 	String^ get (); } ``` |

# See Also

[VendorIdAttribute Class](789e2e36-a560-cbf4-ed62-186d78ba4d51.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)

<!-- Start of Syntax__5cfd0261-bde9-6f05-4056-7873b0c1cfec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ColumnBaseAboveTopFailure Property

---



|  |
| --- |
| [BuiltInFailures ColumnFailures Class](eab97a8a-0a8b-7414-33c0-2b48538202d1.htm)   [See Also](#seeAlsoToggle) |

The column base can't be moved above its top.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ColumnBaseAboveTopFailure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ColumnBaseAboveTopFailure As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ColumnBaseAboveTopFailure { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ColumnFailures Class](eab97a8a-0a8b-7414-33c0-2b48538202d1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cfe0d84-198b-9ecf-1f80-d6d10476ed31.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SheetCheckedBy Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Checked By"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SheetCheckedBy { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SheetCheckedBy As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SheetCheckedBy { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5cff2a01-bac3-e53f-6c98-2dabc281fe6a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureScaleLock Property

---



|  |
| --- |
| [BumpMap Class](7301801c-eef2-3077-7891-a3ee27db1a9b.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Scale Lock" from the "BumpMap" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TextureScaleLock { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextureScaleLock As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TextureScaleLock { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyBoolean".

# See Also

[BumpMap Class](7301801c-eef2-3077-7891-a3ee27db1a9b.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__5cfff6ff-3982-e8f7-a3c8-43d93204d41a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextBox Class

---



|  |
| --- |
| [Members](775009fd-1ab0-1e71-e94d-71ed3be5559a.htm)   [See Also](#seeAlsoToggle) |

The TextBox object represents text-based control that allows the user to enter text.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class TextBox : RibbonItem ``` |

 

| Visual Basic |
| --- |
| ``` Public Class TextBox _ 	Inherits RibbonItem ``` |

 

| Visual C++ |
| --- |
| ``` public ref class TextBox : public RibbonItem ``` |

# Remarks

The ItemText property inherited from RibbonItem has no effect. The text entered in the TextBox is edited by the UI user is accepted only if the user presses the Enter key or click the image button when ShowImageAsButton is true. If the user clicks off of this component without pressing Enter or click the image button; then the text will be reverted to the previous value. Use of this class is not supported in Revit Macros.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.UI RibbonItem](79225f03-1633-3722-15b0-752c91a3740d.htm)    
  Autodesk.Revit.UI TextBox

# See Also

[TextBox Members](775009fd-1ab0-1e71-e94d-71ed3be5559a.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__5d0a6aa5-28e6-517a-fe09-32b380ac7fbc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SculptingCurvesTouchAxis Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

The highlighted curves touch the axis.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SculptingCurvesTouchAxis { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SculptingCurvesTouchAxis As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SculptingCurvesTouchAxis { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d0ebbf8-0da0-fc23-5a02-7da20980fd5d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SketchFailurePlanes Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Sketch is no longer parallel to its defining plane

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SketchFailurePlanes { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SketchFailurePlanes As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SketchFailurePlanes { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d0f746c-2b58-ba10-9060-a7f653122e53.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FoldWidth Property

---



|  |
| --- |
| [StructuralSectionSigmaProfileWithFold Class](a723efc0-a5a5-a157-1345-bf55a6fb4894.htm)   [See Also](#seeAlsoToggle) |

Fold segment width.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public double FoldWidth { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FoldWidth As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double FoldWidth { 	double get (); 	void set (double value); } ``` |

# See Also

[StructuralSectionSigmaProfileWithFold Class](a723efc0-a5a5-a157-1345-bf55a6fb4894.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__5d13ec14-d18f-cceb-b56e-955b7d59f9b5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementArrayIterator Constructor

---



|  |
| --- |
| [ElementArrayIterator Class](fc1af4a8-d97f-da4e-97bd-d97061977360.htm)   [See Also](#seeAlsoToggle) |

For Internal Use Only.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ElementArrayIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementArrayIterator() ``` |

# Remarks

This constructor is exposed to enable support for COM interop only. This object should never be created by the developer.

# See Also

[ElementArrayIterator Class](fc1af4a8-d97f-da4e-97bd-d97061977360.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d165bb0-2777-e95c-ef18-b2342b07a011.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DekanewtonsPerMeter Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Dekanewtons per meter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DekanewtonsPerMeter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DekanewtonsPerMeter As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DekanewtonsPerMeter { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d17667d-c41b-8ef4-4c2f-4f0fd4a3a9e8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Volume Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Volume, in discipline Common.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Volume { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Volume As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Volume { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d1792e2-758f-3ec3-c1d8-61b186180a2f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PageOrientationType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all Page Orientation types of Print Setting

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public enum PageOrientationType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration PageOrientationType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class PageOrientationType ``` |

# Members

| Member name | Description |
| --- | --- |
| Portrait | The type of Page Orientation is Portrait |
| Landscape | The type of Page Orientation is Landscape |
| Auto | Auto Page Orientation |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d22cdfd-5eff-c54a-4560-c83fa56f47bc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CenterCurve Property

---



|  |
| --- |
| [StructuralElementDefinitionData Class](f7a0e8ec-6fd5-43e5-1a54-5cb6ebe009c7.htm)   [See Also](#seeAlsoToggle) |

The curve lying in the geometrical center of the element.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public Curve CenterCurve { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property CenterCurve As Curve 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Curve^ CenterCurve { 	Curve^ get (); } ``` |

# See Also

[StructuralElementDefinitionData Class](f7a0e8ec-6fd5-43e5-1a54-5cb6ebe009c7.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__5d22ee48-76dd-c314-a551-b6f722eb49a3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SchedulableField Constructor (ScheduleFieldType, ElementId)

---



|  |
| --- |
| [SchedulableField Class](84f03bb5-a9b8-581c-631c-6240b4954099.htm)   [See Also](#seeAlsoToggle) |

Creates a new SchedulableField.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public SchedulableField( 	ScheduleFieldType fieldType, 	ElementId parameterId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	fieldType As ScheduleFieldType, _ 	parameterId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: SchedulableField( 	ScheduleFieldType fieldType,  	ElementId^ parameterId ) ``` |

#### Parameters

fieldType
:   Type:  [Autodesk.Revit.DB ScheduleFieldType](9888db7d-00d0-4fd7-a1a9-cdd1fb5fce16.htm)    
     The type of data displayed by the field.

parameterId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ID of the parameter displayed by the field.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | fieldType is not a schedulable field type |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[SchedulableField Class](84f03bb5-a9b8-581c-631c-6240b4954099.htm)

[SchedulableField Overload](840d13c0-ba08-565b-479c-0769e3cfea34.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d256bc4-e693-99ce-80b4-32c39f23ee9d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhyMaterialParamCompressionPerpendicular Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Compression perpendicular to grain"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PhyMaterialParamCompressionPerpendicular { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PhyMaterialParamCompressionPerpendicular As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PhyMaterialParamCompressionPerpendicular { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d25d459-a1b0-eef4-4766-b00bd1f5ba79.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PostFailure Method

---



|  |
| --- |
| [FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)   [See Also](#seeAlsoToggle) |

Posts an additional failure message to be processed for the current transaction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void PostFailure( 	FailureMessage failure ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub PostFailure ( _ 	failure As FailureMessage _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void PostFailure( 	FailureMessage^ failure ) ``` |

#### Parameters

failure
:   Type:  [Autodesk.Revit.DB FailureMessage](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)    
     Failure message to post.

# Remarks

Should be used during failures processing instead of a similar method in a document class. Using method of the document class with the same name during failures processing is prohibited.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailuresAccessor is inactive (is used outside of failures processing). |

# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d2857ac-200f-30c9-278c-65184fa75ca9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsGridAspectRatioSet Method

---



|  |
| --- |
| [OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)   [See Also](#seeAlsoToggle) |

Checks whether the GridAspectRatio tessellation parameter is explicitly set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public bool IsGridAspectRatioSet() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsGridAspectRatioSet As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsGridAspectRatioSet() ``` |

#### Return Value

True if GridAspectRatio tessellation parameter is explicitly set, false otherwise.

# See Also

[OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d2b053f-3eb4-9642-0339-1c42a6003d89.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShowHiddenLinesValues Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Provides options for display of hidden lines in a given view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum ShowHiddenLinesValues ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ShowHiddenLinesValues ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ShowHiddenLinesValues ``` |

# Members

| Member name | Description |
| --- | --- |
| None | Do not show any hidden lines. |
| ByDiscipline | Show hidden lines according to discipline. |
| All | Show all hidden lines. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d30cbc2-2b80-5b26-3379-00d83a582d3a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RightOffset Property

---



|  |
| --- |
| [CameraInfo Class](facf52cc-bc82-0008-9e4c-60e6a335ef40.htm)   [See Also](#seeAlsoToggle) |

Distance that the target plane is offset towards the right where right is normal to both Up direction and View direction. This offset shifts both left and right planes.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public double RightOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property RightOffset As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double RightOffset { 	double get (); } ``` |

# See Also

[CameraInfo Class](facf52cc-bc82-0008-9e4c-60e6a335ef40.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d324ccb-04a0-0044-dc7d-1e144163082d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SolidGeometry Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing possible ways of exporting solids in 3D views.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum SolidGeometry ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration SolidGeometry ``` |

 

| Visual C++ |
| --- |
| ``` public enum class SolidGeometry ``` |

# Members

| Member name | Description |
| --- | --- |
| Polymesh | All visible solids are exported as polymesh. |
| ACIS | All visible Revit Building geometry is exported as ACIS 3D solids (except for any elements that are already a polymesh.) |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d34b8dd-9137-da2f-9df7-172304d0cc08.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadFamily Method (String, IFamilyLoadOptions, Family)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Loads an entire family and all its types/symbols into the document and provides a reference to the loaded family.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool LoadFamily( 	string filename, 	IFamilyLoadOptions familyLoadOptions, 	out Family family ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function LoadFamily ( _ 	filename As String, _ 	familyLoadOptions As IFamilyLoadOptions, _ 	<OutAttribute> ByRef family As Family _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool LoadFamily( 	String^ filename,  	IFamilyLoadOptions^ familyLoadOptions,  	[OutAttribute] Family^% family ) ``` |

#### Parameters

filename
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The fully qualified filename of the Family file, usually ending in .rfa.

familyLoadOptions
:   Type:  [Autodesk.Revit.DB IFamilyLoadOptions](d447ed92-74e1-2125-dd0a-38a5ae85ce53.htm)    
     The interface implementation to use when loading a family into the document.

family
:   Type:  [Autodesk.Revit.DB Family](f51d019d-6ff3-692b-d1d2-b497cab564de.htm)   %    
     A reference to the family that was loaded if successful, otherwise Nothing.

#### Return Value

True if the entire family was loaded successfully into the project, otherwise False.

# Remarks

Loading an entire family may take a considerable amount of time and memory. It is recommended that you use one of the LoadFamilySymbol() methods and only load those symbols that you need.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when filename is    a null reference (  Nothing  in Visual Basic)  or empty. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument "familyLoadOptions" is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[LoadFamily Overload](2966229b-60b0-404d-5ffe-e4c4d85d2d7a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d36a63b-ebfa-8daf-5d14-625a528daacb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RenderingQuality Property

---



|  |
| --- |
| [RenderingQualitySettings Class](400738fc-3791-666c-10f3-ec46c771d6d5.htm)   [See Also](#seeAlsoToggle) |

The quality applied for rendering.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public RenderingQuality RenderingQuality { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RenderingQuality As RenderingQuality 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property RenderingQuality RenderingQuality { 	RenderingQuality get (); 	void set (RenderingQuality value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[RenderingQualitySettings Class](400738fc-3791-666c-10f3-ec46c771d6d5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d3ffdf8-dce9-0724-d101-44693775671c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ElementFilter Class](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

[ElementFilter Class](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d401ec0-ead1-39bd-459b-2dca075b2797.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetUnderlayTopLevel Method

---



|  |
| --- |
| [ViewPlan Class](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)   [See Also](#seeAlsoToggle) |

Returns the element id of the level that defines the top of the underlay range.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public ElementId GetUnderlayTopLevel() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetUnderlayTopLevel As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetUnderlayTopLevel() ``` |

#### Return Value

If the underlay base level is a valid level, and this method returns InvalidElementId, then the underlay range is unbounded, and consists of everything above the underlay base level.

# See Also

[ViewPlan Class](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d41a620-08ed-e51d-430c-1c4ece82979f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathReinSpacing Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bar Spacing"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PathReinSpacing { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PathReinSpacing As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PathReinSpacing { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d443ed0-5da5-33ca-11d9-00aec9774621.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ColumnZeroHeightError Property

---



|  |
| --- |
| [BuiltInFailures ColumnFailures Class](eab97a8a-0a8b-7414-33c0-2b48538202d1.htm)   [See Also](#seeAlsoToggle) |

The column can't have zero height

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ColumnZeroHeightError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ColumnZeroHeightError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ColumnZeroHeightError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ColumnFailures Class](eab97a8a-0a8b-7414-33c0-2b48538202d1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d44b5d0-b33f-26b6-10f4-b76d1bc4c949.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsLinked Property

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Identifies if a document is a linked RVT.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsLinked { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsLinked As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsLinked { 	bool get (); } ``` |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d4a27d4-bd70-2679-79da-e423c330ca5e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveNext Method

---



|  |
| --- |
| [CorrectionFactorSetIterator Class](743ee1f7-722e-0de6-87a6-9785522df4bb.htm)   [See Also](#seeAlsoToggle) |

Move the iterator one item forward.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
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

Returns True if the iterator was successfully moved forward one item and the Current property will return a valid item. False will be returned it the iterator has reached the end of the set.

#### Implements

 [IEnumerator MoveNext](http://msdn2.microsoft.com/en-us/library/ycwa4b0c)

# Remarks

MoveNext must be called before the Current property is valid with a new or Reset iterator in line with the expected behavior of IEnumerator.

# See Also

[CorrectionFactorSetIterator Class](743ee1f7-722e-0de6-87a6-9785522df4bb.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__5d511a57-f837-a85f-131f-2412a97f2ac6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCopyBetweenFamilyAndProjectCorruption Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

Can't copy between Family and Project.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCopyBetweenFamilyAndProjectCorruption { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCopyBetweenFamilyAndProjectCorruption As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCopyBetweenFamilyAndProjectCorruption { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d5653ab-6b66-fb08-ae26-5c7bba5102a8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetTemperature Method

---



|  |
| --- |
| [CorrectionFactor Class](203305c0-061a-5607-9f94-5d0cb9a2ca06.htm)   [See Also](#seeAlsoToggle) |

Get temperature which is used for specifying correction factor. The value returned is quantified in the document's selected unit of electrical temperature.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public double GetTemperature() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetTemperature As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetTemperature() ``` |

# See Also

[CorrectionFactor Class](203305c0-061a-5607-9f94-5d0cb9a2ca06.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__5d5bd93e-f406-8189-3d82-0c0be2982914.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDeterminedByFormula Property

---



|  |
| --- |
| [FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)   [See Also](#seeAlsoToggle) |

Indicates if the parameter is determined by formula.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsDeterminedByFormula { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsDeterminedByFormula As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsDeterminedByFormula { 	bool get (); } ``` |

# Remarks

The parameter is read only if it is determined by formula.

# See Also

[FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d5c02ad-dd3e-978e-0296-2c36ff6031ec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SolidglassColorByObject Property

---



|  |
| --- |
| [SolidGlass Class](f21fb90a-9c1d-77eb-69c0-775582db84e7.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Custom Color" from the "SolidGlass" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string SolidglassColorByObject { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SolidglassColorByObject As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ SolidglassColorByObject { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyBoolean".

# See Also

[SolidGlass Class](f21fb90a-9c1d-77eb-69c0-775582db84e7.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__5d5c1f17-7c0e-3913-d39f-30cfe5002bd3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDataCompleted Method

---



|  |
| --- |
| [ZoneEquipmentData Class](5c3c90a6-699d-b6cf-44f7-405986d13073.htm)   [See Also](#seeAlsoToggle) |

Is the required data completed for this zone equipment?

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public bool IsDataCompleted() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsDataCompleted As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsDataCompleted() ``` |

# See Also

[ZoneEquipmentData Class](5c3c90a6-699d-b6cf-44f7-405986d13073.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__5d5f7f56-c86c-d87e-ff6c-eb4e465a5183.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewRooms2 Method (Level)

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [See Also](#seeAlsoToggle) |

Creates new rooms in each plan circuit found in the given level in the last phase.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> NewRooms2( 	Level level ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewRooms2 ( _ 	level As Level _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ NewRooms2( 	Level^ level ) ``` |

#### Parameters

level
:   Type:  [Autodesk.Revit.DB Level](577e5d4e-a558-118c-9dea-3b810b061775.htm)    
     The level from which the circuits are found.

#### Return Value

If successful, a set of ElementIds which contains the rooms created should be returned, otherwise    a null reference (  Nothing  in Visual Basic)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | If the view of the relevant level can not be retrieved. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | If the phase is invalid, or regeneration fails at the end of the creation. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the level does not exist in the given document. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[NewRooms2 Overload](dde5849a-c78b-d2c4-20c3-cdd2e121ec54.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__5d6162af-4a9a-41f0-696d-cc8e9a5ec273.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallSweepOrientation Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Orientation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId WallSweepOrientation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WallSweepOrientation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ WallSweepOrientation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d62fb23-60c1-b740-b02c-d0b6fd1d8ed0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RotateElements Method

---



|  |
| --- |
| [ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.htm)   [See Also](#seeAlsoToggle) |

Rotates a set of elements about the given axis and angle.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static void RotateElements( 	Document document, 	ICollection<ElementId> elementsToRotate, 	Line axis, 	double angle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub RotateElements ( _ 	document As Document, _ 	elementsToRotate As ICollection(Of ElementId), _ 	axis As Line, _ 	angle As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void RotateElements( 	Document^ document,  	ICollection<ElementId^>^ elementsToRotate,  	Line^ axis,  	double angle ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document that owns the elements.

elementsToRotate
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The set of elements to rotate.

axis
:   Type:  [Autodesk.Revit.DB Line](e7329450-434a-918b-661c-65e15e0585a5.htm)    
     The axis of rotation.

angle
:   Type:  System Double    
     The angle of rotation in radians.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given element id set is empty. -or- One or more elements in elementsToRotate do not exist in the document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d633c8d-de1f-7b9d-8f00-4c725ce13c81.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecRoomAverageIllumination Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Average Estimated Illumination"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecRoomAverageIllumination { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecRoomAverageIllumination As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecRoomAverageIllumination { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d66b464-9c61-6069-e278-d4f4428b2bef.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreaFilter Constructor

---



|  |
| --- |
| [AreaFilter Class](a13bb51e-5370-99ed-d212-bdd60297393d.htm)   [See Also](#seeAlsoToggle) |

Constructs a filter which matches only areas.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public AreaFilter() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: AreaFilter() ``` |

# See Also

[AreaFilter Class](a13bb51e-5370-99ed-d212-bdd60297393d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d67f734-ab88-6788-e6ce-3a41aede826e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [CurtainGridSet Class](adc86636-024c-9035-700f-e7c43442a9f8.htm)   [See Also](#seeAlsoToggle) |

Removes every item from the set, rendering it empty.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
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

[CurtainGridSet Class](adc86636-024c-9035-700f-e7c43442a9f8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d69139e-f243-2093-b539-e63f6f36dd13.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanInsertRow Method

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Verifies if a new row can be inserted at the given index.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool CanInsertRow( 	int nIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanInsertRow ( _ 	nIndex As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanInsertRow( 	int nIndex ) ``` |

#### Parameters

nIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

#### Return Value

True if the row can be inserted, false otherwise.

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d6b9f6a-d25a-9766-009c-9379e4782dbd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetAttribute Method (String, IFCAnyHandle)

---



|  |
| --- |
| [IFCAnyHandle Class](8b893943-70fa-94bf-90be-1523d516ecb3.htm)   [See Also](#seeAlsoToggle) |

Sets the attribute value.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetAttribute( 	string name, 	IFCAnyHandle value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetAttribute ( _ 	name As String, _ 	value As IFCAnyHandle _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetAttribute( 	String^ name,  	IFCAnyHandle^ value ) ``` |

#### Parameters

name
:   Type:  System String    
     The attribute name.

value
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)    
     The value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCAnyHandle Class](8b893943-70fa-94bf-90be-1523d516ecb3.htm)

[SetAttribute Overload](25c11a79-8e0f-5474-cbf5-6a3e7a2821d2.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__5d6d98b0-6c2f-e6c4-c888-a85776657e61.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasEmbeddedSchedule Property

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Indicates if this ScheduleDefinition has an embedded ScheduleDefinition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool HasEmbeddedSchedule { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HasEmbeddedSchedule As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool HasEmbeddedSchedule { 	bool get (); } ``` |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d7db6ff-8538-2c84-8e39-d683e0de9ca5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TransformWithBoundary Class

---



|  |
| --- |
| [Members](935ecb46-cbb3-058c-d70d-cd6c95ef432a.htm)   [See Also](#seeAlsoToggle) |

This class contains the transform from model space to projection space for a view and the boundary in model space in which the transform is valid.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public class TransformWithBoundary : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class TransformWithBoundary _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class TransformWithBoundary : IDisposable ``` |

# Remarks

Use the model-to-projection transform returned by  GetModelToProjectionTransform  to transform model points to the view's projection space. The model-to-projection transform is only valid for points in 3D model space that that can be seen through the 2D boundary returned by  GetBoundary  , when looking in the direction of  [!:View.ViewDirection]  .

For views that are placed on sheets, you can combine the View's model-to-projection transform and the Viewport's projection-to-sheet transform to transform model points to sheet space:

sheetXYZ = projectionToSheetTransform \* modelToProjectionTransform \* modelXYZ

Model space is the global 3D coordinate space in which the 3D geometry of the model lives.

View projection space is the 3D Euclidean space with a coordinate system such that X and Y are horizontal and vertical directions in the view projection plane and Z is the cross product of X and Y. Distances in the projection space are the same as would be measured on paper if the view is printed without additional scaling.

Sheet space is the coordinate space of one sheet. This is the space in which viewports and titleblocks are arranged on the sheet.

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB TransformWithBoundary

# See Also

[TransformWithBoundary Members](935ecb46-cbb3-058c-d70d-cd6c95ef432a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d7f45ca-6e12-0979-2e6c-e6959e1617de.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidShortName Method

---



|  |
| --- |
| [ExternalResourceServerUtils Class](a3147faa-ddc7-6cc1-8906-260582b6bc4a.htm)   [See Also](#seeAlsoToggle) |

Checks whether the name is a valid short name for the external resource server.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static bool IsValidShortName( 	Guid serverId, 	string serverName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidShortName ( _ 	serverId As Guid, _ 	serverName As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidShortName( 	Guid serverId,  	String^ serverName ) ``` |

#### Parameters

serverId
:   Type:  System Guid    
     The id of the external resource server.

serverName
:   Type:  System String    
     The short name of the external resource server.

#### Return Value

True if the name is a valid short name, false otherwise.

# Remarks

A valid short name should match the restrictions documented in  [GetShortName](a6a074b3-3b57-e954-83d4-64ca4e973852.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternalResourceServerUtils Class](a3147faa-ddc7-6cc1-8906-260582b6bc4a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d80c385-94dd-4601-f83a-1e7db3662a25.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetProfile Method

---



|  |
| --- |
| [Truss Class](e0cdc591-cac6-57c7-6190-f0d48cc0e4a9.htm)   [See Also](#seeAlsoToggle) |

Add or modify the profile of a truss.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetProfile( 	CurveArray topChords, 	CurveArray bottomChords ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetProfile ( _ 	topChords As CurveArray, _ 	bottomChords As CurveArray _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetProfile( 	CurveArray^ topChords,  	CurveArray^ bottomChords ) ``` |

#### Parameters

topChords
:   Type:  [Autodesk.Revit.DB CurveArray](55103aad-38fd-45d2-6bf7-67a5203e99f3.htm)    
     The curves serving as top chords of the truss.

bottomChords
:   Type:  [Autodesk.Revit.DB CurveArray](55103aad-38fd-45d2-6bf7-67a5203e99f3.htm)    
     The curves serving as bottom chords of the truss.

# See Also

[Truss Class](e0cdc591-cac6-57c7-6190-f0d48cc0e4a9.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__5d819cec-31a8-119d-c8a1-ca5e7d7c4a17.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationPartCannotChangeTypeError Property

---



|  |
| --- |
| [BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)   [See Also](#seeAlsoToggle) |

The selected fitting(s) cannot successfully change the type. You must disconnect the connections on the fitting(s) and try again.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FabricationPartCannotChangeTypeError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationPartCannotChangeTypeError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FabricationPartCannotChangeTypeError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d850f8a-4a50-406b-6c59-b85d49dcbb2e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasPhases Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Returns true if this Element has the properties CreatedPhaseId and DemolishedPhaseId.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool HasPhases() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function HasPhases As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool HasPhases() ``` |

#### Return Value

True if this Element has the properties CreatedPhaseId and DemolishedPhaseId, false otherwise.

# Remarks

Acts as a validator for setting the properties CreatedPhaseId and DemolishedPhaseId.

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d876de5-82b2-741f-0c4f-696e58d3cb14.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [ExportLayerTable Class](e68ce1c7-a922-d1b7-53bb-f832a4bad273.htm)   [See Also](#seeAlsoToggle) |

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

[ExportLayerTable Class](e68ce1c7-a922-d1b7-53bb-f832a4bad273.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d87f88a-4d97-baeb-7cf8-7d2991db5a75.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEmbedded Property

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Indicates if this is an embedded ScheduleDefinition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsEmbedded { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsEmbedded As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsEmbedded { 	bool get (); } ``` |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d89b166-9eb2-924b-7c8b-ec41508825d0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReferenceCategoryId Property

---



|  |
| --- |
| [MultiReferenceAnnotationType Class](046b4d91-40b3-4dd0-be1b-635fb30956c2.htm)   [See Also](#seeAlsoToggle) |

The category of elements to which this annotation applies.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ElementId ReferenceCategoryId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ReferenceCategoryId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ReferenceCategoryId { 	ElementId^ get (); } ``` |

# Remarks

The TagTypeId will be cleared because the user must set a new tag type of an appropriate category.

# See Also

[MultiReferenceAnnotationType Class](046b4d91-40b3-4dd0-be1b-635fb30956c2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d8a541a-5224-06de-b2e9-ef51e51a4dfb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CouldNotAcquireAssemblyViews Property

---



|  |
| --- |
| [BuiltInFailures AssemblyFailures Class](d1210198-fad4-6166-bafe-cf155e2dfafd.htm)   [See Also](#seeAlsoToggle) |

The assembly instance could not acquire the assembly views.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CouldNotAcquireAssemblyViews { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CouldNotAcquireAssemblyViews As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CouldNotAcquireAssemblyViews { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AssemblyFailures Class](d1210198-fad4-6166-bafe-cf155e2dfafd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d8f8735-b814-5ac0-e8c5-114da8caa7bc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [Material Class](2ec33007-7a2a-f86a-009b-d4c5d235a307.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new material.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ElementId Create( 	Document document, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	name As String _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ Create( 	Document^ document,  	String^ name ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to create the material.

name
:   Type:  System String    
     The name of the new material.

#### Return Value

Identifier of the new material.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
//Create the material
ElementId materialId = Material.Create(document, "My Material");
Material material = document.GetElement(materialId) as Material;

//Create a new property set that can be used by this material
StructuralAsset strucAsset = new StructuralAsset("My Property Set", StructuralAssetClass.Concrete);
strucAsset.Behavior = StructuralBehavior.Isotropic;
strucAsset.Density = 232.0;

//Assign the property set to the material.
PropertySetElement pse = PropertySetElement.Create(document, strucAsset);
material.SetMaterialAspectByPropertySet(MaterialAspect.Structural, pse.Id);
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
'Create the material
Dim materialId As ElementId = Material.Create(document, "My Material")
Dim material__1 As Material = TryCast(document.GetElement(materialId), Material)

'Create a new property set that can be used by this material
Dim strucAsset As New StructuralAsset("My Property Set", StructuralAssetClass.Concrete)
strucAsset.Behavior = StructuralBehavior.Isotropic
strucAsset.Density = 232.0

'Assign the property set to the material.
Dim pse As PropertySetElement = PropertySetElement.Create(document, strucAsset)
material__1.SetMaterialAspectByPropertySet(MaterialAspect.Structural, pse.Id)
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". -or- The given value for name is already in use as a material element name. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Material Class](2ec33007-7a2a-f86a-009b-d4c5d235a307.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d90af6c-9cca-1064-c240-6c1eb3277a88.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HideWhenNoValue Property

---



|  |
| --- |
| [ExternalDefinition Class](a3e84415-b88e-a8e0-4e11-64795d92da0e.htm)   [See Also](#seeAlsoToggle) |

Indicates whether this parameter should be hidden from the properties palette when it has no value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public bool HideWhenNoValue { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property HideWhenNoValue As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool HideWhenNoValue { 	bool get (); 	void set (bool value); } ``` |

#### Field Value

If true, the parameter will be hidden from the properties palette when it has no value. If false, the parameter will always be shown in the properties palette, no matter if it has a value or not.

# Remarks

Even when hidden, the parameter can still be accessed directly via the API.

# See Also

[ExternalDefinition Class](a3e84415-b88e-a8e0-4e11-64795d92da0e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d92da01-ee52-bab1-01fe-ac060a51a746.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PrinterResolution Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Controls the resolution level in rendering settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum PrinterResolution ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration PrinterResolution ``` |

 

| Visual C++ |
| --- |
| ``` public enum class PrinterResolution ``` |

# Members

| Member name | Description |
| --- | --- |
| Low | Low printer resolution. |
| Medium | Medium printer resolution. |
| High | High printer resolution. |
| VeryHigh | VeryHigh printer resolution. |

# Remarks

It is applicable only when using printer resolution. The suitable resolution value for each resolution level is decided by default in Revit.

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__5d9ab4ae-9c43-c7b7-f851-39f04ab95989.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CheckBuildingType Method

---



|  |
| --- |
| [EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)   [See Also](#seeAlsoToggle) |

Checks that the building type falls within an appropriate range.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static bool CheckBuildingType( 	gbXMLBuildingType buildingType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CheckBuildingType ( _ 	buildingType As gbXMLBuildingType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool CheckBuildingType( 	gbXMLBuildingType buildingType ) ``` |

#### Parameters

buildingType
:   Type:  [Autodesk.Revit.DB.Analysis gbXMLBuildingType](74e09dc3-6b9a-cc3b-a493-d6a20a60bfd6.htm)    
     The building type to be checked.

#### Return Value

True if the building type falls within an appropriate range, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__5d9b9a09-dd20-a79f-4e43-1f0365ed75be.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetWriteAccessLevel Method

---



|  |
| --- |
| [SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)   [See Also](#seeAlsoToggle) |

Sets top level write access (for entities)

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public SchemaBuilder SetWriteAccessLevel( 	AccessLevel writeAccessLevel ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetWriteAccessLevel ( _ 	writeAccessLevel As AccessLevel _ ) As SchemaBuilder ``` |

 

| Visual C++ |
| --- |
| ``` public: SchemaBuilder^ SetWriteAccessLevel( 	AccessLevel writeAccessLevel ) ``` |

#### Parameters

writeAccessLevel
:   Type:  [Autodesk.Revit.DB.ExtensibleStorage AccessLevel](60600a74-450d-a175-ce3d-12e91fb22cd2.htm)    
     Write access level value to be set

#### Return Value

The SchemaBuilder object may be used to add more settings.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The SchemaBuilder has already finished building the Schema. |

# See Also

[SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)

<!-- Start of Syntax__5d9c1584-347b-4f6d-9089-905edaa7bf09.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetEnumerator Method

---



|  |
| --- |
| [IFCAggregate Class](06bbeb56-efc6-1810-3111-f8ab4f615da1.htm)   [See Also](#seeAlsoToggle) |

Returns an enumerator that iterates through a collection.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public virtual IEnumerator<IFCData> GetEnumerator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function GetEnumerator As IEnumerator(Of IFCData) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual IEnumerator<IFCData^>^ GetEnumerator() ``` |

#### Return Value

An IEnumerator object that can be used to iterate through the collection.

#### Implements

 [IEnumerable T GetEnumerator](http://msdn2.microsoft.com/en-us/library/s793z9y2)

# See Also

[IFCAggregate Class](06bbeb56-efc6-1810-3111-f8ab4f615da1.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__5d9f248c-a1be-ac2e-1f4c-2219ed0fc5ae.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RefreshActiveView Method

---



|  |
| --- |
| [UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)   [See Also](#seeAlsoToggle) |

Refresh the display of the active view in the active document.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void RefreshActiveView() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RefreshActiveView ``` |

 

| Visual C++ |
| --- |
| ``` public: void RefreshActiveView() ``` |

# See Also

[UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__5d9f35bb-637d-8b8b-c2e5-816d08feea36.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApplicableSegmentLengthRounding Property

---



|  |
| --- |
| [FabricRoundingManager Class](6a6324cc-a18c-b883-1b1f-f2ad37147842.htm)   [See Also](#seeAlsoToggle) |

The applicable rounding for fabric segments.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public double ApplicableSegmentLengthRounding { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ApplicableSegmentLengthRounding As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ApplicableSegmentLengthRounding { 	double get (); } ``` |

# Remarks

IsActiveOnElement property of ReinforcementSettings RebarRoundingManager has to be true. ApplicableSegmentLengthRounding is meaningless if ReinforcementSettings RebarRoundingManager IsActiveOnElement is false.

# See Also

[FabricRoundingManager Class](6a6324cc-a18c-b883-1b1f-f2ad37147842.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)