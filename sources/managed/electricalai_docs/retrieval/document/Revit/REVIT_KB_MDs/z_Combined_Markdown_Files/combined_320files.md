

<!-- Start of Syntax__3befe4ef-682b-f101-c6a6-e54aa15adf04.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetClipRectangle Method

---



|  |
| --- |
| [DrawContext Class](b9244325-08c8-8bbd-a9f3-5d91d638d85d.htm)   [See Also](#seeAlsoToggle) |

Gets the clip rectangle for the Revit view where rendering takes place. The clip rectangle is the area currently being redrawn, which may be smaller than the view rectangle.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static Rectangle GetClipRectangle() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetClipRectangle As Rectangle ``` |

 

| Visual C++ |
| --- |
| ``` public: static Rectangle^ GetClipRectangle() ``` |

#### Return Value

The clip rectangle.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This DrawContext is not available because Revit is not currently rendering. In general, this DrawContext must be used in the scope of the RenderScene() callback of IDirectContext3DServer. |

# See Also

[DrawContext Class](b9244325-08c8-8bbd-a9f3-5d91d638d85d.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__3bf12e22-a943-c022-51ac-4cd62099dc94.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LayoutRule Property

---



|  |
| --- |
| [RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)   [See Also](#seeAlsoToggle) |

Identifies the layout rule of rebar set.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public RebarLayoutRule LayoutRule { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property LayoutRule As RebarLayoutRule 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property RebarLayoutRule LayoutRule { 	RebarLayoutRule get (); } ``` |

# See Also

[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3bf6d1da-663c-96e7-ec90-0b82f90efebb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetMapOfSizesForStraights Method

---



|  |
| --- |
| [FabricationNetworkChangeService Class](ddd58cb0-54bc-a864-9688-b890a7140112.htm)   [See Also](#seeAlsoToggle) |

Set the mapping for sizes of fabrication part straights to change the sizes to.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.2

# Syntax

| C# |
| --- |
| ``` public void SetMapOfSizesForStraights( 	ISet<FabricationPartSizeMap> fabricationPartSizeMaps ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetMapOfSizesForStraights ( _ 	fabricationPartSizeMaps As ISet(Of FabricationPartSizeMap) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetMapOfSizesForStraights( 	ISet<FabricationPartSizeMap^>^ fabricationPartSizeMaps ) ``` |

#### Parameters

fabricationPartSizeMaps
:   Type:  System.Collections.Generic ISet   [FabricationPartSizeMap](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.htm)    
     The map containing the original straights size to the mapped sizes.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationNetworkChangeService Class](ddd58cb0-54bc-a864-9688-b890a7140112.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)

<!-- Start of Syntax__3bf6e4f4-547c-40b6-acc3-63345f65536d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCopyWallPanelsWarn Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

Cannot copy wall panels unless their parent wall is also being copied.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCopyWallPanelsWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCopyWallPanelsWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCopyWallPanelsWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c04b790-a498-5342-eb88-7cdfa7e315cb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallBaseOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Base Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId WallBaseOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WallBaseOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ WallBaseOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c0c6506-90d2-3047-6716-07039388ae9f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureRealWorldScaleY Property

---



|  |
| --- |
| [Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Size Y" from the "Tile" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TextureRealWorldScaleY { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextureRealWorldScaleY As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TextureRealWorldScaleY { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDistance" with a minimum of "0.01".

# See Also

[Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3c14f25b-981f-0bfa-07a4-87a54d0df94d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NetworkCanNotDeterminCriticalPath Property

---



|  |
| --- |
| [BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)   [See Also](#seeAlsoToggle) |

The calculation has completed, but there may be an error in determining the critical path. Verify that demand flow is specified for all required elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NetworkCanNotDeterminCriticalPath { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NetworkCanNotDeterminCriticalPath As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NetworkCanNotDeterminCriticalPath { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c17c9e5-7018-1cf6-4a20-d8059cec370c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WireConduitType Class

---



|  |
| --- |
| [Members](5381641f-d1fb-959d-1ea0-18445ecd629f.htm)   [See Also](#seeAlsoToggle) |

Represents a specific conduit type of wire type.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class WireConduitType : APIObject ``` |

 

| Visual Basic |
| --- |
| ``` Public Class WireConduitType _ 	Inherits APIObject ``` |

 

| Visual C++ |
| --- |
| ``` public ref class WireConduitType : public APIObject ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB.Electrical WireConduitType

# See Also

[WireConduitType Members](5381641f-d1fb-959d-1ea0-18445ecd629f.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3c1a96f2-6934-8b25-4d18-71ee5fdd9d6a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LampLumenDepreciation Property

---



|  |
| --- |
| [AdvancedLossFactor Class](30e62a9d-eb01-8830-f897-dc8f32b486da.htm)   [See Also](#seeAlsoToggle) |

The lamp lumen depreciation loss factor.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double LampLumenDepreciation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LampLumenDepreciation As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double LampLumenDepreciation { 	double get (); 	void set (double value); } ``` |

#### Field Value

The loss factor as a numerical value between 0.0 and 1.0

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The loss factor is not valid because it is not between 0.0 and 1.0. |

# See Also

[AdvancedLossFactor Class](30e62a9d-eb01-8830-f897-dc8f32b486da.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__3c1ae512-f679-12ec-7b15-7b402ea6db3d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ColorSelectionDialog Class

---



|  |
| --- |
| [Members](78151cd7-f149-131f-a03f-48d6604f1402.htm)   [See Also](#seeAlsoToggle) |

Allows display of the Revit Color dialog.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public class ColorSelectionDialog : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ColorSelectionDialog _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ColorSelectionDialog : IDisposable ``` |

# Remarks

The class provides the option to launch the Revit Color dialog to select the color.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.UI ColorSelectionDialog

# See Also

[ColorSelectionDialog Members](78151cd7-f149-131f-a03f-48d6604f1402.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3c1dd101-57cd-d6ea-7e23-a81e0d5e45da.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotEditDeletedElements Property

---



|  |
| --- |
| [BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)   [See Also](#seeAlsoToggle) |

Can't edit the element. It was deleted in the Central Model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotEditDeletedElements { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotEditDeletedElements As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotEditDeletedElements { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c1f8fdd-21d1-5af2-954b-d64599710df3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FlangeThicknessLocation Property

---



|  |
| --- |
| [StructuralSectionHotRolled Class](60cc6328-1e99-2a7b-03fb-983e52350e55.htm)   [See Also](#seeAlsoToggle) |

Flange Thickness Location.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public double FlangeThicknessLocation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FlangeThicknessLocation As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double FlangeThicknessLocation { 	double get (); 	void set (double value); } ``` |

# See Also

[StructuralSectionHotRolled Class](60cc6328-1e99-2a7b-03fb-983e52350e55.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__3c1fa98d-c080-fc3a-d926-907a1882001d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PaneId Property

---



|  |
| --- |
| [DockableFrameFocusChangedEventArgs Class](1aa44a28-c45d-d77b-ced8-3b5cd5e582f3.htm)   [See Also](#seeAlsoToggle) |

The identifier for dockable pane.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public DockablePaneId PaneId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property PaneId As DockablePaneId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property DockablePaneId^ PaneId { 	DockablePaneId^ get (); } ``` |

# See Also

[DockableFrameFocusChangedEventArgs Class](1aa44a28-c45d-d77b-ced8-3b5cd5e582f3.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__3c2a642e-3c18-d149-7da2-6573bab9972e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SlabEdgeMaterialParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Material"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SlabEdgeMaterialParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SlabEdgeMaterialParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SlabEdgeMaterialParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c2d81cf-0ded-6d08-7547-bd9e06756614.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanCircuitSet Constructor

---



|  |
| --- |
| [PlanCircuitSet Class](8398c79d-1108-6846-cc0c-b7b2b5c1d026.htm)   [See Also](#seeAlsoToggle) |

Initializes a new instance of the  [PlanCircuitSet](8398c79d-1108-6846-cc0c-b7b2b5c1d026.htm)  class

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PlanCircuitSet() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: PlanCircuitSet() ``` |

# See Also

[PlanCircuitSet Class](8398c79d-1108-6846-cc0c-b7b2b5c1d026.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c2fe0d9-3c34-077a-63da-6549bbeaf852.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSuperscriptStatus Method

---



|  |
| --- |
| [FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)   [See Also](#seeAlsoToggle) |

Returns whether  [All](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  ,  [None](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  or a  [Mixed](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  of characters in the entire text are superscripted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public FormatStatus GetSuperscriptStatus() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSuperscriptStatus As FormatStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: FormatStatus GetSuperscriptStatus() ``` |

#### Return Value

The format status of superscript on characters  [FormatStatus](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  .

# Remarks

This function only returns  [All](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  or  [None](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  if the entire text contains one character.

# See Also

[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)

[GetSuperscriptStatus Overload](68e6c6df-ed20-52b7-025a-cb3c18b021b4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c302b80-d1f8-0e17-154a-b809cad2e545.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BreakCurve Method

---



|  |
| --- |
| [PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.htm)   [See Also](#seeAlsoToggle) |

Breaks the pipe curve into two parts at the given position.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static ElementId BreakCurve( 	Document document, 	ElementId pipeId, 	XYZ ptBreak ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function BreakCurve ( _ 	document As Document, _ 	pipeId As ElementId, _ 	ptBreak As XYZ _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ BreakCurve( 	Document^ document,  	ElementId^ pipeId,  	XYZ^ ptBreak ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

pipeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element id of the pipe curve to break.

ptBreak
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The break point on the pipe curve.

#### Return Value

The new pipe curve element id if successful otherwise if a failure occurred an invalidElementId is returned.

# Remarks

This method is not applicable for breaking the flex pipe.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | "The element is neither a pipe nor a pipe placeholder." -or- "The given point is not on the pipe curve." |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__3c311432-e04e-73f9-8b9f-0d50d9e27876.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoopSeparationNotCompleted Property

---



|  |
| --- |
| [BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)   [See Also](#seeAlsoToggle) |

The loop separation is not completed yet. Only one side of the secondary/tertiary loop is separated. In order to correctly calculate the flow and pressure loss, please check and separate the other end of the loop.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId LoopSeparationNotCompleted { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoopSeparationNotCompleted As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ LoopSeparationNotCompleted { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c391404-20c4-a2b1-0212-8b6ee350096c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Rad Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol rad, indicating unit Radians.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Rad { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Rad As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Rad { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c3c930b-ecd3-62e7-f94e-88e6915edd54.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalysisResultSchema Constructor (AnalysisResultSchema)

---



|  |
| --- |
| [AnalysisResultSchema Class](90969170-ac45-68e6-2527-f6fba5b3f7ae.htm)   [See Also](#seeAlsoToggle) |

Constructs a new copy of the input AnalysisResultSchema object.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public AnalysisResultSchema( 	AnalysisResultSchema other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	other As AnalysisResultSchema _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: AnalysisResultSchema( 	AnalysisResultSchema^ other ) ``` |

#### Parameters

other
:   Type:  [Autodesk.Revit.DB.Analysis AnalysisResultSchema](90969170-ac45-68e6-2527-f6fba5b3f7ae.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AnalysisResultSchema Class](90969170-ac45-68e6-2527-f6fba5b3f7ae.htm)

[AnalysisResultSchema Overload](0959e019-8678-62c9-1949-7b2a4603e3b3.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3c3ceb2f-be63-a79d-d5bf-c8b03caee472.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Efficacy Property

---



|  |
| --- |
| [InitialWattageIntensity Class](2bcbaf81-375c-2732-d67a-563d8302cd1e.htm)   [See Also](#seeAlsoToggle) |

The efficacy value.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double Efficacy { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Efficacy As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Efficacy { 	double get (); 	void set (double value); } ``` |

#### Field Value

The efficacy value in lm/W as a numerical value greater than 0.0 and less than 1.0e+10.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The efficacy value is not valid because it is not between 0 and 1e+30. |

# See Also

[InitialWattageIntensity Class](2bcbaf81-375c-2732-d67a-563d8302cd1e.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__3c452286-57b1-40e2-2795-c90bff1fcec2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundingBoxXYZ Class

---



|  |
| --- |
| [Members](d7e07baa-ee85-a6cd-3545-ff78502b221a.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A three-dimensional rectangular box at an arbitrary location and orientation within the Revit model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public class BoundingBoxXYZ : APIObject ``` |

 

| Visual Basic |
| --- |
| ``` Public Class BoundingBoxXYZ _ 	Inherits APIObject ``` |

 

| Visual C++ |
| --- |
| ``` public ref class BoundingBoxXYZ : public APIObject ``` |

# Remarks

BoundingBoxXYZ objects are used in Revit in several places related to views (for example, the section box of a 3D view or the definition of a section or detail view). BoundingBoxXYZ objects can also be obtained from elements representing the boundary of the element in a given view.

The extents of the box are determined by three orthogonal planes extended through the minimum (  [Min](608e6914-2465-b572-2c5d-2a6cd696c740.htm)  ) and maximum (  [Max](b79bd9ee-ccff-cc81-8a32-9eb9bdb1e58c.htm)  ) points, but the coordinates of these points and the orientation of the planes in relation to the coordinates of the source model is determined by the box Transform (  [Transform](297887ab-69bb-548e-cfb6-a3a23f410604.htm)  ).

This class also has the ability to detect and mark certain extents as disabled. Note that in the current Revit API uses of this class it is not expected that Revit will give objects with disabled extents, and disabled extents in objects sent to Revit will likely be ignored.

Note: the bounding box may not be empty even if Element::Geometry::get returns nothing. This can happen if the element contains no 3D model geometry since by default, Element::Geometry::get only returns 3D model geometry while GeometryElement::GetBoundingBox also takes 2D plan-view geometry and elevation-view geometry into account.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetBoundingBoxXYZInfo(View3D view3D)
{
    string message = "BoundingBoxXYZ : ";
    message += "\nView name : " + view3D.Name;
    BoundingBoxXYZ boundingBox = view3D.GetSectionBox();
    // The section box of the 3D view can cut the model.
    if (view3D.IsSectionBoxActive)
    {
        BoundingBoxXYZ sectionBox = view3D.GetSectionBox();

        // Note that the section box can be rotated and transformed.  
        // So the min/max corners coordinates relative to the model must be computed via the transform.
        Transform trf = sectionBox.Transform;

        XYZ max = sectionBox.Max; //Maximum coordinates (upper-right-front corner of the box before transform is applied).
        XYZ min = sectionBox.Min; //Minimum coordinates (lower-left-rear corner of the box before transform is applied).

        // Transform the min and max to model coordinates
        XYZ maxInModelCoords = trf.OfPoint(max);
        XYZ minInModelCoords = trf.OfPoint(min);

        message += "\nView has an active section box: ";
        message += "\n'Maximum' coordinates: " + maxInModelCoords;
        message += "\n'Minimum' coordinates: " + minInModelCoords;
    }
    TaskDialog.Show("Revit", message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetBoundingBoxXYZInfo(view3D As View3D)
    Dim message As String = "BoundingBoxXYZ : "
    message += vbLf & "View name : " + view3D.Name
    Dim boundingBox As BoundingBoxXYZ = view3D.GetSectionBox()
    ' The section box of the 3D view can cut the model.
    If view3D.IsSectionBoxActive Then
        Dim sectionBox As BoundingBoxXYZ = view3D.GetSectionBox()

        ' Note that the section box can be rotated and transformed.  
        ' So the min/max corners coordinates relative to the model must be computed via the transform.
        Dim trf As Transform = sectionBox.Transform

        Dim max As XYZ = sectionBox.Max
        'Maximum coordinates (upper-right-front corner of the box before transform is applied).
        Dim min As XYZ = sectionBox.Min
        'Minimum coordinates (lower-left-rear corner of the box before transform is applied).
        ' Transform the min and max to model coordinates
        Dim maxInModelCoords As XYZ = trf.OfPoint(max)
        Dim minInModelCoords As XYZ = trf.OfPoint(min)

        message += vbLf & "View has an active section box: "
        message += vbLf & "Maximum' coordinates: " + maxInModelCoords.ToString()
        message += vbLf & "Minimum' coordinates: " + minInModelCoords.ToString()
    End If
    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB BoundingBoxXYZ

# See Also

[BoundingBoxXYZ Members](d7e07baa-ee85-a6cd-3545-ff78502b221a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c468c0e-2269-193b-b339-91e8117bdea2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MassDataMassOpeningArea Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Mass Opening Area"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MassDataMassOpeningArea { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MassDataMassOpeningArea As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MassDataMassOpeningArea { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c4b263f-22a1-27a1-8fb4-2e66aa964e8e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShowSettings Method

---



|  |
| --- |
| [IPipeFittingAndAccessoryPressureDropUIServer Interface](727a30e8-f519-3192-0e4b-0d86bc537c0c.htm)   [See Also](#seeAlsoToggle) |

Shows the settings UI.

**Namespace:**   [Autodesk.Revit.UI.Plumbing](a4cc3644-f568-6568-9c2f-dcdb6eafdf6b.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` bool ShowSettings( 	PipeFittingAndAccessoryPressureDropUIData data ) ``` |

 

| Visual Basic |
| --- |
| ``` Function ShowSettings ( _ 	data As PipeFittingAndAccessoryPressureDropUIData _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` bool ShowSettings( 	PipeFittingAndAccessoryPressureDropUIData^ data ) ``` |

#### Parameters

data
:   Type:  [Autodesk.Revit.UI.Plumbing PipeFittingAndAccessoryPressureDropUIData](6dcc2335-c5a0-2122-82ed-566efa781f41.htm)    
     The input data of the calculation.

#### Return Value

True if the user makes any changes in the UI, false otherwise.

# See Also

[IPipeFittingAndAccessoryPressureDropUIServer Interface](727a30e8-f519-3192-0e4b-0d86bc537c0c.htm)

[Autodesk.Revit.UI.Plumbing Namespace](a4cc3644-f568-6568-9c2f-dcdb6eafdf6b.htm)

<!-- Start of Syntax__3c4b62c8-372c-a09d-53f4-5c5247ad0929.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadNatureName Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Name"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LoadNatureName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoadNatureName As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LoadNatureName { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c4bca7d-e030-22e2-cb4b-634dcb9a30f9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DownloadFinished Property

---



|  |
| --- |
| [CreateRelatedFileProgressChangedEventArgs Class](94a4184c-e0d2-a846-ba1d-52cea6b0a29f.htm)   [See Also](#seeAlsoToggle) |

Indicates if all data downloads are finished.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool DownloadFinished { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property DownloadFinished As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool DownloadFinished { 	bool get (); } ``` |

# See Also

[CreateRelatedFileProgressChangedEventArgs Class](94a4184c-e0d2-a846-ba1d-52cea6b0a29f.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__3c4e0c18-8133-ec1b-41a2-ed92c918e44c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NamingUtils Class

---



|  |
| --- |
| [Members](e9a552da-0418-7db1-bee8-c0a895ab62c2.htm)   [See Also](#seeAlsoToggle) |

A collection of utilities related to element naming.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static class NamingUtils ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class NamingUtils ``` |

 

| Visual C++ |
| --- |
| ``` public ref class NamingUtils abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB NamingUtils

# See Also

[NamingUtils Members](e9a552da-0418-7db1-bee8-c0a895ab62c2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c5057a7-b59e-c650-0d46-643f3bae218d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLabelFor Method (BuiltInCategory)

---



|  |
| --- |
| [LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.htm)   [See Also](#seeAlsoToggle) |

Gets the user-visible name for a BuiltInCategory.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public static string GetLabelFor( 	BuiltInCategory builtInCategory ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetLabelFor ( _ 	builtInCategory As BuiltInCategory _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ GetLabelFor( 	BuiltInCategory builtInCategory ) ``` |

#### Parameters

builtInCategory
:   Type:  [Autodesk.Revit.DB BuiltInCategory](ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.htm)    
     The BuiltInCategory to get the user-visible name.

# Remarks

The name is obtained in the current Revit language.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the builtin category is not valid. |

# See Also

[LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.htm)

[GetLabelFor Overload](39e41221-70f9-fae6-53e6-872eff5a2c63.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c54b11b-724a-cd4c-0b80-abcd141fada7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExcessLengthFillSpacing Property

---



|  |
| --- |
| [BalusterPattern Class](bb7868e3-0665-07e5-59e4-a95efb3079ab.htm)   [See Also](#seeAlsoToggle) |

The value defines the spacing between each baluster instance inserted in the excess length.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public double ExcessLengthFillSpacing { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExcessLengthFillSpacing As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ExcessLengthFillSpacing { 	double get (); 	void set (double value); } ``` |

# Remarks

The spacing is used only if a baluster family is set to excess length fill.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for excessLengthFillSpacing must be between 0 and 30000 feet. |

# See Also

[BalusterPattern Class](bb7868e3-0665-07e5-59e4-a95efb3079ab.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__3c54b2eb-2378-c692-4c00-46088b684604.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImportPlacement Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing possible placement modes for imported drawings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2013   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum ImportPlacement ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ImportPlacement ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ImportPlacement ``` |

# Members

| Member name | Description |
| --- | --- |
| Site | Placement at Base Point. Useful for Revit links only. There must be a reference point in order for this option to be valid. |
| Origin | Placement at the Origin. If reference point is provided, then the import is placed so the point is at the model's origin. If no point is provided, then the document's origin is matched with the model's origin. |
| Centered | Placement at the Center. If reference point is provided, then the import is placed so the point is at the model's center. If no point is provided, then the document's center is matched with the model's origin. |
| Shared | Placement with respect to the shared coordinates. Revit Building places the imported geometry according to its location with respect to the shared coordinates between the two files. There must be shared coordinates in a Revit document in order for this option to be valid. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c54cedc-bdbd-fb2c-2250-cb7387a5c3d4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewActivatedEventArgs Class

---



|  |
| --- |
| [Members](24c9982d-8f77-7ec0-c78b-7aafed99bc51.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by the ViewActivated event.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public class ViewActivatedEventArgs : RevitAPIPostDocEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ViewActivatedEventArgs _ 	Inherits RevitAPIPostDocEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ViewActivatedEventArgs : public RevitAPIPostDocEventArgs ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPostEventArgs](93554f52-0145-3454-5697-3f1015e46434.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPostDocEventArgs](7d3fba7a-5efb-6a4c-a49c-16c25f972830.htm)    
  Autodesk.Revit.UI.Events ViewActivatedEventArgs

# See Also

[ViewActivatedEventArgs Members](24c9982d-8f77-7ec0-c78b-7aafed99bc51.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__3c55684a-b4fd-851e-3b32-6a3eb1e9eb3b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetProjectionToSheetTransform Method

---



|  |
| --- |
| [Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.htm)   [See Also](#seeAlsoToggle) |

Returns the transform from the view's projection space to the sheet space.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public Transform GetProjectionToSheetTransform() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetProjectionToSheetTransform As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform^ GetProjectionToSheetTransform() ``` |

#### Return Value

The transform from the view's projection space to the sheet space.

# Remarks

This transform accounts for the position and rotation of a viewport on a sheet.

The transforms from the model space to the view projection space are returned by  [!:View.GetModelToProjectionTransforms()]  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The viewport is not on a sheet. -or- The viewport does not have transforms. |

# See Also

[Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c559c45-263f-d72d-a443-99bce9bf56e7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Tonsf Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol Tonsf, indicating unit US tonnes force.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Tonsf { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Tonsf As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Tonsf { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c55ae48-f75d-ca61-2d6d-961b7bd464ec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomNumberOfPeopleParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Number of People"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RoomNumberOfPeopleParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoomNumberOfPeopleParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RoomNumberOfPeopleParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c573ec2-8a88-d20a-a445-b218d44e15a2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureRealWorldOffsetX Property

---



|  |
| --- |
| [Gradient Class](2b517b49-c915-74a9-bb6f-2a233d6706be.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Offset X" from the "Gradient" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TextureRealWorldOffsetX { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextureRealWorldOffsetX As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TextureRealWorldOffsetX { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDistance".

# See Also

[Gradient Class](2b517b49-c915-74a9-bb6f-2a233d6706be.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3c58145e-085c-7b1e-f680-280406f72e9a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CouplerMark Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Schedule Mark"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CouplerMark { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CouplerMark As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CouplerMark { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c5bb767-5e7a-0080-45e9-c16b161a0e10.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEmpty Property

---



|  |
| --- |
| [MEPSystem Class](65946955-8638-fafb-2657-ef7cb7b2941b.htm)   [See Also](#seeAlsoToggle) |

Indicates if the system is empty or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool IsEmpty { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsEmpty As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsEmpty { 	bool get (); } ``` |

# Remarks

returns true if the system doesn't contain any components

# See Also

[MEPSystem Class](65946955-8638-fafb-2657-ef7cb7b2941b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c5c36cc-3c70-7c30-bf06-8777966e6e81.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsPipingSystemTypeParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"System Type"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsPipingSystemTypeParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsPipingSystemTypeParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsPipingSystemTypeParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c5c4efb-8960-869f-76c0-338979e5a484.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetGeometricalObjects Method

---



|  |
| --- |
| [TessellatedShapeBuilderResult Class](16e1e032-d9fd-2708-0704-ed00b0b85441.htm)   [See Also](#seeAlsoToggle) |

When called the first time, returns geometrical objects which were built. Later calls will throw exceptions.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IList<GeometryObject> GetGeometricalObjects() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetGeometricalObjects As IList(Of GeometryObject) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<GeometryObject^>^ GetGeometricalObjects() ``` |

#### Return Value

Geometrical object which were built.

# Remarks

Normally an array contains a single geometrical object corresponding to either 'target' or 'fallback' type', but if multiple face sets are being built with target/fallback of "AnyGeometry/Mesh", then a two-element array with both geometry as the 1st element and mesh as the 2nd can be returned. It happens if some of the face sets require a fallback processing and some do not.

# See Also

[TessellatedShapeBuilderResult Class](16e1e032-d9fd-2708-0704-ed00b0b85441.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c63095d-6fc7-4cb2-e20d-e90c3d966fcd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewSolarstudyStillDateValue Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Still date"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ViewSolarstudyStillDateValue { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewSolarstudyStillDateValue As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ViewSolarstudyStillDateValue { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c64e1bd-1db3-0a71-c9fa-f70e136cd676.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

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

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c66db61-6009-622d-d76c-33d1371da401.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SourceDocument Property

---



|  |
| --- |
| [TransferringProjectStandardsEventArgs Class](ffc4e960-25e8-9edb-f660-d328c57e65d0.htm)   [See Also](#seeAlsoToggle) |

Source document.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017.2

# Syntax

| C# |
| --- |
| ``` public Document SourceDocument { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property SourceDocument As Document 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Document^ SourceDocument { 	Document^ get (); } ``` |

# See Also

[TransferringProjectStandardsEventArgs Class](ffc4e960-25e8-9edb-f660-d328c57e65d0.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__3c68a291-cbf5-77c9-d15b-e8ed49d8d9f2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsShownOnlyWhenCut Property

---



|  |
| --- |
| [FamilyElementVisibility Class](fae58e2d-817c-77f6-1747-58b0a4e01c7a.htm)   [See Also](#seeAlsoToggle) |

Indicates if the instance is displayed only if it has been cut.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsShownOnlyWhenCut { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsShownOnlyWhenCut As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsShownOnlyWhenCut { 	bool get (); 	void set (bool value); } ``` |

# Remarks

This property matters for objects which visibility type is ViewSpecific.

# See Also

[FamilyElementVisibility Class](fae58e2d-817c-77f6-1747-58b0a4e01c7a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c6c1387-182e-3871-fd1f-12c5eeec65f7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarSystemTopMinorMatchesBottomMinor Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top and Bottom Minor Layers Match"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarSystemTopMinorMatchesBottomMinor { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarSystemTopMinorMatchesBottomMinor As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarSystemTopMinorMatchesBottomMinor { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c6c3cb9-9fa0-ecbf-c6a3-1ef77d783708.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ArrowheadTypeId Property

---



|  |
| --- |
| [StairsPathType Class](36994970-3d80-62a3-df6f-381d38f2eda0.htm)   [See Also](#seeAlsoToggle) |

The arrow head type of the stairs path.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId ArrowheadTypeId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ArrowheadTypeId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ArrowheadTypeId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The arrowheadTypeId is not a valid arrow head type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[StairsPathType Class](36994970-3d80-62a3-df6f-381d38f2eda0.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__3c703fb8-89c6-84fd-73b2-4b45d28a765d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NothingToApplyWarning Property

---



|  |
| --- |
| [BuiltInFailures ViewFailures Class](8aa2d60d-e642-4717-3c73-63e56e49f8ec.htm)   [See Also](#seeAlsoToggle) |

Start and end elevations are the same, nothing to Apply.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NothingToApplyWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NothingToApplyWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NothingToApplyWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ViewFailures Class](8aa2d60d-e642-4717-3c73-63e56e49f8ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c7045d7-7493-4f10-cb94-715a0c922b39.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DistanceFromPreviousOrSpace Property

---



|  |
| --- |
| [BalusterInfo Class](96a6917f-9f36-2e9a-3f94-a42ff103fff0.htm)   [See Also](#seeAlsoToggle) |

The length, in case of balusters, it is a distance from a previous one. For a post, it is a space from the original position of the post.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public double DistanceFromPreviousOrSpace { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DistanceFromPreviousOrSpace As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double DistanceFromPreviousOrSpace { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for distanceFromPreviousOrSpace is not finite |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for distanceFromPreviousOrSpace must be greater than 0 and no more than 30000 feet. |

# See Also

[BalusterInfo Class](96a6917f-9f36-2e9a-3f94-a42ff103fff0.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__3c73e808-b8fb-ed1f-c490-8b08f6df50dd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InvalidCropAreaSketchRegen Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Crop area sketch can either be empty or include one closed, not self-intersecting loop.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId InvalidCropAreaSketchRegen { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InvalidCropAreaSketchRegen As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ InvalidCropAreaSketchRegen { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c74565b-6322-14ed-26b0-c6fc85f6d2e8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumberOfUGridlines Property

---



|  |
| --- |
| [DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)   [See Also](#seeAlsoToggle) |

Get the number of U-gridlines used on the surface.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int NumberOfUGridlines { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property NumberOfUGridlines As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int NumberOfUGridlines { 	int get (); } ``` |

# See Also

[DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c769108-6b9e-96e8-98bf-7793098265cb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetProductListEntryName Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Gets the specified product list entry name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016 Subscription Release

# Syntax

| C# |
| --- |
| ``` public string GetProductListEntryName( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetProductListEntryName ( _ 	index As Integer _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetProductListEntryName( 	int index ) ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The product entry index.

#### Return Value

Returns the specified product entry name.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The product entry index is not larger than 0 and less than GetProductCount. |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c77cb29-49f5-a5d1-9bcf-32e1565abdc5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PaperSourceSet Constructor

---



|  |
| --- |
| [PaperSourceSet Class](d8c1d4df-2afd-bf11-c8ba-729475c6324e.htm)   [See Also](#seeAlsoToggle) |

Initializes a new instance of the  [PaperSourceSet](d8c1d4df-2afd-bf11-c8ba-729475c6324e.htm)  class

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PaperSourceSet() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: PaperSourceSet() ``` |

# See Also

[PaperSourceSet Class](d8c1d4df-2afd-bf11-c8ba-729475c6324e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c7a78d5-f92b-e58b-e7c9-7927537498fd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarHookType Class

---



|  |
| --- |
| [Members](c9d03086-c1ac-b486-e1a1-19a4a0398879.htm)   [See Also](#seeAlsoToggle) |

A Rebar Hook type object that is used in the generation of Rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class RebarHookType : ElementType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RebarHookType _ 	Inherits ElementType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RebarHookType : public ElementType ``` |

# Remarks

This object contains the definition of the hooks that may be created at the ends of the rebar. The specifics of these hooks are angle (range 0-PI) between first/last segment of rebar and the straight segment of the hook, rebar shape style and a multiplier used to compute the length of the straight segment of the hook. The default length is computed as the bar diameter \* the multiplier. Length can be overridden by settings in the RebarBarType class.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  Autodesk.Revit.DB.Structure RebarHookType

# See Also

[RebarHookType Members](c9d03086-c1ac-b486-e1a1-19a4a0398879.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3c7c4e3a-4ea2-6306-d804-911e80934d93.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CableTraySize Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Cable Tray Size, in discipline Electrical.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CableTraySize { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CableTraySize As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CableTraySize { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c81b4e4-de4b-44df-8f80-d90c60976dec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Space Property

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [See Also](#seeAlsoToggle) |

The space in which the instance is located (during the last phase of the project).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Space Space { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Space As Space 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Space^ Space { 	Space^ get (); } ``` |

# Remarks

This property will be the first space encountered that contains the instance. If more than one space includes this point in its volume only the first one is returned. If no space is found that contains the instance, this property is    a null reference (  Nothing  in Visual Basic)  .

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Space Overload](983a485b-e825-e91b-8fc2-b00436819169.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c856db3-000f-0701-2c98-0166f725c53f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [AnalysisDisplayDiagramSettings Class](57e0c5ff-555c-7345-ac24-3592207a4d70.htm)   [See Also](#seeAlsoToggle) |

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

[AnalysisDisplayDiagramSettings Class](57e0c5ff-555c-7345-ac24-3592207a4d70.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3c8b70b1-7e86-3c06-8f9c-87d73b50b89c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetGlobal2DOriginHandle Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Obtains the handle representing the 2D origin.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static IFCAnyHandle GetGlobal2DOriginHandle() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetGlobal2DOriginHandle As IFCAnyHandle ``` |

 

| Visual C++ |
| --- |
| ``` public: static IFCAnyHandle^ GetGlobal2DOriginHandle() ``` |

#### Return Value

The handle.

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__3c8c8e94-e1d6-ed14-a4b0-6c9b9237923e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DividedpathDistance Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Distance"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DividedpathDistance { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DividedpathDistance As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DividedpathDistance { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c90d55b-be33-3aad-a01c-3dc71407218f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [RevitLinkOptions Class](3f710983-5a4d-d515-a633-12b06a419b30.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [RevitLinkOptions](3f710983-5a4d-d515-a633-12b06a419b30.htm)

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

[RevitLinkOptions Class](3f710983-5a4d-d515-a633-12b06a419b30.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c913e04-4444-319e-04bb-61a4784b5d4d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RegisterDockablePane Method

---



|  |
| --- |
| [UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Adds a new dockable pane to the Revit user interface.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void RegisterDockablePane( 	DockablePaneId id, 	string title, 	IDockablePaneProvider provider ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RegisterDockablePane ( _ 	id As DockablePaneId, _ 	title As String, _ 	provider As IDockablePaneProvider _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RegisterDockablePane( 	DockablePaneId^ id,  	String^ title,  	IDockablePaneProvider^ provider ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.UI DockablePaneId](96149d8e-6393-9285-a721-76470e6c15b8.htm)    
     Unique identifier for the new pane.

title
:   Type:  System String    
     String to use for the pane caption.

provider
:   Type:  [Autodesk.Revit.UI IDockablePaneProvider](cde36571-ccf1-f628-9e34-6a720388d348.htm)    
     Your add-in's implementation of the IDockablePaneProvider interface.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public Result OnStartup(UIControlledApplication application)
{
   // Create our pane provider and register it with the application
   PaneProvider prov = new PaneProvider();
   DockablePaneId id = new DockablePaneId(Guid.NewGuid());
   application.RegisterDockablePane(id, "test", prov);

   return Result.Succeeded;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Function OnStartup(application As UIControlledApplication) As Result Implements IExternalApplication.OnStartup
    ' Create our pane provider and register it with the application
    Dim prov As New PaneProvider()
    Dim id As New DockablePaneId(Guid.NewGuid())
    application.RegisterDockablePane(id, "test", prov)

    Return Result.Succeeded
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if a dockable pane with identifier %id% has already been registered. |

# See Also

[UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3c93daf3-82ed-b686-57ff-6e80f06c618e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FindTypeByName Method

---



|  |
| --- |
| [MEPAnalyticalConnectionType Class](a0840c90-ffe0-fc59-7af3-022967128828.htm)   [See Also](#seeAlsoToggle) |

Finds the analytical connection type by its name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static ElementId FindTypeByName( 	Document doc, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function FindTypeByName ( _ 	doc As Document, _ 	name As String _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ FindTypeByName( 	Document^ doc,  	String^ name ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document where the analytical conneciton type is expected.

name
:   Type:  System String    
     The name of the expected analytical connection type.

#### Return Value

The element id of matched analytical connection type, otherwise invalidElementId.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name is an empty string. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MEPAnalyticalConnectionType Class](a0840c90-ffe0-fc59-7af3-022967128828.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c97307b-b9ec-a24d-4e68-3685b93aff43.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DividedSurfaceAllPoints Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Show all points"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DividedSurfaceAllPoints { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DividedSurfaceAllPoints As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DividedSurfaceAllPoints { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3c9ba970-9fa8-914e-07a2-7918b52f5df0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlignPartByInsertionPoint Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Align the part by its insertion point to a point and rotation in free space.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static bool AlignPartByInsertionPoint( 	Document document, 	ElementId partId, 	XYZ position, 	double rotation, 	double rotationPerpendicular, 	double slope, 	FabricationPartJustification justification, 	Transform trf ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function AlignPartByInsertionPoint ( _ 	document As Document, _ 	partId As ElementId, _ 	position As XYZ, _ 	rotation As Double, _ 	rotationPerpendicular As Double, _ 	slope As Double, _ 	justification As FabricationPartJustification, _ 	trf As Transform _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool AlignPartByInsertionPoint( 	Document^ document,  	ElementId^ partId,  	XYZ^ position,  	double rotation,  	double rotationPerpendicular,  	double slope,  	FabricationPartJustification justification,  	Transform^ trf ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

partId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element identifier of the part to align.

position
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The position to move the part's insertion point to.

rotation
:   Type:  System Double    
     The rotation in radians.

rotationPerpendicular
:   Type:  System Double    
     The perpendicular rotation for free placement around the Y axis direction of connection - angle in radians.

slope
:   Type:  System Double    
     The slope value to flex to match if possible in fractional units (eg.1/50). Positive values are up, negative are down. Slopes can only be applied to fittings, whilst straights will inherit the slope from the piece it is connecting to.

justification
:   Type:  [Autodesk.Revit.DB.Fabrication FabricationPartJustification](5c6c9daf-4547-01f1-9ba8-39a970ca9e68.htm)    
     The justification to align eccentric parts.

trf
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     Optional alignment transformation matrix, eg. a Trf that describes plan or side elevation.

#### Return Value

True if the alignment succeeds, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element is not a fabrication part. -or- Not all of the fabrication part's connectors are open. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ca04b0b-1f42-6ad2-5bcd-af1c1dd5e58f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DefaultParamaterValuesIncorrect Property

---



|  |
| --- |
| [BuiltInFailures RebarShapeFailures Class](7e0a8c39-c873-730e-6ffd-2fc6d6f71f3e.htm)   [See Also](#seeAlsoToggle) |

Default parameters have incorrect values. One reason for failure might be an edge length that is too short (it's smaller than bent radius).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DefaultParamaterValuesIncorrect { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DefaultParamaterValuesIncorrect As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DefaultParamaterValuesIncorrect { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarShapeFailures Class](7e0a8c39-c873-730e-6ffd-2fc6d6f71f3e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ca7bd7c-d7fd-64a7-da94-139d768d871d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PanelTypeSet Class

---



|  |
| --- |
| [Members](5bfead00-7360-4157-89c0-d912b97b91d7.htm)   [See Also](#seeAlsoToggle) |

A set that contains panel types.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class PanelTypeSet : APIObject,  	IEnumerable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PanelTypeSet _ 	Inherits APIObject _ 	Implements IEnumerable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PanelTypeSet : public APIObject,  	IEnumerable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB PanelTypeSet

# See Also

[PanelTypeSet Members](5bfead00-7360-4157-89c0-d912b97b91d7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cad9a34-eb3e-0889-4288-28c5cf2662d8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CutForegroundPatternColor Property

---



|  |
| --- |
| [Material Class](2ec33007-7a2a-f86a-009b-d4c5d235a307.htm)   [See Also](#seeAlsoToggle) |

The color of the material cut foreground pattern.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public Color CutForegroundPatternColor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CutForegroundPatternColor As Color 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Color^ CutForegroundPatternColor { 	Color^ get (); 	void set (Color^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[Material Class](2ec33007-7a2a-f86a-009b-d4c5d235a307.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cb0b20a-0f27-60ca-0ce0-54f22acee0c8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WinderFilletRadiusTooLargeFailure Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

The value for Fillet Radius is too large to satisfy the Minimum Inside Width value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId WinderFilletRadiusTooLargeFailure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WinderFilletRadiusTooLargeFailure As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ WinderFilletRadiusTooLargeFailure { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cb5994d-0d75-dd1a-7602-9be344366919.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarBarDiameter Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bar Diameter"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarBarDiameter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarBarDiameter As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarBarDiameter { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cbb6ef9-6234-672a-3705-205b43e1da17.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Weights Property

---



|  |
| --- |
| [NurbSpline Class](65c43ffe-3972-ae2b-4aa4-e2901cdbb3a8.htm)   [See Also](#seeAlsoToggle) |

Returns the weights of the nurb spline.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public DoubleArray Weights { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Weights As DoubleArray 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property DoubleArray^ Weights { 	DoubleArray^ get (); } ``` |

# See Also

[NurbSpline Class](65c43ffe-3972-ae2b-4aa4-e2901cdbb3a8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cc137bd-4b9c-e0c8-f93a-14536a11bd18.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Start Method (ElementId, ElementId)

---



|  |
| --- |
| [StairsEditScope Class](47e4576e-4b01-ed1f-6dc1-885b6780aa07.htm)   [See Also](#seeAlsoToggle) |

Creates a new empty stairs element with a default stairs type in the specified levels and then starts stairs edit mode and editing the new stairs.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId Start( 	ElementId baseLevelId, 	ElementId topLevelId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Start ( _ 	baseLevelId As ElementId, _ 	topLevelId As ElementId _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ Start( 	ElementId^ baseLevelId,  	ElementId^ topLevelId ) ``` |

#### Parameters

baseLevelId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The base level on which the stairs is to be placed.

topLevelId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The top level where the stairs is to reach.

#### Return Value

ElementId of the new stairs.

# Remarks

A new stairs will be created after this operation. User will need to start a transaction to actually make changes to the stairs element. StairsEditScope can only be started when there is no transaction active Thus it does not work for commands running in automatic transaction mode.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | It is not a Level's id. -or- Top level should be higher than base level. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This StairsEditScope is not permitted to start at this moment for one of the following possible reasons: The document is in read-only state, or the document is currently modifiable, or there already is another edit mode active in the document. |

# See Also

[StairsEditScope Class](47e4576e-4b01-ed1f-6dc1-885b6780aa07.htm)

[Start Overload](f81f3ffd-4ed2-2917-1f2e-353433272c88.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cc426b3-e4e1-dbe8-1130-9a79c9541bfa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.AlignmentFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](d6f3982f-0126-8066-44c5-ea21ba7c8b77.htm)   [See Also](#seeAlsoToggle) |

Failures related to alignment elements and annotations.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public static class AlignmentFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class AlignmentFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class AlignmentFailures abstract sealed ``` |

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB BuiltInFailures AlignmentFailures

# See Also

[BuiltInFailures AlignmentFailures Members](d6f3982f-0126-8066-44c5-ea21ba7c8b77.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cc4983a-3d57-95d9-71f9-39144254c839.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LeaderEndPosition Property

---



|  |
| --- |
| [DimensionSegment Class](36b254a0-3dc5-7bdc-d6b4-986e5d82ddbf.htm)   [See Also](#seeAlsoToggle) |

The position of the dimension leader end point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2015 Subscription Update.

# Syntax

| C# |
| --- |
| ``` public XYZ LeaderEndPosition { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LeaderEndPosition As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ LeaderEndPosition { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

This property is not applicable to all dimensions. For example, it is not available for spot dimensions, dimensions using equality formula, and when dimension style is ordinate.

If the position is not applicable, this property returns NULL and will not allow setting a value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.htm) | Thrown when the dimension text is unavailable. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when:  * The dimension text is a SpotElevation * When using equality formula. * When dimension style is ordinate. |

# See Also

[DimensionSegment Class](36b254a0-3dc5-7bdc-d6b4-986e5d82ddbf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cc86cde-7898-e314-2eb2-fd9fc0c9a895.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CollectGeometryInfo Method (ExporterIFC, IFCGeometryInfo, GeometryObject, XYZ, Boolean)

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Collects all the target geometry from the input geometry object and adds it as IFC handles to the IFCInfo.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static void CollectGeometryInfo( 	ExporterIFC exporterIFC, 	IFCGeometryInfo geometryInfo, 	GeometryObject gNode, 	XYZ offset, 	bool forceVisible ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub CollectGeometryInfo ( _ 	exporterIFC As ExporterIFC, _ 	geometryInfo As IFCGeometryInfo, _ 	gNode As GeometryObject, _ 	offset As XYZ, _ 	forceVisible As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void CollectGeometryInfo( 	ExporterIFC^ exporterIFC,  	IFCGeometryInfo^ geometryInfo,  	GeometryObject^ gNode,  	XYZ^ offset,  	bool forceVisible ) ``` |

#### Parameters

exporterIFC
:   Type:  [Autodesk.Revit.DB.IFC ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.htm)    
     The exporter.

geometryInfo
:   Type:  [Autodesk.Revit.DB.IFC IFCGeometryInfo](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)    
     The container object which collects the geometry.

gNode
:   Type:  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
     The geometry object to be processed.

offset
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The offset to apply to each of the collected geometry handles.

forceVisible
:   Type:  System Boolean    
     True to process geometry which is not set as visible. False to only process visible geometry.

# Remarks

The type of geometry collected is determined by the method of creation for the IFCGeometryInfo.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[CollectGeometryInfo Overload](056fa367-794e-d4af-6dd2-3a4d6f4db467.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__3cca92eb-843c-45a3-d4d6-6b6880b0ff61.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NotAllPartsWereConvertedCannotAddPlaceholderWarning Property

---



|  |
| --- |
| [BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)   [See Also](#seeAlsoToggle) |

Not all parts were converted. Placeholders could not be added to fill the gap (the gap was too small). Check the fabrication service definition for the system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NotAllPartsWereConvertedCannotAddPlaceholderWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NotAllPartsWereConvertedCannotAddPlaceholderWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NotAllPartsWereConvertedCannotAddPlaceholderWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ccb2457-63ec-c918-abfa-94662ce6650f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PaperOrientation Property

---



|  |
| --- |
| [PDFExportOptions Class](e4236fc8-f8e7-fc74-1b81-9e3a4d9e966b.htm)   [See Also](#seeAlsoToggle) |

Paper orientation - Portrait/Landscape/Auto

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public PageOrientationType PaperOrientation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PaperOrientation As PageOrientationType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property PageOrientationType PaperOrientation { 	PageOrientationType get (); 	void set (PageOrientationType value); } ``` |

# Remarks

Ignored when the PaperFormat is ExportPaperFormat.Default, which means "Use Sheet Size".

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[PDFExportOptions Class](e4236fc8-f8e7-fc74-1b81-9e3a4d9e966b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ccbda07-3d25-cfaa-3098-90cdd283fe97.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Rounding Property

---



|  |
| --- |
| [AnalysisDisplayVectorSettings Class](2e74462f-4216-f6eb-d560-87a1b103e87e.htm)   [See Also](#seeAlsoToggle) |

Increment to which numeric values of analysis results are rounded in vectors.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double Rounding { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Rounding As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Rounding { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | When setting this property: rounding is not positive |

# See Also

[AnalysisDisplayVectorSettings Class](2e74462f-4216-f6eb-d560-87a1b103e87e.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3cd02844-a37b-9a93-e926-7d7f32450839.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PerformanceAdviserRuleId Class

---



|  |
| --- |
| [Members](470e6070-ed9a-d25a-3347-796ab6db4269.htm)   [See Also](#seeAlsoToggle) |

The unique identifier of a PerformanceAdviserRule

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class PerformanceAdviserRuleId : GuidEnum ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PerformanceAdviserRuleId _ 	Inherits GuidEnum ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PerformanceAdviserRuleId : public GuidEnum ``` |

# Remarks

Each performance adviser rule registered in application must be given a unique id that can be used to identify and unregister rule later.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB GuidEnum](36623d19-ba65-63c0-337a-f43c593a9931.htm)    
  Autodesk.Revit.DB PerformanceAdviserRuleId

# See Also

[PerformanceAdviserRuleId Members](470e6070-ed9a-d25a-3347-796ab6db4269.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cd08582-405c-b589-d9a5-23b09929bdae.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurtaingridAnglen1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Angle"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CurtaingridAnglen1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CurtaingridAnglen1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CurtaingridAnglen1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cd5237d-bef2-7a12-f0e3-43318820f75a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetReleaseType Method

---



|  |
| --- |
| [AnalyticalMember Class](57c87ac5-a82e-5c7e-2f06-6dbf1f697566.htm)   [See Also](#seeAlsoToggle) |

Gets the release type.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public ReleaseType GetReleaseType( 	bool start ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetReleaseType ( _ 	start As Boolean _ ) As ReleaseType ``` |

 

| Visual C++ |
| --- |
| ``` public: ReleaseType GetReleaseType( 	bool start ) ``` |

#### Parameters

start
:   Type:  System Boolean    
     The position on Analytical Member element. True for start, false for end.

#### Return Value

The type of release.

# See Also

[AnalyticalMember Class](57c87ac5-a82e-5c7e-2f06-6dbf1f697566.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3cd7e56a-f168-5a3e-2e53-92a8d842ea5f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InsertComponentViewError Property

---



|  |
| --- |
| [BuiltInFailures ViewFailures Class](8aa2d60d-e642-4717-3c73-63e56e49f8ec.htm)   [See Also](#seeAlsoToggle) |

This type of Component cannot be placed in Elevation or Section view

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId InsertComponentViewError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InsertComponentViewError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ InsertComponentViewError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ViewFailures Class](8aa2d60d-e642-4717-3c73-63e56e49f8ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ce14b4a-0907-1787-2390-2ef11e8df2cc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBasicIEnumerator Method

---



|  |
| --- |
| [ExportLinetypeTable Class](136c6197-2f4c-5686-e70c-09cee48b71ad.htm)   [See Also](#seeAlsoToggle) |

Returns an enumerator that iterates through a collection.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` internal virtual IEnumerator GetBasicIEnumerator() ``` |

 

| Visual Basic |
| --- |
| ``` Friend Overridable Function GetBasicIEnumerator As IEnumerator ``` |

 

| Visual C++ |
| --- |
| ``` internal: virtual IEnumerator^ GetBasicIEnumerator() ``` |

#### Return Value

An IEnumerator object that can be used to iterate through the collection.

#### Implements

 [IEnumerable GetEnumerator](http://msdn2.microsoft.com/en-us/library/5zae5365)

# See Also

[ExportLinetypeTable Class](136c6197-2f4c-5686-e70c-09cee48b71ad.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ce4d82f-7f24-8ee9-bf28-f9b49f113971.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ExportLayerInfo](88a99694-968a-99f7-870a-f46737bd5927.htm)

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

[ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cf16c33-dc3d-9ca5-40f5-cfca5ce591f7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCopyMustBeUniqueViewportWarn Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

Multiple instances of the same view in sheets not supported. CannotCopyMustBeUniqueViewportWarn is deprecated in Revit 2023 and may be removed in future verison of Revit. Please use ViewInAModelMustBeUniqueWarn instead.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCopyMustBeUniqueViewportWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCopyMustBeUniqueViewportWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCopyMustBeUniqueViewportWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cf1e3b4-bb36-e276-8459-f21da70a6cc4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SheetScheduled Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Appears In Sheet List"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SheetScheduled { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SheetScheduled As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SheetScheduled { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cf616a4-1d0c-a568-f6df-cf505563f1e2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoofLevelOffsetParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Base Offset From Level"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RoofLevelOffsetParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoofLevelOffsetParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RoofLevelOffsetParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cf71958-5d6c-5484-90af-e7e020886874.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecPanelTotalloadPowerParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Power Total Connected"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecPanelTotalloadPowerParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecPanelTotalloadPowerParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecPanelTotalloadPowerParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cf77bb2-3780-296e-0d19-698a289098eb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, Element, XYZ, ElementId, ElementId, ElementId)

---



|  |
| --- |
| [AreaReinforcement Class](889aa3cf-9b32-dd78-b660-bcfbad2cf87e.htm)   [See Also](#seeAlsoToggle) |

Creates a new AreaReinforcement object based on a host boundary.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static AreaReinforcement Create( 	Document document, 	Element hostElement, 	XYZ majorDirection, 	ElementId areaReinforcementTypeId, 	ElementId rebarBarTypeId, 	ElementId rebarHookTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	hostElement As Element, _ 	majorDirection As XYZ, _ 	areaReinforcementTypeId As ElementId, _ 	rebarBarTypeId As ElementId, _ 	rebarHookTypeId As ElementId _ ) As AreaReinforcement ``` |

 

| Visual C++ |
| --- |
| ``` public: static AreaReinforcement^ Create( 	Document^ document,  	Element^ hostElement,  	XYZ^ majorDirection,  	ElementId^ areaReinforcementTypeId,  	ElementId^ rebarBarTypeId,  	ElementId^ rebarHookTypeId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

hostElement
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element that will host the AreaReinforcement. The host can be a Structural Floor, Structural Wall, Structural Slab, or a Part created from a structural layer belonging to one of those element types.

majorDirection
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     A vector to define the major direction of the AreaReinforcement.

areaReinforcementTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the AreaReinforcementType.

rebarBarTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the RebarBarType.

rebarHookTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the RebarHookType. If this parameter is InvalidElementId, it means to create a rebar with no hooks.

#### Return Value

The newly created AreaReinforcement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element hostElement was not found in the given document. -or- the host Element is not a valid host for Area Reinforcement, Path Reinforcement, Fabric Area or Fabric Sheet. -or- areaReinforcementTypeId should refer to an AreaReinforcementType element. -or- rebarBarTypeId should refer to an RebarBarType element. -or- rebarHookTypeId should be invalid or refer to an RebarHookType element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | majorDirection has zero length. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | This method may not be called during dynamic update. |

# See Also

[AreaReinforcement Class](889aa3cf-9b32-dd78-b660-bcfbad2cf87e.htm)

[Create Overload](ce8506a4-9d6f-ef8b-fd9e-9f79edeb936e.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3cf8c9dc-f4d1-12f0-d7a9-e126331cd858.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveElements Method

---



|  |
| --- |
| [ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.htm)   [See Also](#seeAlsoToggle) |

Moves a set of elements by a given transformation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static void MoveElements( 	Document document, 	ICollection<ElementId> elementsToMove, 	XYZ translation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub MoveElements ( _ 	document As Document, _ 	elementsToMove As ICollection(Of ElementId), _ 	translation As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void MoveElements( 	Document^ document,  	ICollection<ElementId^>^ elementsToMove,  	XYZ^ translation ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document that owns the elements.

elementsToMove
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The set of elements to move.

translation
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The translation vector for the elements.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given element id set is empty. -or- One or more elements in elementsToMove do not exist in the document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | If we are not able to move all the elements (for example, if one or more elements is pinned). -or- Move operation failed. |

# See Also

[ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3cfd44c9-9b82-bac2-a532-ad6eec073248.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MinRunWidth Property

---



|  |
| --- |
| [StairsType Class](efa84f53-19fa-039b-c5bb-8fcb72e09878.htm)   [See Also](#seeAlsoToggle) |

The initial value for the width of a common run.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double MinRunWidth { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MinRunWidth As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double MinRunWidth { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for minRunWidth must be greater than 0 and no more than 30000 feet. |

# See Also

[StairsType Class](efa84f53-19fa-039b-c5bb-8fcb72e09878.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__3cfda085-5bba-a1d2-1a40-0f2872a6ef22.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanHaveTypeAssigned Method (Document, ICollection(ElementId))

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Checks if all elements in the set can have a type assigned.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static bool CanHaveTypeAssigned( 	Document document, 	ICollection<ElementId> elementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CanHaveTypeAssigned ( _ 	document As Document, _ 	elementIds As ICollection(Of ElementId) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool CanHaveTypeAssigned( 	Document^ document,  	ICollection<ElementId^>^ elementIds ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

elementIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A collection of element IDs.

#### Return Value

True if all elements in the set can have a type assigned, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when at least one of the elements does not exist in the document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[CanHaveTypeAssigned Overload](a75f62de-8d3f-aad9-3577-4767c019edf6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d018bf9-651c-7d7f-38b0-6a37f95a9124.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetMeasurementDescriptions Method

---



|  |
| --- |
| [SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)   [See Also](#seeAlsoToggle) |

Sets Descriptions for all measurements

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetMeasurementDescriptions( 	IList<string> measurementDescriptions ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetMeasurementDescriptions ( _ 	measurementDescriptions As IList(Of String) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetMeasurementDescriptions( 	IList<String^>^ measurementDescriptions ) ``` |

#### Parameters

measurementDescriptions
:   Type:  System.Collections.Generic IList   String    
     Array of measurement descriptions. The lengths of the array must be equal to the number of measurements set during creation of SpatialFieldManager.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | measurementDescriptions lengths is not equal to the number of measurements set during creation of SpatialFieldManager |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3d01a5ed-3c9f-fde4-4899-5a6ef76f7199.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ModelPath Class](40a84c72-e4b8-72ac-2f71-3216c66a11b3.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ModelPath](40a84c72-e4b8-72ac-2f71-3216c66a11b3.htm)

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

[ModelPath Class](40a84c72-e4b8-72ac-2f71-3216c66a11b3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d01ba8a-bf7a-b89b-573d-6c8113aa17f6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ExportLayerTableIterator Class](24174426-8fd0-a24c-8ee0-1d32532e6f77.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ExportLayerTableIterator](24174426-8fd0-a24c-8ee0-1d32532e6f77.htm)

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

# See Also

[ExportLayerTableIterator Class](24174426-8fd0-a24c-8ee0-1d32532e6f77.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d05ec79-0289-c6d1-2a13-7e6b07241afd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WireMaterialType Class

---



|  |
| --- |
| [Members](170c5182-235b-2f41-cbde-f551dcf2ab76.htm)   [See Also](#seeAlsoToggle) |

Represents electrical wire material type definition information of wire type.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class WireMaterialType : ElementType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class WireMaterialType _ 	Inherits ElementType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class WireMaterialType : public ElementType ``` |

# Remarks

All the other properties of wire type are based on wire material type. Only the wire material types which are retrieved from ElectricalSetting can work well, so don't retrieve it from Revit project directly.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  Autodesk.Revit.DB.Electrical WireMaterialType

# See Also

[WireMaterialType Members](170c5182-235b-2f41-cbde-f551dcf2ab76.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3d0d6481-e2b2-c2d3-f6f5-5dedb761c241.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RiserIntWithBoundaryMoreThanOnceFailure Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Riser intersects with boundary more than once.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RiserIntWithBoundaryMoreThanOnceFailure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RiserIntWithBoundaryMoreThanOnceFailure As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RiserIntWithBoundaryMoreThanOnceFailure { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d109321-6a47-f148-e0c8-812fb0c19de2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecCircuitPathModeParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Path Mode"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecCircuitPathModeParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecCircuitPathModeParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecCircuitPathModeParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d159400-28fb-9f92-b4b1-1aab870c21f0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsReaction Property

---



|  |
| --- |
| [LoadBase Class](4130f6dc-1963-2105-d85b-e08a7c34af8b.htm)   [See Also](#seeAlsoToggle) |

The load is reaction option.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool IsReaction { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsReaction As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsReaction { 	bool get (); 	void set (bool value); } ``` |

# See Also

[LoadBase Class](4130f6dc-1963-2105-d85b-e08a7c34af8b.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3d161566-8205-4056-521f-b0a868290170.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotMergeGeometry Property

---



|  |
| --- |
| [BuiltInFailures MassFailures Class](c9804646-1735-fe87-b758-a466adf5eae8.htm)   [See Also](#seeAlsoToggle) |

The Mass contains geometry that cannot be combined. Mass Floors, volume, and surface area, won't be computed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotMergeGeometry { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotMergeGeometry As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotMergeGeometry { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MassFailures Class](c9804646-1735-fe87-b758-a466adf5eae8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d16af11-f577-0496-4281-733064dc330a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPresureDropItems Method

---



|  |
| --- |
| [DuctFittingAndAccessoryPressureDropData Class](5411567a-c556-61ec-a41b-182d2277d8a5.htm)   [See Also](#seeAlsoToggle) |

Returns the pressure drop items.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public IList<DuctFittingAndAccessoryPressureDropItem> GetPresureDropItems() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPresureDropItems As IList(Of DuctFittingAndAccessoryPressureDropItem) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<DuctFittingAndAccessoryPressureDropItem^>^ GetPresureDropItems() ``` |

# See Also

[DuctFittingAndAccessoryPressureDropData Class](5411567a-c556-61ec-a41b-182d2277d8a5.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__3d1f5129-decb-de77-7bf1-7e4fd4f675d3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MinimumLength Property

---



|  |
| --- |
| [RouteAnalysisSettings Class](e6742b6a-9c35-5344-736b-7bf9af6f4254.htm)   [See Also](#seeAlsoToggle) |

The constant storing minimum allowed length of path of travel

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public double MinimumLength { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property MinimumLength As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double MinimumLength { 	double get (); } ``` |

# See Also

[RouteAnalysisSettings Class](e6742b6a-9c35-5344-736b-7bf9af6f4254.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3d25d1d7-367e-039c-0681-5c6549701c86.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GraphicDisplayOptionsSketchyLines Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Sketchy Lines"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId GraphicDisplayOptionsSketchyLines { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GraphicDisplayOptionsSketchyLines As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ GraphicDisplayOptionsSketchyLines { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d2a12de-0c85-da2d-006c-e5b3714ebdf4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetInsulationIds Method

---



|  |
| --- |
| [InsulationLiningBase Class](938d1b57-b9bb-44b0-81ec-c22dff57fc8e.htm)   [See Also](#seeAlsoToggle) |

Returns the ids of the insulation elements associated to a given element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetInsulationIds( 	Document document, 	ElementId elemId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetInsulationIds ( _ 	document As Document, _ 	elemId As ElementId _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetInsulationIds( 	Document^ document,  	ElementId^ elemId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

elemId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element.

#### Return Value

A collection of the ids of the insulation elements.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This id does not represent a valid host for insulation. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[InsulationLiningBase Class](938d1b57-b9bb-44b0-81ec-c22dff57fc8e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d2abac5-bc09-eaf3-598f-f6c0d3661f16.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SheetNumberEmpty Property

---



|  |
| --- |
| [BuiltInFailures SheetFailures Class](78c58be5-64f9-fef3-8379-0445640c964f.htm)   [See Also](#seeAlsoToggle) |

Sheet Number is empty

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SheetNumberEmpty { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SheetNumberEmpty As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SheetNumberEmpty { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SheetFailures Class](78c58be5-64f9-fef3-8379-0445640c964f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d357c63-7ac9-01d1-7468-ebd4a3bf998a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSpecificFittingAngleStatus Method

---



|  |
| --- |
| [DuctSettings Class](cd632c8e-a520-2efb-a417-9dfa5677d134.htm)   [See Also](#seeAlsoToggle) |

Gets the status of given specific angle.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool GetSpecificFittingAngleStatus( 	double angle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSpecificFittingAngleStatus ( _ 	angle As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool GetSpecificFittingAngleStatus( 	double angle ) ``` |

#### Parameters

angle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The specific fitting angle (in degree) that must be one of 90, 60, 45, 30, 22.5 or 11.25 degrees.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for angle must be 90, 60, 45, 30, 22.5 or 11.25 degrees. |

# See Also

[DuctSettings Class](cd632c8e-a520-2efb-a417-9dfa5677d134.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__3d36d4c2-f736-db7b-ae6a-945f89dce0b9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ValidateCurve Method (Curve, DirectShapeTargetViewType)

---



|  |
| --- |
| [ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)   [See Also](#seeAlsoToggle) |

Validates curve to be added to the view-specific shape being constructed. Called by AddCurve() to validate input. This function may be used to pre-validate the geometry being added to avoid AddCurve() throwing an InvalidArgumentException

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static bool ValidateCurve( 	Curve GCurve, 	DirectShapeTargetViewType targetViewType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ValidateCurve ( _ 	GCurve As Curve, _ 	targetViewType As DirectShapeTargetViewType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ValidateCurve( 	Curve^ GCurve,  	DirectShapeTargetViewType targetViewType ) ``` |

#### Parameters

GCurve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     Curve object to be validated.

targetViewType
:   Type:  [Autodesk.Revit.DB DirectShapeTargetViewType](1c5cd94e-3804-54da-73af-505655b0948f.htm)    
     View type for which this curve is intended.

#### Return Value

True is %GCurve% is acceptable as a part of view-specific shape representation.

# Remarks

Validation conditions depend on the type of view for which the shape representation is intended. For plan views, a curve is expected to be planar and non-degenerate (e.g., NOT a circle of zero radius).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)

[ValidateCurve Overload](b4a33128-d93f-0ac3-61d6-de0f4b771872.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d37cd81-48ba-4011-82bc-dbb7ae14b270.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurrentType Property

---



|  |
| --- |
| [FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)   [See Also](#seeAlsoToggle) |

The current family type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyType CurrentType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CurrentType As FamilyType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property FamilyType^ CurrentType { 	FamilyType^ get (); 	void set (FamilyType^ value); } ``` |

# Remarks

Only the current family type is editable using the methods in  [FamilyManager](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)  . If you want to modify the properties of any family type, it must be set to be the current type first. This value will be    a null reference (  Nothing  in Visual Basic)  if there is no type in the family. In order to modify parameter values, you will need to create one using  [NewType(String)](b46e98b1-54a1-7e04-66b7-a35efe5bc3f8.htm)  .

# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d399dee-e13d-b3f5-7f8c-32ba0910b5d5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CoarseScaleFillPatternIdParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Coarse Scale Fill Pattern"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CoarseScaleFillPatternIdParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CoarseScaleFillPatternIdParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CoarseScaleFillPatternIdParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d3b817b-e9df-a898-b562-eb4ae8f2ab0f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadAreaForceFy2 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Fy 2"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LoadAreaForceFy2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoadAreaForceFy2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LoadAreaForceFy2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d4b2969-fe55-7b1a-bdc0-b60165e12856.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FilteredWorksetIdIterator Class

---



|  |
| --- |
| [Members](97cff188-4f8b-0a50-bd67-de554b29806d.htm)   [See Also](#seeAlsoToggle) |

An iterator to a set of workset ids filtered by the settings of a FilteredWorksetCollector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class FilteredWorksetIdIterator : IEnumerator<WorksetId> ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FilteredWorksetIdIterator _ 	Implements IEnumerator(Of WorksetId) ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FilteredWorksetIdIterator : IEnumerator<WorksetId^> ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB FilteredWorksetIdIterator

# See Also

[FilteredWorksetIdIterator Members](97cff188-4f8b-0a50-bd67-de554b29806d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d4c1b04-f574-7ff5-cac3-0c14e80b74ee.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPointConstraintType Method

---



|  |
| --- |
| [AdaptiveComponentFamilyUtils Class](6fdc0a79-5217-21b2-122d-b1987180cc5b.htm)   [See Also](#seeAlsoToggle) |

Sets constrain type of an Adaptive Shape Handle Point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static void SetPointConstraintType( 	Document doc, 	ElementId refPointId, 	AdaptivePointConstraintType constraintType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SetPointConstraintType ( _ 	doc As Document, _ 	refPointId As ElementId, _ 	constraintType As AdaptivePointConstraintType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SetPointConstraintType( 	Document^ doc,  	ElementId^ refPointId,  	AdaptivePointConstraintType constraintType ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document

refPointId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ReferencePoint id

constraintType
:   Type:  [Autodesk.Revit.DB AdaptivePointConstraintType](9aa479aa-36be-bf1b-7570-026afcd4d02e.htm)    
     Constraint type of the Adaptive Shape Handle Point.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The ElementId refPointId does not correspond to a valid ReferencePoint. -or- The Element corresponding to ElementId refPointId does not belong to an Adaptive Family. -or- The ElementId refPointId does not correspond to a Shape Handle Point. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation failed. |

# See Also

[AdaptiveComponentFamilyUtils Class](6fdc0a79-5217-21b2-122d-b1987180cc5b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d55db12-8517-135f-1a63-9a1446c64480.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionGeneralT Constructor

---



|  |
| --- |
| [StructuralSectionGeneralT Class](308dc954-e403-b95c-3f1c-3a9a4c22beaf.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of Tees shape.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public StructuralSectionGeneralT( 	double width, 	double height, 	double flangeThickness, 	double flangeThicknessLocation, 	double flangeFillet, 	double flangeToeOfFillet, 	double slopedFlangeAngle, 	double webThickness, 	double webThicknessLocation, 	double webFillet, 	double topWebFillet, 	double webToeOfFillet, 	double slopedWebAngle, 	double centroidHorizontal, 	double centroidVertical, 	StructuralSectionAnalysisParams analysisParams ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	width As Double, _ 	height As Double, _ 	flangeThickness As Double, _ 	flangeThicknessLocation As Double, _ 	flangeFillet As Double, _ 	flangeToeOfFillet As Double, _ 	slopedFlangeAngle As Double, _ 	webThickness As Double, _ 	webThicknessLocation As Double, _ 	webFillet As Double, _ 	topWebFillet As Double, _ 	webToeOfFillet As Double, _ 	slopedWebAngle As Double, _ 	centroidHorizontal As Double, _ 	centroidVertical As Double, _ 	analysisParams As StructuralSectionAnalysisParams _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: StructuralSectionGeneralT( 	double width,  	double height,  	double flangeThickness,  	double flangeThicknessLocation,  	double flangeFillet,  	double flangeToeOfFillet,  	double slopedFlangeAngle,  	double webThickness,  	double webThicknessLocation,  	double webFillet,  	double topWebFillet,  	double webToeOfFillet,  	double slopedWebAngle,  	double centroidHorizontal,  	double centroidVertical,  	StructuralSectionAnalysisParams^ analysisParams ) ``` |

#### Parameters

width
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Section width.

height
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Section height, depth.

flangeThickness
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Flange Thickness.

flangeThicknessLocation
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Flange Thickness Location.

flangeFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Flange Fillet - fillet radius at the flange end.

flangeToeOfFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Detailing distance from center of web to flange toe of fillet, in. (mm)

slopedFlangeAngle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Sloped flange angle. (rad)

webThickness
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Web Thickness.

webThicknessLocation
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Web Thickness Location.

webFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Web Fillet - fillet radius between web and flange.

topWebFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Top Web Fillet - fillet radius at the top of web.

webToeOfFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Detailing distance from outer face of flange to web toe of fillet, in. (mm)

slopedWebAngle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Sloped web angle. (rad)

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

[StructuralSectionGeneralT Class](308dc954-e403-b95c-3f1c-3a9a4c22beaf.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__3d587a64-ba7b-4b9c-a9dd-cc96a871efa9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCreateGeometryForPipe Property

---



|  |
| --- |
| [BuiltInFailures PipingFailures Class](315ce880-e60a-1af9-bdf9-09ac738260c6.htm)   [See Also](#seeAlsoToggle) |

Cannot create geometry for flex pipe. The flex pipe is intersecting itself or the start and end are too close together.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCreateGeometryForPipe { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCreateGeometryForPipe As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCreateGeometryForPipe { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures PipingFailures Class](315ce880-e60a-1af9-bdf9-09ac738260c6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d5943e5-deb3-2daf-e528-78d498e6b038.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidIssue Method

---



|  |
| --- |
| [TessellatedBuildIssue Class](123454f4-f295-c687-213b-da97c032aba6.htm)   [See Also](#seeAlsoToggle) |

Reports whether the issue is well-formed, valid and does describe a real problem.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool IsValidIssue() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidIssue As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidIssue() ``` |

#### Return Value

Whether the issue is well formed and does describe a real problem.

# See Also

[TessellatedBuildIssue Class](123454f4-f295-c687-213b-da97c032aba6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d59ebc3-3585-0411-f17a-4ec0abebdb8a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSolidInView Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Checks if this rebar element is shown solidly in a 3D view.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` [ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit. The Rebar will always be shown solidly in 3D views with Fine level of detail. To change this, you can override the detail level of view for Structural Rebar category.")] public bool IsSolidInView( 	View3D view ) ``` |

 

| Visual Basic |
| --- |
| ``` <ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit. The Rebar will always be shown solidly in 3D views with Fine level of detail. To change this, you can override the detail level of view for Structural Rebar category.")> _ Public Function IsSolidInView ( _ 	view As View3D _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` [ObsoleteAttribute(L"This method is deprecated in Revit 2023 and may be removed in a later version of Revit. The Rebar will always be shown solidly in 3D views with Fine level of detail. To change this, you can override the detail level of view for Structural Rebar category.")] public: bool IsSolidInView( 	View3D^ view ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View3D](d795a238-fc24-1875-e64f-a2bef56ae949.htm)    
     The 3D view element

#### Return Value

True if rebar is shown solidly, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | This rebar element doesn't have valid visibility data. |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3d625bdb-4227-a923-8a1a-fc8076f9d4f6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CommonButtons Property

---



|  |
| --- |
| [TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)   [See Also](#seeAlsoToggle) |

The push buttons displayed in the task dialog.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public TaskDialogCommonButtons CommonButtons { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CommonButtons As TaskDialogCommonButtons 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property TaskDialogCommonButtons CommonButtons { 	TaskDialogCommonButtons get (); 	void set (TaskDialogCommonButtons value); } ``` |

# Remarks

If no common button or CommandLink is added to the task dialog, the dialog will contain the Close common button by default.

Revit task dialogs are following these conventions for commit button usage:

* Use a single Close button instead of a single OK button on informational messages.
* Use a question at the end of the Main Instruction with a Yes/No combo (or Yes/No/Cancel) instead of OK/Cancel. This should work 99% of the time. For example: "Are you sure you want to overwrite the file?" and use Yes/No buttons.
* Do not customize the button names unless there is a very good reason to do so. For example, "Are you sure you want to save the file?" would use Yes/No buttons and not Save/No or Save/Cancel.

# See Also

[TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3d652d69-084c-3f2b-f966-e95760a6f038.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetSurfaceNumber Method

---



|  |
| --- |
| [DefaultDivideSettings Class](c4d57a70-3192-458c-faa7-619d11c69f60.htm)   [See Also](#seeAlsoToggle) |

Sets the default Divided Surface number for a fixed number layout for U or V gridlines.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void SetSurfaceNumber( 	UVGridlineType gridlines, 	int number ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetSurfaceNumber ( _ 	gridlines As UVGridlineType, _ 	number As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetSurfaceNumber( 	UVGridlineType gridlines,  	int number ) ``` |

#### Parameters

gridlines
:   Type:  [Autodesk.Revit.DB UVGridlineType](df2bed21-2c63-f165-27be-8004ea2f7ad0.htm)    
     U-gridlines or V-gridlines.

number
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     A default number for a fixed number layout.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for number is not positive. -or- A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[DefaultDivideSettings Class](c4d57a70-3192-458c-faa7-619d11c69f60.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d656cd3-778a-efa7-a3a8-2ee090025491.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PropertySetKeywords Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Keywords"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PropertySetKeywords { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PropertySetKeywords As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PropertySetKeywords { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d6a14b7-0399-2ef9-8685-cbfaaf7739cf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VoltageTypeSet Class

---



|  |
| --- |
| [Members](c4d395bb-387a-9805-5a69-fba9149e8b3c.htm)   [See Also](#seeAlsoToggle) |

A set that contains voltage types.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class VoltageTypeSet : APIObject,  	IEnumerable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class VoltageTypeSet _ 	Inherits APIObject _ 	Implements IEnumerable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class VoltageTypeSet : public APIObject,  	IEnumerable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB.Electrical VoltageTypeSet

# See Also

[VoltageTypeSet Members](c4d395bb-387a-9805-5a69-fba9149e8b3c.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3d6a3a24-feb8-013c-f6d4-09e40c57ca14.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpotElevBase Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Elevation Base"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpotElevBase { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpotElevBase As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpotElevBase { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d6b0eb5-ed36-278d-a5df-38b6d600e876.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleField Class

---



|  |
| --- |
| [Members](0376a7dd-0c9e-1b11-0c8c-924ee6e6a3de.htm)   [See Also](#seeAlsoToggle) |

A field in a schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class ScheduleField : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ScheduleField _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ScheduleField : IDisposable ``` |

# Remarks

The ScheduleField class represents a single field in a ScheduleDefinition's list of fields. Each (non-hidden) field becomes a column in the schedule.

Most commonly, a field represents an instance or type parameter of elements appearing in the schedule. Some fields represent parameters of other related elements, like the room that a scheduled element belongs to. Fields can also represent data calculated from other fields in the schedule, specifically Formula and Percentage fields.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ScheduleField

# See Also

[ScheduleField Members](0376a7dd-0c9e-1b11-0c8c-924ee6e6a3de.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d6f0d5d-fa47-adac-3c9c-fa4f1c4691d1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ZeroLengthSegmentWarning Property

---



|  |
| --- |
| [BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)   [See Also](#seeAlsoToggle) |

The solution is failing to do segments which are zero length.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ZeroLengthSegmentWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ZeroLengthSegmentWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ZeroLengthSegmentWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d7248c5-558d-60ba-42da-c3b46d35f1cd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReferenceLevel Property

---



|  |
| --- |
| [MEPCurve Class](38714847-0f40-7021-aa79-2884c3a02ce2.htm)   [See Also](#seeAlsoToggle) |

The reference level of the MEP curve.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Level ReferenceLevel { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ReferenceLevel As Level 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Level^ ReferenceLevel { 	Level^ get (); 	void set (Level^ value); } ``` |

# Remarks

This property is used to retrieve the reference level of the MEP curve. If the curve is not in a horizontal plane, this value will be the start point's reference level.

# See Also

[MEPCurve Class](38714847-0f40-7021-aa79-2884c3a02ce2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d73a7f1-905c-59f4-bfcf-05bf7aa549ce.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reset Method

---



|  |
| --- |
| [WireConduitTypeSetIterator Class](d6f64a0b-6752-6df6-821d-9f8bb85f4ab3.htm)   [See Also](#seeAlsoToggle) |

Bring the iterator back to the start of the set.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
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

[WireConduitTypeSetIterator Class](d6f64a0b-6752-6df6-821d-9f8bb85f4ab3.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3d752980-c4ea-6a3b-3708-c00ae5c377e5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLayerModifiers Method

---



|  |
| --- |
| [ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.htm)   [See Also](#seeAlsoToggle) |

Gets all the project layer modifiers from the layer info.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public IList<LayerModifier> GetLayerModifiers() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLayerModifiers As IList(Of LayerModifier) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<LayerModifier^>^ GetLayerModifiers() ``` |

#### Return Value

The project layer modifier array.

# See Also

[ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d7add45-c7bf-279c-dbe9-d99556add8fa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsGreaterThan Method

---



|  |
| --- |
| [MathComparisonUtils Class](ddb32a4c-b742-0286-36b5-e5f2ce0d1daf.htm)   [See Also](#seeAlsoToggle) |

Checks if value1 is strictly greater than value2, using the internal tolerance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static bool IsGreaterThan( 	double value1, 	double value2 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsGreaterThan ( _ 	value1 As Double, _ 	value2 As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsGreaterThan( 	double value1,  	double value2 ) ``` |

#### Parameters

value1
:   Type:  System Double    
     The first value.

value2
:   Type:  System Double    
     The second value.

#### Return Value

True if value1 is strictly greater than value2, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for value1 is not finite -or- The given value for value2 is not finite |

# See Also

[MathComparisonUtils Class](ddb32a4c-b742-0286-36b5-e5f2ce0d1daf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d7dc58d-83c0-f515-7575-b7bdf85e5b55.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCGenericImportWarning Property

---



|  |
| --- |
| [BuiltInFailures ImportFailures Class](37a5e9d1-ffe4-363f-2033-1cabbf5634aa.htm)   [See Also](#seeAlsoToggle) |

The following problems were encountered in the IFC file: [Description]

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId IFCGenericImportWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property IFCGenericImportWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ IFCGenericImportWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ImportFailures Class](37a5e9d1-ffe4-363f-2033-1cabbf5634aa.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d85968c-3b73-0fe4-8ff8-ffedf05bf723.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [LeaderArray Class](65617b56-3f9f-447b-8b24-66eda86f684a.htm)   [See Also](#seeAlsoToggle) |

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

[LeaderArray Class](65617b56-3f9f-447b-8b24-66eda86f684a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d85c12a-7b46-49d9-aed7-a120f1951e2f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextBoxData Constructor

---



|  |
| --- |
| [TextBoxData Class](36a6ad8e-237b-6ca4-07d4-3cadb1ebb6dd.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of TextBoxData.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public TextBoxData( 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	name As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: TextBoxData( 	String^ name ) ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The internal name of the TextBoxData.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when    a null reference (  Nothing  in Visual Basic)  is passed for name. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when an empty string is passed for name. |

# See Also

[TextBoxData Class](36a6ad8e-237b-6ca4-07d4-3cadb1ebb6dd.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3d863213-6baf-3eaf-79f4-8f92a294bc93.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApplyTo Property

---



|  |
| --- |
| [StructuralConnectionType Class](e3b74cf3-71d8-a230-7fb6-0fdc4c81fca2.htm)   [See Also](#seeAlsoToggle) |

Choose whether this connection type applies to beams and braces, to tops of columns, or to bases of columns.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public StructuralConnectionApplyTo ApplyTo { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ApplyTo As StructuralConnectionApplyTo 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property StructuralConnectionApplyTo ApplyTo { 	StructuralConnectionApplyTo get (); } ``` |

# Remarks

The property cannot be changed. Create a new StructuralConnectionType if a different value is needed.

# See Also

[StructuralConnectionType Class](e3b74cf3-71d8-a230-7fb6-0fdc4c81fca2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3d87dd54-a970-c09b-c113-d2e700cd2f0f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DockPosition Property

---



|  |
| --- |
| [DockablePaneState Class](0255200b-8af3-3254-ca6b-043f5cc291cf.htm)   [See Also](#seeAlsoToggle) |

Which part of the Revit application frame the pane should dock to.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public DockPosition DockPosition { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DockPosition As DockPosition 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property DockPosition DockPosition { 	DockPosition get (); 	void set (DockPosition value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[DockablePaneState Class](0255200b-8af3-3254-ca6b-043f5cc291cf.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3d89cbdb-0653-7820-5b94-e1fd8b6bf144.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternallyTaggedGeometryValidation Class

---



|  |
| --- |
| [Members](6d3b3508-b9c4-3de7-fc4c-fcd4f2e1e2ca.htm)   [See Also](#seeAlsoToggle) |

Provides validation for geometry to be stored in an ExternallyTaggedGeometry.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static class ExternallyTaggedGeometryValidation ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class ExternallyTaggedGeometryValidation ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExternallyTaggedGeometryValidation abstract sealed ``` |

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB ExternallyTaggedGeometryValidation

# See Also

[ExternallyTaggedGeometryValidation Members](6d3b3508-b9c4-3de7-fc4c-fcd4f2e1e2ca.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d8b7f68-cfe0-c1ac-c8b3-532a80155e0d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLayoutAsNumberWithSpacing Method

---



|  |
| --- |
| [RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)   [See Also](#seeAlsoToggle) |

Sets the Layout Rule property of rebar set to NumberWithSpacing

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void SetLayoutAsNumberWithSpacing( 	int numberOfBarPositions, 	double spacing, 	bool barsOnNormalSide, 	bool includeFirstBar, 	bool includeLastBar ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLayoutAsNumberWithSpacing ( _ 	numberOfBarPositions As Integer, _ 	spacing As Double, _ 	barsOnNormalSide As Boolean, _ 	includeFirstBar As Boolean, _ 	includeLastBar As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLayoutAsNumberWithSpacing( 	int numberOfBarPositions,  	double spacing,  	bool barsOnNormalSide,  	bool includeFirstBar,  	bool includeLastBar ) ``` |

#### Parameters

numberOfBarPositions
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The number of bar positions in rebar set

spacing
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The maximum spacing between rebar in rebar set

barsOnNormalSide
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     Identifies if the bars of the rebar set are on the same side of the rebar plane indicated by the normal

includeFirstBar
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     Identifies if the first bar in rebar set is shown

includeLastBar
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     Identifies if the last bar in rebar set is shown

# Remarks

When changing the layout rule to NumberWithSpacing, you must also simultaneously set NumberOfBarPositions, Spacing, BarsOnNormalSide, IncludeFirstBar, and IncludeLastBar properties.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the number of bar positions numberOfBarPositions is less than 1 or more than 1002. -or- The spacing isn't bigger than 0.0. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | This RebarShapeDrivenAccessor is an instance of a spiral or multiplanar shape. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RebarShapeDrivenAccessor doesn't contain a valid rebar reference. |

# See Also

[RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3d8ca3f6-2e0d-c45a-c58d-40170ea037d9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Stage Property

---



|  |
| --- |
| [ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)   [See Also](#seeAlsoToggle) |

The current stage of the progress bar

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ProgressStage Stage { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Stage As ProgressStage 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ProgressStage Stage { 	ProgressStage get (); } ``` |

# See Also

[ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__3d8eb5c1-8154-1211-4308-f33a3dd92ec2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetUnits Method

---



|  |
| --- |
| [AnalysisResultSchema Class](90969170-ac45-68e6-2527-f6fba5b3f7ae.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Sets names and multipliers of all units for result visualization

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetUnits( 	IList<string> names, 	IList<double> multipliers ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetUnits ( _ 	names As IList(Of String), _ 	multipliers As IList(Of Double) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetUnits( 	IList<String^>^ names,  	IList<double>^ multipliers ) ``` |

#### Parameters

names
:   Type:  System.Collections.Generic IList   String    
     Unit names for all units (e.g., "Lb" and "Kg")

multipliers
:   Type:  System.Collections.Generic IList   Double    
     Numerical coefficients mapped to unit names. They adjust measurement values shown in the legend and display (e.g., 1.0 and 0.451 - if actual measurements are in Lb)

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
IList<string> unitNames = new List<string>();
unitNames.Add("Feet");
unitNames.Add("Inches");
IList<double> multipliers = new List<double>();
multipliers.Add(1);
multipliers.Add(12);

AnalysisResultSchema resultSchema = new AnalysisResultSchema("Schema Name", "Description");

resultSchema.SetUnits(unitNames, multipliers);
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Dim unitNames As IList(Of String) = New List(Of String)()
unitNames.Add("Feet")
unitNames.Add("Inches")
Dim multipliers As IList(Of Double) = New List(Of Double)()
multipliers.Add(1)
multipliers.Add(12)

Dim resultSchema As New AnalysisResultSchema("Schema Name", "Description")

resultSchema.SetUnits(unitNames, multipliers)
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | names is zero-length or contains duplicate or empty names -or- multipliers contains non-positive numbers, or its length is not equal to the length of names |

# See Also

[AnalysisResultSchema Class](90969170-ac45-68e6-2527-f6fba5b3f7ae.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3d8f0356-fd71-6e45-35bd-7e573affdef8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [TessellatedFace Class](6b007c37-6c87-50c5-8cf3-c3c68aa130ae.htm)   [See Also](#seeAlsoToggle) |

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

[TessellatedFace Class](6b007c37-6c87-50c5-8cf3-c3c68aa130ae.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3d9c4f6b-8e64-33c1-c0e4-2a1157b823d9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ServerPath Constructor

---



|  |
| --- |
| [ServerPath Class](c304ffcf-b3ae-46be-e361-a80bec83b5c0.htm)   [See Also](#seeAlsoToggle) |

Constructs a ServerPath

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ServerPath( 	string centralServerLocation, 	string path ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	centralServerLocation As String, _ 	path As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ServerPath( 	String^ centralServerLocation,  	String^ path ) ``` |

#### Parameters

centralServerLocation
:   Type:  System String    
     The name of the central Revit server

path
:   Type:  System String    
     The path of the model. This path must be relative.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ServerPath Class](c304ffcf-b3ae-46be-e361-a80bec83b5c0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3da00567-298b-5130-df47-f33ea6a3f0c2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SortPoints Method

---



|  |
| --- |
| [CurveByPoints Class](2df7ab39-1ac0-5803-79fa-b23a959bf8f2.htm)   [See Also](#seeAlsoToggle) |

Order a set of ReferencePoints in the same way Revit does when creating a curve from points.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static bool SortPoints( 	ReferencePointArray arr ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function SortPoints ( _ 	arr As ReferencePointArray _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool SortPoints( 	ReferencePointArray^ arr ) ``` |

#### Parameters

arr
:   Type:  [Autodesk.Revit.DB ReferencePointArray](4780adea-9e68-b0b4-09c7-68f7752dd650.htm)    
     An array of ReferencePoints. The array is reordered if sortPoints returns true, and is unchanged if sortPoints returns false.

#### Return Value

False if the least-squares method is unable to find a solution; true otherwise.

# Remarks

Finds a best-fit line to the points by the least squares method, and orders the points by their projection onto the line.

# See Also

[CurveByPoints Class](2df7ab39-1ac0-5803-79fa-b23a959bf8f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3da20906-2027-58df-e1fd-a62b1d45d9e3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MismatchNmbAssignedDistSysToCircuit Property

---



|  |
| --- |
| [BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)   [See Also](#seeAlsoToggle) |

Cannot assign or add [Element] to Circuit. There is no assigned distribution system for [Element].

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId MismatchNmbAssignedDistSysToCircuit { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MismatchNmbAssignedDistSysToCircuit As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ MismatchNmbAssignedDistSysToCircuit { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3da4c84c-9a77-2996-99cf-040e057abbcd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddSegment Method

---



|  |
| --- |
| [SlabEdge Class](8c1ba09e-d1d0-b1e4-bc2f-26ec4b6c5afa.htm)   [See Also](#seeAlsoToggle) |

Add segments to the slab edge.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public override void AddSegment( 	Reference targetRef ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Sub AddSegment ( _ 	targetRef As Reference _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void AddSegment( 	Reference^ targetRef ) override ``` |

#### Parameters

targetRef
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     Segment's reference on which want to be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | This exception will be thrown in following cases: 1. Input targetRef is    a null reference (  Nothing  in Visual Basic)  . 2. Input targetRef is not    a null reference (  Nothing  in Visual Basic)  but contains nothing. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This exception will be thrown in following cases: 1. Input targetRef has already been added into the slab edge. 2. Internal code fails to create the segment object. 3. Regeneration fails. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | This exception will be thrown if the reference is suitable for creating a slab edge as required. The reference allowed is : 1. Model Line 2. Floor's horizontal edges 3. Other slab edge's horizontal edges |

# See Also

[SlabEdge Class](8c1ba09e-d1d0-b1e4-bc2f-26ec4b6c5afa.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3da75f23-fcf5-28bb-fcc1-7bdb6886342a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoofUptoLevelOffsetParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Cutoff Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RoofUptoLevelOffsetParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoofUptoLevelOffsetParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RoofUptoLevelOffsetParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3da7e561-66d4-97d5-ed12-7ff77b478421.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetStatus Method

---



|  |
| --- |
| [SubTransaction Class](801e5f17-cab0-044d-835c-a39592374f89.htm)   [See Also](#seeAlsoToggle) |

Returns the current status of the sub-transaction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public TransactionStatus GetStatus() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetStatus As TransactionStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: TransactionStatus GetStatus() ``` |

#### Return Value

The current status of the sub-transaction.

# See Also

[SubTransaction Class](801e5f17-cab0-044d-835c-a39592374f89.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3da9a916-d6ca-2f56-b818-4cc60d7252a7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsWallCrossSectionValid Method

---



|  |
| --- |
| [Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)   [See Also](#seeAlsoToggle) |

Checks whether the desired cross section is valid for the current wall.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public bool IsWallCrossSectionValid( 	WallCrossSection wallCrossSection ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsWallCrossSectionValid ( _ 	wallCrossSection As WallCrossSection _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsWallCrossSectionValid( 	WallCrossSection wallCrossSection ) ``` |

#### Parameters

wallCrossSection
:   Type:  [Autodesk.Revit.DB WallCrossSection](c0017a61-ed27-8124-f3f7-17d73c446169.htm)    
     The desired cross section.

#### Return Value

True if the wall can be set to the desired cross section.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3db1fadb-0349-f0cd-c3cc-c9aa90454880.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Print Method (ViewSet, View)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Prints a set of views with a specified view template and default print settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void Print( 	ViewSet views, 	View viewTemplate ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Print ( _ 	views As ViewSet, _ 	viewTemplate As View _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Print( 	ViewSet^ views,  	View^ viewTemplate ) ``` |

#### Parameters

views
:   Type:  [Autodesk.Revit.DB ViewSet](47b47de2-4234-01e0-af21-64334e2a4a4b.htm)    
     The set of views which need to be printed.

viewTemplate
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view template which apply to the set of views.

# Remarks

If one view in the set can not be printed successfully then an exception will be thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when printing is not allowed in the current application mode. Or when at least one view from the view set is not a printable view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the view set to be printed is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the view set contains a    a null reference (  Nothing  in Visual Basic)  element. |
| [Autodesk.Revit.Exceptions ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.htm) | Thrown when at least one view from the view set could not be printed. |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | Thrown when print is cancelled by event handler. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Print Overload](e491ce6c-4350-0335-5388-28875da09c7e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3db42276-cab0-81d1-7396-2a1fbe0a8261.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### KilogramsPerMeterSecond Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Kilograms per meter second.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId KilogramsPerMeterSecond { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property KilogramsPerMeterSecond As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ KilogramsPerMeterSecond { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3db6609d-62ba-ceda-4862-5d68ab4c3440.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PartMakerSplitterProfileEdgeMatch Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Edge Match"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PartMakerSplitterProfileEdgeMatch { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PartMakerSplitterProfileEdgeMatch As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PartMakerSplitterProfileEdgeMatch { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3db72aff-7a71-25cd-7db5-27432cd158e4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralCopingDistance Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Coping Distance"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralCopingDistance { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralCopingDistance As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralCopingDistance { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3dbd4eab-664f-0048-13a9-959c27fce729.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSubelement Method (Reference)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Gets the subelement referenced by the input reference.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public Subelement GetSubelement( 	Reference reference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSubelement ( _ 	reference As Reference _ ) As Subelement ``` |

 

| Visual C++ |
| --- |
| ``` public: Subelement^ GetSubelement( 	Reference^ reference ) ``` |

#### Parameters

reference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The reference that identifies element or subelement.

#### Return Value

The subelement referenced by the input argument.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | reference does not identify a valid element or subelement. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[GetSubelement Overload](fdd67b30-5d02-e5c4-ebf1-ddcb5382ffc1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3dbe57e5-fdea-5bf9-c715-52653f56073f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Location Class

---



|  |
| --- |
| [Members](b85eed72-6a01-6456-5da3-f4d55af11aec.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Provides location functionality for all elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class Location : APIObject ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Location _ 	Inherits APIObject ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Location : public APIObject ``` |

# Remarks

The location object provides the ability to translate and rotate elements. More detailed location information and control can be found by using the derivatives of this object, such as LocationPoint or LocationCurve.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
void ShowLocationUsage(Autodesk.Revit.ApplicationServices.Application application, Wall wall)
{
    // Get the location instance.
    Autodesk.Revit.DB.Location position = wall.Location;

    // Check whether the wall is pinned.
    if (wall.Pinned)
    {
        throw new Exception("The wall has been pinned.");
    }

    // Move the wall location, it provides same function as Move method of Document class.
    XYZ direction = new XYZ(10, 0, 0);
    bool result = position.Move(direction);
    if (!result)
    {
        throw new Exception("Move wall location failed.");
    }

    // Rotate the wall location, it provides same function as Rotate method of Document class.
    XYZ axisStart = new XYZ(0, 0, 0);
    XYZ axisEnd = new XYZ(0, 0, 1);
    Line axis = Line.CreateUnbound(axisStart, axisEnd);
    result = position.Rotate(axis, 30);
    if (!result)
    {
        throw new Exception("Rotate wall location failed.");
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub ShowLocationUsage(application As Autodesk.Revit.ApplicationServices.Application, wall As Wall)
    ' Get the location instance.
    Dim position As Autodesk.Revit.DB.Location = wall.Location

    ' Check whether the wall is pinned.
    If wall.Pinned Then
        Throw New Exception("The wall has been pinned.")
    End If

    ' Move the wall location, it provides same function as Move method of Document class.
    Dim direction As New XYZ(10, 0, 0)
    Dim result As Boolean = position.Move(direction)
    If Not result Then
        Throw New Exception("Move wall location failed.")
    End If

    ' Rotate the wall location, it provides same function as Rotate method of Document class.
    Dim axisStart As New XYZ(0, 0, 0)
    Dim axisEnd As New XYZ(0, 0, 1)
    Dim axis As Line = Line.CreateUnbound(axisStart, axisEnd)
    result = position.Rotate(axis, 30)
    If Not result Then
        Throw New Exception("Rotate wall location failed.")
    End If
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB Location    
  [Autodesk.Revit.DB LocationCurve](9dd6eb99-f105-a05f-dc1b-dfde17b8768c.htm)    
  [Autodesk.Revit.DB LocationPoint](0a36b1c4-f112-38f6-7b14-d572ea11584b.htm)

# See Also

[Location Members](b85eed72-6a01-6456-5da3-f4d55af11aec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3dbebcb8-792b-a3dd-fe63-faaa05704f3c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StorageType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all of the internal parameter data storage types that Autodesk Revit supports.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum StorageType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration StorageType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class StorageType ``` |

# Members

| Member name | Description |
| --- | --- |
| None | None represents an invalid storage type. This value should not be used. |
| Integer | The internal data is stored in the form of a signed 32 bit integer. |
| Double | The data will be stored internally in the form of an 8 byte floating point number. |
| String | The internal data will be stored in the form of a string of characters. |
| ElementId | The data type represents an element and is stored as the id of the element. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3dc12e49-711d-cdba-0d16-6b43302a03fd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CutLineType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The available line types for a stairs cut line.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum CutLineType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration CutLineType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class CutLineType ``` |

# Members

| Member name | Description |
| --- | --- |
| SingleLine | Cutline type is single-line. |
| DoubleLine | Cutline type is double-line. |

# See Also

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__3dc6542a-ed72-81a1-7cf8-8af17a6c2949.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCFileReadOptions Class

---



|  |
| --- |
| [Members](37f9f91f-eea1-70f3-83cd-a8c639891be4.htm)   [See Also](#seeAlsoToggle) |

This class contains options to read an IFC file.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class IFCFileReadOptions : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class IFCFileReadOptions _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class IFCFileReadOptions : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.IFC IFCFileReadOptions

# See Also

[IFCFileReadOptions Members](37f9f91f-eea1-70f3-83cd-a8c639891be4.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__3dc6d73e-8078-b65a-6e6b-d77d259110dc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Hour Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol h, indicating unit Hours.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Hour { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Hour As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Hour { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3dc90301-35e6-970d-e7bf-f9230e8058a2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsCurvetypeDefaultTeeupParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Tee Up"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsCurvetypeDefaultTeeupParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsCurvetypeDefaultTeeupParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsCurvetypeDefaultTeeupParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3dcd2580-48d5-3646-c2b0-74297ca0556f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MSup6 Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol mâ¶, indicating unit Meters to the sixth power.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MSup6 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MSup6 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MSup6 { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3dd2435e-3b12-8d38-279a-e6141de1b390.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FaceArrayIterator Class

---



|  |
| --- |
| [Members](8ac65658-7e01-dba2-5991-cbad0b67e42c.htm)   [See Also](#seeAlsoToggle) |

An iterator to a face array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public abstract class FaceArrayIterator : APIObject,  	IEnumerator ``` |

 

| Visual Basic |
| --- |
| ``` Public MustInherit Class FaceArrayIterator _ 	Inherits APIObject _ 	Implements IEnumerator ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FaceArrayIterator abstract : public APIObject,  	IEnumerator ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB FaceArrayIterator

# See Also

[FaceArrayIterator Members](8ac65658-7e01-dba2-5991-cbad0b67e42c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3de46f00-fbf9-0c6b-b7fa-5d33052d0091.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumericRevisionSettings Class

---



|  |
| --- |
| [Members](3e7a7a13-5c18-10bc-5bdb-697bcfa916cf.htm)   [See Also](#seeAlsoToggle) |

Contains settings that apply to Revisions with the Numeric RevisionNumberType.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public class NumericRevisionSettings : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class NumericRevisionSettings _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class NumericRevisionSettings : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB NumericRevisionSettings

# See Also

[NumericRevisionSettings Members](3e7a7a13-5c18-10bc-5bdb-697bcfa916cf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3de51365-3c24-586c-0d0e-2431448ad4c8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AllowOverrideCellStyle Method

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Identifies if the style can be overridden in the given cell.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool AllowOverrideCellStyle( 	int nRow, 	int nCol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AllowOverrideCellStyle ( _ 	nRow As Integer, _ 	nCol As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool AllowOverrideCellStyle( 	int nRow,  	int nCol ) ``` |

#### Parameters

nRow
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

nCol
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

#### Return Value

True if allow to override cell style.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given row number nRow is invalid. -or- The given column number nCol is invalid. |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3de65ee0-50f1-c601-62f9-c77479b08418.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RollBack Method

---



|  |
| --- |
| [SubTransaction Class](801e5f17-cab0-044d-835c-a39592374f89.htm)   [See Also](#seeAlsoToggle) |

Discards all changes made to the model during the sub-transaction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public TransactionStatus RollBack() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function RollBack As TransactionStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: TransactionStatus RollBack() ``` |

#### Return Value

If finished successfully, this method returns TransactionStatus.RolledBack.

# Remarks

The parent transaction (or a parent sub-transaction, if any) can still be committed, but the changes rolled back by this method will not be part of the committed transaction.

RollBack can be called only when all inner sub-transaction, if any, are finished, i.e. they were either committed or rolled back. If there is still a sub-transaction open, an attempt to roll this outer sub-transaction back will cause an exception.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | A sub-transaction can only be active inside an open Transaction. -or- The sub-transaction's current status is not TransactionStatus.Started, therefore it may not be committed or rolled back. |

# See Also

[SubTransaction Class](801e5f17-cab0-044d-835c-a39592374f89.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3decba62-28ce-5f07-0d78-447de6641932.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetSurfaceBackgroundPatternId Method

---



|  |
| --- |
| [OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)   [See Also](#seeAlsoToggle) |

Sets the ElementId of the surface background pattern override. The fill pattern must be a drafting pattern. A value of InvalidElementId means no override is set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public OverrideGraphicSettings SetSurfaceBackgroundPatternId( 	ElementId fillPatternId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetSurfaceBackgroundPatternId ( _ 	fillPatternId As ElementId _ ) As OverrideGraphicSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: OverrideGraphicSettings^ SetSurfaceBackgroundPatternId( 	ElementId^ fillPatternId ) ``` |

#### Parameters

fillPatternId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Value of the surface background fill pattern override.

#### Return Value

Reference to the changed object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3def4273-99ce-5158-c8d0-293eb7c924b5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NoSketchPlane Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

Can't paste because no Work Plane is defined in the View.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NoSketchPlane { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NoSketchPlane As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NoSketchPlane { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3def553a-e76d-cd75-2a27-087f2b0394ba.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MassDataPercentageSkylights Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Target Percentage Skylights"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MassDataPercentageSkylights { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MassDataPercentageSkylights As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MassDataPercentageSkylights { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3df0b78d-5bd4-c944-a350-e4f0423bdf15.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [CopyPasteOptions Class](d8f58fd5-2106-7a88-6218-106a30415791.htm)   [See Also](#seeAlsoToggle) |

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

[CopyPasteOptions Class](d8f58fd5-2106-7a88-6218-106a30415791.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3df10700-a305-dba7-fc4a-5afb5387256c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportDGNSettings Class

---



|  |
| --- |
| [Members](4569d50c-9ed6-8650-b2f6-1128702aa3a0.htm)   [See Also](#seeAlsoToggle) |

This element contains DGN export settings which are saved in a Revit document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class ExportDGNSettings : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExportDGNSettings _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExportDGNSettings : public Element ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB ExportDGNSettings

# See Also

[ExportDGNSettings Members](4569d50c-9ed6-8650-b2f6-1128702aa3a0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3df59ea1-731b-ebb5-a602-aa0f56899344.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SketchGalleryOptions Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Enumerates all the sketch options.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public enum SketchGalleryOptions ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration SketchGalleryOptions ``` |

 

| Visual C++ |
| --- |
| ``` public enum class SketchGalleryOptions ``` |

# Members

| Member name | Description |
| --- | --- |
| SGO\_Default | The default option which means the real option is decided by Revit internally. |
| SGO\_Line | Sketch a line. |
| SGO\_Rect | Sketch a rectangle. |
| SGO\_InscribedPolygon | Sketch an inscribed polygon. |
| SGO\_CircumscribedPolygon | Sketch a circumscribed polygon. |
| SGO\_Circle | Sketch a circle. |
| SGO\_Arc3Point | Sketch a Start-End-Radius arc. |
| SGO\_ArcCenterEnds | Sketch a Center-Ends arc. |
| SGO\_ArcTanEnd | Sketch a Tangent-End arc. |
| SGO\_ArcFillet | Sketch a fillet arc. |
| SGO\_Spline | Sketch a spline. |
| SGO\_SplineByPoints | Sketch a spline by points. |
| SGO\_FullEllipse | Sketch a full ellipse. |
| SGO\_PartialEllipse | Sketch a partial ellipse. |
| SGO\_PickLines | Pick lines. |
| SGO\_PickFaces | Pick faces. |
| SGO\_PickWalls | Pick walls. |
| SGO\_PickSupports | Pick supports. |
| SGO\_PickRoofs | Pick roofs. |
| SGO\_Point | Pick a point. |
| SGO\_PickPoints | Pick points. |
| SGO\_PointElement | Pick point element. |
| SGO\_RunLine | Sketch a line for a run of stairs. |
| SGO\_RunArcFullStep | Sketch a Full-Step spiral for a run of stairs. |
| SGO\_RunArcCenterEnds | Sketch a Center-Ends spiral for a run of stairs. |
| SGO\_LandingSquare | Sketch a landing square. |
| SGO\_WinderLShape | Sketch a L-Shape winder. |
| SGO\_WinderPattern | Pick winder pattern. |
| SGO\_SupportPickLine | Pick a line to create a support. |
| SGO\_WinderUShape | Sketch a U-Shape winder. |
| SGO\_LandingWithTwoRuns | Pick two runs to create a landing. |
| SGO\_SketchRun | Sketch a run. |
| SGO\_SketchLanding | Sketch a landing. |

# See Also

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3dfb45e3-59e1-6543-1869-796c94b1965e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [HVACLoadBuildingType Class](db7c8da2-260f-94b7-990e-f32ad234ec87.htm)   [See Also](#seeAlsoToggle) |

Creates a building type element.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static HVACLoadBuildingType Create( 	Document document, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	name As String _ ) As HVACLoadBuildingType ``` |

 

| Visual C++ |
| --- |
| ``` public: static HVACLoadBuildingType^ Create( 	Document^ document,  	String^ name ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

name
:   Type:  System String    
     The building type name.

#### Return Value

The new building type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name is an empty string or contains only whitespace. -or- name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". -or- The given value for name is already in use as a building type name. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[HVACLoadBuildingType Class](db7c8da2-260f-94b7-990e-f32ad234ec87.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3dfbad53-1e61-ea1f-23d4-46bb26e631f5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TotalViews Property

---



|  |
| --- |
| [ViewPrintingEventArgs Class](8e7d048f-a50b-7903-6001-6716f7eabdb5.htm)   [See Also](#seeAlsoToggle) |

The number of all views being printed.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public int TotalViews { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property TotalViews As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int TotalViews { 	int get (); } ``` |

# See Also

[ViewPrintingEventArgs Class](8e7d048f-a50b-7903-6001-6716f7eabdb5.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__3dfdd0ac-7f08-b6bf-187e-bcb93ab9e54b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpaceHeatingSetPoint Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Heating Set Point"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpaceHeatingSetPoint { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpaceHeatingSetPoint As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpaceHeatingSetPoint { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3dfea5d9-8b6c-cb57-c54f-cdc3ed9e92ab.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RailProfileOpen Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Open Profile Loop can't be used as a Rail Profile

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RailProfileOpen { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RailProfileOpen As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RailProfileOpen { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e01937d-a001-8fd4-9cc8-270ad4b4ba10.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumberOfSegments Property

---



|  |
| --- |
| [Dimension Class](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm)   [See Also](#seeAlsoToggle) |

The number of segments for the dimension.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int NumberOfSegments { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property NumberOfSegments As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int NumberOfSegments { 	int get (); } ``` |

# See Also

[Dimension Class](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e05439e-90a4-0f1e-a518-45a763afe2be.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MSup2KPerW Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol (mÂ²Â·K)/W, indicating unit Square meter kelvins per watt.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MSup2KPerW { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MSup2KPerW As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MSup2KPerW { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e05f5e6-72a2-f633-3740-93feecee8156.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AsElementId Method

---



|  |
| --- |
| [Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)   [See Also](#seeAlsoToggle) |

Provides access to the Autodesk::Revit::DB::ElementId^ stored within the parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ElementId AsElementId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AsElementId As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ AsElementId() ``` |

#### Return Value

The Autodesk::Revit::DB::ElementId^ contained in the parameter.

# Remarks

The AsAutodesk::Revit::DB::ElementId^ method should only be used if the StorageType property returns that the internal contents of the parameter is an ElementId.

# See Also

[Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e08054f-6a00-ac9b-ccd0-37b426d86678.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhyMaterialParamExpCoeff1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Thermal expansion coefficient X"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PhyMaterialParamExpCoeff1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PhyMaterialParamExpCoeff1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PhyMaterialParamExpCoeff1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e08fa98-7193-8337-c34e-41d299a154e5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Smoothness Property

---



|  |
| --- |
| [MaterialNode Class](c70338a6-7f40-e89e-607b-47162df3a5ef.htm)   [See Also](#seeAlsoToggle) |

The level of smoothness of the material.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public int Smoothness { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Smoothness As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int Smoothness { 	int get (); } ``` |

# See Also

[MaterialNode Class](c70338a6-7f40-e89e-607b-47162df3a5ef.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e0974c7-144d-b83c-0a6f-504622e2adf8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhyMaterialParamYoungModn2 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Young's Modulus 2"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PhyMaterialParamYoungModn2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PhyMaterialParamYoungModn2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PhyMaterialParamYoungModn2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e0a6725-ee40-c4d5-839f-b7720c1fe2af.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DatumPlane Class

---



|  |
| --- |
| [Members](1f49a2d1-5fe9-386a-3ad5-a92c268adfe6.htm)   [See Also](#seeAlsoToggle) |

A base class representing a datum surface (level, grid or reference plane) in Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public class DatumPlane : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DatumPlane _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DatumPlane : public Element ``` |

# Remarks

A DatumPlane represents a 3d surface with finite extents. It can be either a rectangle with arbitrary orientation, or a cylinder whose axis is parallel to the project z-axis. If a datum is visible in a plan or section view, it will be displayed as one or more curves. These curves are determined by the intersection of the datum surface with the cut plane of the view. By default, the extents of these curves reflect the 3d extents of the datum surface. If the surface is a plane, then the extents represent the projection of the surface onto the cut plane. This matters, for example, when viewing a datum plane, really a 3d rectangle, along one of its diagonals. The extents of the curve do not vary with the location of the view, because we use the projection of the rectangle and not the actual intersection. If the surface is a cylinder, then the extents reflect the actual intersection of the surface with the cut plane. In addition, the curves that represent a DatumPlane can be modified on a view specific basis. In this case, the ends of the curve no longer reflect the 3d extents of the datum.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB DatumPlane    
  [Autodesk.Revit.DB Grid](47888507-2d69-664a-ead4-e481c7c5f42d.htm)    
  [Autodesk.Revit.DB Level](577e5d4e-a558-118c-9dea-3b810b061775.htm)    
  [Autodesk.Revit.DB ReferencePlane](e7003ec7-1dbe-50a2-fb3d-a83a5a3b5b9f.htm)

# See Also

[DatumPlane Members](1f49a2d1-5fe9-386a-3ad5-a92c268adfe6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e0b1280-99bf-8350-3223-b22c5089fa33.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Latitude Property

---



|  |
| --- |
| [City Class](2ceeb3cd-05a1-02c6-3d95-ef689221acdc.htm)   [See Also](#seeAlsoToggle) |

Latitude of the city

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double Latitude { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Latitude As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Latitude { 	double get (); } ``` |

# Remarks

A read only property that contains the latitude of the city. The value returned is in radians, ranging from -PI to +PI.

# See Also

[City Class](2ceeb3cd-05a1-02c6-3d95-ef689221acdc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e0d0aea-7bfc-ac33-405e-2e26cbdc6e8f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Flipped Property

---



|  |
| --- |
| [Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)   [See Also](#seeAlsoToggle) |

Indicates if the railing is flipped.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool Flipped { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Flipped As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool Flipped { 	bool get (); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | The railing has incorrect internal data. |

# See Also

[Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__3e10329e-4114-73f7-65a6-17bf40056be9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Contains Method

---



|  |
| --- |
| [Outline Class](1ffe9215-0dd5-358f-495d-e983f9e7d295.htm)   [See Also](#seeAlsoToggle) |

Determine if this Outline contains the specified point to within a tolerance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool Contains( 	XYZ point, 	double tolerance ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Contains ( _ 	point As XYZ, _ 	tolerance As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Contains( 	XYZ^ point,  	double tolerance ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The point to test for containment.

tolerance
:   Type:  System Double    
     The tolerance to use when determining whether the point is contained. Defaults to zero.

#### Return Value

True if this outline contains the given point, or false otherwise.

# Remarks

If the tolerance is positive, the point may lie up to the tolerance amount outside the outline in each coordinate. If the tolerance is negative, the point must lie at least the tolerance amount inside the outline in each coordinate.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Outline Class](1ffe9215-0dd5-358f-495d-e983f9e7d295.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e103cf0-3d07-5cab-ba6e-0d122f14ce35.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCopyTag Property

---



|  |
| --- |
| [BuiltInFailures TagFailures Class](466bf4b7-571e-a718-4900-965e2569d60b.htm)   [See Also](#seeAlsoToggle) |

A tag cannot be arrayed without copying the associated element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCopyTag { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCopyTag As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCopyTag { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures TagFailures Class](466bf4b7-571e-a718-4900-965e2569d60b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e10c7e8-3abd-b593-cb27-2603323eac7b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoofConstraintOffsetParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Level Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RoofConstraintOffsetParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoofConstraintOffsetParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RoofConstraintOffsetParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e13b33f-4468-9c86-94c3-253faf272ae8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotKeepWallJoinToRoof Property

---



|  |
| --- |
| [BuiltInFailures JoinElementsFailures Class](2d7e4353-c24a-38d5-f3aa-3cbc2cb92698.htm)   [See Also](#seeAlsoToggle) |

Can't keep wall and [target] joined

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotKeepWallJoinToRoof { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotKeepWallJoinToRoof As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotKeepWallJoinToRoof { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures JoinElementsFailures Class](2d7e4353-c24a-38d5-f3aa-3cbc2cb92698.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e1416ef-179c-82a0-8124-7cc95f80b04a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UIView Property

---



|  |
| --- |
| [PreviewControl Class](50112279-5c9d-0351-bbd1-698e76be9e36.htm)   [See Also](#seeAlsoToggle) |

The UI view representing the preview view.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public UIView UIView { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property UIView As UIView 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property UIView^ UIView { 	UIView^ get (); } ``` |

# Remarks

Use this handle to manipulate the zoom and pan of the view.

# See Also

[PreviewControl Class](50112279-5c9d-0351-bbd1-698e76be9e36.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3e172b58-0b5c-d0ba-1b47-b8d6b1a4f367.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ZoneLevelOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Level Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ZoneLevelOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ZoneLevelOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ZoneLevelOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e1dced5-48a6-e9af-cc00-8eda38149b88.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InverseKilonewtons Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Inverse kilonewtons.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId InverseKilonewtons { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InverseKilonewtons As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ InverseKilonewtons { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e2129fb-770f-be50-b551-eef05f1b5d43.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OperatorType Property

---



|  |
| --- |
| [FilterOperatorAndTextString Class](90d2062e-8e6e-a69e-68de-bef31a7810c2.htm)   [See Also](#seeAlsoToggle) |

The filter operator.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public ScheduleFilterType OperatorType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property OperatorType As ScheduleFilterType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ScheduleFilterType OperatorType { 	ScheduleFilterType get (); } ``` |

# See Also

[FilterOperatorAndTextString Class](90d2062e-8e6e-a69e-68de-bef31a7810c2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e217ff7-7946-1036-78b3-ccab50f03c8b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForwardIterator Method

---



|  |
| --- |
| [GroupSet Class](cac73a6e-e521-7af1-281c-22c8e5245c03.htm)   [See Also](#seeAlsoToggle) |

Retrieve a forward moving iterator to the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual GroupSetIterator ForwardIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ForwardIterator As GroupSetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual GroupSetIterator^ ForwardIterator() ``` |

#### Return Value

Returns a forward moving iterator to the set.

# See Also

[GroupSet Class](cac73a6e-e521-7af1-281c-22c8e5245c03.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e21b30a-9af7-6171-5e0a-695c597f9e66.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CircularDependencySketchError Property

---



|  |
| --- |
| [BuiltInFailures RegenFailures Class](c7726de2-e4f0-8861-8115-0ef9de7935b1.htm)   [See Also](#seeAlsoToggle) |

There is a circular chain of references among the highlighted elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CircularDependencySketchError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CircularDependencySketchError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CircularDependencySketchError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RegenFailures Class](c7726de2-e4f0-8861-8115-0ef9de7935b1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e24586d-4a80-5331-8e79-74d1b6249ca6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetExtrusionBase Method

---



|  |
| --- |
| [ExtrusionAnalyzer Class](ba9e3283-6868-8834-e8bf-2ea9e7358930.htm)   [See Also](#seeAlsoToggle) |

Obtains the face that represents the base contour of the extrusion analysis.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public Face GetExtrusionBase() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetExtrusionBase As Face ``` |

 

| Visual C++ |
| --- |
| ``` public: Face^ GetExtrusionBase() ``` |

#### Return Value

The face that represents the base contour.

# See Also

[ExtrusionAnalyzer Class](ba9e3283-6868-8834-e8bf-2ea9e7358930.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e28283d-701e-4b00-5bab-0d1da2e8bb86.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewDisplayEdges Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

A collection of settings defining how visible edges are displayed

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public enum ViewDisplayEdges ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ViewDisplayEdges ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ViewDisplayEdges ``` |

# Members

| Member name | Description |
| --- | --- |
| None | The edges are invisible |
| Simple | The edges are visible and drawn according to style |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e28ffe1-bae9-6826-9042-285f9bfd98fe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LeaderRightAttachment Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Right Attachment"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LeaderRightAttachment { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LeaderRightAttachment As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LeaderRightAttachment { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e290a46-d42a-be59-f645-9dcc499fecc3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuildingPadNotConnected Property

---



|  |
| --- |
| [BuiltInFailures SiteFailures Class](7ab66d74-f1ab-17f6-9ecf-e51b3d5326bf.htm)   [See Also](#seeAlsoToggle) |

Can't create a single Pad with several connected regions.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId BuildingPadNotConnected { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BuildingPadNotConnected As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ BuildingPadNotConnected { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SiteFailures Class](7ab66d74-f1ab-17f6-9ecf-e51b3d5326bf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e2b159c-4d23-0c84-5b6a-df1a9053fb71.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsPipeSlopeOptionsDefParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Pipe Slope Options"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsPipeSlopeOptionsDefParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsPipeSlopeOptionsDefParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsPipeSlopeOptionsDefParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e2c025a-2e4d-1aac-c8d4-2bfbe0fc2e1f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MasonryCMUPattern Property

---



|  |
| --- |
| [MasonryCMU Class](1cd24382-d660-029d-ef09-9f553ebdb199.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Relief Pattern" from the "MasonryCMU" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string MasonryCMUPattern { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MasonryCMUPattern As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ MasonryCMUPattern { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyInteger" with accepted values in the enumerated type "MasonryCMUPatternType".

# See Also

[MasonryCMU Class](1cd24382-d660-029d-ef09-9f553ebdb199.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3e30d0b4-6c74-18bf-043f-2430ff9ac17b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLineStyleIds Method

---



|  |
| --- |
| [CurveElement Class](61673852-2d08-003d-e9fd-4be89d533774.htm)   [See Also](#seeAlsoToggle) |

Ids of all line style Elements that are applicable to this curve element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> GetLineStyleIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLineStyleIds As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ GetLineStyleIds() ``` |

#### Return Value

A collection of Ids of line style elements.

# Remarks

The elements are of the  [GraphicsStyle](da26fe81-ee66-1036-1f5b-dffe612182d9.htm)  class.

# See Also

[CurveElement Class](61673852-2d08-003d-e9fd-4be89d533774.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e334aaf-2b39-58bd-d2cc-94e9c89bac57.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LogicalAndFilter Class

---



|  |
| --- |
| [Members](1b21d9d2-f07a-d092-a5e5-ed151ae6fb1c.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A filter that contains a set of filters. The filter passes when all filters in the set pass.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class LogicalAndFilter : ElementLogicalFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class LogicalAndFilter _ 	Inherits ElementLogicalFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class LogicalAndFilter : public ElementLogicalFilter ``` |

# Remarks

The component filters may be reordered by Revit to cause the quickest acting filters to be evaluated first.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Find all door instances in the project by finding all elements that both belong to the door 
// category and are family instances.
ElementClassFilter familyInstanceFilter = new ElementClassFilter(typeof(FamilyInstance));

// Create a category filter for Doors
ElementCategoryFilter doorsCategoryfilter = new ElementCategoryFilter(BuiltInCategory.OST_Doors);

// Create a logic And filter for all Door FamilyInstances
LogicalAndFilter doorInstancesFilter = new LogicalAndFilter(familyInstanceFilter, doorsCategoryfilter);

// Apply the filter to the elements in the active document
FilteredElementCollector collector = new FilteredElementCollector(document);
IList<Element> doors = collector.WherePasses(doorInstancesFilter).ToElements();
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Find all door instances in the project by finding all elements that both belong to the door 
' category and are family instances.
Dim familyInstanceFilter As New ElementClassFilter(GetType(FamilyInstance))

' Create a category filter for Doors
Dim doorsCategoryfilter As New ElementCategoryFilter(BuiltInCategory.OST_Doors)

' Create a logic And filter for all Door FamilyInstances
Dim doorInstancesFilter As New LogicalAndFilter(familyInstanceFilter, doorsCategoryfilter)

' Apply the filter to the elements in the active document
Dim collector As New FilteredElementCollector(document)
Dim doors As IList(Of Element) = collector.WherePasses(doorInstancesFilter).ToElements()
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementLogicalFilter](3b8d6b55-0cab-1810-1188-840800e5eaa2.htm)    
  Autodesk.Revit.DB LogicalAndFilter

# See Also

[LogicalAndFilter Members](1b21d9d2-f07a-d092-a5e5-ed151ae6fb1c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e33cb9d-6535-cb73-12ab-d8949640d94d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarSystemLayerSummaryWithSpacing Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Layer Summary"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarSystemLayerSummaryWithSpacing { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarSystemLayerSummaryWithSpacing As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarSystemLayerSummaryWithSpacing { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e38785e-f987-f570-6618-96e1cc96438b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TrapMullWidth Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Center Width"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TrapMullWidth { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TrapMullWidth As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TrapMullWidth { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e38b7b1-1ee8-c7f0-6cdd-bacf67bf61f4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CentralModelAccessDeniedException Class

---



|  |
| --- |
| [Members](38563468-4bcb-0f04-5b26-134c4bc515b1.htm)   [See Also](#seeAlsoToggle) |

The exceptions thrown when a central model can be reached but access is denied due to a lack of access privileges.

**Namespace:**   [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` [SerializableAttribute] public class CentralModelAccessDeniedException : CentralModelException ``` |

 

| Visual Basic |
| --- |
| ``` <SerializableAttribute> _ Public Class CentralModelAccessDeniedException _ 	Inherits CentralModelException ``` |

 

| Visual C++ |
| --- |
| ``` [SerializableAttribute] public ref class CentralModelAccessDeniedException : public CentralModelException ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)    
  [Autodesk.Revit.Exceptions ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.htm)    
  [Autodesk.Revit.Exceptions CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.htm)    
  Autodesk.Revit.Exceptions CentralModelAccessDeniedException

# See Also

[CentralModelAccessDeniedException Members](38563468-4bcb-0f04-5b26-134c4bc515b1.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__3e3e1e55-74bb-5815-2227-9ecccbf36647.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurtaingridBeltn2 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Measurement Line"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CurtaingridBeltn2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CurtaingridBeltn2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CurtaingridBeltn2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e3fe969-2758-ac8d-eaf5-fe2472553b31.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LinePattern Constructor

---



|  |
| --- |
| [LinePattern Class](a2de5c67-d9be-760b-638a-579500216874.htm)   [See Also](#seeAlsoToggle) |

Creates a simple line pattern.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public LinePattern() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: LinePattern() ``` |

# See Also

[LinePattern Class](a2de5c67-d9be-760b-638a-579500216874.htm)

[LinePattern Overload](f5f19923-7319-81bb-caba-c6993445e025.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e434b28-aaa2-1132-9b04-d71eeddbe2da.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsCtcTopElevation Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Upper End Top Elevation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsCtcTopElevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsCtcTopElevation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsCtcTopElevation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e47440a-9d7f-5ca8-4773-3851d8efa999.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceExists Property

---



|  |
| --- |
| [BuiltInFailures SiteImportFailures Class](8f9298be-9e12-d84b-8459-c862355e698d.htm)   [See Also](#seeAlsoToggle) |

You are importing data into a surface that already contains points. You may want to go back, create a new surface, and import the data into that instead. You can continue, and Revit will sew the meshes together, but the boundary may be larger than you want.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SurfaceExists { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SurfaceExists As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SurfaceExists { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SiteImportFailures Class](8f9298be-9e12-d84b-8459-c862355e698d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e483f05-93ad-0b13-0dc0-d50e6ec1b6a2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDone Method

---



|  |
| --- |
| [ExportLinetypeTableIterator Class](901e037c-f870-f85f-8002-3223ff6c2061.htm)   [See Also](#seeAlsoToggle) |

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

[ExportLinetypeTableIterator Class](901e037c-f870-f85f-8002-3223ff6c2061.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e497cae-a95c-ebb7-a4e5-238b471bafc6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reset Method

---



|  |
| --- |
| [RebarContainerIterator Class](a1aff36e-7cd3-d0b8-f192-c47f4dfb8e7d.htm)   [See Also](#seeAlsoToggle) |

Resets the iterator to the initial state.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

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

# See Also

[RebarContainerIterator Class](a1aff36e-7cd3-d0b8-f192-c47f4dfb8e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3e5003c7-877c-2630-e5ff-82112e96808a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RasterSymbolPixelwidth Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Width (pixels)"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RasterSymbolPixelwidth { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RasterSymbolPixelwidth As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RasterSymbolPixelwidth { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e510f02-1a4c-3e4f-f923-e96972d03862.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DWGExportOptions Class

---



|  |
| --- |
| [Members](42ceebdc-f185-c459-115a-953d8ed972a1.htm)   [See Also](#seeAlsoToggle) |

The export options used by exporting DWG format file.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class DWGExportOptions : ACADExportOptions ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DWGExportOptions _ 	Inherits ACADExportOptions ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DWGExportOptions : public ACADExportOptions ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB BaseExportOptions](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)    
  [Autodesk.Revit.DB ACADExportOptions](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)    
  Autodesk.Revit.DB DWGExportOptions

# See Also

[DWGExportOptions Members](42ceebdc-f185-c459-115a-953d8ed972a1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e5144b2-76a1-75fb-31a5-5902dc23b172.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ScheduleDefinition](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

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

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e56968e-6c7e-a576-245f-d5e22dd61a02.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeEndHookOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"End Hook Offset Length"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarShapeEndHookOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarShapeEndHookOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarShapeEndHookOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e59b23f-0396-5577-6311-cf99c9760d78.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetDoubleValue Method

---



|  |
| --- |
| [ColorFillSchemeEntry Class](065ddef3-065a-8bd5-9d34-4d2efd126e43.htm)   [See Also](#seeAlsoToggle) |

Sets new Double value of entry.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void SetDoubleValue( 	double value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetDoubleValue ( _ 	value As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetDoubleValue( 	double value ) ``` |

#### Parameters

value
:   Type:  System Double

# Remarks

You should only use this method if the  [StorageType](45659568-cb90-6712-3355-120f7cff9dd4.htm)  property reports the type of the entry as a Double.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The entry has different storage type with Double, or value is not finite. |

# See Also

[ColorFillSchemeEntry Class](065ddef3-065a-8bd5-9d34-4d2efd126e43.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e5c8c80-64ae-77f0-90de-c3b61a78b9f3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreatePointSetIterator Method (PointCloudFilter, ElementId)

---



|  |
| --- |
| [IPointCloudAccess Interface](d5e8d1d7-9375-ce6b-ff4f-6d4764c92736.htm)   [See Also](#seeAlsoToggle) |

Implement this method to return an iterator for iterating over blocks of this point cloud.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` IPointSetIterator CreatePointSetIterator( 	PointCloudFilter rFilter, 	ElementId viewId ) ``` |

 

| Visual Basic |
| --- |
| ``` Function CreatePointSetIterator ( _ 	rFilter As PointCloudFilter, _ 	viewId As ElementId _ ) As IPointSetIterator ``` |

 

| Visual C++ |
| --- |
| ``` IPointSetIterator^ CreatePointSetIterator( 	PointCloudFilter^ rFilter,  	ElementId^ viewId ) ``` |

#### Parameters

rFilter
:   Type:  [Autodesk.Revit.DB.PointClouds PointCloudFilter](ca6f916b-2eba-f8e5-8939-1c063330c886.htm)    
     The filter used to process cloud points and determine which ones lie with the target volume.

viewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The view id for the current view passed as auxiliary information to allow the engine to optimize retrieval of points. If viewId == InvalidElementId, the query is not for a view display operation.

#### Return Value

The newly created iterator.

# See Also

[IPointCloudAccess Interface](d5e8d1d7-9375-ce6b-ff4f-6d4764c92736.htm)

[CreatePointSetIterator Overload](9e53e476-6f82-0947-b4cc-95063c0e95b0.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__3e602e58-3059-4c7f-f158-575d42984137.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Wattage Property

---



|  |
| --- |
| [InitialWattageIntensity Class](2bcbaf81-375c-2732-d67a-563d8302cd1e.htm)   [See Also](#seeAlsoToggle) |

The wattage value.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double Wattage { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Wattage As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Wattage { 	double get (); 	void set (double value); } ``` |

#### Field Value

The wattage value in W as a numerical value between 0 and 1e+30.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The wattage value is not valid because it is not between 0 and 1e+30. |

# See Also

[InitialWattageIntensity Class](2bcbaf81-375c-2732-d67a-563d8302cd1e.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__3e61755b-deef-eedc-d110-7a84533cf70b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [ExportLayerKey Class](64d77004-5c0c-9af2-cae4-39448bbaffe9.htm)   [See Also](#seeAlsoToggle) |

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

[ExportLayerKey Class](64d77004-5c0c-9af2-cae4-39448bbaffe9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e645b47-8201-373f-60e8-25ada959629a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TileColorVariance Property

---



|  |
| --- |
| [Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Color Variance" from the "Tile" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TileColorVariance { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TileColorVariance As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TileColorVariance { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble" within the range of "0, 100".

# See Also

[Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3e69c303-461e-8ea9-ac4b-26fd7f33326b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Profile1FamType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Profile"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Profile1FamType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Profile1FamType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Profile1FamType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e6aaebc-28a1-da82-8022-ec76d26122c6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreReferencesValidForLinearDimension Method

---



|  |
| --- |
| [MultiReferenceAnnotation Class](2224ac33-d7c0-bda8-70de-0005023c2149.htm)   [See Also](#seeAlsoToggle) |

If the DimensionStyleType is Linear, validates that the references are valid for an aligned multi-reference annotation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool AreReferencesValidForLinearDimension( 	Document document, 	ElementId ownerViewId, 	MultiReferenceAnnotationOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function AreReferencesValidForLinearDimension ( _ 	document As Document, _ 	ownerViewId As ElementId, _ 	options As MultiReferenceAnnotationOptions _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool AreReferencesValidForLinearDimension( 	Document^ document,  	ElementId^ ownerViewId,  	MultiReferenceAnnotationOptions^ options ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document for the multi-reference annotation.

ownerViewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The view in which the multi-reference annotation will appear.

options
:   Type:  [Autodesk.Revit.DB MultiReferenceAnnotationOptions](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)    
     Options containing the references which the dimension will witness.

#### Return Value

True DimensionStyleType does not equal Linear or if an aligned multi-reference annotation can be created from the references.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MultiReferenceAnnotation Class](2224ac33-d7c0-bda8-70de-0005023c2149.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e6f6504-c88c-f977-f914-08d8c423a5b5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TopOfPartElevation Property

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

The associated elevation to the top of fabrication part off of the current level.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public double TopOfPartElevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property TopOfPartElevation As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double TopOfPartElevation { 	double get (); } ``` |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e725855-09ae-92ef-3d3e-ea26353b1101.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarBendData Constructor

---



|  |
| --- |
| [RebarBendData Class](027b5619-ad82-74b3-1d78-efe86a1ef96b.htm)   [See Also](#seeAlsoToggle) |

Constructs a new RebarBendData with default settings.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public RebarBendData() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarBendData() ``` |

# See Also

[RebarBendData Class](027b5619-ad82-74b3-1d78-efe86a1ef96b.htm)

[RebarBendData Overload](4d1aabbd-79b2-617f-151b-2e4097c8a4d5.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3e7b8773-eb2b-5bdb-cc35-37ee992f988c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewDependency Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Dependency"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ViewDependency { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewDependency As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ViewDependency { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e7cb75e-73ad-d381-1f89-3dab63463c7e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PickBox Method (PickBoxStyle, String)

---



|  |
| --- |
| [Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)   [See Also](#seeAlsoToggle) |

Invokes a general purpose two-click editor that lets the user to specify a rectangular area on the screen.

**Namespace:**   [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PickedBox PickBox( 	PickBoxStyle style, 	string statusPrompt ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function PickBox ( _ 	style As PickBoxStyle, _ 	statusPrompt As String _ ) As PickedBox ``` |

 

| Visual C++ |
| --- |
| ``` public: PickedBox^ PickBox( 	PickBoxStyle style,  	String^ statusPrompt ) ``` |

#### Parameters

style
:   Type:  [Autodesk.Revit.UI.Selection PickBoxStyle](b66a5404-4dba-abc0-f16d-0477e5c8a974.htm)    
     Specifies the value that controls the style of the pick box.

statusPrompt
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The message shown on the status bar.

#### Return Value

The picked box that contains two XYZ points.

# Remarks

The method starts an editor and returns when it finishes. Returns a PickedBox that contains two XYZ points.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the style is not a recognized value. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the argument statusPrompt is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | Thrown when the Revit user cancelled this operation. Thrown when the Revit user tried to switch the active view, close the active document or Revit application when responding to this mode. |

# See Also

[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)

[PickBox Overload](976cde81-988a-d8bf-fc3f-07f62b18b488.htm)

[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.htm)

<!-- Start of Syntax__3e7e48ca-efc5-27ee-e6d6-ddf5ec6934ff.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallTypeWidthMeasuredAt Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Width Measured At"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId WallTypeWidthMeasuredAt { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WallTypeWidthMeasuredAt As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ WallTypeWidthMeasuredAt { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e83bc2c-7f43-2e97-3df7-519bb07e7695.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFailureDefinitionId Method

---



|  |
| --- |
| [FailureMessage Class](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)   [See Also](#seeAlsoToggle) |

Retrieves the id of the failure definition for the failure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FailureDefinitionId GetFailureDefinitionId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFailureDefinitionId As FailureDefinitionId ``` |

 

| Visual C++ |
| --- |
| ``` public: FailureDefinitionId^ GetFailureDefinitionId() ``` |

#### Return Value

The id of the FailureDefinition for the failure.

# See Also

[FailureMessage Class](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e83c46e-170c-60b9-960f-e809a1431e96.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Second Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol s, indicating unit Seconds.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Second { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Second As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Second { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e845cad-eca0-ccb3-785b-48a32a9f2677.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IRebarUpdateServer Interface

---



|  |
| --- |
| [Members](f954b20f-a21b-35d3-fab1-d2bfdb616f39.htm)   [See Also](#seeAlsoToggle) |

Represents an interface that should be overridden to allow the generation and update of free form rebar geometry.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public interface IRebarUpdateServer : IExternalServer ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IRebarUpdateServer _ 	Inherits IExternalServer ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IRebarUpdateServer : IExternalServer ``` |

# Remarks

This interface should be overridden in order to create a free form rebar with constraints and to allow generation and update of its geometry.

Once a rebar is created with a server, it will be called  [GetCustomHandles(RebarHandlesData)](37833063-e74a-26bb-bdf8-9700f7a446cb.htm)  function. In the execution on this function should be defined the handles of the rebar.

Based on these handles rebar constraints can be defined. Once the constraints are defined a regeneration should be triggered in order to generate the bar geometry.

During the regeneration the functions  [GenerateCurves(RebarCurvesData)](2b83cc23-076c-1843-f078-46d0c1f2dc74.htm)  and  [TrimExtendCurves(RebarTrimExtendData)](6db89b01-28aa-8b95-f3c0-a0f00cdb84c5.htm)  will be called. For GenerateCurves() it is supposed to calculate bars in set based on constraints. For TrimExtendCurves() it is supposed to trim or extend curves that were obtained from GenerateCurves(). Also in this function new constraints for start and end bar handles can be created. After the execution of these two functions the bar should appear on screen.

Every time when a constraint is modified a new regeneration is triggered and the functions GenerateCurves() and TrimExtendCurves() are called again.

We also can edit constraints for this rebar. When user starts to do this, the function  [GetHandlesPosition(RebarHandlePositionData)](7f991fe0-6c77-ba43-3d52-64a8c0390809.htm)  will be called and it is supposed to return positions of handles defined in GetCustomHandles(). This positions will be shown on screen. While editing constraints if the mouse is over a position that was specified, the function  [GetCustomHandleName(RebarHandleNameData)](7f072a66-48c3-43d1-5d3e-a8a5ae787477.htm)  will be called in order to obtain the name of that handle.

While editing constraints an user will modify constraints (e.g. add a new reference or remove one) a regeneration will be triggered and the functions GenerateCurves() and TrimExtendCurves() will be called again.

# See Also

[IRebarUpdateServer Members](f954b20f-a21b-35d3-fab1-d2bfdb616f39.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3e86f8bf-b9b6-5383-3f65-0a9c9a5acf61.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLabelFor Method (gbXMLBuildingType, Document)

---



|  |
| --- |
| [LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.htm)   [See Also](#seeAlsoToggle) |

Gets the user-visible name for a gbXMLBuildingType.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static string GetLabelFor( 	gbXMLBuildingType buildingType, 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetLabelFor ( _ 	buildingType As gbXMLBuildingType, _ 	document As Document _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ GetLabelFor( 	gbXMLBuildingType buildingType,  	Document^ document ) ``` |

#### Parameters

buildingType
:   Type:  [Autodesk.Revit.DB.Analysis gbXMLBuildingType](74e09dc3-6b9a-cc3b-a493-d6a20a60bfd6.htm)    
     The gbXMLBuildingType to get the user-visible name.

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document from which to get the gbXMLBuildingType.

# Remarks

The name is obtained in the current Revit language.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input gXMLBuildingType is not available in the document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.htm)

[GetLabelFor Overload](39e41221-70f9-fae6-53e6-872eff5a2c63.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e87bc0e-e04b-f76a-2b06-82e951b5aec2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportPatternTable Class

---



|  |
| --- |
| [Members](e5b88354-d033-f559-f254-bbd7c84a72a1.htm)   [See Also](#seeAlsoToggle) |

A table supporting a mapping of FillPatterns in Revit to pattern names that will be set in the target export format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class ExportPatternTable : IEnumerable<KeyValuePair<ExportPatternKey, ExportPatternInfo>>,  	IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExportPatternTable _ 	Implements IEnumerable(Of KeyValuePair(Of ExportPatternKey, ExportPatternInfo)),  _ 	IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExportPatternTable : IEnumerable<KeyValuePair<ExportPatternKey^, ExportPatternInfo^>>,  	IDisposable ``` |

# Remarks

This table is structured as a mapping from  [ExportPatternKey](8e55a491-0886-37f5-b867-e4eea95276eb.htm)  to  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  members. The  [ExportPatternKey](8e55a491-0886-37f5-b867-e4eea95276eb.htm)  contains the identification information for the pattern table: the Revit fill pattern type and name. The  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  contains the pattern name to use in the export format.

The table can be accessed via direct iteration as a collection of KeyValuePairs, or by traversal of the stored keys obtained from GetKeys(), or via specific lookup of a key constructed externally. In all cases, the  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  returned will be a copy of the  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  from the table. In order to make changes to the  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  and use those settings during export, set the modified  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  back into the table using the same key.

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB ExportPatternTable

# See Also

[ExportPatternTable Members](e5b88354-d033-f559-f254-bbd7c84a72a1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e89356a-f974-728b-9e94-ac267b7c2d76.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Size Property

---



|  |
| --- |
| [CombinableElementArray Class](dc5f6afb-a30d-dc82-fcd3-340eff1685c7.htm)   [See Also](#seeAlsoToggle) |

Returns the number of CombinableElements that are in the array.

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

[CombinableElementArray Class](dc5f6afb-a30d-dc82-fcd3-340eff1685c7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e8c4422-11eb-4713-e776-ce6511331e00.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LayeredNormal Property

---



|  |
| --- |
| [AdvancedLayered Class](308d3112-a63f-0c76-7737-8cf201454790.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Image" from the "AdvancedLayered" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string LayeredNormal { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LayeredNormal As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ LayeredNormal { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyReference" and will only contain a reference to a connected image.

# See Also

[AdvancedLayered Class](308d3112-a63f-0c76-7737-8cf201454790.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3e901c1a-530d-90a8-94a5-fba3b4f0d2fc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OnStandby Property

---



|  |
| --- |
| [MechanicalEquipmentSet Class](ce3c8e90-566c-bb8e-57f7-06f10dac5b7c.htm)   [See Also](#seeAlsoToggle) |

The number of pieces of mechanical equipment that are not operational at any given time.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public int OnStandby { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property OnStandby As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int OnStandby { 	int get (); 	void set (int value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: There should be at least one equipment on duty. |

# See Also

[MechanicalEquipmentSet Class](ce3c8e90-566c-bb8e-57f7-06f10dac5b7c.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__3e907223-e8c2-a8b0-0031-53cd7befab06.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [MEPBuildingConstructionSet Class](fbe2c9fe-89ea-fc75-e418-cebc452ca1dd.htm)   [See Also](#seeAlsoToggle) |

Removes every MEPBuildingConstruction from the set, rendering it empty.

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

[MEPBuildingConstructionSet Class](fbe2c9fe-89ea-fc75-e418-cebc452ca1dd.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__3e9653ff-d2e7-3058-0bbd-6fb6649b81a0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MinimumDigits Property

---



|  |
| --- |
| [NumericRevisionSettings Class](3de46f00-fbf9-0c6b-b7fa-5d33052d0091.htm)   [See Also](#seeAlsoToggle) |

Controls the minimum number of digits for a revision number.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public int MinimumDigits { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MinimumDigits As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int MinimumDigits { 	int get (); 	void set (int value); } ``` |

# Remarks

Use MinimumDigits to force the minimum number of digits for a revision number. Zeros will be added to the front of the revision number until the minimum number of digits is satisfied. For example, if MinimumDigits is 3, then 9 will be printed as 009 and 10 will be printed as 010. If MinimumDigits is 1, then no zeros are added to the front of the revision number. The default value for MinimumDigits is 1. Values less than 1 are not allowed.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for minimumDigits is not positive. |

# See Also

[NumericRevisionSettings Class](3de46f00-fbf9-0c6b-b7fa-5d33052d0091.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3e9fa6ec-3739-b5cb-e0a7-ebea6149b24b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralConnectionInputElements Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Input Elements"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralConnectionInputElements { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralConnectionInputElements As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralConnectionInputElements { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ea2e4ff-1569-413a-35a0-5f1f83575a0b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionIshapeWebToeOfFillet Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Web Toe of Fillet"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralSectionIshapeWebToeOfFillet { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralSectionIshapeWebToeOfFillet As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralSectionIshapeWebToeOfFillet { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ea47f9a-607e-72d0-4a48-552c58ab5cbc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FbxLightPhotometrics Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Light Source Definition"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FbxLightPhotometrics { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FbxLightPhotometrics As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FbxLightPhotometrics { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ea7262c-5f95-91d8-dd81-b3292e3dc0b5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecPowerFactor Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Power Factor"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecPowerFactor { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecPowerFactor As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecPowerFactor { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3eaab06f-0da5-dd0a-6063-b3907f6de7a8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointCollection Class

---



|  |
| --- |
| [Members](9e2f0516-82fb-f683-5358-b51d33c31470.htm)   [See Also](#seeAlsoToggle) |

A class that represents a set of points created and returned by Revit in response to a query.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class PointCollection : IEnumerable<CloudPoint>,  	IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PointCollection _ 	Implements IEnumerable(Of CloudPoint), IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PointCollection : IEnumerable<CloudPoint>,  	IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.PointClouds PointCollection

# See Also

[PointCollection Members](9e2f0516-82fb-f683-5358-b51d33c31470.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__3eac6440-7a8e-4dfb-2bf2-7be55ecb2488.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UserWorksets Property

---



|  |
| --- |
| [RelinquishOptions Class](af30374c-7e99-d52e-f648-c5969e91e9d8.htm)   [See Also](#seeAlsoToggle) |

True means all user-created worksets owned by the current user should be relinquished. False means none of these are relinquished.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool UserWorksets { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property UserWorksets As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool UserWorksets { 	bool get (); 	void set (bool value); } ``` |

# Remarks

This defaults to false in the User Interface.

# See Also

[RelinquishOptions Class](af30374c-7e99-d52e-f648-c5969e91e9d8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3eacc872-bb46-73a5-9ae7-d309d1d3ad64.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InsulationType Class

---



|  |
| --- |
| [Members](cd6b4f1a-0b8b-66d0-e97c-0f8908957a0c.htm)   [See Also](#seeAlsoToggle) |

Represents electrical insulation type definition information.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class InsulationType : ElementType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class InsulationType _ 	Inherits ElementType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class InsulationType : public ElementType ``` |

# Remarks

Insulation type is defined based on corresponding wire material type and temperature rating type.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  Autodesk.Revit.DB.Electrical InsulationType

# See Also

[InsulationType Members](cd6b4f1a-0b8b-66d0-e97c-0f8908957a0c.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3eb3c125-de9d-bb0d-4463-a1443e2a3338.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAutomaticLanding Property

---



|  |
| --- |
| [StairsLanding Class](cae109cd-bc50-6c36-300e-35d3457c0982.htm)   [See Also](#seeAlsoToggle) |

True if the landing is an automatic landing, False otherwise.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsAutomaticLanding { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsAutomaticLanding As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsAutomaticLanding { 	bool get (); } ``` |

# See Also

[StairsLanding Class](cae109cd-bc50-6c36-300e-35d3457c0982.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__3ebfaa4f-6802-ffb2-5f5a-74ae3d27c6f6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConceptualEnergyData Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Conceptual Energy Data"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ConceptualEnergyData { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ConceptualEnergyData As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ConceptualEnergyData { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ec2a3c5-2534-6c0c-e08b-1ac02735292c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSystemsAnalysisWorkflowNames Method

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Returns names for systems analysis workflows.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public IList<string> GetSystemsAnalysisWorkflowNames() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSystemsAnalysisWorkflowNames As IList(Of String) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<String^>^ GetSystemsAnalysisWorkflowNames() ``` |

#### Return Value

An array of names of systems analysis workflows.

# Remarks

The array that is returned contains the name of the systems analysis workflow, in the order they are specified in Options.

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__3ec5c5dc-23de-38d4-fe68-527bfcab311a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Size Property

---



|  |
| --- |
| [WireTypeSet Class](4cd0b254-674b-e605-89e3-a016d586f535.htm)   [See Also](#seeAlsoToggle) |

Returns the number of wire types that are in the set.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
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

[WireTypeSet Class](4cd0b254-674b-e605-89e3-a016d586f535.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3ec9c4d7-b9b0-61b0-9250-e104781e5d31.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FaceIsNoLongerVertical Property

---



|  |
| --- |
| [BuiltInFailures WallFailures Class](22d82d7e-a7d6-c096-991c-728df0b2d61c.htm)   [See Also](#seeAlsoToggle) |

Face defining this vertical Wall is no longer vertical.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FaceIsNoLongerVertical { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FaceIsNoLongerVertical As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FaceIsNoLongerVertical { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures WallFailures Class](22d82d7e-a7d6-c096-991c-728df0b2d61c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ecba497-f621-8877-7711-14923668318d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarSystemAddlInteriorOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Additional Interior Cover Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarSystemAddlInteriorOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarSystemAddlInteriorOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarSystemAddlInteriorOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ecc065c-dcf0-3b97-96da-95c7a00a92e0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCutGeometryWarn Property

---



|  |
| --- |
| [BuiltInFailures CutFailures Class](6bec436a-fefb-b90c-454f-ce494f3b06c5.htm)   [See Also](#seeAlsoToggle) |

Elements do not intersect.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCutGeometryWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCutGeometryWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCutGeometryWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CutFailures Class](6bec436a-fefb-b90c-454f-ce494f3b06c5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ecd9cd1-d9c9-025d-af65-10f6f20ee309.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CustomAxis Property

---



|  |
| --- |
| [IFCExtrusionCalculatorOptions Class](3aa9bc3b-5ce0-e0ba-4211-9a08526c1c1b.htm)   [See Also](#seeAlsoToggle) |

The custom axis to try (if extrusionAxes includes an option for a custom direction).

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public XYZ CustomAxis { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CustomAxis As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ CustomAxis { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[IFCExtrusionCalculatorOptions Class](3aa9bc3b-5ce0-e0ba-4211-9a08526c1c1b.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__3ecdd8b3-57ff-9ec7-8f48-d381414413de.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportFontTableIterator Class

---



|  |
| --- |
| [Members](b838f824-1a12-85ca-30a2-68c940971c20.htm)   [See Also](#seeAlsoToggle) |

An iterator to a set of font table.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class ExportFontTableIterator : IEnumerator<KeyValuePair<ExportFontKey, ExportFontInfo>> ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExportFontTableIterator _ 	Implements IEnumerator(Of KeyValuePair(Of ExportFontKey, ExportFontInfo)) ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExportFontTableIterator : IEnumerator<KeyValuePair<ExportFontKey^, ExportFontInfo^>> ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ExportFontTableIterator

# See Also

[ExportFontTableIterator Members](b838f824-1a12-85ca-30a2-68c940971c20.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ecde669-5e9d-e4fd-5b19-c5605684bce1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralAssetClass Property

---



|  |
| --- |
| [StructuralAsset Class](39c2e2ad-474e-2514-bc15-07c24a989a61.htm)   [See Also](#seeAlsoToggle) |

The type of material that this structural asset describes (e.g. wood, concrete, metal.)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public StructuralAssetClass StructuralAssetClass { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property StructuralAssetClass As StructuralAssetClass 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property StructuralAssetClass StructuralAssetClass { 	StructuralAssetClass get (); } ``` |

# See Also

[StructuralAsset Class](39c2e2ad-474e-2514-bc15-07c24a989a61.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ece56e2-3980-c86f-cfdf-7b5d2b371da5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [Definitions Class](5ff217ff-215d-9d1a-6555-3f45b34a5517.htm)   [See Also](#seeAlsoToggle) |

Creates a new parameter definition using specified options.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public Definition Create( 	ExternalDefinitionCreationOptions option ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Create ( _ 	option As ExternalDefinitionCreationOptions _ ) As Definition ``` |

 

| Visual C++ |
| --- |
| ``` public: Definition^ Create( 	ExternalDefinitionCreationOptions^ option ) ``` |

#### Parameters

option
:   Type:  [Autodesk.Revit.DB ExternalDefinitionCreationOptions](1cd9e425-23a3-04f8-c130-4d4a799abd13.htm)    
     The options used to create the new parameter definition.

#### Return Value

If successful a reference to the new parameter definition is returned, otherwise    a null reference (  Nothing  in Visual Basic)  .

# Remarks

This method only supports creation of new external definitions (shared parameters).

# See Also

[Definitions Class](5ff217ff-215d-9d1a-6555-3f45b34a5517.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ed202d6-0aae-32ec-5b02-50ac0274728b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetApplicableDemandFactor Method

---



|  |
| --- |
| [ElectricalDemandFactorDefinition Class](8ad48bcf-05f3-b9c3-ebfb-2a7b2db2fd83.htm)   [See Also](#seeAlsoToggle) |

This method will return the applicable demand factor for the specified number of devices or load.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public double GetApplicableDemandFactor( 	double numberOrLoad ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetApplicableDemandFactor ( _ 	numberOrLoad As Double _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetApplicableDemandFactor( 	double numberOrLoad ) ``` |

#### Parameters

numberOrLoad
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The number of devices or load for which the demand factor should be looked up.

#### Return Value

The applicable demand factor.

# See Also

[ElectricalDemandFactorDefinition Class](8ad48bcf-05f3-b9c3-ebfb-2a7b2db2fd83.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3ed483b3-662b-8205-fabd-3f637eb89534.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LbMassPerInSup3 Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol lb/inÂ³, indicating unit Pounds mass per cubic inch.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LbMassPerInSup3 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LbMassPerInSup3 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LbMassPerInSup3 { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ee1e9dc-eb78-7089-8bde-c1d928b26fe3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecPanelTotalDemandFactorParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Total Demand Factor"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecPanelTotalDemandFactorParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecPanelTotalDemandFactorParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecPanelTotalDemandFactorParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ee4da28-2a21-f9a3-0b58-03286ec21bfc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetElementIdValue Method

---



|  |
| --- |
| [ScheduleFilter Class](a5dfec9f-1efd-b507-d079-eabcbf5032f8.htm)   [See Also](#seeAlsoToggle) |

Gets the filter value for a filter using an ElementId value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId GetElementIdValue() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetElementIdValue As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetElementIdValue() ``` |

#### Return Value

The filter value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The filter value is not an ElementId. |

# See Also

[ScheduleFilter Class](a5dfec9f-1efd-b507-d079-eabcbf5032f8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3eeb55a9-ced3-165d-5a9e-d75a9d7f2f20.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPath Method (String)

---



|  |
| --- |
| [ImageTypeOptions Class](981135c3-777b-df9b-747f-60a35b74e00e.htm)   [See Also](#seeAlsoToggle) |

Update the path of the file that specifies the image to be used.

The provided string path must specify a local file. The path can be absolute or relative to the project's location. ImageType will respectively use an absolute or relative path.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public void SetPath( 	string path ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetPath ( _ 	path As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetPath( 	String^ path ) ``` |

#### Parameters

path
:   Type:  System String    
     The file path that specifies the image to be used.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ImageTypeOptions Class](981135c3-777b-df9b-747f-60a35b74e00e.htm)

[SetPath Overload](64f4404e-a352-6fc6-72e2-821855ae1c50.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3eebff6a-ccfa-d4ab-fcf8-239d4d2ec8de.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDefaultFloorType Method

---



|  |
| --- |
| [Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.htm)   [See Also](#seeAlsoToggle) |

Returns id of default floor type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static ElementId GetDefaultFloorType( 	Document document, 	bool isFoundation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetDefaultFloorType ( _ 	document As Document, _ 	isFoundation As Boolean _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ GetDefaultFloorType( 	Document^ document,  	bool isFoundation ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

isFoundation
:   Type:  System Boolean    
     True to return id of foundation floor type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3eec7500-a2e5-bd1f-2eac-5e2ea6953104.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Elbow Property

---



|  |
| --- |
| [MEPCurveType Class](97c98bd6-0966-5b0c-6f75-4c34f16adce1.htm)   [See Also](#seeAlsoToggle) |

The default elbow fitting of the MEP curve type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilySymbol Elbow { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Elbow As FamilySymbol 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property FamilySymbol^ Elbow { 	FamilySymbol^ get (); 	void set (FamilySymbol^ value); } ``` |

# Remarks

This property is used to retrieve the default elbow fitting of the MEP curve type, and can be    a null reference (  Nothing  in Visual Basic)  if there is no default value. Use  [RoutingPreferenceManager](a8300b97-72a6-beb5-733b-ec4cfea6c472.htm)  to set this property for PipeType MEPCurves.

# See Also

[MEPCurveType Class](97c98bd6-0966-5b0c-6f75-4c34f16adce1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3eed68c4-620a-c993-54b2-5e51f04b814c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Formula Property

---



|  |
| --- |
| [FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)   [See Also](#seeAlsoToggle) |

The formula.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public string Formula { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Formula As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Formula { 	String^ get (); } ``` |

# Remarks

Returns    a null reference (  Nothing  in Visual Basic)  if there is no formula governing this parameter.

# See Also

[FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3eeea616-44b9-1dee-fec7-d15ae91f2abd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyNoExternalParametersError Property

---



|  |
| --- |
| [BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)   [See Also](#seeAlsoToggle) |

Family's Category can't be changed because the Family contains Shared Parameters which are not permitted in the new Category.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FamilyNoExternalParametersError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FamilyNoExternalParametersError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FamilyNoExternalParametersError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3eef29c9-7384-77e7-e4c1-d2149ea79e95.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentSaved Event

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the DocumentSaved event to be notified immediately after Revit has finished saving a document.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<DocumentSavedEventArgs> DocumentSaved ``` |

 

| Visual Basic |
| --- |
| ``` Public Event DocumentSaved As EventHandler(Of DocumentSavedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<DocumentSavedEventArgs^>^ DocumentSaved { 	void add (EventHandler<DocumentSavedEventArgs^>^ value); 	void remove (EventHandler<DocumentSavedEventArgs^>^ value); } ``` |

# Remarks

This event is raised immediately after Revit has finished saving a document. Note that the first save of a newly created document will raise  [DocumentSavedAs](6d3e2981-dfe0-fd33-9bd0-57e04815c4fd.htm)  rather than the DocumentSaved event. It is raised even when document saving failed or was cancelled (during DocumentSaving event).

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Check the 'Status' property in event's argument to see whether the action itself was successful or not.

This event is not cancellable, for the process of saving document has already been finished.

The following API functions are not available for the current document during this event:

* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  .
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__3ef30e6a-73e8-2d80-7f76-00fe1f42fed7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPrimaryViewId Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Get the id of the primary view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId GetPrimaryViewId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPrimaryViewId As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetPrimaryViewId() ``` |

#### Return Value

The id of the primary view, or InvalidElementId if there is no primary view.

# Remarks

The primary view is the view from which a dependent view is created.

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ef858e5-0984-0d1d-c063-2ff07feed167.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DoesConduitStandardTypeExist Method

---



|  |
| --- |
| [ConduitSizeSettings Class](d385e4b4-f675-9bcc-d067-5ca7d1d000d4.htm)   [See Also](#seeAlsoToggle) |

Checks if the specified conduit standard exist.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public bool DoesConduitStandardTypeExist( 	string standardName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function DoesConduitStandardTypeExist ( _ 	standardName As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool DoesConduitStandardTypeExist( 	String^ standardName ) ``` |

#### Parameters

standardName
:   Type:  System String    
     The conduit standard name.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ConduitSizeSettings Class](d385e4b4-f675-9bcc-d067-5ca7d1d000d4.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3ef8f558-c706-9972-ad70-594f6762e7a9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [AnalyticalOpening Class](201af27b-c908-83b6-19f2-23d5fa9b69ed.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of an Analytical Opening within the project.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public static AnalyticalOpening Create( 	Document aDoc, 	CurveLoop curveLoop, 	ElementId panelId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	aDoc As Document, _ 	curveLoop As CurveLoop, _ 	panelId As ElementId _ ) As AnalyticalOpening ``` |

 

| Visual C++ |
| --- |
| ``` public: static AnalyticalOpening^ Create( 	Document^ aDoc,  	CurveLoop^ curveLoop,  	ElementId^ panelId ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Revit document.

curveLoop
:   Type:  [Autodesk.Revit.DB CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     CurveLoop for the Analytical Opening.

panelId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     ElementId of the AnalyticalPanel on which we create the Opening.

#### Return Value

The newly created AnalyticalOpening instance.

# Remarks

CurveLoop must be planar, not self-intersecting and in the same plane as the Analytical Panel. CurveLoop must intersect or to be inside the AnalyticalPanel contour. PanelId must be the ElementId of an AnalyticalPanel otherwise an exception is thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One of the following requirements is not satisfied : - curve loop curveLoop is not planar - curve loop curveLoop is self-intersecting - curve loop curveLoop contains zero length curves - curve loop curveLoop is not inside or does not intersect the AnalyticalPanel on which we want to create the Opening. - panelId is not the ElementId of an AnalyticalPanel - curve loop curveLoop is not in the same plane as the Analytical Panel |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[AnalyticalOpening Class](201af27b-c908-83b6-19f2-23d5fa9b69ed.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3efb775d-b129-0e0b-5f57-5290eb12fa43.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetInnerRule Method

---



|  |
| --- |
| [FilterInverseRule Class](bd21b884-c026-5a16-4470-72172b71db4a.htm)   [See Also](#seeAlsoToggle) |

Gets the rule being inverted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FilterRule GetInnerRule() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetInnerRule As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: FilterRule^ GetInnerRule() ``` |

# See Also

[FilterInverseRule Class](bd21b884-c026-5a16-4470-72172b71db4a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3efbcd20-13d2-e518-a827-bd56d200812f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotConstrainBasePointAlignments Property

---



|  |
| --- |
| [BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)   [See Also](#seeAlsoToggle) |

Alignments to base points cannot be constrained.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotConstrainBasePointAlignments { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotConstrainBasePointAlignments As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotConstrainBasePointAlignments { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3efddea0-63fb-8440-aead-904f2f393ff2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Visibility Property

---



|  |
| --- |
| [DirectContext3DHandleSettings Class](cc9d7b07-a4d9-8570-9ed8-c953e241c0d6.htm)   [See Also](#seeAlsoToggle) |

Visibility of the handle and the associated DirectContext3D graphics. A value of true means that the graphics are visible.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool Visibility { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Visibility As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool Visibility { 	bool get (); 	void set (bool value); } ``` |

# See Also

[DirectContext3DHandleSettings Class](cc9d7b07-a4d9-8570-9ed8-c953e241c0d6.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__3eff487b-cf88-edb9-d43d-b637164e64e6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsStartLevelParam Property

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
| ``` public static ForgeTypeId RbsStartLevelParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsStartLevelParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsStartLevelParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f015caf-7844-ab56-c962-9020b141e0d2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetReportedShape Method

---



|  |
| --- |
| [RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)   [See Also](#seeAlsoToggle) |

This method changes the RebarShape of a Free Form Rebar that is using RebarWorkInstructions.Straight property to the provided RebarShape.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void SetReportedShape( 	ElementId rebarShapeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetReportedShape ( _ 	rebarShapeId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetReportedShape( 	ElementId^ rebarShapeId ) ``` |

#### Parameters

rebarShapeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

# Remarks

The Rebar element RebarWorkInstructions property should be Straight. The rebarShapeId parameter should be the id of a straight RebarShape (single straight segment, no RebarHookType, no EndTreatmentType). Moreover the straight RebarShape RebarStyle should match ( if the current RebarShape RebarStyle is Standard then the RebarShape cannot be changed to a straigh RebarShape using the RebarStyle Stirrup/Tie ). If current RebarShape and the provided rebarShapeId has Stirrup/Tie RebarStyle then also the StirrupTieAttachmentType should match ( both InteriorFace or ExteriorFace ).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | rebarShapeId cannot be set as a reporting RebarShape for this Rebar element. |

# See Also

[RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3f01880c-ea78-a3e3-e216-4836503bbda3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [Units Class](89d89465-897f-4105-b935-27edf67aab3e.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [Units](89d89465-897f-4105-b935-27edf67aab3e.htm)

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

[Units Class](89d89465-897f-4105-b935-27edf67aab3e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f01c0da-ac5b-129c-1dea-7b9f766491d2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyTemplatePath Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Default path for family template files.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string FamilyTemplatePath { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property FamilyTemplatePath As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ FamilyTemplatePath { 	String^ get (); } ``` |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__3f01f592-4d76-4347-23d9-31becc3c54c0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFailingElementIds Method

---



|  |
| --- |
| [FailureMessageAccessor Class](753477d8-b720-97a0-26f5-439d49de418c.htm)   [See Also](#seeAlsoToggle) |

Retrieves Ids of Elements that have caused the failure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> GetFailingElementIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFailingElementIds As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ GetFailingElementIds() ``` |

#### Return Value

Ids of Elements that have caused the failure.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailureMessageAccessor has not been properly initialized. |

# See Also

[FailureMessageAccessor Class](753477d8-b720-97a0-26f5-439d49de418c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f02ab20-256e-31e8-f283-fba52ae70e53.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotHaveIndependentOverlappingGrids Property

---



|  |
| --- |
| [BuiltInFailures CurtainWallFailures Class](a3d691c9-5f8f-29ca-cfad-fa1d1d66f203.htm)   [See Also](#seeAlsoToggle) |

Overlapping independent type associated gridlines are not allowed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotHaveIndependentOverlappingGrids { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotHaveIndependentOverlappingGrids As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotHaveIndependentOverlappingGrids { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CurtainWallFailures Class](a3d691c9-5f8f-29ca-cfad-fa1d1d66f203.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f0456e9-59a6-2c68-0f0c-d2355edb9693.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VertexPair Class

---



|  |
| --- |
| [Members](6f8fbf93-a920-3b42-b00a-253a8547d220.htm)   [See Also](#seeAlsoToggle) |

Indices of a pair of vertices in two CurveLoops(one vertex in each loop).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class VertexPair : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class VertexPair _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class VertexPair : IDisposable ``` |

# Remarks

A vertex is specified by the index in the CurveLoop of the curve having that vertex as its start point. Indexes start at 0.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB VertexPair

# See Also

[VertexPair Members](6f8fbf93-a920-3b42-b00a-253a8547d220.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f089f69-3a06-cff9-dbc7-a2ed58192f85.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WriteAccessGranted Method

---



|  |
| --- |
| [Schema Class](9817e7db-8367-ea4e-1769-0488f3faa37f.htm)   [See Also](#seeAlsoToggle) |

Checks whether Entities of this Schema may be stored by the current add-in.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool WriteAccessGranted() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function WriteAccessGranted As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool WriteAccessGranted() ``` |

#### Return Value

True if write access is allowed.

# See Also

[Schema Class](9817e7db-8367-ea4e-1769-0488f3faa37f.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)

<!-- Start of Syntax__3f08eefc-5cb4-69b4-4ae8-dddd5705f5c9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DebugtabDataboundcontrolsdemoInteger Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Integer"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DebugtabDataboundcontrolsdemoInteger { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DebugtabDataboundcontrolsdemoInteger As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DebugtabDataboundcontrolsdemoInteger { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f09c2c2-b9b1-052c-c058-81f569eb5966.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotConvertSketch Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Can't convert Sketch to Rebar Shape.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotConvertSketch { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotConvertSketch As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotConvertSketch { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f0f3b10-8a75-b8ca-c10d-17755ecde8f5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MepAnalyticalLoopName Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Name"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MepAnalyticalLoopName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MepAnalyticalLoopName As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MepAnalyticalLoopName { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f0f9fcb-72f4-a968-a600-25590fc3b0c6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [SteelElementProperties Class](911b649a-d108-14a2-dc09-8e97d489c17d.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.Steel](9b98b590-ace1-9487-a688-8942d90305f1.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
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

[SteelElementProperties Class](911b649a-d108-14a2-dc09-8e97d489c17d.htm)

[Autodesk.Revit.DB.Steel Namespace](9b98b590-ace1-9487-a688-8942d90305f1.htm)

<!-- Start of Syntax__3f140e73-ea0e-8d67-7061-63ff73d2de4c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSizeCount Method

---



|  |
| --- |
| [CableTraySizes Class](dbd6f408-fbae-1fe0-0e61-7d611141d6b5.htm)   [See Also](#seeAlsoToggle) |

Gets the size count of the cable tray size table.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public int GetSizeCount() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSizeCount As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int GetSizeCount() ``` |

# See Also

[CableTraySizes Class](dbd6f408-fbae-1fe0-0e61-7d611141d6b5.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3f1b13ff-0488-0a46-b646-21c2e29398e7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalResourceTypes.BuiltInExternalResourceTypes Class

---



|  |
| --- |
| [ExternalResourceTypes Class](5baf8951-9e05-5a7d-a507-ec2a0161d3da.htm)   [Members](be4b0440-8d50-c403-2125-f26d9a484018.htm)   [See Also](#seeAlsoToggle) |

A collection of ids of the ExternalResourceTypes provided by Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class BuiltInExternalResourceTypes ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class BuiltInExternalResourceTypes ``` |

 

| Visual C++ |
| --- |
| ``` public ref class BuiltInExternalResourceTypes abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ExternalResourceTypes BuiltInExternalResourceTypes

# See Also

[ExternalResourceTypes BuiltInExternalResourceTypes Members](be4b0440-8d50-c403-2125-f26d9a484018.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f22ee55-5f27-bd05-2947-e023528a719a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### YJustification Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The justification of the framing element in Y.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public enum YJustification ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration YJustification ``` |

 

| Visual C++ |
| --- |
| ``` public enum class YJustification ``` |

# Members

| Member name | Description |
| --- | --- |
| Left | Justification to the left of the element. |
| Center | Justification to the geometrical center of the element. |
| Origin | Justification to the origin of the element. |
| Right | Justification to the right of the element. |

# See Also

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3f299d95-fd17-23ea-0916-8b3e1b4009f4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBlue Method

---



|  |
| --- |
| [ColorWithTransparency Class](b68f80e1-5ea0-a485-ec3e-7dd077043230.htm)   [See Also](#seeAlsoToggle) |

get blue

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public uint GetBlue() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBlue As UInteger ``` |

 

| Visual C++ |
| --- |
| ``` public: unsigned int GetBlue() ``` |

#### Return Value

blue

# See Also

[ColorWithTransparency Class](b68f80e1-5ea0-a485-ec3e-7dd077043230.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f2b4bc7-e405-9fb5-8aff-cfc87d021fc5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsPressureDrop Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Pressure Drop"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsPressureDrop { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsPressureDrop As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsPressureDrop { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f3269fc-367c-1fec-9ddb-d0b54ecc4f0e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WhereElementIsCurveDriven Method

---



|  |
| --- |
| [FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)   [See Also](#seeAlsoToggle) |

Applies an ElementIsCurveDrivenFilter to the collector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FilteredElementCollector WhereElementIsCurveDriven() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function WhereElementIsCurveDriven As FilteredElementCollector ``` |

 

| Visual C++ |
| --- |
| ``` public: FilteredElementCollector^ WhereElementIsCurveDriven() ``` |

#### Return Value

A handle to this collector. This is the same collector that has just been modified, returned so you can chain multiple calls together in one line.

# Remarks

Only elements that are curve driven will pass the collector. If you have an active iterator to this collector it will be stopped by this call.

# See Also

[FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f331b67-b918-5d8d-7fad-7313614c6e5e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationAncillaryType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all fabrication ancillary types.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public enum FabricationAncillaryType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration FabricationAncillaryType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class FabricationAncillaryType ``` |

# Members

| Member name | Description |
| --- | --- |
| Unknown | Unknown or unsupported ancillary type. |
| Fixing | Ancillary nuts and bolts. Used to fix and bind other ancillaries. |
| Corner | Ancillary corner joints. Used to join ancillary materials." |
| Clip | Ancillary clips and washers. Used to additionally fix and clip ancillaries together. |
| TieRod | Ancillary tie rod types. Used to internally stiffen fittings. |
| Gasket | Ancillary gaskets. Used to seal connector joints. |
| Sealant | Ancillary sealants. Used to seal seams. |
| SupportRod | Ancillary support drop rod types. Used to support fittings. |
| AncillaryMaterial | Ancillary materials used to support and externally stiffen fittings, eg. angle iron, unistrut. |
| AirturnTrack | Ancillary airturn tracks. Used to fasten airturn vanes in place. |
| AirturnVane | Ancillary airturn vanes. Used to manage flow through fittings. |
| Isolator | Ancillary support isolators. Used inline ancillary support rods. |
| SeamMaterial | Ancillary seam material. |

# See Also

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)

<!-- Start of Syntax__3f3368a4-d9ba-622e-9e21-3123d384df75.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VVDerivative Property

---



|  |
| --- |
| [FaceSecondDerivatives Class](6a876769-1607-4cfa-87d0-2b679e9da6e1.htm)   [See Also](#seeAlsoToggle) |

The second derivative with respect to V.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public XYZ VVDerivative { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property VVDerivative As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ VVDerivative { 	XYZ^ get (); } ``` |

# See Also

[FaceSecondDerivatives Class](6a876769-1607-4cfa-87d0-2b679e9da6e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f368fef-e0ac-1430-d409-1fa5136d1b8f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidPathForRailing Method

---



|  |
| --- |
| [Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)   [See Also](#seeAlsoToggle) |

Checks whether a railing can be created along a railing path.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static bool IsValidPathForRailing( 	CurveLoop curveLoop ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidPathForRailing ( _ 	curveLoop As CurveLoop _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidPathForRailing( 	CurveLoop^ curveLoop ) ``` |

#### Parameters

curveLoop
:   Type:  [Autodesk.Revit.DB CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     The railing path along which the new railing will be created.

#### Return Value

True if the new railing path can be used in a railing definition, False otherwise.

# Remarks

The railing path should be located on the same horizontal plane and it should contain lines or arcs only. It also has to be continuous and its three or more curves cannot meet in one end point.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__3f3b608e-52cb-1f81-fdf1-0965e021bc3f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElemCutType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Type"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SteelElemCutType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElemCutType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SteelElemCutType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f3b60cb-d029-2eb5-b4dd-51795c2a0380.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CutLineDistance Property

---



|  |
| --- |
| [CutMarkType Class](6f2d8dc7-6a19-fba3-00ae-a88cfe0e3d34.htm)   [See Also](#seeAlsoToggle) |

The distance between 2 cut lines.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double CutLineDistance { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CutLineDistance As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double CutLineDistance { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for distanceBetweenTwoLines must be greater than 0 and no more than 30000 feet. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The cut mark type is not a double cut line type. |

# See Also

[CutMarkType Class](6f2d8dc7-6a19-fba3-00ae-a88cfe0e3d34.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__3f3c93a6-008b-f9de-40d4-5cd99bb32b34.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InvalidPathArgumentException Class

---



|  |
| --- |
| [Members](2b5d011c-a210-ad08-0ab4-9b17b79f5b88.htm)   [See Also](#seeAlsoToggle) |

The exception that is thrown when a method received a pathname as an argument, but the pathname is illegal: too long, invalid characters, etc.

**Namespace:**   [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` [SerializableAttribute] public class InvalidPathArgumentException : ArgumentException ``` |

 

| Visual Basic |
| --- |
| ``` <SerializableAttribute> _ Public Class InvalidPathArgumentException _ 	Inherits ArgumentException ``` |

 

| Visual C++ |
| --- |
| ``` [SerializableAttribute] public ref class InvalidPathArgumentException : public ArgumentException ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)    
  [Autodesk.Revit.Exceptions ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.htm)    
  [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm)    
  Autodesk.Revit.Exceptions InvalidPathArgumentException

# See Also

[InvalidPathArgumentException Members](2b5d011c-a210-ad08-0ab4-9b17b79f5b88.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__3f40b842-1ea9-534a-7e77-b47dc589bb3a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Parameter Property

---



|  |
| --- |
| [ParameterValueProvider Class](5978eb2a-4598-f458-1504-80caff09cf7c.htm)   [See Also](#seeAlsoToggle) |

The parameter used to provide a string, integer, double-precision, or ElementId value on request for a given element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElementId Parameter { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Parameter As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ Parameter { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ParameterValueProvider Class](5978eb2a-4598-f458-1504-80caff09cf7c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f44845c-9603-0c28-99d4-e247e6622361.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [FabricationRodInfo Class](b52fe314-2639-a697-cf97-b3e4824818f8.htm)   [See Also](#seeAlsoToggle) |

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

[FabricationRodInfo Class](b52fe314-2639-a697-cf97-b3e4824818f8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f476c8b-ad47-fe69-945c-e94eebfbf5b1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WPerMSup2 Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol W/mÂ², indicating unit Watts per square meter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId WPerMSup2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WPerMSup2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ WPerMSup2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f4d00a8-9044-0f08-9cfe-813bfb7226ff.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEmpty Property

---



|  |
| --- |
| [EdgeArray Class](7069d0a1-fc52-a347-e0d8-6de1f40797d3.htm)   [See Also](#seeAlsoToggle) |

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

[EdgeArray Class](7069d0a1-fc52-a347-e0d8-6de1f40797d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f54c34f-76bb-be21-1ef6-bb83aebbbed9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarSystemHookOrientBackDirn1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Interior Major Hook Orientation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarSystemHookOrientBackDirn1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarSystemHookOrientBackDirn1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarSystemHookOrientBackDirn1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f5916f1-0f50-e16e-fa3a-6044d5877e38.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotMoveHostedFixtureViaCopyMonitor Property

---



|  |
| --- |
| [BuiltInFailures CopyMonitorFailures Class](a895e19b-bfd3-d5d3-9aae-3abda79ea902.htm)   [See Also](#seeAlsoToggle) |

The fixture is hosted and cannot be moved. Use the Move command to relocate the fixture in the host file as required.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotMoveHostedFixtureViaCopyMonitor { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotMoveHostedFixtureViaCopyMonitor As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotMoveHostedFixtureViaCopyMonitor { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyMonitorFailures Class](a895e19b-bfd3-d5d3-9aae-3abda79ea902.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f5a9937-e709-3b5e-21dd-05d1376b3da6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewInAModelMustBeUnique Property

---



|  |
| --- |
| [BuiltInFailures ViewSheetFailures Class](4488ecc8-243f-b6b5-ff98-ad780cd0bdc2.htm)   [See Also](#seeAlsoToggle) |

Sheet views in this model cannot contain more than one instance of "%1!s!."

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ViewInAModelMustBeUnique { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewInAModelMustBeUnique As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ViewInAModelMustBeUnique { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ViewSheetFailures Class](4488ecc8-243f-b6b5-ff98-ad780cd0bdc2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f622a7f-5416-1e03-45a8-ce7647f89757.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMassZoneIds Method

---



|  |
| --- |
| [MassGBXMLExportOptions Class](ac0f3089-3aa2-7dbd-511f-07c4a491df19.htm)   [See Also](#seeAlsoToggle) |

Gets a list of mass zones to analyze in the exported gbXML.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> GetMassZoneIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMassZoneIds As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ GetMassZoneIds() ``` |

#### Return Value

The ids of the mass zone.

# See Also

[MassGBXMLExportOptions Class](ac0f3089-3aa2-7dbd-511f-07c4a491df19.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3f63bfcc-a969-159f-93e7-377c49abcdd5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewId Property

---



|  |
| --- |
| [ViewExportedEventArgs Class](d0e95c70-c5f4-8b12-2f7a-5279ba667948.htm)   [See Also](#seeAlsoToggle) |

Identifies the view that was exported.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

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

[ViewExportedEventArgs Class](d0e95c70-c5f4-8b12-2f7a-5279ba667948.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__3f641f9d-169e-0f98-4554-00194b342a27.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FittingMustBeOnPipe Property

---



|  |
| --- |
| [BuiltInFailures ConnectorFailures Class](6a9d497c-6923-0689-e0bd-2cd00fb792f8.htm)   [See Also](#seeAlsoToggle) |

The [Tap] must be attached to pipe.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FittingMustBeOnPipe { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FittingMustBeOnPipe As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FittingMustBeOnPipe { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ConnectorFailures Class](6a9d497c-6923-0689-e0bd-2cd00fb792f8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f64e765-9531-c198-debe-71dee8b82ee7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidConditionIndex Method

---



|  |
| --- |
| [FabricationServiceButton Class](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)   [See Also](#seeAlsoToggle) |

Validates if the given condition index is valid or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static bool IsValidConditionIndex( 	FabricationServiceButton button, 	int condition ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidConditionIndex ( _ 	button As FabricationServiceButton, _ 	condition As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidConditionIndex( 	FabricationServiceButton^ button,  	int condition ) ``` |

#### Parameters

button
:   Type:  [Autodesk.Revit.DB FabricationServiceButton](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)    
     The button to check.

condition
:   Type:  System Int32    
     The condition index.

#### Return Value

True if larger or equal to 0 and less than ConditionCount.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationServiceButton Class](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f68c97f-3116-44e7-cea8-da9bf5d299e8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CommonTintColor Property

---



|  |
| --- |
| [Concrete Class](a3b65010-dc9e-f2ee-46ed-97e453198a62.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Tint Color" from the "Concrete" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string CommonTintColor { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CommonTintColor As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ CommonTintColor { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDoubleArray4d".

# See Also

[Concrete Class](a3b65010-dc9e-f2ee-46ed-97e453198a62.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3f69a061-eb08-85fb-7652-de4477dd43f5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TagTag Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Label"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TagTag { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TagTag As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TagTag { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f6c39b5-2ca1-75be-6b03-0ab8d1a56e2e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DataDictionaryDifferentInLink Property

---



|  |
| --- |
| [BuiltInFailures LinkFailures Class](99f8c34f-60bc-2dc8-eb93-c8db7d276e53.htm)   [See Also](#seeAlsoToggle) |

Linked file [Name] was last saved in a previous version of Revit. Changes to it cannot be saved until it is upgraded.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DataDictionaryDifferentInLink { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DataDictionaryDifferentInLink As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DataDictionaryDifferentInLink { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures LinkFailures Class](99f8c34f-60bc-2dc8-eb93-c8db7d276e53.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f6c7f73-e558-3879-e580-5305f6cd1b96.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EqualityConstraintsUnsatisfiedWarn Property

---



|  |
| --- |
| [BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)   [See Also](#seeAlsoToggle) |

Equality constraints are not satisfied. The action either violates a locked constraint or tries to modify a sketch based object outside of the sketch mode.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId EqualityConstraintsUnsatisfiedWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property EqualityConstraintsUnsatisfiedWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ EqualityConstraintsUnsatisfiedWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f6d25f0-173a-f6d4-43e5-fc7d0e863ca4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Profile1OffsetX Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Horizontal Profile Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Profile1OffsetX { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Profile1OffsetX As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Profile1OffsetX { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f6d5b54-979e-fe9f-9a8d-c124fd15c411.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [FilteredElementIdIterator Class](dfd0acee-d626-d5b2-fa2a-f9fc4edb49e8.htm)   [See Also](#seeAlsoToggle) |

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

[FilteredElementIdIterator Class](dfd0acee-d626-d5b2-fa2a-f9fc4edb49e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f6f9b7f-9227-9be5-eaad-fd8e0ce803ea.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveEndReference Method

---



|  |
| --- |
| [StructuralFramingUtils Class](93d93c87-dfa2-12d5-dcb0-13d5cb0c0696.htm)   [See Also](#seeAlsoToggle) |

Resets the end reference of the structural framing element.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static void RemoveEndReference( 	FamilyInstance familyInstance, 	int end ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub RemoveEndReference ( _ 	familyInstance As FamilyInstance, _ 	end As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void RemoveEndReference( 	FamilyInstance^ familyInstance,  	int end ) ``` |

#### Parameters

familyInstance
:   Type:  [Autodesk.Revit.DB FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)    
     The FamilyInstance, which must be of a structural framing category, non-concrete and joined.

end
:   Type:  System Int32    
     The index of the end (0 for the start, 1 for the end).

# Remarks

The setback value will be changed as a result of the removal.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1. |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | The input familyInstance is not of a structural framing category or is concrete or is not joined at given end and cannot have an end reference set. |

# See Also

[StructuralFramingUtils Class](93d93c87-dfa2-12d5-dcb0-13d5cb0c0696.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3f703eb6-7eac-c80e-e693-ebcdd6b35bbe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointLoad Class

---



|  |
| --- |
| [Members](bc80259d-8acc-3f3b-ecb7-0997d38bd4d2.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

An object that represents a force/moment applied to a single point.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class PointLoad : LoadBase ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PointLoad _ 	Inherits LoadBase ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PointLoad : public LoadBase ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void Getinfo_PointLoad(PointLoad pointLoad)
{
    string message = "Point Load :";

    // Get the load case name
    message += "\nLoad case for load: " + pointLoad.LoadCaseName;

    //get the three dimensional force applied to the point load
    message += "\nForce: (" + pointLoad.ForceVector.X + ", " +
             pointLoad.ForceVector.Y + ", " + pointLoad.ForceVector.Z + ")";

    //get the three dimensional moment application to the point load
    message += "\nMoment: (" + pointLoad.MomentVector.X + ", " +
             pointLoad.MomentVector.Y + ", " + pointLoad.MomentVector.Z + ")";

    //get the three dimensional coordinates of point load
    message += "\nPoint load location: (" + pointLoad.Point.X + ", " +
             pointLoad.Point.Y + ", " + pointLoad.Point.Z + ")";

    TaskDialog.Show("Revit",message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub Getinfo_PointLoad(pointLoad As PointLoad)
    Dim message As String = "Point Load :"

    ' Get the load case name
    message += vbLf & "Load case for load: " & Convert.ToString(pointLoad.LoadCaseName)

    'get the three dimensional force applied to the point load
 message += vbLf & "Force: (" & Convert.ToString(pointLoad.ForceVector.X) & ", " & Convert.ToString(pointLoad.ForceVector.Y) & ", " & Convert.ToString(pointLoad.ForceVector.Z) & ")"

    'get the three dimensional moment application to the point load
 message += vbLf & "Moment: (" & Convert.ToString(pointLoad.MomentVector.X) & ", " & Convert.ToString(pointLoad.MomentVector.Y) & ", " & Convert.ToString(pointLoad.MomentVector.Z) & ")"

    'get the three dimensional coordinates of point load
    message += vbLf & "Point load location: (" & Convert.ToString(pointLoad.Point.X) & ", " & Convert.ToString(pointLoad.Point.Y) & ", " & Convert.ToString(pointLoad.Point.Z) & ")"

    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB.Structure LoadBase](4130f6dc-1963-2105-d85b-e08a7c34af8b.htm)    
  Autodesk.Revit.DB.Structure PointLoad

# See Also

[PointLoad Members](bc80259d-8acc-3f3b-ecb7-0997d38bd4d2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3f70774d-39db-827d-1571-ed5dfd5de9f1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetObjectData Method

---



|  |
| --- |
| [CentralModelException Class](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.htm)   [See Also](#seeAlsoToggle) |

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

[CentralModelException Class](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__3f727dcd-1fab-dd8f-1198-d276cd81d10f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewUV Method

---



|  |
| --- |
| [Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)   [See Also](#seeAlsoToggle) |

Creates a UV object at the origin.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public UV NewUV() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewUV As UV ``` |

 

| Visual C++ |
| --- |
| ``` public: UV^ NewUV() ``` |

# See Also

[Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)

[NewUV Overload](ab6441b9-8958-6e2d-d6dc-ca0b69a8ae01.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__3f73b205-4121-eb63-c6de-d31fd1c74be7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewFlexDuct Method (Connector, IList(XYZ), FlexDuctType)

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [See Also](#seeAlsoToggle) |

Adds a new flexible duct into the document, using a connector, point array and duct type.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FlexDuct NewFlexDuct( 	Connector connector, 	IList<XYZ> points, 	FlexDuctType ductType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewFlexDuct ( _ 	connector As Connector, _ 	points As IList(Of XYZ), _ 	ductType As FlexDuctType _ ) As FlexDuct ``` |

 

| Visual C++ |
| --- |
| ``` public: FlexDuct^ NewFlexDuct( 	Connector^ connector,  	IList<XYZ^>^ points,  	FlexDuctType^ ductType ) ``` |

#### Parameters

connector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The connector to be connected to the duct, including the end points.

points
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The point array indicating the path of the flexible duct.

ductType
:   Type:  [Autodesk.Revit.DB.Mechanical FlexDuctType](cd9a7d63-9b1b-921f-f3ec-b2ec862eb2f2.htm)    
     The type of the flexible duct.

#### Return Value

If creation was successful then a new flexible duct is returned, otherwise an exception with failure information will be thrown.

# Remarks

If the connector is a fitting or equipment connector of the correct domain, and if the connector's direction matches the direction of the flexible duct to be created, the connectors will be automatically connected. A transition fitting will be added at the connector(s) if necessary. If the connector's type, domain, does not match the one of the input connector, no connection will be established.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument connector or points is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the flexible duct cannot be created or regenerate fails. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the flexible duct type does not exist in the given document. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[NewFlexDuct Overload](cece46e1-c086-aa28-2a88-ff6dbdc3a700.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__3f751d4e-37f4-9977-31ce-31e35f201d96.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HvacTemperature Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Temperature, in discipline HVAC.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId HvacTemperature { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property HvacTemperature As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ HvacTemperature { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f764b90-19b0-8fbb-50ae-f38400a89676.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadNatureName Property

---



|  |
| --- |
| [LoadBase Class](4130f6dc-1963-2105-d85b-e08a7c34af8b.htm)   [See Also](#seeAlsoToggle) |

A string representing the nature of the load.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public string LoadNatureName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property LoadNatureName As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ LoadNatureName { 	String^ get (); } ``` |

# See Also

[LoadBase Class](4130f6dc-1963-2105-d85b-e08a7c34af8b.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3f77a7ca-54e8-28b5-e1e6-cee57afd13e6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMaximumIndentLevel Method

---



|  |
| --- |
| [FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)   [See Also](#seeAlsoToggle) |

Returns the maximum allowed indent level

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public int GetMaximumIndentLevel() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMaximumIndentLevel As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int GetMaximumIndentLevel() ``` |

# See Also

[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f7f5aca-0f49-8938-6c77-cd6326341593.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewFilterId Property

---



|  |
| --- |
| [FilterDialog Class](9d0df7ca-0a3d-12b3-26b7-d28752220f59.htm)   [See Also](#seeAlsoToggle) |

The ElementId of the new filter created. The value is populated after Show method is executed.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public ElementId NewFilterId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property NewFilterId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ NewFilterId { 	ElementId^ get (); } ``` |

# See Also

[FilterDialog Class](9d0df7ca-0a3d-12b3-26b7-d28752220f59.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3f87d115-6b71-9ffa-67f6-b274d46fd0f4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceResolutionOutOfRange Property

---



|  |
| --- |
| [BuiltInFailures EnergyAnalysisFailures Class](8b9bfa39-1c9b-5cb0-14f1-0f49e2f8828a.htm)   [See Also](#seeAlsoToggle) |

Pixel size is out of range.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SurfaceResolutionOutOfRange { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SurfaceResolutionOutOfRange As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SurfaceResolutionOutOfRange { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures EnergyAnalysisFailures Class](8b9bfa39-1c9b-5cb0-14f1-0f49e2f8828a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f8c2daf-6f77-1288-fa37-9eebd54cedb6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsPlaceholder Property

---



|  |
| --- |
| [Pipe Class](aa1b8294-c12d-ece0-00af-b17c1f1c9e03.htm)   [See Also](#seeAlsoToggle) |

Identifies if the pipe is a placeholder or not.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsPlaceholder { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsPlaceholder As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsPlaceholder { 	bool get (); } ``` |

# See Also

[Pipe Class](aa1b8294-c12d-ece0-00af-b17c1f1c9e03.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__3f8dc2b4-1c46-7438-66c8-799acef150fc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionCantileverHeight Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Cantilever Height"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralSectionCantileverHeight { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralSectionCantileverHeight As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralSectionCantileverHeight { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f952c67-35da-eec2-1ae5-01502b4563b9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TestPoint Method

---



|  |
| --- |
| [PointCloudFilter Class](ca6f916b-2eba-f8e5-8939-1c063330c886.htm)   [See Also](#seeAlsoToggle) |

Checks if a point is inside the volume of interest.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool TestPoint( 	CloudPoint point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function TestPoint ( _ 	point As CloudPoint _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool TestPoint( 	CloudPoint point ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB.PointClouds CloudPoint](c780514e-fc08-e055-bda4-c4fe455c13d3.htm)    
     The point to be tested.

#### Return Value

If true, the point is accepted, if false, the point is not accepted.

# See Also

[PointCloudFilter Class](ca6f916b-2eba-f8e5-8939-1c063330c886.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__3f990d29-c743-ab3f-0a30-3b0a9b1f14cf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Ceramic Class

---



|  |
| --- |
| [Members](505a09e2-d877-a267-176e-eca076c7bec7.htm)   [See Also](#seeAlsoToggle) |

A static class that provides access to the property names that appear in the Ceramic visual asset schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static class Ceramic ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class Ceramic ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Ceramic abstract sealed ``` |

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB.Visual Ceramic

# See Also

[Ceramic Members](505a09e2-d877-a267-176e-eca076c7bec7.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3f9b82ef-8ace-deab-d496-029bbe98d65d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FbxLightEfficacy Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Efficacy"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FbxLightEfficacy { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FbxLightEfficacy As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FbxLightEfficacy { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3f9fd4b7-147e-a342-e257-394c0ea41de8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDocumentTransmitted Method

---



|  |
| --- |
| [TransmissionData Class](d78d1e9c-1cee-1336-88d5-b605dacd077d.htm)   [See Also](#seeAlsoToggle) |

Determines whether the document at a given file location is transmitted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool IsDocumentTransmitted( 	ModelPath filePath ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsDocumentTransmitted ( _ 	filePath As ModelPath _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsDocumentTransmitted( 	ModelPath^ filePath ) ``` |

#### Parameters

filePath
:   Type:  [Autodesk.Revit.DB ModelPath](40a84c72-e4b8-72ac-2f71-3216c66a11b3.htm)    
     The path to the document whose transmitted state will be checked.

#### Return Value

True if the document is a transmitted file, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TransmissionData Class](d78d1e9c-1cee-1336-88d5-b605dacd077d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)